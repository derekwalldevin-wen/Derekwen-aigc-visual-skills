<div align="center">

[中文](./README.zh.md) · **English**

# DerekWen AIGC Visual Skills

**Open-source visual-generation skills for image transformation, editorial posters, character systems, explainers, and premium product films.**

![Skills](https://img.shields.io/badge/SKILLS-10-2ea44f?style=flat-square&labelColor=333)
![Version](https://img.shields.io/badge/COLLECTION-1.0.0-214f9b?style=flat-square&labelColor=333)
![License](https://img.shields.io/badge/LICENSE-MIT-e37f2c?style=flat-square&labelColor=333)
![Author](https://img.shields.io/badge/AUTHOR-%E5%BE%B7%E9%87%8C%E5%85%8B%E6%96%87-7d4cdb?style=flat-square&labelColor=333)

</div>

A growing collection of production-oriented `SKILL.md` workflows created by **德里克文** from the long-running **AI绘画每日一词** practice.

These skills are not just prompt snippets. Each one encodes a repeatable workflow: input routing, composition logic, identity preservation, tool-execution rules, failure conditions, and quality checks.

## Skills

| Skill | What it does | Default output |
|---|---|---|
| [Day / Night Twin Poster](./skills/day-night-dual-poster/) | Same subject and composition, two time states, physically separated comparison layout | Image |
| [Geometric Flat Twin Poster](./skills/geometric-flat-twin-poster/) | Photo + modernist geometric flat reinterpretation | Image |
| [Quirky Hand-drawn Twin Poster](./skills/quirky-handdrawn-twin-poster/) | Photo + personality-driven colored-pencil / crayon hand-drawn reinterpretation | Image |
| [Etched Concept Twin Poster](./skills/etched-concept-twin-poster/) | Photo + black-and-white engraving reinterpretation with restrained conceptual reinforcement | Image |
| [Then / Now Film Twin Poster](./skills/then-now-film-twin-poster/) | Recreates the same moment as contemporary photography and a believable circa-1985 35mm photograph | Image |
| [Character Sheet Board](./skills/character-sheet-board/) | Locks a character's identity, turnarounds, palette, expressions, poses, costume details, and hands | Image |
| [Materialized Explainer](./skills/materialized-explainer/) | Turns flows, layers, cycles, comparisons, networks, and other concepts into tactile studio-shot models | Image |
| [Memory Tile Portrait Poster](./skills/memory-tile-portrait-poster/) | One continuous portrait tiled with a small number of real memory photographs | Image |
| [Shadow Theater Twin Poster](./skills/shadow-theater-twin-poster/) | Keeps the real subject unchanged while transforming only the physically plausible cast shadow | Image |
| [Premium Product Launch Film](./skills/premium-product-launch-film/) | Routes by product type and prioritizes single-invocation end-to-end premium launch-film generation | Video |

## Design principles

1. **Workflow over prompt fragments.** Each skill includes routing, constraints, execution, and quality gates.
2. **Preserve identity.** Uploaded people, products, places, and characters remain recognizable unless the user explicitly asks otherwise.
3. **Choose the layout from the input.** Where appropriate, the skill evaluates aspect ratio, subject axis, crop loss, and visual hierarchy instead of blindly applying one template.
4. **Generate the requested artifact.** Image skills default to actual image generation when tools are available; the video skill defaults to an actual video, not a text prompt pretending to be a finished output.
5. **Fail explicitly.** Each skill defines common structural and visual failure modes so an agent can inspect and retry intelligently.

## Install

Clone the collection:

```bash
git clone https://github.com/derekwalldevin-wen/Derekwen-aigc-visual-skills.git
```

For agent environments that load skills from individual directories, copy the desired skill folder. Example for Claude Code:

```bash
cp -R Derekwen-aigc-visual-skills/skills/day-night-dual-poster ~/.claude/skills/
```

Restart the agent environment if required. Other environments can load the relevant `SKILL.md` as their skill entry point where supported.

## Try it

```text
Use day-night-dual-poster on this photo. Keep the person and camera framing unchanged; make the second state a believable night version.
```

```text
Use geometric-flat-twin-poster on this travel photo. Preserve the composition and turn the comparison panel into a modernist geometric flat illustration.
```

```text
Use shadow-theater-twin-poster. Keep me exactly as photographed, but make my cast shadow a firefighter.
```

```text
Use character-sheet-board with this character image and build a professional identity sheet with turnarounds, expressions, pose studies, costume details, and hands.
```

```text
Use materialized-explainer to visualize an AI Agent workflow: input → understanding → tool use → execution → validation → output.
```

## Repository layout

```text
derekwen-aigc-visual-skills/
├── .github/workflows/validate.yml
├── examples/README.md
├── scripts/validate_skills.py
├── skills/
│   ├── day-night-dual-poster/
│   ├── geometric-flat-twin-poster/
│   ├── quirky-handdrawn-twin-poster/
│   ├── etched-concept-twin-poster/
│   ├── then-now-film-twin-poster/
│   ├── character-sheet-board/
│   ├── materialized-explainer/
│   ├── memory-tile-portrait-poster/
│   ├── shadow-theater-twin-poster/
│   └── premium-product-launch-film/
├── skills.json
├── README.md
├── README.zh.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── ASSET-LICENSE.md
└── LICENSE
```

## Examples and visual assets

The skills are open source under MIT. Visual example files should only be committed when the uploader has the right to publish them. See [`ASSET-LICENSE.md`](./ASSET-LICENSE.md).

## License

The skill instructions, documentation, validation scripts, and repository source files are released under the [MIT License](./LICENSE).

Visual examples are handled separately; see [ASSET-LICENSE.md](./ASSET-LICENSE.md).

---

Created by **德里克文** · GitHub: [@derekwalldevin-wen](https://github.com/derekwalldevin-wen) · X: [@derek_wall90176](https://x.com/derek_wall90176)