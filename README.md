# html-effectiveness

> **Trade documents people skim for documents people actually read.**

A skill for generating beautiful, self-contained, single-file HTML artifacts. No build step. No dependencies. Open directly in a browser.

[![GitHub](https://img.shields.io/badge/GitHub-YardonYan%2Fhtml--skill--effectiveness-181717?logo=github)](https://github.com/YardonYan/html-effectiveness)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue)](LICENSE.txt)

---

## What This Is

AI defaults to Markdown. Markdown is linear text — great for reading sequentially, terrible for:

- Side-by-side comparisons
- Architecture diagrams  
- Interactive explainers
- Data dashboards
- Slide decks
- Code diffs with annotations

**HTML can do all of these.** This skill teaches AI how to generate them well.

Every artifact is:
- **Single file** — inline CSS and JavaScript, zero external dependencies
- **Self-contained** — open in any browser, no server needed
- **Visually polished** — design system, typography, spacing, color tokens
- **Pattern-based** — 13 proven patterns for common AI output scenarios

---

## What's New in v2.1

> "From generate once to generate, critique, refine, converge."

v2.1 introduces the **Critique Revolution** — the skill no longer just generates HTML and hopes for the best. It now systematically critiques its own output across 6 dimensions using radar chart visualization, band scoring (0-10), and evidence-cited judgments, then iterates via a **DevLoop** until quality converges (score ≥ 4). This is powered by deep integration with **open-design-main**'s critique framework and **html-ppt**'s 36-theme presentation system.

### New Features

- **Enhanced Critique System** — Radar chart visualization, band scoring (0-10), Keep/Fix/Quick-wins categorization with evidence-cited reasoning. No more vague "looks good" — every judgment is anchored to a specific dimension with concrete evidence.
- **DevLoop: Iterative Self-Improvement** — critique → fix → repeat until score ≥ 4. The skill now converges on quality through structured iteration, not one-shot generation.
- **2 New Patterns** — Live Artifact Dashboard (#12) with template+data+artifact+provenance workflow, and Frame Effects (#13) for cinematic visual moments (glitch titles, liquid backgrounds, light leaks).
- **Enhanced PPT/Slide Pattern** — Now powered by 36 themes, 31 layout variants, 15 full-deck templates, 27 CSS animations, and 20 Canvas FX with presenter mode.
- **Scoring Discipline Rules** — Anti-inflation: no averaging across dimensions, no score inflation. Each dimension judged independently.
- **Critique Report Output Contract** — Standardized critique report format with radar chart, band summary, evidence table, and actionable Keep/Fix/Quick-wins.

---

## Installation

### For OpenClaw

```bash
# Copy to your workspace skills directory
cp -r html-skill-effectiveness ~/.qclaw/skills/
```

Or use the SkillHub:
```bash
openclaw skill install html-effectiveness
```

### For Claude (Claude Code)

```bash
# Copy to Claude skills directory
cp -r html-skill-effectiveness ~/.claude/skills/
```

---

## Pattern Catalog

| # | Pattern | Use For |
|---|---------|---------|
| 1 | **Side-by-Side Comparison** | Tech choices, design options, trade-offs |
| 2 | **Annotated Diff** | PR reviews, code changes, before/after |
| 3 | **Module Map** | Architecture diagrams, data flow |
| 4 | **Living Design System** | Color palettes, typography, component catalogs |
| 5 | **Slide Deck** | Presentations, walkthroughs, demos |
| 6 | **Interactive Explainer** | Teaching concepts, documentation |
| 7 | **Status Report** | Weekly updates, incident reports |
| 8 | **Flowchart** | Pipelines, decision trees, workflows |
| 9 | **SVG Illustration** | Blog diagrams, figures, icons |
| 10 | **Custom Editor** | Triage boards, prompt tuning, configuration |
| 11 | **Dashboard** | Metrics, KPIs, monitoring views |
| 12 | **Live Artifact Dashboard** | Refreshable dashboards with template+data architecture |
| 13 | **Frame Effects** | Cinematic visual moments: glitch titles, liquid backgrounds, light leaks |

---

## Design System

### Core Tokens (6 variables)

```css
:root {
  --bg:      #fafaf7;   /* page background */
  --surface: #ffffff;   /* cards, panels */
  --fg:      #1a1916;   /* primary text */
  --muted:   #6b6964;   /* secondary text */
  --border:  #e8e5df;   /* dividers */
  --accent:  #c96442;   /* one accent, max 2× per screen */
}
```

Everything else derives from these via `color-mix()`. No raw hex outside `:root`.

### Typography

| Element | Font | Size |
|---------|------|------|
| H1 | Display serif | clamp(44px, 6vw, 76px) |
| H2 | Display serif | clamp(32px, 4vw, 48px) |
| Body | System sans | 16px |
| Code | Mono | 13px |
| Eyebrow | Mono | 11px, uppercase |

**No Inter/Roboto/Arial as display fonts.** Choose distinctive, beautiful typefaces.

---

## Workflow

### Step 0 — Pre-flight
1. Read SKILL.md end-to-end
2. Understand user's intent (purpose, tone, audience, density)
3. Map to Pattern Catalog
4. Plan section list — state layout before writing

### Step 1 — Choose Aesthetic Direction
- Purpose, Tone, Constraints, Differentiation
- Pick an extreme: minimal, maximalist, retro, brutalist, luxury, playful...

### Step 2 — Write the Artifact
- Copy HTML Structure Template
- Define tokens in `:root`
- Build sections from Pattern Catalog
- Add minimal interaction (CSS-first)
- Tag sections with `data-od-id`

### Step 3 — Critique (NEW in v2.1)
- Run 6-Dimension Self-Critique with radar chart visualization
- Band scoring (0-10) per dimension with evidence-cited reasoning
- Generate Keep/Fix/Quick-wins report
- If any dimension < 4, enter DevLoop: fix → re-critique → repeat

### Step 4 — DevLoop (NEW in v2.1)
- Apply Keep items as-is
- Address Fix items systematically
- Consider Quick-wins for immediate impact
- Re-score after fixes; converge when all dimensions ≥ 4

### Step 5 — Emit
```
<artifact identifier="slug" type="text/html" title="Title">
<!doctype html>
<html>...</html>
</artifact>
```

---

## Quality Standards

### P0 — Must Never Happen
- No external CSS/JS files
- No CDN libraries
- No raw hex outside `:root`
- No purple/violet gradient backgrounds
- No emoji as feature icons
- No invented metrics
- No filler copy ("Feature One/Two")
- `data-od-id` on every `<section>`
- Mobile reflow works (≤920px)

### P1 — Should Avoid
- Walls of text
- Pure black/white
- Over-animation
- Generic AI aesthetics
- Inter/Roboto as display fonts
- Glassmorphism on KPI cards

### Scoring Discipline (NEW in v2.1)
- **No averaging**: each dimension scored independently
- **No inflation**: 7+ requires exceptional evidence
- **Evidence-cited**: every score must cite specific observations
- **Band interpretation**: 0-3 Critical / 4-6 Acceptable / 7-8 Strong / 9-10 Exceptional

---

## File Structure

```
html-skill-effectiveness/
├── SKILL.md                    # Core skill definition
├── README.md                   # This file
├── LICENSE.txt                 # Apache 2.0
├── BLOG.md                     # Detailed blog post
├── INTEGRATION_SUMMARY.md      # Version integration history
├── indexxxxxxx_en.html         # English showcase (20+ examples)
├── indexxxxxxx_zh.html         # Chinese showcase
└── references/
    ├── pattern-examples.md     # Code snippets by pattern
    ├── complete-examples.md    # Full HTML examples
    ├── critique-guide.md       # Complete critique system guide (NEW)
    └── frame-effects.md        # Frame Effects pattern reference (NEW)
```

---

## Example Prompts

- "Generate a status report as HTML"
- "Make this comparison visual with HTML"
- "Create an interactive explainer for [concept]"
- "Build a slide deck about [topic]"
- "Design a triage board for these tickets"
- "Draw a flowchart of this process"
- "Show me component variants in HTML"
- "Make this HTML prettier / more professional"
- "Create a dashboard for [metrics]"
- "Make a presentation with speaker notes"
- "Critique this HTML output and suggest improvements"
- "Add a live artifact dashboard with refreshable data"
- "Apply frame effects to make this page cinematic"

---

## Credits

- **Original concept**: [The Unreasonable Effectiveness of HTML](https://github.com/ThariqS/html-effectiveness) by Thariq Shihipar
- **Aesthetic philosophy**: [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) by Anthropic
- **Engineering rigor & critique system**: [open-design](https://github.com/opendesign) by OpenDesign — radar chart critique, band scoring, DevLoop convergence
- **PPT/Slide enhancement**: [html-ppt](https://github.com/opendesign) — 36 themes, 31 layouts, canvas FX, presenter mode
- **Integration & enhancement**: [Yardon](https://github.com/YardonYan)

---

## License

Apache 2.0 — see [LICENSE.txt](LICENSE.txt)