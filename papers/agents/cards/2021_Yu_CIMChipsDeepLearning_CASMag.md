---
id: W3194056411
key: 2021_Yu_CIMChipsDeepLearning_CASMag
title: "Compute-in-Memory Chips for Deep Learning: Recent Trends and Prospects"
short: "CIM Chips for Deep Learning"
year: 2021
venue: "CASMag"
venue_full: "IEEE Circuits and Systems Magazine, vol. 21, no. 3, pp. 31-56 (2021)"
authors: "Shimeng Yu, Hongwu Jiang, Shanshi Huang, Xiaochen Peng, Anni Lu"
category: "01 Surveys & Foundations"
devices: ["SRAM-analog", "ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "analog-mvm", "macro", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 12
cites_in_collection: 20
citations_overall: 393
priority_score: 8.65
doi: "https://doi.org/10.1109/mcas.2021.3092533"
pdf: null
fulltext: null
---

# CIM Chips for Deep Learning

**Compute-in-Memory Chips for Deep Learning: Recent Trends and Prospects** — IEEE Circuits and Systems Magazine, vol. 21, no. 3, pp. 31-56 (2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Review of silicon-demonstrated SRAM- and RRAM-based CIM macros for DNNs, their common design challenges (ADC bottleneck, analog variation, device non-idealities), and the DNN+NeuroSim framework for device-to-system co-design of CIM inference and training.

## Summary
CIM performs DNN multiply-and-accumulate in the analog domain within memory sub-arrays to address the memory wall. The review first surveys recent SRAM and RRAM CIM macros demonstrated in silicon (e.g., ISSCC/VLSI macros). It then discusses general CIM chip challenges: the analog-to-digital conversion bottleneck, variations in analog computation, and device non-idealities. Finally, it introduces the DNN+NeuroSim benchmark framework for evaluating device technologies in CIM inference and training from a software/hardware co-design perspective. Abstract-only basis; specific macro metrics not reproduced.

## Contributions
- Survey of measured SRAM and RRAM CIM macros in silicon.
- Discussion of ADC bottleneck, analog variation and device non-idealities as cross-cutting CIM challenges.
- Tutorial-style introduction to DNN+NeuroSim for device-to-system CIM benchmarking.

## Key claims (stable IDs)
- **2021_Yu_CIMChipsDeepLearning_CASMag#C1** — Performing MACs in the analog domain inside memory sub-arrays yields significant throughput and energy-efficiency improvements. — _support:_ Abstract states this as the motivating premise of CIM. — _loc:_ Abstract
- **2021_Yu_CIMChipsDeepLearning_CASMag#C2** — ADC conversion is a key bottleneck of CIM chips, together with analog-compute variation and device non-idealities. — _support:_ Abstract: 'general design challenges of the CIM chips including analog-to-digital conversion (ADC) bottleneck, variations in analog compute, and device non-idealities'. — _loc:_ Abstract
- **2021_Yu_CIMChipsDeepLearning_CASMag#C3** — DNN+NeuroSim can evaluate versatile device technologies for CIM inference and training. — _support:_ Abstract: 'DNN+NeuroSim benchmark framework that is capable of evaluating versatile device technologies for CIM inference and training'. — _loc:_ Abstract

## Results
- Quantitative macro comparisons not extracted (abstract-only basis).

## Limitations
- Full text not accessed; macro metrics (TOPS/W, precision) not verified.
- Benchmarking relies on the authors' own NeuroSim framework.
- CNN-centric; no Transformer workloads.

## Remarks
A good 2021 snapshot of measured SRAM/RRAM CIM macros and the peripheral (ADC) problem, useful for situating analog crossbar accelerators against silicon reality. Pair with Sebastian et al. 2020 for device breadth and with NeuroSim papers (Peng et al.) for methodology.

## Cites (in collection, 20)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Jiang_MINT_ISCAS](2020_Jiang_MINT_ISCAS.md) MINT (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 12)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "In situ MVM has been demonstrated using a wide variety of memory cell technologies [55, 61, 68]."
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _background_: "ReRAM-based PIM has become increasingly attractive in energy-efficient accelerators for edge computing where batteries or energy harvesting devices are the primary power sources [29–36]."
- [2022_Lin_DNAT_JETCAS](2022_Lin_DNAT_JETCAS.md) D-NAT (2022) — _uses-method-or-tool_: "On the other hand, to develop the A-MAC-EM for the target SRAM-based CIM macro, we assume the variation mainly occurs in ADC and DAC [28]."
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _background_: "In recent years, analog in memory compute (AIMC) arrays have attracted much attention in the accelerator design [3]."
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _motivation_: "Moreover, a further challenge is the fabricable size of nvIMC devices, which de-facto is limited to 1024×1024 with up to 8-bit equivalent memory cells [4]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "In addition to traditional digital accelerators, including the Google Tensor Processing Unit, Amazon Inferentia, and IBM Artificial Intelligence Unit1 , accelerators based on Analog In-Memory Computing (AIMC) using Non-Volatile Memory (NVM) are being actively researched2–4 ."
- [2022_Wen_RRAMReadDisturb_DFT](2022_Wen_RRAMReadDisturb_DFT.md) RRAM Read Disturb (2022)
- [2022_Jiang_ENNA_TCAS-I](2022_Jiang_ENNA_TCAS-I.md) ENNA (2022)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Ahsan_SPICEenvmACIMFramework_ICCAD](2024_Ahsan_SPICEenvmACIMFramework_ICCAD.md) SPICE eNVM ACIM Framework (2024)

## Files
- PDF: not available locally (save as `papers/01_Surveys_and_Foundations/2021_Yu_CIMChipsDeepLearning_CASMag.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/mcas.2021.3092533
