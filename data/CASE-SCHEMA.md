# Case Schema v1.0

This directory is the canonical data layer for **DerekWen AIGC Visual Library**.

## Core rule

A Case records a visual method or Daily Word. It is not automatically a Template or a Skill.

`Daily Word → Case → Template → Skill`

## Required fields

- `schema_version`: currently `1.0.0`
- `id`: permanent semantic ID, beginning with `dw-`
- `title_zh` / `title_en`
- `series`: normally `AI绘画每日一词`
- `category`: one or more kebab-case categories
- `status`: method maturity only
- `source`: where the historical/current record came from
- `evidence`: how much supporting material has been recovered
- `published`: publication state
- `template`: related Template reference and its state
- `skill`: linked Skill or Skill candidate
- `assets_status`
- `rights_status`

## Status

Only these values are valid:

- `experimental` — concept or method exists, but reliable execution evidence is incomplete
- `tested` — the method has been run in practice
- `verified` — the method has been reviewed and confirmed reusable

Do not use `drafted` or `recovered` as a method status. Those concepts belong under `evidence` and `source`.

## Source and dates

Recovered historical records use:

```yaml
source:
  type: recovered-history
  original_date: null
  evidence_date: "2026-09-16"
  evidence_date_precision: exact
```

`original_date` is reserved for a directly supported original/publication date. A chat timestamp, file creation date, or later recovery date must not be silently promoted to `original_date`.

`evidence_date` preserves the best historical date evidence already known. A missing date must use `evidence_date: null` with `evidence_date_precision: unknown`; `exact` and `month` require a real date value.

## Evidence

```yaml
evidence:
  confidence: high
  article: partial
  prompt: partial
  assets: candidates-found
```

Allowed values:

- confidence: `high | medium | low`
- article: `confirmed-final | confirmed-draft | partial | not-found`
- prompt: `confirmed-final | confirmed | partial | not-found`
- assets: `confirmed | candidates-found | not-found`

## Current Daily Word publication contract

A `current-daily` Case with `published.github: true` must have:

- a supported `source.original_date`
- a real Daily Word page at `daily-words/YYYY/MM/<slug>.md`
- an `assets.preview` path that exists in the repository
- a reviewed `rights_status`

The validator checks the article and preview paths. Do not publish placeholder assets.

## Templates

A Case may reference a proposed Template, but that does **not** mean the Template already exists.

Public statistics must distinguish:

- published Templates
- proposed Template references

A proposed reference must never be displayed as a published Template count.

## Missing data

Use `null`, `pending`, or an explicit evidence state. Do not invent dates, models, prompt text, assets, or rights clearance.

## Generated files

`data/case-index.json`, `data/stats.json`, and `data/latest.json` are generated from Case YAML files by:

```bash
python scripts/build_case_data.py
```

- `case-index.json` — canonical Case index
- `stats.json` — aggregate counts and category / rights statistics
- `latest.json` — latest GitHub-published `current-daily` entries for homepage, gallery, or external consumers

Validation:

```bash
python scripts/validate_cases.py
```
