#!/usr/bin/env python3
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
MANIFEST = ROOT / "skills.json"

errors = []
validated = []

if not MANIFEST.exists():
    errors.append("missing skills.json")
else:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest_ids = {x["id"] for x in manifest.get("skills", [])}
    disk_ids = {p.name for p in SKILLS.iterdir() if p.is_dir()} if SKILLS.exists() else set()
    if manifest_ids != disk_ids:
        errors.append(f"manifest/folder mismatch: manifest={sorted(manifest_ids)} disk={sorted(disk_ids)}")

for folder in sorted(SKILLS.iterdir()) if SKILLS.exists() else []:
    if not folder.is_dir():
        continue
    skill = folder / "SKILL.md"
    if not skill.exists():
        errors.append(f"{folder.name}: missing SKILL.md")
        continue
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
    validated.append((folder.name, version))

if errors:
    print("VALIDATION FAILED")
    for e in errors:
        print(" -", e)
    sys.exit(1)

print(f"Validated {len(validated)} skills")
for name, version in validated:
    print(f" - {name} {version}")
