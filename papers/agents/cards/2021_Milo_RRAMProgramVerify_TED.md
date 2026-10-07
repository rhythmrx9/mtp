---
id: W3180792321
key: 2021_Milo_RRAMProgramVerify_TED
title: "Accurate Program/Verify Schemes of Resistive Switching Memory (RRAM) for In-Memory Neural Network Circuits"
short: "RRAM Program/Verify Schemes"
year: 2021
venue: "TED"
venue_full: "IEEE Transactions on Electron Devices"
authors: "Valerio Milo, Artem Glukhov, Eduardo Pérez, Cristian Zambelli, Nicola Lepri, Mamathamba Kalishettyhalli Mahadevaiah, Emilio Pérez-Bosch Quesada, Piero Olivo, Christian Wenger, Daniele Ielmini"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["write-verify-programming", "device-variation", "read-write-noise", "ir-drop-parasitics", "weight-mapping", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 8
citations_overall: 107
priority_score: 5.85
doi: "https://doi.org/10.1109/ted.2021.3089995"
pdf: "../../06_Nonidealities_and_Reliability/2021_Milo_RRAMProgramVerify_TED.pdf"
fulltext: "../fulltext/2021_Milo_RRAMProgramVerify_TED.txt"
---

# RRAM Program/Verify Schemes

**Accurate Program/Verify Schemes of Resistive Switching Memory (RRAM) for In-Memory Neural Network Circuits** — IEEE Transactions on Electron Devices (2021)

## TL;DR
Compares three multilevel-cell program/verify algorithms (ISPVA, IGVVA-100, IGVVA-10) on a measured 4-kbit 1T1R HfO2 RRAM array and shows fine gate-voltage stepping (10 mV) gives the lowest D2D variability, enabling a simulated 2-layer FC-NN to reach 96.58% MNIST accuracy versus 96.77% for FP-64.

## Summary
RRAM in-memory computing is limited by conductance precision (programming variation, RTN, drift, relaxation), and MLC program/verify is the main countermeasure, yet its effect on system-level accuracy and power is poorly understood. The authors measure a 64x64 (4 kbit) 1T1R TiN/Ti/HfO2/TiN array in 0.25 um CMOS. They compare ISPVA (incremental top-electrode voltage with fixed gate voltage, dVTE = 100 mV) against IGVVA (incremental gate voltage, fixed VTE = 1.2 V) with steps of 100 mV (IGVVA-100) and 10 mV (IGVVA-10), measuring conductance immediately after switching (AS) and at the end of the algorithm (EA) to capture relaxation. IGVVA-10 yields the smallest D2D variability but needs ~121 pulses. Measured conductance CDFs for HRS plus 8 LRS levels (50-225 uS) feed a simulation of a 197-20/100-10 FC-NN trained offline on 14x14 MNIST; each weight is a difference G+ - G- of two 1T1R devices, giving 19 weight levels, and 10 level combinations (C1-C10) trade variability against conductance magnitude. Accuracy, array current and IR-drop (32x32 tiles, wire resistance 0-3 ohm) are evaluated. Higher conductance combinations are more precise but draw about 5x more current and suffer more IR drop.

## Contributions
- Measured side-by-side comparison of ISPVA, IGVVA-100 and IGVVA-10 MLC programming on a 4-kbit 1T1R HfO2 array, including post-programming relaxation (AS vs EA)
- Shows gate-voltage control with fine steps yields shallow conductance-vs-pulse slopes and the lowest D2D variability, at a pulse-count cost
- System-level study of FC-NN accuracy versus weight levels, weight-mapping combination, hidden-layer size and IR drop
- Quantifies accuracy / current / area tradeoffs of conductance-level selection for differential weight encoding

## Key claims (stable IDs)
- **2021_Milo_RRAMProgramVerify_TED#C1** — IGVVA-10 gives the lowest device-to-device conductance variability among the three schemes — _support:_ Measured CDFs for AS and EA; ordering IGVVA-10 < ISPVA < IGVVA-100 — _loc:_ Sec. III, Fig. 4
- **2021_Milo_RRAMProgramVerify_TED#C2** — Best weight mapping reaches near-software accuracy — _support:_ 96.58% (C10) vs 96.77% FP-64 on MNIST (14x14) — _loc:_ Sec. V, Fig. 8(a)
- **2021_Milo_RRAMProgramVerify_TED#C3** — Accuracy-power tradeoff: highest-precision mapping consumes ~5x the current of C1 — _support:_ max current at C10 about 5x C1 — _loc:_ Fig. 8(b)
- **2021_Milo_RRAMProgramVerify_TED#C4** — Larger networks gain accuracy with 19 weight levels — _support:_ 92% (NH=20) to 96.2% (NH=100) — _loc:_ Fig. 10(b)

## Results
- ISPVA shows abrupt conductance jumps near Vset ~0.9 V; IGVVA gives gradual increase (Fig. 2)
- IGVVA-10 requires 121 pulses vs 16 for ISPVA: precision-vs-programming-time tradeoff
- Conductance relaxation between AS and EA lowers some cells below target but has only ~0.15% effect on FC-NN accuracy (Fig. 8)
- FC-NN accuracy rises as weight levels increase from 9 to 19; IGVVA-10 gives best improvement (Fig. 9a)
- IR drop reduces accuracy with r from 0 to 3 ohm in 32x32 tiles, worse for higher-conductance combinations and larger arrays (Fig. 8c,d)

## Key numbers
- tech_node: 0.25um CMOS (1T1R test array)
- array_size: 64x64 (4 kbit); 32x32 tiles for IR-drop study
- accuracy: 96.58% MNIST (C10, 19 levels, NH=100) vs 96.77% FP-64
- bits_weight: 19 differential levels (9 device levels)

## Datasets / benchmarks
MNIST (14x14 downsampled)

## Limitations
- Network inference is calculated (simulation using measured CDFs), not executed on the array
- Tiny network (197-20/100-10, 14x14 MNIST) and 0.25 um CMOS test chip
- Conductance drift and RTN are not measured over time beyond AS-to-EA relaxation
- Programming time / energy of IGVVA-10 (121 pulses per device) not quantified for large arrays
- Differential encoding doubles devices; wires modelled with simple uniform resistance

## Remarks
Well-grounded device-to-system evidence that MLC programming protocol, not just the device, sets achievable analog precision, and that high-conductance (more precise) levels collide with IR drop and power. The workload is trivial, so conclusions mostly inform write-verify and level-selection choices for larger models; for language models with wide dynamic range weights, the cost of many-pulse write-verify would be much larger. It complements chip papers in the collection (e.g. Xue et al.) that note MLC variation as a limiter.

## Cites (in collection, 8)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _uses-method-or-tool_: "Namely by encoding the weight as the difference of two 1T1R conductances G+ and G- [3]."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "A major advantage of IMC is the capability to execute matrix-vector multiplication (MVM) in parallel on multiple rows and columns of a memory array, which allows for a strong acceleration of neural networks [3]-[7]."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "A major advantage of IMC is the capability to execute matrix-vector multiplication (MVM) in parallel on multiple rows and columns of a memory array, which allows for a strong acceleration of neural networks [3]-[7]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "The recent demonstration of embedded RRAM devices at Mbit capacity [8] enables the design and integration of IMC circuits [9]-[11], thus paving the way for energy efficient RRAM-based accelerators of artificial intelligence (AI)."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "Fig. 1. (b) Multilevel I - V characteristics of 1T1R RRAM device measured for increasing VG. [2]."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _background_: "The recent demonstration of embedded RRAM devices at Mbit capacity [8] enables the design and integration of IMC circuits [9]-[11], thus paving the way for energy efficient RRAM-based accelerators of artificial intelligence (AI)."
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021) — _motivation_: "However, partial reset was shown to lead to higher conductance variation compared to gradual set [30], suggesting that combined algorithms based on partial set/reset pulses need further studies."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "The recent demonstration of embedded RRAM devices at Mbit capacity [8] enables the design and integration of IMC circuits [9]-[11], thus paving the way for energy efficient RRAM-based accelerators of artificial intelligence (AI)."

## Cited by (in collection, 2)
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "Previous studies have indicated that incremental steps in write voltage pulse amplitude, particularly via the word line84,85, offer superior efficiency compared with incremental steps in pulse width86."
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2021_Milo_RRAMProgramVerify_TED.pdf](../../06_Nonidealities_and_Reliability/2021_Milo_RRAMProgramVerify_TED.pdf)
- Full text: [../fulltext/2021_Milo_RRAMProgramVerify_TED.txt](../fulltext/2021_Milo_RRAMProgramVerify_TED.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/ted.2021.3089995
