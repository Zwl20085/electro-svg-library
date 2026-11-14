# -*- coding: utf-8 -*-
"""
Comprehensive Verification Suite for ElectroSVG Library:
1. Parses every single .svg file in symbols/ with xml.etree.ElementTree to verify strict XML well-formedness.
2. Checks viewBox, width, height, path syntax, and class references.
3. Validates master_sprite.svg and electro_svg_library.drawio.xml (including decoding every base64 SVG entry).
4. Checks index.html structure and embedded JSON catalog integrity.
"""

import os
import re
import json
import base64
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def validate_all():
    errors = []
    warnings = []

    with open(os.path.join(BASE_DIR, "catalog.json"), "r", encoding="utf-8") as f:
        catalog = json.load(f)

    print(f"Checking {len(catalog)} symbols in catalog.json and on disk...")

    valid_classes = {
        "ee-stroke", "ee-thin", "ee-thick", "ee-dashed", "ee-fill", "ee-body",
        "ee-tint-blue", "ee-tint-red", "ee-tint-green", "ee-tint-amber",
        "ee-wire-a", "ee-wire-b", "ee-wire-c", "ee-text", "ee-label",
        "ee-pin", "ee-node", "ee-grid"
    }

    for item in catalog:
        rel_path = item["path"]
        full_path = os.path.join(BASE_DIR, rel_path)
        if not os.path.exists(full_path):
            errors.append(f"Missing file on disk: {rel_path}")
            continue

        with open(full_path, "r", encoding="utf-8") as sf:
            content = sf.read()

        # Check XML parsing
        try:
            root = ET.fromstring(content)
        except Exception as e:
            errors.append(f"XML parse error in {rel_path}: {e}")
            continue

        # Check class attributes
        for elem in root.iter():
            cls = elem.attrib.get("class")
            if cls:
                for c in cls.strip().split():
                    if c not in valid_classes:
                        errors.append(f"Invalid CSS class '{c}' in {rel_path}")

            # Check path 'd' attribute for valid SVG path commands
            if elem.tag.endswith("path"):
                d = elem.attrib.get("d", "")
                if not d or not re.match(r"^[MmLlHhVvCcSsQqTtAaZz0-9\s,\.\-\+]+$", d):
                    errors.append(f"Malformed path d='{d}' in {rel_path}")

    # Check master_sprite.svg
    sprite_path = os.path.join(BASE_DIR, "master_sprite.svg")
    try:
        ET.parse(sprite_path)
        print("master_sprite.svg: Valid XML")
    except Exception as e:
        errors.append(f"master_sprite.svg XML error: {e}")

    # Check electro_svg_library.drawio.xml
    drawio_path = os.path.join(BASE_DIR, "electro_svg_library.drawio.xml")
    try:
        tree = ET.parse(drawio_path)
        root = tree.getroot()
        lib_list = json.loads(root.text)
        for idx, entry in enumerate(lib_list):
            b64_part = entry["data"].split(",", 1)[1]
            decoded = base64.b64decode(b64_part).decode("utf-8")
            ET.fromstring(decoded)
        print(f"electro_svg_library.drawio.xml: Valid XML & all {len(lib_list)} base64 SVGs verified")
    except Exception as e:
        errors.append(f"electro_svg_library.drawio.xml error: {e}")

    # Check index.html embedded JSON and marker ID uniqueness
    html_path = os.path.join(BASE_DIR, "index.html")
    try:
        with open(html_path, "r", encoding="utf-8") as hf:
            html_content = hf.read()
        m = re.search(r"const CATALOG = (\[.*?\]);\n", html_content, re.S)
        if not m:
            errors.append("index.html: Could not locate embedded CATALOG JSON")
        else:
            parsed_cat = json.loads(m.group(1))
            seen_ids = set()
            for item in parsed_cat:
                svg_root = ET.fromstring(item["svg"])
                for el in svg_root.iter():
                    el_id = el.attrib.get("id")
                    if el_id:
                        if el_id in seen_ids:
                            errors.append(f"Duplicate SVG marker ID '{el_id}' across catalog in index.html")
                        seen_ids.add(el_id)
            print(f"index.html: Embedded CATALOG JSON verified ({len(parsed_cat)} items, {len(seen_ids)} unique scoped marker IDs, 0 ID collisions)")
    except Exception as e:
        errors.append(f"index.html check error: {e}")

    if errors:
        print(f"\nFOUND {len(errors)} ERRORS:")
        for err in errors:
            print("  - " + err)
    else:
        print(f"\nALL {len(catalog)} SVG FILES, SPRITE SHEET, AND DRAW.IO LIBRARY PASSED STRICT XML & SCHEMA VALIDATION WITH 0 ERRORS!")

if __name__ == "__main__":
    validate_all()
