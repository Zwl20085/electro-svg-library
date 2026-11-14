# -*- coding: utf-8 -*-
"""
Builds:
1. master_sprite.svg (Unified <symbol> sprite sheet of all 124 symbols)
2. electro_svg_library.drawio.xml (Native Draw.io / diagrams.net drag-and-drop stencil library)
3. index.html (Interactive ElectroSVG Studio: Searchable Catalog + Scope SVG Generator + Schematic Composer)
"""

import os
import json
import base64
import urllib.parse
from xml.sax.saxutils import escape as xml_escape

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE_DIR, "catalog.json"), "r", encoding="utf-8") as f:
    CATALOG = json.load(f)

# 1. Build master_sprite.svg
from generate_library import STYLE_DEFS

sprite_symbols = []
for item in CATALOG:
    svg_txt = item["svg"]
    # Extract inner body after </defs> and before </svg>
    start_idx = svg_txt.find("</defs>")
    end_idx = svg_txt.rfind("</svg>")
    inner = svg_txt[start_idx + len("</defs>"):end_idx].strip()
    # Normalize scoped marker references back to master sprite's shared #arrow, #arrow-red, #arrow-blue
    slug = item["slug"]
    inner = inner.replace(f'url(#arrow-{slug})', 'url(#arrow)') \
                 .replace(f'url(#arrow-red-{slug})', 'url(#arrow-red)') \
                 .replace(f'url(#arrow-blue-{slug})', 'url(#arrow-blue)')
    w, h = item["width"], item["height"]
    sprite_symbols.append(f'  <symbol id="{item["slug"]}" viewBox="0 0 {w} {h}">\n    {inner}\n  </symbol>')

master_sprite = f"""<svg xmlns="http://www.w3.org/2000/svg" style="display:none">
{STYLE_DEFS}
{chr(10).join(sprite_symbols)}
</svg>
"""

with open(os.path.join(BASE_DIR, "master_sprite.svg"), "w", encoding="utf-8") as f:
    f.write(master_sprite)

# 2. Build Draw.io / diagrams.net Library (electro_svg_library.drawio.xml)
drawio_items = []
for item in CATALOG:
    b64_svg = base64.b64encode(item["svg"].encode("utf-8")).decode("ascii")
    data_uri = f"data:image/svg+xml;base64,{b64_svg}"
    drawio_items.append({
        "data": data_uri,
        "w": item["width"],
        "h": item["height"],
        "title": item["name"],
        "aspect": "fixed"
    })

drawio_xml = f"<mxlibrary>{xml_escape(json.dumps(drawio_items))}</mxlibrary>"
with open(os.path.join(BASE_DIR, "electro_svg_library.drawio.xml"), "w", encoding="utf-8") as f:
    f.write(drawio_xml)

print("Built master_sprite.svg and electro_svg_library.drawio.xml.")
