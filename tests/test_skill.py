"""Parser tests over the shipped rustylake-style skill files.

Drives scripts/check_skill.py against the real SKILL.md (and files it
references). Negative cases feed the shipped validate() function in memory —
they do not mock or duplicate the skill files.
"""

from __future__ import annotations

import importlib.util
import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
_CHECKER_PATH = ROOT / "scripts" / "check_skill.py"

_spec = importlib.util.spec_from_file_location("check_skill", _CHECKER_PATH)
if _spec is None or _spec.loader is None:
    raise RuntimeError(f"cannot load {_CHECKER_PATH}")
check_skill = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(check_skill)


def _ok_frontmatter(**overrides: str) -> dict[str, str]:
    fm = {
        "name": "rustylake-style",
        "description": (
            "Generate Rusty Lake / 锈湖 style 头像/avatars and 物品/items "
            "from a user-uploaded image / 上传照片."
        ),
    }
    fm.update(overrides)
    return fm


class TestShippedSkill(unittest.TestCase):
    def test_loads_real_skill_md_not_a_fixture(self):
        skill_path = ROOT / "SKILL.md"
        self.assertTrue(skill_path.is_file(), "shipped SKILL.md must exist")
        fm, body, refs = check_skill.load_skill(ROOT)
        disk = skill_path.read_text(encoding="utf-8")
        parsed_fm, parsed_body = check_skill.parse_frontmatter(disk)
        self.assertEqual(fm, parsed_fm)
        self.assertEqual(body, parsed_body)
        self.assertIn("references/style.md", refs)
        style_path = ROOT / "references" / "style.md"
        self.assertEqual(
            refs["references/style.md"],
            style_path.read_text(encoding="utf-8"),
        )

    def test_shipped_repo_passes(self):
        errors = check_skill.check_repo(ROOT)
        self.assertEqual(errors, [], msg="\n".join(errors))

    def test_cli_entry_point_on_shipped_files(self):
        buf = io.StringIO()
        with redirect_stdout(buf):
            code = check_skill.main(["--root", str(ROOT)])
        self.assertEqual(code, 0)
        self.assertIn("OK", buf.getvalue())
        self.assertIn("rustylake-style", buf.getvalue())


class TestShippedValidator(unittest.TestCase):
    def test_missing_frontmatter_fails(self):
        errors = check_skill.validate({}, "body", {})
        self.assertTrue(
            any("frontmatter" in e.lower() or "name" in e.lower() for e in errors),
            errors,
        )

    def test_invalid_name_fails(self):
        errors = check_skill.validate(
            _ok_frontmatter(name="Rusty_Lake"), "body", {}
        )
        self.assertTrue(any("name" in e.lower() for e in errors), errors)

    def test_empty_description_fails(self):
        errors = check_skill.validate(_ok_frontmatter(description="  "), "body", {})
        self.assertTrue(any("description" in e.lower() for e in errors), errors)

    def test_description_missing_triggers_fails(self):
        errors = check_skill.validate(
            _ok_frontmatter(description="a restyle skill"),
            "body",
            {},
        )
        joined = " ".join(errors).lower()
        self.assertIn("rusty lake", joined)
        self.assertTrue("avatar" in joined or "头像" in " ".join(errors))

    def test_missing_avatar_workflow_fails(self):
        body = (
            "## Item\n"
            "Use image-edit / image-to-image on the upload. Isolated "
            "inventory object on a plain pale ground.\n"
        )
        refs = {
            "references/style.md": (
                "flat low-fi muted desaturated greys ochre pale earth "
                "sickly green doll-like simplified geometric face isolated "
                "bold black outlines flat cel fills damask wallpaper "
                "moles piercings from the upload"
            )
        }
        errors = check_skill.validate(_ok_frontmatter(), body, refs)
        self.assertTrue(any("avatar" in e.lower() for e in errors), errors)

    def test_missing_item_workflow_fails(self):
        body = (
            "## Avatar\n"
            "If no photo, ask for an upload and stop; do not invent a face. "
            "Restyle the likeness with image-edit / image-to-image. "
            "Keep identity as a full illustration. Face marks follow the "
            "upload: moles and piercings from the photo only.\n"
        )
        refs = {
            "references/style.md": (
                "flat low-fi muted desaturated greys ochre pale earth "
                "sickly green doll-like simplified geometric face isolated "
                "bold black outlines flat cel fills damask wallpaper "
                "moles piercings from the upload"
            )
        }
        errors = check_skill.validate(_ok_frontmatter(), body, refs)
        self.assertTrue(any("item" in e.lower() for e in errors), errors)

    def test_vague_style_only_fails(self):
        body = (
            "## Avatar\n"
            "If no photo, ask for an upload and stop. "
            "Use image-edit on the likeness. Keep identity.\n"
            "## Item\n"
            "Use image-edit. Isolated inventory object on a plain pale ground.\n"
        )
        refs = {"references/style.md": "Make it Rusty Lake style."}
        errors = check_skill.validate(_ok_frontmatter(), body, refs)
        self.assertTrue(
            any("low-fi" in e.lower() or "style recipe" in e.lower() for e in errors),
            errors,
        )

    def test_item_that_copies_avatar_portrait_fails(self):
        body = (
            "## Avatar\n"
            "If no photo, ask for an upload and stop. "
            "Use image-edit on the likeness. Keep identity as a full illustration. "
            "Face marks follow the upload: moles and piercings from the photo only.\n"
            "## Item\n"
            "Use image-edit. Isolated inventory object on a plain pale ground. "
            "Head-and-shoulders bust likeness.\n"
        )
        refs = {
            "references/style.md": (
                "flat low-fi muted desaturated greys ochre pale earth "
                "sickly green doll-like simplified geometric face isolated "
                "bold black outlines flat cel fills damask wallpaper "
                "moles piercings from the upload"
            )
        }
        errors = check_skill.validate(_ok_frontmatter(), body, refs)
        self.assertTrue(
            any("second copy" in e.lower() or "portrait" in e.lower() for e in errors),
            errors,
        )


class TestFrontmatterParser(unittest.TestCase):
    def test_rejects_unfenced_markdown(self):
        with self.assertRaises(check_skill.SkillError):
            check_skill.parse_frontmatter("# just a heading\n")

    def test_parses_folded_description(self):
        text = (
            "---\n"
            "name: rustylake-style\n"
            "description: >\n"
            "  line one\n"
            "  line two\n"
            "---\n"
            "\n"
            "body here\n"
        )
        fm, body = check_skill.parse_frontmatter(text)
        self.assertEqual(fm["name"], "rustylake-style")
        self.assertEqual(fm["description"], "line one line two")
        self.assertIn("body here", body)


if __name__ == "__main__":
    unittest.main()
