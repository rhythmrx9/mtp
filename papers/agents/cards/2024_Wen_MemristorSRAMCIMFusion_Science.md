---
id: W4394909859
key: 2024_Wen_MemristorSRAMCIMFusion_Science
title: "Fusion of memristor and digital compute-in-memory processing for energy-efficient edge computing"
short: "Memristor-SRAM CIM Fusion"
year: 2024
venue: "Science"
venue_full: "Science"
authors: "Tai-Hao Wen, Je-Min Hung, Wei-Hsing Huang, Chuan-Jia Jhang, Yun-Chen Lo, Hung-Hsi Hsu, Zhao-En Ke, Yu-Chiao Chen, Yu-Hsiang Chin, Chin-I Su, Win-San Khwa, Chung‐Chuan Lo et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM", "SRAM-digital"]
models: ["CNN", "MobileNet", "ResNet", "Speech"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "heterogeneous-analog-digital", "on-chip-training", "bit-slicing", "adc-dac", "calibration-compensation", "device-variation", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 8
cites_in_collection: 11
citations_overall: 122
priority_score: 9.42
doi: "https://doi.org/10.1126/science.adf5538"
pdf: "../../02_Fabricated_Chips_and_Macros/2024_Wen_MemristorSRAMCIMFusion_Science.pdf"
fulltext: "../fulltext/2024_Wen_MemristorSRAMCIMFusion_Science.txt"
---

# Memristor-SRAM CIM Fusion

**Fusion of memristor and digital compute-in-memory processing for energy-efficient edge computing** — Science (2024)

## TL;DR
Fabricated 22-nm TSMC chip fusing foundry RRAM memristor CIM with digital SRAM CIM (MSB/LSB weight split, per-layer mode selection) plus on-chip adaptive local training, measured at 392.5 us wakeup-to-response, 34.24-77.64 TOPS/W and 0.14-0.51% accuracy loss.

## Summary
Memristor CIM is dense, nonvolatile and efficient but loses accuracy from process variation and has limited endurance (~10,000 cycles), while digital SRAM CIM is accurate but volatile and large (SRAM bit cell ~3x a 22-nm memristor cell; digital circuitry ~50% of SRAM-CIM units). The chip has four CIM-fusion units, a fusion controller, ALT circuitry and a 512 KB activation SRAM, with all weights stored in the RRAM array (no weight SRAM buffer). A mode controller assigns each network layer to a memristor-CIM mode (MM-S, MM-2, MM-1, MM-M using SLC and MLC cells, 8b weights in two's complement across 4-6 columns), a mixed-device mode (MDM: weight bits W[7:4] in memristor, W[3:0] in SRAM via a weight distributor) or pure SRAM-CIM mode for the most sensitive layers (Fig. 2). Memristor-CIM reads bit-line currents with 5-bit ADCs and a configurable adder building 24-bit dot products; SRAM-CIM uses MUX-based local compute cells with 128 accumulations (Fig. 4). Dynamic accumulation uses 16/32/64/128 accumulations per bit-plane (fewer for MSB inputs), in-memory-cell-array current quantisation regulates V_BL by accumulation count, and weight shifting with compensation (add a positive bias, e.g. 16, then subtract) raises the HRS-cell fraction to cut current (Fig. 5). Adaptive local training fine-tunes only the SRAM-resident (accuracy-oriented) weights, avoiding memristor writes. Measurements at 0.8 V, 200 MHz, 8b cover MobileNet-V2/ResNet-20 (MNIST, CIFAR-10/100, ImageNet), a parallel-CNN gesture model and DS-CNN keyword spotting.

## Contributions
- Memristor-SRAM CIM-fusion architecture with layer-wise mode selection (memristor, mixed, SRAM) on a fully CMOS-integrated 22-nm foundry RRAM chip.
- On-chip adaptive local training that fine-tunes SRAM-held weights to absorb memristor process variation and user-specific conditions while sparing RRAM endurance.
- Macro-level schemes: dynamic accumulation, in-memory-cell-array current quantisation, and weight shifting with compensation.
- Chip measurements across image, gesture and keyword-spotting tasks, including wakeup-to-response latency.

## Key claims (stable IDs)
- **2024_Wen_MemristorSRAMCIMFusion_Science#C1** — The fusion processor keeps accuracy close to software baseline across tasks. — _support:_ image classification 0.14-0.51% below software (MNIST, CIFAR-10/100, ImageNet); gesture 0.19%; keyword spotting 0.21% — _loc:_ Measurement results, Fig. 6A
- **2024_Wen_MemristorSRAMCIMFusion_Science#C2** — High energy efficiency. — _support:_ 34.24 to 77.64 TOPS/W for image classification; 62.21 TOPS/W for gesture recognition (8b, 0.8 V, 200 MHz) — _loc:_ Fig. 6B, abstract
- **2024_Wen_MemristorSRAMCIMFusion_Science#C3** — Short wakeup-to-response latency from nonvolatile weights. — _support:_ 392.5 us one-shot inference, ResNet-20 CIFAR-100 — _loc:_ Fig. 6D
- **2024_Wen_MemristorSRAMCIMFusion_Science#C4** — Improvement over previous version of the work. — _support:_ 1.14x greater energy efficiency while accuracy degradation limited to 0.49x of previous work (10) — _loc:_ Table 1, Overview
- **2024_Wen_MemristorSRAMCIMFusion_Science#C5** — On-chip adaptive local training reduces accuracy degradation under memristor variation. — _support:_ ALT reduces degradation 'from 53.7 to 48.4%' for ResNet-20 / CIFAR-10 as printed in the text and Fig. 3C caption (figure itself needed to interpret the units) — _loc:_ Fig. 3C

## Results
- All tasks run end-to-end on chip at 0.8 V and 200 MHz with 8-bit precision.
- Process variation can change dot-product accuracy by up to 10% in multilevel memristor cells.
- Simple tasks use more memristor-CIM-mode layers; complex tasks use more SRAM and mixed-mode layers (Fig. 6C).
- Dynamic accumulation: with 512 accumulations a CIM macro needs 16 cycles for MSB planes (N_ACCU=16) versus 4 for LSB planes (N_ACCU=128).

## Key numbers
- tech_node: 22nm foundry RRAM and SRAM
- array_size: SRAM-CIM: 64 subarrays of 8x25; 4 CIM-fusion units; 512 KB activation SRAM
- energy_eff: 34.24-77.64 TOPS/W (image), 62.21 TOPS/W (gesture)
- accuracy: 0.14-0.51% below software (image), 0.19% (gesture), 0.21% (keyword spotting)
- bits_weight: 8b (SLC/MLC RRAM + SRAM)
- bits_adc: 5b

## Datasets / benchmarks
MNIST, CIFAR-10, CIFAR-100, ImageNet, Dynamic hand gesture dataset (14 gestures), Google Speech Commands V1 (12 commands)

## Limitations
- Only small CNN-style edge workloads (MobileNet-V2, ResNet-20, DS-CNN); no transformers or language models.
- RRAM endurance (~10^4 cycles) prevents training on memristor weights; ALT only works on SRAM-resident bits, which needs SRAM capacity and limits the benefit for MM-only layers.
- Comparison to prior works is through the authors' own previous chip and a summary table; the main-text numbers for area/capacity are mostly in supplementary figures not available in the extracted text.
- Accuracy-degradation numbers for ALT are given in a confusing form in the text (53.7 to 48.4%).

## Remarks
Strong silicon evidence (Science, foundry RRAM, end-to-end tasks) that heterogeneous memristor+digital CIM is a practical route to deployable, trainable edge AI, resolving the RRAM accuracy/endurance trade-off by splitting weight bits and layers between analog-ish RRAM and digital SRAM. The MSB/LSB weight split and per-layer sensitivity mapping are directly relevant to mapping larger models: attention and FC layers that tolerate little noise could be placed in the SRAM or mixed modes. Related to the hybrid designs the IBM tile-design Perspective in this collection points to. Not evaluated on LMs.

## Cites (in collection, 11)
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _contrasts/critiques_: "A memristor-CIM core with in-lab 32-level cell and multiple discrete components on a printed circuit board (9) has been demonstrated to classify images from the Modified National Institute of Standards and Technology database (MNIST) and the Canadian Institute for Advanced Research (CIFAR-10)."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."

## Cited by (in collection, 8)
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _background_: "Recent publications of large-scale integrated AIMC chips, using phase change memory (PCM) 22,23, resistive RAM (ReRAM)24-26 and Flash27, show the viability of the technology."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _contrasts/critiques_: "One approach to the challenge of training at the edge is to combine memristors with accurate digital static random-access memory, which can be made using standard transistors15."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _extends/builds-on_: "Hybrid designs combining SRAM and memristive devices may also offer a compelling trade-off between robustness, density and energy efficiency, paving the way for practical and scalable AIMC solutions31,100."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _motivation_: "Simulation results confirm that our method is effective on a 25.3M-parameter transformer model, a practical size suitable for deployment on currently available AIMC chips18,19."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "These hybrid designs typically partition computational tasks based on the characteristics of each memory device: deploying high-precision, frequently updated operations on SRAM while allocating computation-intensive yet structurally simple operations to RRAM [1, 56]."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _data/numbers_: "Whereas single devices demonstrating up to 2,048 and 16,520 conductance states have been reported28,48, practical analogue CIM systems typically utilize only 2–32 states7–9,46."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "In order to store larger neural networks fully on-chip, a more scalable memory technology must be used, which is why researchers explored AIMC with dense Non-Volatile Memory (NVM) such as embedded flash [18], Phase Change Memory (PCM) [19, 20], ReRAM [21, 22], or MRAM [23]."

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2024_Wen_MemristorSRAMCIMFusion_Science.pdf](../../02_Fabricated_Chips_and_Macros/2024_Wen_MemristorSRAMCIMFusion_Science.pdf)
- Full text: [../fulltext/2024_Wen_MemristorSRAMCIMFusion_Science.txt](../fulltext/2024_Wen_MemristorSRAMCIMFusion_Science.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1126/science.adf5538
