#!/usr/bin/env python3
"""Migrate selected research blog posts from `QiushiSun-Blog-old-2/` to Jekyll.

Differences vs `migrate_old_blog.py`:

- Source files have NO YAML front matter; we hand-pick `title`, `date`,
  `categories`, `tags`, `cover`, `excerpt` per post in the `MIGRATE` list below.
- Source files live in per-post folders, with images alongside in
  `static/` / `figure(s)/` / `images/` subfolders. References look like
  `./static/x.png`, `figure/y.jpg`, `images/z.png`.
- Image references can also be HTML `<img src="...">` (e.g. OS-Genesis post).
- We strip an optional leading H1 line (since the title goes into front matter).

Usage:
    python3 scripts/migrate_old_blog_v2.py
"""
from __future__ import annotations

import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SRC_ROOT = REPO_ROOT / "QiushiSun-Blog-old-2"
DST_POSTS = REPO_ROOT / "_posts"
DST_ASSETS = REPO_ROOT / "assets" / "blog"


@dataclass
class Migration:
    src_relpath: str  # path relative to SRC_ROOT
    slug: str  # used for filename + asset folder + permalink
    title: str
    date: str  # YYYY-MM-DD HH:MM:SS
    categories: list[str] = field(default_factory=list)
    tags: list[str] = field(default_factory=list)
    excerpt: str = ""
    # Optional: relative path inside the post folder to use as cover.
    # If None, we fall back to the first image found in the body.
    cover_src: str | None = None


MIGRATE: list[Migration] = [
    Migration(
        src_relpath="2407-InstructGraph/InstructGraph宣传稿.md",
        slug="instructgraph-acl2024",
        title="InstructGraph：以图为中心的大模型指令微调与偏好对齐 (ACL 2024)",
        date="2024-07-15 10:00:00",
        categories=["LLM", "Graph"],
        tags=["LLM", "Graph", "Instruction Tuning", "ACL 2024"],
        excerpt="[论文分享] 当大语言模型遇到图——华东师大 & UCSD 联合提出 InstructGraph，以图为中心的指令微调与偏好对齐框架。ACL 2024 Findings.",
        cover_src="images/image0.png",
    ),
    Migration(
        src_relpath="2407-SEA/SEA.md",
        slug="sea-automated-peer-reviewing",
        title="SEA：基于大模型的自动评审框架",
        date="2024-07-30 10:00:00",
        categories=["LLM", "Research Methodology"],
        tags=["LLM", "Peer Review", "Evaluation"],
        excerpt="[论文分享] Automated Peer Reviewing in Paper SEA: Standardization, Evaluation, and Analysis。",
        cover_src="static/paper.png",
    ),
    Migration(
        src_relpath="2408-CoK/CoK.md",
        slug="chain-of-knowledge-acl2024",
        title="知识链 = 知识图谱 + 大模型 + 推理 − 幻觉 (ACL 2024)",
        date="2024-08-15 10:00:00",
        categories=["LLM", "Reasoning"],
        tags=["LLM", "Knowledge Graph", "Hallucination", "ACL 2024"],
        excerpt="[论文分享] Chain-of-Knowledge：华东师大 & 港大联合提出的、面向大语言模型推理的幻觉缓解方法，被 ACL 2024 接收为长文主会。",
        cover_src=None,  # No clear title figure; let the first body image be cover
    ),
    Migration(
        src_relpath="2411-ChatGen/ChatGen_zhihu_eq/ChatGen.md",
        slug="chatgen-text-to-image",
        title="ChatGen：自动化文生图系统",
        date="2024-11-25 10:00:00",
        categories=["Multimodal", "LLM"],
        tags=["Text-to-Image", "Multimodal", "Agents"],
        excerpt="[论文分享] ChatGen: Automatic Text-to-Image Generation From FreeStyle Chatting —— 用聊天驱动的文生图系统。",
        cover_src="static/title.png",
    ),
    Migration(
        src_relpath="2411-LD-DPO/LD-DPO_241105/[论文分享] LD-DPO：基于DPO的长度脱敏偏好优化算法.md",
        slug="ld-dpo-length-desensitization",
        title="LD-DPO：基于 DPO 的长度脱敏偏好优化算法",
        date="2024-11-05 10:00:00",
        categories=["LLM", "Alignment"],
        tags=["DPO", "Alignment", "Preference Optimization"],
        excerpt="[论文分享] Length Desensitization in Direct Preference Optimization。",
        cover_src="figure/paper.jpg",
    ),
    Migration(
        src_relpath="2501-Corex/corex.md",
        slug="corex-multi-model-collaboration",
        title="Corex：通过多模型协作增强推理能力 (COLM 2024)",
        date="2025-01-15 10:00:00",
        categories=["LLM", "Reasoning"],
        tags=["Multi-Agent", "Reasoning", "COLM 2024"],
        excerpt="[论文分享] Corex: Pushing the Boundaries of Complex Reasoning through Multi-Model Collaboration。",
        cover_src="static/title.png",
    ),
    Migration(
        src_relpath="2502 AgentStore/AgentStore.md",
        slug="agentstore-generalist-computer-assistant",
        title="AgentStore：迈向通专融合的自动化计算机助手",
        date="2025-02-15 10:00:00",
        categories=["Computer-Using Agents", "LLM"],
        tags=["GUI Agent", "Multi-Agent", "OS Agent"],
        excerpt="[论文分享] AgentStore: Scalable Integration of Heterogeneous Agents as Specialized Generalist Computer Assistant。",
        cover_src="static/title.png",
    ),
    Migration(
        src_relpath="2502-OCEAN/iclr25_ocean/main.md",
        slug="ocean-offline-cot-evaluation-iclr2025",
        title="OCEAN：离线多步推理评估与对齐 (ICLR 2025)",
        date="2025-02-20 10:00:00",
        categories=["LLM", "Reasoning"],
        tags=["Reasoning", "Knowledge Graph", "ICLR 2025"],
        excerpt="[论文分享] OCEAN: Offline Chain-of-thought Evaluation and Alignment in Large Language Models via Knowledge Graph Exploration. ICLR 2025.",
        cover_src=None,
    ),
    Migration(
        src_relpath="2502-OS-Atlas/OS-Atlas.md",
        slug="os-atlas-foundation-action-model",
        title="OS-Atlas：面向通用 GUI Agent 的基础动作模型",
        date="2025-02-25 10:00:00",
        categories=["Computer-Using Agents"],
        tags=["GUI Agent", "Foundation Model", "Action Model"],
        excerpt="[论文分享] OS-Atlas: A Foundation Action Model for Generalist GUI Agents.",
        cover_src="static/title.png",
    ),
    Migration(
        src_relpath="2503-LogiEval/LogicEval.md",
        slug="logical-reasoners-evaluation-tkde",
        title="大型语言模型真的擅长逻辑推理吗？(IEEE TKDE)",
        date="2025-03-20 10:00:00",
        categories=["LLM", "Reasoning"],
        tags=["Reasoning", "Evaluation", "IEEE TKDE"],
        excerpt="[论文分享] Are Large Language Models Really Good Logical Reasoners? A Comprehensive Evaluation and Beyond.",
        cover_src=None,
    ),
    Migration(
        src_relpath="2505-OS-Genesis-AINLP/OS-Genesis-AINLP.md",
        slug="os-genesis-acl2025",
        title="OS-Genesis：自动构造 GUI Agent 所需的训练数据 (ACL 2025)",
        date="2025-05-15 10:00:00",
        categories=["Computer-Using Agents"],
        tags=["GUI Agent", "Data Synthesis", "ACL 2025"],
        excerpt="[论文分享] OS-Genesis: Automating GUI Agent Trajectory Construction via Reverse Task Synthesis. ACL 2025.",
        cover_src="figures/AINLP推文内可以使用的covers/os-genesis-ainlp-cover-big.png",
    ),
]


# --------------------------------------------------------------------------
# Image rewriting
# --------------------------------------------------------------------------

# Markdown image: ![alt](path "title")
MD_IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
# HTML <img src="...">
HTML_IMG_RE = re.compile(r'<img\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>', re.IGNORECASE)
H1_RE = re.compile(r"^#\s+.*$", re.MULTILINE)


def is_remote_url(url: str) -> bool:
    return url.startswith(("http://", "https://", "//", "data:"))


def normalize_local_path(rel: str) -> str:
    """Normalize a local image path inside a post folder.

    - Strip surrounding whitespace
    - Drop a leading "./"
    - Decode common URL-escapes for spaces
    """
    rel = rel.strip()
    if rel.startswith("./"):
        rel = rel[2:]
    rel = rel.replace("%20", " ")
    return rel


def safe_dest_filename(rel: str) -> str:
    """Flatten a relative path into a single dest filename, preserving extension.

    Examples:
        "static/title.png"                       -> "title.png"
        "images/image0.png"                      -> "image0.png"
        "figures/sub/cover.png"                  -> "sub_cover.png" (folders joined by '_')
    """
    parts = rel.replace("\\", "/").split("/")
    if len(parts) <= 2:
        # Drop the leading subfolder (static/figure/images), keep the file name
        return parts[-1]
    # Multiple subfolders: join intermediate parts with '_' to avoid name collision
    middle = "_".join(parts[1:-1])
    name = parts[-1]
    return f"{middle}_{name}" if middle else name


def collect_and_rewrite_images(body: str, src_folder: Path, slug: str,
                               copy_log: dict[Path, Path]) -> str:
    """Replace local image paths in body and record source/dest pairs to copy."""

    def remap(local_rel: str) -> str | None:
        local_rel = normalize_local_path(local_rel)
        src_p = (src_folder / local_rel).resolve()
        if not src_p.exists():
            return None
        dst_filename = safe_dest_filename(local_rel)
        dst_p = DST_ASSETS / slug / dst_filename
        copy_log[src_p] = dst_p
        return f"/assets/blog/{slug}/{dst_filename}"

    def md_replace(m: re.Match) -> str:
        alt, url = m.group(1), m.group(2).strip()
        # Some refs include a "title" after the path: ![alt](path "title")
        url_only, _, title_part = url.partition(" ")
        if is_remote_url(url_only):
            return m.group(0)
        new = remap(url_only)
        if new is None:
            return m.group(0)
        if title_part:
            return f"![{alt}]({new} {title_part})"
        return f"![{alt}]({new})"

    def html_replace(m: re.Match) -> str:
        url = m.group(1).strip()
        if is_remote_url(url):
            return m.group(0)
        new = remap(url)
        if new is None:
            return m.group(0)
        return m.group(0).replace(m.group(1), new)

    body = MD_IMG_RE.sub(md_replace, body)
    body = HTML_IMG_RE.sub(html_replace, body)
    return body


def strip_leading_h1(body: str) -> str:
    """If the first non-blank content line is an H1, drop it (title moved to FM)."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        s = line.strip()
        if not s:
            continue
        if s.startswith("# "):
            return "\n".join(lines[:i] + lines[i + 1:])
        return body
    return body


# --------------------------------------------------------------------------
# Front matter
# --------------------------------------------------------------------------

def to_yaml_list(items: list[str]) -> str:
    out = []
    for item in items:
        safe = str(item).strip().replace('"', '\\"')
        out.append(f'  - "{safe}"')
    return "\n".join(out)


def build_front_matter(m: Migration, cover_url: str | None) -> str:
    parts = ["---"]
    parts.append(f'title: "{m.title.replace(chr(34), chr(92) + chr(34))}"')
    parts.append(f"date: {m.date} +0800")
    parts.append("lang: zh")
    if m.categories:
        parts.append("categories:")
        parts.append(to_yaml_list(m.categories))
    if m.tags:
        parts.append("tags:")
        parts.append(to_yaml_list(m.tags))
    if cover_url:
        parts.append(f'cover: "{cover_url}"')
    if m.excerpt:
        excerpt_safe = m.excerpt.replace('"', '\\"').replace("\n", " ").strip()
        parts.append(f'excerpt: "{excerpt_safe}"')
    parts.append("---")
    parts.append("")
    return "\n".join(parts)


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------

def main() -> None:
    DST_POSTS.mkdir(parents=True, exist_ok=True)
    DST_ASSETS.mkdir(parents=True, exist_ok=True)

    written: list[str] = []
    total_copied = 0
    total_missing = 0
    skipped: list[str] = []

    for m in MIGRATE:
        src_path = SRC_ROOT / m.src_relpath
        if not src_path.exists():
            print(f"[skip] missing source: {src_path}")
            skipped.append(m.slug)
            continue
        src_folder = src_path.parent

        body = src_path.read_text(encoding="utf-8")
        body = strip_leading_h1(body)

        copy_log: dict[Path, Path] = {}
        body = collect_and_rewrite_images(body, src_folder, m.slug, copy_log)

        # Cover handling
        cover_url: str | None = None
        if m.cover_src:
            cover_src = (src_folder / normalize_local_path(m.cover_src)).resolve()
            if cover_src.exists():
                dst_filename = safe_dest_filename(normalize_local_path(m.cover_src))
                dst_p = DST_ASSETS / m.slug / dst_filename
                copy_log[cover_src] = dst_p
                cover_url = f"/assets/blog/{m.slug}/{dst_filename}"
            else:
                print(f"  [warn] cover not found for {m.slug}: {m.cover_src}")
        if cover_url is None:
            # Fall back to the first body image
            for src_p, dst_p in copy_log.items():
                rel_inside_assets = dst_p.relative_to(REPO_ROOT / "assets")
                cover_url = "/assets/" + str(rel_inside_assets).replace("\\", "/")
                break

        front_matter = build_front_matter(m, cover_url)
        out_name = f"{m.date.split(' ')[0]}-{m.slug}.md"
        out_path = DST_POSTS / out_name
        out_path.write_text(front_matter + body.strip() + "\n", encoding="utf-8")
        written.append(out_name)

        # Copy images
        for src_p, dst_p in copy_log.items():
            dst_p.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(src_p, dst_p)
                total_copied += 1
            except Exception as e:
                print(f"  [error] copy {src_p} -> {dst_p}: {e}")
                total_missing += 1

    print("\n[posts] wrote:")
    for name in written:
        print("  -", name)
    print(f"\n[summary] {len(written)} posts, {total_copied} images copied, "
          f"{total_missing} errors, {len(skipped)} skipped")


if __name__ == "__main__":
    main()
