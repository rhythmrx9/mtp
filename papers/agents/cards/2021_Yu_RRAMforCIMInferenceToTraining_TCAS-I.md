---
id: W3155456425
key: 2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I
title: "RRAM for Compute-in-Memory: From Inference to Training"
short: "RRAM for CIM: Inference to Training"
year: 2021
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 68, no. 7, pp. 2753-2765 (2021)"
authors: "Shimeng Yu, Wonbo Shim, Xiaochen Peng, Yandong Luo"
category: "01 Surveys & Foundations"
devices: ["ReRAM", "Charge/Capacitor"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["survey", "on-chip-training", "device-variation", "3d-integration", "benchmarking"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 17
citations_overall: 141
priority_score: 7.34
doi: "https://doi.org/10.1109/tcsi.2021.3072200"
pdf: null
fulltext: null
---

# RRAM for CIM: Inference to Training

**RRAM for Compute-in-Memory: From Inference to Training** — IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 68, no. 7, pp. 2753-2765 (2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Review of RRAM-based CIM that adds measured multilevel RRAM data from a test vehicle, a scalability/monolithic-3D benchmark of RRAM CIM inference, and a hybrid-precision RRAM+capacitor synapse for in-situ training evaluated at system level.

## Summary
Targeting edge ML, the paper reviews RRAM-based compute-in-memory accelerators and their instant-on, non-volatile benefits. First, multilevel RRAM characteristics are measured on a test vehicle to assess key device properties for inference. Second, a benchmark (NeuroSim-based) studies the scalability of RRAM CIM inference engines and the feasibility of monolithic 3D integration of RRAM arrays above advanced logic nodes. Third, it presents the grand challenges for in-situ training on RRAM and proposes a hybrid-precision synapse combining RRAM with a volatile capacitor-based memory to enable fast, accurate in-situ training followed by inference, evaluated at system level. Abstract-only basis; numbers not reproduced.

## Contributions
- Measurement of multilevel RRAM states from a test vehicle for inference-relevant properties.
- System-level benchmark of RRAM CIM scalability and monolithic 3D (RRAM-on-logic) integration.
- Analysis of grand challenges for in-situ training on RRAM.
- Hybrid-precision RRAM + capacitor synapse design and system-level evaluation for training then inference.

## Key claims (stable IDs)
- **2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I#C1** — RRAM enables instant-on CIM inference at the edge with improved throughput and energy efficiency. — _support:_ Abstract: 'Instant-on inference is further enabled by emerging non-volatile memory technologies such as RRAM'. — _loc:_ Abstract
- **2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I#C2** — Monolithic 3D stacking of RRAM arrays on advanced logic is feasible for CIM inference engines. — _support:_ Abstract: benchmark studies 'feasibility towards monolithic 3D integration that stacks RRAM arrays on top of advanced logic process node'. — _loc:_ Abstract
- **2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I#C3** — A hybrid precision synapse (RRAM + capacitor) supports accurate and fast in-situ training and subsequent inference on one platform. — _support:_ Abstract describes design and system-level evaluation of this synapse. — _loc:_ Abstract

## Results
- Quantitative results not extracted (abstract-only basis).

## Limitations
- Full text not accessed; measured and benchmarked numbers not verified.
- Benchmarks rely on NeuroSim models rather than full silicon.
- Capacitor-based volatile weights need refresh/transfer overhead (typical of hybrid-precision schemes).

## Remarks
Represents the Georgia Tech/NeuroSim view that RRAM is ready for inference but training needs hybrid volatile/non-volatile synapses, echoing IBM's PCM+capacitor 3T1C work (Ambrogio 2018). Useful for M3D and scaling arguments, but its numbers come from the authors' simulator.

## Cites (in collection, 17)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)

## Cited by (in collection, 5)
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _data/numbers_: "According to [66], a WS system with TaOx/HfOx RRAM shows an 11% accuracy drop in VGG8 on CIFAR10 when compared to GPU with floating-point arithmetic."
- [2024_Chowdhury_MELISO_ICONS](2024_Chowdhury_MELISO_ICONS.md) MELISO (2024) — _background_: "This mechanism underscores the computational efficiency inherent in the RRAM crossbar design for implementing VMM operations, with improved energy efficiency and reduced latency metrics [8-16]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _data/numbers_: "Specifically, the RRAM features an on-state resistance (RON) of 6 kΩ with an on/off ratio of 150 [77]."
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2024_Ahsan_SPICEenvmACIMFramework_ICCAD](2024_Ahsan_SPICEenvmACIMFramework_ICCAD.md) SPICE eNVM ACIM Framework (2024)

## Files
- PDF: not available locally (save as `papers/01_Surveys_and_Foundations/2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcsi.2021.3072200
