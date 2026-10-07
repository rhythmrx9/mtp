---
id: W4408245641
key: 2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature
title: "A mixed-precision memristor and SRAM compute-in-memory AI processor"
short: "Khwa Mixed-Precision Memristor-SRAM CIM"
year: 2025
venue: "Nature"
venue_full: "Nature"
authors: "Win-San Khwa, Tai-Hao Wen, Hung-Hsi Hsu, Wei-Hsing Huang, Yu‐Chen Chang, Ting-Chien Chiu, Zhao-En Ke, Yu-Hsiang Chin, Hua-Jin Wen, Wei‐Ting Hsu, Chung‐Chuan Lo, Ren-Shuo Liu et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM", "SRAM-digital"]
models: ["CNN", "ResNet", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "heterogeneous-analog-digital", "mixed-precision", "energy-efficiency", "edge-ai", "device-variation", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 11
citations_overall: 68
priority_score: 8.19
doi: "https://doi.org/10.1038/s41586-025-08639-2"
pdf: "../../02_Fabricated_Chips_and_Macros/2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.pdf"
fulltext: "../fulltext/2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.txt"
---

# Khwa Mixed-Precision Memristor-SRAM CIM

**A mixed-precision memristor and SRAM compute-in-memory AI processor** — Nature (2025)

## TL;DR
A TSMC/NTHU 22 nm edge AI processor with 64 Mb foundry memristor CIM plus 1 Mb SRAM-CIM and tiny-digital units partitions layers/kernels by error sensitivity across INT and FP formats, measuring 40.91 TFLOPS/W (ResNet-20/CIFAR-100, 0.27% degradation) and 373.52 us wakeup-to-response.

## Summary
Edge AI needs high precision, efficiency, large on-chip model storage and fast wakeup; multi-level memristor CIM is dense and non-volatile but sensitive to process variation, while digital SRAM-CIM is lossless but small and needs weight loading. The chip is a heterogeneous design fabricated in 22 nm with foundry-ready 64 Mb memristors (4 x 16 Mb) and 1 Mb SRAM-CIM (4 x 256 kb) plus tiny-digital units, 8 MB activation SRAM and 512 kB buffers, with four kernel-based mix-CIM engines. A layer-based INT-FP hybrid controller assigns each layer one of four modes (pure-INT, INT-input/FP-weight, FP-input/INT-weight, pure-FP) and a kernel-based controller assigns each weight kernel to memristor-CIM, SRAM-CIM or the digital unit using offline-extracted kernel features (e.g. small shared exponent means insensitive). FP is done via shared-exponent pre-alignment of inputs/weights, with weights stored in MLC memristor cells (2 b/cell, 5-bit ADCs) and partial dot products recombined with exponents. Error-sensitive first/last layers and FC layers go to FP/SRAM-CIM, insensitive hidden layers to INT/memristor. Measured end-to-end (no FPGA host) at 0.8 V/200 MHz on ResNet-20/CIFAR-100 and MobileNet-v2/ImageNet, plus a FLAME forest-fire drone demo.

## Contributions
- Layer-granular INT/FP hybrid-mode controller with four input/weight format modes
- Kernel-granular mix-CIM assignment across MLC memristor-CIM, digital SRAM-CIM and tiny-digital units based on error sensitivity
- Fabricated 22 nm chip with 64 Mb foundry-ready memristor array plus SRAM-CIM and end-to-end inference without FPGA host
- Wakeup-to-response time measurement showing an order-of-magnitude reduction vs SRAM-CIM with off-chip memory

## Key claims (stable IDs)
- **2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature#C1** — Mixed memristor/SRAM/digital partitioning with INT/FP hybrid formats gives high efficiency with sub-0.5% accuracy loss — _support:_ 40.91 TFLOPS/W with 0.27% degradation (ResNet-20/CIFAR-100); 28.63 TFLOPS/W with 0.42% (MobileNet-v2/ImageNet) — _loc:_ Abstract, Fig. 4
- **2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature#C2** — On-chip NVM reduces wakeup-to-response latency by an order of magnitude — _support:_ 373.52 us at 0.8 V, 200 MHz vs SRAM-CIM with off-chip memory — _loc:_ Fig. 4c,d
- **2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature#C3** — Hybrid INT-FP mode improves figure of merit (energy efficiency / accuracy degradation) by 1.79-3.09x — _support:_ Efficiency 25.35-75.38 TOPS/W, accuracy 68.78%-69.59% across modes — _loc:_ Extended Data Fig. 2
- **2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature#C4** — Mix-CIM assignment reduces output deviation 1.52x and improves FoM 1.1-2.67x — _support:_ 20 chip samples, 10,000 image patterns — _loc:_ Extended Data Fig. 3

## Results
- 40.91 TFLOPS/W, 0.27% degradation, ResNet-20 on CIFAR-100
- 28.63 TFLOPS/W, 0.42% degradation, MobileNet-v2 on ImageNet
- Wakeup-to-response 373.52 us, ~10x better than SRAM-CIM with off-chip memory
- Mix-CIM: energy efficiency 22.02-52.24 TOPS/W with 0-0.92% accuracy degradation (ResNet-20/CIFAR-100)
- Pure-INT vs pure-FP: 25.35-75.38 TOPS/W, accuracy 68.78-69.59%

## Key numbers
- tech_node: 22nm
- array_size: 64 Mb memristor (4x16 Mb) + 1 Mb SRAM-CIM
- energy_eff: 40.91 TFLOPS/W (ResNet-20); 28.63 TFLOPS/W (MobileNet-v2)
- accuracy: 0.27% degradation CIFAR-100 ResNet-20; 0.42% ImageNet MobileNet-v2
- bits_weight: INT or FP; MLC 2 b/cell
- bits_adc: 5-bit

## Datasets / benchmarks
CIFAR-100, ImageNet, MNIST, CIFAR-10, FLAME

## Limitations
- Only CNNs (ResNet-20, MobileNet-v2) evaluated; no transformers or language models
- Offline sensitivity analysis and kernel assignment per model
- Accuracy preserved partly by routing sensitive kernels to SRAM-CIM, so a fraction of compute is not analog-NVM
- Wakeup baseline compares against SRAM-CIM with an assumed 1 pJ/bit off-chip memory energy
- Memristor type/device details limited (foundry 22 nm, MLC 2 b/cell)

## Remarks
A strong measured-silicon result from Nature showing that heterogeneous analog-NVM plus digital partitioning, guided by per-layer/kernel error sensitivity, is a practical way to bound accuracy loss. It is directly relevant to mapping LMs: outlier-heavy or sensitive layers could be assigned to digital/SRAM-CIM and FP-shared-exponent formats while bulk weights sit in memristors. It extends the authors' Science 2024 fusion work and the ISSCC ReRAM macros cited in the collection.

## Cites (in collection, 11)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _contrasts/critiques_: "Previous works using self-designed analogue13 or MLC devices exceeding 2 bits per cell14,15 have achieved good results with relatively simple NN models and datasets; however, further assessments based on foundry-ready memristors will be required."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _contrasts/critiques_: "Previous works using self-designed analogue13 or MLC devices exceeding 2 bits per cell14,15 have achieved good results with relatively simple NN models and datasets; however, further assessments based on foundry-ready memristors will be required."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)

## Cited by (in collection, 3)
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Although some works on SRAM-based IMC have explored floating-point precision of inputs and weights, by handling the exponent and mantissa representations separately using a combination of time, digital and voltage (analogue) domain computing blocks29–31, this requires considerably higher memory capacity and computation energy than the more conventional designs using integer precision31."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "In practical scenarios, strategies of different granularities can be jointly used for achieving a better performance, such as combining both the layer-wise and cell-wise mix-CIM113 or utilizing both bit-wise and layer-wise approaches46."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "Existing work related to CIM has investigated the implementation of small-scale neural networks [1, 7, 8]."

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.pdf](../../02_Fabricated_Chips_and_Macros/2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.pdf)
- Full text: [../fulltext/2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.txt](../fulltext/2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41586-025-08639-2
