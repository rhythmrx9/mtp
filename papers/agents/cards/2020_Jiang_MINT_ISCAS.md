---
id: W3090816752
key: 2020_Jiang_MINT_ISCAS
title: "MINT: Mixed-Precision RRAM-Based IN-Memory Training Architecture"
short: "MINT"
year: 2020
venue: "ISCAS"
venue_full: "IEEE International Symposium on Circuits and Systems (ISCAS 2020)"
authors: "Hongwu Jiang, Shanshi Huang, Xiaochen Peng, Shimeng Yu"
category: "10 On-chip & Analog Training"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["on-chip-training", "mixed-precision", "crossbar-architecture", "bit-slicing"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 4
citations_overall: 27
priority_score: 3.94
doi: "https://doi.org/10.1109/iscas45731.2020.9181020"
pdf: null
fulltext: null
---

# MINT

**MINT: Mixed-Precision RRAM-Based IN-Memory Training Architecture** — IEEE International Symposium on Circuits and Systems (ISCAS 2020) (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
MINT splits DNN weights into MSBs (processed by transposable RRAM compute-in-memory arrays for forward/backward propagation) and LSBs (stored and updated in regular memory arrays), enabling on-chip training with ~91% CIFAR-10 accuracy, ~4.46 TOPS/W, 1.35x higher energy efficiency, and only 31.9% of the chip area versus a baseline RRAM CIM architecture.

## Summary
On-chip training of DNNs using compute-in-memory (CIM) is attractive for solving the memory-wall problem but is challenged by the need for higher weight precision and higher ADC resolution than inference-only CIM. MINT (Mixed-precision IN-memory Training) addresses this by splitting each multi-bit weight into most-significant bits (MSBs) and least-significant bits (LSBs): forward and backward propagation use CIM transposable RRAM arrays that store only the MSBs, while the weight update (which needs higher precision) is performed in regular (non-CIM) memory arrays that store the LSBs. The paper analyzes the impact of ADC resolution on training accuracy and evaluates training of a VGG-like CNN on CIFAR-10 under this mixed-precision architecture.

## Contributions
- A mixed-precision RRAM-based CIM training architecture (MINT) that splits weights into MSBs (in CIM transposable arrays) and LSBs (in regular memory arrays) to balance training precision needs against CIM hardware costs
- An analysis of how ADC resolution affects on-chip training accuracy under this split-precision scheme
- Evaluation of a VGG-like CNN trained on CIFAR-10 with the proposed architecture under realistic hardware constraints
- A chip-area and energy-efficiency comparison against baseline full-precision RRAM CIM training architectures

## Key claims (stable IDs)
- **2020_Jiang_MINT_ISCAS#C1** — MINT achieves competitive training accuracy on CIFAR-10 under realistic hardware (ADC resolution, mixed precision) constraints — _support:_ ~91% accuracy reported for a VGG-like network on CIFAR-10 (abstract) — _loc:_ Abstract
- **2020_Jiang_MINT_ISCAS#C2** — MINT improves energy efficiency over baseline RRAM CIM training architectures — _support:_ ~4.46 TOPS/W energy efficiency, 1.35x higher than baseline CIM architectures based on RRAM (abstract) — _loc:_ Abstract
- **2020_Jiang_MINT_ISCAS#C3** — MINT substantially reduces chip area versus a baseline full-precision CIM training architecture — _support:_ Only 31.9% of baseline chip size (~98.86 mm^2 at 32nm node) (abstract) — _loc:_ Abstract

## Results
- ~91% accuracy for VGG-like CNN on CIFAR-10 under hardware constraints
- ~4.46 TOPS/W energy efficiency
- 1.35x higher energy efficiency vs. baseline RRAM CIM architecture
- Chip area reduced to 31.9% of baseline (~98.86 mm^2 at 32nm technology node)

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Xplore is not downloadable here); exact MSB/LSB bit-split, ADC resolution values, and training hyperparameters could not be verified
- Evaluation limited to a single VGG-like network on CIFAR-10 per the abstract; generalization to larger/deeper networks or datasets is not addressed
- As a short ISCAS conference paper, the architectural and experimental detail is likely limited compared to a journal-length treatment

## Remarks
Based on the abstract, MINT is a concrete architectural proposal for the on-chip (analog) training problem, directly addressing the known tension between CIM's need for compact low-precision arrays and training's need for high weight-update precision, via an MSB/LSB split across CIM and conventional memory. The quantitative results (91% CIFAR-10 accuracy, 4.46 TOPS/W, ~32% baseline chip area) are notable but, lacking full-text access, cannot be independently checked against the exact baseline configuration or verified for consistency with the companion DNN+NeuroSim V2.0 benchmarking framework that is reported to cite it.

## Cites (in collection, 4)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 2)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _extends/builds-on_: "In CIM accelerators, to support on-chip training, we also implement extra peripheral circuits to calculate error and weight gradient in back-propagation (design as done in other works [14][15])."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)

## Files
- PDF: not available locally (save as `papers/10_On_Chip_and_Analog_Training/2020_Jiang_MINT_ISCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iscas45731.2020.9181020
