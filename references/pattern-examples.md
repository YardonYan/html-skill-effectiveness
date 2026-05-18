# Pattern Examples

Real code snippets extracted from the reference collection, organized by pattern.

**Skill**: html-effectiveness by [Yardon](https://github.com/YardonYan) | May 2026
**Based on**: [The Unreasonable Effectiveness of HTML](https://github.com/ThariqS/html-effectiveness)

## 1. Side-by-Side Comparison

From `01-exploration-code-approaches.html` — Three approaches in a grid:

```css
.approaches {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 28px;
}
@media (max-width: 1100px) {
  .approaches { grid-template-columns: 1fr; }
}

.approach {
  background: var(--white);
  border: 1.5px solid var(--gray-300);
  border-radius: 14px;
  padding: 24px;
  display: flex;
  flex-direction: column;
}
.approach.recommended {
  border-color: var(--slate);
  box-shadow: 0 8px 24px rgba(20,20,19,.08);
}
```

Trade-off tags:
```css
.tag {
  font-family: var(--mono);
  font-size: 11px;
  padding: 3px 10px;
  border-radius: 999px;
  background: var(--gray-100);
  color: var(--gray-700);
}
.tag.pro { background: #E8F0E0; color: var(--olive); }
.tag.con { background: #F5E8E4; color: var(--rust); }
```

## 2. Annotated Diff

From `03-code-review-pr.html` — Diff block with margin notes:

```css
.diff-block {
  background: var(--white);
  border: 1.5px solid var(--gray-300);
  border-radius: 12px;
  overflow: hidden;
}
.diff-line {
  display: flex;
  font-family: var(--mono);
  font-size: 13px;
  line-height: 1.6;
  padding: 2px 16px;
}
.diff-line.add {
  background: #F0F7EC;
  border-left: 3px solid var(--olive);
}
.diff-line.del {
  background: #FDF2F0;
  border-left: 3px solid var(--rust);
}
.diff-line .ln {
  color: var(--gray-500);
  width: 40px;
  flex-shrink: 0;
  text-align: right;
  padding-right: 12px;
}
```

Severity pills:
```css
.severity {
  font-family: var(--mono);
  font-size: 10px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 2px 8px;
  border-radius: 999px;
}
.severity.critical { background: var(--rust); color: #fff; }
.severity.warn     { background: var(--clay); color: #fff; }
.severity.note     { background: var(--olive); color: #fff; }
.severity.style    { background: var(--gray-100); color: var(--gray-700); }
```

## 3. Module Map

From `04-code-understanding.html` — SVG architecture diagram:

```html
<svg viewBox="0 0 800 400" class="arch">
  <!-- Module box -->
  <rect x="50" y="50" width="140" height="60" rx="8"
        fill="var(--white)" stroke="var(--gray-300)" stroke-width="1.5"/>
  <text x="120" y="85" text-anchor="middle"
        font-family="var(--mono)" font-size="13" fill="var(--slate)">Router</text>

  <!-- Arrow -->
  <line x1="190" y1="80" x2="280" y2="80"
        stroke="var(--gray-300)" stroke-width="1.5"/>
  <polygon points="280,80 272,76 272,84" fill="var(--gray-300)"/>

  <!-- External (dashed) -->
  <rect x="300" y="50" width="140" height="60" rx="8" fill="none"
        stroke="var(--clay)" stroke-width="1.5" stroke-dasharray="4 4"/>
</svg>
```

## 4. Design System

From `05-design-system.html` — Color swatch grid:

```css
.swatch-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(120px, 1fr));
  gap: 16px;
}
.swatch {
  border-radius: var(--radius-row);
  overflow: hidden;
  border: var(--border);
}
.swatch .color {
  height: 80px;
}
.swatch .label {
  padding: 10px 12px;
  background: var(--white);
  font-family: var(--mono);
  font-size: 12px;
}
```

Typography scale:
```css
.type-scale .row {
  display: flex;
  align-items: baseline;
  gap: 20px;
  padding: 12px 0;
  border-bottom: 1px solid var(--gray-200);
}
.type-scale .size {
  font-family: var(--mono);
  font-size: 12px;
  color: var(--gray-500);
  width: 60px;
}
```

## 5. Slide Deck

From `09-slide-deck.html` — Scroll-snap slides:

```css
body {
  scroll-snap-type: y mandatory;
  overflow-x: hidden;
}
.slide {
  width: 100vw;
  height: 100vh;
  scroll-snap-align: start;
  scroll-snap-stop: always;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 8vh 6vw;
}
.slide.invert {
  background: var(--slate);
  color: var(--ivory);
}
```

Navigation:
```javascript
document.addEventListener('keydown', (e) => {
  const slides = document.querySelectorAll('.slide');
  const current = Math.round(window.scrollY / window.innerHeight);
  if (e.key === 'ArrowDown' || e.key === 'ArrowRight') {
    slides[Math.min(current + 1, slides.length - 1)]?.scrollIntoView();
  }
  if (e.key === 'ArrowUp' || e.key === 'ArrowLeft') {
    slides[Math.max(current - 1, 0)]?.scrollIntoView();
  }
});
```

## 6. Interactive Explainer

From `15-research-concept-explainer.html` — Collapsible sections:

```html
<details class="deep-dive">
  <summary>How does virtual node placement work?</summary>
  <div class="content">
    <p>Each node is hashed to a point on the ring...</p>
  </div>
</details>
```

```css
details.deep-dive {
  border: 1.5px solid var(--gray-300);
  border-radius: 12px;
  padding: 16px 20px;
  margin-bottom: 12px;
}
details.deep-dive summary {
  font-weight: 500;
  cursor: pointer;
  list-style: none;
}
details.deep-dive summary::before {
  content: "▸";
  margin-right: 8px;
  color: var(--clay);
  display: inline-block;
  transition: transform 150ms;
}
details[open] summary::before {
  transform: rotate(90deg);
}
```

Interactive demo with slider:
```html
<div class="demo">
  <input type="range" min="1" max="10" value="3" id="nodeCount">
  <div id="ring"></div>
</div>
<script>
  const slider = document.getElementById('nodeCount');
  const ring = document.getElementById('ring');
  slider.addEventListener('input', (e) => {
    renderRing(parseInt(e.target.value));
  });
</script>
```

## 7. Status Report

From `11-status-report.html` — Health pills and mini chart:

```css
.health {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  font-family: var(--mono);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  padding: 4px 10px;
  border-radius: 999px;
}
.health::before {
  content: "";
  width: 6px; height: 6px;
  border-radius: 50%;
}
.health.on-track  { background: #E8F0E0; color: var(--olive); }
.health.on-track::before  { background: var(--olive); }
.health.at-risk   { background: #F5E8E4; color: var(--clay-d); }
.health.at-risk::before   { background: var(--clay); }
.health.blocked   { background: #F5E8E4; color: var(--rust); }
.health.blocked::before   { background: var(--rust); }
```

Mini bar chart (CSS-only):
```css
.bar-chart {
  display: flex;
  align-items: flex-end;
  gap: 8px;
  height: 120px;
}
.bar {
  flex: 1;
  border-radius: 4px 4px 0 0;
  min-height: 4px;
}
.bar.done { background: var(--olive); }
.bar.in-progress { background: var(--clay); }
.bar.planned { background: var(--gray-200); }
```

## 8. Flowchart

From `13-flowchart-diagram.html` — Clickable SVG nodes:

```html
<svg viewBox="0 0 600 400">
  <g class="node" data-step="build" cursor="pointer">
    <rect x="100" y="100" width="120" height="50" rx="6"
          fill="var(--white)" stroke="var(--gray-300)" stroke-width="1.5"/>
    <text x="160" y="130" text-anchor="middle" font-size="13">Build</text>
  </g>
</svg>

<div class="detail-panel" id="details">
  <p>Click a step to see details</p>
</div>
```

```javascript
document.querySelectorAll('.node').forEach(node => {
  node.addEventListener('click', () => {
    const step = node.dataset.step;
    document.getElementById('details').innerHTML = detailData[step];
  });
});
```

## 9. SVG Illustration

From `10-svg-illustrations.html` — Reusable SVG classes:

```css
svg.figure .st { stroke: var(--g500); fill: none; stroke-width: 2.5; }
svg.figure .fl { fill: var(--g300); }
svg.figure .cl { fill: var(--clay); }
svg.figure .ol { fill: var(--olive); }
svg.figure .oa { fill: var(--oat); stroke: var(--g500); stroke-width: 2.5; }
svg.figure .sl { fill: var(--slate); }
svg.figure .wh { fill: var(--paper); stroke: var(--g500); stroke-width: 2.5; }
svg.figure .ln { stroke: var(--g500); stroke-width: 2.5; fill: none; stroke-linecap: round; }
```

## 10. Custom Editor

From `18-editor-triage-board.html` — Drag and drop:

```javascript
// HTML5 Drag API
card.draggable = true;
card.addEventListener('dragstart', (e) => {
  e.dataTransfer.setData('text/plain', card.dataset.id);
  card.classList.add('dragging');
});

column.addEventListener('dragover', (e) => {
  e.preventDefault();
  column.classList.add('drop-target');
});

column.addEventListener('drop', (e) => {
  e.preventDefault();
  const id = e.dataTransfer.getData('text/plain');
  const card = document.querySelector(`[data-id="${id}"]`);
  column.appendChild(card);
  updateState();
});
```

Export to markdown:
```javascript
function exportMarkdown() {
  const columns = document.querySelectorAll('.column');
  let md = '';
  columns.forEach(col => {
    md += `## ${col.dataset.name}\n\n`;
    col.querySelectorAll('.card').forEach(card => {
      md += `- ${card.querySelector('.title').textContent}\n`;
    });
    md += '\n';
  });
  navigator.clipboard.writeText(md);
}
```

## 11. Dashboard

Metric card with sparkline:

```css
.metric {
  background: var(--white);
  border: var(--border);
  border-radius: var(--radius-panel);
  padding: 24px;
}
.metric .value {
  font-family: var(--serif);
  font-size: 42px;
  font-weight: 500;
  color: var(--slate);
  letter-spacing: -0.02em;
}
.metric .delta {
  font-family: var(--mono);
  font-size: 13px;
}
.metric .delta.up   { color: var(--olive); }
.metric .delta.down { color: var(--rust); }

.sparkline {
  display: flex;
  align-items: flex-end;
  gap: 3px;
  height: 40px;
  margin-top: 16px;
}
.sparkline .bar {
  flex: 1;
  background: var(--gray-200);
  border-radius: 2px 2px 0 0;
}
.sparkline .bar:last-child {
  background: var(--clay);
}
```
