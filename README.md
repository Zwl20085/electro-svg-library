<div align="center">

# ⚡ ElectroSVG

### Publication-Grade IEEE / IEC Electrical Engineering Vector Symbol Library, Converter Topologies, Machine Windings, Lab Instruments & Scope SVG Studio

[![Symbols](https://img.shields.io/badge/Vector_Assets-142_SVGs-1d4ed8?style=for-the-badge)](#complete-142-asset-catalog-with-visual-previews)
[![Standard](https://img.shields.io/badge/Standard-IEEE_315_%2F_IEC_60617-0f766e?style=for-the-badge)](#unified-design-system--ieeeiec-style-guide)
[![Draw.io](https://img.shields.io/badge/Draw.io_Stencil-Ready_(.xml)-dc2626?style=for-the-badge)](#2-drag-and-drop-in-drawio--diagramsnet-visio-replacement)
[![License: MIT](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)](LICENSE)

<p align="center">
  <strong>Stop fighting Microsoft Visio for your IEEE Transactions & IEC journal papers.</strong><br/>
  <strong>ElectroSVG</strong> provides <strong>142 mathematically aligned, publication-ready SVG symbols, converter topologies, electrical machine cross-sections, stator windings, bench measurement instruments, and oscilloscope figures</strong>—all crafted in a single, strictly unified visual language.
</p>

<p align="center">
  <img src="symbols/08_power_topologies/topology_3ph_2level_vsi.svg" height="145" alt="3-Phase 2L-VSI Drive"/>
  &nbsp;&nbsp;
  <img src="symbols/08_power_topologies/topology_dab_converter.svg" height="145" alt="Dual Active Bridge Converter"/>
  &nbsp;&nbsp;
  <img src="symbols/09_scope_waveforms/scope_4ch_power_electronics.svg" height="145" alt="4-Channel Power Electronics Scope"/>
</p>

<p align="center">
  <img src="symbols/05_electrical_machines/rotor_cross_section_ipmsm.svg" height="105" alt="IPMSM Rotor"/>
  &nbsp;
  <img src="symbols/04_transformers_windings/winding_dual_3ph_6ph.svg" height="105" alt="Dual 3-Phase Winding"/>
  &nbsp;
  <img src="symbols/03_semiconductors/sic_mosfet_kelvin.svg" height="105" alt="SiC MOSFET Kelvin"/>
  &nbsp;
  <img src="symbols/10_measurement_instruments/instrument_bench_oscilloscope.svg" height="105" alt="Bench Oscilloscope"/>
  &nbsp;
  <img src="symbols/10_measurement_instruments/instrument_power_analyzer.svg" height="105" alt="Power Analyzer"/>
  &nbsp;
  <img src="symbols/10_measurement_instruments/instrument_torque_transducer_dyno.svg" height="105" alt="Torque Sensor Dyno"/>
</p>

</div>

---

## ✨ Why ElectroSVG?

When preparing figures for **IEEE Transactions on Power Electronics (TPEL)**, **IEEE Transactions on Industrial Electronics (TIE)**, **IEEE Transactions on Energy Conversion (TEC)**, or **IET / Elsevier** journals, authors typically struggle with:
1. **Inconsistent stroke weights and fonts** when mixing Visio stencils, Simulink screenshots, and MATLAB plots.
2. **Missing modern components** such as 4-pin Kelvin-source SiC MOSFETs, GaN HEMTs, Hairpin stator slots, Dual 3-Phase ($30^\circ$) windings, IPMSM V-shape rotors, or bench hardware-in-the-loop (HIL) / Power Analyzer testbench icons.
3. **Rasterized / blurry oscilloscope screenshots** instead of crisp vector waveforms.

**ElectroSVG solves all three:**
- **142 Pure Vector SVGs** across **10 curated categories** (`symbols/01_passives` through `symbols/10_measurement_instruments`).
- **Interactive Web Studio (`index.html`)** with instant search, live stroke-width adjustment, 1-click SVG clipboard copy, and a **Parametric Multi-Channel Scope & PWM Waveform Synthesizer**.
- **Native Draw.io / diagrams.net Library (`electro_svg_library.drawio.xml`)** for zero-cost, drag-and-drop schematic drawing with orthogonal wire routing.
- **Zero-Error Validated XML**: Every SVG is verified by `verify_library.py` for strict XML well-formedness, unique scoped marker IDs, and $10\text{ px}$ terminal grid alignment.

---

## 🚀 Three Ways to Use

### 1. Interactive Web Studio & Scope SVG Generator (`index.html`)
Open `index.html` in any browser:
- **Tab 1 — Symbol & Circuit Explorer**: Filter by category or keyword, switch global stroke weights (`1.5 px`, `2.0 px`, `2.5 px`), and click **Copy SVG** to paste directly into **Figma, Inkscape, Adobe Illustrator, or PowerPoint**.
- **Tab 2 — Parametric Scope & Waveform Synthesizer**: Generate publication-ready multi-channel oscilloscope figures (3-phase SPWM + currents, Synchronous Buck steady-state, DAB Single-Phase-Shift waveforms, PMSM FOC step response) with real-time sliders for carrier frequency ratio, modulation index, and ripple.

### 2. Drag-and-Drop in Draw.io / diagrams.net (Visio Replacement)
1. Open [app.diagrams.net](https://app.diagrams.net/) or the **VS Code Draw.io Extension**.
2. Click **File → Open Library from → Device...** and select **`electro_svg_library.drawio.xml`**.
3. All **142 symbols** appear in your sidebar stencil palette! Drag them onto the canvas, snap wires to the $10\text{ px}$ pins, and export directly to cropped PDF or SVG for LaTeX (`\includegraphics` / `\includesvg`).

### 3. Direct SVG Files (`symbols/`) & Master Sprite (`master_sprite.svg`)
Use individual files in `symbols/<category>/<slug>.svg` or reference any symbol from `master_sprite.svg` via `<use href="master_sprite.svg#igbt_with_diode"/>`.

---

## 🎨 Unified Design System & IEEE/IEC Style Guide

| Parameter | Specification | CSS Class |
| :--- | :--- | :--- |
| **Canvas & Pin Grid** | `100 × 100` (standard symbols), terminals snapped to multiples of `10 px` | `.ee-pin` (`r = 2.2 px`, white fill) |
| **Primary Component Stroke** | `2.0 px` solid `#111827`, round caps & joins | `.ee-stroke` |
| **Secondary / Annotation Stroke** | `1.3 px` solid `#111827` (arrows, reference frames, ticks) | `.ee-thin` |
| **Busbar / Shaft / Plate Stroke** | `3.0 px` solid `#111827` (DC busbars, mechanical shafts) | `.ee-thick` |
| **Three-Phase / Semantic Colors** | Phase A / N-Pole: `#dc2626` · Phase B: `#16a34a` · Phase C / S-Pole: `#2563eb` | `.ee-wire-a`, `.ee-wire-b`, `.ee-wire-c` |
| **Typography** | `Times New Roman` *italic* for math variables ($v_{ds}, i_q, \theta_e$); `Inter` bold for labels | `.ee-text`, `.ee-label` |

---

## 📂 Complete 142-Asset Catalog with Visual Previews

### 01. Passives & Magnetics (`symbols/01_passives/` — 19 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/01_passives/resistor_ieee.svg" width="64"/> | **Resistor (IEEE)**<br/>`resistor_ieee.svg` | <img src="symbols/01_passives/resistor_iec.svg" width="64"/> | **Resistor (IEC)**<br/>`resistor_iec.svg` | <img src="symbols/01_passives/resistor_variable.svg" width="64"/> | **Variable Resistor**<br/>`resistor_variable.svg` |
| <img src="symbols/01_passives/potentiometer.svg" width="64"/> | **Potentiometer**<br/>`potentiometer.svg` | <img src="symbols/01_passives/resistor_shunt_kelvin.svg" width="64"/> | **4-Wire Kelvin Shunt**<br/>`resistor_shunt_kelvin.svg` | <img src="symbols/01_passives/capacitor_unpolarized.svg" width="64"/> | **Capacitor**<br/>`capacitor_unpolarized.svg` |
| <img src="symbols/01_passives/capacitor_polarized_ieee.svg" width="64"/> | **Polarized Cap (IEEE)**<br/>`capacitor_polarized_ieee.svg` | <img src="symbols/01_passives/capacitor_polarized_iec.svg" width="64"/> | **Polarized Cap (IEC)**<br/>`capacitor_polarized_iec.svg` | <img src="symbols/01_passives/capacitor_variable.svg" width="64"/> | **Variable Capacitor**<br/>`capacitor_variable.svg` |
| <img src="symbols/01_passives/inductor_air.svg" width="64"/> | **Inductor (Air Core)**<br/>`inductor_air.svg` | <img src="symbols/01_passives/inductor_iron_core.svg" width="64"/> | **Inductor (Iron Core)**<br/>`inductor_iron_core.svg` | <img src="symbols/01_passives/inductor_ferrite_core.svg" width="64"/> | **Inductor (Ferrite)**<br/>`inductor_ferrite_core.svg` |
| <img src="symbols/01_passives/inductor_variable.svg" width="64"/> | **Variable Inductor**<br/>`inductor_variable.svg` | <img src="symbols/01_passives/coupled_inductor_cmc.svg" width="64"/> | **Common-Mode Choke**<br/>`coupled_inductor_cmc.svg` | <img src="symbols/01_passives/ferrite_bead.svg" width="64"/> | **Ferrite Bead**<br/>`ferrite_bead.svg` |
| <img src="symbols/01_passives/thermistor_ntc.svg" width="64"/> | **Thermistor (NTC/PTC)**<br/>`thermistor_ntc.svg` | <img src="symbols/01_passives/varistor_mov.svg" width="64"/> | **MOV Varistor**<br/>`varistor_mov.svg` | <img src="symbols/01_passives/crystal_resonator.svg" width="64"/> | **Crystal Resonator**<br/>`crystal_resonator.svg` |
| <img src="symbols/01_passives/memristor.svg" width="64"/> | **Memristor**<br/>`memristor.svg` | | | | |

### 02. Sources & Grounds (`symbols/02_sources_grounds/` — 11 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/02_sources_grounds/source_dc_voltage.svg" width="64"/> | **DC Voltage Source**<br/>`source_dc_voltage.svg` | <img src="symbols/02_sources_grounds/source_battery.svg" width="64"/> | **Battery Cell / Pack**<br/>`source_battery.svg` | <img src="symbols/02_sources_grounds/source_ac_voltage.svg" width="64"/> | **AC Voltage Source**<br/>`source_ac_voltage.svg` |
| <img src="symbols/02_sources_grounds/source_current.svg" width="64"/> | **Current Source**<br/>`source_current.svg` | <img src="symbols/02_sources_grounds/source_controlled_voltage.svg" width="64"/> | **Controlled V-Source**<br/>`source_controlled_voltage.svg` | <img src="symbols/02_sources_grounds/source_controlled_current.svg" width="64"/> | **Controlled I-Source**<br/>`source_controlled_current.svg` |
| <img src="symbols/02_sources_grounds/source_pv_array.svg" width="64"/> | **PV Solar Array**<br/>`source_pv_array.svg` | <img src="symbols/02_sources_grounds/source_3ph_grid.svg" width="64"/> | **3-Phase AC Grid**<br/>`source_3ph_grid.svg` | <img src="symbols/02_sources_grounds/ground_earth.svg" width="64"/> | **Earth Ground**<br/>`ground_earth.svg` |
| <img src="symbols/02_sources_grounds/ground_chassis.svg" width="64"/> | **Chassis Ground**<br/>`ground_chassis.svg` | <img src="symbols/02_sources_grounds/ground_signal.svg" width="64"/> | **Signal Ground**<br/>`ground_signal.svg` | | |

### 03. Power Electronics Devices & Semiconductors (`symbols/03_semiconductors/` — 22 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/03_semiconductors/diode_power.svg" width="64"/> | **Power Diode**<br/>`diode_power.svg` | <img src="symbols/03_semiconductors/diode_filled.svg" width="64"/> | **Power Diode (Filled)**<br/>`diode_filled.svg` | <img src="symbols/03_semiconductors/diode_schottky.svg" width="64"/> | **SiC Schottky Diode**<br/>`diode_schottky.svg` |
| <img src="symbols/03_semiconductors/diode_zener.svg" width="64"/> | **Zener Diode**<br/>`diode_zener.svg` | <img src="symbols/03_semiconductors/diode_tvs_bidir.svg" width="64"/> | **Bidirectional TVS**<br/>`diode_tvs_bidir.svg` | <img src="symbols/03_semiconductors/diode_led.svg" width="64"/> | **LED**<br/>`diode_led.svg` |
| <img src="symbols/03_semiconductors/diode_photo.svg" width="64"/> | **Photodiode**<br/>`diode_photo.svg` | <img src="symbols/03_semiconductors/thyristor_scr.svg" width="64"/> | **SCR Thyristor**<br/>`thyristor_scr.svg` | <img src="symbols/03_semiconductors/thyristor_gto_igct.svg" width="64"/> | **GTO / IGCT**<br/>`thyristor_gto_igct.svg` |
| <img src="symbols/03_semiconductors/triac.svg" width="64"/> | **TRIAC**<br/>`triac.svg` | <img src="symbols/03_semiconductors/igbt_bare.svg" width="64"/> | **IGBT (Bare)**<br/>`igbt_bare.svg` | <img src="symbols/03_semiconductors/igbt_with_diode.svg" width="64"/> | **IGBT + Freewheeling Diode**<br/>`igbt_with_diode.svg` |
| <img src="symbols/03_semiconductors/mosfet_nch_power.svg" width="64"/> | **N-Ch Power MOSFET**<br/>`mosfet_nch_power.svg` | <img src="symbols/03_semiconductors/mosfet_pch_power.svg" width="64"/> | **P-Ch Power MOSFET**<br/>`mosfet_pch_power.svg` | <img src="symbols/03_semiconductors/sic_mosfet_kelvin.svg" width="64"/> | **SiC MOSFET (4-Pin Kelvin)**<br/>`sic_mosfet_kelvin.svg` |
| <img src="symbols/03_semiconductors/gan_hemt.svg" width="64"/> | **GaN HEMT**<br/>`gan_hemt.svg` | <img src="symbols/03_semiconductors/bjt_npn.svg" width="64"/> | **BJT NPN**<br/>`bjt_npn.svg` | <img src="symbols/03_semiconductors/bjt_pnp.svg" width="64"/> | **BJT PNP**<br/>`bjt_pnp.svg` |
| <img src="symbols/03_semiconductors/ideal_power_switch.svg" width="64"/> | **Ideal Gate Switch**<br/>`ideal_power_switch.svg` | <img src="symbols/03_semiconductors/bidirectional_switch_4q.svg" width="64"/> | **4-Quadrant Switch**<br/>`bidirectional_switch_4q.svg` | <img src="symbols/03_semiconductors/half_bridge_leg_module.svg" width="54"/> | **2-in-1 Half-Bridge Module**<br/>`half_bridge_leg_module.svg` |
| <img src="symbols/03_semiconductors/optocoupler_isolated_driver.svg" width="64"/> | **Isolated Gate Driver**<br/>`optocoupler_isolated_driver.svg` | | | | |

### 04. Transformers & Machine Windings (`symbols/04_transformers_windings/` — 17 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/04_transformers_windings/transformer_1ph_2w.svg" width="64"/> | **1-Ph 2-Winding TX**<br/>`transformer_1ph_2w.svg` | <img src="symbols/04_transformers_windings/transformer_hf_center_tapped.svg" width="64"/> | **HF Center-Tapped TX**<br/>`transformer_hf_center_tapped.svg` | <img src="symbols/04_transformers_windings/transformer_2winding_iec.svg" width="64"/> | **2-Winding TX (IEC)**<br/>`transformer_2winding_iec.svg` |
| <img src="symbols/04_transformers_windings/transformer_3winding_iec.svg" width="64"/> | **3-Winding TX (IEC)**<br/>`transformer_3winding_iec.svg` | <img src="symbols/04_transformers_windings/autotransformer.svg" width="64"/> | **Autotransformer**<br/>`autotransformer.svg` | <img src="symbols/04_transformers_windings/current_transformer_ct.svg" width="64"/> | **Current Transformer (CT)**<br/>`current_transformer_ct.svg` |
| <img src="symbols/04_transformers_windings/transformer_planar_pcb.svg" width="64"/> | **Planar PCB Transformer**<br/>`transformer_planar_pcb.svg` | <img src="symbols/04_transformers_windings/winding_3ph_wye.svg" width="64"/> | **3-Ph Wye ($Y$) Winding**<br/>`winding_3ph_wye.svg` | <img src="symbols/04_transformers_windings/winding_3ph_wye_grounded.svg" width="64"/> | **Grounded Wye ($Y_n$)**<br/>`winding_3ph_wye_grounded.svg` |
| <img src="symbols/04_transformers_windings/winding_3ph_delta.svg" width="64"/> | **3-Ph Delta ($\Delta$) Winding**<br/>`winding_3ph_delta.svg` | <img src="symbols/04_transformers_windings/winding_3ph_open_end.svg" width="64"/> | **Open-End Winding (OEW)**<br/>`winding_3ph_open_end.svg` | <img src="symbols/04_transformers_windings/winding_dual_3ph_6ph.svg" width="64"/> | **Dual 3-Ph ($30^\circ$ 6-Ph)**<br/>`winding_dual_3ph_6ph.svg` |
| <img src="symbols/04_transformers_windings/winding_5ph_star.svg" width="64"/> | **5-Ph Star Winding**<br/>`winding_5ph_star.svg` | <img src="symbols/04_transformers_windings/winding_zigzag.svg" width="64"/> | **Zig-Zag Winding**<br/>`winding_zigzag.svg` | <img src="symbols/04_transformers_windings/stator_slot_hairpin.svg" width="64"/> | **Hairpin Stator Slot**<br/>`stator_slot_hairpin.svg` |
| <img src="symbols/04_transformers_windings/winding_concentrated_tooth.svg" width="64"/> | **FSCW Tooth-Coil Winding**<br/>`winding_concentrated_tooth.svg` | <img src="symbols/04_transformers_windings/winding_star_of_slots.svg" width="64"/> | **Star of Slots Phasors**<br/>`winding_star_of_slots.svg` | | |

### 05. Electrical Machines & Rotor Cross-Sections (`symbols/05_electrical_machines/` — 13 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/05_electrical_machines/machine_dc_brushed.svg" width="64"/> | **DC Machine (Brushed)**<br/>`machine_dc_brushed.svg` | <img src="symbols/05_electrical_machines/machine_dc_sep_excited.svg" width="64"/> | **Separately Excited DC**<br/>`machine_dc_sep_excited.svg` | <img src="symbols/05_electrical_machines/machine_3ph_induction_scim.svg" width="64"/> | **3-Ph Induction Motor (IM)**<br/>`machine_3ph_induction_scim.svg` |
| <img src="symbols/05_electrical_machines/machine_3ph_dfig.svg" width="64"/> | **Doubly-Fed IG (DFIG)**<br/>`machine_3ph_dfig.svg` | <img src="symbols/05_electrical_machines/machine_3ph_pmsm.svg" width="64"/> | **PMSM / BLDC Motor**<br/>`machine_3ph_pmsm.svg` | <img src="symbols/05_electrical_machines/rotor_cross_section_spmsm.svg" width="64"/> | **SPMSM Rotor Cross-Section**<br/>`rotor_cross_section_spmsm.svg` |
| <img src="symbols/05_electrical_machines/rotor_cross_section_ipmsm.svg" width="64"/> | **IPMSM V-Shape Rotor**<br/>`rotor_cross_section_ipmsm.svg` | <img src="symbols/05_electrical_machines/rotor_cross_section_synrm.svg" width="64"/> | **SynRM Flux-Barrier Rotor**<br/>`rotor_cross_section_synrm.svg` | <img src="symbols/05_electrical_machines/machine_srm_salient.svg" width="64"/> | **6/4 Switched Reluctance**<br/>`machine_srm_salient.svg` |
| <img src="symbols/05_electrical_machines/machine_3ph_sync_generator.svg" width="64"/> | **Sync Generator (WFSG)**<br/>`machine_3ph_sync_generator.svg` | <img src="symbols/05_electrical_machines/machine_axial_flux_afpm.svg" width="64"/> | **Axial-Flux PM (AFPM)**<br/>`machine_axial_flux_afpm.svg` | <img src="symbols/05_electrical_machines/machine_linear_motor_lsm.svg" width="64"/> | **Linear PMSM (LPMSM)**<br/>`machine_linear_motor_lsm.svg` |
| <img src="symbols/05_electrical_machines/sensor_encoder_resolver.svg" width="64"/> | **Rotary Encoder / Resolver**<br/>`sensor_encoder_resolver.svg` | | | | |

### 06. Control Blocks & Coordinate Transforms (`symbols/06_control_blocks/` — 12 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/06_control_blocks/control_summing_junction.svg" width="64"/> | **Summing Junction**<br/>`control_summing_junction.svg` | <img src="symbols/06_control_blocks/control_pi_regulator.svg" width="64"/> | **PI / PID Controller**<br/>`control_pi_regulator.svg` | <img src="symbols/06_control_blocks/control_pr_regulator.svg" width="64"/> | **PR Resonant Controller**<br/>`control_pr_regulator.svg` |
| <img src="symbols/06_control_blocks/control_integrator.svg" width="64"/> | **Integrator ($\int dt$)**<br/>`control_integrator.svg` | <img src="symbols/06_control_blocks/transform_clarke_abc_ab.svg" width="64"/> | **Clarke ($abc \to \alpha\beta$)**<br/>`transform_clarke_abc_ab.svg` | <img src="symbols/06_control_blocks/transform_park_ab_dq.svg" width="64"/> | **Park ($\alpha\beta \to dq$)**<br/>`transform_park_ab_dq.svg` |
| <img src="symbols/06_control_blocks/transform_inv_park_dq_ab.svg" width="64"/> | **Inverse Park ($dq \to \alpha\beta$)**<br/>`transform_inv_park_dq_ab.svg` | <img src="symbols/06_control_blocks/transform_abc_to_dq.svg" width="64"/> | **Direct Park ($abc \to dq$)**<br/>`transform_abc_to_dq.svg` | <img src="symbols/06_control_blocks/control_svpwm_block.svg" width="64"/> | **SVPWM Modulator**<br/>`control_svpwm_block.svg` |
| <img src="symbols/06_control_blocks/control_pll_block.svg" width="64"/> | **SRF-PLL Block**<br/>`control_pll_block.svg` | <img src="symbols/06_control_blocks/control_limiter_saturation.svg" width="64"/> | **Saturation Limiter**<br/>`control_limiter_saturation.svg` | <img src="symbols/06_control_blocks/control_hysteresis.svg" width="64"/> | **Hysteresis Comparator**<br/>`control_hysteresis.svg` |

### 07. Sensors, Switchgear & Protection (`symbols/07_sensors_protection/` — 8 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/07_sensors_protection/opamp.svg" width="64"/> | **Operational Amplifier**<br/>`opamp.svg` | <img src="symbols/07_sensors_protection/sensor_hall_current.svg" width="64"/> | **Hall Current Sensor (LEM)**<br/>`sensor_hall_current.svg` | <img src="symbols/07_sensors_protection/meter_voltmeter.svg" width="64"/> | **Voltmeter (V)**<br/>`meter_voltmeter.svg` |
| <img src="symbols/07_sensors_protection/meter_ammeter.svg" width="64"/> | **Ammeter (A)**<br/>`meter_ammeter.svg` | <img src="symbols/07_sensors_protection/breaker_cb.svg" width="64"/> | **Circuit Breaker (CB)**<br/>`breaker_cb.svg` | <img src="symbols/07_sensors_protection/fuse_iec.svg" width="64"/> | **Fuse (IEC)**<br/>`fuse_iec.svg` |
| <img src="symbols/07_sensors_protection/contactor_relay.svg" width="64"/> | **Contactor / Relay**<br/>`contactor_relay.svg` | <img src="symbols/07_sensors_protection/sld_3wire_bus.svg" width="64"/> | **SLD 3-Wire Busbar**<br/>`sld_3wire_bus.svg` | | |

### 08. Complete Power Electronics Topologies (`symbols/08_power_topologies/` — 15 Assets)
| Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- |
| <img src="symbols/08_power_topologies/topology_sync_buck.svg" width="210"/> | **Synchronous Buck Converter**<br/>`topology_sync_buck.svg` | <img src="symbols/08_power_topologies/topology_boost.svg" width="210"/> | **Boost DC-DC Converter**<br/>`topology_boost.svg` |
| <img src="symbols/08_power_topologies/topology_h_bridge_1ph.svg" width="190"/> | **1-Phase Full-Bridge (H-Bridge)**<br/>`topology_h_bridge_1ph.svg` | <img src="symbols/08_power_topologies/topology_3ph_2level_vsi.svg" width="230"/> | **3-Phase 2-Level VSI Motor Drive**<br/>`topology_3ph_2level_vsi.svg` |
| <img src="symbols/08_power_topologies/topology_3level_npc_leg.svg" width="160"/> | **3-Level NPC Phase Leg**<br/>`topology_3level_npc_leg.svg` | <img src="symbols/08_power_topologies/topology_3level_ttype_leg.svg" width="160"/> | **3-Level T-Type Phase Leg**<br/>`topology_3level_ttype_leg.svg` |
| <img src="symbols/08_power_topologies/topology_3level_flying_cap.svg" width="150"/> | **3-Level Flying Capacitor Leg**<br/>`topology_3level_flying_cap.svg` | <img src="symbols/08_power_topologies/topology_dab_converter.svg" width="240"/> | **Dual Active Bridge (DAB)**<br/>`topology_dab_converter.svg` |
| <img src="symbols/08_power_topologies/topology_llc_resonant_tank.svg" width="190"/> | **LLC Resonant Tank Stage**<br/>`topology_llc_resonant_tank.svg` | <img src="symbols/08_power_topologies/topology_mmc_submodule.svg" width="140"/> | **MMC Half-Bridge Submodule**<br/>`topology_mmc_submodule.svg` |
| <img src="symbols/08_power_topologies/topology_lcl_filter.svg" width="170"/> | **LCL Grid-Tie Filter**<br/>`topology_lcl_filter.svg` | <img src="symbols/08_power_topologies/topology_3ph_diode_rectifier.svg" width="170"/> | **3-Ph 6-Pulse Diode Rectifier**<br/>`topology_3ph_diode_rectifier.svg` |
| <img src="symbols/08_power_topologies/topology_vienna_rectifier_leg.svg" width="170"/> | **Vienna Rectifier Phase Leg**<br/>`topology_vienna_rectifier_leg.svg` | <img src="symbols/08_power_topologies/topology_z_source_network.svg" width="160"/> | **Z-Source Impedance Network**<br/>`topology_z_source_network.svg` |
| <img src="symbols/08_power_topologies/diagram_foc_complete_loop.svg" width="260"/> | **Complete PMSM Field-Oriented Control (FOC) Loop**<br/>`diagram_foc_complete_loop.svg` | | |

### 09. Scope & Waveform Publication Figures (`symbols/09_scope_waveforms/` — 7 Assets)
| Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- |
| <img src="symbols/09_scope_waveforms/scope_4ch_power_electronics.svg" width="220"/> | **4-Channel Digital Oscilloscope Plot**<br/>`scope_4ch_power_electronics.svg` | <img src="symbols/09_scope_waveforms/waveform_spwm_carrier.svg" width="210"/> | **Carrier SPWM Modulation**<br/>`waveform_spwm_carrier.svg` |
| <img src="symbols/09_scope_waveforms/diagram_svpwm_hexagon.svg" width="170"/> | **SVPWM Space-Vector Hexagon**<br/>`diagram_svpwm_hexagon.svg` | <img src="symbols/09_scope_waveforms/diagram_dq_phasor_frame.svg" width="170"/> | **$abc / \alpha\beta / dq$ Phasor Diagram**<br/>`diagram_dq_phasor_frame.svg` |
| <img src="symbols/09_scope_waveforms/waveform_zvs_commutation.svg" width="200"/> | **ZVS Soft-Switching & Dead-Time**<br/>`waveform_zvs_commutation.svg` | <img src="symbols/09_scope_waveforms/waveform_bode_plot.svg" width="200"/> | **Control Loop Bode Plot**<br/>`waveform_bode_plot.svg` |
| <img src="symbols/09_scope_waveforms/waveform_fft_thd_spectrum.svg" width="200"/> | **Harmonic FFT & THD Bar Chart**<br/>`waveform_fft_thd_spectrum.svg` | | |

### 10. Lab & Read Instruments (`symbols/10_measurement_instruments/` — 18 Assets)
| Preview | Name & File | Preview | Name & File | Preview | Name & File |
| :---: | :--- | :---: | :--- | :---: | :--- |
| <img src="symbols/10_measurement_instruments/meter_wattmeter.svg" width="64"/> | **Wattmeter (W)**<br/>`meter_wattmeter.svg` | <img src="symbols/10_measurement_instruments/meter_varmeter.svg" width="64"/> | **VARmeter (var)**<br/>`meter_varmeter.svg` | <img src="symbols/10_measurement_instruments/meter_power_factor.svg" width="64"/> | **Power Factor ($\cos\varphi$)**<br/>`meter_power_factor.svg` |
| <img src="symbols/10_measurement_instruments/meter_frequency_hz.svg" width="64"/> | **Frequency Meter (Hz)**<br/>`meter_frequency_hz.svg` | <img src="symbols/10_measurement_instruments/meter_energy_kwh.svg" width="64"/> | **Smart Energy Meter (kWh)**<br/>`meter_energy_kwh.svg` | <img src="symbols/10_measurement_instruments/meter_galvanometer.svg" width="64"/> | **Galvanometer (G)**<br/>`meter_galvanometer.svg` |
| <img src="symbols/10_measurement_instruments/meter_ohmmeter.svg" width="64"/> | **Ohmmeter ($\Omega$)**<br/>`meter_ohmmeter.svg` | <img src="symbols/10_measurement_instruments/instrument_analog_dial_gauge.svg" width="64"/> | **Analog Pointer Gauge**<br/>`instrument_analog_dial_gauge.svg` | <img src="symbols/10_measurement_instruments/instrument_potential_transformer_vt.svg" width="64"/> | **Potential Transformer (PT/VT)**<br/>`instrument_potential_transformer_vt.svg` |
| <img src="symbols/10_measurement_instruments/probe_current_clamp_rogowski.svg" width="64"/> | **Clamp / Rogowski Probe**<br/>`probe_current_clamp_rogowski.svg` | <img src="symbols/10_measurement_instruments/probe_hv_differential.svg" width="64"/> | **HV Differential Probe**<br/>`probe_hv_differential.svg` | <img src="symbols/10_measurement_instruments/instrument_bench_oscilloscope.svg" width="105"/> | **Bench Oscilloscope (DSO)**<br/>`instrument_bench_oscilloscope.svg` |
| <img src="symbols/10_measurement_instruments/instrument_power_analyzer.svg" width="115"/> | **Precision Power Analyzer**<br/>`instrument_power_analyzer.svg` | <img src="symbols/10_measurement_instruments/instrument_digital_multimeter.svg" width="95"/> | **6½-Digit Bench DMM**<br/>`instrument_digital_multimeter.svg` | <img src="symbols/10_measurement_instruments/instrument_spectrum_impedance_analyzer.svg" width="105"/> | **Impedance / EMI Analyzer**<br/>`instrument_spectrum_impedance_analyzer.svg` |
| <img src="symbols/10_measurement_instruments/instrument_programmable_dc_supply_load.svg" width="105"/> | **Prog. DC Supply / Load**<br/>`instrument_programmable_dc_supply_load.svg` | <img src="symbols/10_measurement_instruments/instrument_dsp_fpga_hil_box.svg" width="115"/> | **DSP / FPGA / HIL Box**<br/>`instrument_dsp_fpga_hil_box.svg` | <img src="symbols/10_measurement_instruments/instrument_torque_transducer_dyno.svg" width="120"/> | **Torque Sensor & Dyno**<br/>`instrument_torque_transducer_dyno.svg` |

---

## 🛠️ Rebuilding & Verifying from Source

The entire library is generated deterministically via Python 3 (zero external dependencies):

```bash
python generate_library.py          # Generates all 142 SVG files + catalog.json
python build_studio_and_exports.py  # Builds master_sprite.svg + electro_svg_library.drawio.xml
python build_html_studio.py         # Builds interactive index.html Studio
python verify_library.py            # Runs strict XML, path, class & ID collision verification
python cross_verify_with_jmag_suite.py  # Cross-verifies windings, dq-phasors, KVL/power balance & FFT/THD against jmag-agent-suite
```

### 🔬 Cross-Verification with `jmag-agent-suite` Physics & Winding Engine

All machine, winding, phasor, and harmonic figures are mathematically cross-verified against the analytical and physics-invariant engines in `jmag-agent-suite` (`jmag_bridge.winding`, `jmag_bridge.estimate`, `jmag_bridge.health`):

- **Star of Slots & FSCW Tooth-Coil Layout (`winding_star_of_slots.svg`, `winding_concentrated_tooth.svg`)**: Verified against `winding.plan(slots=12, poles=10, phases=3, layers=2)` ($q = 0.4$, coil pitch $y = 1$, fundamental winding factor $k_{w1} = 0.93301$, anti-periodic $180^\circ$ symmetry).
- **5-Phase Pentaphase Star Winding (`winding_5ph_star.svg`)**: Verified against `winding.plan(slots=10, poles=8, phases=5, layers=2)` ($q = 0.25$, $k_{w1} = 0.95106$).
- **$dq$-Axis Phasor & MTPA Reluctance Torque (`diagram_dq_phasor_frame.svg`, `rotor_cross_section_ipmsm.svg`)**: Verified against `estimate.torque_dq` ($T = \frac{3}{2} p [\psi_m i_q + (L_d - L_q) i_d i_q]$, with $i_d < 0$ in the 2nd quadrant of the $d$-$q$ frame for IPMSM MTPA and $K_t / K_e = 1.500000$).
- **Waveform Invariants & Harmonic THD (`scope_4ch_power_electronics.svg`, `waveform_fft_thd_spectrum.svg`)**: Verified against `health.kvl_residual` ($\max |R i + d\psi/dt - v| / V_{\max} = 1.44 \times 10^{-14} < 10^{-3}$), `health.power_balance` ($0.30\%$ difference $< 5\%$), and `health.harmonics` ($\text{THD} = 2.16\%$).

---

## 📄 License

Released under the **MIT License**. Free for academic papers, IEEE/IEC publications, textbooks, slides, and commercial engineering documentation.
