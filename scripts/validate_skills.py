#!/usr/bin/env python3
"""Validate Skill metadata, raster examples, and README image references."""
from pathlib import Path
import json
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
VIDEO_SKILL = "premium-product-launch-film"
RASTER = {".png", ".jpg", ".jpeg", ".webp"}
NOTICE = "Preview shown here is a representative generated frame, not the final video file."
FEATURED = {"day-night-dual-poster", "geometric-flat-twin-poster",
            "shadow-theater-twin-poster", "character-sheet-board"}


def image_refs(text):
    refs = re.findall(r'<img\b[^>]*\bsrc\s*=\s*[\"\']([^\"\']+)', text, re.I)
    refs += re.findall(r'!\[[^\]]*\]\(\s*<?([^\s)>]+)', text)
    definitions = {key.casefold(): value for key, value in re.findall(
        r'^\s*\[([^\]]+)\]:\s*<?([^\s>]+)', text, re.M)}
    for alt, label in re.findall(r'!\[([^\]]*)\](?:\[([^\]]*)\])?(?!\()', text):
        ref = definitions.get((label or alt).casefold())
        if ref:
            refs.append(ref)
    return refs


def raster_files(folder, stem):
    return [p for p in folder.glob(stem + ".*") if p.is_file() and p.suffix.lower() in RASTER]


def check_raster(path):
    with path.open("rb") as stream:
        header = stream.read(32)
    if path.suffix.lower() == ".png":
        return header.startswith(b"\x89PNG\r\n\x1a\n") and header[12:16] == b"IHDR"
    if path.suffix.lower() in {".jpg", ".jpeg"}:
        return header.startswith(b"\xff\xd8\xff")
    return header[:4] == b"RIFF" and header[8:12] == b"WEBP"


def validate(root=ROOT):
    root = Path(root).resolve()
    skills, examples = root / "skills", root / "examples"
    errors, warnings, validated = [], [], []
    try:
        manifest = json.loads((root / "skills.json").read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        return [f"cannot read skills.json: {exc}"], warnings, validated
    entries = manifest.get("skills", [])
    if not isinstance(entries, list) or not all(isinstance(x, dict) and isinstance(x.get("id"), str) for x in entries):
        return ["skills.json: invalid skill entries"], warnings, validated
    ids = {entry["id"] for entry in entries}
    if len(entries) != 10 or len(ids) != 10:
        errors.append("expected exactly 10 unique manifest skills")
    for directory in (skills, examples):
        disk = {p.name for p in directory.iterdir() if p.is_dir()} if directory.exists() else set()
        if disk != ids:
            errors.append(f"manifest/{directory.name} mismatch: manifest={sorted(ids)} disk={sorted(disk)}")
    if manifest.get("version") != "1.1.0":
        errors.append("collection version must be 1.1.0")
    if manifest.get("author") != "德里克文":
        errors.append("manifest author must be 德里克文")
    for entry in entries:
        sid = entry["id"]
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", sid):
            errors.append(f"invalid skill id: {sid!r}")
            continue
        for key, expected in (("entry", f"skills/{sid}/SKILL.md"), ("example", f"examples/{sid}/README.md")):
            if entry.get(key) != expected:
                errors.append(f"{sid}: manifest {key} must be {expected}")
        if "author" in entry and entry["author"] != "德里克文":
            errors.append(f"{sid}: manifest author must be 德里克文")
        if entry.get("output") != ("video" if sid == VIDEO_SKILL else "image"):
            errors.append(f"{sid}: incorrect manifest output type")
        skill = skills / sid / "SKILL.md"
        if not skill.is_file():
            errors.append(f"{sid}: missing SKILL.md")
            continue
        text = skill.read_text(encoding="utf-8")
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not front:
            errors.append(f"{sid}: missing YAML front matter")
            continue
        def grab(field):
            match = re.search(rf"(?m)^\s*{field}:\s*[\"']?([^\n\"']+)", front.group(1))
            return match.group(1).strip() if match else None
        if grab("name") != sid:
            errors.append(f"{sid}: front-matter name mismatch")
        if grab("author") != "德里克文":
            errors.append(f"{sid}: author must be 德里克文")
        if not grab("version"):
            errors.append(f"{sid}: missing version")
        if len(text) < 1000:
            errors.append(f"{sid}: SKILL.md unexpectedly short")
        ex = examples / sid
        stem = "preview-frame" if sid == VIDEO_SKILL else "after"
        outputs = raster_files(ex, stem)
        if not outputs:
            errors.append(f"{sid}: missing {stem}.png / jpg / webp")
        if not raster_files(ex, "before"):
            warnings.append(f"{sid}: before raster recommended; any references must resolve")
        if sid == VIDEO_SKILL and list(ex.glob("after.*")):
            errors.append(f"{sid}: use preview-frame, not after")
        for page in (skills / sid / "README.md", ex / "README.md"):
            if not page.is_file():
                errors.append(f"{page.relative_to(root)}: missing README.md")
                continue
            content = page.read_text(encoding="utf-8")
            linked = {(page.parent / unquote(urlsplit(ref).path)).resolve()
                      for ref in image_refs(content) if not urlsplit(ref).scheme}
            if outputs and not any(output.resolve() in linked for output in outputs):
                errors.append(f"{page.relative_to(root)}: missing {stem} image reference")
            if sid == VIDEO_SKILL:
                if "Video Preview" not in content:
                    errors.append(f"{page.relative_to(root)}: must use Video Preview terminology")
                if NOTICE not in content:
                    errors.append(f"{page.relative_to(root)}: missing generated-frame disclaimer")
                section = content.split("## Example", 1)[-1].split("## Use", 1)[0]
                if re.search(r"final\s+video|最终视频|最终成片", section.replace(NOTICE, ""), re.I):
                    errors.append(f"{page.relative_to(root)}: static preview must not be labeled final video")
        validated.append((sid, grab("version")))
    for path in examples.rglob("*"):
        if path.is_file() and path.suffix.lower() == ".svg":
            errors.append(f"{path.relative_to(root)}: SVG example assets are prohibited")
        elif path.is_file() and path.suffix.lower() in RASTER and not check_raster(path):
            errors.append(f"{path.relative_to(root)}: file bytes do not match raster extension")
    readmes = [root / "README.md", root / "README.zh.md"]
    readmes += sorted(skills.glob("*/README.md")) + sorted(examples.rglob("README.md"))
    for page in readmes:
        if not page.is_file():
            errors.append(f"{page.relative_to(root)}: missing README")
            continue
        content = page.read_text(encoding="utf-8")
        for ref in image_refs(content):
            parsed = urlsplit(ref)
            ref_path = unquote(parsed.path)
            if re.search(r"(?:^|/)examples/.*\.svg$", ref_path, re.I):
                errors.append(f"{page.relative_to(root)}: forbidden example SVG reference {ref}")
            if parsed.scheme or parsed.netloc:
                continue
            target = (page.parent / ref_path).resolve()
            if not target.is_relative_to(root):
                errors.append(f"{page.relative_to(root)}: image target escapes repository: {ref}")
            elif not target.is_file():
                errors.append(f"{page.relative_to(root)}: missing image target {ref}")
            elif target.is_relative_to(examples) and target.suffix.lower() not in RASTER:
                errors.append(f"{page.relative_to(root)}: example image must be PNG/JPG/WEBP: {ref}")
        if re.search(r"(?:examples/[^\s)\"'<>]+|(?:\./)?(?:before|after|preview-frame))\.svg\b", content, re.I):
            errors.append(f"{page.relative_to(root)}: contains obsolete example SVG reference")
        if page.parent == root:
            sections = (
                ("Visual Case Wall", {f"examples/{sid}/{'preview-frame' if sid == VIDEO_SKILL else 'after'}" for sid in ids}),
                ("Before / After", {f"examples/{sid}/{stem}" for sid in FEATURED for stem in ("before", "after")}),
            )
            for heading, expected in sections:
                match = re.search(rf"^## [^\n]*{re.escape(heading)}[^\n]*\n(.*?)(?=^## |\Z)", content, re.M | re.S)
                refs = image_refs(match.group(1)) if match else []
                actual = {Path(urlsplit(ref).path.removeprefix('./')).with_suffix('').as_posix() for ref in refs}
                if len(refs) != len(expected) or actual != expected:
                    errors.append(f"{page.name}: {heading} must display the exact required raster cases")
    return errors, warnings, validated


if __name__ == "__main__":
    errors, warnings, validated = validate()
    for warning in warnings:
        print("WARNING:", warning)
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(" -", error)
        sys.exit(1)
    print(f"Validated {len(validated)} skills and raster examples")
    for name, version in validated:
        print(f" - {name} {version}")
