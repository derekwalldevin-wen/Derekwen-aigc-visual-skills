# Contributing

Thanks for helping improve DerekWen AIGC Visual Skills.

## What makes a useful contribution

- A reproducible failure case with the input type and expected behavior.
- A change that improves identity, composition, material, lighting, layout, or tool-execution stability.
- A new skill derived from a repeatable visual workflow rather than a one-off prompt.
- Compatibility notes for image or video generation systems.

## Skill requirements

Every skill should:

1. live in `skills/<slug>/SKILL.md`;
2. include YAML frontmatter with `name`, `description`, and metadata containing `author` and `version`;
3. use `author: 德里克文` for official collection skills;
4. define its default output artifact;
5. distinguish reference-image mode from text-only generation when relevant;
6. include quality checks and failure conditions;
7. avoid claiming tool actions that the runtime cannot perform.

## Visual assets

Do not commit an image unless you have permission to publish it. Example assets are not automatically covered by the repository's MIT license. See `ASSET-LICENSE.md`.