---
id: W4300228436
key: 2022_Kim_ExtremePartialSumQuant_JETC
title: "Extreme Partial-Sum Quantization for Analog Computing-In-Memory Neural Network Accelerators"
short: "Extreme Partial-Sum Quantization"
year: 2022
venue: "JETC"
venue_full: "ACM Journal on Emerging Technologies in Computing Systems"
authors: "Yulhwa Kim, Hyungjun Kim, Jae‐Joon Kim"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM", "Generic-NVM"]
models: ["CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["adc-dac", "quantization", "bit-slicing", "peripheral-circuits", "energy-efficiency", "cnn-accelerator", "hardware-aware-training"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 6
citations_overall: 27
priority_score: 4.41
doi: "https://doi.org/10.1145/3528104"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2022_Kim_ExtremePartialSumQuant_JETC.pdf"
fulltext: "../fulltext/2022_Kim_ExtremePartialSumQuant_JETC.txt"
---

# Extreme Partial-Sum Quantization

**Extreme Partial-Sum Quantization for Analog Computing-In-Memory Neural Network Accelerators** — ACM Journal on Emerging Technologies in Computing Systems (2022)

## TL;DR
Data-driven, layer-wise partial-sum quantization with a zero-treading quantizer plus retraining cuts ADC resolution to 3 levels for CIFAR-10 and 9 levels for ImageNet, saving 50-80% area and 74-90% energy versus prior CIM designs.

## Summary
In bit-scalable analog CIM (bit-serial inputs through 1-bit word-line drivers, bit-parallel weights across cells), column partial sums are high-resolution and require ADCs that dominate cost: in a baseline 128x128 array with 16-level (4-bit) ADCs, ADCs account for 57% of area and 86% of energy. Prior work picks the partial-sum quantization range from min/max or mu+/-3sigma of the whole-network distribution and minimizes MSE. The authors analyze partial-sum distributions per layer, introduce a zero-tread quantizer that reduces error near zero (where most partial sums lie), then pick the range by exhaustive data-driven search over a sampled dataset (cheap because the search space is small), optionally per layer, and finally retrain the network with partial-sum quantization in the loop. Evaluation: ResNet-18 and VGG-9 on CIFAR-10, AlexNet on ImageNet, with NeuroSim (32nm CMOS, flash-type ADC built from sense-amplifier comparators, 1T1R pairs for signed weights; 128x128 array for VGG-9, 256x256 for AlexNet).

## Contributions
- Zero-tread quantizer for partial sums
- Data-driven exhaustive search for quantization range, layer-wise vs network-wise
- Retraining with partial-sum quantization to recover accuracy
- Area/energy evaluation of co-designed CIM accelerators with NeuroSim

## Key claims (stable IDs)
- **2022_Kim_ExtremePartialSumQuant_JETC#C1** — CIFAR-10 accuracy preserved with 3-level ADC after retraining; ImageNet with 9-level (<=4-bit) — _support:_ previous works needed >16 levels on CIFAR-10 — _loc:_ Sec. 4.2, Table 2
- **2022_Kim_ExtremePartialSumQuant_JETC#C2** — Layer-wise optimization needs fewer ADC levels than network-wise — _support:_ 5-level vs 8-level on CIFAR-10 without retraining — _loc:_ Fig. 12
- **2022_Kim_ExtremePartialSumQuant_JETC#C3** — 50-80% total area and 74-90% energy reduction vs previous designs — _support:_ NeuroSim, 32nm — _loc:_ Sec. 5, Fig. 15-16, Conclusion

## Results
- 8-level ADC saves 31% area vs 16-level baseline; 3-level saves 50% (VGG-9, Fig. 15a)
- ImageNet: network-wise needs 128-level (7-bit), layer-wise 32-64 levels, retraining 9-16 levels; area saving up to 80%
- Energy saving 46-74% on CIFAR-10 and 48-90% on ImageNet when going from 16 to 3 levels (Fig. 16)
- 1-bit (2-level) ADC is not fully recovered by retraining

## Key numbers
- tech_node: 32nm
- array_size: 128x128 (VGG-9), 256x256 (AlexNet)
- energy_eff: 74-90% energy reduction
- accuracy: preserved with 3-level ADC (CIFAR-10), 9-level (ImageNet)
- bits_adc: 3 levels (~1.6b) CIFAR-10; 9-16 levels ImageNet

## Datasets / benchmarks
CIFAR-10, ImageNet

## Limitations
- No analog noise/variation modelled; only quantization error
- ADC area/energy modelled as proportional to conversion levels for flash ADC
- CNNs only; no transformers where activation outliers and dynamic range differ
- Retraining required, with per-layer ranges requiring per-layer ADC references

## Remarks
Concrete evidence that ADC resolution can be driven much lower than assumed in ISAAC-like designs when quantization range is layer-wise and training is aware of it; the ADC share of energy (86%) motivates the work. Applicability to LM activations with heavy-tailed outliers is untested.

## Cites (in collection, 6)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019) — _contrasts/critiques_: "Previous works tried to reduce the mean-square-error (MSE) of partial-sum quantization and relied on the min/max values or standard deviation (σ) of the partial sum distributions to decide the quantization range [1, 12, 17]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _uses-method-or-tool_: "One-bit word-line drivers are used as input drivers and a couple of 1T1R RRAM cells are used to represent a signed weight [20]."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "We use NeuroSim [12], a benchmark framework of CIM accelerators, to measure the area and energy efficiency of CIM accelerators."
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020) — _baseline/comparison_: "As a result, several previous works developed partial-sum quantization algorithms for CIMbased NN accelerators [1, 12, 17]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Therefore, to support bit-scalable computation with low-resolution DAC, most of CIM accelerators process input values in bit-serial manner [8, 15, 20]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "The overhead of ADCs also increase as their resolution increases so that ADCs significantly degrade area and energy efficiency of CIM accelerators [2, 15, 20]."

## Cited by (in collection, 1)
- [2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED](2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.md) ADC-Less CiM Partial-Sum Quant (2023)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2022_Kim_ExtremePartialSumQuant_JETC.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2022_Kim_ExtremePartialSumQuant_JETC.pdf)
- Full text: [../fulltext/2022_Kim_ExtremePartialSumQuant_JETC.txt](../fulltext/2022_Kim_ExtremePartialSumQuant_JETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3528104
