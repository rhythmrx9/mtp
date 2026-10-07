---
id: W3015982917
key: 2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC
title: "33.2 A Fully Integrated Analog ReRAM Based 78.4TOPS/W Compute-In-Memory Chip with Fully Parallel MAC Computing"
short: "Liu ISSCC'20 Analog ReRAM CIM"
year: 2020
venue: "ISSCC"
venue_full: "2020 IEEE International Solid-State Circuits Conference (ISSCC), paper 33.2"
authors: "Qi Liu, Bin Gao, Peng Yao, Dong Min Wu, Junren Chen, Yachuan Pang, Wenqiang Zhang, Yan Biao Liao, Cheng-Xin Xue, Wei-Hao Chen, Jianshi Tang, Yu Wang et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "adc-dac", "ir-drop-parasitics", "peripheral-circuits", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 20
cites_in_collection: 2
citations_overall: 305
priority_score: 9.8
doi: "https://doi.org/10.1109/isscc19947.2020.9062953"
pdf: "../../02_Fabricated_Chips_and_Macros/2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.pdf"
fulltext: "../fulltext/2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.txt"
---

# Liu ISSCC'20 Analog ReRAM CIM

**33.2 A Fully Integrated Analog ReRAM Based 78.4TOPS/W Compute-In-Memory Chip with Fully Parallel MAC Computing** — 2020 IEEE International Solid-State Circuits Conference (ISSCC), paper 33.2 (2020)

## TL;DR
A 130nm, 158.8kb analog ReRAM CIM chip runs a complete 784-100-10 MLP on-chip using a sign-weighted 2T2R array and a resolution-adjustable ramp ADC, reaching 94.4% MNIST, 77 us/image and 78.4 TOPS/W peak.

## Summary
Earlier ReRAM CIM demonstrations were single macros with limited parallelism, and IR drop plus transient errors and ADC/DAC interface power limit accuracy and parallelism. The chip implements a two-layer fully-connected network (784-100-10) with two arrays: a sign-weighted 2T2R (SW-2T2R) array and a 1T1R array. In SW-2T2R, positive and negative weights of a differential pair sit on the same source line (output column) and are driven with opposite polarity (VBLP = VCLP-VREAD, VBLN = VCLP+VREAD), so cell weight is GPOS-GNEG and currents cancel locally, lowering accumulated SL current and IR drop. Weights are signed quasi-2-bit (3-level) or quasi-3-bit (7-level) from intermediate device states, inputs are 1-bit per MAC. A low-power adjustable-resolution ADC (LPAR-ADC: integrator, comparator, segmented-capacitor DAC ramp) digitises SL currents and its output pulses feed the next array directly, with resolution set by sampling clock frequency; inference takes at least 2^(N1+N2) cycles. Testing uses an FPGA board plus host computer on a single chip, with accuracy measured on MNIST versus ADC resolution.

## Contributions
- First fully integrated analog ReRAM CIM chip running a complete multi-layer NN (claimed)
- SW-2T2R array that reduces IR drop and power versus 1T1R
- Resolution-adjustable LPAR-ADC trading accuracy against power and latency, with direct inter-array interface

## Key claims (stable IDs)
- **2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC#C1** — SW-2T2R reduces CIM power versus 1T1R on the same chip — _support:_ 1.9x lower power than 1T1R version — _loc:_ Fig. 33.2.5
- **2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC#C2** — Chip achieves 94.4% MNIST accuracy, 77 us/image and 78.4 TOPS/W peak — _support:_ Abstract and conclusion — _loc:_ Fig. 33.2.7 / conclusion
- **2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC#C3** — Accuracy increases with ADC resolution of both stages; speed with first-stage resolution — _support:_ 2b/8b ADC settings give ~92% accuracy at 77 us/image — _loc:_ Fig. 33.2.5

## Results
- MAC-OUT access time 51.1 ns at VDD=4.2V, VREAD=0.2V (Fig. 33.2.5)
- SW-2T2R power 1.9x lower than 1T1R on same chip (Fig. 33.2.5)
- 3-bit signed weights: measured 93.4% MNIST, ~2% below simulation (Fig. 33.2.6)
- Peak 78.4 TOPS/W, 77 us/image, 158.8kb ReRAM in 130nm CMOS (Fig. 33.2.7)

## Key numbers
- tech_node: 130nm
- array_size: 158.8kb ReRAM total (784-100-10 MLP)
- energy_eff: 78.4 TOPS/W peak
- throughput: 77 us/image
- accuracy: 94.4% MNIST (93.4% with 3-bit signed weights)
- bits_weight: quasi-2b/3b signed (3 or 7 levels)
- bits_adc: adjustable (e.g. 2b/8b)

## Datasets / benchmarks
MNIST

## Limitations
- MNIST-scale 2-layer MLP only; no CNN or sequence model
- 1-bit inputs, 2-3 bit weights, and slow ADC pulse-count readout
- Accuracy figures vary across text (94.4% abstract, 93.4% for 3-bit, ~92% at 2b/8b ADC) depending on configuration
- Digest paper: limited detail, figures not available in extracted text

## Remarks
A early, concise full-chip demonstration whose value is the SW-2T2R differential array for IR-drop mitigation and a flexible ADC; evidence is measured silicon but on a toy task. It illustrates the accuracy/latency/energy trade set by ADC resolution, which later scales to larger macros. Related to Chen ISSCC'18 and Xue ISSCC'19 macros in the collection; irrelevant directly to language models except as precursor.

## Cites (in collection, 2)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "To overcome the decreasing cost effectiveness of transistor scaling and the intrinsic inefficiency of data-shuttling in the von-Neumann architecture, CIM is proposed to realize high-speed and low-power system with parallel multiplication accumulation (MAC) computing [1][2]."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _contrasts/critiques_: "In the SW-2T2R array, the positive weight and negative weight in a differential device pair are connected on the same output column, which is different from Ref. [2] or [3]."

## Cited by (in collection, 20)
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "A Fully Integrated Analog ReRAM-based 130 nm macro used a 2T2R cell, which decreased the effect of the IR drop by decreasing the accumulative SL current [66]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _contrasts/critiques_: "In addition, voltage-based A/D converters (ADCs) are mostly used [31] that require a voltage to current conversion, usually employing a large capacitor for integration [23], [32]."
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _background_: "Hence, most ReRAM PIM works are based on current-mode sensing [34, 41–44]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _baseline/comparison_: "More recent studies have demonstrated fully integrated RRAM complementary metal–oxide–semiconductor (CMOS) chips capable of performing in-memory matrix-vector multiplication (MVM)6–17."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _extends/builds-on_: "RAELLA uses 2T2R devices, shown in Fig. 6, to realize analog subtraction in-crossbar. 2T2R, with two ReRAMs (2R) per weight accessed via two access transistors (2T), have been explored as a method to represent signed weights [3, 27, 28, 67, 74]."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _contrasts/critiques_: "Unfortunately, most of the recent works focus on the demonstration of the neural network acceleration for inference on edge applications which only consists of the information forwarding process [5–12]."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "The SAR ADC performs successive comparisons of analogue values using a binary search and an adaptive reference set based on previous decisions41,63–67."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "The 2T2R configuration70 offers a distinct advantage by inherently reducing the accumulated source line current to mitigate IR drop while simultaneously enabling sign representation of synaptic weights, establishing it as a practical solution."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _data/numbers_: "Based on the latest technology, scaling of ReRAM PIM devices [14, 35, 37], we set the area-constrained ReRAM PIM capacity to 16 Mb and 32 Mb for a small AI edge devices [7]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.pdf](../../02_Fabricated_Chips_and_Macros/2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.pdf)
- Full text: [../fulltext/2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.txt](../fulltext/2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isscc19947.2020.9062953
