# -*- coding: utf-8 -*-
"""
ElectroSVG Master Library Generator
Generates publication-grade IEEE/IEC SVG symbols, power electronics circuits,
electrical machine & winding diagrams, control diagrams, and scope/waveform templates.
"""

import os
import json
import math
from xml.sax.saxutils import escape as xml_escape

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SYMBOLS_DIR = os.path.join(BASE_DIR, "symbols")

STYLE_DEFS = """  <defs>
    <style>
      .ee-stroke { stroke: #111827; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .ee-thin { stroke: #111827; stroke-width: 1.3; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .ee-thick { stroke: #111827; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .ee-dashed { stroke: #4b5563; stroke-width: 1.5; stroke-dasharray: 4 3; stroke-linecap: round; fill: none; }
      .ee-fill { fill: #111827; stroke: #111827; stroke-width: 1.5; stroke-linejoin: round; }
      .ee-body { fill: #f8fafc; stroke: #111827; stroke-width: 2; stroke-linejoin: round; }
      .ee-tint-blue { fill: #eff6ff; stroke: #1d4ed8; stroke-width: 1.8; stroke-linejoin: round; }
      .ee-tint-red { fill: #fef2f2; stroke: #b91c1c; stroke-width: 1.8; stroke-linejoin: round; }
      .ee-tint-green { fill: #f0fdf4; stroke: #15803d; stroke-width: 1.8; stroke-linejoin: round; }
      .ee-tint-amber { fill: #fffbeb; stroke: #b45309; stroke-width: 1.8; stroke-linejoin: round; }
      .ee-wire-a { stroke: #dc2626; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .ee-wire-b { stroke: #16a34a; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .ee-wire-c { stroke: #2563eb; stroke-width: 2; stroke-linecap: round; stroke-linejoin: round; fill: none; }
      .ee-text { font-family: 'Times New Roman', 'STIX Two Text', Georgia, serif; font-size: 13px; font-style: italic; fill: #111827; text-anchor: middle; dominant-baseline: central; }
      .ee-label { font-family: 'Inter', 'Helvetica Neue', Arial, sans-serif; font-size: 10px; font-weight: 600; fill: #374151; text-anchor: middle; dominant-baseline: central; }
      .ee-pin { fill: #ffffff; stroke: #111827; stroke-width: 1.6; }
      .ee-node { fill: #111827; stroke: none; }
      .ee-grid { stroke: #e5e7eb; stroke-width: 0.8; stroke-dasharray: 2 2; fill: none; }
    </style>
    <marker id="arrow" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 7 4 L 0 7 z" fill="#111827"/>
    </marker>
    <marker id="arrow-red" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 7 4 L 0 7 z" fill="#dc2626"/>
    </marker>
    <marker id="arrow-blue" viewBox="0 0 8 8" refX="6" refY="4" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M 0 1 L 7 4 L 0 7 z" fill="#2563eb"/>
    </marker>
  </defs>"""

def wrap_svg(body, width=100, height=100, title="", desc="", slug="sym"):
    safe_title = xml_escape(title)
    safe_desc = xml_escape(desc)
    # Scope marker IDs per symbol so multiple inline SVGs in HTML never collide
    scoped_defs = STYLE_DEFS.replace('id="arrow"', f'id="arrow-{slug}"') \
                            .replace('id="arrow-red"', f'id="arrow-red-{slug}"') \
                            .replace('id="arrow-blue"', f'id="arrow-blue-{slug}"')
    scoped_body = body.replace('url(#arrow)', f'url(#arrow-{slug})') \
                      .replace('url(#arrow-red)', f'url(#arrow-red-{slug})') \
                      .replace('url(#arrow-blue)', f'url(#arrow-blue-{slug})')
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <title>{safe_title}</title>
  <desc>{safe_desc}</desc>
{scoped_defs}
{scoped_body}
</svg>
"""

CATALOG = []

def save_symbol(category, slug, name, body, width=100, height=100, tags=None, desc=""):
    cat_dir = os.path.join(SYMBOLS_DIR, category)
    os.makedirs(cat_dir, exist_ok=True)
    rel_path = f"symbols/{category}/{slug}.svg"
    full_path = os.path.join(BASE_DIR, rel_path)
    svg_str = wrap_svg(body.strip("\n"), width=width, height=height, title=name, desc=desc or name, slug=slug)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(svg_str)
    CATALOG.append({
        "category": category,
        "slug": slug,
        "name": name,
        "path": rel_path,
        "width": width,
        "height": height,
        "tags": tags or [],
        "desc": desc or name,
        "svg": svg_str
    })

def pin(x, y):
    return f'  <circle class="ee-pin" cx="{x}" cy="{y}" r="2.2"/>'

def node(x, y):
    return f'  <circle class="ee-node" cx="{x}" cy="{y}" r="2.5"/>'

def generate_all():
    from gen_part1_passives_sources import register_part1
    from gen_part2_semiconductors import register_part2
    from gen_part3_machines_windings import register_part3
    from gen_part4_control_protection import register_part4
    from gen_part5_topologies_scopes import register_part5
    from gen_part6_extra import register_part6
    from gen_part7_instruments import register_part7

    register_part1(save_symbol, pin, node)
    register_part2(save_symbol, pin, node)
    register_part3(save_symbol, pin, node)
    register_part4(save_symbol, pin, node)
    register_part5(save_symbol, pin, node)
    register_part6(save_symbol, pin, node)
    register_part7(save_symbol, pin, node)

    catalog_path = os.path.join(BASE_DIR, "catalog.json")
    with open(catalog_path, "w", encoding="utf-8") as f:
        json.dump(CATALOG, f, indent=2)
    print(f"Generated {len(CATALOG)} symbols and templates successfully.")

if __name__ == "__main__":
    generate_all()
