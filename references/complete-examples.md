# Complete Examples

Full HTML files demonstrating the patterns in practice. These are condensed from the reference collection.

**Skill**: html-effectiveness by [Yardon](https://github.com/YardonYan) | May 2026
**Based on**: [The Unreasonable Effectiveness of HTML](https://github.com/ThariqS/html-effectiveness)

## Minimal Status Report

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Week 11 Status</title>
<style>
  :root {
    --ivory:#FAF9F5; --slate:#141413; --clay:#D97757; --olive:#788C5D; --rust:#B04A3F;
    --g100:#F0EEE6; --g300:#D1CFC5; --g500:#87867F; --g700:#3D3D3A; --white:#FFFFFF;
    --serif:ui-serif,Georgia,serif; --sans:system-ui,sans-serif; --mono:ui-monospace,monospace;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:var(--sans); background:var(--ivory); color:var(--g700); line-height:1.6; padding:56px 24px 96px; }
  .page { max-width:860px; margin:0 auto; }
  h1 { font-family:var(--serif); font-size:38px; font-weight:500; color:var(--slate); margin-bottom:8px; }
  .date { color:var(--g500); font-size:14px; margin-bottom:40px; }

  .health { display:inline-flex; align-items:center; gap:6px; font-family:var(--mono); font-size:11px;
    text-transform:uppercase; letter-spacing:0.06em; padding:4px 10px; border-radius:999px; }
  .health::before { content:""; width:6px; height:6px; border-radius:50%; }
  .health.on-track { background:#E8F0E0; color:var(--olive); }
  .health.on-track::before { background:var(--olive); }
  .health.at-risk { background:#F5E8E4; color:var(--clay); }
  .health.at-risk::before { background:var(--clay); }

  .grid { display:grid; grid-template-columns:repeat(auto-fill,minmax(260px,1fr)); gap:20px; margin-top:32px; }
  .card { background:var(--white); border:1.5px solid var(--g300); border-radius:12px; padding:24px; }
  .card h3 { font-family:var(--serif); font-size:19px; font-weight:500; color:var(--slate); margin-bottom:8px; }
  .card p { font-size:14px; color:var(--g700); }
  .card .meta { display:flex; justify-content:space-between; align-items:center; margin-top:16px;
    padding-top:12px; border-top:1px solid var(--g100); font-family:var(--mono); font-size:11px; color:var(--g500); }
</style>
</head>
<body>
<div class="page">
  <h1>Engineering Status</h1>
  <p class="date">Week of March 10 — March 16</p>

  <div class="grid">
    <div class="card">
      <h3>API Migration</h3>
      <p>Completed auth middleware extraction. 3 of 4 services updated.</p>
      <div class="meta"><span class="health on-track">On Track</span><span>Due Mar 20</span></div>
    </div>
    <div class="card">
      <h3>Dashboard Redesign</h3>
      <p>Final review pending. Two blocking UX issues to resolve.</p>
      <div class="meta"><span class="health at-risk">At Risk</span><span>Due Mar 18</span></div>
    </div>
  </div>
</div>
</body>
</html>
```

## Minimal Comparison

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Approach Comparison</title>
<style>
  :root {
    --ivory:#FAF9F5; --slate:#141413; --clay:#D97757; --olive:#788C5D; --rust:#B04A3F;
    --g100:#F0EEE6; --g300:#D1CFC5; --g500:#87867F; --g700:#3D3D3A; --white:#FFFFFF;
    --serif:ui-serif,Georgia,serif; --sans:system-ui,sans-serif; --mono:ui-monospace,monospace;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:var(--sans); background:var(--ivory); color:var(--g700); line-height:1.55; padding:56px 24px; }
  .page { max-width:1100px; margin:0 auto; }
  h1 { font-family:var(--serif); font-size:34px; font-weight:500; color:var(--slate); margin-bottom:32px; }

  .grid { display:grid; grid-template-columns:repeat(3,1fr); gap:24px; }
  @media(max-width:900px){ .grid{ grid-template-columns:1fr; } }

  .card { background:var(--white); border:1.5px solid var(--g300); border-radius:14px; padding:28px; }
  .card.best { border-color:var(--slate); box-shadow:0 8px 24px rgba(20,20,19,.08); }
  .card h3 { font-family:var(--serif); font-size:20px; color:var(--slate); margin-bottom:12px; }
  .card .pros, .card .cons { margin-top:16px; }
  .card .pros li, .card .cons li { font-size:14px; margin:6px 0; list-style:none; }
  .card .pros li::before { content:"✓ "; color:var(--olive); }
  .card .cons li::before { content:"✗ "; color:var(--rust); }
  .badge { display:inline-block; font-family:var(--mono); font-size:10px; text-transform:uppercase;
    letter-spacing:0.06em; padding:3px 10px; border-radius:999px; background:var(--g100); color:var(--g700); margin-bottom:12px; }
  .badge.recommended { background:var(--slate); color:var(--ivory); }
</style>
</head>
<body>
<div class="page">
  <h1>Three Approaches</h1>
  <div class="grid">
    <div class="card">
      <span class="badge">Option A</span>
      <h3>Client-side Rendering</h3>
      <p>Render everything in the browser with React.</p>
      <ul class="pros"><li>Fast navigation</li><li>Rich interactions</li></ul>
      <ul class="cons"><li>Slower initial load</li><li>SEO challenges</li></ul>
    </div>
    <div class="card best">
      <span class="badge recommended">Recommended</span>
      <h3>Static Generation</h3>
      <p>Pre-render at build time, hydrate selectively.</p>
      <ul class="pros"><li>Fast load</li><li>Great SEO</li><li>Low server cost</li></ul>
      <ul class="cons"><li>Build time overhead</li></ul>
    </div>
    <div class="card">
      <span class="badge">Option C</span>
      <h3>Server Components</h3>
      <p>Render on server, stream to client.</p>
      <ul class="pros"><li>Zero JS by default</li><li>Automatic splitting</li></ul>
      <ul class="cons"><li>Newer pattern</li><li>Learning curve</li></ul>
    </div>
  </div>
</div>
</body>
</html>
```

## Minimal Interactive Explainer

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Interactive Explainer</title>
<style>
  :root {
    --ivory:#FAF9F5; --slate:#141413; --clay:#D97757; --olive:#788C5D;
    --g100:#F0EEE6; --g300:#D1CFC5; --g500:#87867F; --g700:#3D3D3A; --white:#FFFFFF;
    --serif:ui-serif,Georgia,serif; --sans:system-ui,sans-serif; --mono:ui-monospace,monospace;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:var(--sans); background:var(--ivory); color:var(--g700); line-height:1.6; padding:56px 24px; }
  .page { max-width:720px; margin:0 auto; }
  h1 { font-family:var(--serif); font-size:32px; font-weight:500; color:var(--slate); margin-bottom:12px; }
  .lead { font-size:16px; color:var(--g700); margin-bottom:40px; max-width:600px; }

  details { border:1.5px solid var(--g300); border-radius:12px; padding:16px 20px; margin-bottom:12px; }
  summary { font-weight:500; cursor:pointer; list-style:none; }
  summary::before { content:"▸"; margin-right:8px; color:var(--clay); display:inline-block; transition:transform 150ms; }
  details[open] summary::before { transform:rotate(90deg); }

  .demo { background:var(--white); border:1.5px solid var(--g300); border-radius:14px; padding:28px; margin:24px 0; }
  .demo input[type="range"] { width:100%; margin:16px 0; }
  .demo .output { font-family:var(--mono); font-size:14px; background:var(--g100); padding:16px; border-radius:8px; margin-top:16px; }
</style>
</head>
<body>
<div class="page">
  <h1>How Caching Works</h1>
  <p class="lead">A quick interactive explainer of TTL-based cache expiration.</p>

  <details>
    <summary>What is TTL?</summary>
    <p>Time To Live (TTL) is the duration a cached value remains valid before requiring a refresh.</p>
  </details>

  <details>
    <summary>When does eviction happen?</summary>
    <p>Eviction occurs when TTL expires, or when the cache reaches capacity and needs to make room.</p>
  </details>

  <div class="demo">
    <label>TTL (seconds): <span id="ttlVal">60</span></label>
    <input type="range" min="10" max="300" value="60" id="ttlSlider">
    <div class="output" id="result">Cache expires after 60s. Hit rate: ~85%</div>
  </div>
</div>
<script>
  const slider = document.getElementById('ttlSlider');
  const ttlVal = document.getElementById('ttlVal');
  const result = document.getElementById('result');
  slider.addEventListener('input', (e) => {
    const v = e.target.value;
    ttlVal.textContent = v;
    const hitRate = Math.min(95, 50 + (v / 10)).toFixed(0);
    result.textContent = `Cache expires after ${v}s. Hit rate: ~${hitRate}%`;
  });
</script>
</body>
</html>
```

## Minimal Flowchart

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Deploy Flow</title>
<style>
  :root {
    --ivory:#FAF9F5; --slate:#141413; --clay:#D97757; --olive:#788C5D; --rust:#B04A3F;
    --g100:#F0EEE6; --g300:#D1CFC5; --g500:#87867F; --g700:#3D3D3A; --white:#FFFFFF;
    --serif:ui-serif,Georgia,serif; --sans:system-ui,sans-serif; --mono:ui-monospace,monospace;
  }
  * { box-sizing:border-box; margin:0; padding:0; }
  body { font-family:var(--sans); background:var(--ivory); color:var(--g700); padding:56px 24px; }
  .page { max-width:900px; margin:0 auto; display:grid; grid-template-columns:1fr 280px; gap:32px; }
  @media(max-width:800px){ .page{ grid-template-columns:1fr; } }

  .canvas { background:var(--white); border:1.5px solid var(--g300); border-radius:14px; padding:28px; }
  svg { width:100%; height:auto; }
  .node { cursor:pointer; }
  .node rect { fill:var(--white); stroke:var(--g300); stroke-width:1.5; transition:stroke 150ms; }
  .node:hover rect { stroke:var(--clay); }
  .node text { font-family:var(--mono); font-size:12px; fill:var(--slate); pointer-events:none; }

  .panel { background:var(--white); border:1.5px solid var(--g300); border-radius:14px; padding:24px; }
  .panel h3 { font-family:var(--serif); font-size:18px; margin-bottom:8px; }
  .panel p { font-size:14px; color:var(--g700); }
</style>
</head>
<body>
<div class="page">
  <div class="canvas">
    <svg viewBox="0 0 400 300">
      <defs>
        <marker id="arrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
          <path d="M0,0 L0,6 L9,3 z" fill="var(--g300)"/>
        </marker>
      </defs>
      <g class="node" data-step="build" transform="translate(140,20)">
        <rect width="120" height="40" rx="6"/>
        <text x="60" y="25" text-anchor="middle">Build</text>
      </g>
      <g class="node" data-step="test" transform="translate(140,100)">
        <rect width="120" height="40" rx="6"/>
        <text x="60" y="25" text-anchor="middle">Test</text>
      </g>
      <g class="node" data-step="deploy" transform="translate(140,180)">
        <rect width="120" height="40" rx="6"/>
        <text x="60" y="25" text-anchor="middle">Deploy</text>
      </g>
      <line x1="200" y1="60" x2="200" y2="100" stroke="var(--g300)" stroke-width="1.5" marker-end="url(#arrow)"/>
      <line x1="200" y1="140" x2="200" y2="180" stroke="var(--g300)" stroke-width="1.5" marker-end="url(#arrow)"/>
    </svg>
  </div>
  <div class="panel" id="panel">
    <h3>Deploy Pipeline</h3>
    <p>Click a step to see details.</p>
  </div>
</div>
<script>
  const details = {
    build: { title: 'Build', desc: 'Compile assets and bundle dependencies. ~2min.' },
    test:  { title: 'Test',  desc: 'Run unit and integration tests. ~5min.' },
    deploy:{ title: 'Deploy',desc: 'Push to production with zero-downtime. ~1min.' }
  };
  document.querySelectorAll('.node').forEach(node => {
    node.addEventListener('click', () => {
      const d = details[node.dataset.step];
      document.getElementById('panel').innerHTML = `<h3>${d.title}</h3><p>${d.desc}</p>`;
    });
  });
</script>
</body>
</html>
```
