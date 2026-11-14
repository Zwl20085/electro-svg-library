# -*- coding: utf-8 -*-
"""
Generates index.html: Interactive ElectroSVG Studio
- Tab 1: Symbol & Circuit Library Explorer (124 IEEE/IEC SVGs, instant search, category filter, color/stroke customization, 1-click Copy SVG / Download)
- Tab 2: Interactive Scope & Waveform SVG Generator (Multi-channel oscilloscope / PWM / 3-phase / ZVS / CSV waveform plotter -> exports publication-ready vector SVG)
- Tab 3: Interactive Circuit & Block Diagram Canvas (Drag-and-drop components on a 10px grid, draw orthogonal wires, add math labels, export composite SVG)
"""

import os
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "catalog.json"), "r", encoding="utf-8") as f:
    catalog_data = json.load(f)

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>ElectroSVG Studio — IEEE/IEC Electrical Engineering Vector Library & Scope Generator</title>
  <style>
    :root {
      --bg: #f8fafc;
      --surface: #ffffff;
      --border: #e2e8f0;
      --text: #0f172a;
      --muted: #64748b;
      --primary: #1d4ed8;
      --primary-light: #eff6ff;
      --accent: #dc2626;
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.5;
    }
    header {
      background: #0f172a;
      color: #ffffff;
      padding: 18px 28px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
      border-bottom: 1px solid #1e293b;
    }
    .brand h1 {
      font-size: 20px;
      font-weight: 700;
      letter-spacing: -0.02em;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .brand p {
      font-size: 13px;
      color: #94a3b8;
      margin-top: 2px;
    }
    .badge {
      background: #1d4ed8;
      color: #fff;
      font-size: 11px;
      padding: 2px 8px;
      border-radius: 999px;
      font-weight: 600;
    }
    .nav-tabs {
      display: flex;
      gap: 8px;
    }
    .tab-btn {
      background: #1e293b;
      color: #cbd5e1;
      border: 1px solid #334155;
      padding: 8px 16px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }
    .tab-btn:hover { background: #334155; color: #fff; }
    .tab-btn.active { background: #2563eb; color: #fff; border-color: #3b82f6; }
    .container {
      max-width: 1500px;
      margin: 0 auto;
      padding: 24px;
    }
    .toolbar {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px 20px;
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 20px;
      box-shadow: 0 1px 2px rgba(0,0,0,0.03);
    }
    .search-box {
      flex: 1;
      min-width: 260px;
      padding: 9px 14px;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 14px;
    }
    .filter-pills {
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      margin-bottom: 20px;
    }
    .pill {
      background: var(--surface);
      border: 1px solid var(--border);
      color: var(--muted);
      padding: 6px 13px;
      border-radius: 999px;
      font-size: 12.5px;
      font-weight: 600;
      cursor: pointer;
      transition: all 0.15s;
    }
    .pill:hover { border-color: #94a3b8; color: var(--text); }
    .pill.active { background: var(--primary); color: #fff; border-color: var(--primary); }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(230px, 1fr));
      gap: 16px;
    }
    .grid.wide-cards {
      grid-template-columns: repeat(auto-fill, minmax(360px, 1fr));
    }
    .card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 14px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      transition: transform 0.12s, box-shadow 0.12s, border-color 0.12s;
    }
    .card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 20px rgba(15,23,42,0.06);
      border-color: #cbd5e1;
    }
    .preview-box {
      height: 150px;
      display: flex;
      align-items: center;
      justify-content: center;
      background: radial-gradient(#cbd5e1 0.75px, transparent 0.75px);
      background-size: 10px 10px;
      background-color: #fcfcfd;
      border: 1px solid #f1f5f9;
      border-radius: 6px;
      padding: 10px;
      overflow: hidden;
    }
    .card.wide .preview-box { height: 220px; }
    .preview-box svg {
      max-width: 100%;
      max-height: 100%;
      width: auto;
      height: auto;
    }
    .card-meta { margin-top: 10px; }
    .card-cat {
      font-size: 10.5px;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      color: var(--primary);
      font-weight: 700;
    }
    .card-title {
      font-size: 13.5px;
      font-weight: 600;
      color: var(--text);
      margin: 2px 0 8px;
    }
    .card-actions {
      display: flex;
      gap: 6px;
      margin-top: 6px;
    }
    .btn-sm {
      flex: 1;
      padding: 6px 8px;
      font-size: 11.5px;
      font-weight: 600;
      border: 1px solid var(--border);
      background: #f8fafc;
      color: var(--text);
      border-radius: 5px;
      cursor: pointer;
      text-align: center;
      text-decoration: none;
    }
    .btn-sm:hover { background: var(--primary); color: #fff; border-color: var(--primary); }
    .panel { display: none; }
    .panel.active { display: block; }
    /* Scope Generator Layout */
    .scope-workspace {
      display: grid;
      grid-template-columns: 360px 1fr;
      gap: 20px;
      align-items: start;
    }
    .control-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 18px;
    }
    .control-group { margin-bottom: 14px; }
    .control-group label {
      display: block;
      font-size: 12px;
      font-weight: 600;
      color: var(--muted);
      margin-bottom: 4px;
    }
    .control-group select, .control-group input {
      width: 100%;
      padding: 8px 10px;
      border: 1px solid var(--border);
      border-radius: 6px;
      font-size: 13px;
    }
    .btn-primary {
      background: var(--primary);
      color: #fff;
      border: none;
      padding: 9px 16px;
      border-radius: 6px;
      font-size: 13px;
      font-weight: 600;
      cursor: pointer;
    }
    .btn-primary:hover { background: #1e40af; }
    .toast {
      position: fixed;
      bottom: 24px;
      right: 24px;
      background: #0f172a;
      color: #fff;
      padding: 10px 18px;
      border-radius: 8px;
      font-size: 13px;
      font-weight: 600;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s;
      z-index: 999;
    }
    .toast.show { opacity: 1; }
  </style>
</head>
<body>

<header>
  <div class="brand">
    <h1>⚡ ElectroSVG Studio <span class="badge" id="total-count-badge">142 SVGs</span></h1>
    <p>Unified IEEE/IEC Publication Vector Symbol Library, Power Electronics Topologies, Machine Windings, Lab Instruments & Scope Plotter</p>
  </div>
  <div class="nav-tabs">
    <button class="tab-btn active" onclick="switchTab('library', this)">1. Symbol & Circuit Library</button>
    <button class="tab-btn" onclick="switchTab('scope', this)">2. Scope & Waveform SVG Generator</button>
    <button class="tab-btn" onclick="switchTab('guide', this)">3. Visio / Draw.io / LaTeX Guide</button>
  </div>
</header>

<div class="container">
  <!-- TAB 1: SYMBOL & CIRCUIT LIBRARY -->
  <div id="tab-library" class="panel active">
    <div class="toolbar">
      <input type="text" id="search-input" class="search-box" placeholder="Search 124 symbols & circuits (e.g., IGBT, SiC, PMSM, Wye, Hairpin, DAB, NPC, SVPWM, PLL, Scope)..." oninput="renderCatalog()"/>
      <div style="display:flex; gap:12px; align-items:center; font-size:13px;">
        <label>Stroke Width:
          <select id="stroke-select" onchange="updateGlobalStyle()" style="padding:5px 8px; border-radius:4px; border:1px solid #cbd5e1;">
            <option value="1.5">1.5 px (Fine)</option>
            <option value="2" selected>2.0 px (IEEE Standard)</option>
            <option value="2.5">2.5 px (Bold Presentation)</option>
          </select>
        </label>
        <a href="electro_svg_library.drawio.xml" download class="btn-primary" style="text-decoration:none;">⬇ Download Draw.io Library (.xml)</a>
      </div>
    </div>

    <div class="filter-pills" id="category-pills"></div>
    <div id="catalog-grid" class="grid"></div>
  </div>

  <!-- TAB 2: INTERACTIVE SCOPE & WAVEFORM SVG GENERATOR -->
  <div id="tab-scope" class="panel">
    <div class="scope-workspace">
      <div class="control-card">
        <h3 style="font-size:15px; margin-bottom:12px;">Publication Scope SVG Synthesizer</h3>
        <div class="control-group">
          <label>Preset Power Electronics / Motor Drive Scenario</label>
          <select id="scope-preset" onchange="renderCustomScope()">
            <option value="pwm_3ph">3-Phase Inverter SPWM + Sinusoidal Currents (v_ab, i_a, i_b, i_c)</option>
            <option value="buck_steady">Synchronous Buck Steady-State (v_gs, v_sw, i_L, v_o ripple)</option>
            <option value="dab_sps">Dual Active Bridge (DAB) Single-Phase-Shift (v_p, v_s, i_Lk)</option>
            <option value="foc_step">PMSM Drive Speed & Torque Step Response (ω_r, i_q, i_d, i_abc)</option>
          </select>
        </div>
        <div class="control-group">
          <label>Switching / Carrier Frequency Ratio (f_sw / f_0)</label>
          <input type="range" id="scope-freq" min="6" max="30" value="15" oninput="renderCustomScope()"/>
        </div>
        <div class="control-group">
          <label>Modulation Index / Duty Cycle / Phase Shift (m / D)</label>
          <input type="range" id="scope-mod" min="20" max="100" value="85" oninput="renderCustomScope()"/>
        </div>
        <div class="control-group">
          <label>Current Ripple / Harmonic Amplitude (%)</label>
          <input type="range" id="scope-ripple" min="5" max="50" value="18" oninput="renderCustomScope()"/>
        </div>
        <div class="control-group">
          <label>Timebase Annotation Label</label>
          <input type="text" id="scope-time-label" value="Time (2 ms/div)" oninput="renderCustomScope()"/>
        </div>
        <div style="display:flex; gap:8px; margin-top:16px;">
          <button class="btn-primary" style="flex:1;" onclick="copyGeneratedScope()">Copy Scope SVG</button>
          <button class="btn-primary" style="flex:1; background:#0f172a;" onclick="downloadGeneratedScope()">Download .SVG</button>
        </div>
      </div>

      <div class="control-card" style="display:flex; flex-direction:column; align-items:center;">
        <div style="width:100%; display:flex; justify-content:space-between; margin-bottom:10px;">
          <span style="font-size:13px; font-weight:600; color:#475569;">Live Vector Preview (100% Crisp Publication SVG)</span>
          <span style="font-size:12px; color:#64748b;">Font: Times New Roman Italic + Inter</span>
        </div>
        <div id="custom-scope-container" style="width:100%; background:#fff; border:1px solid #e2e8f0; border-radius:8px; padding:16px; display:flex; justify-content:center;"></div>
      </div>
    </div>
  </div>

  <!-- TAB 3: WORKFLOW GUIDE -->
  <div id="tab-guide" class="panel">
    <div class="control-card" style="max-width:900px; line-height:1.7;">
      <h2 style="margin-bottom:12px;">How to Use ElectroSVG Without Microsoft Visio</h2>
      <p style="margin-bottom:14px;">All <strong>124 vector symbols, circuit topologies, machine cross-sections, winding diagrams, and oscilloscope templates</strong> share a strict mathematical grid (10 px snap), uniform 2.0 px rounded strokes, and IEEE Transactions typography.</p>
      <h3 style="margin-top:16px; font-size:16px;">Option A: Free Drag-and-Drop in Draw.io / diagrams.net (Recommended Visio Replacement)</h3>
      <ol style="margin-left:20px; margin-top:6px; margin-bottom:14px;">
        <li>Open <a href="https://app.diagrams.net/" target="_blank">app.diagrams.net</a> (or the VS Code Draw.io extension).</li>
        <li>Click <strong>File → Open Library from → Device...</strong> and select <code>electro_svg_library.drawio.xml</code> from this workspace.</li>
        <li>All 124 electrical engineering symbols appear in your sidebar stencil! Drag them onto the canvas, connect orthogonal wires, and export directly to PDF or SVG for your IEEE LaTeX / Word paper.</li>
      </ol>
      <h3 style="margin-top:16px; font-size:16px;">Option B: Direct SVG Composition in Inkscape / Illustrator / Figma</h3>
      <ol style="margin-left:20px; margin-top:6px; margin-bottom:14px;">
        <li>Click <strong>Copy SVG</strong> on any symbol card in Tab 1 and press <code>Ctrl+V</code> directly inside Figma, Inkscape, Adobe Illustrator, or PowerPoint.</li>
        <li>Or browse individual categorized files inside the <code>symbols/</code> folder (<code>01_passives</code> through <code>09_scope_waveforms</code>).</li>
      </ol>
    </div>
  </div>
</div>

<div id="toast" class="toast">Copied SVG to clipboard!</div>

<script>
const CATALOG = __CATALOG_JSON__;

const CATEGORY_LABELS = {
  "all": "All Symbols (" + CATALOG.length + ")",
  "01_passives": "01. Passives & Magnetics",
  "02_sources_grounds": "02. Sources & Grounds",
  "03_semiconductors": "03. Power Devices (IGBT/SiC/GaN)",
  "04_transformers_windings": "04. Transformers & Windings",
  "05_electrical_machines": "05. Electrical Machines & Rotors",
  "06_control_blocks": "06. Control & dq Transforms",
  "07_sensors_protection": "07. Sensors & Switchgear",
  "08_power_topologies": "08. Converter Topologies",
  "09_scope_waveforms": "09. Scope & Waveform Figures",
  "10_measurement_instruments": "10. Lab & Read Instruments"
};

let activeCategory = "all";

function initPills() {
  const container = document.getElementById("category-pills");
  container.innerHTML = "";
  Object.keys(CATEGORY_LABELS).forEach(cat => {
    const btn = document.createElement("button");
    btn.className = "pill" + (cat === activeCategory ? " active" : "");
    btn.textContent = CATEGORY_LABELS[cat];
    btn.onclick = () => {
      activeCategory = cat;
      initPills();
      renderCatalog();
    };
    container.appendChild(btn);
  });
}

function renderCatalog() {
  const q = document.getElementById("search-input").value.toLowerCase().trim();
  const grid = document.getElementById("catalog-grid");
  grid.innerHTML = "";

  const filtered = CATALOG.filter(item => {
    const matchCat = (activeCategory === "all") || (item.category === activeCategory);
    if (!matchCat) return false;
    if (!q) return true;
    const hay = (item.name + " " + item.slug + " " + item.category + " " + item.tags.join(" ")).toLowerCase();
    return hay.includes(q);
  });

  document.getElementById("total-count-badge").textContent = filtered.length + " SVGs";

  filtered.forEach((item, idx) => {
    const isWide = item.width >= 200;
    const card = document.createElement("div");
    card.className = "card" + (isWide ? " wide" : "");
    if (isWide) card.style.gridColumn = "span 2";

    card.innerHTML = `
      <div>
        <div class="preview-box">${item.svg}</div>
        <div class="card-meta">
          <div class="card-cat">${CATEGORY_LABELS[item.category] || item.category}</div>
          <div class="card-title">${item.name}</div>
        </div>
      </div>
      <div class="card-actions">
        <button class="btn-sm" onclick="copySvgBySlug('${item.slug}')">📋 Copy SVG</button>
        <a class="btn-sm" href="${item.path}" download="${item.slug}.svg">⬇ .SVG</a>
      </div>
    `;
    grid.appendChild(card);
  });
}

function copySvgBySlug(slug) {
  const item = CATALOG.find(x => x.slug === slug);
  if (!item) return;
  navigator.clipboard.writeText(item.svg).then(() => showToast("Copied " + item.name + " SVG!"));
}

function updateGlobalStyle() {
  const sw = document.getElementById("stroke-select").value;
  document.querySelectorAll(".ee-stroke").forEach(el => {
    el.style.strokeWidth = sw + "px";
  });
}

function switchTab(tabId, btn) {
  document.querySelectorAll(".panel").forEach(p => p.classList.remove("active"));
  document.querySelectorAll(".tab-btn").forEach(b => b.classList.remove("active"));
  document.getElementById("tab-" + tabId).classList.add("active");
  btn.classList.add("active");
  if (tabId === "scope") renderCustomScope();
}

function showToast(msg) {
  const t = document.getElementById("toast");
  t.textContent = msg;
  t.classList.add("show");
  setTimeout(() => t.classList.remove("show"), 2000);
}

// =========================================================
// TAB 2: PARAMETRIC PUBLICATION SCOPE SVG SYNTHESIZER
// =========================================================
let currentScopeSvg = "";

function renderCustomScope() {
  const preset = document.getElementById("scope-preset").value;
  const fRatio = parseInt(document.getElementById("scope-freq").value, 10);
  const mod = parseInt(document.getElementById("scope-mod").value, 10) / 100.0;
  const ripple = parseInt(document.getElementById("scope-ripple").value, 10) / 100.0;
  const timeLabel = document.getElementById("scope-time-label").value;

  const W = 680, H = 400;
  const x0 = 68, y0 = 28, pw = 580, ph = 330;

  let traces = "";
  let labels = "";

  if (preset === "pwm_3ph") {
    // Channel 1: SPWM Line-to-Line Voltage v_ab
    let pwmPath = `M ${x0} ${y0+75}`;
    const N = fRatio * 2;
    const dx = pw / N;
    for (let k = 0; k < N; k++) {
      const xStart = x0 + k * dx;
      const theta = 2 * Math.PI * (k / N);
      const sVal = mod * Math.sin(theta);
      const duty = Math.max(0.08, Math.min(0.92, Math.abs(sVal)));
      const yBase = y0 + 75;
      const yPeak = sVal >= 0 ? (y0 + 25) : (y0 + 125);
      const xOn = xStart + (1 - duty) * 0.5 * dx;
      const xOff = xStart + (1 + duty) * 0.5 * dx;
      pwmPath += ` L ${xOn.toFixed(1)} ${yBase} L ${xOn.toFixed(1)} ${yPeak} L ${xOff.toFixed(1)} ${yPeak} L ${xOff.toFixed(1)} ${yBase} L ${(xStart+dx).toFixed(1)} ${yBase}`;
    }
    // Channels 2-4: 3-phase currents i_a, i_b, i_c with switching ripple
    let ptsA = [], ptsB = [], ptsC = [];
    for (let i = 0; i <= 360; i++) {
      const x = x0 + (i / 360) * pw;
      const th = 2 * Math.PI * (i / 360);
      const rip = ripple * 18 * Math.sin(fRatio * th);
      const ya = y0 + 245 - 65 * mod * Math.sin(th) - rip;
      const yb = y0 + 245 - 65 * mod * Math.sin(th - 2*Math.PI/3) - rip*0.8;
      const yc = y0 + 245 - 65 * mod * Math.sin(th + 2*Math.PI/3) + rip*0.8;
      ptsA.push(`${x.toFixed(1)},${ya.toFixed(1)}`);
      ptsB.push(`${x.toFixed(1)},${yb.toFixed(1)}`);
      ptsC.push(`${x.toFixed(1)},${yc.toFixed(1)}`);
    }
    traces = `
      <path d="${pwmPath}" fill="none" stroke="#1e293b" stroke-width="1.4"/>
      <polyline points="${ptsA.join(' ')}" fill="none" stroke="#dc2626" stroke-width="2"/>
      <polyline points="${ptsB.join(' ')}" fill="none" stroke="#16a34a" stroke-width="2"/>
      <polyline points="${ptsC.join(' ')}" fill="none" stroke="#2563eb" stroke-width="2"/>
    `;
    labels = `
      <text x="34" y="${y0+75}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">v<tspan dy="3" font-size="10">ab</tspan></text>
      <text x="34" y="${y0+245}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">i<tspan dy="3" font-size="10">abc</tspan></text>
    `;
  } else if (preset === "buck_steady") {
    const N = Math.max(4, Math.floor(fRatio / 3));
    const dx = pw / N;
    let vgs = `M ${x0} ${y0+75}`, vsw = `M ${x0} ${y0+155}`, iL = `M ${x0} ${y0+240}`, vo = [];
    for (let k = 0; k < N; k++) {
      const xs = x0 + k * dx;
      const xm = xs + mod * dx;
      const xe = xs + dx;
      vgs += ` L ${xs.toFixed(1)} ${y0+30} L ${xm.toFixed(1)} ${y0+30} L ${xm.toFixed(1)} ${y0+75} L ${xe.toFixed(1)} ${y0+75}`;
      vsw += ` L ${xs.toFixed(1)} ${y0+105} L ${xm.toFixed(1)} ${y0+105} L ${xm.toFixed(1)} ${y0+155} L ${xe.toFixed(1)} ${y0+155}`;
      const dI = 35 * ripple;
      iL += ` L ${xs.toFixed(1)} ${(y0+230+dI).toFixed(1)} L ${xm.toFixed(1)} ${(y0+230-dI).toFixed(1)} L ${xe.toFixed(1)} ${(y0+230+dI).toFixed(1)}`;
    }
    for (let i = 0; i <= 240; i++) {
      const x = x0 + (i / 240) * pw;
      const y = y0 + 305 - 12 * ripple * Math.sin(N * 2 * Math.PI * (i / 240) - 0.6);
      vo.push(`${x.toFixed(1)},${y.toFixed(1)}`);
    }
    traces = `
      <path d="${vgs}" fill="none" stroke="#2563eb" stroke-width="2"/>
      <path d="${vsw}" fill="none" stroke="#dc2626" stroke-width="2"/>
      <path d="${iL}" fill="none" stroke="#16a34a" stroke-width="2"/>
      <polyline points="${vo.join(' ')}" fill="none" stroke="#d97706" stroke-width="2"/>
    `;
    labels = `
      <text x="34" y="${y0+55}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">v<tspan dy="3" font-size="10">gs</tspan></text>
      <text x="34" y="${y0+130}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">v<tspan dy="3" font-size="10">sw</tspan></text>
      <text x="34" y="${y0+230}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">i<tspan dy="3" font-size="10">L</tspan></text>
      <text x="34" y="${y0+305}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">Δv<tspan dy="3" font-size="10">o</tspan></text>
    `;
  } else if (preset === "dab_sps") {
    const N = 3;
    const dx = pw / N;
    const shift = mod * 0.35 * dx;
    let vp = `M ${x0} ${y0+65}`, vs = `M ${x0} ${y0+155}`, ilk = `M ${x0} ${y0+265}`;
    for (let k = 0; k < N; k++) {
      const xs = x0 + k * dx;
      const xh = xs + 0.5 * dx;
      const xe = xs + dx;
      vp += ` L ${xs.toFixed(1)} ${y0+30} L ${xh.toFixed(1)} ${y0+30} L ${xh.toFixed(1)} ${y0+100} L ${xe.toFixed(1)} ${y0+100}`;
      const x1 = xs + shift, x2 = xh + shift;
      vs += ` L ${xs.toFixed(1)} ${y0+190} L ${x1.toFixed(1)} ${y0+190} L ${x1.toFixed(1)} ${y0+120} L ${x2.toFixed(1)} ${y0+120} L ${x2.toFixed(1)} ${y0+190} L ${xe.toFixed(1)} ${y0+190}`;
      ilk += ` L ${xs.toFixed(1)} ${y0+295} L ${x1.toFixed(1)} ${y0+230} L ${xh.toFixed(1)} ${y0+220} L ${x2.toFixed(1)} ${y0+285} L ${xe.toFixed(1)} ${y0+295}`;
    }
    traces = `
      <path d="${vp}" fill="none" stroke="#2563eb" stroke-width="2"/>
      <path d="${vs}" fill="none" stroke="#dc2626" stroke-width="2"/>
      <path d="${ilk}" fill="none" stroke="#16a34a" stroke-width="2.2"/>
    `;
    labels = `
      <text x="34" y="${y0+65}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">v<tspan dy="3" font-size="10">p</tspan></text>
      <text x="34" y="${y0+155}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">v<tspan dy="3" font-size="10">s</tspan></text>
      <text x="34" y="${y0+260}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">i<tspan dy="3" font-size="10">Lk</tspan></text>
    `;
  } else {
    // FOC Step Response
    let wr = [], iq = [], id = [], ia = [];
    for (let i = 0; i <= 300; i++) {
      const x = x0 + (i / 300) * pw;
      const t = i / 300;
      const step = t > 0.25 ? (1 - Math.exp(-(t - 0.25) * 14)) : 0;
      const y_wr = y0 + 80 - 45 * mod * step;
      const y_iq = y0 + 175 - (t > 0.25 && t < 0.45 ? 45 * mod : 18 * mod) + 4 * ripple * Math.sin(t * 150);
      const y_id = y0 + 225 + 4 * ripple * Math.cos(t * 150);
      const freq = 4 + 10 * step;
      const amp = (t > 0.25 && t < 0.45) ? 38 : 20;
      const y_ia = y0 + 290 - amp * mod * Math.sin(2 * Math.PI * freq * t);
      wr.push(`${x.toFixed(1)},${y_wr.toFixed(1)}`);
      iq.push(`${x.toFixed(1)},${y_iq.toFixed(1)}`);
      id.push(`${x.toFixed(1)},${y_id.toFixed(1)}`);
      ia.push(`${x.toFixed(1)},${y_ia.toFixed(1)}`);
    }
    traces = `
      <polyline points="${wr.join(' ')}" fill="none" stroke="#1d4ed8" stroke-width="2.2"/>
      <polyline points="${iq.join(' ')}" fill="none" stroke="#dc2626" stroke-width="2"/>
      <polyline points="${id.join(' ')}" fill="none" stroke="#16a34a" stroke-width="1.8"/>
      <polyline points="${ia.join(' ')}" fill="none" stroke="#d97706" stroke-width="1.8"/>
    `;
    labels = `
      <text x="34" y="${y0+60}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">ω<tspan dy="3" font-size="10">r</tspan></text>
      <text x="34" y="${y0+160}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">i<tspan dy="3" font-size="10">q</tspan></text>
      <text x="34" y="${y0+225}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">i<tspan dy="3" font-size="10">d</tspan></text>
      <text x="34" y="${y0+290}" font-family="Times New Roman, serif" font-style="italic" font-size="14" text-anchor="middle">i<tspan dy="3" font-size="10">a</tspan></text>
    `;
  }

  let gridLines = "";
  for (let gx = 1; gx < 10; gx++) {
    const x = x0 + (gx / 10) * pw;
    gridLines += `<line x1="${x.toFixed(1)}" y1="${y0}" x2="${x.toFixed(1)}" y2="${y0+ph}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3 3"/>`;
  }
  for (let gy = 1; gy < 6; gy++) {
    const y = y0 + (gy / 6) * ph;
    gridLines += `<line x1="${x0}" y1="${y.toFixed(1)}" x2="${x0+pw}" y2="${y.toFixed(1)}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3 3"/>`;
  }

  currentScopeSvg = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ${W} ${H}" width="${W}" height="${H}">
  <rect x="2" y="2" width="${W-4}" height="${H-4}" rx="6" fill="#f8fafc" stroke="#0f172a" stroke-width="2"/>
  <rect x="${x0}" y="${y0}" width="${pw}" height="${ph}" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>
  ${gridLines}
  ${traces}
  ${labels}
  <text x="${x0 + pw/2}" y="${H - 14}" font-family="Inter, Arial, sans-serif" font-size="12" font-weight="600" fill="#334155" text-anchor="middle">${timeLabel}</text>
</svg>`;

  document.getElementById("custom-scope-container").innerHTML = currentScopeSvg;
}

function copyGeneratedScope() {
  navigator.clipboard.writeText(currentScopeSvg).then(() => showToast("Copied custom Scope SVG!"));
}

function downloadGeneratedScope() {
  const blob = new Blob([currentScopeSvg], {type: "image/svg+xml"});
  const url = URL.createObjectURL(blob);
  const a = document.createElement("a");
  a.href = url;
  a.download = "custom_scope_waveform.svg";
  a.click();
  URL.revokeObjectURL(url);
}

initPills();
renderCatalog();
</script>
</body>
</html>
"""

html_out = HTML_TEMPLATE.replace("__CATALOG_JSON__", json.dumps(catalog_data))
with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(html_out)

print("Built index.html successfully.")
