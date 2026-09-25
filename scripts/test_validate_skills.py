"""Regression tests for repository validation; fixture rasters are test data only."""
import base64
import json
from pathlib import Path
import shutil
import tempfile
import unittest

from validate_skills import FEATURED, NOTICE, ROOT, VIDEO_SKILL, validate

PNG = base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+/l9sAAAAASUVORK5CYII=')


class ValidateSkillsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.manifest = json.loads((ROOT / 'skills.json').read_text(encoding='utf-8'))
        self.write('skills.json', json.dumps(self.manifest, ensure_ascii=False))
        wall, featured = [], []
        for entry in self.manifest['skills']:
            sid = entry['id']
            stem = 'preview-frame' if sid == VIDEO_SKILL else 'after'
            self.write(f'skills/{sid}/SKILL.md', (ROOT / entry['entry']).read_text(encoding='utf-8'))
            for name in ('before', stem):
                path = self.root / 'examples' / sid / f'{name}.png'
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(PNG)
            for parent, prefix in ((f'skills/{sid}', f'../../examples/{sid}/'), (f'examples/{sid}', './')):
                content = f'## Example\n\n![Before]({prefix}before.png)\n![After]({prefix}{stem}.png)\n'
                if sid == VIDEO_SKILL:
                    content = content.replace('![After]', '![Video Preview]') + '\n' + NOTICE + '\n'
                self.write(f'{parent}/README.md', content)
            wall.append(f'<img src="./examples/{sid}/{stem}.png">')
            if sid in FEATURED:
                featured += [f'![](./examples/{sid}/{name}.png)' for name in ('before', 'after')]
        home = '## Visual Case Wall\n\n' + '\n'.join(wall) + '\n\n## Featured Before / After\n\n' + '\n'.join(featured)
        self.write('README.md', home)
        self.write('README.zh.md', home)

    def write(self, relative, text):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding='utf-8')

    def replace(self, relative, old, new):
        path = self.root / relative
        self.write(relative, path.read_text(encoding='utf-8').replace(old, new))

    def assert_error(self, text):
        errors, _, _ = validate(self.root)
        self.assertTrue(any(text in error for error in errors), errors)

    def test_complete_collection_passes(self):
        errors, warnings, skills = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(warnings, [])
        self.assertEqual(len(skills), 10)

    def test_missing_output_fails_even_with_pending_note(self):
        (self.root / 'examples/materialized-explainer/after.png').unlink()
        self.write('examples/materialized-explainer/README.md', 'Pending asset replacement')
        self.assert_error('missing after.png')

    def test_unreferenced_before_is_optional_for_nonfeatured_case(self):
        sid = 'materialized-explainer'
        (self.root / f'examples/{sid}/before.png').unlink()
        for folder, prefix in ((f'examples/{sid}', './'), (f'skills/{sid}', f'../../examples/{sid}/')):
            self.replace(f'{folder}/README.md', f'![Before]({prefix}before.png)', '')
        errors, warnings, _ = validate(self.root)
        self.assertEqual(errors, [])
        self.assertEqual(len(warnings), 1)

    def test_referenced_before_must_exist(self):
        (self.root / 'examples/materialized-explainer/before.png').unlink()
        self.assert_error('missing image target')

    def test_svg_disguised_as_png_fails(self):
        (self.root / 'examples/materialized-explainer/after.png').write_text('<svg/>')
        self.assert_error('file bytes do not match raster extension')

    def test_svg_assets_and_external_svg_references_fail(self):
        self.write('examples/materialized-explainer/after.svg', '<svg/>')
        self.assert_error('SVG example assets are prohibited')
        self.write('examples/materialized-explainer/README.md', '![](https://example.com/examples/case/after.svg)')
        self.assert_error('forbidden example SVG reference')

    def test_reference_style_markdown_missing_image_fails(self):
        page = 'skills/materialized-explainer/README.md'
        self.replace(page, '## Example', '![missing][source]\n[source]: ./missing.png\n\n## Example')
        self.assert_error('missing image target ./missing.png')

    def test_manifest_and_skill_authors_are_checked(self):
        self.manifest['author'] = 'Other'
        self.write('skills.json', json.dumps(self.manifest))
        self.assert_error('manifest author must be')
        self.replace('skills/materialized-explainer/SKILL.md', 'author: 德里克文', 'author: Other')
        self.assert_error('materialized-explainer: author must be')

    def test_extra_example_directory_fails(self):
        (self.root / 'examples/unregistered').mkdir()
        self.assert_error('manifest/examples mismatch')

    def test_duplicate_manifest_id_fails(self):
        self.manifest['skills'].append(self.manifest['skills'][0])
        self.write('skills.json', json.dumps(self.manifest))
        self.assert_error('exactly 10 unique')

    def test_video_label_and_disclaimer_are_checked(self):
        page = f'skills/{VIDEO_SKILL}/README.md'
        self.replace(page, 'Video Preview', 'Final Video')
        self.assert_error('must use Video Preview terminology')
        self.assert_error('static preview must not be labeled final video')
        self.replace(page, NOTICE, '')
        self.assert_error('missing generated-frame disclaimer')

    def test_video_after_filename_fails(self):
        shutil.copyfile(self.root / f'examples/{VIDEO_SKILL}/before.png', self.root / f'examples/{VIDEO_SKILL}/after.png')
        self.assert_error('use preview-frame, not after')

    def test_missing_wall_thumbnail_and_wrong_featured_pair_fail(self):
        self.replace('README.md', '<img src="./examples/materialized-explainer/after.png">', '')
        self.assert_error('Visual Case Wall must display')
        self.replace('README.zh.md', './examples/character-sheet-board/before.png', './examples/memory-tile-portrait-poster/before.png')
        self.assert_error('Before / After must display')

    def test_short_skill_still_fails(self):
        path = self.root / 'skills/materialized-explainer/SKILL.md'
        self.write(str(path.relative_to(self.root)), path.read_text(encoding='utf-8').split('---', 2)[0] +
                   '---\nname: materialized-explainer\nmetadata:\n  author: 德里克文\n  version: 1.0.0\n---\nShort')
        self.assert_error('SKILL.md unexpectedly short')


if __name__ == '__main__':
    unittest.main()
