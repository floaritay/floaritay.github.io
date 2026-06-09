# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal blog and learning notes repository (floaritay) containing technical notes on programming, machine learning, deep learning, computer vision, robotics, and more. Content is written in Chinese (zh-CN).

## Repository Structure

- `docs/` - Main blog site with Markdown files; `docs/index.html` is the entry point
- Topic directories (Agent, CV, DeepLearing, machine_learning, NLP, ROS, SQL, python, etc.) - Source Jupyter notebooks and Python scripts
- `docs/images/` - Shared image assets referenced by notebooks via `../docs/images/`
- `.github/workflows/deploy.yml` - GitHub Pages deployment

## Build and Deploy

Notebooks are converted to Markdown using **nbconvert** and deployed to GitHub Pages:

```bash
jupyter nbconvert --to markdown <notebook>.ipynb --output-dir docs/<category>/
```

The GitHub Actions workflow automatically deploys `docs/` to GitHub Pages on push to `main`.

## Content Workflow

1. Jupyter notebooks (`.ipynb`) in topic directories are the source content
2. Use `/nbconvert-md` skill to convert notebooks to Markdown with auto-generated TOC, output to corresponding `docs/` subdirectories
3. `docs/index.html` is a custom navigation page (not auto-generated) that links to all notes

## Key Files

- `docs/index.html` - Custom blog homepage with module navigation (intro, projects, notes), skill cards, and note search/filter
- `docs/images/` - Shared images; notebooks reference them with `../docs/images/` paths
- `.nojekyll` - Present to disable Jekyll processing on GitHub Pages
