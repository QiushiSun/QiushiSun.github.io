#!/usr/bin/env python3
"""Migrate selected Hexo posts from QiushiSun-Blog-old/ to Jekyll _posts/.

This script does:
  1. Read selected source files (the curated `MIGRATE` list below)
  2. Parse Hexo front matter, normalize to Jekyll front matter
  3. Rewrite image paths from /gallery/<slug>/<file> to /assets/blog/<slug>/<file>
     (and from /gallery/<file> for shared files)
  4. Strip the Hexo `<!--more-->` separator (Jekyll uses `excerpt_separator`)
  5. Write output to _posts/YYYY-MM-DD-slug.md
  6. Copy referenced images from QiushiSun-Blog-old/source/gallery/ to assets/blog/<slug>/

Run from the repository root: `python3 scripts/migrate_old_blog.py`.
"""
from __future__ import annotations

import os
import re
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_POSTS = REPO_ROOT / "QiushiSun-Blog-old" / "source" / "_posts"
SRC_GALLERY = REPO_ROOT / "QiushiSun-Blog-old" / "source" / "gallery"
DST_POSTS = REPO_ROOT / "_posts"
DST_ASSETS = REPO_ROOT / "assets" / "blog"


@dataclass
class Migration:
    src_filename: str
    new_slug: str
    excerpt: str = ""


# Curated list of posts worth migrating.
MIGRATE: list[Migration] = [
    Migration("Novelty in Science.md", "novelty-in-science",
              "学习笔记：判断研究工作的价值，以及研究新意度（Novelty）的五大误解。"),
    Migration("LaTeX-Tricks-undergraduate-thesis.md", "latex-tricks-undergraduate-thesis",
              "撰写本科毕业论文期间用到的一些 (Xe)LaTeX 小技巧。"),
    Migration("2022-3-latex-beamer-tricks.md", "latex-beamer-tricks",
              "配置 LaTeX Beamer 的小技巧合集。"),
    Migration("LaTeX-Template-for-ECNU-undergraduate-thesis.md", "latex-template-ecnu-undergraduate-thesis",
              "华东师大本科毕业设计论文的 LaTeX 模版（Class of 2022）。"),
    Migration("2022-6-12-Code-Capture-Paper.md", "a-structural-analysis-of-codeptms",
              "[论文导读] A Structural Analysis of Pre-Trained Language Model for Source Code (ICSE 2022)。"),
    Migration("2022-7-CodePTMs-Review1.md", "codeptms-review-part1",
              "Code 预训练语言模型学习指南（原理 / 分析 / 代码）Part 1。"),
    Migration("2022-7-CodePTMs-Review2.md", "codeptms-review-part2",
              "Code 预训练语言模型学习指南（原理 / 分析 / 代码）Part 2。"),
    Migration("2022-7-17-Icarus-MathJax.md", "hexo-icarus-mathjax",
              "如何让自己的博客能可靠地渲染数学公式？快速为 Hexo-Icarus 配置 MathJax。"),
    Migration("2022-8-A-new-chapter.md", "a-new-chapter-nus",
              "刚到新加坡的第一周：办手续、晒校园、记录新生活。"),
    Migration("2022-8-10-ViLT.md", "vilt-vision-language-transformer",
              "[论文导读] ViLT: Vision-and-Language Transformer Without Convolution or Region Supervision。"),
    Migration("2022-8-19-Probing-CodePTMs.md", "probing-codeptms",
              "[论文导读] Probing Pretrained Models of Source Code。"),
    Migration("2022-8-23-MacSetup.md", "configure-macbook-for-development-2022",
              "在 2022 年配置一台用于开发的 MacBook 的完整记录。"),
    Migration("2022-9-9-Black-Box-Tuning.md", "black-box-tuning-lmaas",
              "[论文导读] Black-Box Tuning for Language-Model-as-a-Service。"),
]


# ---------- Front matter parsing ----------

FRONT_MATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Very small, purpose-built YAML-ish front-matter parser.

    The Hexo posts only use a small subset of YAML (scalar keys + string lists).
    Avoid pulling PyYAML to keep the script dependency-free.
    """
    m = FRONT_MATTER_RE.match(text)
    if not m:
        return {}, text
    fm_text = m.group(1)
    body = text[m.end():]

    fm: dict = {}
    current_key: str | None = None
    current_list: list[str] | None = None
    for raw_line in fm_text.splitlines():
        line = raw_line.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        if line.startswith("- "):
            if current_list is not None:
                current_list.append(line[2:].strip().strip('"').strip("'"))
            continue
        # Otherwise it's a key: value (or key:) line
        if ":" in line:
            key, _, value = line.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "" or value is None:
                # Could be a list header
                current_list = []
                fm[key] = current_list
                current_key = key
            else:
                value = value.strip('"').strip("'")
                fm[key] = value
                current_key = key
                current_list = None
    return fm, body


# ---------- Helpers ----------

DATE_RE = re.compile(r"^\d{4}-\d{1,2}-\d{1,2}")


def normalize_date(raw: str) -> datetime:
    raw = raw.strip()
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            continue
    # Fall back: take first 10 chars as date
    return datetime.strptime(raw[:10], "%Y-%m-%d")


IMAGE_GALLERY_RE = re.compile(r"/gallery/([^\s)\"']+)")


def rewrite_image_paths(body: str, slug: str, image_log: set[str]) -> str:
    """Rewrite /gallery/<...> references to /assets/blog/<slug>/<file>.

    For files originally in /gallery/<post-folder>/<file>, the new path keeps the
    slug-style folder. For files referenced as /gallery/<file> directly (shared
    images) they are flattened into the same /assets/blog/<slug>/<file>.

    The set `image_log` collects (src_relpath -> dst_relpath_under_assets/blog).
    """
    def replace(match: re.Match) -> str:
        rel = match.group(1)
        # Some posts use double slashes (e.g. /gallery//Data-Center-Structure.png)
        rel = rel.lstrip("/")
        # Normalize: posts may include (e.g.) /source/gallery/... — strip "source/"
        if rel.startswith("source/"):
            rel = rel[len("source/"):]

        src_rel = rel  # path relative to QiushiSun-Blog-old/source/gallery/
        # The file name (last segment) goes into assets/blog/<slug>/
        filename = Path(rel).name
        dst_rel = f"{slug}/{filename}"
        image_log.add((src_rel, dst_rel))
        return f"/assets/blog/{dst_rel}"

    return IMAGE_GALLERY_RE.sub(replace, body)


def strip_more_separator(body: str) -> str:
    return body.replace("<!--more-->", "").strip() + "\n"


def to_yaml_list(items: Iterable[str]) -> str:
    parts = []
    for item in items:
        item = str(item).strip()
        if not item:
            continue
        # Quote if contains special chars
        safe = item.replace('"', '\\"')
        parts.append(f'  - "{safe}"')
    return "\n".join(parts)


def build_jekyll_front_matter(
    title: str,
    date: datetime,
    categories: list[str],
    tags: list[str],
    cover: str | None,
    excerpt: str,
    lang: str = "zh",
) -> str:
    lines = [
        "---",
        f'title: "{title.replace(chr(34), chr(92) + chr(34))}"',
        f"date: {date.strftime('%Y-%m-%d %H:%M:%S')} +0800",
        f'lang: {lang}',
    ]
    if categories:
        lines.append("categories:")
        lines.append(to_yaml_list(categories))
    if tags:
        lines.append("tags:")
        lines.append(to_yaml_list(tags))
    if cover:
        lines.append(f'cover: "{cover}"')
    if excerpt:
        excerpt_safe = excerpt.replace('"', '\\"').replace("\n", " ").strip()
        lines.append(f'excerpt: "{excerpt_safe}"')
    lines.append("---")
    lines.append("")  # blank line after FM
    return "\n".join(lines)


# ---------- Main ----------

def main() -> None:
    DST_POSTS.mkdir(parents=True, exist_ok=True)
    DST_ASSETS.mkdir(parents=True, exist_ok=True)

    image_log: set[tuple[str, str]] = set()
    written = []

    for m in MIGRATE:
        src_path = SRC_POSTS / m.src_filename
        if not src_path.exists():
            print(f"[skip] missing source: {src_path}")
            continue
        text = src_path.read_text(encoding="utf-8")
        fm, body = parse_front_matter(text)

        title = (fm.get("title") or m.new_slug).strip()
        date_raw = fm.get("date") or "2022-01-01 00:00:00"
        date = normalize_date(date_raw)

        categories = fm.get("categories") or []
        tags = fm.get("tags") or []
        cover = fm.get("cover")

        # Rewrite images, both inline body and cover
        per_post_log: set[tuple[str, str]] = set()
        body = rewrite_image_paths(body, m.new_slug, per_post_log)
        if cover:
            cover_rewritten = rewrite_image_paths(cover, m.new_slug, per_post_log)
        else:
            cover_rewritten = None

        body = strip_more_separator(body)

        new_fm = build_jekyll_front_matter(
            title=title,
            date=date,
            categories=categories,
            tags=tags,
            cover=cover_rewritten,
            excerpt=m.excerpt,
            lang="zh",
        )

        out_name = f"{date.strftime('%Y-%m-%d')}-{m.new_slug}.md"
        out_path = DST_POSTS / out_name
        out_path.write_text(new_fm + body, encoding="utf-8")
        written.append(out_path.name)

        # Collect images for copying
        for src_rel, dst_rel in per_post_log:
            image_log.add((src_rel, dst_rel))

    print("\n[posts] wrote:")
    for n in written:
        print("  -", n)

    # Copy images
    print("\n[images] copying:")
    copied, missing = 0, 0
    for src_rel, dst_rel in sorted(image_log):
        src_p = SRC_GALLERY / src_rel
        dst_p = DST_ASSETS / dst_rel
        dst_p.parent.mkdir(parents=True, exist_ok=True)
        if not src_p.exists():
            print(f"  [missing] {src_rel}")
            missing += 1
            continue
        shutil.copy2(src_p, dst_p)
        copied += 1
    print(f"\n[summary] {len(written)} posts, {copied} images copied, {missing} missing")


if __name__ == "__main__":
    main()
