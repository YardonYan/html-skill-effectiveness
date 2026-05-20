---
name: html-effectiveness
author: Yardon (https://github.com/YardonYan)
description: |
  Generate beautiful, self-contained, single-file HTML artifacts that replace walls of markdown with interactive, visual documents. 
  Use when the user asks for HTML output, visual reports, interactive prototypes, slide decks, diagrams, dashboards, code comparisons, 
  design systems, status reports, incident timelines, flowcharts, or any document that would benefit from spatial layout, color, 
  typography hierarchy, interactivity, or visual structure over plain text. Also triggers when the user wants to improve AI-generated 
  HTML, make HTML prettier, optimize HTML presentation, or create HTML-based deliverables like explainer pages, feature comparisons, 
  triage boards, or prompt tuners.
license: Apache-2.0
created: 2026-05
updated: 2026-05-21
based-on:
  - The Unreasonable Effectiveness of HTML (https://github.com/ThariqS/html-effectiveness)
  - frontend-design by Anthropic (https://github.com/anthropics/skills/tree/main/skills/frontend-design)
  - open-design by OpenDesign (https://github.com/opendesign)
---

# HTML Effectiveness

## Overview

This skill guides the generation of single-file `.html` artifacts that are self-contained (no external dependencies), visually polished, and designed for human consumption. The core philosophy: **trade documents people skim for documents people actually read**.

Every artifact is one HTML file with inline CSS and JavaScript. No build step. No dependencies. Open directly in a browser.

**Evolution Note**: This skill combines the structured pattern catalog from [html-effectiveness](https://github.com/ThariqS/html-effectiveness) with the bold aesthetic philosophy from [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) by Anthropic, and the engineering rigor from [open-design](https://github.com/opendesign). It preserves the practical pattern library while elevating visual quality through intentional design thinking and enforcing quality through systematic self-check.

---

## Workflow

### Step 0 — Pre-flight (do this once before writing anything)

1. **Read this SKILL.md end-to-end** — understand the design system, pattern catalog, and hard rules.
2. **Understand the user's intent** — what is the purpose, tone, audience, and density?
3. **Map to Pattern Catalog** — choose the closest pattern (1-13) and aesthetic direction.
4. **Plan the section list** — state your chosen layout in one sentence to the user BEFORE writing. They can redirect cheaply now, not after 200 lines of HTML.

### Step 1 — Choose aesthetic direction

Commit to a **BOLD aesthetic direction** before coding:

- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work — the key is intentionality, not intensity.

### Step 2 — Write the artifact

1. **Copy the HTML Structure Template** (see below) as your seed.
2. **Define tokens** in `:root` — map colors to the six core variables (see Design System).
3. **Build sections** — compose from Pattern Catalog. Don't write from scratch; adapt the closest pattern.
4. **Add interaction** — minimal JS, CSS-first.
5. **Tag sections** — add `data-od-id="slug"` on every `<section>` for traceability.

### Step 3 — Self-check & Critique

Run through the **Quality Checklist** (P0/P1/P2) below. **Every P0 item must pass before you emit.**

Then run the **5-Dimension Self-Critique** (see section below). Score each dimension 0-10 with cited evidence. If any dimension scores < 4, enter DevLoop (see below).

### Step 4 — Emit the artifact

Wrap in `<artifact>` tags with proper metadata:

```
<artifact identifier="kebab-case-slug" type="text/html" title="Human Title">
<!doctype html>
<html>...</html>
</artifact>
```

One sentence before the artifact describing what's there. Stop after `</artifact>`.

---

## Design System

### Core Token Philosophy

Use **six core variables** in `:root`. Everything else derives from these. No raw hex outside `:root`.

```css
:root {
  --bg:      #fafaf7;   /* page background — never #fff */
  --surface: #ffffff;   /* cards, modals, raised areas */
  --fg:      #1a1916;   /* primary text — never #000 */
  --muted:   #6b6964;   /* secondary text, captions */
  --border:  #e8e5df;   /* hairlines, dividers */
  --accent:  #c96442;   /* one accent — used at most 2× per screen */

  /* derived — use color-mix(), do not add more tokens */
  --accent-soft: color-mix(in oklch, var(--accent) 14%, transparent);
  --fg-soft:     color-mix(in oklch, var(--fg) 6%, transparent);
}
```

**Why six tokens?** Constraints breed consistency. The seed template protects you from drift.

### Color Tokens (Default Palette)

Use this warm, editorial palette unless the user requests otherwise:

```css
:root {
  --ivory:    #FAF9F5;  /* page background */
  --slate:    #141413;  /* primary text, headings */
  --clay:     #D97757;  /* accent, links, CTAs, active states */
  --clay-d:   #B85C3E;  /* accent hover / dark variant */
  --oat:      #E3DACC;  /* secondary accent, borders, highlights */
  --olive:    #788C5D;  /* success, positive, secondary action */
  --rust:     #B04A3F;  /* error, warning, destructive */
  --sky:      #6A8CAF;  /* info, tertiary accent (optional) */
  --gray-50:  #F0EEE6;  /* subtle backgrounds, tags */
  --gray-100: #F0EEE6;  /* card backgrounds, code blocks */
  --gray-150: #F0EEE6;  /* prompt boxes, subtle fills */
  --gray-200: #D1CFC5;  /* borders, dividers */
  --gray-300: #D1CFC5;  /* card borders, separators */
  --gray-500: #87867F;  /* muted text, captions, meta */
  --gray-700: #3D3D3A;  /* body text, descriptions */
  --gray-800: #3D3D3A;  /* secondary headings */
  --white:    #FFFFFF;  /* card backgrounds, panels */
}
```

**Alternative Palettes** (choose based on tone):
- **Dark/Luxury**: `--bg: #0a0a0a`, `--text: #e5e5e5`, `--accent: #c9a96e` (gold)
- **Soft/Pastel**: `--bg: #f5f0ff`, `--text: #2d2a32`, `--accent: #9b7ede` (lavender)
- **Brutalist**: `--bg: #fff`, `--text: #000`, `--accent: #ff0000` (pure red)
- **Industrial**: `--bg: #e8e6e1`, `--text: #1a1a1a`, `--accent: #d4652a` (rust orange)

### Typography Tokens

```css
:root {
  --font-display: 'Iowan Old Style', 'Charter', Georgia, 'Times New Roman', serif;
  --font-body:    -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
  --font-mono:    ui-monospace, 'JetBrains Mono', 'SF Mono', Menlo, monospace;
}
```

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| H1 (page title) | var(--font-display) | clamp(44px, 6vw, 76px) | 500 | letter-spacing: -0.02em |
| H2 (section) | var(--font-display) | clamp(32px, 4vw, 48px) | 500 | letter-spacing: -0.015em |
| H3 (card title) | var(--font-display) | 22px | 600 | letter-spacing: -0.005em |
| Body | var(--font-body) | 16px | 400 | line-height: 1.55 |
| Eyebrow / Label | var(--font-mono) | 11-12px | 400 | uppercase, letter-spacing: 0.08em |
| Code / File | var(--font-mono) | 11-13px | 400 | inline background: var(--gray-100) |
| Caption / Meta | var(--font-body) | 13px | 400 | color: var(--muted) |

**Typography Philosophy**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics. Pair a distinctive display font with a refined body font. Consider:
- **Editorial**: Playfair Display + Source Sans Pro
- **Modern**: Space Grotesk + IBM Plex Sans (use sparingly)
- **Classic**: Cormorant Garamond + Work Sans
- **Technical**: JetBrains Mono + Inter (for developer tools)

### Spacing & Radius

```css
--radius-panel: 12px;   /* cards, panels */
--radius-row:    8px;   /* inner elements, buttons */
--radius-pill: 999px;   /* tags, pills, toggles */
--border: 1.5px solid var(--gray-300);
```

Page padding: `56px 24-32px 96-120px`. Max-width: `860-1180px` depending on content density.

**8-point grid**: `--gap-xs: 8px; --gap-sm: 12px; --gap-md: 20px; --gap-lg: 32px; --gap-xl: 56px; --gap-2xl: 96px;`

### Core CSS Reset

```css
*, *::before, *::after { box-sizing: border-box; }
html { 
  scroll-behavior: smooth; 
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
  font-family: var(--font-body);
  background: var(--bg);
  color: var(--fg);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
img, svg { display: block; max-width: 100%; }
a { color: inherit; text-decoration: none; }
button { font: inherit; cursor: pointer; }
p { text-wrap: pretty; }
h1, h2, h3, h4 { text-wrap: balance; }
```

---

## Frontend Aesthetics Guidelines

Focus on:

- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

---

## Pattern Catalog

Choose the pattern that matches the user's intent. Each pattern includes structural guidance and key techniques.

### 1. Side-by-Side Comparison
**Use for:** Comparing approaches, designs, options.
**Structure:** Grid of equal columns (2-4), each in a card with consistent internal structure.
**Key techniques:**
- `display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));`
- Each card: white background, 1.5px border, 12-14px radius
- Highlight the recommended option with `--slate` border + subtle shadow
- Include trade-off callouts as inline tags (color-coded pills)
- **Aesthetic enhancement**: Add subtle hover lift animations, gradient borders for recommended option

### 2. Annotated Diff / Code Review
**Use for:** PR reviews, code changes, before/after.
**Structure:** Two-column or stacked diff blocks with margin notes.
**Key techniques:**
- Old code: strikethrough or muted background (`--gray-100`)
- New code: highlighted with left border (`border-left: 3px solid var(--clay)`)
- Severity tags: `critical` (rust), `warn` (clay), `note` (olive), `style` (gray)
- Line numbers in mono font, muted color
- Jump links for long diffs
- **Aesthetic enhancement**: Syntax highlighting with custom colors, subtle line hover effects

### 3. Module Map / Architecture Diagram
**Use for:** Code understanding, system architecture, data flow.
**Structure:** SVG-based box-and-arrow diagram with interactive tooltips.
**Key techniques:**
- Inline SVG for full control and zero dependencies
- Boxes: `rect` with rounded corners, fill based on type (module, external, db)
- Arrows: `path` or `line` with arrowhead markers
- Hover: show detail panel with `mouseenter` / `mouseleave`
- Hot path: highlight with `--clay` stroke or glow
- **Aesthetic enhancement**: Animated connection lines, gradient fills on nodes, subtle shadow depth

### 4. Living Design System
**Use for:** Color palettes, typography scales, spacing tokens, component catalogs.
**Structure:** Organized sections with swatches, live previews, copyable values.
**Key techniques:**
- Color swatches: square divs with hex label underneath
- Typography: show sample text at each scale with computed CSS
- Spacing: visual ruler with pixel values
- Components: render every variant (size, state, intent) in a contact sheet
- **Aesthetic enhancement**: Interactive copy-to-clipboard, animated swatch transitions

### 5. Slide Deck (Enhanced)
**Use for:** Presentations, walkthroughs, demos.
**Structure:** Full-viewport sections with scroll-snap navigation.
**Key techniques:**
- Each slide: `width: 100vw; height: 100vh; scroll-snap-align: start;`
- `scroll-snap-type: y mandatory;` on body
- Arrow key / scroll navigation
- Invert variant: dark background (`--slate`) for emphasis slides
- Progress dots or slide counter
- **Aesthetic enhancement**: Staggered content reveals, dramatic transition animations, gradient backgrounds
- **Presenter Mode**: If the user mentions "演讲", "分享", "speaker notes", add `<aside class="notes">` with 150-300 words of script per slide. Press S to open presenter view (current/next/script/timer cards).
- **Advanced Slide Features**:
  - **36 theme options**: tokyo-night, swiss-grid, xiaohongshu-white, dracula-pro, monokai-legacy, nord-frost, gruvbox-dark, catppuccin-mocha, aurora-borealis, solarized-dual, etc.
  - **Canvas FX for transitions**: particle-burst, matrix-rain, knowledge-graph, ripple-expand, typewriter-reveal
  - **Dual-screen presenter mode**: speaker notes panel, timer with warning flash, current/next slide preview
  - **Speaker notes**: `<aside class="notes">` for presenter-only content (never visible on main slide)

### 6. Interactive Explainer
**Use for:** Teaching concepts, feature documentation, research summaries.
**Structure:** Article layout with interactive demos, collapsible sections, tabbed code.
**Key techniques:**
- TL;DR box at top (highlighted background)
- Collapsible `<details>` elements for deep dives
- Tabbed code samples (language switcher)
- Interactive demo panel (canvas, sliders, buttons)
- Margin glossary with hover-linked terms
- **Aesthetic enhancement**: Smooth expand/collapse animations, interactive code playgrounds, progressive disclosure

### 7. Status / Incident Report
**Use for:** Weekly updates, post-mortems, progress tracking.
**Structure:** Header with meta, timeline or chart, risk/health table, follow-ups.
**Key techniques:**
- Health pills: `on-track` (olive), `at-risk` (clay), `blocked` (rust)
- Mini bar charts with CSS flex heights
- Timeline: vertical line with colored dots and event cards
- Risk table: colored left border per severity
- **Aesthetic enhancement**: Animated progress indicators, pulsing status dots, trend sparklines

### 8. Flowchart / Process Diagram
**Use for:** Pipelines, decision trees, workflows.
**Structure:** SVG flowchart with clickable nodes and detail sidebar.
**Key techniques:**
- Nodes: `rect` (process), `path` diamond (decision), `circle` (start/end)
- Edges: `path` with optional dasharray for conditional flows
- Click node → show details in adjacent panel
- Pan/zoom for large diagrams (optional)
- **Aesthetic enhancement**: Path drawing animations, node pulse effects, smooth panel transitions

### 9. SVG Illustration Sheet
**Use for:** Blog diagrams, figures, icons.
**Structure:** Grid of inline SVG figures with captions.
**Key techniques:**
- Each figure: self-contained `<svg viewBox>`
- Reusable CSS classes for strokes and fills
- Export-ready: copy SVG code directly
- **Aesthetic enhancement**: Subtle hover transforms, coordinated color themes across illustrations

### 10. Custom Editor / Triage Board
**Use for:** Sorting, flag editing, prompt tuning, configuration.
**Structure:** Interactive UI with drag-and-drop or form controls + export.
**Key techniques:**
- Drag and drop with HTML5 Drag API
- Toggle switches with CSS-only styling
- Live preview panels that re-render on input
- Export button: serialize state to JSON/markdown and copy to clipboard
- Sticky toolbar for global actions
- **Aesthetic enhancement**: Smooth drag animations, satisfying toggle micro-interactions, real-time preview updates

### 11. Dashboard / Data Display
**Use for:** Metrics, KPIs, monitoring views.
**Structure:** Card grid with numbers, mini charts, status indicators.
**Key techniques:**
- Metric cards: big number + delta + sparkline
- CSS-only bar/line mini charts
- Color coding: olive (good), clay (warning), rust (bad)
- Auto-generated timestamp
- **Aesthetic enhancement**: Number counting animations, live data pulse effects, gradient chart fills

### 12. Live Artifact / Refreshable Dashboard (NEW)
**Use for:** Real-time dashboards, data-backed reports, synced views that need periodic refresh.
**Structure:** Separated template and data for easy updates without regenerating the entire artifact.
**Key techniques:**
- **File structure**: `template.html` + `data.json` + `artifact.json` + `provenance.json` (if OpenDesign available)
- **For standalone artifacts**: Inline the data directly in the HTML, provide a manual refresh mechanism (button or auto-refresh timer)
- **Template binding**: Use `{{data.path}}` style interpolation if in OpenDesign context; for standalone HTML, use JavaScript data injection:
  ```javascript
  // In standalone mode:
  let dashboardData = await fetch('data.json').then(r => r.json());
  // OR inline:
  const dashboardData = { metrics: [...], timestamp: Date.now() };
  ```
- **Refresh mechanism**: 
  - Auto-refresh: `setInterval(() => location.reload(), 60000)`
  - Manual refresh button: `<button onclick="refreshData()">Refresh</button>`
  - WebSocket for real-time: `new WebSocket('ws://...')`
- **Data visualization**: Use CSS charts or SVG that bind to data dynamically
- **Aesthetic enhancement**: Smooth data transition animations, loading skeletons, optimistic UI updates
- **When to use**: 
  - Data changes frequently (metrics, KPIs, monitoring)
  - Multiple people need to see the same live view
  - Report needs to be regenerated with fresh data regularly

### 13. Frame Effects / Visual Moments (NEW)
**Use for:** Hero sections, title reveals, visual emphasis, memorable page moments.
**Structure:** Targeted animation or effect applied to a specific section for dramatic impact.
**Key techniques:**
- **Glitch titles**: CSS keyframes + `clip-path` for cyberpunk/distorted text effect
  ```css
  @keyframes glitch {
    0% { clip-path: inset(40% 0 61% 0); transform: translate(-2px, 2px); }
    20% { clip-path: inset(92% 0 1% 0); transform: translate(1px, -1px); }
    40% { clip-path: inset(43% 0 1% 0); transform: translate(-1px, 3px); }
    60% { clip-path: inset(25% 0 58% 0); transform: translate(3px, 1px); }
    80% { clip-path: inset(54% 0 7% 0); transform: translate(-2px, -3px); }
    100% { clip-path: inset(58% 0 43% 0); transform: translate(0); }
  }
  .glitch-title:hover { animation: glitch 0.3s infinite; }
  ```
- **Liquid background hero**: Animated gradient blobs with CSS `border-radius` animation + `filter: blur()`
- **Light leak cinema effect**: Overlay SVG gradient with `mix-blend-mode: screen` + CSS animation
- **Logo outro animations**: Staggered letter reveals with `animation-delay` + `transform: translateY()`
- **macOS notification card**: Frosted glass (`backdrop-filter: blur(20px)`) + subtle shadow + slide-in animation
- **Key principle**: ONE dramatic moment per page, not constant motion. The effect should surprise and delight, then settle.
- **Performance**: Use `will-change: transform` sparingly; prefer `transform` and `opacity` for animations (GPU-accelerated)
- **Accessibility**: Always respect `prefers-reduced-motion: @media (prefers-reduced-motion: reduce) { animation: none; }`
- **Aesthetic enhancement**: Combine with careful timing (page load stagger), strategic use of `$accent` color, and intentional exit (effect ends, doesn't loop forever)

---

## HTML Structure Template

Every artifact starts from this skeleton:

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title><!-- Descriptive title --></title>
<style>
  :root {
    /* Six core tokens — bind to active design system */
    --bg:      #fafaf7;
    --surface: #ffffff;
    --fg:      #1a1916;
    --muted:   #6b6964;
    --border:  #e8e5df;
    --accent:  #c96442;
    
    /* Derived — do not change */
    --accent-soft: color-mix(in oklch, var(--accent) 14%, transparent);
    --fg-soft:     color-mix(in oklch, var(--fg) 6%, transparent);
    
    /* Type */
    --font-display: 'Iowan Old Style', 'Charter', Georgia, serif;
    --font-body:    -apple-system, BlinkMacSystemFont, 'Segoe UI', system-ui, sans-serif;
    --font-mono:    ui-monospace, 'JetBrains Mono', 'SF Mono', Menlo, monospace;
    
    /* Scale */
    --fs-h1: clamp(44px, 6vw, 76px);
    --fs-h2: clamp(32px, 4vw, 48px);
    --fs-h3: 22px;
    --fs-lead: 19px;
    --fs-body: 16px;
    --fs-meta: 13px;
    
    /* Spacing — 8-point grid */
    --gap-xs: 8px;
    --gap-sm: 12px;
    --gap-md: 20px;
    --gap-lg: 32px;
    --gap-xl: 56px;
    --gap-2xl: 96px;
    --container: 1120px;
    --gutter: 32px;
    
    --radius: 10px;
    --radius-lg: 16px;
  }
  
  /* Reset */
  *, *::before, *::after { box-sizing: border-box; }
  html { scroll-behavior: smooth; -webkit-text-size-adjust: 100%; }
  body {
    margin: 0;
    font-family: var(--font-body);
    background: var(--bg);
    color: var(--fg);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
    text-rendering: optimizeLegibility;
    padding: 56px 24px 96px;
  }
  
  /* Layout primitives */
  .container { max-width: var(--container); margin-inline: auto; padding-inline: var(--gutter); }
  .page { max-width: 980px; margin: 0 auto; }
  
  /* ... pattern-specific styles ... */
</style>
</head>
<body>
<div class="page">
  <header>...</header>
  <!-- content -->
</div>
<script>
  // minimal interaction logic
</script>
</body>
</html>
```

---

## Interaction Guidelines

### When to Add Interactivity
- **Always:** hover states on cards/links, smooth scrolling
- **Often:** collapsible sections, tabbed content, toggle switches
- **Sometimes:** drag-and-drop, live previews, sliders for parameters
- **Rarely:** complex animations, game-like interactions

### Hover Patterns
```css
a.card:hover {
  transform: translateY(-3px);
  box-shadow: 0 10px 30px rgba(20, 20, 19, 0.10);
  border-color: var(--slate);
}
```

### Transitions
```css
transition: transform 150ms ease, box-shadow 150ms ease, border-color 150ms ease;
```

### Animation Principles
- Use `animation-delay` for staggered reveals
- Prefer CSS animations over JS for performance
- Add `prefers-reduced-motion` support
- One well-orchestrated entrance beats scattered micro-interactions
- Focus on high-impact moments: page load with staggered reveals creates more delight than scattered micro-interactions

---

## Responsive Rules

- Mobile breakpoint: `max-width: 920px` (standard)
- Grid collapses to single column: `.grid-2`, `.grid-3`, `.grid-4` → `1fr`
- Font sizes use `clamp()` for fluid scaling
- Padding reduces: `56px 24px` → `32px 16px`
- Touch targets: minimum 44px

---

## Accessibility

- Semantic HTML: `<header>`, `<section>`, `<nav>`, `<main>`, `<footer>`
- Alt text on informative images
- `aria-hidden="true"` on decorative elements
- Sufficient color contrast (WCAG AA)
- Keyboard-navigable interactive elements
- `prefers-reduced-motion` respect for animations
- `text-wrap: pretty` on paragraphs, `text-wrap: balance` on headings

---

## Anti-Patterns to Avoid (Hard Rules)

### P0 — Must Never Happen
- **Don't** use external CSS/JS files — everything must be inline
- **Don't** use CDN libraries — no Bootstrap, no jQuery, no React
- **Don't** use default browser styling — always reset and define
- **Don't** use raw hex outside `:root` token block — every color must be a `var()` or `color-mix()`
- **Don't** use purple/violet gradient backgrounds — no `linear-gradient(... #a855f7 / #8b5cf6 / purple ...)`
- **Don't** use emoji as feature icons — use inline SVG monoline marks or tasteful mono glyphs
- **Don't** invent metrics — "10× faster", "99.9% uptime" without source = remove
- **Don't** use filler copy — zero "Feature One / Feature Two", lorem ipsum
- **Don't** forget `data-od-id` on every top-level `<section>`
- **Don't** break mobile reflow — all grids must collapse at ≤920px

### P1 — Should Avoid
- **Don't** make walls of text — break into cards, grids, diagrams
- **Don't** use pure black/white — use `--slate` and `--ivory` for warmth
- **Don't** over-animate — subtlety is key
- **Don't** converge on generic AI aesthetics — make each design distinctive
- **Don't** use Inter / Roboto / Arial as display fonts — they are body-only
- **Don't** use glassmorphism / backdrop-blur on KPI cards
- **Don't** use colored progress bars under KPI numbers
- **Don't** put presenter-only text on visible slides — use `<aside class="notes">`

### P2 — Nice to Avoid
- **Don't** load heavy animation frameworks
- **Don't** mix image styles on one page — pick a lane

---

## Quality Checklist

Run this before emitting `<artifact>`. P0 = must pass; P1 = should pass; P2 = nice to have.

### P0 — Must Pass
- [ ] **No raw hex outside `:root` token block.** Every color is `var(--bg)` / `var(--fg)` / `var(--muted)` / `var(--border)` / `var(--accent)` / `var(--surface)` (or a `color-mix()` of those).
- [ ] **All headings use `var(--font-display)`.** No sans-serif `<h1>` / `<h2>`. Inter / Roboto / system-sans never serve as a display face.
- [ ] **Accent appears at most twice per screen.** Count: eyebrow color, primary CTA fill, anything else? If three or more, demote one to `var(--fg)` or `var(--muted)`.
- [ ] **No purple/violet gradient backgrounds.** No `linear-gradient(... #a855f7 / #8b5cf6 / purple ...)`.
- [ ] **No emoji used as feature icons.** Use inline SVG monoline marks or tasteful single-character glyph in `--font-mono`.
- [ ] **No invented metrics.** Every number came from the user, the brief, or is clearly labelled as placeholder.
- [ ] **No filler copy.** Zero "Feature One / Feature Two", lorem ipsum. If a section feels empty, delete it.
- [ ] **`data-od-id` on every top-level `<section>`.** Used for traceability.
- [ ] **Mobile reflow works.** All grids collapse to one column at ≤920px. No horizontal scroll.
- [ ] **No `scrollIntoView()` calls.** Use `scrollTo({...})` if scroll behavior needed.

### P1 — Should Pass
- [ ] **One decisive flourish.** A pull quote, a striking stat, a real-feeling photograph, one micro-animation on the hero. *One.* Not three.
- [ ] **Section rhythm alternates.** No two stat rows in a row. No two feature triplets in a row. No two quote blocks in a row.
- [ ] **Headlines under 14 words.** If longer, the writing is doing the design's job.
- [ ] **Lead text under 56 ch / two sentences.** `max-width: 60ch` on `.lead` enforces this.
- [ ] **CTA buttons say what happens.** "Start free" beats "Get Started". "Read the story" beats "Learn More".
- [ ] **Hover states present** for all `<a>` and `.btn`.
- [ ] **Numerics use `.num` (mono, tabular).** Prices, stats, version numbers, dates.
- [ ] **One image style per page.** Don't mix square portraits with widescreen heroes.

### P2 — Nice to Have
- [ ] **`text-wrap: pretty` / `balance`** on long paragraphs / headings.
- [ ] **`color-mix()` for derived tones.** No additional `--accent-50` / `--accent-300` Bootstrap-style tokens.
- [ ] **Sticky topnav has frosted glass** via `backdrop-filter: blur()`.
- [ ] **Loaded fonts are system-first.** Only pull a Google Font if design system specifies one.

---

## 5-Dimension Self-Critique (Enhanced)

Before emitting, run a structured self-critique across 5 dimensions. **Each dimension scored 0-10 with specific evidence cited.**

### Scoring Bands

| Score | Band | Description |
|-------|------|-------------|
| 0-4 | **Broken** | Fundamental issues that break the experience |
| 5-6 | **Functional** | Works but lacks polish or consistency |
| 7-8 | **Strong** | Competent, polished, intentional |
| 9-10 | **Exceptional** | Memorable, magazine-grade, pushes boundaries |

### Dimensions

#### 1. Philosophy Consistency · 哲学一致性
**Definition**: One declared direction, stick to it. No style drift.

**Scoring**:
- **0-4 (Broken)**: Three or more competing styles. User can't identify the aesthetic direction.
- **5-6 (Functional)**: One direction declared but half the elements drift. Inconsistent execution.
- **7-8 (Strong)**: Coherent direction, occasional drift on 1-2 elements.
- **9-10 (Exceptional)**: Every element argues for the same thesis. Unmistakable direction.

**Evidence required**: Cite specific class names, elements, or sections that support or contradict the declared direction.

#### 2. Visual Hierarchy · 视觉层级
**Definition**: Can a stranger figure out what to read first, second, third?

**Scoring**:
- **0-4 (Broken)**: Everything shouts. No clear reading order. Competing heroes.
- **5-6 (Functional)**: Hierarchy works on hero but breaks in body. Some sections compete.
- **7-8 (Strong)**: Clear tiers, occasional collision on secondary elements.
- **9-10 (Exceptional)**: Eye moves with zero friction. Obvious what matters.

**Evidence required**: Trace the F-pattern or Z-pattern. Cite specific heading sizes, weights, colors that establish hierarchy.

#### 3. Detail Execution · 细节执行
**Definition**: Alignment, leading, kerning, image framing, edge-case spacing. The 90/10 stuff.

**Scoring**:
- **0-4 (Broken)**: Visible tape and string. Misaligned elements, inconsistent spacing, broken images.
- **5-6 (Functional)**: Most pages clean, 1-2 ragged edges. Minor spacing issues.
- **7-8 (Strong)**: Polished, expert eye finds 2-3 misses. Solid craft.
- **9-10 (Exceptional)**: Magazine-grade. Pixel-perfect execution.

**Evidence required**: Cite specific line numbers, class names, or elements where alignment/spacing is off or excellent.

#### 4. Functionality · 功能性
**Definition**: Does it WORK? Keyboard nav, click targets, readability, responsive behavior.

**Scoring**:
- **0-4 (Broken)**: Visually fine but doesn't accomplish its job. Broken interactions, unreadable text.
- **5-6 (Functional)**: Core flow works, edge cases broken. Some links don't work.
- **7-8 (Strong)**: Robust through normal use. Handles edge cases well.
- **9-10 (Exceptional)**: Defensively engineered. Graceful degradation, bulletproof.

**Evidence required**: Cite specific interactive elements, test scenarios, or edge cases that pass or fail.

#### 5. Innovation · 创新性
**Definition**: One unexpected move that makes people lean in. Not generic AI-median.

**Scoring**:
- **0-4 (Broken)**: Generic AI-slop median. Inter font, purple gradient, stock layout.
- **5-6 (Functional)**: Competent and unmemorable. Gets the job done, won't be shared.
- **7-8 (Strong)**: One memorable moment. A surprise, a delight, a "hey look at this".
- **9-10 (Exceptional)**: Multiple moves you'd steal. Pushses past median decisively.

**Evidence required**: Cite the specific unexpected move(s). What will someone remember?

### Scoring Discipline Rules (Hard Rules)

1. **Always cite evidence** — no "feels off" or vague impressions. Every score must reference specific class names, line numbers, or elements.

2. **Don't average up** — score the WORST sustained band. If Philosophy is 9 but Detail Execution is 4, the overall quality is Broken until fixed.

3. **Don't grade-inflate** — a 7 means STRONG, not "acceptable". A 5 is Functional, not "good enough". Be honest.

4. **Innovation can be low** — 5/10 for production work is fine. Not every artifact needs to be a design award winner. Utility matters.

5. **Separate intent from execution** — a maximalist design that executes poorly scores low on Detail Execution even if Philosophy is bold.

### Output Format: Structured Self-Critique

After scoring, output a structured critique with:

1. **Radar chart mention** (describe the shape, not actual chart)
2. **Band labels** for each dimension
3. **Three action lists**:

```
## Self-Critique Report

### Scores
- Philosophy Consistency: 7/10 (Strong)
- Visual Hierarchy: 6/10 (Functional)
- Detail Execution: 5/10 (Functional)
- Functionality: 8/10 (Strong)
- Innovation: 6/10 (Functional)

### Evidence
[Specific citations for each score]

### Keep (3-5 bullets)
- [What's working, don't break]
- ...

### Fix (3-6 bullets, P0/P1 ordered by visual cost saved per minute)
- [P0: Critical issues that must be fixed before emitting]
- [P1: Should fix for quality]
- ...

### Quick Wins (3-5 bullets, 5-15 minute tweaks with disproportionate impact)
- [Small changes that dramatically improve quality]
- ...
```

---

## DevLoop: Iterative Refinement

After the first generation and self-critique:

### The Loop

1. **Generate** → first version of the artifact
2. **Critique** → run 5-dimension self-critique, get scores
3. **Check** → if ANY dimension scores < 4 (Broken), iterate
4. **Fix** → each iteration: fix the lowest-scoring dimension first
5. **Re-critique** → score again after fixes
6. **Repeat** → max 3 iterations total

### Escape Hatch

The user can stop the loop at any time:
- Say "good enough" / "stop iterating" / "emit it"
- Or explicitly approve the current version

### Iteration Strategy

**Each iteration should fix the LOWEST-SCORING dimension first**:

- If Philosophy = 3 and Detail = 5, fix Philosophy first (it drags down everything)
- If all dimensions are 5-6, pick the one with the easiest fix that gives biggest visual improvement
- Never iterate on a dimension that already scores 8+

**Max 3 iterations** to prevent infinite loops. If still broken after 3, emit with caveats.

### When to Skip DevLoop

Skip iteration if:
- All dimensions score ≥ 7 (Strong)
- User explicitly says "don't iterate" or "good enough"
- The artifact is a quick draft / prototype (user says "rough", "draft", "quick")

---

## Critique Report Output Contract

When requested to produce a self-contained HTML critique report (for design reviews, handoffs, or documentation):

### Structure

The critique report should be a standalone HTML file with:

1. **Radar chart** (inline SVG, 5 axes matching the 5 dimensions)
2. **5 dimension cards** with scores + evidence citations
3. **Keep / Fix / Quick-wins action lists** (structured, prioritized)
4. **Before/after comparison** (if in DevLoop, show iteration diffs)

### Template

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Critique Report: [Artifact Name]</title>
  <style>
    /* Inline styles following design system */
    :root { /* six core tokens */ }
  </style>
</head>
<body>
  <div class="page">
    <header>
      <h1>Design Critique Report</h1>
      <p class="meta">Artifact: [name] | Date: [date] | Overall: [band]</p>
    </header>
    
    <!-- Radar Chart (inline SVG) -->
    <section data-od-id="critique-radar">
      <h2>5-Dimension Radar</h2>
      <svg viewBox="0 0 400 400">
        <!-- 5-axis radar with scores plotted -->
      </svg>
    </section>
    
    <!-- Dimension Cards -->
    <section data-od-id="critique-dimensions">
      <h2>Dimension Scores</h2>
      <div class="grid-3">
        <!-- 5 cards, each with score, band, evidence -->
      </div>
    </section>
    
    <!-- Action Lists -->
    <section data-od-id="critique-actions">
      <h2>Action Items</h2>
      <div class="actions">
        <div class="keep">
          <h3>✅ Keep (don't break)</h3>
          <ul>...</ul>
        </div>
        <div class="fix">
          <h3>🔧 Fix (P0/P1)</h3>
          <ul>...</ul>
        </div>
        <div class="quick-wins">
          <h3>⚡ Quick Wins</h3>
          <ul>...</ul>
        </div>
      </div>
    </section>
  </div>
</body>
</html>
```

### Output Options

- **As artifact**: Wrap in `<artifact>` tags for download/sharing
- **Inline**: Display directly in the conversation for quick review
- **Combined**: Attach critique report as second artifact alongside the designed artifact

---

## Decision Flow

When the user asks for HTML output:

1. **What is the purpose?** → Map to Pattern Catalog (1-13)
2. **What is the tone?** → Choose aesthetic direction (minimal, maximalist, retro, etc.)
3. **What is the density?** → Choose max-width (860px dense, 1180px spacious)
4. **Does it need interaction?** → Add minimal JS (keep it simple)
5. **Is there data to visualize?** → Use CSS charts or SVG diagrams
6. **Does it need refresh/sync?** → Structure as Live Artifact (Pattern #12: template + data)
7. **Is it a presentation?** → Add presenter mode support (`<aside class="notes">`, Pattern #5 enhanced)
8. **Does it need visual impact?** → Add Frame Effect (Pattern #13: one dramatic moment)
9. **Export needed?** → Add copy-to-clipboard or download button
10. **Run critique** → Score 5 dimensions, iterate if < 4 on any

---

## Section Rhythm Guide

Alternate section types to avoid visual fatigue:

| Page kind | Default rhythm |
|---|---|
| Landing | hero → features → stats *or* quote → split detail → cta |
| Marketing / editorial | hero-center → log list → cta |
| Pricing | hero-center → comparison table → cta |
| Docs index | hero-center → log list (sections) → cta |
| Dashboard | KPI row → primary chart → secondary chart/table |
| Presentation | cover → toc → section-divider → [2-4 body] → section-divider → cta → thanks |
| Live Dashboard | header → KPI row → chart grid → data table → refresh indicator |
| Visual Moment | hero (with frame effect) → content → cta |

**Rules**: 
- No two stat rows in a row
- No two quote blocks in a row  
- No two feature triplets in a row
- Alternate density: airy → dense → airy
- Max one Frame Effect per page (Pattern #13)

---

## Example Prompts This Skill Handles

- "Generate a status report as HTML"
- "Make this comparison visual with HTML"
- "Create an interactive explainer for [concept]"
- "Build a slide deck about [topic]"
- "Design a triage board for these tickets"
- "Draw a flowchart of this process"
- "Show me component variants in HTML"
- "Make this HTML prettier / more professional"
- "Optimize the layout of this AI-generated HTML"
- "Create a design system reference page"
- "Build a landing page for [product]"
- "Create a dashboard for [metrics]"
- "Create a live dashboard that refreshes from [source]"
- "Make a presentation with speaker notes"
- "Build a kanban board for [project]"
- "Add a dramatic hero effect to this page"
- "Create a glitch title effect for [topic]"
- "Make a real-time metrics dashboard"
- "Generate a critique report for this design"

---

## Output Contract

For standard artifacts:
```
<artifact identifier="kebab-case-slug" type="text/html" title="Human Title">
<!doctype html>
<html>...</html>
</artifact>
```

For critique reports:
```
<artifact identifier="critique-[slug]" type="text/html" title="Critique Report: [Title]">
<!doctype html>
<html>...</html>
</artifact>
```

For live artifacts (template + data):
```
<artifact identifier="[slug]-template" type="text/html" title="[Title] Template">
<!doctype html>
<html>...</html>
</artifact>

<file path="data.json">
{ "metrics": [...], "timestamp": "..." }
</file>
```

One sentence before the artifact. Nothing after `</artifact>`.

---

## Chinese-Friendly Notes (中文说明)

本技能支持中文本地化：

- **字体选择**: 中文字体使用 `Noto Sans SC`, `PingFang SC`, `Microsoft YaHei` 等系统字体
- **排版规则**: 中文段落使用 `text-wrap: pretty`, 标题使用 `text-wrap: balance`
- **色彩系统**: 保持 6  token 约束，中文场景可使用更温暖的调色板
- **动画效果**: Frame Effects 支持中文标题的 glitch 效果（需要等宽字体）
- **演示模式**: Pattern #5 支持中文演讲者备注（`<aside class="notes">` 内写中文）
- **评判标准**: 5维度自我评判同样适用于中文场景，注意引证具体的类名、行号、元素

**常用中文字体栈**:
```css
--font-display-cn: 'Noto Serif SC', 'Source Han Serif SC', 'SimSun', serif;
--font-body-cn: 'Noto Sans SC', 'Source Han Sans SC', 'PingFang SC', sans-serif;
```

---

## Version History

- **v2.1** (2026-05-21): Enhanced 5-dimension self-critique, added DevLoop iterative refinement, added Pattern #12 (Live Artifact) and Pattern #13 (Frame Effects), enhanced Pattern #5 (Slide Deck) with advanced features, added Critique Report output contract, added Scoring Discipline Rules
- **v2.0** (2026-05-20): Combined html-effectiveness + frontend-design + open-design; established 6-token design system, 11 patterns, P0/P1/P2 anti-patterns
- **v1.0** (2026-05): Initial release based on html-effectiveness
