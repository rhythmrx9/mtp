---
id: W3109300165
key: 2021_Zhang_RobustTrainableQuantizer_ASPDAC
title: "A Quantized Training Framework for Robust and Accurate ReRAM-based Neural Network Accelerators"
short: "Robust Trainable Quantizer"
year: 2021
venue: "ASP-DAC"
venue_full: "26th Asia and South Pacific Design Automation Conference (ASP-DAC 2021)"
authors: "Chenguang Zhang, Pingqiang Zhou"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["quantization", "hardware-aware-training", "device-variation", "noise-injection", "analog-mvm", "mixed-precision"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 8
citations_overall: 4
priority_score: 4.89
doi: "https://doi.org/10.1145/3394885.3431528"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2021_Zhang_RobustTrainableQuantizer_ASPDAC.pdf"
fulltext: "../fulltext/2021_Zhang_RobustTrainableQuantizer_ASPDAC.txt"
---

# Robust Trainable Quantizer

**A Quantized Training Framework for Robust and Accurate ReRAM-based Neural Network Accelerators** — 26th Asia and South Pacific Design Automation Conference (ASP-DAC 2021) (2021)

## TL;DR
A learnable non-uniform weight quantizer, trained with an EM-style clustering that penalises levels at high-variation (high-conductance) regions, makes a LeNet-300-100 on a simulated ReRAM crossbar far more robust to lognormal conductance variation (e.g., 88.7% vs 58.79% at sigma = 0.6) with no extra hardware.

## Summary
Conductance variation (device-to-device and pulse-to-pulse) degrades ReRAM accelerators, and uniform quantization only partly helps. The authors model conductance as lognormal (G_actual = G_target * e^theta) from a tunnelling-gap device model, and note two observations: devices at high conductance suffer more variation, and quantization itself costs accuracy. They cast quantization as 1-D clustering of each layer's weights into K levels, minimising quantization error plus gamma times a variation-sensitivity term S(q) (approximated as alpha*q, using the 3-sigma criterion and the accumulated squared error metric). An EM-style layer-by-layer algorithm alternates the assignment (E-step) and level update (M-step) during the forward pass, with a straight-through estimator for back-propagation and uniform initial levels. Weights map to crossbar conductances with differential scaling, inputs to voltages and outputs through ADCs. Evaluation uses a PytorX-based PyTorch simulator (crossbar 64x64) with Monte-Carlo variation on LeNet-300-100 and MNIST, sweeping bit-widths (qNx bNw Ny), gamma and variation amplitude sigma in 0-2.0.

## Contributions
- Variation-aware quantized training framework for multi-bit ReRAM crossbars with no extra hardware overhead
- Metric combining quantization error and variation sensitivity with tunable trade-off gamma
- Trainable non-uniform quantizer via EM-style clustering integrated into standard training
- Simulation framework for accuracy under conductance variation

## Key claims (stable IDs)
- **2021_Zhang_RobustTrainableQuantizer_ASPDAC#C1** — Non-uniform trainable quantization improves inference accuracy by 10-30% under large conductance variation versus uniform quantization — _support:_ abstract; Fig. 4 — _loc:_ Abstract, Sec. 4.2, Fig. 4
- **2021_Zhang_RobustTrainableQuantizer_ASPDAC#C2** — Uniform quantization collapses with variation while the proposed method degrades slower — _support:_ uniform: 93.07% (sigma 0) to 58.79%, 32.67%, 25.64% at sigma 0.6, 1.2, 2.0; proposed (best): 94.69%, 88.7%, 51.65%, 24.05% — _loc:_ Sec. 4.2, Fig. 4
- **2021_Zhang_RobustTrainableQuantizer_ASPDAC#C3** — Without variation the method matches or beats uniform quantization — _support:_ 94.69% vs 93.07% at sigma = 0 — _loc:_ Sec. 4.2
- **2021_Zhang_RobustTrainableQuantizer_ASPDAC#C4** — ReRAM conductance follows a lognormal distribution and variation is larger near high conductance — _support:_ G_actual ~ G_target e^theta; cited experimental support — _loc:_ Sec. 2.2.1, Observation 1

## Results
- LeNet-300-100 on MNIST (64x64 crossbars): proposed 88.7% vs uniform 58.79% at sigma = 0.6
- At sigma = 1.2: 51.65% vs 32.67%; at sigma = 2.0 both near 24-26%
- Prior digital-crossbar quantized training [14] cited as losing 7.09% (94.11% to 87.02%) at 10% variation

## Key numbers
- array_size: 64x64
- accuracy: 88.7% MNIST at sigma=0.6 (uniform 58.79%)
- bits_weight: variable (qNx bNw Ny sweep)
- bits_adc: variable (Ny sweep)

## Datasets / benchmarks
MNIST

## Limitations
- Tiny MLP on MNIST only; no CNN, transformer or LM evaluation
- Simulation with an assumed variation model; no measured ReRAM data
- Sensitivity simplified to S(q) = alpha*q (constant 3-sigma/g ratio); gains vanish at extreme sigma = 2.0
- Ignores IR drop, ADC noise and stuck-at faults; quantizer trained per layer with hyperparameter gamma

## Remarks
A compact, training-only lever showing quantization levels themselves can be placed to avoid high-conductance regions, giving robustness without hardware cost. Proof-of-concept scale (MNIST MLP) limits generalisation to deep CNNs or transformers, where activation outliers and long accumulation matter more. It extends noise-injection style work in the collection (e.g., Noise Injection Adaption) by making the grid learnable.

## Cites (in collection, 8)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Weight compensation: Some works [5, 7] cooperate mask retraining and re-mapping methods to compensate the conductance deviation measured on a specific ReRAM crossbar."
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019) — _baseline/comparison_: "And [13, 14] try to incorporate quantization with training to eliminate the quantization error."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _uses-method-or-tool_: "To evaluate our proposed training algorithm, we build a comprehensive simulation framework based on PytorX [15], a simulator based on the PyTorch and implemented by Python."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _baseline/comparison_: "Digital crossbar: In [10–12], a high-precision value is represented by several single-bit crossbars, which is also called “ReRAM crossbar in digital mode”."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "With these merits, the ReRAM-based neural network accelerator has been widely studied and is proved to be a promising alternative to Von-Neumann architecture [2] [3] for this type of application."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "With these merits, the ReRAM-based neural network accelerator has been widely studied and is proved to be a promising alternative to Von-Neumann architecture [2] [3] for this type of application."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _contrasts/critiques_: "Other works [8] [9] try to train NN on the ReRAM crossbar hardware directly with stochastic gradient decent algorithm (online train)."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)

## Cited by (in collection, 1)
- [2023_Ma_SAFVariationTolerantMapping_JETC](2023_Ma_SAFVariationTolerantMapping_JETC.md) SAF/Variation Remapping (2023) — _baseline/comparison_: "On MNIST dataset and with a 3-layer fully-connected network, the state-of-the-art method [29] can only increase the accuracy from 50% (without the method) to 80% (with the method)."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2021_Zhang_RobustTrainableQuantizer_ASPDAC.pdf](../../07_Hardware_Aware_Training_and_Robustness/2021_Zhang_RobustTrainableQuantizer_ASPDAC.pdf)
- Full text: [../fulltext/2021_Zhang_RobustTrainableQuantizer_ASPDAC.txt](../fulltext/2021_Zhang_RobustTrainableQuantizer_ASPDAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3394885.3431528
