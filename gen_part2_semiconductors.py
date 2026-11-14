# -*- coding: utf-8 -*-
"""
Part 2: Power Electronics Devices & Semiconductors
"""

def register_part2(save_symbol, pin, node):
    cat = "03_semiconductors"

    # 1. Power Diode (Horizontal)
    save_symbol(cat, "diode_power", "Power Diode", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="38" y2="50"/>
  <polygon class="ee-body" points="38,34 38,66 64,50"/>
  <line class="ee-stroke" x1="64" y1="34" x2="64" y2="66"/>
  <line class="ee-stroke" x1="64" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="22">D</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["diode", "rectifier", "power electronics", "D"])

    # 2. Power Diode (Filled Triangle - IEEE publication style)
    save_symbol(cat, "diode_filled", "Power Diode (Filled IEEE)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="38" y2="50"/>
  <polygon class="ee-fill" points="38,35 38,65 64,50"/>
  <line class="ee-stroke" x1="64" y1="34" x2="64" y2="66"/>
  <line class="ee-stroke" x1="64" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="22">D</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["diode", "filled", "ieee", "rectifier"])

    # 3. Schottky Diode (SiC / Fast Recovery)
    save_symbol(cat, "diode_schottky", "Schottky Barrier Diode (SiC SBD)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="38" y2="50"/>
  <polygon class="ee-body" points="38,34 38,66 64,50"/>
  <path class="ee-stroke" d="M 58 34 L 64 34 L 64 66 L 70 66"/>
  <line class="ee-stroke" x1="64" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="22">D<tspan dy="3" font-size="9">SBD</tspan></text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["schottky", "sbd", "sic", "diode", "fast"])

    # 4. Zener Diode
    save_symbol(cat, "diode_zener", "Zener Diode", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="38" y2="50"/>
  <polygon class="ee-body" points="38,34 38,66 64,50"/>
  <path class="ee-stroke" d="M 57 32 L 64 36 L 64 64 L 71 68"/>
  <line class="ee-stroke" x1="64" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="22">D<tspan dy="3" font-size="9">Z</tspan></text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["zener", "voltage reference", "clamp", "diode"])

    # 5. Bidirectional TVS Diode
    save_symbol(cat, "diode_tvs_bidir", "Bidirectional TVS Diode", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="28" y2="50"/>
  <polygon class="ee-body" points="28,36 28,64 50,50"/>
  <path class="ee-stroke" d="M 45 34 L 50 37 L 50 63 L 55 66"/>
  <polygon class="ee-body" points="72,36 72,64 50,50"/>
  <line class="ee-stroke" x1="72" y1="50" x2="90" y2="50"/>
  <text class="ee-text" x="50" y="22">TVS</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["tvs", "transient", "protection", "clamp", "diode"])

    # 6. Light Emitting Diode (LED)
    save_symbol(cat, "diode_led", "Light Emitting Diode (LED)", f"""
  <line class="ee-stroke" x1="10" y1="55" x2="38" y2="55"/>
  <polygon class="ee-body" points="38,40 38,70 64,55"/>
  <line class="ee-stroke" x1="64" y1="40" x2="64" y2="70"/>
  <line class="ee-stroke" x1="64" y1="55" x2="90" y2="55"/>
  <line class="ee-thin" x1="48" y1="34" x2="60" y2="20" marker-end="url(#arrow)"/>
  <line class="ee-thin" x1="56" y1="38" x2="68" y2="24" marker-end="url(#arrow)"/>
{pin(10, 55)}
{pin(90, 55)}
""", tags=["led", "light", "optical", "diode"])

    # 7. Photodiode
    save_symbol(cat, "diode_photo", "Photodiode", f"""
  <line class="ee-stroke" x1="10" y1="55" x2="38" y2="55"/>
  <polygon class="ee-body" points="38,40 38,70 64,55"/>
  <line class="ee-stroke" x1="64" y1="40" x2="64" y2="70"/>
  <line class="ee-stroke" x1="64" y1="55" x2="90" y2="55"/>
  <line class="ee-thin" x1="36" y1="20" x2="48" y2="34" marker-end="url(#arrow)"/>
  <line class="ee-thin" x1="46" y1="16" x2="58" y2="30" marker-end="url(#arrow)"/>
{pin(10, 55)}
{pin(90, 55)}
""", tags=["photodiode", "optical", "sensor", "pv"])

    # 8. Thyristor / SCR (Silicon Controlled Rectifier)
    save_symbol(cat, "thyristor_scr", "Thyristor / SCR", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="36"/>
  <polygon class="ee-body" points="34,36 66,36 50,62"/>
  <line class="ee-stroke" x1="34" y1="62" x2="66" y2="62"/>
  <line class="ee-stroke" x1="50" y1="62" x2="50" y2="90"/>
  <path class="ee-stroke" d="M 38 62 L 26 74 L 14 74"/>
  <text class="ee-text" x="78" y="48">SCR</text>
{pin(50, 10)}
{pin(50, 90)}
{pin(14, 74)}
""", tags=["thyristor", "scr", "hvdc", "facts", "phase control"])

    # 9. GTO / IGCT (Gate Turn-Off Thyristor)
    save_symbol(cat, "thyristor_gto_igct", "GTO / IGCT Thyristor", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="36"/>
  <polygon class="ee-body" points="34,36 66,36 50,62"/>
  <line class="ee-stroke" x1="34" y1="62" x2="66" y2="62"/>
  <line class="ee-stroke" x1="50" y1="62" x2="50" y2="90"/>
  <path class="ee-stroke" d="M 38 62 L 26 74 L 14 74"/>
  <line class="ee-thin" x1="25" y1="67" x2="33" y2="75"/>
  <text class="ee-text" x="78" y="48">GTO</text>
{pin(50, 10)}
{pin(50, 90)}
{pin(14, 74)}
""", tags=["gto", "igct", "thyristor", "high power"])

    # 10. TRIAC (Bidirectional Triode Thyristor)
    save_symbol(cat, "triac", "TRIAC (Bidirectional Thyristor)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="34"/>
  <line class="ee-stroke" x1="28" y1="34" x2="72" y2="34"/>
  <polygon class="ee-body" points="28,34 48,34 38,56"/>
  <polygon class="ee-body" points="52,56 72,56 62,34"/>
  <line class="ee-stroke" x1="28" y1="56" x2="72" y2="56"/>
  <line class="ee-stroke" x1="50" y1="56" x2="50" y2="90"/>
  <path class="ee-stroke" d="M 62 56 L 74 70 L 86 70"/>
{pin(50, 10)}
{pin(50, 90)}
{pin(86, 70)}
""", tags=["triac", "ac switch", "dimmer", "thyristor"])

    # 11. IGBT (Bare N-Channel)
    save_symbol(cat, "igbt_bare", "IGBT (Insulated Gate Bipolar Transistor)", f"""
  <line class="ee-stroke" x1="12" y1="58" x2="32" y2="58"/>
  <line class="ee-stroke" x1="32" y1="32" x2="32" y2="68"/>
  <line class="ee-stroke" x1="39" y1="28" x2="39" y2="72"/>
  <path class="ee-stroke" d="M 39 40 L 60 26 L 60 10"/>
  <path class="ee-stroke" d="M 39 60 L 58 72" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="60" y1="73" x2="60" y2="90"/>
  <text class="ee-text" x="78" y="50">S</text>
{pin(12, 58)}
{pin(60, 10)}
{pin(60, 90)}
""", tags=["igbt", "transistor", "switch", "power electronics"])

    # 12. IGBT with Anti-Parallel Freewheeling Diode (Standard Power Switch Cell)
    save_symbol(cat, "igbt_with_diode", "IGBT with Anti-Parallel Diode", f"""
  <line class="ee-stroke" x1="10" y1="58" x2="26" y2="58"/>
  <line class="ee-stroke" x1="26" y1="32" x2="26" y2="68"/>
  <line class="ee-stroke" x1="33" y1="28" x2="33" y2="72"/>
  <path class="ee-stroke" d="M 33 40 L 50 28 L 50 10"/>
  <path class="ee-stroke" d="M 33 60 L 48 70" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="50" y1="71" x2="50" y2="90"/>
  <!-- Anti-parallel diode -->
  <path class="ee-stroke" d="M 50 22 L 74 22 L 74 78 L 50 78"/>
  <polygon class="ee-body" points="64,58 84,58 74,40"/>
  <line class="ee-stroke" x1="64" y1="40" x2="84" y2="40"/>
{node(50, 22)}
{node(50, 78)}
{pin(10, 58)}
{pin(50, 10)}
{pin(50, 90)}
""", tags=["igbt", "freewheeling diode", "switch cell", "inverter", "power switch"])

    # 13. Power MOSFET (N-Channel with Body Diode - Si / SiC)
    save_symbol(cat, "mosfet_nch_power", "Power MOSFET (N-Ch with Body Diode)", f"""
  <line class="ee-stroke" x1="10" y1="60" x2="26" y2="60"/>
  <line class="ee-stroke" x1="26" y1="32" x2="26" y2="68"/>
  <!-- Broken channel -->
  <line class="ee-stroke" x1="33" y1="30" x2="33" y2="40"/>
  <line class="ee-stroke" x1="33" y1="45" x2="33" y2="55"/>
  <line class="ee-stroke" x1="33" y1="60" x2="33" y2="70"/>
  <!-- Drain, Source, Substrate -->
  <path class="ee-stroke" d="M 33 35 L 52 35 L 52 10"/>
  <path class="ee-stroke" d="M 52 50 L 36 50" marker-end="url(#arrow)"/>
  <path class="ee-stroke" d="M 33 65 L 52 65 L 52 90"/>
  <line class="ee-stroke" x1="52" y1="50" x2="52" y2="65"/>
  <!-- Body Diode -->
  <path class="ee-stroke" d="M 52 24 L 74 24 L 74 76 L 52 76"/>
  <polygon class="ee-body" points="65,58 83,58 74,42"/>
  <line class="ee-stroke" x1="65" y1="42" x2="83" y2="42"/>
{node(52, 24)}
{node(52, 65)}
{node(52, 76)}
{pin(10, 60)}
{pin(52, 10)}
{pin(52, 90)}
""", tags=["mosfet", "sic", "power mosfet", "body diode", "n-channel", "switch"])

    # 14. Power MOSFET (P-Channel)
    save_symbol(cat, "mosfet_pch_power", "Power MOSFET (P-Channel)", f"""
  <line class="ee-stroke" x1="12" y1="60" x2="28" y2="60"/>
  <line class="ee-stroke" x1="28" y1="32" x2="28" y2="68"/>
  <line class="ee-stroke" x1="35" y1="30" x2="35" y2="40"/>
  <line class="ee-stroke" x1="35" y1="45" x2="35" y2="55"/>
  <line class="ee-stroke" x1="35" y1="60" x2="35" y2="70"/>
  <path class="ee-stroke" d="M 35 35 L 56 35 L 56 10"/>
  <path class="ee-stroke" d="M 35 50 L 53 50" marker-end="url(#arrow)"/>
  <path class="ee-stroke" d="M 35 65 L 56 65 L 56 90"/>
  <line class="ee-stroke" x1="56" y1="35" x2="56" y2="50"/>
{node(56, 35)}
{pin(12, 60)}
{pin(56, 10)}
{pin(56, 90)}
""", tags=["mosfet", "p-channel", "pmos", "high side"])

    # 15. SiC MOSFET with Kelvin Source (4-Pin Package TO-247-4)
    save_symbol(cat, "sic_mosfet_kelvin", "SiC MOSFET (4-Pin Kelvin Source)", f"""
  <circle class="ee-dashed" cx="50" cy="50" r="34"/>
  <line class="ee-stroke" x1="10" y1="56" x2="28" y2="56"/>
  <line class="ee-stroke" x1="28" y1="34" x2="28" y2="66"/>
  <line class="ee-stroke" x1="34" y1="32" x2="34" y2="41"/>
  <line class="ee-stroke" x1="34" y1="46" x2="34" y2="54"/>
  <line class="ee-stroke" x1="34" y1="59" x2="34" y2="68"/>
  <path class="ee-stroke" d="M 34 36 L 54 36 L 54 10"/>
  <path class="ee-stroke" d="M 54 50 L 37 50" marker-end="url(#arrow)"/>
  <path class="ee-stroke" d="M 34 64 L 54 64 L 54 90"/>
  <line class="ee-stroke" x1="54" y1="50" x2="54" y2="64"/>
  <!-- Kelvin source pin -->
  <path class="ee-thin" d="M 54 68 L 28 68 L 10 74"/>
  <text class="ee-label" x="18" y="48">G</text>
  <text class="ee-label" x="18" y="82">S<tspan dy="2" font-size="7">K</tspan></text>
{node(54, 64)}
{node(54, 68)}
{pin(10, 56)}
{pin(10, 74)}
{pin(54, 10)}
{pin(54, 90)}
""", tags=["sic", "mosfet", "kelvin source", "4-pin", "wide bandgap", "wbg"])

    # 16. GaN HEMT (Enhancement Mode e-GaN FET)
    save_symbol(cat, "gan_hemt", "GaN HEMT (Enhancement-Mode FET)", f"""
  <rect class="ee-tint-blue" x="20" y="24" width="56" height="52" rx="4"/>
  <line class="ee-stroke" x1="8" y1="50" x2="28" y2="50"/>
  <line class="ee-stroke" x1="28" y1="34" x2="28" y2="66"/>
  <line class="ee-thick" x1="35" y1="32" x2="35" y2="68"/>
  <path class="ee-stroke" d="M 35 38 L 54 38 L 54 10"/>
  <path class="ee-stroke" d="M 35 62 L 54 62 L 54 90"/>
  <text class="ee-label" x="56" y="50">GaN</text>
{pin(8, 50)}
{pin(54, 10)}
{pin(54, 90)}
""", tags=["gan", "hemt", "wide bandgap", "wbg", "fet", "high frequency"])

    # 17. BJT NPN Transistor
    save_symbol(cat, "bjt_npn", "BJT Transistor (NPN)", f"""
  <line class="ee-stroke" x1="12" y1="50" x2="36" y2="50"/>
  <line class="ee-thick" x1="36" y1="30" x2="36" y2="70"/>
  <path class="ee-stroke" d="M 36 40 L 60 24 L 60 10"/>
  <path class="ee-stroke" d="M 36 60 L 58 74" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="60" y1="75" x2="60" y2="90"/>
{pin(12, 50)}
{pin(60, 10)}
{pin(60, 90)}
""", tags=["bjt", "npn", "transistor", "bipolar"])

    # 18. BJT PNP Transistor
    save_symbol(cat, "bjt_pnp", "BJT Transistor (PNP)", f"""
  <line class="ee-stroke" x1="12" y1="50" x2="36" y2="50"/>
  <line class="ee-thick" x1="36" y1="30" x2="36" y2="70"/>
  <path class="ee-stroke" d="M 36 40 L 60 24 L 60 10"/>
  <path class="ee-stroke" d="M 60 76 L 39 62" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="60" y1="76" x2="60" y2="90"/>
{pin(12, 50)}
{pin(60, 10)}
{pin(60, 90)}
""", tags=["bjt", "pnp", "transistor", "bipolar"])

    # 19. Ideal Power Switch (with Gate Control Input)
    save_symbol(cat, "ideal_power_switch", "Ideal Power Switch (Gate Controlled)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="34"/>
  <line class="ee-stroke" x1="50" y1="66" x2="50" y2="90"/>
  <line class="ee-stroke" x1="50" y1="66" x2="32" y2="36"/>
  <line class="ee-dashed" x1="14" y1="50" x2="38" y2="50" marker-end="url(#arrow)"/>
  <circle class="ee-pin" cx="50" cy="34" r="2.5"/>
  <circle class="ee-pin" cx="50" cy="66" r="2.5"/>
  <text class="ee-text" x="72" y="50">S</text>
{pin(50, 10)}
{pin(50, 90)}
{pin(14, 50)}
""", tags=["ideal switch", "pwm switch", "chopper", "switch"])

    # 20. Bidirectional 4-Quadrant Switch (Common-Emitter Anti-Series IGBTs)
    save_symbol(cat, "bidirectional_switch_4q", "Bidirectional 4-Quadrant Switch (Matrix/T-Type)", f"""
  <rect class="ee-body" x="18" y="24" width="64" height="52" rx="4"/>
  <line class="ee-stroke" x1="4" y1="50" x2="18" y2="50"/>
  <line class="ee-stroke" x1="82" y1="50" x2="96" y2="50"/>
  <polygon class="ee-body" points="28,34 28,50 44,42"/>
  <line class="ee-stroke" x1="44" y1="34" x2="44" y2="50"/>
  <polygon class="ee-body" points="72,34 72,50 56,42"/>
  <line class="ee-stroke" x1="56" y1="34" x2="56" y2="50"/>
  <line class="ee-stroke" x1="22" y1="42" x2="78" y2="42"/>
  <path class="ee-stroke" d="M 28 62 L 42 54 L 58 54 L 72 62"/>
  <line class="ee-stroke" x1="38" y1="66" x2="62" y2="66"/>
  <line class="ee-stroke" x1="50" y1="66" x2="50" y2="88"/>
{pin(4, 50)}
{pin(96, 50)}
{pin(50, 88)}
""", tags=["bidirectional switch", "4-quadrant", "matrix converter", "t-type", "ac switch"])

    # 21. Half-Bridge Phase Leg Module (2-in-1 Power Module)
    save_symbol(cat, "half_bridge_leg_module", "Half-Bridge Phase Leg Module (2-in-1)", f"""
  <rect class="ee-body" x="18" y="10" width="64" height="120" rx="5"/>
  <!-- Upper switch -->
  <line class="ee-stroke" x1="46" y1="10" x2="46" y2="28"/>
  <line class="ee-stroke" x1="34" y1="28" x2="34" y2="48"/>
  <path class="ee-stroke" d="M 34 33 L 46 25"/>
  <path class="ee-stroke" d="M 34 43 L 46 51" marker-end="url(#arrow)"/>
  <polygon class="ee-body" points="58,44 68,44 63,32"/>
  <line class="ee-stroke" x1="58" y1="32" x2="68" y2="32"/>
  <path class="ee-thin" d="M 46 22 L 63 22 L 63 54 L 46 54"/>
  <!-- Midpoint -->
  <line class="ee-stroke" x1="46" y1="51" x2="46" y2="88"/>
  <line class="ee-stroke" x1="46" y1="70" x2="92" y2="70"/>
  <!-- Lower switch -->
  <line class="ee-stroke" x1="34" y1="84" x2="34" y2="104"/>
  <path class="ee-stroke" d="M 34 89 L 46 81"/>
  <path class="ee-stroke" d="M 34 99 L 46 107" marker-end="url(#arrow)"/>
  <polygon class="ee-body" points="58,100 68,100 63,88"/>
  <line class="ee-stroke" x1="58" y1="88" x2="68" y2="88"/>
  <path class="ee-thin" d="M 46 78 L 63 78 L 63 110 L 46 110"/>
  <line class="ee-stroke" x1="46" y1="107" x2="46" y2="130"/>
  <text class="ee-label" x="32" y="18">+DC</text>
  <text class="ee-label" x="32" y="122">-DC</text>
  <text class="ee-label" x="74" y="62">AC</text>
{node(46, 70)}
{pin(46, 10)}
{pin(46, 130)}
{pin(92, 70)}
""", width=100, height=140, tags=["half bridge", "phase leg", "power module", "2-in-1", "inverter leg"])

    # 22. Optocoupler / Isolated Gate Driver IC
    save_symbol(cat, "optocoupler_isolated_driver", "Optocoupler / Isolated Gate Driver", f"""
  <rect class="ee-body" x="16" y="20" width="68" height="60" rx="4"/>
  <line class="ee-dashed" x1="50" y1="20" x2="50" y2="80"/>
  <!-- LED side -->
  <path class="ee-stroke" d="M 6 35 L 30 35 L 30 42"/>
  <polygon class="ee-body" points="23,42 37,42 30,54"/>
  <line class="ee-stroke" x1="23" y1="54" x2="37" y2="54"/>
  <path class="ee-stroke" d="M 30 54 L 30 65 L 6 65"/>
  <!-- Arrows -->
  <line class="ee-thin" x1="39" y1="44" x2="48" y2="44" marker-end="url(#arrow)"/>
  <line class="ee-thin" x1="39" y1="52" x2="48" y2="52" marker-end="url(#arrow)"/>
  <!-- Output BJT/Buffer side -->
  <line class="ee-stroke" x1="60" y1="36" x2="60" y2="64"/>
  <path class="ee-stroke" d="M 60 42 L 72 34 L 94 34"/>
  <path class="ee-stroke" d="M 60 58 L 72 66" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="72" y1="66" x2="94" y2="66"/>
{pin(6, 35)}
{pin(6, 65)}
{pin(94, 34)}
{pin(94, 66)}
""", tags=["optocoupler", "gate driver", "isolation", "galvanic"])
