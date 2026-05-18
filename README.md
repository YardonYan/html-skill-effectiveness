# HTML Effectiveness Skill

[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE.txt)
[![GitHub Stars](https://img.shields.io/github/stars/YardonYan/html-skill-effectiveness?style=social)](https://github.com/YardonYan/html-skill-effectiveness)
[![GitHub repo](https://img.shields.io/badge/GitHub-YardonYan%2Fhtml--skill--effectiveness-181717?logo=github)](https://github.com/YardonYan/html-skill-effectiveness)

> 让 AI 生成的不再是"扫一眼就跳过"的文档，而是"真正愿意读"的交互式 HTML 页面。

**作者**: [Yardon](https://github.com/YardonYan) | **创作时间**: 2026年5月  
**基于开源项目**: [The Unreasonable Effectiveness of HTML](https://github.com/ThariqS/html-effectiveness) by ThariqS

---

## Overview

What if your AI stopped writing walls of markdown and started producing things you'd actually *read*?

This skill guides AI assistants to create **self-contained, single-file HTML artifacts** that are visually polished, interactive, and designed for real human consumption. Every artifact is one HTML file with inline CSS and JavaScript — zero dependencies, no build step, open directly in a browser.

### Why HTML beats Markdown

| | Markdown | HTML |
|---|---|---|
| **Layout** | Linear, sequential | Spatial, multi-column, responsive |
| **Tables** | Basic pipes | Sortable, filterable, styled |
| **Charts** | ❌ None | SVG, canvas, CSS-only charts |
| **Interactivity** | ❌ None | Forms, sliders, drag-drop, toggle switches |
| **Code display** | Monospace block | Syntax highlighting, line numbers, diff colors |
| **Typography** | Limited | Kerning, leading, font stacks, ligatures |
| **Space** | Pure text | Whitespace, hierarchy, visual grouping |

---

## Features

- **11 Design Patterns** — From side-by-side comparisons to interactive dashboards
- **Self-Contained** — Every artifact is one HTML file with inline CSS and JavaScript
- **Zero Dependencies** — No build step, no CDN, no external files
- **Warm Editorial Design** — Carefully crafted color palette and typography system
- **Responsive** — Works on desktop, tablet, and mobile
- **Accessible** — Semantic HTML, keyboard navigation, color contrast compliant

---

## Pattern Catalog

| # | Pattern | Use Case |
|---|---------|----------|
| 1 | **Side-by-Side Comparison** | Compare approaches, designs, options |
| 2 | **Annotated Diff / Code Review** | PR reviews, before/after code changes |
| 3 | **Module Map / Architecture Diagram** | System architecture with interactive tooltips |
| 4 | **Living Design System** | Color palettes, typography scales, component catalogs |
| 5 | **Slide Deck** | Full-viewport presentations with scroll-snap navigation |
| 6 | **Interactive Explainer** | Teaching concepts with interactive demos |
| 7 | **Status / Incident Report** | Weekly updates, post-mortems, progress tracking |
| 8 | **Flowchart / Process Diagram** | Pipelines, decision trees, workflows |
| 9 | **SVG Illustration Sheet** | Blog diagrams, figures, icons |
| 10 | **Custom Editor / Triage Board** | Sorting, flag editing, prompt tuning |
| 11 | **Dashboard / Data Display** | Metrics, KPIs, monitoring views |

---

## Design System

### Color Palette

```css
:root {
  --ivory: #FAF9F5;   /* page background */
  --slate: #141413;   /* primary text, headings */
  --clay:  #D97757;   /* accent, links, CTAs */
  --oat:   #E3DACC;   /* secondary accent, borders */
  --olive: #788C5D;   /* success, positive states */
  --rust:  #B04A3F;   /* error, warning, destructive */
}
```

### Typography

| Element | Font Stack |
|---------|-----------|
| Headings | `ui-serif, Georgia, "Times New Roman", serif` |
| Body | `system-ui, -apple-system, "Segoe UI", Roboto, sans-serif` |
| Code | `ui-monospace, "SF Mono", Menlo, Monaco, monospace` |

### Spacing & Radius

- Card radius: `12px` / Pill radius: `999px`
- Border: `1.5px solid var(--g300)`
- Page padding: `56px 24px 96px`

---

## File Structure

```
html-effectiveness/
├── SKILL.md                          # Main skill definition (OpenClaw compatible)
├── README.md                         # This file — skill documentation
├── references/
│   ├── pattern-examples.md           # Code snippets by pattern (extracted from 20 examples)
│   └── complete-examples.md          # Full standalone HTML examples
├── indexxxxxxx_en.html               # English showcase page (keep untouched)
└── indexxxxxxx_zh.html               # Chinese showcase page (keep untouched)
```

---

## Installation

### OpenClaw

Copy this folder to your OpenClaw skills directory:
```bash
# Find your skills directory
openclaw config get workspace.skills.dir
# Copy the folder there
cp -r html-effectiveness /path/to/skills/
```

### Claude.ai / Claude Code

Follow the [Claude skill installation guide](https://support.claude.com/en/articles/12512180-using-skills-in-claude) to upload this skill.

---

## Usage Examples

Once installed, trigger the skill with requests like:

- "Generate a status report as HTML"
- "Make this comparison visual with HTML"
- "Create an interactive explainer for [concept]"
- "Build a slide deck about [topic]"
- "Design a triage board for these tickets"
- "Draw a flowchart of this process"
- "Show me component variants in HTML"
- "Create a dashboard for [metrics]"

---

## Pattern Quick Reference

| Pattern | Grid | Interactivity | Responsive |
|---------|------|---------------|------------|
| Comparison | `repeat(3, 1fr)` → 1 col | Hover lift | ✅ |
| Diff | 1 col + margin notes | Hover line highlight | ✅ |
| Module Map | SVG full-width | Click tooltips | ✅ |
| Design System | `auto-fill, minmax(120px, 1fr)` | Copy to clipboard | ✅ |
| Slide Deck | 100vw × 100vh | Keyboard nav | ✅ |
| Explainer | 1 col max-width 720px | Details/sliders/tabs | ✅ |
| Report | `auto-fill, minmax(260px, 1fr)` | Status pills | ✅ |
| Flowchart | SVG + side panel | Click nodes | ✅ |
| Illustrations | `auto-fill, minmax(200px, 1fr)` | Hover transform | ✅ |
| Editor | Drag columns | Drag-and-drop, export | ✅ |
| Dashboard | `auto-fill, minmax(260px, 1fr)` | Sparklines, delta | ✅ |

---

## Credits & License

This skill is built on the design pattern catalog and visual system from [**The Unreasonable Effectiveness of HTML**](https://github.com/ThariqS/html-effectiveness) by ThariqS, merged with the aesthetic philosophy from [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) by Anthropic.

- **Author**: [Yardon](https://github.com/YardonYan)
- **Created**: May 2026
- **License**: Apache 2.0 (see `LICENSE.txt`)

---

*"Trade documents people skim for documents people actually read."*
