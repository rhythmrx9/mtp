---
id: W4402742347
key: 2024_Gu_VariationTolerantOUFramework_TCASI
title: "A Hardware Friendly Variation-Tolerant Framework for RRAM-Based Neuromorphic Computing"
short: "Variation-Tolerant OU Framework"
year: 2024
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers (2024)"
authors: "Fang-Yi Gu, Cheng‐Han Yang, Ing-Chao Lin, Da-Wei Chang, Darsen D. Lu, Ulf Schlichtmann"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "device-variation", "quantization", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 10
priority_score: 4.73
doi: "https://doi.org/10.1109/tcsi.2024.3443180"
pdf: null
fulltext: null
---

# Variation-Tolerant OU Framework

**A Hardware Friendly Variation-Tolerant Framework for RRAM-Based Neuromorphic Computing** — IEEE Transactions on Circuits and Systems I: Regular Papers (2024) (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A hardware-friendly variation-tolerant framework combines unary-based non-uniform weight quantization with a variation-aware Operation-Unit (OU) scheme (plus OU skipping/recombination/compensation) to cut RRAM conductance-variation-induced accuracy loss and ADC power on 2-bit-cell crossbars, outperforming prior methods on four NN models across two datasets.

## Summary
RRAM cells used in compute-in-memory DNN accelerators suffer from conductance variation that shifts stored weight values from their targets, degrading inference accuracy; the problem worsens as more wordlines/bitlines are concurrently activated, which also drives up ADC resolution requirements and power. The paper proposes a two-part methodology: a unary-based non-uniform quantization scheme that equalizes the significance of weights stored across RRAM cells (so that variation on any one cell matters less), and a variation-aware Operation-Unit (OU)-based framework that only activates RRAM cells belonging to the same OU simultaneously, limiting both the scope of variation accumulation and the required ADC resolution/power. Three additional techniques - OU skipping, OU recombination, and OU compensation - are introduced to further mitigate the residual impact of variations within and across OUs. The approach is evaluated with 2-bit cell resolution on four NN models across two datasets, and the authors report it outperforms the state of the art.

## Contributions
- Unary-based non-uniform quantization that equalizes per-cell weight significance to reduce sensitivity to conductance variation
- A variation-aware Operation-Unit (OU) based computation framework limiting concurrently activated wordlines/bitlines to control variation accumulation and ADC overhead
- Three refinement techniques - OU skipping, OU recombination, and OU compensation - to further reduce the impact of variations
- Evaluation across four NN models and two datasets at 2-bit RRAM cell resolution showing improvement over prior state-of-the-art variation-mitigation methods

## Key claims (stable IDs)
- **2024_Gu_VariationTolerantOUFramework_TCASI#C1** — The proposed unary-based non-uniform quantization plus variation-aware OU framework outperforms state-of-the-art variation-mitigation approaches — _support:_ 'the proposed approach outperforms the state-of-the-art among four NN models on two datasets with 2-bit cell resolution' (abstract) — _loc:_ Abstract
- **2024_Gu_VariationTolerantOUFramework_TCASI#C2** — Restricting simultaneous activation to RRAM cells within the same OU reduces required ADC resolution/power while mitigating variation impact — _support:_ stated motivation and mechanism in abstract/methodology description — _loc:_ Abstract

## Results
- Outperforms state-of-the-art variation-mitigation baselines across four NN models on two datasets at 2-bit cell resolution (specific accuracy/power numbers not available from abstract alone)

## Limitations
- Abstract-only analysis in this record: full text unavailable, so exact accuracy deltas, ADC power savings, and comparison baselines could not be verified
- Evaluation limited to 2-bit cell resolution; behavior at other cell resolutions not described in the abstract
- Relies on an OU-based restricted-parallelism scheme, which (as in related work such as BWQ) inherently trades off crossbar throughput for accuracy/robustness

## Remarks
This fits squarely into the non-ideality/reliability literature alongside works like Unary Coding and Variation-Aware Optimal Mapping (an in-set reference by the same OU/unary-coding lineage) and CASCADE; the combination of unary quantization with OU-level scheduling and three dedicated mitigation sub-techniques (skip/recombine/compensate) suggests an incremental but systematic engineering contribution to variation tolerance. Without full text, it is not possible to assess how the accuracy/ADC-power trade-off compares quantitatively to the cited ISAAC/PRIME baselines or how large the 2-bit-resolution constraint limits generality to higher-bit-cell designs.

## Cites (in collection, 8)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2024_Gu_VariationTolerantOUFramework_TCASI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcsi.2024.3443180
