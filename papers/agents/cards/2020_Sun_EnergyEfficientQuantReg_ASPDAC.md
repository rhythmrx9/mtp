---
id: W3013241373
key: 2020_Sun_EnergyEfficientQuantReg_ASPDAC
title: "An Energy-Efficient Quantized and Regularized Training Framework For Processing-In-Memory Accelerators"
short: "Quantized+Regularized PIM Training"
year: 2020
venue: "ASP-DAC"
venue_full: "25th Asia and South Pacific Design Automation Conference (ASP-DAC 2020)"
authors: "Hanbo Sun, Zhenhua Zhu, Yi Cai, Xiaoming Chen, Yu Wang, Huazhong Yang"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "quantization", "adc-dac", "energy-efficiency", "analog-mvm", "cnn-accelerator", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 4
citations_overall: 41
priority_score: 5.94
doi: "https://doi.org/10.1109/asp-dac47756.2020.9045192"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2020_Sun_EnergyEfficientQuantReg_ASPDAC.pdf"
fulltext: "../fulltext/2020_Sun_EnergyEfficientQuantReg_ASPDAC.txt"
---

# Quantized+Regularized PIM Training

**An Energy-Efficient Quantized and Regularized Training Framework For Processing-In-Memory Accelerators** — 25th Asia and South Pacific Design Automation Conference (ASP-DAC 2020) (2020)

## TL;DR
A training framework for RRAM PIM combining a non-uniform activation quantization scheme (implemented by non-linear ADCs plus MUXes) that cuts ADC resolution by 2 bits and an energy-aware weight regularizer that cuts analog crossbar energy by ~35%, yielding 3.4x better energy efficiency (9.02 TOPS/W) with little accuracy loss on CIFAR-10 CNNs.

## Summary
ADCs consume more than 60% of PIM system energy, and crossbar energy depends on the specific input voltage and cell conductance (HRS vs LRS can differ by 1-2 orders of magnitude). The framework has two parts. (1) PIM-based non-uniform activation quantization: the quantization range is set to [-|mu|-3 sigma, |mu|+3 sigma] instead of the max (covering >97% of data and shrinking the range to ~25%), the scale is a high-precision, non-power-of-two value smoothed with momentum, and non-uniform quantization follows a sigmoid approximation to the activation CDF; in hardware this is realised by non-linear ADC reference levels and MUXes that map the low-precision non-linear code to a high-precision linear value (simulated by a linear-mapping module during training). (2) Energy-aware weight regularization: an analytical crossbar energy model (TIA sensing model; energy proportional to V^2-like dependence on input voltage level and to conductance) is added to the loss so that high-voltage-level inputs land on high-resistance cells, reducing the share of HVL-on-LRS by ~41%. Evaluation trains LeNet, VGG-8 and ResNet-18 on CIFAR-10 with 256x256 crossbars (PRIME/configurable-framework-style architecture), RRAM HRS 150 kOhm, LRS 30 kOhm, read voltage 0.15 V, 100 MHz, ADC data from published 8/6/4-bit designs, 1-bit DAC, digital synthesised at 45 nm. Energy is computed analytically, not measured.

## Contributions
- PIM-aware non-linear activation quantization with range optimisation, high-precision scale and CDF-based non-uniform levels, implementable with non-linear ADCs and MUXes
- Analytical energy model of crossbar computing as a function of input voltage and conductance state, and a regularizer that lowers it during training
- Experiments on LeNet, VGG-8, ResNet-18 (CIFAR-10) showing 2-bit lower ADC resolution, ~35% lower analog energy and 3.4x overall energy-efficiency gain

## Key claims (stable IDs)
- **2020_Sun_EnergyEfficientQuantReg_ASPDAC#C1** — The scheme reduces ADC resolution by 2 bits with ~70% ADC energy reduction and accuracy comparable to traditional activation quantization — _support:_ A4W4 'Ours' vs A6W4 baseline [7]: LeNet 0.7467 vs 0.7463, VGG-8 0.9286 vs 0.9243, ResNet-18 0.8655 vs 0.8756 — _loc:_ Sec. I contributions, Table I
- **2020_Sun_EnergyEfficientQuantReg_ASPDAC#C2** — Energy-aware weight regularization reduces analog computing energy by ~35% (up to ~40% in one test) by cutting HVL-on-LRS share by ~41% — _support:_ normalized energy before/after regularization — _loc:_ Sec. V, Fig. 4
- **2020_Sun_EnergyEfficientQuantReg_ASPDAC#C3** — Overall framework improves energy efficiency 3.4x, reaching 9.02 TOPS/W (2.6-4.2x vs existing work) — _support:_ CIFAR-10, 256x256 crossbars, 100 MHz — _loc:_ Sec. I contributions, Sec. VI
- **2020_Sun_EnergyEfficientQuantReg_ASPDAC#C4** — At the same A4W4 precision, previous low-bit-width training collapses (VGG-8 0.1887) while the proposed framework keeps 0.9286 — _support:_ Table I comparison against [7] — _loc:_ Table I

## Results
- Table I (accuracy / energy nJ): float baselines LeNet 0.7448, VGG-8 0.9336, ResNet-18 0.8887
- Prior [7] A6W4: 0.7463/408 nJ (LeNet), 0.9243/458,193 nJ (VGG-8), 0.8756/4,517 nJ (ResNet-18)
- Ours A4W4: 0.7467/142 nJ, 0.9286/138,793 nJ, 0.8655/1,500 nJ - about 3x lower energy at comparable accuracy
- Energy-breakdown figure: ADC energy drops ~62-68% in the optimised configurations
- Assumed RRAM: HRS 150 kOhm, LRS 30 kOhm, 0.15 V read, 256x256 arrays

## Key numbers
- tech_node: 45nm (digital synthesis)
- array_size: 256x256
- energy_eff: 9.02 TOPS/W (3.4x improvement)
- accuracy: A4W4: 0.9286 VGG-8, 0.8655 ResNet-18, 0.7467 LeNet (CIFAR-10)
- bits_weight: 4b
- bits_adc: 4b (2 bits lower than baseline)

## Datasets / benchmarks
CIFAR-10

## Limitations
- Energy estimates come from an analytical model and ADC/DAC numbers borrowed from other papers; no silicon validation
- Ignores analog non-idealities (device variation, IR drop, noise); only CIFAR-10 CNNs, with low LeNet baseline accuracy on CIFAR-10 (74%)
- Non-linear ADC + MUX hardware overhead only qualitatively discussed
- Comparison primarily against one prior low-bit-width RRAM method [7]
- No transformer or LM evaluation

## Remarks
A software/training-side co-design: its value is showing that ADC range/shape (not just resolution) can be learned and that value-dependent analog energy can be regularised. The 3.4x figure is a modelled estimate and should not be read as a hardware result. The idea of range clipping and non-uniform ADC levels is directly relevant to LM mapping, where outliers make full-range ADC quantization wasteful (cf. static-range ADC training in later analog LLM work), but nothing here was tested beyond small CNNs.

## Cites (in collection, 4)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019) — _baseline/comparison_: "In the software level, researchers design the low bit-width CNN for PIM architectures to reduce the resolution requirement of ADCs, which introduce additional accuracy loss overhead [7]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _motivation_: "Researchers have pointed out that the ADCs occupy more than 60% energy consumption of the overall PIM architectures, which damage the energy efficiency gains of PIM architectures [2]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "From Figure 3, non-uniform quantization can reduce 1 bit ADC resolution compared with uniform quantization without accuracy loss, and ADC overheads grow exponentially with resolution [11]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Because PIM architectures have the ability to complete the CNN computing in memory by converting convolution operations into analog-domain Matrix-VectorMultiplications (MVMs), data movements are greatly reduced and energy efficiency can be enhanced by over 100× compared with CMOS-based architectures [1]."

## Cited by (in collection, 3)
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022) — _baseline/comparison_: "As a result, several previous works developed partial-sum quantization algorithms for CIMbased NN accelerators [1, 12, 17]."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "Reference [29] uses the Cumulative distribution function (CDF) of the partial sum to decide the nonlinear references corresponding to linear quantized cumulative distribution."
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2020_Sun_EnergyEfficientQuantReg_ASPDAC.pdf](../../07_Hardware_Aware_Training_and_Robustness/2020_Sun_EnergyEfficientQuantReg_ASPDAC.pdf)
- Full text: [../fulltext/2020_Sun_EnergyEfficientQuantReg_ASPDAC.txt](../fulltext/2020_Sun_EnergyEfficientQuantReg_ASPDAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/asp-dac47756.2020.9045192
