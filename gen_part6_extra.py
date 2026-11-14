# -*- coding: utf-8 -*-
"""
Part 6: Additional Topologies, Windings, Machines, Control & Scope Templates
"""

def register_part6(save_symbol, pin, node):
    # More Winding & Magnetic Symbols
    cat_tx = "04_transformers_windings"

    # Planar PCB Transformer / Coupled Inductor
    save_symbol(cat_tx, "transformer_planar_pcb", "Planar Transformer (Spiral PCB Winding)", f"""
  <!-- Outer ferrite E-core frame -->
  <rect class="ee-body" x="14" y="14" width="72" height="72" rx="4"/>
  <rect class="ee-tint-amber" x="22" y="22" width="56" height="56" rx="2"/>
  <!-- Spiral PCB copper trace -->
  <path class="ee-wire-a" d="M 50 50 L 56 50 L 56 42 L 42 42 L 42 58 L 64 58 L 64 34 L 34 34 L 34 66 L 72 66"/>
  <circle class="ee-node" cx="50" cy="50" r="2.5"/>
  <line class="ee-stroke" x1="72" y1="66" x2="94" y2="66"/>
  <line class="ee-stroke" x1="50" y1="50" x2="94" y2="34"/>
{pin(94, 34)}
{pin(94, 66)}
""", tags=["planar transformer", "pcb winding", "spiral", "high frequency", "magnetic"])

    # Distributed vs Concentrated Stator Winding Phasor Star of Slots (12s/10p FSCW verified with jmag_bridge.winding: kw1 = 0.93301)
    save_symbol(cat_tx, "winding_star_of_slots", "Star of Slots (12s/10p FSCW EMF Phasor Star, kw1=0.933)", f"""
  <circle class="ee-dashed" cx="50" cy="50" r="36"/>
  <!-- 12 Slot Phasors (30 deg spacing): U(Red), V(Green), W(Blue) -->
  <line class="ee-wire-a" x1="50" y1="50" x2="50" y2="14" marker-end="url(#arrow-red)"/>
  <line class="ee-wire-a" x1="50" y1="50" x2="68" y2="19" marker-end="url(#arrow-red)"/>
  <line class="ee-wire-b" x1="50" y1="50" x2="81" y2="32" marker-end="url(#arrow)"/>
  <line class="ee-wire-b" x1="50" y1="50" x2="86" y2="50" marker-end="url(#arrow)"/>
  <line class="ee-wire-c" x1="50" y1="50" x2="81" y2="68" marker-end="url(#arrow-blue)"/>
  <line class="ee-wire-c" x1="50" y1="50" x2="68" y2="81" marker-end="url(#arrow-blue)"/>
  <line class="ee-wire-a" x1="50" y1="50" x2="50" y2="86"/>
  <line class="ee-wire-a" x1="50" y1="50" x2="32" y2="81"/>
  <line class="ee-wire-b" x1="50" y1="50" x2="19" y2="68"/>
  <line class="ee-wire-b" x1="50" y1="50" x2="14" y2="50"/>
  <line class="ee-wire-c" x1="50" y1="50" x2="19" y2="32"/>
  <line class="ee-wire-c" x1="50" y1="50" x2="32" y2="19"/>
  <circle class="ee-node" cx="50" cy="50" r="3"/>
  <text class="ee-label" x="50" y="95">kw1 = 0.933</text>
""", tags=["star of slots", "winding factor", "fractional slot", "fscw", "emf phasor", "winding", "12s10p"])

    # Five-Phase Star Winding (Pentaphase Motor Winding)
    save_symbol(cat_tx, "winding_5ph_star", "5-Phase Star Winding (Pentaphase 72° Shift)", f"""
  <!-- 5 axes separated by 72 deg around (50,52) -->
  <line class="ee-wire-a" x1="50" y1="52" x2="50" y2="12"/>
  <line class="ee-wire-b" x1="50" y1="52" x2="88" y2="40"/>
  <line class="ee-wire-c" x1="50" y1="52" x2="74" y2="84"/>
  <line class="ee-stroke" x1="50" y1="52" x2="26" y2="84"/>
  <line class="ee-stroke" x1="50" y1="52" x2="12" y2="40"/>
  <circle class="ee-body" cx="50" cy="52" r="9"/>
  <text class="ee-label" x="50" y="52">5φ</text>
  <text class="ee-label" x="60" y="14">A</text>
  <text class="ee-label" x="90" y="30">B</text>
  <text class="ee-label" x="84" y="86">C</text>
  <text class="ee-label" x="16" y="86">D</text>
  <text class="ee-label" x="10" y="30">E</text>
{pin(50, 12)}
{pin(88, 40)}
{pin(74, 84)}
{pin(26, 84)}
{pin(12, 40)}
""", tags=["5-phase", "five phase", "pentaphase", "multiphase", "fault tolerant", "winding"])

    # Concentrated Tooth-Coil Winding vs Distributed Winding Diagram (12s/10p FSCW double-layer slot polarity verified via jmag_bridge.winding)
    save_symbol(cat_tx, "winding_concentrated_tooth", "Concentrated Tooth-Coil Winding (FSCW Double-Layer)", f"""
  <!-- 3 Stator Teeth -->
  <path class="ee-body" d="M 10 20 L 90 20 L 90 34 L 78 34 L 78 72 L 64 72 L 64 34 L 57 34 L 57 72 L 43 72 L 43 34 L 36 34 L 36 72 L 22 72 L 22 34 L 10 34 Z"/>
  <!-- Tooth 1 Coil: Phase U (Red, +left / -right) -->
  <rect class="ee-tint-red" x="15" y="40" width="7" height="28"/>
  <rect class="ee-tint-red" x="36" y="40" width="4" height="28"/>
  <path class="ee-wire-a" d="M 18 40 Q 29 27 38 40"/>
  <text class="ee-label" x="18" y="54">U+</text>
  <!-- Tooth 2 Coil: Phase V (Green, -left / +right) -->
  <rect class="ee-tint-green" x="40" y="40" width="3" height="28"/>
  <rect class="ee-tint-green" x="57" y="40" width="4" height="28"/>
  <path class="ee-wire-b" d="M 41 40 Q 50 27 59 40"/>
  <!-- Tooth 3 Coil: Phase W (Blue, +left / -right) -->
  <rect class="ee-tint-blue" x="61" y="40" width="3" height="28"/>
  <rect class="ee-tint-blue" x="78" y="40" width="7" height="28"/>
  <path class="ee-wire-c" d="M 62 40 Q 71 27 81 40"/>
  <text class="ee-label" x="81" y="54">W-</text>
  <text class="ee-label" x="50" y="86">FSCW (q=0.4, y=1)</text>
""", tags=["fscw", "tooth coil", "concentrated winding", "stator", "winding", "double layer"])

    # More Machines
    cat_m = "05_electrical_machines"

    # Axial Flux Permanent Magnet (AFPM / Yokeless Dual-Rotor) Machine
    save_symbol(cat_m, "machine_axial_flux_afpm", "Axial-Flux PM Machine (AFPM Dual-Rotor Yokeless)", f"""
  <!-- Shaft horizontal -->
  <line class="ee-thick" x1="8" y1="50" x2="92" y2="50"/>
  <!-- Left Rotor Disc with PMs -->
  <rect class="ee-body" x="22" y="16" width="10" height="68"/>
  <rect class="ee-tint-red" x="32" y="18" width="6" height="24"/>
  <rect class="ee-tint-blue" x="32" y="58" width="6" height="24"/>
  <!-- Center StatorSegmented Yokeless Core -->
  <rect class="ee-tint-amber" x="44" y="18" width="12" height="26"/>
  <rect class="ee-tint-amber" x="44" y="56" width="12" height="26"/>
  <!-- Right Rotor Disc with PMs -->
  <rect class="ee-tint-blue" x="62" y="18" width="6" height="24"/>
  <rect class="ee-tint-red" x="62" y="58" width="6" height="24"/>
  <rect class="ee-body" x="68" y="16" width="10" height="68"/>
  <text class="ee-label" x="50" y="93">AFPM</text>
""", tags=["axial flux", "afpm", "yasa", "disc motor", "dual rotor", "pmsm"])

    # Linear Synchronous Motor (LSM / Linear Actuator)
    save_symbol(cat_m, "machine_linear_motor_lsm", "Linear Permanent Magnet Synchronous Motor (LPMSM)", f"""
  <!-- Primary Mover with 3-phase coils -->
  <rect class="ee-body" x="16" y="18" width="68" height="30" rx="2"/>
  <rect class="ee-tint-red" x="22" y="34" width="14" height="14"/>
  <rect class="ee-tint-green" x="43" y="34" width="14" height="14"/>
  <rect class="ee-tint-blue" x="64" y="34" width="14" height="14"/>
  <!-- Secondary Track with alternating N/S magnets -->
  <rect class="ee-body" x="8" y="64" width="84" height="14"/>
  <rect class="ee-tint-red" x="12" y="56" width="16" height="8"/>
  <rect class="ee-tint-blue" x="32" y="56" width="16" height="8"/>
  <rect class="ee-tint-red" x="52" y="56" width="16" height="8"/>
  <rect class="ee-tint-blue" x="72" y="56" width="16" height="8"/>
  <line class="ee-thin" x1="35" y1="10" x2="65" y2="10" marker-end="url(#arrow)"/>
  <text class="ee-text" x="50" y="88" font-size="11">v<tspan dy="2" font-size="8">x</tspan></text>
""", tags=["linear motor", "lpmsm", "lsm", "maglev", "actuator", "machine"])

    # More Power Electronics Topologies
    cat_pe = "08_power_topologies"

    # 13. Flying Capacitor (3-Level FC) Multilevel Phase Leg
    save_symbol(cat_pe, "topology_3level_flying_cap", "3-Level Flying Capacitor (3L-FC) Phase Leg", f"""
  <line class="ee-stroke" x1="40" y1="15" x2="130" y2="15"/>
  <line class="ee-stroke" x1="40" y1="185" x2="130" y2="185"/>
  <!-- 4 Series Switches at x=130 -->
  <line class="ee-stroke" x1="130" y1="15" x2="130" y2="185"/>
  <rect class="ee-tint-blue" x="120" y="26" width="20" height="22" rx="2"/><text class="ee-label" x="130" y="37">S1</text>
  <rect class="ee-tint-blue" x="120" y="66" width="20" height="22" rx="2"/><text class="ee-label" x="130" y="77">S2</text>
  <rect class="ee-tint-blue" x="120" y="112" width="20" height="22" rx="2"/><text class="ee-label" x="130" y="123">S3</text>
  <rect class="ee-tint-blue" x="120" y="152" width="20" height="22" rx="2"/><text class="ee-label" x="130" y="163">S4</text>
  <!-- Clamping Flying Capacitor Cfc between nodes (130,56) and (130,144) -->
  <path class="ee-stroke" d="M 130 56 L 75 56 L 75 95"/>
  <line class="ee-stroke" x1="63" y1="95" x2="87" y2="95"/>
  <line class="ee-stroke" x1="63" y1="105" x2="87" y2="105"/>
  <path class="ee-stroke" d="M 75 105 L 75 144 L 130 144"/>
  <text class="ee-text" x="45" y="100">C<tspan dy="3" font-size="8">fc</tspan></text>
  <!-- AC Output -->
  <line class="ee-wire-a" x1="130" y1="100" x2="185" y2="100"/>
{node(130, 56)}
{node(130, 100)}
{node(130, 144)}
{pin(185, 100)}
""", width=200, height=200, tags=["flying capacitor", "3-level", "multilevel", "fc", "inverter leg", "topology"])

    # 14. Z-Source / Quasi-Z-Source Impedance Network
    save_symbol(cat_pe, "topology_z_source_network", "Z-Source Impedance Network (L1, L2, C1, C2)", f"""
  <!-- Top and bottom rails -->
  <path class="ee-stroke" d="M 15 35 L 45 35 A 6 7 0 0 1 57 35 A 6 7 0 0 1 69 35 A 6 7 0 0 1 81 35 L 185 35"/>
  <path class="ee-stroke" d="M 15 125 L 45 125 A 6 7 0 0 0 57 125 A 6 7 0 0 0 69 125 A 6 7 0 0 0 81 125 L 185 125"/>
  <!-- Cross X capacitors C1, C2 -->
  <line class="ee-stroke" x1="35" y1="35" x2="92" y2="75"/>
  <line class="ee-stroke" x1="86" y1="81" x2="98" y2="69"/>
  <line class="ee-stroke" x1="92" y1="87" x2="104" y2="75"/>
  <line class="ee-stroke" x1="98" y1="81" x2="155" y2="125"/>
  <line class="ee-stroke" x1="35" y1="125" x2="92" y2="85"/>
  <line class="ee-stroke" x1="98" y1="79" x2="155" y2="35"/>
  <text class="ee-text" x="63" y="18">L<tspan dy="3" font-size="8">1</tspan></text>
  <text class="ee-text" x="63" y="145">L<tspan dy="3" font-size="8">2</tspan></text>
  <text class="ee-text" x="135" y="55">C<tspan dy="3" font-size="8">1</tspan></text>
  <text class="ee-text" x="135" y="108">C<tspan dy="3" font-size="8">2</tspan></text>
{node(35, 35)}
{node(155, 35)}
{node(35, 125)}
{node(155, 125)}
{pin(15, 35)}
{pin(15, 125)}
{pin(185, 35)}
{pin(185, 125)}
""", width=200, height=160, tags=["z-source", "qzsi", "impedance source", "shoot through", "inverter", "topology"])

    # 15. Complete Field-Oriented Control (FOC) Block Diagram for PMSM Drive
    save_symbol(cat_pe, "diagram_foc_complete_loop", "Complete PMSM Field-Oriented Control (FOC) Architecture", f"""
  <rect class="ee-body" x="8" y="8" width="444" height="224" rx="6"/>
  <!-- Speed Error & PI -->
  <circle class="ee-body" cx="42" cy="55" r="10"/><text class="ee-label" x="42" y="55">Σ</text>
  <line class="ee-stroke" x1="16" y1="55" x2="32" y2="55"/><text class="ee-text" x="22" y="42" font-size="10">ω*</text>
  <line class="ee-stroke" x1="52" y1="55" x2="72" y2="55"/>
  <rect class="ee-tint-blue" x="72" y="42" width="38" height="26" rx="3"/><text class="ee-label" x="91" y="55">PI<tspan dy="2" font-size="7">ω</tspan></text>
  <!-- q-axis Current Error & PI -->
  <line class="ee-stroke" x1="110" y1="55" x2="135" y2="55"/><text class="ee-text" x="122" y="44" font-size="10">i<tspan dy="2" font-size="7">q</tspan>*</text>
  <circle class="ee-body" cx="145" cy="55" r="10"/><text class="ee-label" x="145" y="55">Σ</text>
  <line class="ee-stroke" x1="155" y1="55" x2="175" y2="55"/>
  <rect class="ee-tint-blue" x="175" y="42" width="38" height="26" rx="3"/><text class="ee-label" x="194" y="55">PI<tspan dy="2" font-size="7">q</tspan></text>
  <!-- d-axis Current Error (id* = 0) & PI -->
  <line class="ee-stroke" x1="110" y1="105" x2="135" y2="105"/><text class="ee-text" x="118" y="94" font-size="10">i<tspan dy="2" font-size="7">d</tspan>*=0</text>
  <circle class="ee-body" cx="145" cy="105" r="10"/><text class="ee-label" x="145" y="105">Σ</text>
  <line class="ee-stroke" x1="155" y1="105" x2="175" y2="105"/>
  <rect class="ee-tint-blue" x="175" y="92" width="38" height="26" rx="3"/><text class="ee-label" x="194" y="105">PI<tspan dy="2" font-size="7">d</tspan></text>
  <!-- Inverse Park dq -> alpha/beta -->
  <line class="ee-stroke" x1="213" y1="55" x2="235" y2="55"/>
  <line class="ee-stroke" x1="213" y1="105" x2="235" y2="105"/>
  <rect class="ee-body" x="235" y="42" width="44" height="76" rx="3"/>
  <text class="ee-label" x="257" y="66">dq</text>
  <text class="ee-label" x="257" y="94">αβ</text>
  <line class="ee-thin" x1="235" y1="118" x2="279" y2="42"/>
  <!-- SVPWM + VSI -->
  <line class="ee-stroke" x1="279" y1="65" x2="298" y2="65"/>
  <line class="ee-stroke" x1="279" y1="95" x2="298" y2="95"/>
  <rect class="ee-tint-amber" x="298" y="42" width="54" height="76" rx="3"/>
  <text class="ee-label" x="325" y="72">SVPWM</text>
  <text class="ee-label" x="325" y="90">+ VSI</text>
  <!-- 3-Phase Wires to PMSM -->
  <line class="ee-wire-a" x1="352" y1="60" x2="392" y2="60"/>
  <line class="ee-wire-b" x1="352" y1="80" x2="388" y2="80"/>
  <line class="ee-wire-c" x1="352" y1="100" x2="392" y2="100"/>
  <circle class="ee-body" cx="414" cy="80" r="24"/>
  <text class="ee-text" x="414" y="76" font-size="11">PMSM</text>
  <text class="ee-label" x="414" y="90">3~</text>
  <!-- Feedback Park Transform abc -> dq -->
  <rect class="ee-body" x="235" y="145" width="54" height="52" rx="3"/>
  <text class="ee-label" x="262" y="162">abc → dq</text>
  <text class="ee-label" x="262" y="180">(Park)</text>
  <path class="ee-thin" d="M 372 60 L 372 158 L 289 158"/>
  <path class="ee-thin" d="M 380 100 L 380 182 L 289 182"/>
  <path class="ee-thin" d="M 235 158 L 145 158 L 145 65" marker-end="url(#arrow)"/>
  <path class="ee-thin" d="M 235 182 L 160 182 L 160 128 L 145 128 L 145 115" marker-end="url(#arrow)"/>
  <!-- Rotor Speed/Position Feedback -->
  <path class="ee-dashed" d="M 414 104 L 414 212 L 42 212 L 42 65" marker-end="url(#arrow)"/>
  <text class="ee-text" x="340" y="204" font-size="10">θ<tspan dy="2" font-size="7">e</tspan>, ω<tspan dy="2" font-size="7">r</tspan></text>
""", width=460, height=240, tags=["foc", "field oriented control", "vector control", "pmsm drive", "block diagram", "complete system"])
