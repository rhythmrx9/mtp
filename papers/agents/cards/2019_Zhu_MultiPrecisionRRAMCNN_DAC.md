---
id: W2946659370
key: 2019_Zhu_MultiPrecisionRRAMCNN_DAC
title: "A Configurable Multi-Precision CNN Computing Framework Based on Single Bit RRAM"
short: "Multi-Precision Single-Bit RRAM"
year: 2019
venue: "DAC"
venue_full: "56th ACM/IEEE Design Automation Conference (DAC 2019)"
authors: "Zhenhua Zhu, Hanbo Sun, Yujun Lin, Guohao Dai, Lixue Xia, Song Han, Yu Wang, Huazhong Yang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "quantization", "mixed-precision", "bit-slicing", "adc-dac", "crossbar-architecture", "tiling-partitioning", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 15
cites_in_collection: 5
citations_overall: 86
priority_score: 8.46
doi: "https://doi.org/10.1145/3316781.3317739"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2019_Zhu_MultiPrecisionRRAMCNN_DAC.pdf"
fulltext: "../fulltext/2019_Zhu_MultiPrecisionRRAMCNN_DAC.txt"
---

# Multi-Precision Single-Bit RRAM

**A Configurable Multi-Precision CNN Computing Framework Based on Single Bit RRAM** — 56th ACM/IEEE Design Automation Conference (DAC 2019) (2019)

## TL;DR
A layer-wise, RRAM-overhead-aware quantization plus a reconfigurable architecture that stores multi-bit weights across single-bit RRAM crossbars, giving 70% less area, 75% less energy, 3.44 TOps/W (8.6x ISAAC, 1.6x PRIME) with near full-precision accuracy.

## Summary
Multi-bit RRAM is hard to fabricate and suffers non-linearity and variation, while single-bit RRAM accelerators only handle binary/ternary CNNs with 10-20% ImageNet accuracy loss. The paper (a) proposes an RRAM computing deviation-aware layer-wise quantization (Algorithm 1) that selects per-layer weight and activation precision by minimizing a weighted sum of crossbar count (Num_c = sum 2*W_i*ceil(K^2 Cin/N)*ceil(Cout/N)) and crossbar latency (sum M_i/m * sliding times) subject to an accuracy loss threshold, modelling ADC/SA quantization error since Q_ideal = m + log2(N) + 1, and retraining; and (b) designs a hardware architecture where each weight bit lives in the same position of a different crossbar (spatial) while inputs are fed bit-serially through low-resolution (2-bit) DACs (temporal). A PE has positive and negative crossbars with analog subtraction, shared SA/ADC; a PE slice has eight PEs (up to 8-bit weights), barrel shifters and shift-and-add; an RRAM bank has 16 256x256 crossbars linked by an H-tree of Joint Modules; 512x512 RRAM crossbars act as data buffers. The mapping computes PE slices and banks per layer (Eq. 8) and uses a diagonal diffusion allocation on the H-tree. Evaluation: LeNet, modified VGG-16 and ResNet-18 on CIFAR-10 with RTL synthesis at 45 nm/500 MHz, RRAM at 100 MHz and literature ADC/DAC models.

## Contributions
- RRAM computing overhead-aware layer-wise quantization of weights and activations
- Configurable multi-precision architecture where multi-bit weights are spread over single-bit crossbars at the same position (spatial) with temporal input splitting
- Mapping strategy (PE slices/banks per layer plus H-tree diffusion allocation)
- Design-space exploration of crossbar size, ADC and DAC precision, giving {256, 6-bit, 2-bit DAC} configuration

## Key claims (stable IDs)
- **2019_Zhu_MultiPrecisionRRAMCNN_DAC#C1** — Mapping a GPU-quantized model onto RRAM loses much accuracy; the RRAM-aware quantization recovers it — _support:_ VGG on CIFAR-10: baseline 92.02%, GPU quantization 88.80%, GPU quantization on RRAM 83.80%, ours 88.48% — _loc:_ Table 1
- **2019_Zhu_MultiPrecisionRRAMCNN_DAC#C2** — Framework cuts area and energy substantially with little accuracy loss — _support:_ 70% computing area and 75% computing energy reduction on average — _loc:_ Abstract, Sec. 6, Fig. 4
- **2019_Zhu_MultiPrecisionRRAMCNN_DAC#C3** — Equivalent energy efficiency exceeds prior RRAM accelerators — _support:_ 3.44 TOps/W, 8.6x ISAAC and 1.6x PRIME, with 6% extra energy and 1.07% extra area from added digital logic — _loc:_ Sec. 6.3, Fig. 5
- **2019_Zhu_MultiPrecisionRRAMCNN_DAC#C4** — 256x256 crossbar with 6-bit ADC and 2-bit DAC is the best configuration — _support:_ 256x256 only 8% area over 128x128 but 1.2x-1.8x lower energy; 512x512 costs 1.5x area over 256x256 — _loc:_ Sec. 6.2, Tables 2-3

## Results
- VGG CIFAR-10 accuracy 88.48% vs 83.80% for GPU quantization mapped to RRAM (baseline 92.02%)
- Table 2 (crossbar 256, Q=6/8/10): LeNet 75.96/76.52/76.54%, VGG-16 91.80/92.20/92.32%, ResNet-18 94.78/94.94/95.06% accuracy
- 70% area and 75% energy reduction on average; 3.44 TOps/W (1.6x-8.6x vs existing RRAM accelerators)
- Extra overhead 6% energy and 1.07% area for PE-slice digital logic and Joint Modules

## Key numbers
- tech_node: 45nm (digital synthesis, 500MHz)
- array_size: 256x256 (16 per bank)
- energy_eff: 3.44 TOps/W
- accuracy: VGG-16 92.20% (Q=8, 256x256); 88.48% under overhead-aware quantization (VGG CIFAR-10)
- bits_weight: 1-bit cells, up to 8-bit weights
- bits_adc: 6-bit (chosen), 2-bit DAC

## Datasets / benchmarks
CIFAR-10

## Limitations
- Simulation only; RTL-synthesized digital parts and literature-based RRAM/ADC/DAC models
- Assumes single-bit RRAM variation has negligible effect, only ADC/SA quantization error is modelled
- CNNs on CIFAR-10 only; no ImageNet, transformers or language models
- Comparison with ISAAC/PRIME uses reported figures and different assumptions

## Remarks
A solid quantization-architecture co-design in the ISAAC/PRIME lineage; the idea of spreading bits across crossbars so peripherals need not be reconfigured is a practical bridge between manufacturable binary devices and precision. The cost model linking per-layer bit-width to crossbar count and DAC-limited latency is a reusable mapping idea, and bit-sliced single-bit weights are directly applicable to LM weights. Evidence is simulation-only, so variation, IR drop and yield are not captured.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _uses-method-or-tool_: "When the length of the unrolled weight is larger than the crossbar size, the column vector of inputs and weights are split for mapping onto different crossbars [16]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "In order to achieve high reliable and accurate CNN computing, researchers and chip designers also proposed several CNN accelerators based on single bit RRAM [2, 17, 18, 21]."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _extends/builds-on_: "Besides, since the crossbar size determines the number of crossbars we need for storing the weights, it will also affect the hardware area and energy overhead [24]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "the equivalent energy efficiency of the computing units (i.e., RRAM Banks) is 3.44TOps/W, nearly 8.6x and 1.6x compared with existing RRAM-based accelerators, ISAAC [15] and PRIME [3], respectively."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "In addition, some RRAM-based accelerators utilize the multi-bit RRAM devices which have more than two stable resistance states, to achieve higher storage and computation density, such as PRIME [3] and PipeLayer [16] with 4-bit RRAM."

## Cited by (in collection, 15)
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020) — _motivation_: "Researchers have pointed out that the ADCs occupy more than 60% energy consumption of the overall PIM architectures, which damage the energy efficiency gains of PIM architectures [2]."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _baseline/comparison_: "Digital crossbar: In [10–12], a high-precision value is represented by several single-bit crossbars, which is also called “ReRAM crossbar in digital mode”."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _background_: "Since weights in NNs are either positive or negative, two crossbars are used to represent the weight matrix, with one storing the positive weights and the other storing the negative weights [27] [28]."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _contrasts/critiques_: "Zhu et al. [29] provide a framework for quantizing CNNs on single-bit ReRAM crossbars."
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022) — _uses-method-or-tool_: "One-bit word-line drivers are used as input drivers and a couple of 1T1R RRAM cells are used to represent a signed weight [20]."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "Similarly, Zhenhua et al. [19] proposed the RRAM Computing Deviation Aware Quantization Scheme to search for the optimal precision for the weights and activations."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _extends/builds-on_: "To accommodate different CIM designs for executing MVM on crossbars [4, 39, 42, 51], we introduce the concept of VXB (Virtual Crossbar) as the computational unit rather than physical crossbars to facilitate the computing scheduling in the compiler."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _uses-method-or-tool_: "We adopt the PIM architecture proposed in MultiPrecision [6] as our infrastructure, for it can achieve higher equivalent energy efficiency with nearly no accuracy loss."
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _contrasts/critiques_: "For example, CMP [15] conducts layerwise mixed-precision quantization, and its model compression performance is limited."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _baseline/comparison_: "In contrast, the single-bit architecture enhances memristor robustness by storing only onebit information, allowing for higher resistance levels and lower energy consumption [20]."
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020)
- [2021_Li_RaQu_TCAD](2021_Li_RaQu_TCAD.md) RaQu (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2019_Zhu_MultiPrecisionRRAMCNN_DAC.pdf](../../05_Mapping_Compilation_and_Dataflow/2019_Zhu_MultiPrecisionRRAMCNN_DAC.pdf)
- Full text: [../fulltext/2019_Zhu_MultiPrecisionRRAMCNN_DAC.txt](../fulltext/2019_Zhu_MultiPrecisionRRAMCNN_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3316781.3317739
