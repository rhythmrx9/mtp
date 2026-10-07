---
id: W4321488325
key: 2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED
title: "Experimental Assessment of Multilevel RRAM-Based Vector-Matrix Multiplication Operations for In-Memory Computing"
short: "Multilevel-RRAM-VMM-Assessment"
year: 2023
venue: "TED"
venue_full: "IEEE Transactions on Electron Devices (2023)"
authors: "Emilio Pérez-Bosch Quesada, Mamathamba Kalishettyhalli Mahadevaiah, Tommaso Rizzi, Jianan Wen, Markus Ulbricht, Milos D. Krstic, Christian Wenger, Eduardo Pérez"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: []
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["device-variation", "read-write-noise", "analog-mvm", "endurance-retention"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 7
citations_overall: 21
priority_score: 4.84
doi: "https://doi.org/10.1109/ted.2023.3244509"
pdf: null
fulltext: null
---

# Multilevel-RRAM-VMM-Assessment

**Experimental Assessment of Multilevel RRAM-Based Vector-Matrix Multiplication Operations for In-Memory Computing** — IEEE Transactions on Electron Devices (2023) (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Programs two 8x8 1T1R RRAM subarrays with different conductance-level distributions and subjects them to 1000 consecutive identical vector-matrix-multiplication operations, quantifying the accuracy loss and robustness-vs-linearity trade-off of multilevel RRAM conductance states for in-memory computing.

## Summary
RRAM-based hardware accelerators rely on vector-matrix multiplication (VMM) operations whose accuracy is challenged by the stochastic, nonideal nature of RRAM devices. The authors programmed two 8x8 one-transistor-one-resistor (1T1R) RRAM subarrays using two different distributions of conductance levels and then repeated the same VMM operation 1000 times consecutively on each subarray, monitoring the devices' inherent nonidealities throughout the test. They quantify the resulting accuracy loss of the VMM operations once digitized, and examine the trade-off between using a linearly spaced distribution of resistive states (for programming simplicity/predictability) versus robustness against the devices' nonideal behavior, aiming to inform future RRAM-based in-memory-computing hardware design.

## Contributions
- Direct experimental characterization of two different conductance-level distribution strategies in real 1T1R RRAM subarrays for multilevel VMM operations
- Repeated (1000x) consecutive identical VMM operation testing to quantify accuracy degradation and device nonideality drift over repeated use
- Quantitative comparison of the trade-off between linearly distributed resistive states and robustness to RRAM nonidealities for future IMC hardware design

## Key claims (stable IDs)
- **2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED#C1** — Consecutive repeated VMM operations on programmed multilevel RRAM subarrays accumulate measurable accuracy loss due to device nonidealities — _support:_ 1000 identical consecutive VMM operations performed on two 8x8 1T1R subarrays, with accuracy loss quantified in the digital domain after monitoring nonidealities throughout — _loc:_ Abstract
- **2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED#C2** — There is a trade-off between linearly distributing RRAM conductance levels and robustness against nonidealities — _support:_ comparison of two different conductance-level distributions across the 1000-operation robustness test — _loc:_ Abstract

## Results
- 1000 consecutive identical VMM operations characterized on two 8x8 1T1R RRAM subarrays with different conductance-level distributions
- Accuracy loss of VMM operations quantified in the digital domain after repeated operation (specific accuracy percentages not given in the abstract)

## Limitations
- This entry is based on the abstract only (no full text or PDF was located); specific accuracy-loss numbers, the exact conductance-level distributions tested, and the digitization/readout methodology are not confirmed here
- Experiments are limited to small 8x8 subarrays, which may not capture nonideality effects (e.g., IR drop, sneak paths) that scale with larger array sizes
- No neural-network-level (end-to-end DNN accuracy) evaluation is indicated in the abstract; this is a device/circuit-level VMM characterization study

## Remarks
This is a device-experiment paper providing direct, repeated-operation hardware characterization of multilevel RRAM VMM accuracy and the linearity-vs-robustness trade-off, which is useful ground-truth evidence for the many simulation-based mapping and non-ideality papers in this collection that assume particular RRAM conductance distributions. Being limited to small 8x8 subarrays and (per the abstract) to VMM-level rather than full DNN-level accuracy, its main contribution is characterizing device behavior rather than demonstrating a complete accelerator or mapping method; a later paper in this collection ('The Lynchpin of In-Memory Computing: A Benchmarking Framework for Vector-Matrix Multiplication in RRAMs') is listed as building on it.

## Cites (in collection, 7)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 1)
- [2024_Chowdhury_MELISO_ICONS](2024_Chowdhury_MELISO_ICONS.md) MELISO (2024) — _background_: "This mechanism underscores the computational efficiency inherent in the RRAM crossbar design for implementing VMM operations, with improved energy efficiency and reduced latency metrics [8-16]."

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/ted.2023.3244509
