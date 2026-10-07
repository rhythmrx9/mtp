---
id: W3016048022
key: 2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC
title: "33.1 A 74 TMACS/W CMOS-RRAM Neurosynaptic Core with Dynamically Reconfigurable Dataflow and In-situ Transposable Weights for Probabilistic Graphical Models"
short: "Transposable RRAM Neurosynaptic Core"
year: 2020
venue: "ISSCC"
venue_full: "2020 IEEE International Solid-State Circuits Conference (ISSCC), paper 33.1"
authors: "Weier Wan, Rajkumar Chinnakonda Kubendran, Sukru Burc Eryilmaz, Wenqiang Zhang, Yan Biao Liao, Dabin Wu, Stephen R. Deiss, Bin Gao, Priyanka Raina, Siddharth Joshi, Huaqiang Wu, Gert Cauwenberghs et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["PGM", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "dataflow-pipelining", "recurrent-models", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 10
cites_in_collection: 2
citations_overall: 141
priority_score: 8.72
doi: "https://doi.org/10.1109/isscc19947.2020.9062979"
pdf: null
fulltext: null
---

# Transposable RRAM Neurosynaptic Core

**33.1 A 74 TMACS/W CMOS-RRAM Neurosynaptic Core with Dynamically Reconfigurable Dataflow and In-situ Transposable Weights for Probabilistic Graphical Models** — 2020 IEEE International Solid-State Circuits Conference (ISSCC), paper 33.1 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A 130-nm CMOS/RRAM CIM core with runtime-reconfigurable dataflow and in-situ transposable weight access, reaching 74 TMACS/W, the highest reported for RRAM CIM at the time, aimed at probabilistic graphical models.

## Summary
Models such as probabilistic graphical models (e.g., RBMs) and RNNs need both forward and transposed weight access and flexible dataflow. Typical CIM designs either lack this or duplicate ADCs/neurons on both rows and columns. This Stanford/UCSD/Tsinghua core in 130-nm CMOS/RRAM lets the same RRAM array be read in either direction through a reconfigurable dataflow. It uses a voltage-sensing stochastic integrate-and-fire analog neuron that is reused for correlated double sampling, stochastic voltage integration and threshold comparison, which avoids replicated periphery. The design reports 74 TMACS/W computational efficiency. It is a precursor of the NeuRRAM chip.

## Contributions
- Runtime-reconfigurable dataflow with in-situ access to the RRAM array and its transpose
- Voltage-sensing stochastic integrate-and-fire neuron reused for CDS, integration and comparison
- Highest reported RRAM-CIM computational efficiency at the time (74 TMACS/W)

## Key claims (stable IDs)
- **2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC#C1** — Transposable access can be supported without duplicating ADC/neuron periphery on rows and columns. — _support:_ Reconfigurable dataflow plus shared analog neuron — _loc:_ Abstract
- **2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC#C2** — The core has the highest computational energy efficiency reported for RRAM CIM. — _support:_ 74 TMACS/W — _loc:_ Abstract

## Results
- 130-nm CMOS/RRAM core
- 74 TMACS/W computational energy efficiency

## Limitations
- Abstract-only analysis. Benchmark accuracy and workload details were not verified
- Old 130-nm node and small array scale
- Efficiency counts computation only and excludes system I/O

## Remarks
This is the direct predecessor of the NeuRRAM chip (Wan et al., Nature 2022). Its transposable neurosynaptic array (TNSA) and voltage-mode neuron ideas went into that chip. For mapping, it shows that bidirectional crossbar reads support backprop-like and PGM sampling dataflows at low periphery cost, which matters for RNNs and on-chip learning.

## Cites (in collection, 2)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)

## Cited by (in collection, 10)
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _background_: "Multi-Bit Multiplication in ReRAM-Based PIM Although the analog nature of ReRAM allows it to store a multi-bit weight for improved memory capacity [34, 35], Fig. 10."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "Most commonly, CiM systems keep DNN weights in memory because they do not change during DNN inference [2, 18, 20, 29]."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _data/numbers_: "The noise level was derived from the studies by Wan et al. [61] and Fan et al. [15], utilizing the non-idealities measured from the fabricated real MLC RRAM chips."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)

## Files
- PDF: not available locally (save as `papers/02_Fabricated_Chips_and_Macros/2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/isscc19947.2020.9062979
