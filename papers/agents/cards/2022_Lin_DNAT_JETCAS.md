---
id: W4226427756
key: 2022_Lin_DNAT_JETCAS
title: "D-NAT: Data-Driven Non-Ideality Aware Training Framework for Fabricated Computing-In-Memory Macros"
short: "D-NAT"
year: 2022
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), vol. 12, no. 2, June 2022"
authors: "Ming-Guang Lin, Chi-Tse Huang, Yu-Chuan Chuang, Yi-Ta Chen, Ying–Tuan Hsu, Yukai Chen, Jyun‐Jhe Chou, Tsung-Te Liu, Chi‐Sheng Shih, An-Yeu Andy Wu"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["SRAM-analog"]
models: ["CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["hardware-aware-training", "noise-injection", "chip-in-the-loop", "analog-mvm", "adc-dac", "quantization", "calibration-compensation", "macro"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 3
citations_overall: 10
priority_score: 4.23
doi: "https://doi.org/10.1109/jetcas.2022.3171268"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2022_Lin_DNAT_JETCAS.pdf"
fulltext: "../fulltext/2022_Lin_DNAT_JETCAS.txt"
---

# D-NAT

**D-NAT: Data-Driven Non-Ideality Aware Training Framework for Fabricated Computing-In-Memory Macros** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), vol. 12, no. 2, June 2022 (2022)

## TL;DR
D-NAT trains DNNs against a MAC-error model measured on a fabricated 7-bit-DAC SRAM-based CIM macro (plus a statistical gradient estimator and learnable-range E-PACT activation quantization), recovering VGG8/CIFAR-10 on-chip accuracy from 14.17% to 87.17% (ideal-CIM software bound 88.33%).

## Summary
CIM accelerators suffer MAC errors from array and peripheral (DAC/ADC) non-idealities, and prior analytical non-ideality-aware training (A-NAT) relies on pre-defined Gaussian-type models not validated on fabricated silicon. The authors build an FPGA test setup around a fabricated SRAM-based CIM macro (64 7-bit current-steering DACs, 16 computation banks, unified charge-processing network equivalent to 16 7-bit ADCs, filter depth up to 64, 1-bit weights, 7-bit inputs and partial sums) and record measured outputs against theoretical outputs while running VGG8 on CIFAR-10 to obtain a data-driven MAC error model (D-MAC-EM), a discrete probability distribution that distorts more at larger values and differs markedly from a Gaussian analytical model (A-MAC-EM). VGG8 layers 2-5 are mapped to the macro (e.g., conv2 with 64 in/128 out channels uses 8 banks, four channels per column, 16 weight reloads). Training incorporates the D-MAC-EM through a statistical training mechanism (gradient estimator using the measured distribution instead of STE) and E-PACT, which learns both upper and lower activation clipping bounds per layer. Simulation covers ResNet20, VGG8 (CIFAR-10), ResNet34 and VGG16 (CIFAR-100); on-chip validation runs 600 CIFAR-10 images, with the first conv layer on the macro and the remaining layers evaluated with the D-MAC-EM.

## Contributions
- Measured data-driven MAC error model (D-MAC-EM) of a fabricated SRAM CIM macro and showing the analytical A-MAC-EM is insufficient
- Statistical training mechanism using the measured discrete error distribution for gradient estimation (+0.55% ResNet20, +1.3% VGG8 over STE)
- Extended PACT (E-PACT) with learned upper and lower activation bounds (+1.1-30.1% ResNet20, +0.51-12.06% VGG8 over other quantizers)
- Simulation on four models and on-chip validation on the fabricated macro without added circuits

## Key claims (stable IDs)
- **2022_Lin_DNAT_JETCAS#C1** — D-NAT improves accuracy of ResNet20, VGG8, ResNet34 and VGG16 under the measured non-idealities by 78.98%, 71.8%, 72.04% and 57.85%, reaching the ideal quantized-model bound — _support:_ Table III vs Non-Ideal CIM — _loc:_ Sec. V-D, Table III
- **2022_Lin_DNAT_JETCAS#C2** — On the fabricated macro D-NAT lifts VGG8 accuracy from 14.17% to 87.17% on 600 CIFAR-10 images — _support:_ Ideal-CIM-trained model 14.17% (a 74.16% drop from 88.33%) — _loc:_ Sec. VI, Table IV
- **2022_Lin_DNAT_JETCAS#C3** — Analytical Gaussian-based MAC error models do not capture the practical non-idealities of the macro — _support:_ A-NAT only slightly improves accuracy and remains low; D-MAC-EM distorts more at large outputs — _loc:_ Fig. 5-6, Sec. V-D
- **2022_Lin_DNAT_JETCAS#C4** — Training overhead is about 5x time and 2x GPU memory relative to FP32 training — _support:_ stated one-time offline cost — _loc:_ Sec. VI

## Results
- Software: FP32 90.1% and Ideal CIM 88.33% on the 600-image subset
- On-chip: Ideal-CIM-trained 14.17% versus D-NAT 87.17% (VGG8, CIFAR-10)
- Simulation recoveries: ResNet20 +78.98%, VGG8 +71.8%, ResNet34 +72.04% (CIFAR-100), VGG16 +57.85% (CIFAR-100)
- Hardware setting: 7-bit input, 1-bit weight, 7-bit partial sums; SGD 256 epochs, batch 128

## Key numbers
- array_size: 16 banks x 16 columns x 64 bitcells (64-deep filters)
- accuracy: 87.17% on-chip VGG8 CIFAR-10 (600 images); ideal bound 88.33%
- bits_weight: 1b
- bits_adc: 7b input DAC, 7b partial sum

## Datasets / benchmarks
CIFAR-10, CIFAR-100

## Limitations
- On-chip validation only on 600 images; only the first conv layer actually ran on the macro, remaining layers were emulated with the measured D-MAC-EM
- 1-bit weights and a single macro; model is specific to this chip and requires re-measurement per chip/macro
- SRAM-based digital-analog CIM, not NVM; claim of applicability to emerging memories is untested
- About 5x training time and 2x GPU memory overhead
- No transformers or language models

## Remarks
A convincing demonstration that measured, data-dependent error distributions beat Gaussian noise models for HWA training, with real silicon evidence (though only partially on-chip). Contrasts with IBM-style generic noise models (Rasch et al.) that avoid chip-specific calibration; here the trade-off is per-chip measurement for much higher recovery at 1-bit weights. Limited relevance to analog LM deployment beyond the methodological lesson of chip-calibrated noise models.

## Cites (in collection, 3)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Recently, computingin-memory (CIM) [5, 6] mechanism has been proposed as a promising solution to the von-Neumann bottleneck through the integration of computational units and memories."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _uses-method-or-tool_: "On the other hand, to develop the A-MAC-EM for the target SRAM-based CIM macro, we assume the variation mainly occurs in ADC and DAC [28]."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021) — _baseline/comparison_: "In [20], an iterative training algorithm was proposed to regularize model parameters to fit into a linear operating range of 1T1R cells in a layer-by-layer manner to compensate for the accuracy degradation."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2022_Lin_DNAT_JETCAS.pdf](../../07_Hardware_Aware_Training_and_Robustness/2022_Lin_DNAT_JETCAS.pdf)
- Full text: [../fulltext/2022_Lin_DNAT_JETCAS.txt](../fulltext/2022_Lin_DNAT_JETCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jetcas.2022.3171268
