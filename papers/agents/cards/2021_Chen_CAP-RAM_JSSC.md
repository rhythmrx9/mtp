---
id: W3164913974
key: 2021_Chen_CAP-RAM_JSSC
title: "CAP-RAM: A Charge-Domain In-Memory Computing 6T-SRAM for Accurate and Precision-Programmable CNN Inference"
short: "CAP-RAM"
year: 2021
venue: "JSSC"
venue_full: "IEEE Journal of Solid-State Circuits, vol. 56 (2021)"
authors: "Zhiyu Chen, Zhanghao Yu, Qing Jin, Yan He, Jingyu Wang, Sheng Lin, Dai Li, Yanzhi Wang, Kaiyuan Yang"
category: "02 Fabricated Chips & Macros"
devices: ["SRAM-analog", "Charge/Capacitor"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "adc-dac", "bit-slicing", "calibration-compensation", "pruning-sparsity", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 3
citations_overall: 136
priority_score: 7.52
doi: "https://doi.org/10.1109/jssc.2021.3056447"
pdf: "../../02_Fabricated_Chips_and_Macros/2021_Chen_CAP-RAM_JSSC.pdf"
fulltext: "../fulltext/2021_Chen_CAP-RAM_JSSC.txt"
---

# CAP-RAM

**CAP-RAM: A Charge-Domain In-Memory Computing 6T-SRAM for Accurate and Precision-Programmable CNN Inference** — IEEE Journal of Solid-State Circuits, vol. 56 (2021) (2021)

## TL;DR
CAP-RAM is a 65 nm charge-domain in-memory-computing macro built on standard 6T SRAM with a semi-parallel 8-cells-per-MAC-circuit structure, programmable weight/input precision and a 7-bit charge-injection SAR ADC, achieving 98.8% MNIST, 89.0% CIFAR-10 (ResNet-20), 573.4 GOPS peak and 49.4 TOPS/W.

## Summary
Prior IMC SRAMs trade off computing accuracy, memory density and precision configurability. CAP-RAM stores weights in standard 6T SRAM cells (logic-rule layout) and shares one lossless charge-domain MAC circuit across a cluster of eight cells, so filters from multiple CNN layers fit in one 512x128 macro while the MAC capacitors give process-variation-tolerant linearity. The semi-parallel scheme supports eight levels of input activations (multi-bit DAC input) and six levels of weights with two encoding schemes (differential mode for ternary weights and a +1/0/-1 two-bitcell unit), computing multi-bit MACs over several cycles via the generalized bit-weighted sum. A 7-bit charge-injection SAR (ciSAR) ADC (429 um2) removes sample-and-hold and input/reference buffers and reduces energy. A two-step calibration (per-ADC linear fit then master-curve calibration) corrects offset/gain variation; system linearity error is less than 2 LSB across 524,288 measured samples. The macro is compatible with structured pruning and quantisation: LeNet-5 and ResNet-20 are pruned/quantised (ADMM-NN style training) so a complete model fits on chip, and layers are executed layer by layer, with the 8 KB SRAM array taking 62.6% of the 0.179 mm2 macro. Measurements are reported on two prototype chips at 1.2 V and 25 degrees C.

## Contributions
- Compact 6T-SRAM charge-domain IMC macro with cluster-sharing of one MAC circuit for high storage density
- Semi-parallel reconfigurable computing with 8-level inputs and 6-level weights
- Charge-injection SAR ADC without sample-and-hold and reference buffers
- Two-step linearity calibration and measured linearity/noise characterisation
- Full-model on-chip inference for LeNet-5 (MNIST) and ResNet-20 (CIFAR-10)

## Key claims (stable IDs)
- **2021_Chen_CAP-RAM_JSSC#C1** — System linearity error is below two LSBs after calibration — _support:_ measured over 524,288 samples, two prototype chips — _loc:_ Sec. IV, Figs. 16-17
- **2021_Chen_CAP-RAM_JSSC#C2** — 98.8% MNIST accuracy matches the quantised software baseline — _support:_ LeNet-5 pruned/quantised with ADMM — _loc:_ Sec. IV-3
- **2021_Chen_CAP-RAM_JSSC#C3** — 89.0% CIFAR-10 accuracy with quantised ResNet-20 on a single 512x128 macro — _support:_ measured — _loc:_ Sec. IV-4, Table II
- **2021_Chen_CAP-RAM_JSSC#C4** — 573.4 GOPS peak throughput and 49.4 TOPS/W (text states 49.3 in conclusion) — _support:_ 1.2 V, 25 C; 3.4 TOPS/mm2 for convolution — _loc:_ Sec. IV, Table III, Abstract
- **2021_Chen_CAP-RAM_JSSC#C5** — Semi-parallel architecture gives best-in-class weight storage density while computing density remains competitive — _support:_ C3SRAM has higher compute density (20.2 TOPS/mm2) at 1b precision; CAP-RAM reaches 27.2 TOPS/mm2 on a normalised metric — _loc:_ Sec. IV, Table III

## Results
- 65 nm prototype: macro area 0.179 mm2; 8 KB SRAM array = 62.6% of macro
- ciSAR ADC area 429 um2; 7-bit resolution
- 98.8% MNIST (LeNet-5) and 89.0% CIFAR-10 (ResNet-20)
- Peak throughput 573.4 GOPS; energy efficiency 49.4 TOPS/W; 3.4 TOPS/mm2 for convolution at 1.2 V
- Jia et al. reach higher accuracy using 8-bit ADCs and a VGG-like network with 7.04x more operations than ResNet-20
- Power 6.35 mW in differential mode with all 32 slices on

## Key numbers
- tech_node: 65nm
- array_size: 512x128 (8 KB SRAM) macro
- energy_eff: 49.4 TOPS/W
- throughput: 573.4 GOPS peak; 3.4 TOPS/mm2
- accuracy: 98.8% MNIST; 89.0% CIFAR-10 (ResNet-20)
- bits_weight: up to six weight levels; ternary/differential
- bits_adc: 7b ciSAR

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- SRAM, not NVM: relevance to NVM crossbars is via charge-domain/ADC/calibration design
- Small CNNs only (LeNet-5, ResNet-20); no transformers or language models
- Layer-by-layer execution; semi-parallel structure lowers compute density relative to fully parallel macros
- Needs on-chip calibration logic and per-chip master curve calibration
- Accuracy at 89.0% on CIFAR-10 is below prior works at 90.4-92.0% that use larger parallelism or different ADCs

## Remarks
A well-instrumented silicon macro that quantifies linearity, ADC noise and calibration effects, giving real data on analog-accuracy loss for small CNNs. Its storage-density versus compute-density 'cluster size' knob is a useful abstraction for mapping weight-heavy models, including LMs where capacity rather than throughput dominates. Not NVM-based, so not directly transferable to drift and programming-noise concerns.

## Cites (in collection, 3)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "It is worth mentioning that fully parallelism of all MAC operations is possible with inter-layer pipelining [27, 28], and the imbalanced speed/throughput of each pipeline stage can be solved by mapping techniques, such as replication."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _baseline/comparison_: "Compared with recent IMC architectures, Jia et al. [26] show higher accuracy since it uses 8-bit ADCs and utilizes VGG-like network with 7.04 times more operations than ResNet-20."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "It is worth mentioning that fully parallelism of all MAC operations is possible with inter-layer pipelining [27, 28], and the imbalanced speed/throughput of each pipeline stage can be solved by mapping techniques, such as replication."

## Cited by (in collection, 2)
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "The SAR ADC performs successive comparisons of analogue values using a binary search and an adaptive reference set based on previous decisions41,63–67."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "Moreover, charge-domain CIM also offers an effective means to high energy efficiency and throughput110."

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2021_Chen_CAP-RAM_JSSC.pdf](../../02_Fabricated_Chips_and_Macros/2021_Chen_CAP-RAM_JSSC.pdf)
- Full text: [../fulltext/2021_Chen_CAP-RAM_JSSC.txt](../fulltext/2021_Chen_CAP-RAM_JSSC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jssc.2021.3056447
