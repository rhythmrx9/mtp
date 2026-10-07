---
id: W4389166806
key: 2023_Jang_VECOM_ICCAD
title: "VECOM: Variation-Resilient Encoding and Offset Compensation Schemes for Reliable ReRAM-Based DNN Accelerator"
short: "VECOM"
year: 2023
venue: "ICCAD"
venue_full: "2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD 2023)"
authors: "Je-Woo Jang, Thai-Hoang Nguyen, Joon-Sung Yang"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["device-variation", "weight-mapping", "bit-slicing", "calibration-compensation", "adc-dac", "energy-efficiency", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 5
priority_score: 3.54
doi: "https://doi.org/10.1109/iccad57390.2023.10323803"
pdf: "../../06_Nonidealities_and_Reliability/2023_Jang_VECOM_ICCAD.pdf"
fulltext: "../fulltext/2023_Jang_VECOM_ICCAD.txt"
---

# VECOM

**VECOM: Variation-Resilient Encoding and Offset Compensation Schemes for Reliable ReRAM-Based DNN Accelerator** — 2023 IEEE/ACM International Conference on Computer Aided Design (ICCAD 2023) (2023)

## TL;DR
VECOM re-biases 8-bit weights (bias 64 instead of 128) with redundant mapping of the [5:4] bits so high-significance MLC cells sit at low-conductance, low-variation levels, and adds a G00 conductance offset so HRS offset-current subtraction is exact for MLC, allowing up to 9.1x throughput (7.2x average on CIFAR-10) and over 50% energy saving with no retraining.

## Summary
ReRAM PIM accelerators limit the number of activated wordlines (NAW) because conductance variation and HRS offset current overlap MAC-sum distributions and confuse the ADC, reducing parallelism. The authors observe that, in 8-bit quantised weights split into four 2-bit MLC cells, the MSB pair [7:6] is almost always 01 or 10 (weights within +-64), and the high-conductance state 10 (log-normal variation G = G0 exp(theta)) causes the largest overlap. VECOM encoding has two steps: bias control (bias 64 instead of the usual 128, so [7:6] becomes 00/01; negative weights are clipped, only 0.00018-0.002% of weights, Table I) and redundant mapping of a minor portion of 01/10 patterns of [5:4] to a redundant array (original [5:4] ADC result multiplied by 3). A second technique, conductance offset mapping, programs every MLC level at G' = G + G00 so that subtracting one extra-column current N*I00 recovers exactly the sum of useful currents, overcoming the SLC-only limitation of input-aware current compensation (IAC). Evaluation is PyTorch Monte-Carlo simulation on an ISAAC-like architecture (128x128 arrays, 2b/cell, 1-bit DAC, SAR ADC with log2(NAW)+2 bits) on VGG-16, ResNet-18, Inception-V3 across CIFAR-10/100 and ImageNet plus LeNet/MNIST. Throughput and energy are estimated analytically from NAW at 1% accuracy loss and ADC resolution scaling.

## Contributions
- Analysis of MLC level distributions of quantised DNN weights (ResNet-18, VGG-16, Inception-V3) showing MSB patterns concentrate on 01/10
- VECOM encoding: bias control plus redundant mapping that moves high-variation levels to lower-conductance ones without retraining
- Conductance offset mapping that makes HRS offset-current compensation exact for MLC and higher bits per cell
- Evaluation of accuracy vs NAW, R-ratio and bits-per-cell, with estimated speedup and energy

## Key claims (stable IDs)
- **2023_Jang_VECOM_ICCAD#C1** — VECOM raises achievable wordline parallelism at fixed accuracy — _support:_ At variation 0.08, accuracy gains up to 58.4% (NAW=8) and 64.9% (NAW=128) on CIFAR-10, up to 77.6% on CIFAR-100, 62% on ImageNet at NAW=8 — _loc:_ Sec. IV-B2, Fig. 9
- **2023_Jang_VECOM_ICCAD#C2** — Robust at low R-ratio including MLC, unlike IAC — _support:_ Almost no degradation down to R-ratio 7; IAC worse than conventional for VGG-16 with MLC — _loc:_ Sec. IV-B3, Fig. 10
- **2023_Jang_VECOM_ICCAD#C3** — Scales to QLC — _support:_ <1% accuracy difference from baseline up to 4 bits/cell; IAC fails from 2 b/cell — _loc:_ Fig. 11
- **2023_Jang_VECOM_ICCAD#C4** — Throughput and energy gains — _support:_ speedup up to 9.1x (avg 7.2x) CIFAR-10, up to 5.3x (avg 3.9x) CIFAR-100; >50% average energy reduction — _loc:_ Figs. 12, 13

## Results
- Area overhead about 25% over baseline (8-bit weights) from redundant mapping; IAC ~1%; Go Unary ~25% at 4-bit and ~20x at 8-bit (Fig. 7)
- Clipped weight ratio only 0.00059% (ResNet-18), 0.00018% (VGG-16), 0.002% (Inception-V3) (Table I)
- Better variation tolerance than conventional mapping and Go Unary on VGG-16/CIFAR-10 and LeNet/MNIST with all 128 wordlines active (Fig. 8)
- Up to 9.1x throughput and average >50% energy reduction vs baseline despite higher-resolution ADC (Sec. IV-B4/5)

## Key numbers
- array_size: 128x128, 2 bits/cell
- energy_eff: >50% average energy reduction vs baseline
- throughput: up to 9.1x (avg 7.2x CIFAR-10)
- accuracy: up to +64.9% over conventional mapping at variation 0.08, NAW=128 (CIFAR-10)
- bits_weight: 8b (4 x 2b MLC)
- bits_adc: log2(NAW)+2 bits (SAR)

## Datasets / benchmarks
CIFAR-10, CIFAR-100, ImageNet, MNIST

## Limitations
- Purely simulated with a log-normal variation model; no device or chip measurements
- Speedup and energy are analytical estimates built on extrapolated baseline NAW at 1% accuracy drop and an ADC resolution/power scaling model
- Relies on weight distribution being concentrated within +-64 (true for the CNNs tested); transformer weights with larger outliers not evaluated
- Redundant mapping adds ~25% crossbar area; only variation and HRS offset modelled, not drift, IR drop or faults
- Only CNNs evaluated

## Remarks
A neat encoding-level fix whose results depend on the simulator assumptions; gains in NAW translate directly into ADC/throughput benefits, which is the key lever for analog PIM. The weight-distribution argument would need re-examination for LLMs, whose outlier weights/activations break the +-64 concentration. Closely related to Go Unary (Sun et al.) which it compares against, and to the IAC offset scheme (Park et al.).

## Cites (in collection, 6)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Notably, software-based techniques [4], [6], [7] have aimed to lessen the impact of ReRAM's variation by retraining or fine-tuning the DNNs to adapt to the non-ideal distribution of ReRAM resistance."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "Several works have been proposed to ensure reliable operations with a low Rratio ReRAM device [5], [9]-[12]."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _contrasts/critiques_: "There are also studies that use Error Correcting Code (ECC) to increase the variation-tolerability of the ReRAM-based PIM accelerators. [15]-[17] have used ECC such as AN code, Low Density Parity Check (LDPC) or successive error correction to lessen variation in the ReRAM-based PIM."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Processing-In Memory (PIM) architecture, utilizing Resistive Random Access Memory (ReRAM), offers a promising solution to address the limitations of conventional von Neumann architecture [1-3]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The simulations focus on a ReRAM-based DNN accelerator with a hardware configuration based on ISAAC architecture [1]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Processing-In Memory (PIM) architecture, utilizing Resistive Random Access Memory (ReRAM), offers a promising solution to address the limitations of conventional von Neumann architecture [1-3]."

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2023_Jang_VECOM_ICCAD.pdf](../../06_Nonidealities_and_Reliability/2023_Jang_VECOM_ICCAD.pdf)
- Full text: [../fulltext/2023_Jang_VECOM_ICCAD.txt](../fulltext/2023_Jang_VECOM_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccad57390.2023.10323803
