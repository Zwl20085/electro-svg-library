# -*- coding: utf-8 -*-
"""
Part 7: Measurement & Laboratory Test Instruments (Bench Equipment, Meters, Probes, HIL/RCP)
"""

def register_part7(save_symbol, pin, node):
    cat_inst = "10_measurement_instruments"

    # 1. Wattmeter (4-Terminal Electrodynamic / Power Meter with Current & Voltage Coils)
    save_symbol(cat_inst, "meter_wattmeter", "Wattmeter (Active Power Meter W)", f"""
  <!-- Current Coil (Horizontal series path) -->
  <line class="ee-stroke" x1="6" y1="36" x2="94" y2="36"/>
  <!-- Voltage Coil (Vertical shunt path) -->
  <line class="ee-thin" x1="26" y1="36" x2="26" y2="54"/>
  <path class="ee-thin" d="M 26 54 L 50 54 L 50 92"/>
  <circle class="ee-body" cx="50" cy="50" r="24"/>
  <!-- Internal coils & W label -->
  <path class="ee-stroke" d="M 32 36 L 68 36"/>
  <text class="ee-text" x="50" y="54" font-size="16">W</text>
  <circle class="ee-node" cx="35" cy="31" r="2"/>
  <circle class="ee-node" cx="42" cy="64" r="2"/>
{node(26, 36)}
{pin(6, 36)}
{pin(94, 36)}
{pin(50, 92)}
""", tags=["wattmeter", "power meter", "active power", "W", "instrument", "meter"])

    # 2. VARmeter (Reactive Power Meter)
    save_symbol(cat_inst, "meter_varmeter", "VARmeter (Reactive Power Meter var)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="26" y2="50"/>
  <circle class="ee-body" cx="50" cy="50" r="24"/>
  <text class="ee-text" x="50" y="50" font-size="14">var</text>
  <line class="ee-stroke" x1="74" y1="50" x2="90" y2="50"/>
  <line class="ee-thin" x1="50" y1="74" x2="50" y2="92"/>
{pin(10, 50)}
{pin(90, 50)}
{pin(50, 92)}
""", tags=["varmeter", "reactive power", "var", "instrument", "meter"])

    # 3. Power Factor / Phase Angle Meter (cos φ)
    save_symbol(cat_inst, "meter_power_factor", "Power Factor / Phase Meter (cos φ)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="26" y2="50"/>
  <circle class="ee-body" cx="50" cy="50" r="24"/>
  <text class="ee-text" x="50" y="50" font-size="13">cos φ</text>
  <line class="ee-stroke" x1="74" y1="50" x2="90" y2="50"/>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["power factor", "cos phi", "phase meter", "instrument", "meter"])

    # 4. Frequency Meter (Hz)
    save_symbol(cat_inst, "meter_frequency_hz", "Frequency Meter (Hz)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="26"/>
  <circle class="ee-body" cx="50" cy="50" r="24"/>
  <text class="ee-text" x="50" y="50" font-size="15">Hz</text>
  <line class="ee-stroke" x1="50" y1="74" x2="50" y2="90"/>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["frequency meter", "hz", "grid frequency", "instrument", "meter"])

    # 5. Energy / Kilowatt-Hour Smart Meter (kWh)
    save_symbol(cat_inst, "meter_energy_kwh", "Energy / Smart Meter (kWh)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="24" y2="50"/>
  <rect class="ee-body" x="24" y="24" width="52" height="52" rx="4"/>
  <rect class="ee-tint-blue" x="30" y="30" width="40" height="18" rx="2"/>
  <text class="ee-label" x="50" y="39">kWh</text>
  <circle class="ee-thin" cx="50" cy="62" r="8"/>
  <line class="ee-thin" x1="44" y1="62" x2="56" y2="62" marker-end="url(#arrow)"/>
  <line class="ee-stroke" x1="76" y1="50" x2="90" y2="50"/>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["kwh", "energy meter", "smart meter", "instrument", "grid"])

    # 6. Galvanometer / Null Detector (G)
    save_symbol(cat_inst, "meter_galvanometer", "Galvanometer / Null Detector (G)", f"""
  <line class="ee-stroke" x1="50" y1="10" x2="50" y2="26"/>
  <circle class="ee-body" cx="50" cy="50" r="24"/>
  <line class="ee-stroke" x1="50" y1="64" x2="50" y2="34" marker-end="url(#arrow)"/>
  <text class="ee-text" x="38" y="52" font-size="12">G</text>
  <line class="ee-stroke" x1="50" y1="74" x2="50" y2="90"/>
{pin(50, 10)}
{pin(50, 90)}
""", tags=["galvanometer", "wheatstone bridge", "null detector", "instrument"])

    # 7. Ohmmeter / Insulation Resistance Tester (Ω)
    save_symbol(cat_inst, "meter_ohmmeter", "Ohmmeter / Megohmmeter (Ω)", f"""
  <line class="ee-stroke" x1="10" y1="50" x2="26" y2="50"/>
  <circle class="ee-body" cx="50" cy="50" r="24"/>
  <text class="ee-text" x="50" y="50" font-size="16">Ω</text>
  <line class="ee-stroke" x1="74" y1="50" x2="90" y2="50"/>
{pin(10, 50)}
{pin(90, 50)}
""", tags=["ohmmeter", "resistance", "megger", "omega", "instrument"])

    # 8. Analog Dial Pointer Gauge (Classic Panel Meter Icon)
    save_symbol(cat_inst, "instrument_analog_dial_gauge", "Analog Pointer Dial Gauge (Panel Meter)", f"""
  <rect class="ee-body" x="16" y="16" width="68" height="68" rx="6"/>
  <!-- Graduated Scale Arc -->
  <path class="ee-thin" d="M 26 58 A 28 28 0 0 1 74 58"/>
  <!-- Tick marks -->
  <line class="ee-thin" x1="26" y1="58" x2="30" y2="55"/>
  <line class="ee-thin" x1="36" y1="36" x2="39" y2="40"/>
  <line class="ee-thin" x1="50" y1="30" x2="50" y2="35"/>
  <line class="ee-thin" x1="64" y1="36" x2="61" y2="40"/>
  <line class="ee-thin" x1="74" y1="58" x2="70" y2="55"/>
  <!-- Needle pointer -->
  <line class="ee-wire-a" x1="50" y1="68" x2="62" y2="38" marker-end="url(#arrow-red)"/>
  <circle class="ee-node" cx="50" cy="68" r="3"/>
  <line class="ee-stroke" x1="36" y1="84" x2="36" y2="94"/>
  <line class="ee-stroke" x1="64" y1="84" x2="64" y2="94"/>
{pin(36, 94)}
{pin(64, 94)}
""", tags=["analog gauge", "dial", "pointer meter", "panel meter", "instrument"])

    # 9. Potential / Voltage Transformer (PT / VT for Instrument Metering)
    save_symbol(cat_inst, "instrument_potential_transformer_vt", "Potential / Voltage Transformer (PT / VT)", f"""
  <line class="ee-stroke" x1="10" y1="22" x2="90" y2="22"/>
  <line class="ee-thin" x1="38" y1="22" x2="38" y2="38"/>
  <circle class="ee-body" cx="50" cy="48" r="14"/>
  <circle class="ee-body" cx="50" cy="66" r="14"/>
  <circle class="ee-body" cx="50" cy="86" r="10"/>
  <text class="ee-text" x="50" y="86" font-size="11">V</text>
{node(38, 22)}
{pin(10, 22)}
{pin(90, 22)}
""", tags=["voltage transformer", "potential transformer", "pt", "vt", "instrument transformer"])

    # 10. Rogowski Coil / Clamp-On Current Probe
    save_symbol(cat_inst, "probe_current_clamp_rogowski", "Clamp-On Current Probe / Rogowski Coil", f"""
  <!-- Primary busbar conductor -->
  <line class="ee-thick" x1="10" y1="45" x2="90" y2="45"/>
  <!-- Rogowski / Split-core jaws around conductor -->
  <path class="ee-tint-red" d="M 38 45 C 38 22, 62 22, 62 45 C 62 68, 38 68, 38 45 Z" fill="none"/>
  <ellipse class="ee-wire-a" cx="50" cy="45" rx="11" ry="20"/>
  <!-- Probe handle & BNC coaxial lead -->
  <rect class="ee-body" x="45" y="65" width="10" height="14" rx="2"/>
  <line class="ee-thin" x1="50" y1="79" x2="50" y2="92" marker-end="url(#arrow)"/>
  <text class="ee-text" x="68" y="84" font-size="11">i<tspan dy="2" font-size="8">probe</tspan></text>
{pin(10, 45)}
{pin(90, 45)}
{pin(50, 92)}
""", tags=["current probe", "rogowski coil", "clamp meter", "pearson coil", "oscilloscope probe"])

    # 11. High-Voltage Differential Voltage Probe (HV Diff Probe)
    save_symbol(cat_inst, "probe_hv_differential", "High-Voltage Differential Probe (HV Diff Probe)", f"""
  <!-- + and - HV test leads with grabber hooks -->
  <path class="ee-wire-a" d="M 10 32 L 32 32"/>
  <path class="ee-wire-c" d="M 10 68 L 32 68"/>
  <rect class="ee-tint-amber" x="32" y="24" width="42" height="52" rx="4"/>
  <!-- Internal diff amp triangle -->
  <polygon class="ee-body" points="40,34 40,66 64,50"/>
  <text class="ee-label" x="45" y="42">+</text>
  <text class="ee-label" x="45" y="58">−</text>
  <text class="ee-label" x="53" y="16">÷100 / ÷1000</text>
  <!-- BNC Output to Scope -->
  <line class="ee-stroke" x1="74" y1="50" x2="92" y2="50" marker-end="url(#arrow)"/>
{pin(10, 32)}
{pin(10, 68)}
{pin(92, 50)}
""", tags=["differential probe", "hv probe", "voltage probe", "oscilloscope", "instrument"])

    # 12. Bench Digital Storage Oscilloscope (DSO Front-Panel Instrument Block)
    save_symbol(cat_inst, "instrument_bench_oscilloscope", "Digital Storage Oscilloscope (DSO Bench Instrument)", f"""
  <rect class="ee-body" x="10" y="14" width="140" height="86" rx="5"/>
  <!-- Screen bezel -->
  <rect x="18" y="22" width="84" height="56" rx="2" fill="#0f172a" stroke="#111827" stroke-width="1.5"/>
  <!-- Grid on screen -->
  <line x1="18" y1="50" x2="102" y2="50" stroke="#334155" stroke-width="0.8" stroke-dasharray="2 2"/>
  <line x1="60" y1="22" x2="60" y2="78" stroke="#334155" stroke-width="0.8" stroke-dasharray="2 2"/>
  <!-- CH1 Sine & CH2 PWM traces -->
  <path d="M 20 40 C 33 22, 46 22, 60 40 C 74 58, 87 58, 100 40" fill="none" stroke="#38bdf8" stroke-width="1.6"/>
  <path d="M 20 68 L 32 68 L 32 56 L 48 56 L 48 68 L 64 68 L 64 56 L 80 56 L 80 68 L 100 68" fill="none" stroke="#facc15" stroke-width="1.4"/>
  <!-- Control knobs on right panel -->
  <circle class="ee-body" cx="118" cy="32" r="6"/>
  <circle class="ee-body" cx="136" cy="32" r="6"/>
  <circle class="ee-body" cx="118" cy="52" r="5"/>
  <circle class="ee-body" cx="136" cy="52" r="5"/>
  <!-- 4 BNC Input Channels at bottom -->
  <circle class="ee-tint-blue" cx="30" cy="89" r="4"/>
  <circle class="ee-tint-red" cx="52" cy="89" r="4"/>
  <circle class="ee-tint-green" cx="74" cy="89" r="4"/>
  <circle class="ee-tint-amber" cx="96" cy="89" r="4"/>
  <text class="ee-label" x="127" y="88">DSO</text>
{pin(30, 100)}
{pin(52, 100)}
{pin(74, 100)}
{pin(96, 100)}
""", width=160, height=110, tags=["oscilloscope", "dso", "bench instrument", "scope", "measurement", "bnc"])

    # 13. Precision Power Analyzer (WT5000 /WT3000 3-Phase Efficiency & THD Analyzer)
    save_symbol(cat_inst, "instrument_power_analyzer", "Precision 3-Phase Power Analyzer (WT Series)", f"""
  <rect class="ee-body" x="10" y="12" width="160" height="96" rx="5"/>
  <!-- Multi-readout display -->
  <rect class="ee-tint-blue" x="18" y="20" width="106" height="58" rx="2"/>
  <text class="ee-label" x="45" y="32">Urms: 400.2V</text>
  <text class="ee-label" x="45" y="46">Irms:  28.45A</text>
  <text class="ee-label" x="45" y="60">P:    19.62kW</text>
  <text class="ee-label" x="98" y="32">η: 98.6%</text>
  <text class="ee-label" x="98" y="46">PF: 0.998</text>
  <text class="ee-label" x="98" y="60">THD: 1.4%</text>
  <!-- Function keys -->
  <rect class="ee-body" x="132" y="22" width="28" height="10" rx="1"/>
  <rect class="ee-body" x="132" y="38" width="28" height="10" rx="1"/>
  <rect class="ee-body" x="132" y="54" width="28" height="22" rx="2"/>
  <!-- 3-Phase Wattmeter Element Terminals -->
  <text class="ee-label" x="90" y="92">Power Analyzer (CH1 / CH2 / CH3 / CH4)</text>
{pin(35, 108)}
{pin(70, 108)}
{pin(105, 108)}
{pin(140, 108)}
""", width=180, height=120, tags=["power analyzer", "yokogawa", "wt5000", "efficiency", "thd", "instrument"])

    # 14. Bench Digital Multimeter (DMM 6.5-Digit)
    save_symbol(cat_inst, "instrument_digital_multimeter", "Bench Digital Multimeter (DMM)", f"""
  <rect class="ee-body" x="12" y="18" width="116" height="74" rx="5"/>
  <rect class="ee-tint-green" x="20" y="26" width="68" height="28" rx="2"/>
  <text class="ee-label" x="54" y="40" font-size="13">+800.04 Vdc</text>
  <text class="ee-label" x="48" y="72">DMM 6½ Digit</text>
  <!-- HI / LO / AI Banana Jacks -->
  <circle class="ee-tint-red" cx="102" cy="34" r="5"/>
  <circle class="ee-body" cx="102" cy="52" r="5"/>
  <circle class="ee-tint-amber" cx="102" cy="70" r="5"/>
  <text class="ee-label" x="116" y="34">HI</text>
  <text class="ee-label" x="116" y="52">LO</text>
  <text class="ee-label" x="116" y="70">I</text>
{pin(128, 34)}
{pin(128, 52)}
{pin(128, 70)}
""", width=140, height=105, tags=["dmm", "multimeter", "voltmeter", "bench instrument", "measurement"])

    # 15. Spectrum / Network / Impedance Analyzer (Bode / EMI Receiver)
    save_symbol(cat_inst, "instrument_spectrum_impedance_analyzer", "Spectrum / Impedance / Vector Network Analyzer (VNA)", f"""
  <rect class="ee-body" x="10" y="14" width="140" height="86" rx="5"/>
  <rect x="18" y="22" width="88" height="56" rx="2" fill="#f8fafc" stroke="#111827" stroke-width="1.5"/>
  <!-- Resonance impedance curve |Z(f)| -->
  <path class="ee-wire-a" d="M 22 32 L 45 48 L 58 70 L 72 28 L 88 45 L 102 56"/>
  <text class="ee-label" x="62" y="88">|Z(f)| / EMI Analyzer</text>
  <circle class="ee-body" cx="124" cy="36" r="8"/>
  <circle class="ee-pin" cx="118" cy="68" r="4"/>
  <circle class="ee-pin" cx="134" cy="68" r="4"/>
{pin(118, 100)}
{pin(134, 100)}
""", width=160, height=110, tags=["spectrum analyzer", "vna", "impedance analyzer", "emi receiver", "bode", "instrument"])

    # 16. Programmable Bidirectional DC Power Supply / Electronic Load
    save_symbol(cat_inst, "instrument_programmable_dc_supply_load", "Programmable Bidirectional DC Supply / Electronic Load", f"""
  <rect class="ee-body" x="10" y="20" width="140" height="70" rx="4"/>
  <rect class="ee-tint-amber" x="18" y="28" width="68" height="32" rx="2"/>
  <text class="ee-label" x="52" y="38">800.0V / 50.0A</text>
  <text class="ee-label" x="52" y="51">CV / CC Bidir</text>
  <text class="ee-label" x="62" y="76">Prog. DC Source / Load</text>
  <!-- + and - Output Bus Terminals -->
  <circle class="ee-tint-red" cx="112" cy="38" r="5"/>
  <circle class="ee-tint-blue" cx="112" cy="58" r="5"/>
  <line class="ee-wire-a" x1="117" y1="38" x2="150" y2="38"/>
  <line class="ee-wire-c" x1="117" y1="58" x2="150" y2="58"/>
  <text class="ee-label" x="100" y="38">+</text>
  <text class="ee-label" x="100" y="58">−</text>
{pin(150, 38)}
{pin(150, 58)}
""", width=160, height=105, tags=["dc supply", "electronic load", "programmable source", "battery emulator", "instrument"])

    # 17. DSP / FPGA Real-Time Controller & HIL Simulator (dSPACE / OPAL-RT / Plecs RT Box / TI C2000)
    save_symbol(cat_inst, "instrument_dsp_fpga_hil_box", "DSP / FPGA Real-Time Controller / HIL Simulator Box", f"""
  <rect class="ee-tint-blue" x="14" y="14" width="152" height="82" rx="5"/>
  <text class="ee-label" x="90" y="32" font-size="11">DSP + FPGA Real-Time Target</text>
  <text class="ee-label" x="90" y="48">(C2000 / dSPACE / OPAL-RT)</text>
  <!-- Left Side: ADC Analog Inputs -->
  <rect class="ee-body" x="22" y="62" width="54" height="22" rx="2"/>
  <text class="ee-label" x="49" y="73">16-bit ADC</text>
  <!-- Right Side: PWM Fiber/Digital Outputs -->
  <rect class="ee-body" x="104" y="62" width="54" height="22" rx="2"/>
  <text class="ee-label" x="131" y="73">PWM / Gate</text>
  <line class="ee-stroke" x1="35" y1="84" x2="35" y2="104"/>
  <line class="ee-stroke" x1="60" y1="84" x2="60" y2="104"/>
  <line class="ee-stroke" x1="118" y1="84" x2="118" y2="104"/>
  <line class="ee-stroke" x1="144" y1="84" x2="144" y2="104"/>
{pin(35, 104)}
{pin(60, 104)}
{pin(118, 104)}
{pin(144, 104)}
""", width=180, height=115, tags=["dsp", "fpga", "hil", "dspace", "opal-rt", "plecs rt box", "controller", "instrument"])

    # 18. Inline Torque & Speed Transducer + Dynamometer Test Bench Coupling
    save_symbol(cat_inst, "instrument_torque_transducer_dyno", "Inline Torque Sensor & Dynamometer Test Bench", f"""
  <!-- Left Shaft from Test Motor (MUT) -->
  <line class="ee-thick" x1="8" y1="50" x2="48" y2="50"/>
  <rect class="ee-body" x="28" y="38" width="8" height="24"/>
  <!-- Torque & Speed Sensor Block -->
  <rect class="ee-tint-amber" x="48" y="26" width="54" height="48" rx="4"/>
  <text class="ee-text" x="75" y="43" font-size="12">T<tspan dy="2" font-size="8">em</tspan>, ω<tspan dy="2" font-size="8">m</tspan></text>
  <text class="ee-label" x="75" y="60">Torque Sensor</text>
  <!-- Right Shaft to Load Dynamometer -->
  <line class="ee-thick" x1="102" y1="50" x2="132" y2="50"/>
  <rect class="ee-body" x="112" y="38" width="8" height="24"/>
  <circle class="ee-body" cx="156" cy="50" r="24"/>
  <text class="ee-label" x="156" y="45">Load</text>
  <text class="ee-label" x="156" y="57">Dyno</text>
  <!-- BNC Measurement Output -->
  <line class="ee-thin" x1="75" y1="74" x2="75" y2="94" marker-end="url(#arrow)"/>
{pin(75, 94)}
""", width=190, height=105, tags=["torque sensor", "torque transducer", "dynamometer", "dyno", "test bench", "instrument"])
