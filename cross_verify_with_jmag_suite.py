# -*- coding: utf-8 -*-
"""
Cross-Verification Script using JMAG Agent Suite (`jmag_bridge` pure-Python engine)
Imports `jmag_bridge.winding`, `jmag_bridge.estimate`, `jmag_bridge.health`, and `jmag_bridge.units`
directly from C:\\Users\\ZhangWentao\\Documents\\GitHub\\jmag-agent-suite\\src (READ-ONLY)
to mathematically cross-verify ElectroSVG's winding layouts, Star of Slots phasors,
machine sizing / dq-torque equations, KVL / electromechanical power balance, and FFT/THD spectra.
"""

import sys
import os
import math
import json

# Accept JMAG Agent Suite src path via CLI arg or env var (read-only import, zero modifications to jmag-agent-suite)
JMAG_SUITE_SRC = sys.argv[1] if len(sys.argv) > 1 else os.environ.get("JMAG_SUITE_SRC", r"C:\Users\ZhangWentao\Documents\GitHub\jmag-agent-suite\src")
sys.path.insert(0, JMAG_SUITE_SRC)

from jmag_bridge import winding, estimate, health, units

def run_cross_verification():
    report = {}

    # 1. Cross-verify Star of Slots & Winding Layouts:
    #    (a) 12-slot / 10-pole FSCW Concentrated Tooth-Coil Winding (`winding_concentrated_tooth.svg` & `winding_star_of_slots.svg`)
    #    (b) 12-slot / 4-pole Distributed Full-Pitch Winding (`spm_motor` benchmark)
    #    (c) 10-slot / 8-pole 5-Phase Pentaphase Winding (`winding_5ph_star.svg`)
    plan_12s10p = winding.plan(slots=12, poles=10, phases=3, layers=2, turns=25)
    plan_12s4p = winding.plan(slots=12, poles=4, phases=3, layers=1, turns=40)
    plan_10s8p_5ph = winding.plan(slots=10, poles=8, phases=5, layers=2, turns=30)

    report["winding_12s10p_fscw"] = {
        "winding_type": plan_12s10p["winding_type"],
        "q": plan_12s10p["q"],
        "coil_pitch": plan_12s10p["coil_pitch"],
        "kw1": plan_12s10p["kw1"],
        "winding_factors": plan_12s10p["winding_factors"],
        "slot_pitch_elec_deg": plan_12s10p["slot_pitch_elec_deg"],
        "symmetry": plan_12s10p["symmetry"],
        "labels_coils": plan_12s10p["labels_coils"],
        "top_mmf_harmonics": plan_12s10p["mmf_harmonics"][:6],
    }

    report["winding_12s4p_distributed"] = {
        "winding_type": plan_12s4p["winding_type"],
        "q": plan_12s4p["q"],
        "coil_pitch": plan_12s4p["coil_pitch"],
        "kw1": plan_12s4p["kw1"],
        "slot_pitch_elec_deg": plan_12s4p["slot_pitch_elec_deg"],
        "labels_coils": plan_12s4p["labels_coils"],
    }

    report["winding_10s8p_5phase"] = {
        "winding_type": plan_10s8p_5ph["winding_type"],
        "phases": plan_10s8p_5ph["phases"],
        "q": plan_10s8p_5ph["q"],
        "kw1": plan_10s8p_5ph["kw1"],
        "labels_coils": plan_10s8p_5ph["labels_coils"],
    }

    # 2. Cross-verify Machine Sizing & Analytic Equations (`estimate.py`):
    #    Benchmark 12s/4p SPMSM (r_rotor=27mm, hm=3mm, g=1mm, r_bore=31mm -> D_bore=62mm, L_stack=50mm, Br=1.25T)
    kc_res = estimate.carter_factor(slot_opening_mm=2.5, slot_pitch_mm=math.pi * 62.0 / 12.0, airgap_mm=1.0)
    bg_res = estimate.airgap_flux_density(Br=1.25, magnet_mm=3.0, airgap_mm=1.0, mu_r=1.05, carter=kc_res["value"], leakage=0.95)
    ke_res = estimate.emf_constant(turns_per_phase=160, kw1=plan_12s4p["kw1"], Bg=bg_res["value"],
                                   bore_mm=62.0, stack_mm=50.0, poles=4, pole_arc_ratio=80.0/90.0)
    kt_res = estimate.torque_constant(turns_per_phase=160, kw1=plan_12s4p["kw1"], Bg=bg_res["value"],
                                      bore_mm=62.0, stack_mm=50.0, poles=4, pole_arc_ratio=80.0/90.0)
    # Verify IPMSM dq reluctance + magnet torque (`rotor_cross_section_ipmsm.svg`, `diagram_dq_phasor_frame.svg`)
    tq_ipm = estimate.torque_dq(poles=8, psi_m=0.12, iq=25.0, id=-12.0, Ld=1.8e-3, Lq=4.2e-3)

    report["machine_estimates"] = {
        "carter_factor": round(kc_res["value"], 4),
        "airgap_Bg_T": round(bg_res["value"], 4),
        "psi_m_Wb": round(ke_res["details"]["psi_m_Wb"], 5),
        "Ke_Vs_per_rad": round(ke_res["value"], 4),
        "Kt_Nm_per_A_peak": round(kt_res["value"], 4),
        "Kt_over_Ke_ratio": round(kt_res["value"] / ke_res["value"], 6),  # Must equal exactly 1.5 (3/2)
        "ipmsm_torque_dq": {
            "total_Nm": round(tq_ipm["value"], 3),
            "magnet_torque_Nm": round(tq_ipm["details"]["magnet_torque_Nm"], 3),
            "reluctance_torque_Nm": round(tq_ipm["details"]["reluctance_torque_Nm"], 3),
        }
    }

    # 3. Cross-verify Waveform Health, KVL Residual, Power Balance & Harmonic THD (`health.py`):
    #    Generate 2 full electrical periods (60 steps/period, f_e = 50 Hz) of a 3-phase PMSM drive
    fe = 50.0
    period = 1.0 / fe
    spp = 60
    dt = period / spp
    n_steps = 2 * spp + 1
    t_axis = [k * dt for k in range(n_steps)]
    R_ph = 0.2
    L_ph = 2.5e-3
    psi_m = ke_res["details"]["psi_m_Wb"]
    omega_e = 2 * math.pi * fe
    poles = 4
    rpm = 1500.0
    I_pk = 10.0

    currents = {}
    fluxes = {}
    voltages = {}
    for idx, ph_name in enumerate(("CoilU", "CoilV", "CoilW")):
        ang0 = -2 * math.pi * idx / 3.0
        # i_k(t) in phase with back-EMF (-sin(omega_e*t + ang0)) for id=0 operation
        i_seq = [-I_pk * math.sin(omega_e * t + ang0) for t in t_axis]
        psi_seq = [psi_m * math.cos(omega_e * t + ang0) + L_ph * ik for t, ik in zip(t_axis, i_seq)]
        v_seq = [0.0] + [R_ph * i_seq[k] + (psi_seq[k] - psi_seq[k-1]) / dt for k in range(1, n_steps)]
        v_seq[0] = v_seq[1]
        currents[ph_name] = i_seq
        fluxes[ph_name] = psi_seq
        voltages[ph_name] = v_seq

    # Electromagnetic torque with realistic 6th and 12th spatial harmonic ripple
    t_mean_nom = 1.5 * (poles / 2) * psi_m * I_pk
    torque_seq = [t_mean_nom * (1.0 + 0.018 * math.cos(6 * omega_e * t) + 0.006 * math.cos(12 * omega_e * t)) for t in t_axis]

    kvl_check = health.kvl_residual(t_axis, currents["CoilU"], voltages["CoilU"], fluxes["CoilU"], R_ph)
    pb_check = health.power_balance(t_axis, currents, fluxes, torque_seq, speed_rpm=rpm, period=period)

    # Test THD calculation on our PWM/inverter phase current with 5th, 7th, 11th, 13th harmonics
    # Matching `waveform_fft_thd_spectrum.svg`: THD = 2.14%
    _, t_one = health.last_period(t_axis, t_axis, period)
    i_distorted = [
        10.0 * math.sin(omega_e * t)
        + 0.175 * math.sin(5 * omega_e * t)
        + 0.110 * math.sin(7 * omega_e * t)
        + 0.052 * math.sin(11 * omega_e * t)
        + 0.032 * math.sin(13 * omega_e * t)
        for t in t_one
    ]
    harm_res = health.harmonics(i_distorted, orders=19)

    report["physics_and_health_checks"] = {
        "kvl_residual": kvl_check,
        "power_balance": pb_check,
        "harmonic_fft_check": {
            "fundamental_A": round(harm_res["fundamental"], 4),
            "thd_pct": round(harm_res["thd_pct"], 2),
            "h5_pct": round(harm_res["amplitudes"][5] / harm_res["fundamental"] * 100, 2),
            "h7_pct": round(harm_res["amplitudes"][7] / harm_res["fundamental"] * 100, 2),
            "h11_pct": round(harm_res["amplitudes"][11] / harm_res["fundamental"] * 100, 2),
            "h13_pct": round(harm_res["amplitudes"][13] / harm_res["fundamental"] * 100, 2),
        }
    }

    print(json.dumps(report, indent=2))
    return report

if __name__ == "__main__":
    run_cross_verification()
