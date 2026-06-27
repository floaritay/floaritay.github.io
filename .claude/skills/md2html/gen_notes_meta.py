"""Generate notes metadata JSON from docs/ directory.

Scans all docs/**/*.md files, extracts git last-commit dates,
and writes docs/_notes.json.
"""

import json
import re
import subprocess
from pathlib import Path

DOCS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "docs"
POSTS_DIR = DOCS_DIR / "posts"
OUTPUT = DOCS_DIR / "_notes.json"
OUTPUT_JS = DOCS_DIR / "_notes.js"
OUTPUT_POSTS = DOCS_DIR / "_posts.json"
OUTPUT_POSTS_JS = DOCS_DIR / "_posts.js"

# Category display names (Chinese)
CATEGORY_NAMES = {
    "Agent": "Agent",
    "Backend": "Backend",
    "CV": "CV",
    "DeepLearing": "DeepLearning",
    "Intelligent_decision_planning": "决策与规划",
    "MatLab": "MatLab",
    "NLP": "NLP",
    "ROS": "ROS",
    "SQL": "SQL",
    "Vibe_Coding": "Vibe Coding",
    "basic": "Basic",
    "data_analysis": "数据分析",
    "machine_learning": "机器学习",
    "python": "Python",
    "reptile": "爬虫",
    "scrapy": "Scrapy",
}


def get_git_date(file_path: Path) -> str:
    """Get the last git commit date for a file (YYYY-MM-DD)."""
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%as", "--", str(file_path)],
            capture_output=True, text=True, cwd=DOCS_DIR.parent,
            timeout=10,
        )
        date = result.stdout.strip()
        if date and re.match(r"\d{4}-\d{2}-\d{2}", date):
            return date
    except Exception:
        pass
    return ""


def extract_title(md_path: Path) -> str:
    """Extract the note title from a markdown file.

    Strategy: use the filename stem as the title, since the first H1 after
    the TOC is typically a numbered section heading (e.g., '# 1 简介'),
    not the note's actual title.
    """
    return md_path.stem


def extract_desc(md_path: Path) -> str:
    """Extract a short description from the markdown content.

    Looks for the first non-heading, non-empty, non-code paragraph after the TOC.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
        # Find the first --- after # 目录 (the TOC separator)
        # Use regex to find the TOC block and skip past it
        m = re.search(r"^# 目录\n.*?\n---\n", text, re.DOTALL | re.MULTILINE)
        if m:
            body = text[m.end():]
        else:
            # Fallback: skip past first ---
            idx = text.find("\n---\n")
            body = text[idx + 5:] if idx >= 0 else text

        in_code_block = False
        for line in body.split("\n"):
            stripped = line.strip()

            # Track code blocks
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue

            if not stripped:
                continue
            if stripped.startswith("#"):
                continue
            if stripped.startswith("- ") or stripped.startswith("* "):
                continue
            if stripped.startswith(">"):
                continue
            if stripped.startswith("|") or stripped.startswith("!"):
                continue
            if stripped.startswith("---") or stripped.startswith("==="):
                continue
            if re.match(r"^[-|:\s]+$", stripped):
                continue
            # Skip import/class/def lines (code)
            if re.match(r"^(import |from |class |def |if __)", stripped):
                continue
            # Got a real paragraph
            desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", stripped)
            desc = re.sub(r"`([^`]+)`", r"\1", desc)
            desc = re.sub(r"\*\*([^*]+)\*\*", r"\1", desc)
            desc = re.sub(r"\*([^*]+)\*", r"\1", desc)
            if len(desc) > 80:
                desc = desc[:77] + "..."
            return desc
    except Exception:
        pass
    return ""


def build_note_entry(md_path: Path) -> dict:
    """Build a single note metadata entry."""
    rel = md_path.relative_to(DOCS_DIR)
    category = rel.parts[0] if len(rel.parts) > 1 else "root"
    title = extract_title(md_path) or md_path.stem
    desc = extract_desc(md_path)
    date = get_git_date(md_path)

    return {
        "category": category,
        "categoryName": CATEGORY_NAMES.get(category, category),
        "title": title,
        "file": rel.name,
        "path": str(rel.with_suffix(".html")).replace("\\", "/"),
        "mdPath": str(rel).replace("\\", "/"),
        "desc": desc,
        "updated": date,
    }


def extract_post_title(md_path: Path) -> str:
    """Extract the blog post title from the first H1 heading."""
    try:
        text = md_path.read_text(encoding="utf-8")
        m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
        if m:
            return m.group(1).strip()
    except Exception:
        pass
    return md_path.stem


def extract_post_desc(md_path: Path) -> str:
    """Extract a short description from the blog post content.

    Looks for the first blockquote (> ...) as summary, or the first paragraph.
    """
    try:
        text = md_path.read_text(encoding="utf-8")
        lines = text.split("\n")
        in_code_block = False

        # First try: look for blockquote summary
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            if stripped.startswith("> "):
                desc = stripped[2:]
                desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", desc)
                desc = re.sub(r"`([^`]+)`", r"\1", desc)
                desc = re.sub(r"\*\*([^*]+)\*\*", r"\1", desc)
                desc = re.sub(r"\*([^*]+)\*", r"\1", desc)
                if len(desc) > 80:
                    desc = desc[:77] + "..."
                return desc

        # Fallback: first real paragraph
        in_code_block = False
        passed_heading = False
        for line in lines:
            stripped = line.strip()
            if stripped.startswith("```"):
                in_code_block = not in_code_block
                continue
            if in_code_block:
                continue
            if stripped.startswith("#"):
                passed_heading = True
                continue
            if not stripped:
                continue
            if not passed_heading:
                continue
            if stripped.startswith(">") or stripped.startswith("-") or stripped.startswith("*"):
                continue
            if stripped.startswith("|") or stripped.startswith("!") or stripped.startswith("---"):
                continue
            desc = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", stripped)
            desc = re.sub(r"`([^`]+)`", r"\1", desc)
            desc = re.sub(r"\*\*([^*]+)\*\*", r"\1", desc)
            desc = re.sub(r"\*([^*]+)\*", r"\1", desc)
            if len(desc) > 80:
                desc = desc[:77] + "..."
            return desc
    except Exception:
        pass
    return ""


def build_post_entry(md_path: Path) -> dict:
    """Build a single blog post metadata entry."""
    rel = md_path.relative_to(DOCS_DIR)
    title = extract_post_title(md_path) or md_path.stem
    desc = extract_post_desc(md_path)
    date = get_git_date(md_path)

    return {
        "title": title,
        "file": rel.name,
        "path": str(rel.with_suffix(".html")).replace("\\", "/"),
        "mdPath": str(rel).replace("\\", "/"),
        "desc": desc,
        "updated": date,
    }


def main():
    print(f"Scanning {DOCS_DIR} for markdown files...\n")

    notes = []
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        # Skip _notes.json, _posts.json, and other special files
        if md_file.name.startswith("_"):
            continue
        # Skip posts directory (handled separately)
        if POSTS_DIR in md_file.parents:
            continue
        entry = build_note_entry(md_file)
        notes.append(entry)
        print(f"  {entry['mdPath']} -> date={entry['updated']}")

    # Sort by category then title
    notes.sort(key=lambda n: (n["category"], n["title"]))

    # Write JSON (for tools / external use)
    OUTPUT.write_text(
        json.dumps(notes, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Write JS (for browser <script> tag — works with file:// and http://)
    js_content = "window.__NOTES_DATA = " + json.dumps(notes, ensure_ascii=False) + ";\n"
    OUTPUT_JS.write_text(js_content, encoding="utf-8")

    print(f"\nDone. Wrote {len(notes)} notes to:")
    print(f"  {OUTPUT.relative_to(DOCS_DIR.parent)}")
    print(f"  {OUTPUT_JS.relative_to(DOCS_DIR.parent)}")

    # Scan blog posts
    print(f"\nScanning {POSTS_DIR} for blog posts...\n")
    posts = []
    if POSTS_DIR.is_dir():
        for md_file in sorted(POSTS_DIR.rglob("*.md")):
            if md_file.name.startswith("_"):
                continue
            entry = build_post_entry(md_file)
            posts.append(entry)
            print(f"  {entry['mdPath']} -> date={entry['updated']}")

    # Sort by date descending (newest first)
    posts.sort(key=lambda p: p.get("updated", ""), reverse=True)

    # Write posts JSON
    OUTPUT_POSTS.write_text(
        json.dumps(posts, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Write posts JS
    posts_js = "window.__POSTS_DATA = " + json.dumps(posts, ensure_ascii=False) + ";\n"
    OUTPUT_POSTS_JS.write_text(posts_js, encoding="utf-8")

    print(f"\nDone. Wrote {len(posts)} posts to:")
    print(f"  {OUTPUT_POSTS.relative_to(DOCS_DIR.parent)}")
    print(f"  {OUTPUT_POSTS_JS.relative_to(DOCS_DIR.parent)}")


if __name__ == "__main__":
    main()
