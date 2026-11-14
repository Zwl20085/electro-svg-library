# -*- coding: utf-8 -*-
"""
Part 4: Control Blocks, Coordinate Transforms, Protection, Switchgear, Sensors & Analog
"""

def register_part4(save_symbol, pin, node):
    # ==========================================
    # CATEGORY 06: CONTROL BLOCKS & COORDINATE TRANSFORMS
    # ==========================================
    cat_ctrl = "06_control_blocks"

    # 1. Summing / Subtracting Junction
    save_symbol(cat_ctrl, "control_summing_junction", "Summing / Subtracting Junction", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="32" y2="50" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="50" y1="90" x2="50" y2="68" marker-end="url(#arrow)"/>
  <circle class="ee-body" cx="50" cy="50" r="16"/>
  <line class="ee-thin" x1="39" y1="39" x2="61" y2="61"/>
  <line class="ee-thin" x1="39" y1="61" x2="61" y2="39"/>
  <line class="ee-stroke" x1="66" y1="50" x2="90" y2="50" marker-end="url(#arrow)"/>
  <text class="ee-label" x="28" y="38">+</text>
  <text class="ee-label" x="62" y="74">−</text>
{pin(10, 50)}
{pin(50, 90)}
{pin(90, 50)}
""", tags=["summing junction", "error", "comparator", "control block", "feedback"])

    # 2. PI / PID Controller Block
    save_symbol(cat_ctrl, "control_pi_regulator", "PI / PID Controller Block", f"""
  <line class="ee-stroke" x1="6" y1="50" x2="20" y2="50" marker-end="url(#arrow)"/>
  <rect class="ee-tint-blue" x="22" y="26" width="56" height="48" rx="4"/>
  <text class="ee-label" x="50" y="38">PI</text>
  <path class="ee-thin" d="M 32 62 L 38 62 L 38 52 L 66 40"/>
  <line class="ee-stroke" x1="78" y1="50" x2="94" y2="50" marker-end="url(#arrow)"/>
{pin(6, 50)}
{pin(94, 50)}
""", tags=["pi controller", "pid", "regulator", "control", "compensator"])

    # 3. PR (Proportional-Resonant) Controller Block
    save_symbol(cat_ctrl, "control_pr_regulator", "PR (Proportional-Resonant) Controller", f"""
  <line class="ee-stroke" x1="6" y1="50" x2="20" y2="50" marker-end="url(#arrow)"/>
  <rect class="ee-tint-blue" x="22" y="24" width="56" height="52" rx="4"/>
  <text class="ee-label" x="50" y="38">PR</text>
  <text class="ee-text" x="50" y="58" font-size="10">K<tspan dy="2" font-size="7">p</tspan>+K<tspan dy="2" font-size="7">r</tspan>s/(s²+ω₀²)</text>
  <line class="ee-stroke" x1="78" y1="50" x2="94" y2="50" marker-end="url(#arrow)"/>
{pin(6, 50)}
{pin(94, 50)}
""", tags=["pr controller", "resonant", "harmonic", "grid inverter", "control"])

    # 4. Integrator Block (1/s)
    save_symbol(cat_ctrl, "control_integrator", "Integrator Block (1/s)", f"""
  <line class="ee-stroke" x1="8" y1="50" x2="24" y2="50" marker-end="url(#arrow)"/>
  <rect class="ee-body" x="26" y="26" width="48" height="48" rx="4"/>
  <text class="ee-text" x="50" y="50" font-size="16">∫ dt</text>
  <line class="ee-stroke" x1="74" y1="50" x2="92" y2="50" marker-end="url(#arrow)"/>
{pin(8, 50)}
{pin(92, 50)}
""", tags=["integrator", "1/s", "integral", "control"])

    # 5. Clarke Transform Block (abc -> αβ)
    save_symbol(cat_ctrl, "transform_clarke_abc_ab", "Clarke Transform (abc → αβ)", f"""
  <line class="ee-wire-a" x1="6" y1="34" x2="22" y2="34"/>
  <line class="ee-wire-b" x1="6" y1="50" x2="22" y2="50"/>
  <line class="ee-wire-c" x1="6" y1="66" x2="22" y2="66"/>
  <rect class="ee-body" x="22" y="22" width="56" height="56" rx="4"/>
  <line class="ee-thin" x1="22" y1="78" x2="78" y2="22"/>
  <text class="ee-text" x="38" y="38" font-size="12">abc</text>
  <text class="ee-text" x="62" y="64" font-size="12">αβ</text>
  <line class="ee-stroke" x1="78" y1="40" x2="94" y2="40"/>
  <line class="ee-stroke" x1="78" y1="60" x2="94" y2="60"/>
{pin(6, 34)}
{pin(6, 50)}
{pin(6, 66)}
{pin(94, 40)}
{pin(94, 60)}
""", tags=["clarke", "abc to alpha beta", "coordinate transform", "foc", "vector control"])

    # 6. Park Transform Block (αβ -> dq)
    save_symbol(cat_ctrl, "transform_park_ab_dq", "Park Transform (αβ → dq)", f"""
  <line class="ee-stroke" x1="6" y1="40" x2="22" y2="40"/>
  <line class="ee-stroke" x1="6" y1="60" x2="22" y2="60"/>
  <rect class="ee-tint-blue" x="22" y="22" width="56" height="56" rx="4"/>
  <line class="ee-thin" x1="22" y1="78" x2="78" y2="22"/>
  <text class="ee-text" x="38" y="38" font-size="12">αβ</text>
  <text class="ee-text" x="62" y="64" font-size="12">dq</text>
  <line class="ee-stroke" x1="78" y1="40" x2="94" y2="40"/>
  <line class="ee-stroke" x1="78" y1="60" x2="94" y2="60"/>
  <!-- Angle theta input -->
  <line class="ee-stroke" x1="50" y1="94" x2="50" y2="80" marker-end="url(#arrow)"/>
  <text class="ee-text" x="60" y="90" font-size="11">θ</text>
{pin(6, 40)}
{pin(6, 60)}
{pin(94, 40)}
{pin(94, 60)}
{pin(50, 94)}
""", tags=["park", "alpha beta to dq", "dq transform", "foc", "synchronous frame"])

    # 7. Inverse Park Transform Block (dq -> αβ)
    save_symbol(cat_ctrl, "transform_inv_park_dq_ab", "Inverse Park Transform (dq → αβ)", f"""
  <line class="ee-stroke" x1="6" y1="40" x2="22" y2="40"/>
  <line class="ee-stroke" x1="6" y1="60" x2="22" y2="60"/>
  <rect class="ee-tint-blue" x="22" y="22" width="56" height="56" rx="4"/>
  <line class="ee-thin" x1="22" y1="78" x2="78" y2="22"/>
  <text class="ee-text" x="38" y="38" font-size="12">dq</text>
  <text class="ee-text" x="62" y="64" font-size="12">αβ</text>
  <line class="ee-stroke" x1="78" y1="40" x2="94" y2="40"/>
  <line class="ee-stroke" x1="78" y1="60" x2="94" y2="60"/>
  <line class="ee-stroke" x1="50" y1="94" x2="50" y2="80" marker-end="url(#arrow)"/>
  <text class="ee-text" x="60" y="90" font-size="11">θ</text>
{pin(6, 40)}
{pin(6, 60)}
{pin(94, 40)}
{pin(94, 60)}
{pin(50, 94)}
""", tags=["inverse park", "dq to alpha beta", "coordinate transform", "foc"])

    # 8. Direct Park Transform (abc -> dq)
    save_symbol(cat_ctrl, "transform_abc_to_dq", "Direct Park Transform (abc → dq)", f"""
  <line class="ee-wire-a" x1="6" y1="34" x2="22" y2="34"/>
  <line class="ee-wire-b" x1="6" y1="50" x2="22" y2="50"/>
  <line class="ee-wire-c" x1="6" y1="66" x2="22" y2="66"/>
  <rect class="ee-tint-blue" x="22" y="22" width="56" height="56" rx="4"/>
  <line class="ee-thin" x1="22" y1="78" x2="78" y2="22"/>
  <text class="ee-text" x="38" y="38" font-size="12">abc</text>
  <text class="ee-text" x="62" y="64" font-size="12">dq</text>
  <line class="ee-stroke" x1="78" y1="40" x2="94" y2="40"/>
  <line class="ee-stroke" x1="78" y1="60" x2="94" y2="60"/>
  <line class="ee-stroke" x1="50" y1="94" x2="50" y2="80" marker-end="url(#arrow)"/>
  <text class="ee-text" x="60" y="90" font-size="11">θ</text>
{pin(6, 34)}
{pin(6, 50)}
{pin(6, 66)}
{pin(94, 40)}
{pin(94, 60)}
{pin(50, 94)}
""", tags=["abc to dq", "park transform", "foc", "pll", "vector control"])

    # 9. Space Vector PWM (SVPWM) Modulator Block
    save_symbol(cat_ctrl, "control_svpwm_block", "SVPWM Modulator Block", f"""
  <line class="ee-stroke" x1="6" y1="40" x2="20" y2="40"/>
  <line class="ee-stroke" x1="6" y1="60" x2="20" y2="60"/>
  <rect class="ee-tint-amber" x="20" y="20" width="60" height="60" rx="4"/>
  <text class="ee-label" x="50" y="34">SVPWM</text>
  <!-- Hexagon icon -->
  <polygon class="ee-thin" points="50,42 62,48 62,62 50,68 38,62 38,48"/>
  <line class="ee-thin" x1="50" y1="55" x2="59" y2="49" marker-end="url(#arrow-red)"/>
  <line class="ee-stroke" x1="80" y1="34" x2="94" y2="34"/>
  <line class="ee-stroke" x1="80" y1="50" x2="94" y2="50"/>
  <line class="ee-stroke" x1="80" y1="66" x2="94" y2="66"/>
{pin(6, 40)}
{pin(6, 60)}
{pin(94, 34)}
{pin(94, 50)}
{pin(94, 66)}
""", tags=["svpwm", "space vector", "pwm", "modulator", "inverter control"])

    # 10. Phase-Locked Loop (PLL / SRF-PLL) Block
    save_symbol(cat_ctrl, "control_pll_block", "Phase-Locked Loop (SRF-PLL)", f"""
  <line class="ee-wire-a" x1="6" y1="34" x2="22" y2="34"/>
  <line class="ee-wire-b" x1="6" y1="50" x2="22" y2="50"/>
  <line class="ee-wire-c" x1="6" y1="66" x2="22" y2="66"/>
  <rect class="ee-tint-green" x="22" y="24" width="56" height="52" rx="4"/>
  <text class="ee-label" x="50" y="42">SRF-PLL</text>
  <path class="ee-thin" d="M 34 62 L 66 50 L 66 62 Z"/>
  <line class="ee-stroke" x1="78" y1="42" x2="94" y2="42" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="78" y1="58" x2="94" y2="58" marker-end="url(#arrow)"/>
  <text class="ee-text" x="86" y="32" font-size="10">θ<tspan dy="2" font-size="7">g</tspan></text>
  <text class="ee-text" x="86" y="70" font-size="10">ω<tspan dy="2" font-size="7">g</tspan></text>
{pin(6, 34)}
{pin(6, 50)}
{pin(6, 66)}
{pin(94, 42)}
{pin(94, 58)}
""", tags=["pll", "phase locked loop", "srf-pll", "grid synchronization", "theta"])

    # 11. Saturation / Limiter Block
    save_symbol(cat_ctrl, "control_limiter_saturation", "Saturation / Limiter Block", f"""
  <line class="ee-stroke" x1="8" y1="50" x2="24" y2="50" marker-end="url(#arrow)"/>
  <rect class="ee-body" x="26" y="26" width="48" height="48" rx="4"/>
  <line class="ee-grid" x1="32" y1="50" x2="68" y2="50"/>
  <line class="ee-grid" x1="50" y1="32" x2="50" y2="68"/>
  <path class="ee-stroke" d="M 32 64 L 42 64 L 58 36 L 68 36"/>
  <line class="ee-stroke" x1="74" y1="50" x2="92" y2="50" marker-end="url(#arrow)"/>
{pin(8, 50)}
{pin(92, 50)}
""", tags=["saturation", "limiter", "anti-windup", "nonlinear", "control"])

    # 12. Hysteresis Comparator Block
    save_symbol(cat_ctrl, "control_hysteresis", "Hysteresis Comparator Block", f"""
  <line class="ee-stroke" x1="8" y1="50" x2="24" y2="50" marker-end="url(#arrow)"/>
  <rect class="ee-body" x="26" y="26" width="48" height="48" rx="4"/>
  <path class="ee-stroke" d="M 32 62 L 56 62 L 56 38 L 68 38 M 44 62 L 44 38 L 56 38"/>
  <line class="ee-stroke" x1="74" y1="50" x2="92" y2="50" marker-end="url(#arrow)"/>
{pin(8, 50)}
{pin(92, 50)}
""", tags=["hysteresis", "relay", "bang-bang", "dtc", "current control"])

    # ==========================================
    # CATEGORY 07: SENSORS, ANALOG, SWITCHGEAR & PROTECTION
    # ==========================================
    cat_sp = "07_sensors_protection"

    # 13. Operational Amplifier (Op-Amp)
    save_symbol(cat_sp, "opamp", "Operational Amplifier (Op-Amp)", f"""
  <line class="ee-stroke" x1="10" y1="36" x2="28" y2="36"/>
  <line class="ee-stroke" x1="10" y1="64" x2="28" y2="64"/>
  <polygon class="ee-body" points="28,20 28,80 76,50"/>
  <line class="ee-stroke" x1="76" y1="50" x2="92" y2="50"/>
  <text class="ee-label" x="36" y="36">−</text>
  <text class="ee-label" x="36" y="64">+</text>
{pin(10, 36)}
{pin(10, 64)}
{pin(92, 50)}
""", tags=["opamp", "operational amplifier", "analog", "amplifier", "comparator"])

    # 14. Hall-Effect Current Sensor (Closed-Loop LEM Style)
    save_symbol(cat_sp, "sensor_hall_current", "Hall-Effect Current Sensor (LEM)", f"""
  <!-- Primary power conductor -->
  <line class="ee-thick" x1="10" y1="50" x2="90" y2="50"/>
  <!-- Toroidal core around conductor -->
  <ellipse class="ee-tint-blue" cx="50" cy="50" rx="12" ry="22"/>
  <line class="ee-thick" x1="46" y1="50" x2="90" y2="50"/>
  <!-- Secondary measurement output -->
  <line class="ee-thin" x1="50" y1="72" x2="50" y2="90" marker-end="url(#arrow)"/>
  <text class="ee-text" x="66" y="84">i<tspan dy="3" font-size="8">m</tspan></text>
{pin(10, 50)}
{pin(90, 50)}
{pin(50, 90)}
""", tags=["current sensor", "hall effect", "lem", "measurement", "probe"])

    # 15. Voltmeter (Circle V)
    save_symbol(cat_sp, "meter_voltmeter", "Voltmeter (V)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="28"/>
  <circle class="ee-body" cx="50" cy="50" r="22"/>
  <text class="ee-text" x="50" y="50" font-size="16">V</text>
  <line class="ee-stroke" x1="50" y1="72" x2="50" y2="90"/>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["voltmeter", "voltage sensor", "measurement", "V"])

    # 16. Ammeter (Circle A)
    save_symbol(cat_sp, "meter_ammeter", "Ammeter (A)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="28" y2="50"/>
  <circle class="ee-body" cx="50" cy="50" r="22"/>
  <text class="ee-text" x="50" y="50" font-size="16">A</text>
  <line class="ee-stroke" x1="72" y1="50" x2="90" y2="50"/>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["ammeter", "current sensor", "measurement", "A"])

    # 17. Circuit Breaker (CB - IEC/IEEE with Cross)
    save_symbol(cat_sp, "breaker_cb", "Circuit Breaker (CB)", f"""
  <line class="ee-stroke" x1="10" y1="55" x2="34" y2="55"/>
  <line class="ee-stroke" x1="66" y1="55" x2="90" y2="55"/>
  <line class="ee-stroke" x1="34" y1="55" x2="64" y2="33"/>
  <!-- Cross at contact point (66,55) -->
  <line class="ee-stroke" x1="62" y1="51" x2="70" y2="59"/>
  <line class="ee-stroke" x1="62" y1="59" x2="70" y2="51"/>
  <text class="ee-text" x="50" y="22">CB</text>
{pin(10, 55)}
{pin(90, 55)}
""", tags=["circuit breaker", "cb", "switchgear", "protection", "relay"])

    # 18. Fuse (IEC Standard)
    save_symbol(cat_sp, "fuse_iec", "Fuse (IEC)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="90" y2="50"/>
  <rect class="ee-stroke" x="30" y="40" width="40" height="20"/>
  <text class="ee-text" x="50" y="26">F</text>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["fuse", "overcurrent", "protection", "iec"])

    # 19. Contactor / Relay Switch (NO + Coil)
    save_symbol(cat_sp, "contactor_relay", "Electromagnetic Contactor / Relay", f"""
  <!-- NO Contact -->
  <line class="ee-stroke" x1="12" y1="30" x2="36" y2="30"/>
  <line class="ee-stroke" x1="64" y1="30" x2="88" y2="30"/>
  <line class="ee-stroke" x1="36" y1="30" x2="62" y2="16"/>
  <circle class="ee-pin" cx="36" cy="30" r="2"/>
  <circle class="ee-pin" cx="64" cy="30" r="2"/>
  <!-- Mechanical link -->
  <line class="ee-dashed" x1="50" y1="24" x2="50" y2="58"/>
  <!-- Relay Coil -->
  <rect class="ee-body" x="34" y="58" width="32" height="20"/>
  <line class="ee-thin" x1="34" y1="78" x2="66" y2="58"/>
  <line class="ee-stroke" x1="12" y1="68" x2="34" y2="68"/>
  <line class="ee-stroke" x1="66" y1="68" x2="88" y2="68"/>
  <text class="ee-text" x="50" y="90">K</text>
{pin(12, 30)}
{pin(88, 30)}
{pin(12, 68)}
{pin(88, 68)}
""", tags=["contactor", "relay", "switch", "coil", "precharge"])

    # 20. Three-Phase Busbar with Slash (Single-Line Diagram 3-Wire Notation)
    save_symbol(cat_sp, "sld_3wire_bus", "Single-Line Diagram 3-Phase Busbar & Slash", f"""
  <line class="ee-thick" x1="20" y1="15" x2="20" y2="85"/>
  <line class="ee-stroke" x1="20" y1="50" x2="88" y2="50"/>
  <line class="ee-thin" x1="48" y1="58" x2="58" y2="42"/>
  <text class="ee-label" x="53" y="34">3</text>
  <text class="ee-text" x="20" y="94" font-size="11">Bus</text>
{node(20, 50)}
{pin(88, 50)}
""", tags=["busbar", "single line diagram", "sld", "3-wire", "power system"])
