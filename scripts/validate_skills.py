#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
EXAMPLES = ROOT / "examples"
MANIFEST = ROOT / "skills.json"
EXPECTED_COUNT = 10
VIDEO_SKILL = "premium-product-launch-film"

errors = []
validated = []

if not MANIFEST.exists():
    errors.append("missing skills.json")
    manifest = {"skills": []}
else:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))

manifest_ids = {x["id"] for x in manifest.get("skills", [])}
disk_ids = {p.name for p in SKILLS.iterdir() if p.is_dir()} if SKILLS.exists() else set()

if len(manifest_ids) != EXPECTED_COUNT:
    errors.append(f"expected {EXPECTED_COUNT} manifest skills, got {len(manifest_ids)}")
if manifest_ids != disk_ids:
    errors.append(f"manifest/folder mismatch: manifest={sorted(manifest_ids)} disk={sorted(disk_ids)}")
if manifest.get("version") != "1.1.0":
    errors.append(f"collection version must be 1.1.0, got {manifest.get('version')!r}")

for folder in sorted(SKILLS.iterdir()) if SKILLS.exists() else []:
    if not folder.is_dir():
        continue
    skill = folder / "SKILL.md"
    readme = folder / "README.md"
    if not skill.exists():
        errors.append(f"{folder.name}: missing SKILL.md")
        continue
    if not readme.exists():
        errors.append(f"{folder.name}: missing README.md")

    text = skill.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        errors.append(f"{folder.name}: missing YAML front matter")
        continue

    def grab(field):
        m = re.search(rf"(?m)^\s*{re.escape(field)}:\s*[\"']?([^\n\"']+)", text)
        return m.group(1).strip() if m else None

    name = grab("name")
    author = grab("author")
    version = grab("version")

    if name != folder.name:
        errors.append(f"{folder.name}: front-matter name={name!r}")
    if author != "德里克文":
        errors.append(f"{folder.name}: author must be 德里克文, got {author!r}")
    if not version:
        errors.append(f"{folder.name}: missing version")
    if len(text) < 1000:
        errors.append(f"{folder.name}: SKILL.md unexpectedly short")

    ex = EXAMPLES / folder.name
    if not ex.exists():
        errors.append(f"{folder.name}: missing examples directory")
    else:
        if not (ex / "README.md").exists():
            errors.append(f"{folder.name}: missing example README.md")
        if not (ex / "before.svg").exists():
            errors.append(f"{folder.name}: missing before.svg")
        if folder.name == VIDEO_SKILL:
            if not (ex / "preview-frame.svg").exists():
                errors.append(f"{folder.name}: missing preview-frame.svg")
        else:
            if not (ex / "after.svg").exists():
                errors.append(f"{folder.name}: missing after.svg")
    validated.append((folder.name, version))

for readme_path in [ROOT / "README.md", ROOT / "README.zh.md"]:
    if not readme_path.exists():
        errors.append(f"missing {readme_path.name}")
    elif "Visual Case Wall" not in readme_path.read_text(encoding="utf-8"):
        errors.append(f"{readme_path.name}: missing Visual Case Wall reference")

for readme_path in [ROOT / "README.md", ROOT / "README.zh.md"]:
    if readme_path.exists():
        text = readme_path.read_text(encoding="utf-8")
        refs = re.findall(r'(?:src="|!\[[^\]]*\]\()([^")]+\.(?:jpg|jpeg|png|webp|svg))', text, flags=re.I)
        for ref in refs:
            if ref.startswith("http"):
                continue
            target = (readme_path.parent / ref).resolve()
            if not target.exists():
                errors.append(f"{readme_path.name}: missing image target {ref}")

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(f"Validated {len(validated)} skills and examples")
for name, version in validated:
    print(f" - {name} {version}")
