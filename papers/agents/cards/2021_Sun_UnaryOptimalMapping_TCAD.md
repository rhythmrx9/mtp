---
id: W3119537022
key: 2021_Sun_UnaryOptimalMapping_TCAD
title: "Unary Coding and Variation-Aware Optimal Mapping Scheme for Reliable ReRAM-Based Neuromorphic Computing"
short: "Unary Optimal Mapping"
year: 2021
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Yanan Sun, Chang Ma, Zhi Li, Yilong Zhao, Jiachen Jiang, Weikang Qian, Rui Xia Yang, Zhezhi He, Li Jiang"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["device-variation", "weight-mapping", "quantization", "adc-dac", "energy-efficiency", "analog-mvm", "bit-slicing"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 9
citations_overall: 32
priority_score: 5.49
doi: "https://doi.org/10.1109/tcad.2021.3051856"
pdf: "../../06_Nonidealities_and_Reliability/2021_Sun_UnaryOptimalMapping_TCAD.pdf"
fulltext: "../fulltext/2021_Sun_UnaryOptimalMapping_TCAD.txt"
---

# Unary Optimal Mapping

**Unary Coding and Variation-Aware Optimal Mapping Scheme for Reliable ReRAM-Based Neuromorphic Computing** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2021)

## TL;DR
Replaces binary weight coding in multilevel-cell ReRAM crossbars with unary coding plus a variation-aware optimal mapping (exhaustive search over equivalent unary forms using pre-detected device variation), limiting accuracy loss to <0.89% (CIFAR10 top-1) and <4.45% (ImageNet top-5) at sigma=1.0, versus ~20-90% for binary coding.

## Summary
ReRAM resistance follows R' = R*exp(theta), theta ~ N(0, sigma^2); in binary coding the MSB cells amplify this deviation, and MLC makes it worse. The paper encodes each synaptic weight in unary coding, where all cells have equal significance and the value is the sum of the cell levels, implemented with MLCs (e.g. five 2-bit MLCs to cover [0,15], versus two for binary). Since unary coding has many equivalent codes for one value (e.g. 10 = '33310' or '22222'), a variation-aware optimal mapping uses per-cell variation coefficients (detected via ATE/BIST) and exhaustively searches all L^N level combinations to minimise |sum G_k e^(-theta_k) - w| for every weight (Fig. 6). Networks are first briefly retrained with quantisation in the loop, since unary coding restricts the representable range (e.g. [0,12] with four 2-bit MLCs). Accuracy is evaluated by Monte Carlo variation injection in Python (ResNet18, VGG16; CIFAR10, ImageNet) while energy/area use a cycle-accurate C++ simulator based on ISAAC (168 tiles, 12 IMAs per tile, eight 128x128 crossbars per IMA, 1-bit DAC, ADC resolution ceil(log2((L-1)*128))). A design-space study varies the number of ReRAMs per weight N (1-5) and MLC level L (2-10) to trade accuracy, energy and area. Positive and negative weights use two crossbars; only weights are unary coded while inputs and outputs remain binary.

## Contributions
- First use of unary coding with MLC ReRAM for synaptic weights to tolerate resistance variation
- Variation-aware optimal mapping exploiting multiple representations of a value (extends the authors' priority mapping, Go Unary)
- Design-space analysis of accuracy versus energy and area over the number of cells N and MLC level L
- Evaluation on CIFAR10 and ImageNet with ResNet18 and VGG16 under extreme variation (sigma up to 1.0)

## Key claims (stable IDs)
- **2021_Sun_UnaryOptimalMapping_TCAD#C1** — Proposed method keeps accuracy loss small under sigma=1.0 — _support:_ <0.89% top-1 loss on CIFAR10 and <4.45% top-5 loss on ImageNet (N=4, L=4) — _loc:_ Sec. IV-B, Table III
- **2021_Sun_UnaryOptimalMapping_TCAD#C2** — Large gains over binary coding — _support:_ +83.39% (ResNet18/CIFAR10) and +87.6% (abstract figure for ImageNet) accuracy; at least 62.58% higher than binary — _loc:_ Abstract; Table III
- **2021_Sun_UnaryOptimalMapping_TCAD#C3** — Optimal mapping cuts weight error versus priority mapping — _support:_ average RMSE 0.28 vs 1.50 (priority) vs 2.41 (basic unary); 88.3% and 81.2% reduction — _loc:_ Sec. III-C, Fig. 7
- **2021_Sun_UnaryOptimalMapping_TCAD#C4** — Best energy/area point uses high MLC level and few cells — _support:_ N=2, L=8 gives 1.1% loss (energy 0.96 mJ, area 43 mm^2 in Figs. 13-14) — _loc:_ Sec. IV-C, Figs. 12-14

## Results
- ResNet18/CIFAR10 top-1: ideal 94.30%, binary 10.83%, unary basic 12.56%, unary priority 74.16%, unary optimal 94.22% (0.08% loss) at sigma=1.0
- VGG16/CIFAR10: ideal 93.66%, unary opt 92.77% (0.89% loss); ImageNet ResNet18 top-5: ideal 89.07% vs unary opt 84.62% (4.45% loss); VGG16 top-5: 91.52% vs 88.09% (3.43% loss)
- Binary coding loses nearly 20% accuracy already at sigma=0.2 on ImageNet ResNet18 (Fig. 11); DVA training adds little over priority mapping
- Unary coding limited precision: 87.014% at sigma=0 versus 89.07% ideal (ImageNet ResNet18 top-5)
- Energy is more sensitive to N than L; ADC power dominates as L grows (Fig. 14)

## Key numbers
- array_size: 128x128 crossbars (ISAAC-style IMA)
- energy_eff: N=2, L=8: 0.96 mJ per image (ResNet18/CIFAR10)
- accuracy: 0.08% loss ResNet18/CIFAR10; 4.45% top-5 loss ResNet18/ImageNet at sigma=1.0
- bits_weight: 4 x 2-bit MLC (unary range [0,12])
- bits_adc: ceil(log2((L-1)*128)) bits, 8b at L=4

## Datasets / benchmarks
CIFAR-10, ImageNet

## Limitations
- Simulation only with log-normal device-to-device variation; cycle-to-cycle variation, drift, IR drop, stuck-at faults and ADC noise not modelled
- Requires per-device variation maps (ATE/BIST) and per-chip mapping computation; exhaustive search scales as L^N per weight
- Unary coding has a smaller weight range than binary; some residual loss comes from reduced precision and needs quantisation-aware retraining
- Energy/area use ISAAC-scaled parameters; hardware cost depends on assumed 1000x HRS/LRS ratio
- Only CNNs evaluated

## Remarks
Strong robustness numbers under an extreme sigma, but they depend on perfect knowledge of per-cell variation and a simple multiplicative noise model, which flatters the method relative to real devices with drift and noise. Conceptually the same idea (equal-significance cells to avoid MSB amplification) reappears as encodings and redundancy in later work; VECOM explicitly compares to Go Unary and notes the unary area overhead (~20x at 8 bit). No language-model workloads; a transformer's wider dynamic range would raise the required N.

## Cites (in collection, 9)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "At the algorithmic level, the weights are trained to enhance the tolerance of NNs to the resistance variations of ReRAMs [15]-[18]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Recent works present several NN accelerators based on ReRAM crossbars, such as PRIME [4], ISAAC [5], and PipeLayer [6]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _motivation_: "However, due to the immaturity of fabrication process combined with stochastic filament-based switching, ReRAM suffers from the resistance variations problem [10] [11], manifested as the deviation of actual resistance from its target value."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _background_: "Since weights in NNs are either positive or negative, two crossbars are used to represent the weight matrix, with one storing the positive weights and the other storing the negative weights [27] [28]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Moreover, several ReRAM-based chips have been fabricated to accelerate NN computing using Multi-Level Cells (MLCs) [7] [8]."
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020) — _contrasts/critiques_: "The previous work [18] proposed a software and hardware co-design method to get higher accuracy in CNN, even under large device variations. The off-device training was employed to get a relatively high accuracy while the on-device training was used to further suppress the accuracy loss."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The hardware simulator is cycle-accurate. It can calculate the energy consumption and area of the architecture based on the data from ISAAC [5] as listed in Table II."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Recent works present several NN accelerators based on ReRAM crossbars, such as PRIME [4], ISAAC [5], and PipeLayer [6]."
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)

## Cited by (in collection, 2)
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _background_: "To mitigate the post-mapping accuracy loss in DNNs, variation-aware training (VAT) and special encoding schemes are employed [5–9, 13]."
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2021_Sun_UnaryOptimalMapping_TCAD.pdf](../../06_Nonidealities_and_Reliability/2021_Sun_UnaryOptimalMapping_TCAD.pdf)
- Full text: [../fulltext/2021_Sun_UnaryOptimalMapping_TCAD.txt](../fulltext/2021_Sun_UnaryOptimalMapping_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2021.3051856
