---
id: W4225739994
key: 2022_Kim_PIMCircuitsOverview_JETCAS
title: "An Overview of Processing-in-Memory Circuits for Artificial Intelligence and Machine Learning"
short: "PIM Circuits Overview"
year: 2022
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems, vol. 12, no. 2, pp. 338-353, June 2022"
authors: "Donghyuk Kim, Chengshuo Yu, Shanshan Xie, Yuzong Chen, Joo-Young Kim, Bongjin Kim, Jaydeep P. Kulkarni, Tony Tae-Hyoung Kim"
category: "01 Surveys & Foundations"
devices: ["SRAM-analog", "SRAM-digital", "DRAM", "ReRAM", "Charge/Capacitor"]
models: ["CNN", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "macro", "peripheral-circuits", "adc-dac", "analog-mvm", "bit-slicing", "energy-efficiency", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 7
citations_overall: 85
priority_score: 5.76
doi: "https://doi.org/10.1109/jetcas.2022.3160455"
pdf: "../../01_Surveys_and_Foundations/2022_Kim_PIMCircuitsOverview_JETCAS.pdf"
fulltext: "../fulltext/2022_Kim_PIMCircuitsOverview_JETCAS.txt"
---

# PIM Circuits Overview

**An Overview of Processing-in-Memory Circuits for Artificial Intelligence and Machine Learning** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems, vol. 12, no. 2, pp. 338-353, June 2022 (2022)

## TL;DR
JETCAS overview of SRAM-, DRAM- and ReRAM-based processing-in-memory circuits for AI, highlighting that data converters dominate ReRAM PIM cost (ADCs 61% of power and 91% of area at 8b output in a 1152x128 macro) and that CIFAR-10 CIM demos reach 80.1-92.52% accuracy.

## Summary
The article motivates PIM as a remedy for the von-Neumann memory wall in MAC-dominated neural networks and reviews state-of-the-art PIM by memory type. Section II covers analog and digital SRAM PIM (Table I), Section III DRAM PIM (bank-level, 3-D HMC-based such as Neurocube, Tetris, iPIM; Table II), and Section IV ReRAM PIM. For ReRAM it explains current-mode sensing, why most macros use digital (binary HRS/LRS) cells, multi-bit MAC via Parallel-Input-Parallel-Weight vs Serial-Input-Parallel-Weight, ternary weights using positive/negative arrays (Table III), and design challenges (ADC/DAC overhead, bit-line current overlap from device variation). Table IV summarises ReRAM PIM prototypes. Section V discusses the PIM software stack (offloading, data mapping, scheduling, cache coherence), and Section VI lists open directions: data-converter overhead (Table V), test accuracy (Table VI), and intra-memory data movement (im2col duplication). Evaluation is purely literature-based tabulation.

## Contributions
- Unified circuit-level survey across SRAM, DRAM and ReRAM PIM
- Comparison tables of SRAM PIMs, DRAM PIMs, ReRAM MAC prototypes, data converters, and reported CIM test accuracy
- Discussion of the PIM software stack challenges
- Identification of three open problems: data-converter overhead, accuracy, intra-memory data movement

## Key claims (stable IDs)
- **2022_Kim_PIMCircuitsOverview_JETCAS#C1** — ADCs and DACs dominate ReRAM PIM macro cost — _support:_ 1152x128 array with 2b DACs and 8b ADCs: DACs 24% and ADCs 61% of power; ADCs 91% of area at 8b output — _loc:_ Sec. IV-D1
- **2022_Kim_PIMCircuitsOverview_JETCAS#C2** — Most ReRAM PIM works use digital (two-state) ReRAM because of device variation — _support:_ 'Digital ReRAM is more preferred compared with analog ReRAM due to large ReRAM device variations' — _loc:_ Sec. IV-E
- **2022_Kim_PIMCircuitsOverview_JETCAS#C3** — Reported CIM CIFAR-10 accuracy lies in 80.1-92.52%, with 0.55-1.39% drop from software — _support:_ Table VI summary — _loc:_ Sec. VI-B, Table VI
- **2022_Kim_PIMCircuitsOverview_JETCAS#C4** — Binary NN PIM suffers about 3% accuracy loss on CIFAR-10 — _support:_ 'BNNs ... suffer a 3% accuracy loss on the CIFAR-10 dataset' — _loc:_ Sec. VI-B
- **2022_Kim_PIMCircuitsOverview_JETCAS#C5** — Retraining recovers accuracy lost to analog nonlinearity in an SRAM CIM — _support:_ 90.3% (81.6% uncalibrated) to 91.6% (86.2%) after 3 epochs vs 91.9% software — _loc:_ Sec. VI-B

## Results
- MNIST CIM test accuracy range 97%-99.63%; CIFAR-10 80.1%-92.52% (Table VI)
- ReRAM macro cost breakdown: DAC 24% / ADC 61% of power, ADC 91% of area at 8b (Sec. IV-D1, from the 78.4 TOPS/W chip)
- Bit-line current for MAC value +1 ranges from 1 I_LRS to 1 I_LRS + 8 I_HRS in a 9-WL ternary macro, shrinking sensing margin (Sec. IV-D2)

## Key numbers
- array_size: 1152x128 (cited ReRAM macro)
- accuracy: 97-99.63% MNIST; 80.1-92.52% CIFAR-10 (range over cited CIM demos)
- bits_adc: 8b (breakdown example)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Survey only; tables are literature compilations, extracted table contents are partly unreadable
- Models considered are CNN/MLP; no transformers or language models
- Software-stack section is DRAM/HBM-PIM-centred and does not cover analog crossbar mapping or noise
- Little coverage of analog multi-level ReRAM/PCM

## Remarks
A compact circuit-designer primer that explains why fabricated ReRAM macros favour binary cells, current-mode sensing and bit-serial inputs, and why ADC cost is the main bottleneck. Its ADC breakdown (from the Liu et al. ISSCC'20 chip) is a convenient motivation for ADC-reduction work. Not helpful for LM-on-AIMC mapping beyond background.

## Cites (in collection, 7)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _background_: "Reference [53] proposes an optimized weight mapping and dataflow in computing convolutional neural networks on ReRAM-based PIM."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "Hence, most ReRAM PIM works are based on current-mode sensing [34, 41–44]."
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020) — _background_: "Multi-Bit Multiplication in ReRAM-Based PIM Although the analog nature of ReRAM allows it to store a multi-bit weight for improved memory capacity [34, 35], Fig. 10."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _background_: "ReRAM-based PIM has become increasingly attractive in energy-efficient accelerators for edge computing where batteries or energy harvesting devices are the primary power sources [29–36]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "Various MAC strategies have been reported to address this challenge [41–44]."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _uses-method-or-tool_: "In general, for PIM architectures based on digital ReRAM, the multiplication of multi-bit inputs and weights can be implemented in two different ways named ‘Parallel-Input-Parallel-Weight (PIPW)’ and ‘Serial-Input-Parallel-Weight (SIPW)’ [42]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Various MAC strategies have been reported to address this challenge [41–44]."

## Cited by (in collection, 1)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)

## Files
- PDF: [../../01_Surveys_and_Foundations/2022_Kim_PIMCircuitsOverview_JETCAS.pdf](../../01_Surveys_and_Foundations/2022_Kim_PIMCircuitsOverview_JETCAS.pdf)
- Full text: [../fulltext/2022_Kim_PIMCircuitsOverview_JETCAS.txt](../fulltext/2022_Kim_PIMCircuitsOverview_JETCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jetcas.2022.3160455
