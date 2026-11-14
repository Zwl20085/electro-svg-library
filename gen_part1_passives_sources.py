# -*- coding: utf-8 -*-
"""
Part 1: Passives, Magnetics, Sources, Grounds, and Connections
"""

def register_part1(save_symbol, pin, node):
    # ==========================================
    # CATEGORY 01: PASSIVE COMPONENTS & MAGNETICS
    # ==========================================
    cat = "01_passives"

    # 1. Resistor (IEEE Zigzag)
    save_symbol(cat, "resistor_ieee", "Resistor (IEEE)", f"""
  <path class="ee-stroke" d="M 10 50 L 26 50 L 30 40 L 38 60 L 46 40 L 54 60 L 62 40 L 70 60 L 74 50 L 90 50"/>
  <text class="ee-text" x="50" y="28">R</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["resistor", "ieee", "zigzag", "passive", "R"])

    # 2. Resistor (IEC Box)
    save_symbol(cat, "resistor_iec", "Resistor (IEC)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="28" y2="50"/>
  <rect class="ee-body" x="28" y="40" width="44" height="20"/>
  <line class="ee-stroke" x1="72" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="28">R</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["resistor", "iec", "box", "passive", "R"])

    # 3. Variable Resistor / Rheostat
    save_symbol(cat, "resistor_variable", "Variable Resistor (Rheostat)", f"""
  <path class="ee-stroke" d="M 10 50 L 26 50 L 30 40 L 38 60 L 46 40 L 54 60 L 62 40 L 70 60 L 74 50 L 90 50"/>
  <line class="ee-thin" x1="30" y1="68" x2="70" y2="30" marker-end="url(#arrow)"/>
  <text class="ee-text" x="45" y="22">R</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["resistor", "variable", "rheostat", "tunable"])

    # 4. Potentiometer (3-terminal)
    save_symbol(cat, "potentiometer", "Potentiometer (3-Terminal)", f"""
  <path class="ee-stroke" d="M 10 55 L 26 55 L 30 45 L 38 65 L 46 45 L 54 65 L 62 45 L 70 65 L 74 55 L 90 55"/>
  <path class="ee-stroke" d="M 50 15 L 50 40" marker-end="url(#arrow)"/>
{pin(10, 55)}
{pin(90, 55)}
{pin(50, 15)}
""", tags=["potentiometer", "divider", "resistor", "wiper"])

    # 5. Shunt Resistor (4-wire Kelvin)
    save_symbol(cat, "resistor_shunt_kelvin", "Current Shunt (4-Wire Kelvin)", f"""
  <line class="ee-stroke" x1="10" y1="45" x2="28" y2="45"/>
  <rect class="ee-body" x="28" y="36" width="44" height="18"/>
  <line class="ee-stroke" x1="72" y1="45" x2="90" y2="45"/>
  <path class="ee-thin" d="M 32 54 L 38 68 L 38 82"/>
  <path class="ee-thin" d="M 68 54 L 62 68 L 62 82"/>
  <text class="ee-text" x="50" y="24">R<tspan dy="3" font-size="9">sh</tspan></text>
{pin(10, 45)}
{pin(90, 45)}
{pin(38, 82)}
{pin(62, 82)}
""", tags=["shunt", "kelvin", "current sense", "resistor"])

    # 6. Capacitor (Non-polarized)
    save_symbol(cat, "capacitor_unpolarized", "Capacitor (Non-Polarized)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="45" y2="50"/>
  <line class="ee-stroke" x1="45" y1="30" x2="45" y2="70"/>
  <line class="ee-stroke" x1="55" y1="30" x2="55" y2="70"/>
  <line class="ee-stroke" x1="55" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="18">C</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["capacitor", "C", "passive", "film", "ceramic"])

    # 7. Polarized / Electrolytic Capacitor (Curved Plate IEEE)
    save_symbol(cat, "capacitor_polarized_ieee", "Polarized Capacitor (IEEE)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="45" y2="50"/>
  <line class="ee-stroke" x1="45" y1="30" x2="45" y2="70"/>
  <path class="ee-stroke" d="M 58 30 Q 49 50 58 70"/>
  <line class="ee-stroke" x1="54" y1="50" x2="90" y2="50"/>
  <text class="ee-label" x="35" y="34">+</text>
  <text class="ee-text" x="50" y="18">C<tspan dy="3" font-size="9">dc</tspan></text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["capacitor", "polarized", "electrolytic", "dc-link", "C"])

    # 8. Polarized Capacitor (IEC Box Plate)
    save_symbol(cat, "capacitor_polarized_iec", "Polarized Capacitor (IEC)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="43" y2="50"/>
  <rect class="ee-body" x="43" y="30" width="6" height="40"/>
  <rect class="ee-fill" x="54" y="30" width="5" height="40"/>
  <line class="ee-stroke" x1="59" y1="50" x2="90" y2="50"/>
  <text class="ee-label" x="35" y="34">+</text>
  <text class="ee-text" x="50" y="18">C</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["capacitor", "polarized", "iec", "electrolytic"])

    # 9. Variable Capacitor
    save_symbol(cat, "capacitor_variable", "Variable Capacitor", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="45" y2="50"/>
  <line class="ee-stroke" x1="45" y1="30" x2="45" y2="70"/>
  <line class="ee-stroke" x1="55" y1="30" x2="55" y2="70"/>
  <line class="ee-stroke" x1="55" y1="50" x2="90" y2="50"/>
  <line class="ee-thin" x1="32" y1="68" x2="68" y2="32" marker-end="url(#arrow)"/>
  <text class="ee-text" x="42" y="18">C</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["capacitor", "variable", "tunable"])

    # 10. Inductor (Air Core, 4 Arches)
    save_symbol(cat, "inductor_air", "Inductor (Air Core)", f"""
  <path class="ee-stroke" d="M 10 55 L 22 55 A 7 9 0 0 1 36 55 A 7 9 0 0 1 50 55 A 7 9 0 0 1 64 55 A 7 9 0 0 1 78 55 L 90 55"/>
  <text class="ee-text" x="50" y="30">L</text>
{pin(10, 55)}
{pin(90, 55)}
""", tags=["inductor", "coil", "choke", "L", "air core"])

    # 11. Inductor (Iron Core)
    save_symbol(cat, "inductor_iron_core", "Inductor (Iron Core)", f"""
  <path class="ee-stroke" d="M 10 58 L 22 58 A 7 9 0 0 1 36 58 A 7 9 0 0 1 50 58 A 7 9 0 0 1 64 58 A 7 9 0 0 1 78 58 L 90 58"/>
  <line class="ee-stroke" x1="22" y1="42" x2="78" y2="42"/>
  <line class="ee-stroke" x1="22" y1="37" x2="78" y2="37"/>
  <text class="ee-text" x="50" y="23">L</text>
{pin(10, 58)}
{pin(90, 58)}
""", tags=["inductor", "iron core", "magnetic", "choke", "L"])

    # 12. Inductor (Ferrite Core)
    save_symbol(cat, "inductor_ferrite_core", "Inductor (Ferrite Core)", f"""
  <path class="ee-stroke" d="M 10 58 L 22 58 A 7 9 0 0 1 36 58 A 7 9 0 0 1 50 58 A 7 9 0 0 1 64 58 A 7 9 0 0 1 78 58 L 90 58"/>
  <line class="ee-dashed" x1="22" y1="41" x2="78" y2="41"/>
  <line class="ee-dashed" x1="22" y1="36" x2="78" y2="36"/>
  <text class="ee-text" x="50" y="23">L<tspan dy="3" font-size="9">f</tspan></text>
{pin(10, 58)}
{pin(90, 58)}
""", tags=["inductor", "ferrite", "high frequency", "L"])

    # 13. Variable / Saturable Inductor
    save_symbol(cat, "inductor_variable", "Variable / Saturable Inductor", f"""
  <path class="ee-stroke" d="M 10 55 L 22 55 A 7 9 0 0 1 36 55 A 7 9 0 0 1 50 55 A 7 9 0 0 1 64 55 A 7 9 0 0 1 78 55 L 90 55"/>
  <line class="ee-thin" x1="28" y1="70" x2="72" y2="32" marker-end="url(#arrow)"/>
  <text class="ee-text" x="44" y="24">L</text>
{pin(10, 55)}
{pin(90, 55)}
""", tags=["inductor", "variable", "saturable"])

    # 14. Coupled Inductor / Common-Mode Choke
    save_symbol(cat, "coupled_inductor_cmc", "Coupled Inductor / Common-Mode Choke", f"""
  <path class="ee-stroke" d="M 10 30 L 22 30 A 7 8 0 0 0 36 30 A 7 8 0 0 0 50 30 A 7 8 0 0 0 64 30 A 7 8 0 0 0 78 30 L 90 30"/>
  <line class="ee-stroke" x1="22" y1="47" x2="78" y2="47"/>
  <line class="ee-stroke" x1="22" y1="53" x2="78" y2="53"/>
  <path class="ee-stroke" d="M 10 70 L 22 70 A 7 8 0 0 1 36 70 A 7 8 0 0 1 50 70 A 7 8 0 0 1 64 70 A 7 8 0 0 1 78 70 L 90 70"/>
  <circle class="ee-node" cx="20" cy="22" r="2.2"/>
  <circle class="ee-node" cx="20" cy="78" r="2.2"/>
{pin(10, 30)}
{pin(90, 30)}
{pin(10, 70)}
{pin(90, 70)}
""", tags=["coupled inductor", "common mode choke", "cmc", "emi filter", "dot convention"])

    # 15. Ferrite Bead
    save_symbol(cat, "ferrite_bead", "Ferrite Bead", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="90" y2="50"/>
  <polygon class="ee-body" points="40,34 64,34 58,66 34,66"/>
  <text class="ee-text" x="50" y="22">FB</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["ferrite bead", "emi", "filter", "FB"])

    # 16. Thermistor (NTC/PTC)
    save_symbol(cat, "thermistor_ntc", "Thermistor (NTC/PTC)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="28" y2="50"/>
  <rect class="ee-body" x="28" y="40" width="44" height="20"/>
  <line class="ee-stroke" x1="72" y1="50" x2="90" y2="50"/>
  <path class="ee-thin" d="M 26 68 L 36 68 L 66 30"/>
  <text class="ee-label" x="50" y="24">t°</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["thermistor", "ntc", "ptc", "temperature", "inrush"])

    # 17. Varistor / MOV (Surge Arrester)
    save_symbol(cat, "varistor_mov", "Metal Oxide Varistor (MOV)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="28" y2="50"/>
  <rect class="ee-body" x="28" y="40" width="44" height="20"/>
  <line class="ee-stroke" x1="72" y1="50" x2="90" y2="50"/>
  <path class="ee-thin" d="M 28 68 L 38 68 L 64 30"/>
  <text class="ee-label" x="50" y="24">U</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["varistor", "mov", "surge", "overvoltage", "protection"])

    # 18. Quartz Crystal / Resonator
    save_symbol(cat, "crystal_resonator", "Quartz Crystal Resonator", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="36" y2="50"/>
  <line class="ee-stroke" x1="36" y1="32" x2="36" y2="68"/>
  <rect class="ee-body" x="43" y="28" width="14" height="44"/>
  <line class="ee-stroke" x1="64" y1="32" x2="64" y2="68"/>
  <line class="ee-stroke" x1="64" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="16">XTAL</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["crystal", "xtal", "resonator", "clock", "piezo"])

    # 19. Memristor
    save_symbol(cat, "memristor", "Memristor", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="26" y2="50"/>
  <rect class="ee-body" x="26" y="36" width="48" height="28"/>
  <path class="ee-stroke" d="M 26 50 L 36 50 L 36 42 L 46 42 L 46 58 L 56 58 L 56 42 L 66 42 L 66 50"/>
  <rect class="ee-fill" x="68" y="36" width="6" height="28"/>
  <line class="ee-stroke" x1="74" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="22">M</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["memristor", "nonlinear", "M"])

    # ==========================================
    # CATEGORY 02: SOURCES, GROUNDS & TERMINALS
    # ==========================================
    cat2 = "02_sources_grounds"

    # 20. Independent DC Voltage Source (Circle)
    save_symbol(cat2, "source_dc_voltage", "DC Voltage Source", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="28"/>
  <circle class="ee-body" cx="50" cy="50" r="22"/>
  <line class="ee-stroke" x1="50" y1="72" x2="50" y2="90"/>
  <path class="ee-thin" d="M 46 39 L 54 39 M 50 35 L 50 43"/>
  <line class="ee-thin" x1="46" y1="61" x2="54" y2="61"/>
  <text class="ee-text" x="82" y="50">V<tspan dy="3" font-size="9">dc</tspan></text>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["voltage source", "dc", "Vdc", "source"])

    # 21. Battery / Multi-cell DC Source
    save_symbol(cat2, "source_battery", "Battery Cell / Pack", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="38"/>
  <line class="ee-stroke" x1="30" y1="38" x2="70" y2="38"/>
  <line class="ee-thick" x1="40" y1="46" x2="60" y2="46"/>
  <line class="ee-stroke" x1="30" y1="54" x2="70" y2="54"/>
  <line class="ee-thick" x1="40" y1="62" x2="60" y2="62"/>
  <line class="ee-stroke" x1="50" y1="62" x2="50" y2="90"/>
  <text class="ee-label" x="24" y="32">+</text>
  <text class="ee-text" x="82" y="50">V<tspan dy="3" font-size="9">bat</tspan></text>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["battery", "cell", "ess", "dc", "storage"])

    # 22. Independent AC Voltage Source
    save_symbol(cat2, "source_ac_voltage", "AC Voltage Source (Sinusoidal)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="28"/>
  <circle class="ee-body" cx="50" cy="50" r="22"/>
  <path class="ee-stroke" d="M 38 50 C 42 38, 46 38, 50 50 C 54 62, 58 62, 62 50"/>
  <line class="ee-stroke" x1="50" y1="72" x2="50" y2="90"/>
  <text class="ee-text" x="82" y="50">v<tspan dy="3" font-size="9">s</tspan></text>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["ac source", "grid", "sine", "voltage source"])

    # 23. Independent Current Source
    save_symbol(cat2, "source_current", "Independent Current Source", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="28"/>
  <circle class="ee-body" cx="50" cy="50" r="22"/>
  <line class="ee-stroke" x1="50" y1="64" x2="50" y2="38" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="50" y1="72" x2="50" y2="90"/>
  <text class="ee-text" x="82" y="50">I<tspan dy="3" font-size="9">s</tspan></text>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["current source", "Is", "source"])

    # 24. Controlled / Dependent Voltage Source (Diamond)
    save_symbol(cat2, "source_controlled_voltage", "Controlled Voltage Source (VCVS/CCVS)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="26"/>
  <polygon class="ee-body" points="50,26 74,50 50,74 26,50"/>
  <path class="ee-thin" d="M 46 40 L 54 40 M 50 36 L 50 44"/>
  <line class="ee-thin" x1="46" y1="60" x2="54" y2="60"/>
  <line class="ee-stroke" x1="50" y1="74" x2="50" y2="90"/>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["dependent source", "controlled voltage", "vcvs", "ccvs", "diamond"])

    # 25. Controlled / Dependent Current Source (Diamond)
    save_symbol(cat2, "source_controlled_current", "Controlled Current Source (VCCS/CCCS)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="26"/>
  <polygon class="ee-body" points="50,26 74,50 50,74 26,50"/>
  <line class="ee-stroke" x1="50" y1="63" x2="50" y2="39" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="50" y1="74" x2="50" y2="90"/>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["dependent source", "controlled current", "vccs", "cccs", "diamond"])

    # 26. Photovoltaic (PV) Solar Array Symbol
    save_symbol(cat2, "source_pv_array", "Photovoltaic (PV) Solar Panel / Array", f"""
  <line class="ee-stroke" x1="55" y1="10" x2="55" y2="28"/>
  <circle class="ee-body" cx="55" cy="50" r="22"/>
  <line class="ee-stroke" x1="43" y1="45" x2="67" y2="45"/>
  <line class="ee-thick" x1="48" y1="53" x2="62" y2="53"/>
  <line class="ee-stroke" x1="55" y1="28" x2="55" y2="45"/>
  <line class="ee-stroke" x1="55" y1="53" x2="55" y2="72"/>
  <line class="ee-stroke" x1="55" y1="72" x2="55" y2="90"/>
  <line class="ee-thin" x1="18" y1="30" x2="32" y2="40" marker-end="url(#arrow)"/>
  <line class="ee-thin" x1="14" y1="40" x2="28" y2="50" marker-end="url(#arrow)"/>
  <text class="ee-text" x="85" y="50">PV</text>
{pin(55, 10)}
{pin(55, 90)}
""", tags=["pv", "solar", "renewable", "photovoltaic", "source"])

    # 27. Three-Phase AC Grid / Infinite Bus Source
    save_symbol(cat2, "source_3ph_grid", "Three-Phase AC Grid Source", f"""
  <circle class="ee-body" cx="42" cy="50" r="24"/>
  <path class="ee-stroke" d="M 30 50 C 34 38, 38 38, 42 50 C 46 62, 50 62, 54 50"/>
  <text class="ee-label" x="42" y="34">3~</text>
  <line class="ee-wire-a" x1="63" y1="36" x2="90" y2="36"/>
  <line class="ee-wire-b" x1="66" y1="50" x2="90" y2="50"/>
  <line class="ee-wire-c" x1="63" y1="64" x2="90" y2="64"/>
  <line class="ee-stroke" x1="42" y1="74" x2="42" y2="86"/>
  <line class="ee-stroke" x1="32" y1="86" x2="52" y2="86"/>
  <line class="ee-stroke" x1="36" y1="90" x2="48" y2="90"/>
{pin(90, 36)}
{pin(90, 50)}
{pin(90, 64)}
""", tags=["three phase", "grid", "utility", "3ph", "ac source"])

    # 28. Earth Ground (Standard)
    save_symbol(cat2, "ground_earth", "Earth Ground", f"""
  <line class="ee-stroke" x1="50" y1="15" x2="50" y2="50"/>
  <line class="ee-stroke" x1="30" y1="50" x2="70" y2="50"/>
  <line class="ee-stroke" x1="37" y1="58" x2="63" y2="58"/>
  <line class="ee-stroke" x1="44" y1="66" x2="56" y2="66"/>
{pin(50, 15)}
""", tags=["ground", "earth", "gnd", "reference"])

    # 29. Chassis / Frame Ground
    save_symbol(cat2, "ground_chassis", "Chassis / Frame Ground", f"""
  <line class="ee-stroke" x1="50" y1="15" x2="50" y2="50"/>
  <path class="ee-stroke" d="M 30 50 L 70 50 M 30 50 L 22 64 M 50 50 L 42 64 M 70 50 L 62 64"/>
{pin(50, 15)}
""", tags=["ground", "chassis", "frame", "enclosure"])

    # 30. Signal / Digital Ground (Triangle)
    save_symbol(cat2, "ground_signal", "Signal / Digital Ground", f"""
  <line class="ee-stroke" x1="50" y1="15" x2="50" y2="50"/>
  <polygon class="ee-body" points="32,50 68,50 50,70"/>
{pin(50, 15)}
""", tags=["ground", "signal", "analog", "digital", "triangle"])
