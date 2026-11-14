# -*- coding: utf-8 -*-
"""
Part 5: Complete Power Electronics Circuit Topologies & Publication Scope/Waveform SVGs
"""
import math

def register_part5(save_symbol, pin, node):
    # ==========================================
    # CATEGORY 08: POWER ELECTRONICS CIRCUIT TOPOLOGIES
    # ==========================================
    cat_pe = "08_power_topologies"

    # Helper to draw a compact vertical MOSFET/IGBT switch box at (cx, cy)
    def sw_cell(cx, cy, label=""):
        lbl = f'  <text class="ee-text" x="{cx-18}" y="{cy}" font-size="11">{label}</text>\n' if label else ""
        return f"""{lbl}  <rect class="ee-tint-blue" x="{cx-10}" y="{cy-14}" width="20" height="28" rx="2"/>
  <line class="ee-thin" x1="{cx-5}" y1="{cy-8}" x2="{cx-5}" y2="{cy+8}"/>
  <path class="ee-thin" d="M {cx-5} {cy-4} L {cx+4} {cy-10} L {cx+4} {cy-14}"/>
  <path class="ee-thin" d="M {cx-5} {cy+4} L {cx+4} {cy+10} L {cx+4} {cy+14}"/>
  <polygon class="ee-fill" points="{cx+5},{cy+3} {cx+9},{cy+3} {cx+7},{cy-3}"/>"""

    # 1. Synchronous Buck Converter (Step-Down DC-DC)
    save_symbol(cat_pe, "topology_sync_buck", "Synchronous Buck Converter (Step-Down DC-DC)", f"""
  <!-- Input DC source -->
  <line class="ee-stroke" x1="35" y1="30" x2="35" y2="150"/>
  <circle class="ee-body" cx="35" cy="90" r="18"/>
  <text class="ee-label" x="35" y="82">+</text>
  <text class="ee-label" x="35" y="98">−</text>
  <text class="ee-text" x="14" y="90">V<tspan dy="3" font-size="9">in</tspan></text>
  <!-- Top rail to High-Side Switch Q1 -->
  <line class="ee-stroke" x1="35" y1="30" x2="110" y2="30"/>
  <line class="ee-stroke" x1="110" y1="30" x2="110" y2="46"/>
{sw_cell(110, 60, "Q1")}
  <line class="ee-stroke" x1="110" y1="74" x2="110" y2="106"/>
{sw_cell(110, 120, "Q2")}
  <line class="ee-stroke" x1="110" y1="134" x2="110" y2="150"/>
  <!-- Switch node & Inductor L -->
  <path class="ee-stroke" d="M 110 90 L 145 90 A 8 9 0 0 1 161 90 A 8 9 0 0 1 177 90 A 8 9 0 0 1 193 90 A 8 9 0 0 1 209 90 L 295 90"/>
  <text class="ee-text" x="177" y="70">L</text>
  <!-- Output Capacitor C -->
  <line class="ee-stroke" x1="240" y1="90" x2="240" y2="114"/>
  <line class="ee-stroke" x1="228" y1="114" x2="252" y2="114"/>
  <line class="ee-stroke" x1="228" y1="122" x2="252" y2="122"/>
  <line class="ee-stroke" x1="240" y1="122" x2="240" y2="150"/>
  <text class="ee-text" x="216" y="120">C<tspan dy="3" font-size="8">o</tspan></text>
  <!-- Load Resistor R -->
  <line class="ee-stroke" x1="295" y1="90" x2="295" y2="104"/>
  <rect class="ee-body" x="287" y="104" width="16" height="32"/>
  <line class="ee-stroke" x1="295" y1="136" x2="295" y2="150"/>
  <text class="ee-text" x="320" y="120">R<tspan dy="3" font-size="8">L</tspan></text>
  <!-- Bottom ground rail -->
  <line class="ee-stroke" x1="35" y1="150" x2="295" y2="150"/>
{node(110, 90)}
{node(240, 90)}
{node(240, 150)}
{node(110, 150)}
""", width=340, height=180, tags=["buck converter", "synchronous buck", "dc-dc", "step down", "topology"])

    # 2. Boost Converter (Step-Up DC-DC)
    save_symbol(cat_pe, "topology_boost", "Boost Converter (Step-Up DC-DC)", f"""
  <!-- Input DC source -->
  <line class="ee-stroke" x1="35" y1="40" x2="35" y2="150"/>
  <circle class="ee-body" cx="35" cy="95" r="18"/>
  <text class="ee-label" x="35" y="87">+</text>
  <text class="ee-label" x="35" y="103">−</text>
  <text class="ee-text" x="14" y="95">V<tspan dy="3" font-size="9">in</tspan></text>
  <!-- Input Inductor L -->
  <path class="ee-stroke" d="M 35 40 L 65 40 A 8 9 0 0 1 81 40 A 8 9 0 0 1 97 40 A 8 9 0 0 1 113 40 A 8 9 0 0 1 129 40 L 175 40"/>
  <text class="ee-text" x="97" y="20">L</text>
  <!-- Shunt Switch S -->
  <line class="ee-stroke" x1="155" y1="40" x2="155" y2="81"/>
{sw_cell(155, 95, "S")}
  <line class="ee-stroke" x1="155" y1="109" x2="155" y2="150"/>
  <!-- Boost Diode D -->
  <polygon class="ee-body" points="175,30 175,50 197,40"/>
  <line class="ee-stroke" x1="197" y1="30" x2="197" y2="50"/>
  <line class="ee-stroke" x1="197" y1="40" x2="295" y2="40"/>
  <text class="ee-text" x="186" y="20">D</text>
  <!-- Output Capacitor C -->
  <line class="ee-stroke" x1="240" y1="40" x2="240" y2="90"/>
  <line class="ee-stroke" x1="228" y1="90" x2="252" y2="90"/>
  <line class="ee-stroke" x1="228" y1="98" x2="252" y2="98"/>
  <line class="ee-stroke" x1="240" y1="98" x2="240" y2="150"/>
  <text class="ee-text" x="216" y="95">C<tspan dy="3" font-size="8">o</tspan></text>
  <!-- Load R -->
  <line class="ee-stroke" x1="295" y1="40" x2="295" y2="75"/>
  <rect class="ee-body" x="287" y="75" width="16" height="40"/>
  <line class="ee-stroke" x1="295" y1="115" x2="295" y2="150"/>
  <text class="ee-text" x="320" y="95">R<tspan dy="3" font-size="8">L</tspan></text>
  <line class="ee-stroke" x1="35" y1="150" x2="295" y2="150"/>
{node(155, 40)}
{node(155, 150)}
{node(240, 40)}
{node(240, 150)}
""", width=340, height=180, tags=["boost converter", "step up", "dc-dc", "pfc", "topology"])

    # 3. Single-Phase Full-Bridge (H-Bridge) Inverter / Converter
    save_symbol(cat_pe, "topology_h_bridge_1ph", "Single-Phase Full-Bridge (H-Bridge) Converter", f"""
  <!-- DC bus rails -->
  <line class="ee-stroke" x1="25" y1="25" x2="250" y2="25"/>
  <line class="ee-stroke" x1="25" y1="165" x2="250" y2="165"/>
  <!-- DC Link Capacitor -->
  <line class="ee-stroke" x1="55" y1="25" x2="55" y2="88"/>
  <line class="ee-stroke" x1="42" y1="88" x2="68" y2="88"/>
  <line class="ee-stroke" x1="42" y1="98" x2="68" y2="98"/>
  <line class="ee-stroke" x1="55" y1="98" x2="55" y2="165"/>
  <text class="ee-text" x="28" y="95">V<tspan dy="3" font-size="9">dc</tspan></text>
  <!-- Leg A (x=125) -->
  <line class="ee-stroke" x1="125" y1="25" x2="125" y2="44"/>
{sw_cell(125, 58, "S1")}
  <line class="ee-stroke" x1="125" y1="72" x2="125" y2="118"/>
{sw_cell(125, 132, "S2")}
  <line class="ee-stroke" x1="125" y1="146" x2="125" y2="165"/>
  <!-- Leg B (x=235) -->
  <line class="ee-stroke" x1="235" y1="25" x2="235" y2="44"/>
{sw_cell(235, 58, "S3")}
  <line class="ee-stroke" x1="235" y1="72" x2="235" y2="118"/>
{sw_cell(235, 132, "S4")}
  <line class="ee-stroke" x1="235" y1="146" x2="235" y2="165"/>
  <!-- AC Output Load between midpoints -->
  <path class="ee-wire-a" d="M 125 95 L 154 95 A 6 7 0 0 1 166 95 A 6 7 0 0 1 178 95 A 6 7 0 0 1 190 95 L 235 95"/>
  <text class="ee-text" x="180" y="78">L<tspan dy="3" font-size="8">f</tspan></text>
{node(55, 25)}
{node(55, 165)}
{node(125, 25)}
{node(125, 165)}
{node(125, 95)}
{node(235, 95)}
""", width=280, height=190, tags=["h-bridge", "full bridge", "inverter", "1-phase", "topology"])

    # 4. Three-Phase Two-Level Voltage Source Inverter (3-Phase 2L-VSI + PMSM Drive)
    save_symbol(cat_pe, "topology_3ph_2level_vsi", "3-Phase 2-Level VSI Motor Drive Topology", f"""
  <!-- DC Link Rails -->
  <line class="ee-stroke" x1="20" y1="25" x2="255" y2="25"/>
  <line class="ee-stroke" x1="20" y1="185" x2="255" y2="185"/>
  <!-- DC Link Capacitor -->
  <line class="ee-stroke" x1="45" y1="25" x2="45" y2="98"/>
  <line class="ee-stroke" x1="33" y1="98" x2="57" y2="98"/>
  <line class="ee-stroke" x1="33" y1="108" x2="57" y2="108"/>
  <line class="ee-stroke" x1="45" y1="108" x2="45" y2="185"/>
  <text class="ee-text" x="22" y="105">C<tspan dy="3" font-size="8">dc</tspan></text>
  <!-- Phase Leg A (x=105) -->
  <line class="ee-stroke" x1="105" y1="25" x2="105" y2="44"/>
{sw_cell(105, 58, "Sa+")}
  <line class="ee-stroke" x1="105" y1="72" x2="105" y2="138"/>
{sw_cell(105, 152, "Sa-")}
  <line class="ee-stroke" x1="105" y1="166" x2="105" y2="185"/>
  <!-- Phase Leg B (x=175) -->
  <line class="ee-stroke" x1="175" y1="25" x2="175" y2="44"/>
{sw_cell(175, 58, "Sb+")}
  <line class="ee-stroke" x1="175" y1="72" x2="175" y2="138"/>
{sw_cell(175, 152, "Sb-")}
  <line class="ee-stroke" x1="175" y1="166" x2="175" y2="185"/>
  <!-- Phase Leg C (x=245) -->
  <line class="ee-stroke" x1="245" y1="25" x2="245" y2="44"/>
{sw_cell(245, 58, "Sc+")}
  <line class="ee-stroke" x1="245" y1="72" x2="245" y2="138"/>
{sw_cell(245, 152, "Sc-")}
  <line class="ee-stroke" x1="245" y1="166" x2="245" y2="185"/>
  <!-- 3-Phase AC Outputs to PMSM -->
  <line class="ee-wire-a" x1="105" y1="90" x2="320" y2="90"/>
  <line class="ee-wire-b" x1="175" y1="105" x2="316" y2="105"/>
  <line class="ee-wire-c" x1="245" y1="120" x2="320" y2="120"/>
  <!-- PMSM Load -->
  <circle class="ee-body" cx="345" cy="105" r="28"/>
  <text class="ee-text" x="345" y="98" font-size="13">PMSM</text>
  <text class="ee-label" x="345" y="114">3~</text>
{node(45, 25)}
{node(45, 185)}
{node(105, 25)}
{node(175, 25)}
{node(105, 185)}
{node(175, 185)}
{node(105, 90)}
{node(175, 105)}
{node(245, 120)}
""", width=390, height=210, tags=["3-phase inverter", "2-level vsi", "vsi", "motor drive", "pmsm drive", "topology"])

    # 5. Three-Level Neutral-Point-Clamped (3L-NPC) Phase Leg
    save_symbol(cat_pe, "topology_3level_npc_leg", "3-Level Neutral-Point-Clamped (3L-NPC) Phase Leg", f"""
  <!-- Split DC Link Capacitors -->
  <line class="ee-stroke" x1="35" y1="18" x2="155" y2="18"/>
  <line class="ee-stroke" x1="35" y1="222" x2="155" y2="222"/>
  <line class="ee-stroke" x1="35" y1="18" x2="35" y2="62"/>
  <line class="ee-stroke" x1="23" y1="62" x2="47" y2="62"/>
  <line class="ee-stroke" x1="23" y1="70" x2="47" y2="70"/>
  <line class="ee-stroke" x1="35" y1="70" x2="35" y2="170"/>
  <line class="ee-stroke" x1="23" y1="170" x2="47" y2="170"/>
  <line class="ee-stroke" x1="23" y1="178" x2="47" y2="178"/>
  <line class="ee-stroke" x1="35" y1="178" x2="35" y2="222"/>
  <!-- Neutral Point O -->
  <line class="ee-stroke" x1="35" y1="120" x2="100" y2="120"/>
  <text class="ee-label" x="18" y="120">O</text>
  <!-- Clamping Diodes D1, D2 -->
  <line class="ee-stroke" x1="100" y1="70" x2="100" y2="170"/>
  <polygon class="ee-body" points="92,98 108,98 100,82"/>
  <line class="ee-stroke" x1="92" y1="82" x2="108" y2="82"/>
  <polygon class="ee-body" points="92,142 108,142 100,158"/>
  <line class="ee-stroke" x1="92" y1="158" x2="108" y2="158"/>
  <line class="ee-stroke" x1="100" y1="70" x2="155" y2="70"/>
  <line class="ee-stroke" x1="100" y1="170" x2="155" y2="170"/>
  <!-- 4 Series Switches S1..S4 at x=155 -->
  <line class="ee-stroke" x1="155" y1="18" x2="155" y2="30"/>
{sw_cell(155, 44, "S1")}
  <line class="ee-stroke" x1="155" y1="58" x2="155" y2="80"/>
{sw_cell(155, 94, "S2")}
  <line class="ee-stroke" x1="155" y1="108" x2="155" y2="132"/>
{sw_cell(155, 146, "S3")}
  <line class="ee-stroke" x1="155" y1="160" x2="155" y2="182"/>
{sw_cell(155, 196, "S4")}
  <line class="ee-stroke" x1="155" y1="210" x2="155" y2="222"/>
  <!-- AC Output -->
  <line class="ee-wire-a" x1="155" y1="120" x2="215" y2="120"/>
  <text class="ee-text" x="200" y="106">v<tspan dy="3" font-size="8">an</tspan></text>
{node(35, 120)}
{node(100, 120)}
{node(155, 70)}
{node(155, 120)}
{node(155, 170)}
{pin(215, 120)}
""", width=240, height=240, tags=["npc", "3-level", "multilevel inverter", "neutral point clamped", "topology"])

    # 6. Three-Level T-Type Inverter Phase Leg (3L-T-Type)
    save_symbol(cat_pe, "topology_3level_ttype_leg", "3-Level T-Type Inverter Phase Leg", f"""
  <!-- Split DC Link -->
  <line class="ee-stroke" x1="30" y1="20" x2="170" y2="20"/>
  <line class="ee-stroke" x1="30" y1="180" x2="170" y2="180"/>
  <line class="ee-stroke" x1="30" y1="20" x2="30" y2="55"/>
  <line class="ee-stroke" x1="18" y1="55" x2="42" y2="55"/>
  <line class="ee-stroke" x1="18" y1="63" x2="42" y2="63"/>
  <line class="ee-stroke" x1="30" y1="63" x2="30" y2="137"/>
  <line class="ee-stroke" x1="18" y1="137" x2="42" y2="137"/>
  <line class="ee-stroke" x1="18" y1="145" x2="42" y2="145"/>
  <line class="ee-stroke" x1="30" y1="145" x2="30" y2="180"/>
  <!-- Half bridge main switches S1, S4 at x=170 -->
  <line class="ee-stroke" x1="170" y1="20" x2="170" y2="42"/>
{sw_cell(170, 56, "S1")}
  <line class="ee-stroke" x1="170" y1="70" x2="170" y2="130"/>
{sw_cell(170, 144, "S4")}
  <line class="ee-stroke" x1="170" y1="158" x2="170" y2="180"/>
  <!-- Bidirectional Neutral Clamp Switch (S2/S3) between (30,100) and (170,100) -->
  <line class="ee-stroke" x1="30" y1="100" x2="76" y2="100"/>
  <rect class="ee-tint-amber" x="76" y="86" width="48" height="28" rx="3"/>
  <text class="ee-label" x="100" y="100">S2 / S3</text>
  <line class="ee-stroke" x1="124" y1="100" x2="220" y2="100"/>
  <text class="ee-text" x="208" y="86">AC</text>
{node(30, 100)}
{node(170, 100)}
{pin(220, 100)}
""", width=240, height=200, tags=["t-type", "3-level", "multilevel", "inverter leg", "topology"])

    # 7. Dual Active Bridge (DAB) Isolated Bidirectional DC-DC Converter
    save_symbol(cat_pe, "topology_dab_converter", "Dual Active Bridge (DAB) Isolated DC-DC Converter", f"""
  <!-- Primary H-Bridge (Left) -->
  <line class="ee-stroke" x1="20" y1="25" x2="135" y2="25"/>
  <line class="ee-stroke" x1="20" y1="165" x2="135" y2="165"/>
  <line class="ee-stroke" x1="70" y1="25" x2="70" y2="42"/>
{sw_cell(70, 56, "S1")}
  <line class="ee-stroke" x1="70" y1="70" x2="70" y2="120"/>
{sw_cell(70, 134, "S2")}
  <line class="ee-stroke" x1="70" y1="148" x2="70" y2="165"/>
  <line class="ee-stroke" x1="135" y1="25" x2="135" y2="42"/>
{sw_cell(135, 56, "S3")}
  <line class="ee-stroke" x1="135" y1="70" x2="135" y2="120"/>
{sw_cell(135, 134, "S4")}
  <line class="ee-stroke" x1="135" y1="148" x2="135" y2="165"/>
  <!-- Leakage Inductor Lk + HF Transformer -->
  <path class="ee-stroke" d="M 70 82 L 155 82 A 5 6 0 0 1 165 82 A 5 6 0 0 1 175 82 A 5 6 0 0 1 185 82 L 205 82"/>
  <text class="ee-text" x="170" y="66">L<tspan dy="3" font-size="8">k</tspan></text>
  <path class="ee-stroke" d="M 205 82 A 6 5.5 0 0 1 205 93 A 6 5.5 0 0 1 205 104 A 6 5.5 0 0 1 205 115 L 135 115"/>
  <line class="ee-dashed" x1="216" y1="76" x2="216" y2="120"/>
  <line class="ee-dashed" x1="221" y1="76" x2="221" y2="120"/>
  <path class="ee-stroke" d="M 295 82 L 232 82 A 6 5.5 0 0 0 232 93 A 6 5.5 0 0 0 232 104 A 6 5.5 0 0 0 232 115 L 360 115"/>
  <!-- Secondary H-Bridge (Right) -->
  <line class="ee-stroke" x1="295" y1="25" x2="410" y2="25"/>
  <line class="ee-stroke" x1="295" y1="165" x2="410" y2="165"/>
  <line class="ee-stroke" x1="295" y1="25" x2="295" y2="42"/>
{sw_cell(295, 56, "Q1")}
  <line class="ee-stroke" x1="295" y1="70" x2="295" y2="120"/>
{sw_cell(295, 134, "Q2")}
  <line class="ee-stroke" x1="295" y1="148" x2="295" y2="165"/>
  <line class="ee-stroke" x1="360" y1="25" x2="360" y2="42"/>
{sw_cell(360, 56, "Q3")}
  <line class="ee-stroke" x1="360" y1="70" x2="360" y2="120"/>
{sw_cell(360, 134, "Q4")}
  <line class="ee-stroke" x1="360" y1="148" x2="360" y2="165"/>
  <text class="ee-text" x="30" y="95">V<tspan dy="3" font-size="8">1</tspan></text>
  <text class="ee-text" x="400" y="95">V<tspan dy="3" font-size="8">2</tspan></text>
{node(70, 82)}
{node(135, 115)}
{node(295, 82)}
{node(360, 115)}
""", width=430, height=190, tags=["dab", "dual active bridge", "isolated dc-dc", "bidirectional", "solid state transformer", "topology"])

    # 8. LLC Resonant Tank (Lr, Cr, Lm + HF Transformer)
    save_symbol(cat_pe, "topology_llc_resonant_tank", "LLC Resonant Tank Stage (Cr, Lr, Lm)", f"""
  <line class="ee-stroke" x1="15" y1="45" x2="42" y2="45"/>
  <!-- Resonant Capacitor Cr -->
  <line class="ee-stroke" x1="42" y1="30" x2="42" y2="60"/>
  <line class="ee-stroke" x1="50" y1="30" x2="50" y2="60"/>
  <text class="ee-text" x="46" y="18">C<tspan dy="3" font-size="8">r</tspan></text>
  <!-- Resonant Inductor Lr -->
  <path class="ee-stroke" d="M 50 45 L 72 45 A 7 8 0 0 1 86 45 A 7 8 0 0 1 100 45 A 7 8 0 0 1 114 45 L 185 45"/>
  <text class="ee-text" x="93" y="22">L<tspan dy="3" font-size="8">r</tspan></text>
  <!-- Magnetizing Inductance Lm -->
  <path class="ee-stroke" d="M 145 45 L 145 62 A 6 6 0 0 1 145 74 A 6 6 0 0 1 145 86 A 6 6 0 0 1 145 98 L 145 115"/>
  <text class="ee-text" x="125" y="80">L<tspan dy="3" font-size="8">m</tspan></text>
  <!-- Transformer Primary & Secondary -->
  <path class="ee-stroke" d="M 185 45 L 185 58 A 6 6 0 0 1 185 70 A 6 6 0 0 1 185 82 A 6 6 0 0 1 185 94 L 185 115"/>
  <line class="ee-dashed" x1="198" y1="42" x2="198" y2="118"/>
  <line class="ee-dashed" x1="204" y1="42" x2="204" y2="118"/>
  <path class="ee-stroke" d="M 245 45 L 216 45 A 6 6 0 0 0 216 62 A 6 6 0 0 0 216 80 A 6 6 0 0 0 216 98 A 6 6 0 0 0 216 115 L 245 115"/>
  <line class="ee-stroke" x1="15" y1="115" x2="185" y2="115"/>
{node(145, 45)}
{node(145, 115)}
{pin(15, 45)}
{pin(15, 115)}
{pin(245, 45)}
{pin(245, 115)}
""", width=260, height=140, tags=["llc", "resonant converter", "resonant tank", "soft switching", "zvs", "topology"])

    # 9. Modular Multilevel Converter (MMC) Submodule (Half-Bridge SM)
    save_symbol(cat_pe, "topology_mmc_submodule", "MMC Half-Bridge Submodule (HB-SM)", f"""
  <rect class="ee-body" x="28" y="15" width="124" height="130" rx="6"/>
  <!-- Upper IGBT T1 -->
  <line class="ee-stroke" x1="70" y1="25" x2="70" y2="38"/>
{sw_cell(70, 52, "T1")}
  <line class="ee-stroke" x1="70" y1="66" x2="70" y2="94"/>
{sw_cell(70, 108, "T2")}
  <line class="ee-stroke" x1="70" y1="122" x2="70" y2="135"/>
  <!-- Submodule Capacitor Csm -->
  <line class="ee-stroke" x1="70" y1="25" x2="122" y2="25"/>
  <line class="ee-stroke" x1="122" y1="25" x2="122" y2="74"/>
  <line class="ee-stroke" x1="110" y1="74" x2="134" y2="74"/>
  <line class="ee-stroke" x1="110" y1="84" x2="134" y2="84"/>
  <line class="ee-stroke" x1="122" y1="84" x2="122" y2="135"/>
  <line class="ee-stroke" x1="70" y1="135" x2="122" y2="135"/>
  <text class="ee-text" x="138" y="55" font-size="11">C<tspan dy="2" font-size="8">sm</tspan></text>
  <!-- External SM Terminals -->
  <line class="ee-stroke" x1="8" y1="80" x2="70" y2="80"/>
  <line class="ee-stroke" x1="8" y1="135" x2="70" y2="135"/>
  <text class="ee-text" x="18" y="68" font-size="11">+v<tspan dy="2" font-size="8">sm</tspan></text>
{node(70, 80)}
{node(70, 135)}
{pin(8, 80)}
{pin(8, 135)}
""", width=170, height=160, tags=["mmc", "modular multilevel converter", "submodule", "hb-sm", "hvdc", "topology"])

    # 10. LCL Grid-Tie Filter Stage (Inverter-side L1, Capacitor Cf + Rd, Grid-side L2)
    save_symbol(cat_pe, "topology_lcl_filter", "LCL Grid-Tie Filter with Damping Resistor", f"""
  <!-- Inverter side L1 -->
  <path class="ee-stroke" d="M 12 40 L 32 40 A 7 8 0 0 1 46 40 A 7 8 0 0 1 60 40 A 7 8 0 0 1 74 40 L 110 40"/>
  <text class="ee-text" x="53" y="20">L<tspan dy="3" font-size="8">1</tspan></text>
  <!-- Grid side L2 -->
  <path class="ee-stroke" d="M 110 40 L 146 40 A 7 8 0 0 1 160 40 A 7 8 0 0 1 174 40 A 7 8 0 0 1 188 40 L 208 40"/>
  <text class="ee-text" x="167" y="20">L<tspan dy="3" font-size="8">2</tspan></text>
  <!-- Shunt branch: Cf + Rd -->
  <line class="ee-stroke" x1="110" y1="40" x2="110" y2="66"/>
  <line class="ee-stroke" x1="98" y1="66" x2="122" y2="66"/>
  <line class="ee-stroke" x1="98" y1="74" x2="122" y2="74"/>
  <line class="ee-stroke" x1="110" y1="74" x2="110" y2="90"/>
  <rect class="ee-body" x="103" y="90" width="14" height="24"/>
  <line class="ee-stroke" x1="110" y1="114" x2="110" y2="128"/>
  <line class="ee-stroke" x1="12" y1="128" x2="208" y2="128"/>
  <text class="ee-text" x="84" y="70">C<tspan dy="3" font-size="8">f</tspan></text>
  <text class="ee-text" x="84" y="102">R<tspan dy="3" font-size="8">d</tspan></text>
{node(110, 40)}
{node(110, 128)}
{pin(12, 40)}
{pin(12, 128)}
{pin(208, 40)}
{pin(208, 128)}
""", width=220, height=145, tags=["lcl filter", "grid tie", "harmonic filter", "damping", "inverter", "topology"])

    # 11. Three-Phase 6-Pulse Diode Bridge Rectifier
    save_symbol(cat_pe, "topology_3ph_diode_rectifier", "3-Phase 6-Pulse Diode Bridge Rectifier", f"""
  <line class="ee-stroke" x1="60" y1="20" x2="220" y2="20"/>
  <line class="ee-stroke" x1="60" y1="150" x2="220" y2="150"/>
  <!-- 3 Diode Legs at x=75, 130, 185 -->
  <!-- Leg 1 -->
  <line class="ee-stroke" x1="75" y1="20" x2="75" y2="150"/>
  <polygon class="ee-body" points="67,60 83,60 75,44"/><line class="ee-stroke" x1="67" y1="44" x2="83" y2="44"/>
  <polygon class="ee-body" points="67,126 83,126 75,110"/><line class="ee-stroke" x1="67" y1="110" x2="83" y2="110"/>
  <!-- Leg 2 -->
  <line class="ee-stroke" x1="130" y1="20" x2="130" y2="150"/>
  <polygon class="ee-body" points="122,60 138,60 130,44"/><line class="ee-stroke" x1="122" y1="44" x2="138" y2="44"/>
  <polygon class="ee-body" points="122,126 138,126 130,110"/><line class="ee-stroke" x1="122" y1="110" x2="138" y2="110"/>
  <!-- Leg 3 -->
  <line class="ee-stroke" x1="185" y1="20" x2="185" y2="150"/>
  <polygon class="ee-body" points="177,60 193,60 185,44"/><line class="ee-stroke" x1="177" y1="44" x2="193" y2="44"/>
  <polygon class="ee-body" points="177,126 193,126 185,110"/><line class="ee-stroke" x1="177" y1="110" x2="193" y2="110"/>
  <!-- 3-Phase AC Inputs -->
  <line class="ee-wire-a" x1="15" y1="74" x2="75" y2="74"/>
  <line class="ee-wire-b" x1="15" y1="85" x2="130" y2="85"/>
  <line class="ee-wire-c" x1="15" y1="96" x2="185" y2="96"/>
{node(75, 74)}
{node(130, 85)}
{node(185, 96)}
{node(75, 20)}
{node(130, 20)}
{node(75, 150)}
{node(130, 150)}
{pin(15, 74)}
{pin(15, 85)}
{pin(15, 96)}
{pin(220, 20)}
{pin(220, 150)}
""", width=240, height=170, tags=["rectifier", "6-pulse", "diode bridge", "3-phase", "ac-dc", "topology"])

    # 12. Vienna Rectifier Phase Leg (3-Phase 3-Level PFC)
    save_symbol(cat_pe, "topology_vienna_rectifier_leg", "Vienna Rectifier Phase Leg (3-Level Unidirectional PFC)", f"""
  <!-- Input Boost Inductor -->
  <path class="ee-wire-a" d="M 15 90 L 35 90 A 6 7 0 0 1 47 90 A 6 7 0 0 1 59 90 A 6 7 0 0 1 71 90 L 115 90"/>
  <text class="ee-text" x="53" y="72">L<tspan dy="3" font-size="8">a</tspan></text>
  <!-- Main Diode Leg -->
  <line class="ee-stroke" x1="115" y1="20" x2="185" y2="20"/>
  <line class="ee-stroke" x1="115" y1="160" x2="185" y2="160"/>
  <line class="ee-stroke" x1="115" y1="20" x2="115" y2="160"/>
  <polygon class="ee-body" points="107,62 123,62 115,44"/><line class="ee-stroke" x1="107" y1="44" x2="123" y2="44"/>
  <polygon class="ee-body" points="107,136 123,136 115,118"/><line class="ee-stroke" x1="107" y1="118" x2="123" y2="118"/>
  <!-- Bidirectional Switch to Neutral O -->
  <rect class="ee-tint-blue" x="135" y="76" width="36" height="28" rx="3"/>
  <text class="ee-label" x="153" y="90">S<tspan dy="2" font-size="7">a</tspan></text>
  <line class="ee-stroke" x1="115" y1="90" x2="135" y2="90"/>
  <line class="ee-stroke" x1="171" y1="90" x2="215" y2="90"/>
  <text class="ee-label" x="205" y="78">O</text>
{node(115, 90)}
{pin(15, 90)}
{pin(185, 20)}
{pin(215, 90)}
{pin(185, 160)}
""", width=230, height=180, tags=["vienna rectifier", "pfc", "3-level", "ev charger", "rectifier", "topology"])

    # ==========================================
    # CATEGORY 09: SCOPE & WAVEFORM SVGs (PUBLICATION FIGURES)
    # ==========================================
    cat_sc = "09_scope_waveforms"

    # 1. 4-Channel Power Electronics Digital Oscilloscope Screen (Publication Vector Figure)
    # Channels: CH1: v_gs (Gate), CH2: v_ds (Drain-Source), CH3: i_L (Inductor Current), CH4: i_a (Sinusoidal AC Phase Current)
    sine_pts = " ".join([f"{45 + x:.1f},{215 - 18*math.sin(2*math.pi*x/140):.1f}" for x in range(0, 295, 4)])
    save_symbol(cat_sc, "scope_4ch_power_electronics", "4-Channel Digital Oscilloscope Plot (v_gs, v_ds, i_L, i_a)", f"""
  <!-- Outer frame -->
  <rect class="ee-body" x="10" y="10" width="360" height="240" rx="4"/>
  <!-- Plot area -->
  <rect x="45" y="25" width="295" height="205" fill="#ffffff" stroke="#111827" stroke-width="1.5"/>
  <!-- Graticule grid -->
  <line class="ee-grid" x1="104" y1="25" x2="104" y2="230"/>
  <line class="ee-grid" x1="163" y1="25" x2="163" y2="230"/>
  <line class="ee-grid" x1="222" y1="25" x2="222" y2="230"/>
  <line class="ee-grid" x1="281" y1="25" x2="281" y2="230"/>
  <line class="ee-grid" x1="45" y1="75" x2="340" y2="75"/>
  <line class="ee-grid" x1="45" y1="125" x2="340" y2="125"/>
  <line class="ee-grid" x1="45" y1="175" x2="340" y2="175"/>
  <!-- CH1: Gate Pulse v_gs (Blue) -->
  <path d="M 45 66 L 75 66 L 75 38 L 130 38 L 130 66 L 165 66 L 165 38 L 220 38 L 220 66 L 255 66 L 255 38 L 310 38 L 310 66 L 340 66" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <text class="ee-text" x="26" y="52" font-size="11">v<tspan dy="2" font-size="8">gs</tspan></text>
  <!-- CH2: Drain-Source Voltage v_ds with switching ringing (Red) -->
  <path d="M 45 86 L 75 86 L 75 116 L 77 110 L 79 118 L 81 115 L 130 115 L 130 82 L 132 90 L 134 85 L 136 86 L 165 86 L 165 116 L 167 110 L 169 115 L 220 115 L 220 82 L 222 89 L 224 86 L 255 86 L 255 115 L 310 115 L 310 86 L 340 86" fill="none" stroke="#dc2626" stroke-width="1.8"/>
  <text class="ee-text" x="26" y="102" font-size="11">v<tspan dy="2" font-size="8">ds</tspan></text>
  <!-- CH3: Triangular Inductor Current Ripple i_L (Green) -->
  <path d="M 45 162 L 75 168 L 130 140 L 165 168 L 220 140 L 255 168 L 310 140 L 340 158" fill="none" stroke="#16a34a" stroke-width="1.8"/>
  <text class="ee-text" x="26" y="155" font-size="11">i<tspan dy="2" font-size="8">L</tspan></text>
  <!-- CH4: Sinusoidal Phase Current i_a (Amber/Dark) -->
  <polyline points="{sine_pts}" fill="none" stroke="#d97706" stroke-width="2"/>
  <text class="ee-text" x="26" y="210" font-size="11">i<tspan dy="2" font-size="8">a</tspan></text>
  <!-- Scale bar annotation -->
  <text class="ee-label" x="192" y="242">Time (10 μs/div)</text>
""", width=380, height=260, tags=["oscilloscope", "scope", "waveform", "4-channel", "switching waveform", "figure"])

    # 2. SPWM / Carrier-Based PWM Modulation Waveform (Triangle Carrier + Sine Reference -> Gate Pulses)
    sine_ref = " ".join([f"{40 + x:.1f},{65 - 26*math.sin(2*math.pi*x/260):.1f}" for x in range(0, 264, 4)])
    save_symbol(cat_sc, "waveform_spwm_carrier", "Carrier-Based SPWM Modulation & Gate Pulse Diagram", f"""
  <rect class="ee-body" x="10" y="10" width="320" height="190" rx="4"/>
  <!-- Upper subplot: Carrier vs Reference -->
  <line class="ee-thin" x1="40" y1="22" x2="40" y2="110"/>
  <line class="ee-grid" x1="40" y1="65" x2="305" y2="65"/>
  <!-- High-frequency Triangle Carrier -->
  <path class="ee-thin" d="M 40 95 L 62 35 L 84 95 L 106 35 L 128 95 L 150 35 L 172 95 L 194 35 L 216 95 L 238 35 L 260 95 L 282 35 L 304 95" stroke="#6b7280"/>
  <!-- Sinusoidal Modulation Reference v_ref -->
  <polyline points="{sine_ref}" fill="none" stroke="#dc2626" stroke-width="2.2"/>
  <!-- Lower subplot: PWM Gate Output -->
  <line class="ee-thin" x1="40" y1="125" x2="40" y2="180"/>
  <line class="ee-thin" x1="40" y1="175" x2="305" y2="175"/>
  <path d="M 40 175 L 48 175 L 48 135 L 78 135 L 78 175 L 88 175 L 88 135 L 124 135 L 124 175 L 136 175 L 136 135 L 164 135 L 164 175 L 184 175 L 184 135 L 204 135 L 204 175 L 232 175 L 232 135 L 244 135 L 244 175 L 276 175 L 276 135 L 288 135 L 288 175 L 304 175" fill="none" stroke="#2563eb" stroke-width="2"/>
  <text class="ee-text" x="23" y="55" font-size="11">v<tspan dy="2" font-size="8">c</tspan>,v*</text>
  <text class="ee-text" x="23" y="155" font-size="11">S<tspan dy="2" font-size="8">a</tspan></text>
""", width=340, height=210, tags=["spwm", "pwm", "carrier", "modulation", "waveform", "scope"])

    # 3. Space Vector PWM (SVPWM) Hexagon & Sector Diagram (V0..V7, Sector I..VI)
    save_symbol(cat_sc, "diagram_svpwm_hexagon", "Space Vector PWM (SVPWM) Voltage Hexagon Diagram", f"""
  <rect class="ee-body" x="10" y="10" width="240" height="220" rx="4"/>
  <!-- Alpha-Beta Axes -->
  <line class="ee-grid" x1="25" y1="120" x2="235" y2="120"/>
  <line class="ee-grid" x1="130" y1="20" x2="130" y2="215"/>
  <!-- Inscribed Circle (Linear Modulation Limit) -->
  <circle class="ee-dashed" cx="130" cy="120" r="69"/>
  <!-- Hexagon Vertices (R=80 around (130,120)) -->
  <polygon class="ee-stroke" points="210,120 170,51 90,51 50,120 90,189 170,189"/>
  <!-- Active Vectors V1..V6 -->
  <line class="ee-thin" x1="130" y1="120" x2="210" y2="120"/>
  <line class="ee-thin" x1="130" y1="120" x2="170" y2="51"/>
  <line class="ee-thin" x1="130" y1="120" x2="90" y2="51"/>
  <line class="ee-thin" x1="130" y1="120" x2="50" y2="120"/>
  <line class="ee-thin" x1="130" y1="120" x2="90" y2="189"/>
  <line class="ee-thin" x1="130" y1="120" x2="170" y2="189"/>
  <!-- Synthesized Reference Vector V_ref in Sector I -->
  <line class="ee-wire-a" x1="130" y1="120" x2="182" y2="82" marker-end="url(#arrow-red)"/>
  <line class="ee-dashed" x1="168" y1="120" x2="182" y2="82"/>
  <line class="ee-dashed" x1="152" y1="82" x2="182" y2="82"/>
  <text class="ee-text" x="195" y="76" font-size="11">V<tspan dy="2" font-size="8">ref</tspan></text>
  <!-- Vector Labels -->
  <text class="ee-label" x="224" y="112">V1(100)</text>
  <text class="ee-label" x="182" y="40">V2(110)</text>
  <text class="ee-label" x="78" y="40">V3(010)</text>
  <text class="ee-label" x="32" y="112">V4(011)</text>
  <text class="ee-label" x="78" y="200">V5(001)</text>
  <text class="ee-label" x="182" y="200">V6(101)</text>
  <text class="ee-label" x="130" y="132">V0,7</text>
""", width=260, height=240, tags=["svpwm", "space vector", "hexagon", "sector", "modulation", "diagram"])

    # 4. Synchronous Machine / PMSM Phasor & Coordinate Frame Diagram (abc, αβ, dq)
    save_symbol(cat_sc, "diagram_dq_phasor_frame", "Machine Reference Frames & Phasor Diagram (abc / αβ / dq)", f"""
  <rect class="ee-body" x="10" y="10" width="230" height="210" rx="4"/>
  <!-- Stationary alpha-beta axes -->
  <line class="ee-stroke" x1="35" y1="145" x2="215" y2="145" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="95" y1="195" x2="95" y2="25" marker-end="url(#arrow)"/>
  <text class="ee-text" x="218" y="158">α (a)</text>
  <text class="ee-text" x="80" y="28">β</text>
  <!-- Rotating d-q axes (rotated by theta_e = 30 deg) -->
  <line class="ee-wire-c" x1="95" y1="145" x2="195" y2="87" marker-end="url(#arrow-blue)"/>
  <line class="ee-wire-c" x1="95" y1="145" x2="37" y2="45" marker-end="url(#arrow-blue)"/>
  <text class="ee-text" x="206" y="82">d</text>
  <text class="ee-text" x="28" y="42">q</text>
  <!-- Stator Current Vector i_s -->
  <line class="ee-wire-a" x1="95" y1="145" x2="135" y2="45" marker-end="url(#arrow-red)"/>
  <text class="ee-text" x="150" y="42">i<tspan dy="2" font-size="8">s</tspan></text>
  <!-- Rotor Flux Linkage psi_f along d-axis -->
  <line class="ee-thick" x1="95" y1="145" x2="155" y2="110" marker-end="url(#arrow)"/>
  <text class="ee-text" x="165" y="120">ψ<tspan dy="2" font-size="8">f</tspan></text>
  <!-- Angle arc theta_e -->
  <path class="ee-thin" d="M 140 145 A 45 45 0 0 0 134 122"/>
  <text class="ee-text" x="152" y="134" font-size="11">θ<tspan dy="2" font-size="8">e</tspan></text>
""", width=250, height=230, tags=["phasor diagram", "dq frame", "vector control", "foc", "pmsm", "flux linkage"])

    # 5. Soft-Switching ZVS / Dead-Time Commutation Waveform
    save_symbol(cat_sc, "waveform_zvs_commutation", "Zero-Voltage Switching (ZVS) Turn-On & Dead-Time Waveform", f"""
  <rect class="ee-body" x="10" y="10" width="300" height="190" rx="4"/>
  <!-- Shaded Dead-Time region td -->
  <rect x="95" y="25" width="45" height="145" fill="#fef3c7" stroke="none"/>
  <line class="ee-dashed" x1="95" y1="25" x2="95" y2="170"/>
  <line class="ee-dashed" x1="140" y1="25" x2="140" y2="170"/>
  <text class="ee-label" x="117" y="34">t<tspan dy="2" font-size="7">dead</tspan></text>
  <!-- High-side gate v_gs1 -->
  <path d="M 40 50 L 95 50 L 95 75 L 280 75" fill="none" stroke="#111827" stroke-width="1.8"/>
  <text class="ee-text" x="25" y="62" font-size="10">v<tspan dy="2" font-size="7">gs1</tspan></text>
  <!-- Low-side gate v_gs2 -->
  <path d="M 40 115 L 140 115 L 140 90 L 280 90" fill="none" stroke="#2563eb" stroke-width="1.8"/>
  <text class="ee-text" x="25" y="104" font-size="10">v<tspan dy="2" font-size="7">gs2</tspan></text>
  <!-- v_ds2 falling to zero BEFORE v_gs2 turns on, i_ds2 rising -->
  <path d="M 40 132 L 95 132 L 122 168 L 280 168" fill="none" stroke="#dc2626" stroke-width="2"/>
  <path d="M 40 168 L 122 168 L 140 155 L 180 132 L 280 132" fill="none" stroke="#16a34a" stroke-width="2"/>
  <circle cx="140" cy="168" r="4" fill="none" stroke="#dc2626" stroke-width="1.5"/>
  <text class="ee-label" x="172" y="178">ZVS Turn-On</text>
  <text class="ee-text" x="25" y="150" font-size="10">v<tspan dy="2" font-size="7">ds</tspan>,i<tspan dy="2" font-size="7">d</tspan></text>
""", width=320, height=210, tags=["zvs", "soft switching", "dead time", "commutation", "waveform", "llc", "dab"])

    # 6. Bode Plot (Magnitude dB & Phase deg vs Frequency) Template
    save_symbol(cat_sc, "waveform_bode_plot", "Control Loop Bode Plot (Magnitude & Phase Margin)", f"""
  <rect class="ee-body" x="10" y="10" width="300" height="200" rx="4"/>
  <!-- Axes -->
  <line class="ee-stroke" x1="45" y1="25" x2="45" y2="185"/>
  <line class="ee-grid" x1="45" y1="75" x2="290" y2="75"/>
  <line class="ee-grid" x1="45" y1="165" x2="290" y2="165"/>
  <!-- Gain curve T(s) crossing 0 dB at x=185 -->
  <path d="M 45 35 L 110 50 L 185 75 L 235 90 L 285 118" fill="none" stroke="#2563eb" stroke-width="2"/>
  <circle class="ee-node" cx="185" cy="75" r="3"/>
  <line class="ee-dashed" x1="185" y1="75" x2="185" y2="165"/>
  <!-- Phase curve crossing with Phase Margin PM -->
  <path d="M 45 125 C 100 125, 130 150, 185 142 C 225 135, 250 165, 285 178" fill="none" stroke="#dc2626" stroke-width="2"/>
  <line class="ee-thin" x1="185" y1="165" x2="185" y2="144" marker-end="url(#arrow-red)"/>
  <text class="ee-label" x="210" y="154">PM = 58°</text>
  <text class="ee-label" x="28" y="75">0dB</text>
  <text class="ee-label" x="26" y="165">-180°</text>
  <text class="ee-label" x="185" y="196">f (Hz, log scale)</text>
""", width=320, height=220, tags=["bode plot", "frequency response", "phase margin", "gain margin", "control", "stability"])

    # 7. Total Harmonic Distortion (THD) / FFT Harmonic Spectrum Bar Chart
    save_symbol(cat_sc, "waveform_fft_thd_spectrum", "Harmonic Spectrum & THD Bar Chart (IEEE 519)", f"""
  <rect class="ee-body" x="10" y="10" width="300" height="180" rx="4"/>
  <line class="ee-stroke" x1="45" y1="25" x2="45" y2="155"/>
  <line class="ee-stroke" x1="45" y1="155" x2="290" y2="155"/>
  <!-- Fundamental h=1 (100%) + Odd Harmonics 5, 7, 11, 13, 17, 19 -->
  <rect x="62" y="38" width="14" height="117" fill="#2563eb"/>
  <rect x="98" y="128" width="12" height="27" fill="#dc2626"/>
  <rect x="122" y="136" width="12" height="19" fill="#dc2626"/>
  <rect x="158" y="142" width="12" height="13" fill="#dc2626"/>
  <rect x="182" y="145" width="12" height="10" fill="#dc2626"/>
  <rect x="218" y="148" width="12" height="7" fill="#dc2626"/>
  <rect x="242" y="150" width="12" height="5" fill="#dc2626"/>
  <text class="ee-label" x="69" y="166">1</text>
  <text class="ee-label" x="104" y="166">5</text>
  <text class="ee-label" x="128" y="166">7</text>
  <text class="ee-label" x="164" y="166">11</text>
  <text class="ee-label" x="188" y="166">13</text>
  <text class="ee-label" x="224" y="166">17</text>
  <text class="ee-label" x="248" y="166">19</text>
  <text class="ee-label" x="215" y="45">THD = 2.14%</text>
  <text class="ee-label" x="170" y="180">Harmonic Order (h)</text>
""", width=320, height=195, tags=["thd", "fft", "harmonic spectrum", "power quality", "ieee 519", "bar chart"])
