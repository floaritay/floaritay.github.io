---
name: md2html
description: 将 docs/ 目录下的 Markdown（.md）文件转换为带样式的 HTML（.html）页面。当用户提到"md转html"、"markdown转html"、"生成html"、"更新html页面"、"转换笔记页面"、"md2html"等关键词时触发。
argument-hint: [file-or-directory]
---

# Markdown 转 HTML

将 `docs/` 目录下的 `.md` 文件转换为带样式的 `.html` 页面，支持数学公式、Mermaid 图表、代码高亮等。

## 执行步骤

1. 运行转换脚本：`python .claude/skills/md2html/md2html.py`
2. 脚本会遍历 `docs/**/*.md`，为每个 `.md` 文件生成同目录下的 `.html`
3. 显示转换结果

## 内置脚本说明

### .claude/skills/md2html/md2html.py

核心转换脚本，处理以下问题：

**预处理（按顺序执行）：**
1. **图片路径规范化** — Windows 反斜杠 `\` 转正斜杠 `/`
2. **Mermaid 图表提取** — `> ```mermaid ... > ``` ` 转为 `<div class="mermaid">`
3. **引用代码块** — `> ```lang ... > ``` ` 去掉 `>` 前缀，转为正常代码块；自动补全缺失的闭合围栏
4. **空行插入** — 列表/表格前缺少空行时自动插入（markdown 解析器需要空行才能识别块级元素）
5. **数学公式保护** — `$$...$$`、`\(...\)`、`$...$` 替换为占位符，跳过代码块内的公式
6. **删除线** — `~~text~~` 转为 `<del>text</del>`

**后处理：**
- 数学占位符恢复为 KaTeX 格式（`\[...\]` 和 `\(...\)`）
- `.md` 内部链接重写为 `.html`
- 标题 ID 修正 — 匹配 TOC 锚点链接（解决中文字符被剥离的问题）

**HTML 模板特性：**
- 复用主页 CSS 变量（`--paper`, `--ink`, `--accent` 等）
- KaTeX 数学公式渲染（CDN）
- Mermaid 图表渲染（CDN）
- Pygments 代码语法高亮（深色主题）
- 面包屑导航 + 回到顶部按钮
- 响应式设计

**使用的 Python 扩展：**
- `markdown` — 核心转换（fenced_code, tables, toc, codehilite, attr_list, md_in_html）
- `pygments` — 代码语法高亮

## 路径映射

| 源文件 | 生成文件 |
|---|---|
| `docs/Agent/Agent.md` | `docs/Agent/Agent.html` |
| `docs/FastAPI.md` | `docs/FastAPI.html` |
| `docs/basic/Git.md` | `docs/basic/Git.html` |

生成的 `.html` 文件由 GitHub Actions 在部署时自动创建，不提交到仓库（已在 `.gitignore` 中排除）。

## 使用方法

```bash
# 转换所有 .md 文件
python .claude/skills/md2html/md2html.py

# CI/CD 中自动执行（.github/workflows/deploy.yml）
pip install markdown==3.10 pygments==2.19.2
python .claude/skills/md2html/md2html.py
```

## 注意事项

- 只处理 `docs/` 目录下的 `.md` 文件，不处理根目录的原始笔记
- `docs/index.html` 是主页，不被脚本修改
- 代码块内的 `$$`、`\(` 等不会被误识别为数学公式
- `> ```markdown > ```mermaid ... > ``` ` 会被保留为代码示例（不会渲染为图表）
- `> ```mermaid ... > ``` ` 会被提取并渲染为实际的 Mermaid 图表

## 经验教训

- Python `markdown` 库默认需要 4 空格缩进才能识别嵌套列表，设置 `tab_length=2` 兼容 2 空格缩进
- `> ```mermaid` 必须在 `> ```markdown` 之前处理，否则会被误认为内层围栏
- 数学公式占位符必须在代码块围栏检测之后处理，否则代码块内的 `$$` 会被误识别
- 标题 ID 中的中文字符会被 markdown 库剥离，需要后处理修正以匹配 TOC 锚点
