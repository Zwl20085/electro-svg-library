# -*- coding: utf-8 -*-
"""
Part 3: Electrical Machines, Windings, and Transformers
"""

def register_part3(save_symbol, pin, node):
    # ==========================================
    # CATEGORY 04: TRANSFORMERS & WINDING CONNECTIONS
    # ==========================================
    cat_tx = "04_transformers_windings"

    # 1. Single-Phase Two-Winding Transformer (Iron Core with Polarity Dots)
    save_symbol(cat_tx, "transformer_1ph_2w", "1-Phase 2-Winding Transformer (Iron Core)", f"""
  <path class="ee-stroke" d="M 12 22 L 34 22 A 7 7 0 0 1 34 36 A 7 7 0 0 1 34 50 A 7 7 0 0 1 34 64 A 7 7 0 0 1 34 78 L 12 78"/>
  <line class="ee-stroke" x1="47" y1="20" x2="47" y2="80"/>
  <line class="ee-stroke" x1="53" y1="20" x2="53" y2="80"/>
  <path class="ee-stroke" d="M 88 22 L 66 22 A 7 7 0 0 0 66 36 A 7 7 0 0 0 66 50 A 7 7 0 0 0 66 64 A 7 7 0 0 0 66 78 L 88 78"/>
  <circle class="ee-node" cx="26" cy="28" r="2.2"/>
  <circle class="ee-node" cx="74" cy="28" r="2.2"/>
  <text class="ee-label" x="50" y="10">N<tspan dy="2" font-size="7">1</tspan> : N<tspan dy="2" font-size="7">2</tspan></text>
{pin(12, 22)}
{pin(12, 78)}
{pin(88, 22)}
{pin(88, 78)}
""", tags=["transformer", "1-phase", "galvanic isolation", "iron core", "dot convention"])

    # 2. High-Frequency Center-Tapped Transformer (Ferrite Core for LLC / Push-Pull / Full-Bridge)
    save_symbol(cat_tx, "transformer_hf_center_tapped", "High-Frequency Center-Tapped Transformer", f"""
  <path class="ee-stroke" d="M 12 22 L 34 22 A 7 7 0 0 1 34 36 A 7 7 0 0 1 34 50 A 7 7 0 0 1 34 64 A 7 7 0 0 1 34 78 L 12 78"/>
  <line class="ee-dashed" x1="47" y1="18" x2="47" y2="82"/>
  <line class="ee-dashed" x1="53" y1="18" x2="53" y2="82"/>
  <path class="ee-stroke" d="M 88 18 L 66 18 A 7 7.5 0 0 0 66 34 A 7 7.5 0 0 0 66 50 A 7 7.5 0 0 0 66 66 A 7 7.5 0 0 0 66 82 L 88 82"/>
  <line class="ee-stroke" x1="66" y1="50" x2="88" y2="50"/>
  <circle class="ee-node" cx="26" cy="28" r="2.2"/>
  <circle class="ee-node" cx="74" cy="24" r="2.2"/>
  <circle class="ee-node" cx="74" cy="56" r="2.2"/>
{node(66, 50)}
{pin(12, 22)}
{pin(12, 78)}
{pin(88, 18)}
{pin(88, 50)}
{pin(88, 82)}
""", tags=["transformer", "center tapped", "high frequency", "ferrite", "llc", "push pull"])

    # 3. Three-Winding Transformer (Tertiary Winding / Multi-port DAB)
    save_symbol(cat_tx, "transformer_3winding_iec", "Three-Winding Power Transformer (IEC Overlapping Circles)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="26" y2="50"/>
  <circle class="ee-stroke" cx="42" cy="50" r="16"/>
  <circle class="ee-stroke" cx="62" cy="36" r="16"/>
  <circle class="ee-stroke" cx="62" cy="64" r="16"/>
  <line class="ee-stroke" x1="78" y1="36" x2="92" y2="36"/>
  <line class="ee-stroke" x1="78" y1="64" x2="92" y2="64"/>
  <text class="ee-label" x="34" y="50">Y</text>
  <text class="ee-label" x="66" y="34">Y</text>
  <text class="ee-label" x="66" y="66">Δ</text>
{pin(10, 50)}
{pin(92, 36)}
{pin(92, 64)}
""", tags=["transformer", "3-winding", "iec", "single line", "power system", "tab"])

    # 4. Two-Winding Transformer (IEC Overlapping Circles for Single-Line Diagrams)
    save_symbol(cat_tx, "transformer_2winding_iec", "Two-Winding Power Transformer (IEC Single-Line)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="26" y2="50"/>
  <circle class="ee-stroke" cx="42" cy="50" r="16"/>
  <circle class="ee-stroke" cx="60" cy="50" r="16"/>
  <line class="ee-stroke" x1="76" y1="50" x2="90" y2="50"/>
  <text class="ee-label" x="35" y="50">Δ</text>
  <text class="ee-label" x="67" y="50">Y</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["transformer", "iec", "single line diagram", "sld", "power system"])

    # 5. Autotransformer (Variable / Stepped)
    save_symbol(cat_tx, "autotransformer", "Autotransformer", f"""
  <line class="ee-stroke" x1="20" y1="16" x2="50" y2="16"/>
  <path class="ee-stroke" d="M 50 16 L 50 24 A 7 7 0 0 1 50 38 A 7 7 0 0 1 50 52 A 7 7 0 0 1 50 66 A 7 7 0 0 1 50 80 L 50 86"/>
  <line class="ee-stroke" x1="20" y1="86" x2="84" y2="86"/>
  <path class="ee-stroke" d="M 84 44 L 62 44" marker-end="url(#arrow)"/>
{node(50, 86)}
{pin(20, 16)}
{pin(20, 86)}
{pin(84, 44)}
{pin(84, 86)}
""", tags=["autotransformer", "variac", "tap changer", "transformer"])

    # 6. Current Transformer (CT)
    save_symbol(cat_tx, "current_transformer_ct", "Current Transformer (CT)", f"""
  <line class="ee-thick" x1="10" y1="50" x2="90" y2="50"/>
  <circle class="ee-stroke" cx="50" cy="50" r="18"/>
  <line class="ee-thin" x1="50" y1="68" x2="50" y2="88"/>
  <line class="ee-thin" x1="58" y1="66" x2="58" y2="88"/>
  <text class="ee-text" x="50" y="20">CT</text>
{pin(10, 50)}
{pin(90, 50)}
{pin(50, 88)}
{pin(58, 88)}
""", tags=["ct", "current transformer", "instrument transformer", "sensor", "protection"])

    # 7. Three-Phase Wye / Star (Y) Winding Connection
    save_symbol(cat_tx, "winding_3ph_wye", "3-Phase Wye / Star (Y) Winding", f"""
  <!-- Neutral center at (50,54) -->
  <!-- Phase A (Up) -->
  <path class="ee-wire-a" d="M 50 54 L 50 44 A 5 4 0 0 1 50 36 A 5 4 0 0 1 50 28 A 5 4 0 0 1 50 20 L 50 12"/>
  <!-- Phase B (Bottom Right, 120 deg) -->
  <path class="ee-wire-b" d="M 50 54 L 58 59 A 5 4 30 0 1 65 63 A 5 4 30 0 1 72 67 A 5 4 30 0 1 79 71 L 86 75"/>
  <!-- Phase C (Bottom Left, 240 deg) -->
  <path class="ee-wire-c" d="M 50 54 L 42 59 A 5 4 -30 0 0 35 63 A 5 4 -30 0 0 28 67 A 5 4 -30 0 0 21 71 L 14 75"/>
  <text class="ee-label" x="62" y="14">A</text>
  <text class="ee-label" x="88" y="64">B</text>
  <text class="ee-label" x="12" y="64">C</text>
{node(50, 54)}
{pin(50, 12)}
{pin(86, 75)}
{pin(14, 75)}
""", tags=["winding", "wye", "star", "Y", "3-phase", "stator"])

    # 8. Three-Phase Grounded Wye (Yn) Winding Connection
    save_symbol(cat_tx, "winding_3ph_wye_grounded", "3-Phase Grounded Wye (Yn) Winding", f"""
  <path class="ee-wire-a" d="M 50 50 L 50 40 A 5 4 0 0 1 50 32 A 5 4 0 0 1 50 24 A 5 4 0 0 1 50 16 L 50 10"/>
  <path class="ee-wire-b" d="M 50 50 L 58 55 A 5 4 30 0 1 65 59 A 5 4 30 0 1 72 63 A 5 4 30 0 1 79 67 L 86 71"/>
  <path class="ee-wire-c" d="M 50 50 L 42 55 A 5 4 -30 0 0 35 59 A 5 4 -30 0 0 28 63 A 5 4 -30 0 0 21 67 L 14 71"/>
  <!-- Neutral Ground -->
  <line class="ee-stroke" x1="50" y1="50" x2="50" y2="78"/>
  <line class="ee-stroke" x1="40" y1="78" x2="60" y2="78"/>
  <line class="ee-stroke" x1="44" y1="83" x2="56" y2="83"/>
  <line class="ee-stroke" x1="47" y1="88" x2="53" y2="88"/>
{node(50, 50)}
{pin(50, 10)}
{pin(86, 71)}
{pin(14, 71)}
""", tags=["winding", "grounded wye", "Yn", "neutral", "star", "3-phase"])

    # 9. Three-Phase Delta (Δ) Winding Connection
    save_symbol(cat_tx, "winding_3ph_delta", "3-Phase Delta (Δ) Winding", f"""
  <!-- Triangle vertices: (50,16), (82,72), (18,72) -->
  <path class="ee-wire-a" d="M 50 16 L 60 34 A 5 4 60 0 1 66 44 A 5 4 60 0 1 72 54 L 82 72"/>
  <path class="ee-wire-b" d="M 82 72 L 64 72 A 5 5 0 0 1 50 72 A 5 5 0 0 1 36 72 L 18 72"/>
  <path class="ee-wire-c" d="M 18 72 L 28 54 A 5 4 -60 0 1 34 44 A 5 4 -60 0 1 40 34 L 50 16"/>
  <line class="ee-stroke" x1="50" y1="16" x2="50" y2="8"/>
  <line class="ee-stroke" x1="82" y1="72" x2="90" y2="78"/>
  <line class="ee-stroke" x1="18" y1="72" x2="10" y2="78"/>
  <text class="ee-label" x="50" y="54">Δ</text>
{node(50, 16)}
{node(82, 72)}
{node(18, 72)}
{pin(50, 8)}
{pin(90, 78)}
{pin(10, 78)}
""", tags=["winding", "delta", "triangle", "3-phase", "stator"])

    # 10. Three-Phase Open-End Winding (OEW - 6 Terminals for Dual-Inverter Drives)
    save_symbol(cat_tx, "winding_3ph_open_end", "3-Phase Open-End Winding (OEW 6-Terminal)", f"""
  <!-- Phase A -->
  <path class="ee-wire-a" d="M 12 25 L 26 25 A 6 7 0 0 1 38 25 A 6 7 0 0 1 50 25 A 6 7 0 0 1 62 25 A 6 7 0 0 1 74 25 L 88 25"/>
  <!-- Phase B -->
  <path class="ee-wire-b" d="M 12 50 L 26 50 A 6 7 0 0 1 38 50 A 6 7 0 0 1 50 50 A 6 7 0 0 1 62 50 A 6 7 0 0 1 74 50 L 88 50"/>
  <!-- Phase C -->
  <path class="ee-wire-c" d="M 12 75 L 26 75 A 6 7 0 0 1 38 75 A 6 7 0 0 1 50 75 A 6 7 0 0 1 62 75 A 6 7 0 0 1 74 75 L 88 75"/>
  <text class="ee-label" x="20" y="15">A1</text>
  <text class="ee-label" x="80" y="15">A2</text>
  <text class="ee-label" x="20" y="40">B1</text>
  <text class="ee-label" x="80" y="40">B2</text>
  <text class="ee-label" x="20" y="65">C1</text>
  <text class="ee-label" x="80" y="65">C2</text>
{pin(12, 25)}
{pin(88, 25)}
{pin(12, 50)}
{pin(88, 50)}
{pin(12, 75)}
{pin(88, 75)}
""", tags=["open end winding", "oew", "dual inverter", "6-terminal", "winding"])

    # 11. Dual Three-Phase / Asymmetric Six-Phase Winding (30° Spatially Shifted Dual-Star)
    save_symbol(cat_tx, "winding_dual_3ph_6ph", "Dual 3-Phase / Asymmetric 6-Phase Winding (30° Shift)", f"""
  <!-- Set 1: ABC (0 deg) -->
  <line class="ee-wire-a" x1="50" y1="50" x2="50" y2="12"/>
  <line class="ee-wire-b" x1="50" y1="50" x2="83" y2="69"/>
  <line class="ee-wire-c" x1="50" y1="50" x2="17" y2="69"/>
  <!-- Set 2: XYZ (30 deg shifted) -->
  <line class="ee-stroke" x1="50" y1="50" x2="69" y2="17"/>
  <line class="ee-stroke" x1="50" y1="50" x2="69" y2="83"/>
  <line class="ee-stroke" x1="50" y1="50" x2="12" y2="50"/>
  <!-- Coil indicators on axes -->
  <circle class="ee-body" cx="50" cy="50" r="10"/>
  <text class="ee-label" x="50" y="50">6φ</text>
  <text class="ee-label" x="42" y="12">A</text>
  <text class="ee-label" x="78" y="17">X</text>
  <text class="ee-label" x="90" y="68">B</text>
  <text class="ee-label" x="78" y="86">Y</text>
  <text class="ee-label" x="12" y="78">C</text>
  <text class="ee-label" x="12" y="40">Z</text>
{pin(50, 12)}
{pin(69, 17)}
{pin(83, 69)}
{pin(69, 83)}
{pin(17, 69)}
{pin(12, 50)}
""", tags=["dual three phase", "six phase", "6-phase", "multiphase", "asymmetric", "winding"])

    # 12. Zig-Zag (Interconnected Star Z) Grounding Transformer Winding
    save_symbol(cat_tx, "winding_zigzag", "Zig-Zag (Interconnected Star) Winding", f"""
  <line class="ee-wire-a" x1="50" y1="50" x2="50" y2="28"/>
  <line class="ee-wire-a" x1="50" y1="28" x2="66" y2="16"/>
  <line class="ee-wire-b" x1="50" y1="50" x2="69" y2="61"/>
  <line class="ee-wire-b" x1="69" y1="61" x2="69" y2="82"/>
  <line class="ee-wire-c" x1="50" y1="50" x2="31" y2="61"/>
  <line class="ee-wire-c" x1="31" y1="61" x2="14" y2="50"/>
{node(50, 50)}
{pin(66, 16)}
{pin(69, 82)}
{pin(14, 50)}
""", tags=["zigzag", "grounding transformer", "phase shifting", "winding"])

    # 13. Concentric vs Hairpin Stator Slot Cross-Section
    save_symbol(cat_tx, "stator_slot_hairpin", "Stator Slot Cross-Section (Flat-Wire Hairpin Winding)", f"""
  <!-- Stator tooth iron -->
  <path class="ee-body" d="M 20 12 L 80 12 L 80 88 L 66 88 L 66 78 L 62 74 L 62 22 L 38 22 L 38 74 L 34 78 L 34 88 L 20 88 Z"/>
  <!-- 4 Rectangular Hairpin Conductors -->
  <rect class="ee-tint-red" x="41" y="25" width="18" height="10" rx="1"/>
  <rect class="ee-tint-red" x="41" y="38" width="18" height="10" rx="1"/>
  <rect class="ee-tint-blue" x="41" y="51" width="18" height="10" rx="1"/>
  <rect class="ee-tint-blue" x="41" y="64" width="18" height="10" rx="1"/>
  <text class="ee-label" x="50" y="94">Airgap</text>
""", tags=["hairpin winding", "stator slot", "flat wire", "ev motor", "cross section"])

    # ==========================================
    # CATEGORY 05: ELECTRICAL MACHINES
    # ==========================================
    cat_m = "05_electrical_machines"

    # 14. DC Brushed Motor / Generator (with Commutator Brushes)
    save_symbol(cat_m, "machine_dc_brushed", "DC Machine (Motor / Generator with Brushes)", f"""
  <line class="ee-stroke" x1="50" y1="6" x2="50" y2="18"/>
  <rect class="ee-fill" x="44" y="18" width="12" height="6"/>
  <circle class="ee-body" cx="50" cy="50" r="26"/>
  <rect class="ee-fill" x="44" y="76" width="12" height="6"/>
  <line class="ee-stroke" x1="50" y1="82" x2="50" y2="94"/>
  <text class="ee-text" x="50" y="45" font-size="16">M</text>
  <line class="ee-stroke" x1="40" y1="58" x2="60" y2="58"/>
  <line class="ee-dashed" x1="40" y1="62" x2="60" y2="62"/>
{pin(50, 6)}
{pin(50, 94)}
""", tags=["dc motor", "dc generator", "brushed", "commutator", "machine"])

    # 15. Separately Excited DC Machine (Armature + Field Coil)
    save_symbol(cat_m, "machine_dc_sep_excited", "Separately Excited DC Machine", f"""
  <line class="ee-stroke" x1="38" y1="8" x2="38" y2="20"/>
  <rect class="ee-fill" x="33" y="20" width="10" height="5"/>
  <circle class="ee-body" cx="38" cy="48" r="23"/>
  <rect class="ee-fill" x="33" y="71" width="10" height="5"/>
  <line class="ee-stroke" x1="38" y1="76" x2="38" y2="90"/>
  <text class="ee-text" x="38" y="46">M</text>
  <!-- Field Winding -->
  <path class="ee-stroke" d="M 90 22 L 76 22 A 6 6 0 0 0 76 34 A 6 6 0 0 0 76 46 A 6 6 0 0 0 76 58 A 6 6 0 0 0 76 70 L 90 70"/>
  <text class="ee-text" x="82" y="12">L<tspan dy="3" font-size="8">f</tspan></text>
{pin(38, 8)}
{pin(38, 90)}
{pin(90, 22)}
{pin(90, 70)}
""", tags=["dc motor", "separately excited", "field winding", "armature"])

    # 16. Three-Phase Squirrel-Cage Induction Motor (SCIM)
    save_symbol(cat_m, "machine_3ph_induction_scim", "3-Phase Squirrel-Cage Induction Motor (IM)", f"""
  <line class="ee-wire-a" x1="8" y1="30" x2="29" y2="30"/>
  <line class="ee-wire-b" x1="8" y1="50" x2="24" y2="50"/>
  <line class="ee-wire-c" x1="8" y1="70" x2="29" y2="70"/>
  <circle class="ee-body" cx="54" cy="50" r="30"/>
  <circle class="ee-thin" cx="54" cy="50" r="22"/>
  <text class="ee-text" x="54" y="42" font-size="15">M</text>
  <text class="ee-label" x="54" y="60">3~</text>
  <!-- Mechanical shaft -->
  <line class="ee-thick" x1="84" y1="50" x2="96" y2="50"/>
{pin(8, 30)}
{pin(8, 50)}
{pin(8, 70)}
""", tags=["induction motor", "scim", "im", "asynchronous", "3-phase", "motor"])

    # 17. Doubly-Fed Induction Generator (DFIG / Wound-Rotor Wind Turbine Generator)
    save_symbol(cat_m, "machine_3ph_dfig", "Doubly-Fed Induction Generator (DFIG / WRIM)", f"""
  <!-- Stator terminals (left) -->
  <line class="ee-wire-a" x1="6" y1="30" x2="25" y2="30"/>
  <line class="ee-wire-b" x1="6" y1="50" x2="22" y2="50"/>
  <line class="ee-wire-c" x1="6" y1="70" x2="25" y2="70"/>
  <!-- Outer stator & inner slip-ring rotor -->
  <circle class="ee-body" cx="50" cy="50" r="28"/>
  <circle class="ee-stroke" cx="50" cy="50" r="18"/>
  <text class="ee-text" x="50" y="44" font-size="13">G</text>
  <text class="ee-label" x="50" y="57">3~</text>
  <!-- Rotor slip-ring terminals (right) -->
  <line class="ee-stroke" x1="66" y1="40" x2="94" y2="32"/>
  <line class="ee-stroke" x1="68" y1="50" x2="94" y2="50"/>
  <line class="ee-stroke" x1="66" y1="60" x2="94" y2="68"/>
{pin(6, 30)}
{pin(6, 50)}
{pin(6, 70)}
{pin(94, 32)}
{pin(94, 50)}
{pin(94, 68)}
""", tags=["dfig", "wound rotor", "wind turbine", "generator", "slip ring", "induction"])

    # 18. Permanent Magnet Synchronous Machine (PMSM / BLDC Standard Symbol)
    save_symbol(cat_m, "machine_3ph_pmsm", "Permanent Magnet Synchronous Machine (PMSM / BLDC)", f"""
  <line class="ee-wire-a" x1="8" y1="30" x2="29" y2="30"/>
  <line class="ee-wire-b" x1="8" y1="50" x2="24" y2="50"/>
  <line class="ee-wire-c" x1="8" y1="70" x2="29" y2="70"/>
  <circle class="ee-body" cx="54" cy="50" r="30"/>
  <text class="ee-text" x="54" y="36" font-size="14">PMSM</text>
  <!-- PM Rotor dipole icon inside -->
  <rect class="ee-tint-red" x="38" y="50" width="16" height="12"/>
  <rect class="ee-tint-blue" x="54" y="50" width="16" height="12"/>
  <text class="ee-label" x="46" y="56">N</text>
  <text class="ee-label" x="62" y="56">S</text>
  <line class="ee-thick" x1="84" y1="50" x2="96" y2="50"/>
{pin(8, 30)}
{pin(8, 50)}
{pin(8, 70)}
""", tags=["pmsm", "bldc", "permanent magnet", "synchronous motor", "ev drive"])

    # 19. Surface-Mounted PM Rotor Cross-Section (SPMSM)
    save_symbol(cat_m, "rotor_cross_section_spmsm", "SPMSM Rotor Cross-Section (Surface-Mounted PM)", f"""
  <!-- Stator bore -->
  <circle class="ee-dashed" cx="50" cy="50" r="42"/>
  <!-- Rotor iron core -->
  <circle class="ee-body" cx="50" cy="50" r="28"/>
  <!-- 4 Surface PM arcs (N, S, N, S) -->
  <path class="ee-tint-red" d="M 32 32 A 26 26 0 0 1 68 32 L 64 36 A 20 20 0 0 0 36 36 Z"/>
  <path class="ee-tint-blue" d="M 68 32 A 26 26 0 0 1 68 68 L 64 64 A 20 20 0 0 0 64 36 Z"/>
  <path class="ee-tint-red" d="M 68 68 A 26 26 0 0 1 32 68 L 36 64 A 20 20 0 0 0 64 64 Z"/>
  <path class="ee-tint-blue" d="M 32 68 A 26 26 0 0 1 32 32 L 36 36 A 20 20 0 0 0 36 64 Z"/>
  <!-- Shaft -->
  <circle class="ee-body" cx="50" cy="50" r="9"/>
  <!-- d-q axes -->
  <line class="ee-thin" x1="50" y1="50" x2="50" y2="6" marker-end="url(#arrow-red)"/>
  <line class="ee-thin" x1="50" y1="50" x2="6" y2="50" marker-end="url(#arrow-blue)"/>
  <text class="ee-text" x="58" y="10">d</text>
  <text class="ee-text" x="12" y="42">q</text>
""", tags=["spmsm", "spm", "surface magnet", "rotor", "dq axis", "pmsm"])

    # 20. Interior PM Rotor Cross-Section (IPMSM V-Shape Magnets)
    save_symbol(cat_m, "rotor_cross_section_ipmsm", "IPMSM Rotor Cross-Section (V-Shape Interior PM)", f"""
  <!-- Stator bore -->
  <circle class="ee-dashed" cx="50" cy="50" r="42"/>
  <!-- Rotor core -->
  <circle class="ee-body" cx="50" cy="50" r="34"/>
  <!-- V-shape buried magnets (Top pole N) -->
  <polygon class="ee-tint-red" points="32,24 37,21 48,36 43,39"/>
  <polygon class="ee-tint-red" points="68,24 63,21 52,36 57,39"/>
  <!-- V-shape buried magnets (Bottom pole N) -->
  <polygon class="ee-tint-red" points="32,76 37,79 48,64 43,61"/>
  <polygon class="ee-tint-red" points="68,76 63,79 52,64 57,61"/>
  <!-- V-shape buried magnets (Left pole S) -->
  <polygon class="ee-tint-blue" points="24,32 21,37 36,48 39,43"/>
  <polygon class="ee-tint-blue" points="24,68 21,63 36,52 39,57"/>
  <!-- V-shape buried magnets (Right pole S) -->
  <polygon class="ee-tint-blue" points="76,32 79,37 64,48 61,43"/>
  <polygon class="ee-tint-blue" points="76,68 79,63 64,52 61,57"/>
  <!-- Shaft -->
  <circle class="ee-body" cx="50" cy="50" r="9"/>
  <!-- d-q axes -->
  <line class="ee-thin" x1="50" y1="50" x2="50" y2="6" marker-end="url(#arrow-red)"/>
  <line class="ee-thin" x1="50" y1="50" x2="18" y2="18" marker-end="url(#arrow-blue)"/>
  <text class="ee-text" x="58" y="10">d</text>
  <text class="ee-text" x="24" y="14">q</text>
""", tags=["ipmsm", "ipm", "interior permanent magnet", "v-shape", "reluctance", "ev motor"])

    # 21. Synchronous Reluctance Machine (SynRM Rotor with Flux Barriers)
    save_symbol(cat_m, "rotor_cross_section_synrm", "SynRM Rotor Cross-Section (Flux Barriers)", f"""
  <circle class="ee-dashed" cx="50" cy="50" r="42"/>
  <circle class="ee-body" cx="50" cy="50" r="34"/>
  <!-- Flux barrier arcs in 4 quadrants -->
  <path class="ee-stroke" d="M 32 19 Q 50 38 68 19"/>
  <path class="ee-stroke" d="M 38 17 Q 50 30 62 17"/>
  <path class="ee-stroke" d="M 32 81 Q 50 62 68 81"/>
  <path class="ee-stroke" d="M 38 83 Q 50 70 62 83"/>
  <path class="ee-stroke" d="M 19 32 Q 38 50 19 68"/>
  <path class="ee-stroke" d="M 81 32 Q 62 50 81 68"/>
  <circle class="ee-body" cx="50" cy="50" r="8"/>
  <text class="ee-label" x="50" y="94">SynRM</text>
""", tags=["synrm", "synchronous reluctance", "flux barrier", "magnet free", "rotor"])

    # 22. Switched Reluctance Machine (SRM Salient Stator & Rotor Poles 6/4)
    save_symbol(cat_m, "machine_srm_salient", "Switched Reluctance Machine (SRM 6/4 Cross-Section)", f"""
  <!-- Outer Stator Ring -->
  <circle class="ee-body" cx="50" cy="50" r="38"/>
  <circle class="ee-body" cx="50" cy="50" r="28"/>
  <!-- 4 Salient Rotor Poles (Cross) -->
  <path class="ee-fill" d="M 45 26 L 55 26 L 55 42 L 74 45 L 74 55 L 55 58 L 55 74 L 45 74 L 45 58 L 26 55 L 26 45 L 45 42 Z"/>
  <circle class="ee-body" cx="50" cy="50" r="6"/>
  <text class="ee-label" x="50" y="95">SRM</text>
""", tags=["srm", "switched reluctance", "salient pole", "doubly salient", "motor"])

    # 23. Wound-Field Synchronous Generator (WFSG / Turbo-Alternator)
    save_symbol(cat_m, "machine_3ph_sync_generator", "3-Phase Synchronous Generator (WFSG / Alternator)", f"""
  <circle class="ee-body" cx="50" cy="50" r="28"/>
  <path class="ee-stroke" d="M 38 56 C 42 44, 46 44, 50 56 C 54 68, 58 68, 62 56"/>
  <text class="ee-text" x="50" y="38" font-size="15">G</text>
  <line class="ee-wire-a" x1="75" y1="36" x2="94" y2="36"/>
  <line class="ee-wire-b" x1="78" y1="50" x2="94" y2="50"/>
  <line class="ee-wire-c" x1="75" y1="64" x2="94" y2="64"/>
  <!-- Exciter field terminals -->
  <line class="ee-stroke" x1="42" y1="23" x2="42" y2="8"/>
  <line class="ee-stroke" x1="58" y1="23" x2="58" y2="8"/>
  <text class="ee-label" x="34" y="12">+f</text>
  <text class="ee-label" x="66" y="12">-f</text>
{pin(94, 36)}
{pin(94, 50)}
{pin(94, 64)}
{pin(42, 8)}
{pin(58, 8)}
""", tags=["synchronous generator", "alternator", "wfsg", "grid", "exciter"])

    # 24. Rotary Encoder / Resolver (Shaft Position Sensor)
    save_symbol(cat_m, "sensor_encoder_resolver", "Rotary Position Encoder / Resolver", f"""
  <!-- Mechanical shaft input (dashed) -->
  <line class="ee-dashed" x1="8" y1="50" x2="28" y2="50"/>
  <circle class="ee-tint-amber" cx="50" cy="50" r="22"/>
  <text class="ee-text" x="50" y="44">θ<tspan dy="3" font-size="9">r</tspan></text>
  <path class="ee-thin" d="M 38 58 L 44 58 L 44 52 L 50 52 L 50 58 L 56 58 L 56 52 L 62 52"/>
  <line class="ee-stroke" x1="72" y1="42" x2="92" y2="42"/>
  <line class="ee-stroke" x1="72" y1="58" x2="92" y2="58"/>
{pin(92, 42)}
{pin(92, 58)}
""", tags=["encoder", "resolver", "position sensor", "shaft", "speed sensor"])
