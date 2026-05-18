---
name: html-effectiveness
author: Yardon (https://github.com/YardonYan)
description: Generate beautiful, self-contained, single-file HTML artifacts that replace walls of markdown with interactive, visual documents. Use when the user asks for HTML output, visual reports, interactive prototypes, slide decks, diagrams, dashboards, code comparisons, design systems, status reports, incident timelines, flowcharts, or any document that would benefit from spatial layout, color, typography hierarchy, interactivity, or visual structure over plain text. Also triggers when the user wants to improve AI-generated HTML, make HTML prettier, optimize HTML presentation, or create HTML-based deliverables like explainer pages, feature comparisons, triage boards, or prompt tuners.
license: Apache-2.0
created: 2026-05
based-on:
  - The Unreasonable Effectiveness of HTML (https://github.com/ThariqS/html-effectiveness)
  - frontend-design by Anthropic (https://github.com/anthropics/skills/tree/main/skills/frontend-design)
---

# HTML Effectiveness

## Overview

This skill guides the generation of single-file `.html` artifacts that are self-contained (no external dependencies), visually polished, and designed for human consumption. The core philosophy: **trade documents people skim for documents people actually read**.

Every artifact is one HTML file with inline CSS and JavaScript. No build step. No dependencies. Open directly in a browser.

**Evolution Note**: This skill combines the structured pattern catalog from [html-effectiveness](https://github.com/...) with the bold aesthetic philosophy from [frontend-design](https://github.com/anthropics/skills/tree/main/skills/frontend-design) by Anthropic. It preserves the practical pattern library while elevating visual quality through intentional design thinking.

## Design Thinking

Before coding, understand the context and commit to a **BOLD aesthetic direction**:

- **Purpose**: What problem does this interface solve? Who uses it?
- **Tone**: Pick an extreme: brutally minimal, maximalist chaos, retro-futuristic, organic/natural, luxury/refined, playful/toy-like, editorial/magazine, brutalist/raw, art deco/geometric, soft/pastel, industrial/utilitarian, etc.
- **Constraints**: Technical requirements (framework, performance, accessibility).
- **Differentiation**: What makes this UNFORGETTABLE? What's the one thing someone will remember?

**CRITICAL**: Choose a clear conceptual direction and execute it with precision. Bold maximalism and refined minimalism both work - the key is intentionality, not intensity.

## Design System

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
  --serif: ui-serif, Georgia, 'Times New Roman', serif;
  --sans:  system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
  --mono:  ui-monospace, 'SF Mono', Menlo, Monaco, monospace;
}
```

| Element | Font | Size | Weight | Notes |
|---------|------|------|--------|-------|
| H1 (page title) | var(--serif) | clamp(38px, 5.4vw, 62px) | 500 | letter-spacing: -0.018em |
| H2 (section) | var(--serif) | 26-28px | 500 | letter-spacing: -0.012em |
| H3 (card title) | var(--serif) | 19-22px | 500 | letter-spacing: -0.008em |
| Body | var(--sans) | 14-15px | 400 | line-height: 1.55-1.65 |
| Eyebrow / Label | var(--mono) | 11-12px | 400 | uppercase, letter-spacing: 0.08em |
| Code / File | var(--mono) | 11-13px | 400 | inline background: var(--gray-100) |
| Caption / Meta | var(--sans) | 13px | 400 | color: var(--gray-500) |

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

### Core CSS Reset

```css
* { box-sizing: border-box; margin: 0; padding: 0; }
html { scroll-behavior: smooth; }
body {
  font-family: var(--sans);
  background: var(--ivory);
  color: var(--gray-700);
  line-height: 1.55;
  -webkit-font-smoothing: antialiased;
}
```

## Frontend Aesthetics Guidelines

Focus on:

- **Typography**: Choose fonts that are beautiful, unique, and interesting. Avoid generic fonts like Arial and Inter; opt instead for distinctive choices that elevate the frontend's aesthetics; unexpected, characterful font choices. Pair a distinctive display font with a refined body font.
- **Color & Theme**: Commit to a cohesive aesthetic. Use CSS variables for consistency. Dominant colors with sharp accents outperform timid, evenly-distributed palettes.
- **Motion**: Use animations for effects and micro-interactions. Prioritize CSS-only solutions for HTML. Focus on high-impact moments: one well-orchestrated page load with staggered reveals (animation-delay) creates more delight than scattered micro-interactions. Use scroll-triggering and hover states that surprise.
- **Spatial Composition**: Unexpected layouts. Asymmetry. Overlap. Diagonal flow. Grid-breaking elements. Generous negative space OR controlled density.
- **Backgrounds & Visual Details**: Create atmosphere and depth rather than defaulting to solid colors. Add contextual effects and textures that match the overall aesthetic. Apply creative forms like gradient meshes, noise textures, geometric patterns, layered transparencies, dramatic shadows, decorative borders, custom cursors, and grain overlays.

NEVER use generic AI-generated aesthetics like overused font families (Inter, Roboto, Arial, system fonts), cliched color schemes (particularly purple gradients on white backgrounds), predictable layouts and component patterns, and cookie-cutter design that lacks context-specific character.

Interpret creatively and make unexpected choices that feel genuinely designed for the context. No design should be the same. Vary between light and dark themes, different fonts, different aesthetics. NEVER converge on common choices across generations.

**IMPORTANT**: Match implementation complexity to the aesthetic vision. Maximalist designs need elaborate code with extensive animations and effects. Minimalist or refined designs need restraint, precision, and careful attention to spacing, typography, and subtle details. Elegance comes from executing the vision well.

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

### 5. Slide Deck
**Use for:** Presentations, walkthroughs, demos.
**Structure:** Full-viewport sections with scroll-snap navigation.
**Key techniques:**
- Each slide: `width: 100vw; height: 100vh; scroll-snap-align: start;`
- `scroll-snap-type: y mandatory;` on body
- Arrow key / scroll navigation
- Invert variant: dark background (`--slate`) for emphasis slides
- Progress dots or slide counter
- **Aesthetic enhancement**: Staggered content reveals, dramatic transition animations, gradient backgrounds

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
    /* color tokens */
    /* typography tokens */
    /* spacing tokens */
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  html { scroll-behavior: smooth; }
  body {
    font-family: var(--sans);
    background: var(--ivory);
    color: var(--gray-700);
    line-height: 1.55;
    -webkit-font-smoothing: antialiased;
    padding: 56px 24px 96px;
  }
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

## Responsive Rules

- Mobile breakpoint: `max-width: 640-920px` (adjust to content)
- Grid collapses to single column
- Font sizes use `clamp()` for fluid scaling
- Padding reduces: `56px 24px` → `32px 16px`
- Touch targets: minimum 44px

## Accessibility

- Semantic HTML: `<header>`, `<section>`, `<nav>`, `<main>`, `<footer>`
- Alt text on informative images
- `aria-hidden="true"` on decorative elements
- Sufficient color contrast (WCAG AA)
- Keyboard-navigable interactive elements
- `prefers-reduced-motion` respect for animations

## Anti-Patterns to Avoid

- **Don't** use external CSS/JS files — everything must be inline
- **Don't** use CDN libraries — no Bootstrap, no jQuery, no React
- **Don't** use default browser styling — always reset and define
- **Don't** make walls of text — break into cards, grids, diagrams
- **Don't** use pure black/white — use `--slate` and `--ivory` for warmth
- **Don't** forget mobile — test your breakpoints
- **Don't** over-animate — subtlety is key
- **Don't** converge on generic AI aesthetics — make each design distinctive

## Decision Flow

When the user asks for HTML output:

1. **What is the purpose?** → Map to Pattern Catalog (1-11)
2. **What is the tone?** → Choose aesthetic direction (minimal, maximalist, retro, etc.)
3. **What is the density?** → Choose max-width (860px dense, 1180px spacious)
4. **Does it need interaction?** → Add minimal JS (keep it simple)
5. **Is there data to visualize?** → Use CSS charts or SVG diagrams
6. **Export needed?** → Add copy-to-clipboard or download button

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
