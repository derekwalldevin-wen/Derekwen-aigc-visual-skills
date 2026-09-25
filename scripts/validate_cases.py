#!/usr/bin/env python3
from datetime import date
from pathlib import Path
import json
import re
import sys
import yaml

from build_case_data import build_index, build_latest, build_stats, load_cases

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "data" / "cases"
INDEX_PATH = ROOT / "data" / "case-index.json"
STATS_PATH = ROOT / "data" / "stats.json"
LATEST_PATH = ROOT / "data" / "latest.json"
SKILLS_DIR = ROOT / "skills"

errors = []
ALLOWED_STATUS = {"experimental", "tested", "verified"}
ALLOWED_SOURCE = {"recovered-history", "current-daily"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
ALLOWED_ARTICLE = {"confirmed-final", "confirmed-draft", "partial", "not-found"}
ALLOWED_PROMPT = {"confirmed-final", "confirmed", "partial", "not-found"}
ALLOWED_ASSETS = {"confirmed", "candidates-found", "not-found"}
ALLOWED_TEMPLATE_STATUS = {"candidate", "proposed", "published"}
ALLOWED_PRECISION = {"exact", "month", "unknown"}
KEBAB = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
CASE_ID = re.compile(r"^dw-[a-z0-9]+(?:-[a-z0-9]+)*$")

def valid_date(value, precision):
    if value is None:
        return precision == "unknown"
    try:
        if precision == "exact":
            date.fromisoformat(value)
            return True
        if precision == "month":
            return bool(re.fullmatch(r"\d{4}-\d{2}", value))
        return False
    except (TypeError, ValueError):
        return False

cases = load_cases()
seen_ids = set()

for path, case in cases:
    if not isinstance(case, dict):
        errors.append(f"{path.name}: root must be a mapping")
        continue

    required = [
        "schema_version", "id", "title_zh", "title_en", "series", "category",
        "status", "source", "evidence", "published", "template", "skill",
        "assets_status", "rights_status"
    ]
    for key in required:
        if key not in case:
            errors.append(f"{path.name}: missing {key}")

    cid = case.get("id")
    if not isinstance(cid, str) or not CASE_ID.fullmatch(cid):
        errors.append(f"{path.name}: invalid id {cid!r}")
    elif path.name != f"{cid}.yaml":
        errors.append(f"{path.name}: filename must match id {cid!r}")
    elif cid in seen_ids:
        errors.append(f"{path.name}: duplicate id {cid}")
    else:
        seen_ids.add(cid)

    if case.get("schema_version") != "1.0.0":
        errors.append(f"{path.name}: schema_version must be 1.0.0")
    if case.get("status") not in ALLOWED_STATUS:
        errors.append(f"{path.name}: invalid status {case.get('status')!r}")

    cats = case.get("category")
    if not isinstance(cats, list) or not cats:
        errors.append(f"{path.name}: category must be a non-empty list")
    else:
        for cat in cats:
            if not isinstance(cat, str) or not KEBAB.fullmatch(cat):
                errors.append(f"{path.name}: invalid category {cat!r}")

    source = case.get("source") or {}
    if source.get("type") not in ALLOWED_SOURCE:
        errors.append(f"{path.name}: invalid source.type {source.get('type')!r}")
    precision = source.get("evidence_date_precision", "unknown")
    if precision not in ALLOWED_PRECISION:
        errors.append(f"{path.name}: invalid evidence_date_precision {precision!r}")
    elif not valid_date(source.get("evidence_date"), precision):
        errors.append(f"{path.name}: evidence_date does not match precision")
    original = source.get("original_date")
    if original is not None:
        try:
            date.fromisoformat(original)
        except (TypeError, ValueError):
            errors.append(f"{path.name}: original_date must be YYYY-MM-DD or null")

    evidence = case.get("evidence") or {}
    if evidence.get("confidence") not in ALLOWED_CONFIDENCE:
        errors.append(f"{path.name}: invalid evidence.confidence")
    if evidence.get("article") not in ALLOWED_ARTICLE:
        errors.append(f"{path.name}: invalid evidence.article")
    if evidence.get("prompt") not in ALLOWED_PROMPT:
        errors.append(f"{path.name}: invalid evidence.prompt")
    if evidence.get("assets") not in ALLOWED_ASSETS:
        errors.append(f"{path.name}: invalid evidence.assets")

    published = case.get("published") or {}
    if published.get("social") not in {None, True, False}:
        errors.append(f"{path.name}: published.social must be boolean or null")
    if not isinstance(published.get("github"), bool):
        errors.append(f"{path.name}: published.github must be boolean")

    template = case.get("template") or {}
    if not template.get("id"):
        errors.append(f"{path.name}: template.id required")
    if template.get("status") not in ALLOWED_TEMPLATE_STATUS:
        errors.append(f"{path.name}: invalid template.status")

    skill = case.get("skill") or {}
    skill_id = skill.get("id")
    if skill_id is not None and not (SKILLS_DIR / skill_id).is_dir():
        errors.append(f"{path.name}: linked skill does not exist: {skill_id}")

    if source.get("type") == "current-daily" and published.get("github"):
        assets = case.get("assets") or {}
        preview = assets.get("preview")
        if not preview:
            errors.append(f"{path.name}: current-daily GitHub publication requires assets.preview")
        elif not (ROOT / preview).is_file():
            errors.append(f"{path.name}: preview asset does not exist: {preview}")

        if original:
            slug = str(cid).removeprefix("dw-")
            year, month, _ = original.split("-")
            article = ROOT / "daily-words" / year / month / f"{slug}.md"
            if not article.is_file():
                errors.append(f"{path.name}: Daily Word article does not exist: {article.relative_to(ROOT)}")

expected_index = build_index(cases)
expected_stats = build_stats(expected_index)
expected_latest = build_latest(cases)

try:
    actual_index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
    if actual_index != expected_index:
        errors.append("data/case-index.json is stale; run python scripts/build_case_data.py")
except Exception as exc:
    errors.append(f"cannot read case-index.json: {exc}")

try:
    actual_stats = json.loads(STATS_PATH.read_text(encoding="utf-8"))
    if actual_stats != expected_stats:
        errors.append("data/stats.json is stale; run python scripts/build_case_data.py")
except Exception as exc:
    errors.append(f"cannot read stats.json: {exc}")

try:
    actual_latest = json.loads(LATEST_PATH.read_text(encoding="utf-8"))
    if actual_latest != expected_latest:
        errors.append("data/latest.json is stale; run python scripts/build_case_data.py")
except Exception as exc:
    errors.append(f"cannot read latest.json: {exc}")

if errors:
    print("CASE VALIDATION FAILED")
    for error in errors:
        print(" -", error)
    sys.exit(1)

print(f"Validated {len(cases)} Cases against schema v1.0")
print(f" - verified: {expected_stats['totals']['status']['verified']}")
print(f" - tested: {expected_stats['totals']['status']['tested']}")
print(f" - experimental: {expected_stats['totals']['status']['experimental']}")
print(f" - published templates: {expected_stats['totals']['templates']['published']}")
print(f" - proposed template refs: {expected_stats['totals']['templates']['proposed_refs']}")
print(f" - latest Daily Words: {expected_latest['count']} on {expected_latest['latest_date']}")
