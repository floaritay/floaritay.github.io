#!/usr/bin/env python3
"""Convert all .md files in docs/ to styled .html pages.

Handles:
- Blockquote-wrapped code blocks (> ```lang ... > ```)
- Missing closing fences in blockquote code blocks
- LaTeX math expressions (backslash-paren, dollar, double-dollar)
- Mermaid diagrams (```mermaid)
- Windows backslash image paths
"""

import re
from pathlib import Path
import markdown

DOCS_DIR = Path(__file__).resolve().parent.parent.parent.parent / "docs"

# ── Math placeholders (to protect from markdown parser mangling) ──
MATH_BLOCK_PLACEHOLDER = "MATH_BLOCK_{idx}_ENDMATH"
MATH_INLINE_PLACEHOLDER = "MATH_INLINE_{idx}_ENDMATH"


def preprocess_blockquote_codeblocks(md_text: str) -> str:
    """Convert blockquote-wrapped code blocks to normal code blocks.

    Handles:
    - > ```lang ... > ``` (normal case)
    - > ```lang ... (missing closing fence — auto-close before next non-blockquote)
    - Preserves inner content exactly (no > prefix)
    """
    lines = md_text.split('\n')
    result = []
    in_bq_code = False
    fence_lang = ""

    for i, line in enumerate(lines):
        stripped = line.lstrip()

        if in_bq_code:
            # Check for closing fence: > ``` (only backticks, no language)
            if re.match(r'^>\s*```\s*$', stripped):
                in_bq_code = False
                result.append('```')
                continue

            # Check for missing closing fence:
            # Next line is non-empty and not a blockquote
            if i + 1 < len(lines):
                next_line = lines[i + 1]
                next_stripped = next_line.lstrip()
                if (next_stripped
                        and not next_stripped.startswith('>')
                        and not re.match(r'^```', next_stripped)):
                    # Missing closing fence — auto-close
                    in_bq_code = False
                    result.append('```')

            # Strip the > prefix from code content
            if stripped.startswith('>'):
                content = line[1:]  # remove first >
                if content.startswith(' '):
                    content = content[1:]  # remove one space after >
                result.append(content)
            else:
                # Empty line or no > prefix inside blockquote code block
                result.append(line)
            continue

        # Check for opening fence: > ```lang
        m = re.match(r'^>\s*```(\w*)', stripped)
        if m:
            in_bq_code = True
            fence_lang = m.group(1)
            result.append(f'```{fence_lang}')
            continue

        result.append(line)

    # Unclosed blockquote code block at end of file
    if in_bq_code:
        result.append('```')

    return '\n'.join(result)


def preprocess_math(md_text: str) -> tuple:
    r"""Replace LaTeX math expressions with placeholders to protect from parser.

    Handles: $$...$$ (block), \(...\) (inline), $...$ (inline).
    Skips content inside fenced code blocks.
    Returns (processed_text, math_blocks, math_inlines).
    """
    math_blocks = []
    math_inlines = []

    lines = md_text.split('\n')
    result = []
    in_code_block = False
    in_block_math = False
    block_math_buf = []

    for line in lines:
        # Track code block boundaries
        if re.match(r'^`{3,}', line.lstrip()):
            if in_code_block:
                in_code_block = False
            else:
                in_code_block = True
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Block math: $$ on its own line
        if not in_block_math:
            stripped = line.strip()
            if stripped == '$$':
                in_block_math = True
                block_math_buf = []
                continue
            # Single-line $$...$$
            if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
                idx = len(math_blocks)
                math_blocks.append(stripped[2:-2].strip())
                result.append(MATH_BLOCK_PLACEHOLDER.format(idx=idx))
                continue

        if in_block_math:
            stripped = line.strip()
            if stripped == '$$':
                in_block_math = False
                idx = len(math_blocks)
                math_blocks.append('\n'.join(block_math_buf))
                result.append(MATH_BLOCK_PLACEHOLDER.format(idx=idx))
                continue
            block_math_buf.append(line)
            continue

        # Inline math: \(...\)
        processed = line
        def replace_inline(m):
            idx = len(math_inlines)
            math_inlines.append(m.group(1))
            return MATH_INLINE_PLACEHOLDER.format(idx=idx)
        processed = re.sub(r'\\\((.+?)\\\)', replace_inline, processed)

        # Inline math: $...$ (but not $$)
        def replace_dollar(m):
            idx = len(math_inlines)
            math_inlines.append(m.group(1))
            return MATH_INLINE_PLACEHOLDER.format(idx=idx)
        processed = re.sub(r'(?<!\$)\$(?!\$)([^\$\n]+?)\$(?!\$)', replace_dollar, processed)

        result.append(processed)

    # Unclosed block math at end of file
    if in_block_math and block_math_buf:
        idx = len(math_blocks)
        math_blocks.append('\n'.join(block_math_buf))
        result.append(MATH_BLOCK_PLACEHOLDER.format(idx=idx))

    return '\n'.join(result), math_blocks, math_inlines


def preprocess_mermaid(md_text: str) -> str:
    """Extract mermaid code blocks and replace with <div class='mermaid'>.

    Handles both:
    - Normal: ```mermaid ... ```
    - Blockquote-wrapped: > ```mermaid ... > ```

    Runs BEFORE blockquote code block preprocessing so that
    > ```markdown > ```mermaid ... > ``` is NOT matched
    (the opening is ```markdown, not ```mermaid).
    """
    def replace_mermaid_blockquote(m):
        code = m.group(1)
        code_lines = code.split('\n')
        cleaned = []
        for line in code_lines:
            if line.lstrip().startswith('>'):
                content = line[1:]
                if content.startswith(' '):
                    content = content[1:]
                cleaned.append(content)
            else:
                cleaned.append(line)
        return f'<div class="mermaid">\n{chr(10).join(cleaned)}\n</div>'

    def replace_mermaid_normal(m):
        code = m.group(1)
        return f'<div class="mermaid">\n{code}\n</div>'

    # First: blockquote-wrapped mermaid (> ```mermaid ... > ```)
    md_text = re.sub(
        r'^>\s*```mermaid\s*\n(.*?)^>\s*```\s*$',
        replace_mermaid_blockquote,
        md_text,
        flags=re.DOTALL | re.MULTILINE,
    )

    # Then: normal mermaid (```mermaid ... ```)
    md_text = re.sub(
        r'```mermaid\s*\n(.*?)```',
        replace_mermaid_normal,
        md_text,
        flags=re.DOTALL,
    )

    return md_text


def preprocess_image_paths(md_text: str) -> str:
    """Normalize Windows backslash paths in image/link references."""
    # Fix backslash in markdown image/link paths: ![...](path\to\file) -> ![...](path/to/file)
    md_text = re.sub(
        r'(!?\[[^\]]*\]\([^\)]*)\\([^\)]*\))',
        lambda m: m.group(1) + '/' + m.group(2),
        md_text,
    )
    # Repeat when backslashes remain
    for _ in range(5):
        prev = md_text
        md_text = re.sub(
            r'(!?\[[^\]]*\]\([^\)]*)\\([^\)]*\))',
            lambda m: m.group(1) + '/' + m.group(2),
            md_text,
        )
        if md_text == prev:
            break
    return md_text


def postprocess_math(html: str, math_blocks: list, math_inlines: list) -> str:
    """Replace math placeholders with KaTeX-compatible HTML."""
    for idx, expr in enumerate(math_blocks):
        placeholder = MATH_BLOCK_PLACEHOLDER.format(idx=idx)
        # Escape HTML entities in math expression
        expr_html = (expr
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))
        html = html.replace(
            placeholder,
            f'<div class="math-block">\\[{expr_html}\\]</div>',
        )

    for idx, expr in enumerate(math_inlines):
        placeholder = MATH_INLINE_PLACEHOLDER.format(idx=idx)
        expr_html = (expr
                     .replace('&', '&amp;')
                     .replace('<', '&lt;')
                     .replace('>', '&gt;'))
        html = html.replace(
            placeholder,
            f'<span class="math-inline">\\({expr_html}\\)</span>',
        )

    return html


def preprocess_strikethrough(md_text: str) -> str:
    """Convert ~~text~~ to <del>text</del>."""
    return re.sub(r'~~(.+?)~~', r'<del>\1</del>', md_text)


def preprocess_blank_lines(md_text: str) -> str:
    """Insert blank lines before lists/tables that directly follow other content.

    Markdown requires a blank line before a list or table to recognize it as
    a block-level element. Without it, the parser merges them into the
    preceding paragraph.
    """
    lines = md_text.split('\n')
    result = []
    in_code_block = False

    for i, line in enumerate(lines):
        stripped = line.lstrip()

        # Track code block boundaries
        if re.match(r'^`{3,}', stripped):
            in_code_block = not in_code_block
            result.append(line)
            continue

        if in_code_block:
            result.append(line)
            continue

        # Skip lines inside blockquotes (they have their own parsing rules)
        if stripped.startswith('>'):
            result.append(line)
            continue

        # Check if current line starts a list or table
        is_list = re.match(r'^[-*+]\s', stripped)
        is_table = re.match(r'^\|', stripped)

        if (is_list or is_table) and result:
            prev = result[-1]
            # If previous line is non-empty and not a list/table/blockquote, insert blank line
            if (prev.strip()
                    and not re.match(r'^[-*+]\s', prev.lstrip())
                    and not re.match(r'^\|', prev.lstrip())
                    and not prev.lstrip().startswith('>')):
                result.append('')

        result.append(line)

    return '\n'.join(result)


def preprocess(md_text: str) -> tuple:
    """Run all preprocessing steps in order. Returns (text, math_blocks, math_inlines)."""
    md_text = preprocess_image_paths(md_text)
    md_text = preprocess_mermaid(md_text)  # Before blockquote: match > ```mermaid
    md_text = preprocess_blockquote_codeblocks(md_text)
    md_text = preprocess_blank_lines(md_text)
    md_text, math_blocks, math_inlines = preprocess_math(md_text)
    md_text = preprocess_strikethrough(md_text)
    return md_text, math_blocks, math_inlines


TEMPLATE = """\
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>{title} - floaritay</title>
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Outfit:wght@300;400;500;600;700&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet" />
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.css" />
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/katex.min.js"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/contrib/auto-render.min.js"
        onload="renderMathInElement(document.body, {{
            delimiters: [
                {{left: '$$', right: '$$', display: true}},
                {{left: '\\\\(', right: '\\\\)', display: false}},
                {{left: '\\\\[', right: '\\\\]', display: true}}
            ]
        }});"></script>
    <script defer src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"
        onload="mermaid.initialize({{startOnLoad:true, theme:'base', themeVariables:{{primaryColor:'#f5f0e8', primaryTextColor:'#1a1814', primaryBorderColor:'rgba(26,24,20,0.12)', lineColor:'#8a8278', secondaryColor:'#faf7f0', tertiaryColor:'#faf7f0'}}}});"></script>
    <style>
        :root {{
            --paper: #f5f0e8;
            --ink: #1a1814;
            --ink-soft: #3d3830;
            --ink-muted: #8a8278;
            --ink-faint: #b5ae9f;
            --accent: #b45309;
            --accent-warm: #d97706;
            --accent-soft: rgba(180, 83, 9, 0.08);
            --teal: #0f766e;
            --card-opaque: rgba(250, 247, 240, 0.88);
            --border: rgba(26, 24, 20, 0.08);
            --border-strong: rgba(26, 24, 20, 0.12);
            --glass-border: rgba(255, 255, 255, 0.35);
            --shadow-sm: 0 1px 2px rgba(26, 24, 20, 0.03);
            --shadow: 0 2px 12px rgba(26, 24, 20, 0.05), 0 1px 3px rgba(26, 24, 20, 0.03);
            --shadow-lg: 0 8px 32px rgba(26, 24, 20, 0.07), 0 2px 8px rgba(26, 24, 20, 0.03);
            --font-display: 'Instrument Serif', Georgia, serif;
            --font-body: 'Outfit', -apple-system, BlinkMacSystemFont, sans-serif;
            --font-mono: 'Space Mono', 'Cascadia Code', monospace;
            --radius: 12px;
            --radius-sm: 8px;
            --radius-lg: 16px;
        }}

        *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
        html {{ scroll-behavior: smooth; }}

        body {{
            font-family: var(--font-body);
            color: var(--ink);
            background: var(--paper);
            background-image:
                radial-gradient(ellipse 80% 60% at 20% 10%, rgba(180, 83, 9, 0.04), transparent),
                radial-gradient(ellipse 60% 50% at 80% 80%, rgba(15, 118, 110, 0.03), transparent);
            line-height: 1.65;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            overflow-x: hidden;
            min-height: 100vh;
        }}

        body::before {{
            content: '';
            position: fixed;
            inset: 0;
            pointer-events: none;
            z-index: 9999;
            opacity: 0.2;
            background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 200 200' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.06'/%3E%3C/svg%3E");
            mix-blend-mode: multiply;
        }}

        ::-webkit-scrollbar {{ width: 6px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{ background: rgba(26, 24, 20, 0.12); border-radius: 3px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: rgba(26, 24, 20, 0.2); }}

        .page {{
            position: relative;
            max-width: 820px;
            margin: 0 auto;
            padding: 0 32px 80px;
        }}

        .page::before {{
            content: '';
            position: fixed;
            left: 0;
            top: 0;
            bottom: 0;
            width: 48px;
            background: var(--card-opaque);
            border-right: 1px solid var(--border);
            z-index: 100;
        }}

        @media (max-width: 1100px) {{
            .page::before {{ display: none; }}
            .page {{ padding: 0 20px 60px; }}
        }}

        /* Breadcrumb */
        .breadcrumb {{
            padding: 32px 0 16px;
            font-family: var(--font-body);
            font-size: 0.85rem;
            color: var(--ink-muted);
            letter-spacing: 0.02em;
        }}
        .breadcrumb a {{
            color: var(--ink-muted);
            text-decoration: none;
            transition: color 0.2s;
        }}
        .breadcrumb a:hover {{ color: var(--accent); }}
        .breadcrumb .sep {{ margin: 0 8px; color: var(--ink-faint); }}

        /* Article */
        .markdown-body {{
            font-family: var(--font-body);
            color: var(--ink-soft);
            font-size: 1.05rem;
            line-height: 1.8;
        }}

        .markdown-body h1, .markdown-body h2, .markdown-body h3,
        .markdown-body h4, .markdown-body h5, .markdown-body h6 {{
            font-family: var(--font-display);
            color: var(--ink);
            font-weight: 400;
            margin-top: 2em;
            margin-bottom: 0.6em;
            line-height: 1.3;
        }}

        .markdown-body h1 {{
            font-size: 2.2rem;
            margin-top: 0;
            padding-bottom: 0.4em;
            border-bottom: 1px solid var(--border);
        }}

        .markdown-body h2 {{
            font-size: 1.65rem;
            padding-bottom: 0.3em;
            border-bottom: 1px solid var(--border);
        }}

        .markdown-body h3 {{ font-size: 1.35rem; }}
        .markdown-body h4 {{ font-size: 1.15rem; }}
        .markdown-body h5 {{ font-size: 1rem; }}
        .markdown-body h6 {{ font-size: 0.95rem; color: var(--ink-muted); }}

        .markdown-body p {{
            margin-bottom: 1em;
        }}

        .markdown-body a {{
            color: var(--accent);
            text-decoration: none;
            border-bottom: 1px solid var(--accent-soft);
            transition: border-color 0.2s;
        }}
        .markdown-body a:hover {{
            border-bottom-color: var(--accent);
        }}

        .markdown-body strong {{ color: var(--ink); font-weight: 600; }}

        .markdown-body img {{
            max-width: 100%;
            height: auto;
            display: block;
            margin: 1.5em auto;
            border-radius: var(--radius);
            box-shadow: var(--shadow);
        }}

        .markdown-body blockquote {{
            margin: 1.2em 0;
            padding: 0.8em 1.2em;
            border-left: 3px solid var(--accent);
            background: var(--accent-soft);
            border-radius: 0 var(--radius-sm) var(--radius-sm) 0;
            color: var(--ink-soft);
        }}
        .markdown-body blockquote p:last-child {{ margin-bottom: 0; }}

        .markdown-body ul, .markdown-body ol {{
            margin: 0.8em 0;
            padding-left: 1.8em;
        }}
        .markdown-body li {{ margin-bottom: 0.3em; }}
        .markdown-body li > ul, .markdown-body li > ol {{ margin-top: 0.3em; }}

        .markdown-body code {{
            font-family: var(--font-mono);
            font-size: 0.88em;
            background: rgba(26, 24, 20, 0.05);
            padding: 0.15em 0.4em;
            border-radius: var(--radius-sm);
            color: var(--accent);
        }}

        .markdown-body pre {{
            margin: 1.2em 0;
            padding: 1em 1.2em;
            background: #2d2a24;
            border-radius: var(--radius);
            overflow-x: auto;
            box-shadow: var(--shadow);
        }}
        .markdown-body pre code {{
            background: none;
            padding: 0;
            color: #e8e0d4;
            font-size: 0.85rem;
            line-height: 1.6;
        }}

        .markdown-body table {{
            width: 100%;
            border-collapse: collapse;
            margin: 1.2em 0;
            font-size: 0.95rem;
        }}
        .markdown-body th {{
            background: rgba(26, 24, 20, 0.04);
            font-weight: 600;
            text-align: left;
            padding: 0.6em 1em;
            border-bottom: 2px solid var(--border-strong);
        }}
        .markdown-body td {{
            padding: 0.5em 1em;
            border-bottom: 1px solid var(--border);
        }}
        .markdown-body tr:hover td {{
            background: var(--accent-soft);
        }}

        .markdown-body hr {{
            border: none;
            border-top: 1px solid var(--border-strong);
            margin: 2em 0;
        }}

        /* Math blocks */
        .math-block {{
            margin: 1.2em 0;
            padding: 0.8em;
            overflow-x: auto;
            text-align: center;
        }}

        /* Mermaid diagrams */
        .mermaid {{
            margin: 1.5em 0;
            text-align: center;
            overflow-x: auto;
        }}
        .mermaid svg {{
            max-width: 100%;
            height: auto;
        }}

        /* Pygments code highlighting (dark theme matching warm palette) */
        .highlight .hll {{ background-color: #49483e }}
        .highlight .c {{ color: #75715e }}
        .highlight .err {{ color: #f92672 }}
        .highlight .k {{ color: #66d9ef }}
        .highlight .l {{ color: #ae81ff }}
        .highlight .n {{ color: #f8f8f2 }}
        .highlight .o {{ color: #f92672 }}
        .highlight .p {{ color: #f8f8f2 }}
        .highlight .cm {{ color: #75715e }}
        .highlight .c1 {{ color: #75715e }}
        .highlight .cp {{ color: #75715e }}
        .highlight .kc {{ color: #66d9ef }}
        .highlight .kd {{ color: #66d9ef }}
        .highlight .kn {{ color: #f92672 }}
        .highlight .kp {{ color: #66d9ef }}
        .highlight .kr {{ color: #66d9ef }}
        .highlight .kt {{ color: #66d9ef }}
        .highlight .ld {{ color: #e6db74 }}
        .highlight .m {{ color: #ae81ff }}
        .highlight .s {{ color: #e6db74 }}
        .highlight .na {{ color: #a6e22e }}
        .highlight .nb {{ color: #f8f8f2 }}
        .highlight .nc {{ color: #a6e22e }}
        .highlight .no {{ color: #66d9ef }}
        .highlight .nd {{ color: #a6e22e }}
        .highlight .ni {{ color: #f8f8f2 }}
        .highlight .ne {{ color: #a6e22e }}
        .highlight .nf {{ color: #a6e22e }}
        .highlight .nl {{ color: #f8f8f2 }}
        .highlight .nn {{ color: #f8f8f2 }}
        .highlight .nx {{ color: #a6e22e }}
        .highlight .py {{ color: #f8f8f2 }}
        .highlight .nt {{ color: #f92672 }}
        .highlight .nv {{ color: #f8f8f2 }}
        .highlight .ow {{ color: #f92672 }}
        .highlight .w {{ color: #f8f8f2 }}
        .highlight .mf {{ color: #ae81ff }}
        .highlight .mh {{ color: #ae81ff }}
        .highlight .mi {{ color: #ae81ff }}
        .highlight .mo {{ color: #ae81ff }}
        .highlight .sb {{ color: #e6db74 }}
        .highlight .sc {{ color: #e6db74 }}
        .highlight .sd {{ color: #e6db74 }}
        .highlight .s2 {{ color: #e6db74 }}
        .highlight .se {{ color: #ae81ff }}
        .highlight .sh {{ color: #e6db74 }}
        .highlight .si {{ color: #e6db74 }}
        .highlight .sx {{ color: #e6db74 }}
        .highlight .sr {{ color: #e6db74 }}
        .highlight .s1 {{ color: #e6db74 }}
        .highlight .ss {{ color: #e6db74 }}
        .highlight .bp {{ color: #f8f8f2 }}
        .highlight .vc {{ color: #f8f8f2 }}
        .highlight .vg {{ color: #f8f8f2 }}
        .highlight .vi {{ color: #f8f8f2 }}
        .highlight .il {{ color: #ae81ff }}

        /* Footer */
        .site-footer {{
            text-align: center;
            padding: 32px 0;
            font-size: 0.8rem;
            color: var(--ink-faint);
            border-top: 1px solid var(--border);
            margin-top: 40px;
        }}
        .site-footer a {{
            color: var(--ink-muted);
            text-decoration: none;
        }}
        .site-footer a:hover {{ color: var(--accent); }}

        /* Back to top button */
        .back-to-top {{
            position: fixed;
            bottom: 32px;
            right: 32px;
            width: 40px;
            height: 40px;
            border: 1px solid var(--border-strong);
            border-radius: var(--radius-sm);
            background: var(--card-opaque);
            backdrop-filter: blur(16px);
            color: var(--ink-muted);
            font-size: 1.1rem;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s, color 0.2s, border-color 0.2s;
            z-index: 200;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .back-to-top:hover {{
            color: var(--accent);
            border-color: var(--accent);
        }}

        @media (max-width: 768px) {{
            .page {{ padding: 0 16px 40px; }}
            .markdown-body h1 {{ font-size: 1.7rem; }}
            .markdown-body h2 {{ font-size: 1.35rem; }}
            .markdown-body {{ font-size: 0.95rem; }}
            .markdown-body pre {{ padding: 0.8em; }}
            .markdown-body pre code {{ font-size: 0.8rem; }}
            .back-to-top {{ bottom: 20px; right: 20px; }}
        }}
    </style>
</head>
<body>
    <div class="page">
        <nav class="breadcrumb">
            <a href="{home_link}">floaritay</a>
            <span class="sep">/</span>
            <span>{category}</span>
        </nav>
        <article class="markdown-body">
{content}
        </article>
        <footer class="site-footer">
            <a href="{home_link}">&larr; 返回首页</a>
        </footer>
    </div>
    <button class="back-to-top" id="backToTop" title="回到顶部">&uarr;</button>
    <script>
        const btn = document.getElementById('backToTop');
        window.addEventListener('scroll', () => {{
            btn.style.opacity = window.scrollY > 300 ? '1' : '0';
        }});
        btn.addEventListener('click', () => {{
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }});
    </script>
</body>
</html>
"""


def extract_title(md_text: str) -> str:
    """Extract the first H1 heading from markdown text."""
    m = re.search(r"^#\s+(.+)$", md_text, re.MULTILINE)
    if m:
        return m.group(1).strip()
    return ""


def rewrite_md_links(html: str) -> str:
    """Rewrite .md links in generated HTML to .html links."""
    return re.sub(r'href="([^"]*?)\.md"', r'href="\1.html"', html)


def fix_heading_ids(html: str) -> str:
    """Fix heading IDs to match TOC anchor links.

    The markdown library strips Chinese characters from auto-generated heading IDs,
    but hand-written TOC links preserve them (e.g., #1-介绍 vs #1).
    This function collects all anchor targets from links, finds the matching
    headings by text content, and updates their IDs.
    """
    # Collect all anchor targets from <a href="#..."> links
    anchor_targets = {}
    for m in re.finditer(r'<a href="#([^"]+)">([^<]+)</a>', html):
        anchor_id, link_text = m.group(1), m.group(2).strip()
        anchor_targets[link_text] = anchor_id

    # Build a case-insensitive lookup for heading ID matching
    # Map lowercase ID -> actual ID from anchors
    anchor_id_lower = {}
    for text, aid in anchor_targets.items():
        anchor_id_lower[aid.lower()] = aid

    # Find all headings and fix their IDs
    def fix_heading(m):
        tag = m.group(1)  # h1, h2, etc.
        attrs = m.group(2)  # everything between <h and >
        text = m.group(3)  # heading text content

        # Get current heading ID
        id_match = re.search(r'id="([^"]*)"', attrs)
        if not id_match:
            return m.group(0)
        current_id = id_match.group(1)

        # Strategy 1: Match by heading text content
        clean_text = re.sub(r'<[^>]+>', '', text).strip()
        if clean_text in anchor_targets:
            target_id = anchor_targets[clean_text]
            new_attrs = re.sub(r'id="[^"]*"', f'id="{target_id}"', attrs)
            return f'<{tag}{new_attrs}>{text}</{tag}>'

        # Strategy 2: Case-insensitive ID match
        if current_id.lower() in anchor_id_lower:
            target_id = anchor_id_lower[current_id.lower()]
            if target_id != current_id:
                new_attrs = re.sub(r'id="[^"]*"', f'id="{target_id}"', attrs)
                return f'<{tag}{new_attrs}>{text}</{tag}>'

        return m.group(0)

    html = re.sub(
        r'<(h[1-6])([^>]*)>(.+?)</\1>',
        fix_heading,
        html,
        flags=re.DOTALL,
    )
    return html


def convert_file(md_path: Path) -> None:
    """Convert a single .md file to .html."""
    md_text = md_path.read_text(encoding="utf-8")

    # Preprocess: fix blockquote codeblocks, protect math, extract mermaid
    md_text, math_blocks, math_inlines = preprocess(md_text)

    html_body = markdown.markdown(
        md_text,
        extensions=["fenced_code", "tables", "toc", "codehilite", "attr_list", "md_in_html"],
        extension_configs={
            "codehilite": {
                "guess_lang": True,
                "css_class": "highlight",
            }
        },
        tab_length=2,
    )

    # Postprocess: restore math placeholders with KaTeX delimiters
    html_body = postprocess_math(html_body, math_blocks, math_inlines)

    # Rewrite internal .md links to .html
    html_body = rewrite_md_links(html_body)

    # Fix heading IDs to match TOC anchor links
    html_body = fix_heading_ids(html_body)

    title = extract_title(md_text) or md_path.stem
    category = md_path.parent.name if md_path.parent != DOCS_DIR else "笔记"

    # Compute relative path back to docs/index.html
    depth = len(md_path.relative_to(DOCS_DIR).parts) - 1
    home_link = "../" * depth + "index.html"

    html_content = TEMPLATE.format(
        title=title,
        category=category,
        home_link=home_link,
        content=html_body,
    )

    html_path = md_path.with_suffix(".html")
    html_path.write_text(html_content, encoding="utf-8")
    print(f"  {md_path.relative_to(DOCS_DIR)} -> {html_path.relative_to(DOCS_DIR)}")


def main():
    print(f"Converting .md files in {DOCS_DIR} ...\n")
    count = 0
    for md_file in sorted(DOCS_DIR.rglob("*.md")):
        convert_file(md_file)
        count += 1
    print(f"\nDone. Converted {count} files.")


if __name__ == "__main__":
    main()
