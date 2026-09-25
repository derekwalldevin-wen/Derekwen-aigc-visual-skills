#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
import json
import yaml

ROOT = Path(__file__).resolve().parents[1]
CASES_DIR = ROOT / "data" / "cases"
INDEX_PATH = ROOT / "data" / "case-index.json"
STATS_PATH = ROOT / "data" / "stats.json"
LATEST_PATH = ROOT / "data" / "latest.json"

def load_cases():
    cases = []
    for path in sorted(CASES_DIR.glob("*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        cases.append((path, data))
    return cases

def build_index(cases):
    rows = []
    for _, case in cases:
        template = case.get("template") or {}
        skill = case.get("skill") or {}
        source = case.get("source") or {}
        evidence = case.get("evidence") or {}
        published = case.get("published") or {}
        rows.append({
            "id": case["id"],
            "title_zh": case["title_zh"],
            "title_en": case["title_en"],
            "status": case["status"],
            "category": case["category"],
            "template": template.get("id"),
            "template_status": template.get("status"),
            "skill": skill.get("id"),
            "skill_candidate": skill.get("candidate"),
            "source_type": source.get("type"),
            "original_date": source.get("original_date"),
            "evidence_date": source.get("evidence_date"),
            "evidence_date_precision": source.get("evidence_date_precision", "unknown"),
            "evidence_confidence": evidence.get("confidence"),
            "assets_status": case.get("assets_status"),
            "rights_status": case.get("rights_status"),
            "github_published": bool(published.get("github", False)),
        })
    return sorted(rows, key=lambda row: row["id"])

def build_stats(index):
    statuses = Counter(row["status"] for row in index)
    categories = Counter(cat for row in index for cat in row["category"])
    rights = Counter(row["rights_status"] for row in index)
    confidence = Counter(row["evidence_confidence"] for row in index)
    source_types = Counter(row["source_type"] for row in index)
    date_precision = Counter(row["evidence_date_precision"] for row in index)
    template_refs = {row["template"] for row in index if row["template"]}
    published_templates = {
        row["template"] for row in index
        if row["template"] and row["template_status"] == "published"
    }
    return {
        "schema_version": "1.0.0",
        "collection": "DerekWen AIGC Visual Library",
        "source": "data/cases/*.yaml",
        "totals": {
            "cases": len(index),
            "status": {
                "verified": statuses.get("verified", 0),
                "tested": statuses.get("tested", 0),
                "experimental": statuses.get("experimental", 0),
            },
            "linked_skills": sum(bool(row["skill"]) for row in index),
            "skill_candidates": sum(bool(row["skill_candidate"]) for row in index),
            "templates": {
                "published": len(published_templates),
                "proposed_refs": len(template_refs),
            },
            "source_types": dict(sorted(source_types.items())),
            "evidence_confidence": {
                "high": confidence.get("high", 0),
                "medium": confidence.get("medium", 0),
                "low": confidence.get("low", 0),
            },
            "dates": {
                "original_known": sum(bool(row["original_date"]) for row in index),
                "evidence_precision": {
                    "exact": date_precision.get("exact", 0),
                    "month": date_precision.get("month", 0),
                    "unknown": date_precision.get("unknown", 0),
                },
            },
        },
        "categories": dict(sorted(categories.items())),
        "rights": dict(sorted(rights.items())),
        "asset_policy": {
            "default": "historical-first",
            "note": "Reuse previously generated assets before creating new images. Regenerate only when historical assets cannot be recovered, published, or meet quality requirements.",
        },
    }

def build_latest(cases):
    published = []
    for _, case in cases:
        source = case.get("source") or {}
        publication = case.get("published") or {}
        if source.get("type") != "current-daily" or not publication.get("github"):
            continue

        original_date = source.get("original_date")
        if not original_date:
            continue

        slug = case["id"].removeprefix("dw-")
        year, month, _ = original_date.split("-")
        assets = case.get("assets") or {}
        published.append({
            "id": case["id"],
            "title_zh": case["title_zh"],
            "title_en": case["title_en"],
            "date": original_date,
            "status": case["status"],
            "article": f"daily-words/{year}/{month}/{slug}.md",
            "preview": assets.get("preview"),
            "rights_status": case.get("rights_status"),
        })

    if not published:
        return {
            "schema_version": "1.0.0",
            "collection": "DerekWen AIGC Visual Library",
            "latest_date": None,
            "count": 0,
            "cases": [],
        }

    latest_date = max(row["date"] for row in published)
    latest_cases = sorted(
        (row for row in published if row["date"] == latest_date),
        key=lambda row: row["id"],
    )
    return {
        "schema_version": "1.0.0",
        "collection": "DerekWen AIGC Visual Library",
        "latest_date": latest_date,
        "count": len(latest_cases),
        "cases": latest_cases,
    }

def dump(index, stats, latest):
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    STATS_PATH.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    LATEST_PATH.write_text(json.dumps(latest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

if __name__ == "__main__":
    cases = load_cases()
    index = build_index(cases)
    stats = build_stats(index)
    latest = build_latest(cases)
    dump(index, stats, latest)
    print(f"Built {len(index)} Case records")
    print(f"Latest Daily Words: {latest['count']} on {latest['latest_date']}")
