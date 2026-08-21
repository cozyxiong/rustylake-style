#!/usr/bin/env python3
"""Validate the shipped rustylake-style skill files.

Reads SKILL.md (and every relative file it points at) from the repo.
No fixtures, no copies of those files. Exit 0 if the skill is well-formed.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
MD_LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
BACKTICK_PATH_RE = re.compile(r"`(references/[^`]+)`")


class SkillError(ValueError):
    pass


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def parse_simple_yaml_map(raw: str) -> dict[str, str]:
    """Parse a flat YAML map with optional folded (>) / literal (|) scalars."""
    result: dict[str, str] = {}
    lines = raw.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if not line.strip() or line.lstrip().startswith("#"):
            i += 1
            continue
        if line[:1] in " \t":
            raise SkillError(f"unexpected indent in frontmatter: {line!r}")
        if ":" not in line:
            raise SkillError(f"invalid frontmatter line: {line!r}")
        key, _, rest = line.partition(":")
        key = key.strip()
        rest = rest.strip()
        if rest in (">", "|", ">-", "|-", ">+", "|+"):
            folded = rest.startswith(">")
            i += 1
            block: list[str] = []
            while i < len(lines) and (
                not lines[i].strip() or lines[i][:1] in " \t"
            ):
                block.append(lines[i])
                i += 1
            indents = [len(b) - len(b.lstrip(" ")) for b in block if b.strip()]
            pad = min(indents) if indents else 0
            stripped = [b[pad:] if len(b) >= pad else b for b in block]
            if folded:
                value = " ".join(s.strip() for s in stripped if s.strip())
            else:
                value = "\n".join(stripped).strip("\n")
            result[key] = value
            continue
        result[key] = rest.strip().strip("'\"")
        i += 1
    return result


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    text = text.lstrip("\ufeff")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise SkillError("SKILL.md is missing YAML frontmatter")
    end = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end = i
            break
    if end is None:
        raise SkillError("SKILL.md frontmatter is not closed")
    raw = "\n".join(lines[1:end])
    body = "\n".join(lines[end + 1 :]).lstrip("\n")
    if not raw.strip():
        raise SkillError("SKILL.md frontmatter is empty")
    return parse_simple_yaml_map(raw), body


def _normalize_rel(href: str) -> str | None:
    target = href.strip().split()[0].strip("<>")
    if not target or target.startswith(("#", "http://", "https://", "mailto:")):
        return None
    return target.replace("\\", "/")


def referenced_relpaths(body: str) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for match in (*MD_LINK_RE.finditer(body), *BACKTICK_PATH_RE.finditer(body)):
        rel = _normalize_rel(match.group(1))
        if rel and rel not in seen:
            seen.add(rel)
            found.append(rel)
    return found


def collect_referenced_files(body: str, root: Path) -> dict[str, str]:
    refs: dict[str, str] = {}
    root = root.resolve()
    for rel in referenced_relpaths(body):
        path = (root / rel).resolve()
        try:
            path.relative_to(root)
        except ValueError:
            continue
        if path.is_file():
            refs[rel] = path.read_text(encoding="utf-8")
    return refs


def load_skill(root: Path) -> tuple[dict[str, str], str, dict[str, str]]:
    skill_path = root / "SKILL.md"
    if not skill_path.is_file():
        raise SkillError(f"missing skill file: {skill_path}")
    fm, body = parse_frontmatter(skill_path.read_text(encoding="utf-8"))
    refs = collect_referenced_files(body, root)
    return fm, body, refs


def _corpus(body: str, refs: dict[str, str]) -> str:
    return body + "\n" + "\n".join(refs.values())


def _sections(markdown: str) -> dict[str, str]:
    parts = re.split(r"(?m)^##\s+", markdown)
    out: dict[str, str] = {}
    for part in parts[1:]:
        lines = part.splitlines()
        title = lines[0].strip().lower()
        out[title] = "\n".join(lines[1:])
    return out


def _has_any(text: str, needles: tuple[str, ...]) -> bool:
    lower = text.lower()
    for needle in needles:
        if not needle.isascii():
            if needle in text:
                return True
        elif needle.lower() in lower:
            return True
    return False


def _valid_name(name: str) -> bool:
    return (
        isinstance(name, str)
        and 1 <= len(name) <= 64
        and NAME_RE.fullmatch(name) is not None
    )


def validate(
    fm: dict[str, str], body: str, refs: dict[str, str]
) -> list[str]:
    errors: list[str] = []
    name = (fm or {}).get("name", "")
    description = (fm or {}).get("description", "")

    if not fm:
        errors.append("frontmatter is missing")
    if not name:
        errors.append("frontmatter name is missing")
    elif not _valid_name(name):
        errors.append(
            "frontmatter name must be 1–64 chars of lowercase letters, "
            "digits, and single hyphens (no leading/trailing/consecutive hyphens)"
        )
    if not description or not str(description).strip():
        errors.append("frontmatter description is empty")
    else:
        desc = str(description)
        if not _has_any(desc, ("Rusty Lake", "锈湖")):
            errors.append("description must mention Rusty Lake or 锈湖")
        if not _has_any(desc, ("头像", "avatar")):
            errors.append("description must mention 头像 or avatar")
        if not _has_any(desc, ("物品", "item")):
            errors.append("description must mention 物品 or item")
        if not _has_any(
            desc, ("upload", "photo", "image", "上传", "照片", "图片")
        ):
            errors.append(
                "description must mention upload/photo/image or 上传/照片/图片"
            )

    if not body.strip():
        errors.append("SKILL.md body is empty")

    corpus = _corpus(body, refs)
    sections = _sections(body)
    # Merge referenced sections so prompts living in references/ still count.
    for ref_text in refs.values():
        for title, text in _sections(ref_text).items():
            sections[title] = sections.get(title, "") + "\n" + text

    avatar = sections.get("avatar", "")
    if not avatar.strip():
        errors.append("avatar workflow section is missing")
    else:
        if not _has_any(avatar, ("image-edit", "image-to-image")):
            errors.append(
                "avatar workflow must use image-edit / image-to-image"
            )
        if not _has_any(avatar, ("upload", "attached", "photo", "上传")):
            errors.append("avatar workflow must require a user image/upload")
        if not _has_any(
            avatar, ("ask", "stop", "do not invent", "rather than invent")
        ):
            errors.append(
                "avatar workflow must ask for an upload when no photo is present"
            )
        if not _has_any(
            avatar,
            (
                "likeness",
                "identity",
                "face structure",
                "cut-out",
                "collage",
            ),
        ):
            errors.append("avatar workflow must keep likeness / cut-out portrait")

    item = sections.get("item", "")
    if not item.strip():
        errors.append("item workflow section is missing")
    else:
        if not _has_any(item, ("image-edit", "image-to-image")):
            errors.append("item workflow must use image-edit / image-to-image")
        if not _has_any(item, ("inventory", "物品", "puzzle")):
            errors.append(
                "item workflow must present an isolated inventory / puzzle object"
            )
        if not _has_any(item, ("isolated",)):
            errors.append("item workflow must isolate the object")
        if not _has_any(item, ("plain", "pale")):
            errors.append("item workflow must use a plain/pale ground")
        if _has_any(item, ("head-and-shoulders", "bust", "likeness")):
            errors.append(
                "item workflow must not be a second copy of the avatar portrait recipe"
            )

    style_haystack = corpus.lower()
    if not (
        ("flat" in style_haystack and "low-fi" in style_haystack)
        or ("flat" in style_haystack and "lo-fi" in style_haystack)
        or ("flat" in style_haystack and "lowfi" in style_haystack)
    ):
        errors.append("style recipe must state flat low-fi illustration")
    if not _has_any(corpus, ("muted", "desaturated")):
        errors.append("style recipe must state a muted/desaturated palette")
    palette_hits = sum(
        bool(p in style_haystack)
        for p in ("grey", "gray", "ochre", "earth", "sickly green")
    )
    if palette_hits < 3:
        errors.append(
            "style recipe must name the muted palette "
            "(greys, ochre, pale earth, sickly green)"
        )
    if not _has_any(corpus, ("doll-like", "doll like")):
        errors.append("style recipe must state uncanny doll-like stillness")
    if not _has_any(corpus, ("simplified geometric face", "simplified geometric")):
        errors.append("style recipe must state a simplified geometric face")
    if "isolated" not in style_haystack:
        errors.append("style recipe must isolate the subject")
    if not _has_any(corpus, ("cut-out", "cut out", "collage")):
        errors.append(
            "style recipe must state photographic-collage / cut-out portrait quality"
        )
    if re.search(r"rusty lake style", style_haystack) and not (
        "low-fi" in style_haystack or "collage" in style_haystack
    ):
        errors.append(
            "style recipe is only a 'Rusty Lake style' synonym with no visual constraints"
        )

    return errors


def validate_readme(root: Path) -> list[str]:
    errors: list[str] = []
    readme_path = root / "README.md"
    if not readme_path.is_file():
        return ["missing README.md"]
    text = readme_path.read_text(encoding="utf-8")
    url = "https://github.com/cozyxiong/rustylake-style.git"
    if url not in text:
        errors.append(f"README must name {url}")
    if not _has_any(text, ("npx skills add", "Agent", "skill")):
        errors.append("README must tell the user how an Agent installs the skill")
    if not (root / "SKILL.md").is_file():
        errors.append("scanner-visible SKILL.md missing at repo root")
    return errors


def check_repo(root: Path) -> list[str]:
    errors: list[str] = []
    try:
        fm, body, refs = load_skill(root)
    except SkillError as exc:
        return [str(exc)]
    errors.extend(validate(fm, body, refs))
    errors.extend(validate_readme(root))
    pointed = referenced_relpaths(body)
    if "references/style.md" in pointed and "references/style.md" not in (
        load_skill(root)[2]
    ):
        errors.append("SKILL.md points at references/style.md but the file is missing")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=None,
        help="Skill repo root (default: parent of scripts/)",
    )
    args = parser.parse_args(argv)
    root = (args.root or repo_root()).resolve()
    errors = check_repo(root)
    if errors:
        print("FAIL")
        for err in errors:
            print(f"- {err}")
        return 1
    fm, body, refs = load_skill(root)
    print("OK")
    print(f"name: {fm.get('name')}")
    print(f"description: {fm.get('description')}")
    print(f"referenced_files: {', '.join(refs) if refs else '(none)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
