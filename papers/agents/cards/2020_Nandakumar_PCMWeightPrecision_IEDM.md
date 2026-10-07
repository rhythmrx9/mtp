---
id: W3138725418
key: 2020_Nandakumar_PCMWeightPrecision_IEDM
title: "Precision of synaptic weights programmed in phase-change memory devices for deep learning inference"
short: "PCM Weight Precision"
year: 2020
venue: "IEDM"
venue_full: "2020 IEEE International Electron Devices Meeting (IEDM 2020)"
authors: "S. R. Nandakumar, Irem Boybat, Jin‐Ping Han, Stefano Ambrogio, Praneet Adusumilli, Robert L. Bruce, Matthew J. BrightSky, Malte J. Rasch, Manuel Le Gallo, Abu Sebastian"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["PCM"]
models: ["CNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["write-verify-programming", "device-variation", "conductance-drift", "read-write-noise"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 10
cites_in_collection: 3
citations_overall: 35
priority_score: 6.71
doi: "https://doi.org/10.1109/iedm13553.2020.9371990"
pdf: null
fulltext: null
---

# PCM Weight Precision

**Precision of synaptic weights programmed in phase-change memory devices for deep learning inference** — 2020 IEEE International Electron Devices Meeting (IEDM 2020) (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Derives analytically that the precision achievable when iteratively programming PCM conductance states with closed-loop feedback is fundamentally limited by read noise, validates this against measurements on >1k doped-GST PCM device arrays, and shows that tuning the feedback timing improves deep-learning inference accuracy retention on CIFAR-10, CIFAR-100 and PTB.

## Summary
The paper (from IBM Research, including Sebastian/Le Gallo/Ambrogio and collaborators) studies the precision with which synaptic weights can be programmed into phase-change memory (PCM) conductance states using iterative program-verify with closed-loop feedback, the standard approach for achieving target conductance values in analog in-memory computing. The authors analytically derive the programming-noise precision limit, showing it is fundamentally set by the PCM cell's read noise, and quantitatively match this prediction against measurements on more than 1,000 PCM devices across two doped-GST phase-change material variants. They further show that conductance drift causes the programmed state to diverge over time in a way that depends on when (how late) feedback was applied during programming, and that tuning this feedback-timing parameter yields significant improvements in deep-learning inference accuracy retention over time on CIFAR-10, CIFAR-100 and Penn Treebank (PTB) benchmarks run on PCM-based DNN inference hardware simulations.

## Contributions
- An analytical derivation of the programming precision limit for iterative closed-loop program-verify schemes on PCM, showing it is fundamentally bounded by read noise
- Experimental validation of this precision model on >1000 PCM devices spanning two doped-GST phase-change materials
- Demonstration that conductance-drift-driven divergence of programmed states depends on the timing of the last feedback step during iterative programming
- Practical demonstration that tuning feedback timing significantly improves long-term inference accuracy retention for CNNs (CIFAR-10/100) and sequence models (PTB) run on PCM-based inference hardware

## Key claims (stable IDs)
- **2020_Nandakumar_PCMWeightPrecision_IEDM#C1** — The precision of iteratively programmed PCM conductance states is fundamentally limited by the device's read noise — _support:_ analytical derivation matched quantitatively to measurements on >1k PCM device arrays — _loc:_ Abstract / analytical section
- **2020_Nandakumar_PCMWeightPrecision_IEDM#C2** — Conductance-drift-driven divergence of the programmed state depends on the time of the last feedback step in the iterative programming process — _support:_ stated analysis in the abstract — _loc:_ Abstract
- **2020_Nandakumar_PCMWeightPrecision_IEDM#C3** — Tuning the feedback timing yields significant accuracy-retention improvements for deep learning inference on PCM-based hardware — _support:_ demonstrated on CIFAR-10, CIFAR-100, and PTB benchmarks — _loc:_ Abstract

## Results
- Analytically derived programming-noise precision model quantitatively matches measurements across >1,000 PCM devices (two doped-GST variants)
- Significant accuracy-retention improvements reported on CIFAR-10, CIFAR-100, and PTB when feedback timing is tuned (specific percentage figures not given in the abstract)

## Limitations
- Full text not available to this review; the quantitative magnitude of the accuracy-retention improvements and the exact feedback-timing parameter values were not disclosed in the abstract
- Analysis based only on the abstract; details of the inference hardware simulation setup and dataset-specific network architectures are unknown from the abstract alone

## Remarks
This is a well-cited (35+ citations) IBM Research paper that gives a rigorous, device-physics-grounded explanation (read-noise-limited programming precision) for a key practical knob -- feedback timing in iterative program-verify -- that is widely used across PCM-based in-memory computing work, and it is cited by several later PCM accelerator and drift-mitigation papers in this collection (HERMES-Core, Optimised weight programming, drift-aware regularization work). Because full text was not accessible (IEDM proceedings not downloadable from this environment), this entry is abstract-only and specific numeric accuracy-retention results could not be captured.

## Cites (in collection, 3)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)

## Cited by (in collection, 10)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "The analog nature of the device, however, allows the encoding of more levels, the only limit being ADC precision and allowable programming time [35], [36]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _uses-method-or-tool_: "We have previously employed this weight programming time-scale as an effective compromise between conductance stability and programming speed for the programming of millions of weights40."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "Despite the reduced precision weights, AIMC implementations were shown to address the inference of MLPs [30, 31], CNNs [16, 30, 31], RNNs [19, 30, 31], and transformers [20] with high accuracies."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _contrasts/critiques_: "However, the toolkit currently does not natively support a bit-wise ”digital” mapping of weights, where only 1 and 0 states are (approximately) represented by conductances, and multiple devices are used with different significances to approximate a digital MVM19 ."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _background_: "Early work on Analog CIM accelerators mostly focus on the precision of weight-programming [3], [22], [23], which provides a mutual understanding of Analog CIM working mechanism and robust on-tile data storage."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _background_: "Similar to any other analog NVMs [19-21], PCM has its intrinsic nonidealities, such as read noise [12, 22, 23], device-to-device variations [24], conductance drift over time after programing [13, 25, 26], limited memory window [17, 27], which can adversely affect DNN inference accuracy."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "Static weight noise (does not get resampled during inference) is mainly due to programming noise, which is the conductance error from the target weight that remains after a device has been programmed with an iterative read-write-verify programming scheme [27]."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2020_Nandakumar_PCMWeightPrecision_IEDM.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iedm13553.2020.9371990
