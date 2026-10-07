---
id: W2899749435
key: 2018_Lin_DLRSIM_ICCAD
title: "DL-RSIM"
short: "DL-RSIM"
year: 2018
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2018)"
authors: "Meng-Yao Lin, Hsiang-Yun Cheng, Wei‐Ting Lin, Tzu-Hsien Yang, I-Ching Tseng, Chia-Lin Yang, Han-Wen Hu, Hung-Sheng Chang, Hsiang-Pang Li, Meng‐Fan Chang"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "device-variation", "read-write-noise", "peripheral-circuits", "adc-dac", "crossbar-architecture", "bit-slicing", "benchmarking"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 12
cites_in_collection: 5
citations_overall: 76
priority_score: 7.15
doi: "https://doi.org/10.1145/3240765.3240800"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2018_Lin_DLRSIM_ICCAD.pdf"
fulltext: "../fulltext/2018_Lin_DLRSIM_ICCAD.txt"
---

# DL-RSIM

**DL-RSIM** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2018) (2018)

## TL;DR
DL-RSIM is a two-module simulator that computes per-bitline sum-of-products error rates from lognormal ReRAM resistance variation, operation-unit size and sense-amplifier settings, then injects them into TensorFlow CNNs, showing that deeper networks (CIFAR-10, YTF) need larger R-ratio, smaller sigma, smaller OU and tighter SA margins than MNIST.

## Summary
Prior ReRAM accelerator simulators (PRIME, ISAAC-style performance models) ignore current-sensing errors, circuit-level tools (NeuroSim) are hard to integrate with arbitrary networks, and behavior-level tools (MNSIM) give imprecise accuracy estimates. DL-RSIM's NVM Error Analytical Module takes hardware parameters (WLD resolution, bits per cell, Ron, R-ratio, resistance deviation sigma, SA resolution, SA reference currents, SA guard band dVSA, operation-unit size S_OU) and builds LRS/HRS lognormal resistance distributions, converts them to current distributions via Ohm's law (Vr = 0.6 V plus clamping error), and Monte-Carlo samples (32,000 samples per result) the accumulated bitline current for each number of activated wordlines to derive error tables (stored as PKL) under a dual-reference sensing scheme. The TensorFlow module wraps conv and FC layers with Decomposition (fixed-point inputs split per WLD bit, weights split per bits-per-cell and per OU), Error Injection (sampling the sensed value from the error table) and Composition (OU sum, shift-and-add over input and weight bits). Weights are thus mapped bit-sliced onto crossbars with at most S_OU wordlines active per cycle. It is validated against SPICE (RMS error <0.5% at S_OU=9) and applied to MNIST (1 conv + 2 FC), CIFAR-10 (3 conv + 3 FC) and Youtube Face (4 conv + 2 FC) with a baseline from a practical ReRAM chip (S_OU=9, 1-bit DAC, SLC, 4-bit SA, dVSA=0).

## Contributions
- Flexible TensorFlow-integrated ReRAM reliability simulator exposing cell, OU and sense-amplifier parameters
- Analytical Monte-Carlo error model of bitline sum-of-products under lognormal resistance variation, validated against SPICE (RMS error <0.5%)
- Decomposition/Error-injection/Composition flow modelling OU-based, bit-sliced dot products
- Design-space exploration of R-ratio, sigma, OU size and dVSA, and a workload-dependent sensing scheme that shifts reference currents

## Key claims (stable IDs)
- **2018_Lin_DLRSIM_ICCAD#C1** — The analytical current-distribution model matches SPICE with <0.5% RMS error at S_OU=9 — _support:_ Fig. 13 — _loc:_ Sec. 5.1
- **2018_Lin_DLRSIM_ICCAD#C2** — Deeper networks need better cells: with R-ratio=50 CIFAR-10 and YTF reach only 59.33% and 62.00% accuracy while MNIST recovers 99.99% at R-ratio>=25 — _support:_ Fig. 14 — _loc:_ Sec. 5.2.1
- **2018_Lin_DLRSIM_ICCAD#C3** — Reducing resistance deviation is more effective than increasing R-ratio — _support:_ CIFAR-10 86.00% at sigma=2/5 sigma_b (R-ratio 10) and 87.33% at 3/5 sigma_b (R-ratio 50) — _loc:_ Sec. 5.2.2, Fig. 15
- **2018_Lin_DLRSIM_ICCAD#C4** — Smaller operation-unit size and smaller SA guard band improve accuracy, more so for deeper CNNs — _support:_ MNIST tolerates dVSA<=35 mV, CIFAR-10 <20 mV, YTF <5 mV — _loc:_ Sec. 5.2.3-5.2.4, Fig. 16-17
- **2018_Lin_DLRSIM_ICCAD#C5** — A workload-dependent shift of the SA reference current IR[0] improves accuracy because >40% of bitline sums are zero — _support:_ shifts of 0.000397 mA (MNIST) and 0.000265 mA (CIFAR-10) — _loc:_ Sec. 5.2.5, Fig. 18-19

## Results
- Original (error-free) accuracy: MNIST 99.99%, CIFAR-10 88.67%, YTF 90.53%
- Baseline config S_OU=9, 1-bit WLD, SLC, 4-bit SA, dual-reference sensing, dVSA=0
- Error rate of sum 0 drops from 25% to 0% when R-ratio goes 10 to 50
- Sensing-scheme tuning notably raises CIFAR-10 and YTF accuracy (Fig. 19)

## Key numbers
- array_size: OU size 9 wordlines (baseline)
- accuracy: error-free MNIST 99.99%, CIFAR-10 88.67%, YTF 90.53%
- bits_weight: SLC (1 bit per cell), fixed-point weights bit-sliced
- bits_adc: 4b SA

## Datasets / benchmarks
MNIST, CIFAR-10, Youtube Face (YTF)

## Limitations
- Models only ReRAM (lognormal) read variation and SA errors; no wire IR-drop, drift, programming noise or cell-to-cell interference (SPICE comparison shows interference not modelled)
- Only small CNNs (MNIST, CIFAR-10, YTF); no transformers or language models
- Errors are injected independently per bitline per OU, ignoring spatial correlation
- Fixed-point 1-bit DAC, SLC baseline; limited design points explored

## Remarks
An early, influential accuracy-oriented reliability simulator that bridges device statistics and system-level inference via per-OU error tables; its Decomposition/Composition view is essentially the bit-sliced crossbar mapping used by later tools. Because it only injects sensing errors for CNN workloads, it cannot say how attention or LM workloads fare, and later simulators (RxNN, AIHWKit/Rasch et al.) cover far more non-idealities. Useful as the template for OU-based reliability analysis of NVM crossbars.

## Cites (in collection, 5)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _contrasts/critiques_: "Some circuit-level [1] and behavior-level [12] simulation platforms take the impact of hardware errors into consideration. However, the circuit-level tool [1] is hard to be integrated with various neural networks while the behavior-level tool [12] provides only imprecise analysis on inference accuracy."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _uses-method-or-tool_: "Based on a practical ReRAM-based accelerator chip [2], we choose SOU = 9, WLD resolution=1, and single-level cell as our baseline configuration in the following evaluation."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _motivation_: "Even if none of cells in a bitline is in error, the sum-of-products result read out by the sense amplifier may be incorrect [5] mainly due to (1) the accumulation of read noise from each activated cell in the bitline and (2) the imperfect sense amplifier with limited resolution."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "First, original feature maps from the input or pooling layer are transformed to fixed-point representation using the same method introduced by Shafiee et al. [9], and these feature maps are decomposed based on the WLD resolution."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "The non-ideal circuit and device properties that cause the current sensing errors are usually ignored in prior system-level work [3, 9]."

## Cited by (in collection, 12)
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020) — _contrasts/critiques_: "Recently, Lin et al. [18] proposed a simulation framework to compute and model the error rates of the memristor computation in the DNN model to partially recover the inference accuracy."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _contrasts/critiques_: "This can be achieved by using smaller arrays [43, 66], but this is inefficient as it amortizes the ADC energy cost over fewer MACs."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _uses-method-or-tool_: ""Whitin this group, we found for instance the DL-RSIM simulator, proposed by Lin et al., which simulates the error rates of every sum-of-products computation in memristor-based accelerators externally, and injects the errors in targeted TensorFlow-based neural network models.""
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _background_: "For a practical ReRAM-based DNN accelerator, the VMM on the crossbar arrays should operate at a much finer granularity, termed as an Operation Unit (OU), rather than at the subarray granularity. [3, 9, 10]."
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2018_Lin_DLRSIM_ICCAD.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2018_Lin_DLRSIM_ICCAD.pdf)
- Full text: [../fulltext/2018_Lin_DLRSIM_ICCAD.txt](../fulltext/2018_Lin_DLRSIM_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3240765.3240800
