---
id: W3131573445
key: 2021_Li_RaQu_TCAD
title: "An Automated Quantization Framework for High-Utilization RRAM-Based PIM"
short: "RaQu"
year: 2021
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Bing Li, Songyun Qu, Ying Wang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["quantization", "mixed-precision", "crossbar-architecture", "cnn-accelerator", "nas-codesign"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 20
priority_score: 3.43
doi: "https://doi.org/10.1109/tcad.2021.3061521"
pdf: null
fulltext: null
---

# RaQu

**An Automated Quantization Framework for High-Utilization RRAM-Based PIM** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
RaQu is an AutoML-based quantization framework for RRAM-based PIM that generates a fine-grained, hardware-structure-aware quantization strategy to maximize crossbar resource utilization, improving utilization by 29.2-37.4% and accuracy by 1.8-3.3% over prior coarse-grained quantization methods.

## Summary
The paper addresses resource under-utilization in RRAM-based processing-in-memory (PIM) DNN accelerators caused by a mismatch between neural-network layer structure and the fixed crossbar array geometry, which leaves many RRAM cells unused when deploying a network. Prior quantization approaches, the authors argue, ignore this hardware-structure information and therefore fail to improve utilization. RaQu is proposed as an automated quantization framework that leverages AutoML to generate a fine-grained quantization strategy jointly informed by the neural network model and the heterogeneous RRAM crossbar structure, aiming to fully utilize PIM hardware resources for any given model.

## Contributions
- Identification of the resource-utilization problem caused by mismatch between DNN layer dimensions and fixed RRAM crossbar array sizes under conventional (coarse-grained) quantization
- RaQu: an AutoML-driven quantization framework that incorporates hardware structure information (heterogeneous crossbar sizes) into the quantization search
- Joint consideration of model parameters and RRAM hardware information to automatically generate fine-grained, per-layer quantization strategies
- Demonstrated improvements in both resource utilization and model accuracy versus prior coarse-grained quantization baselines

## Key claims (stable IDs)
- **2021_Li_RaQu_TCAD#C1** — RaQu improves RRAM-based PIM resource utilization by 29.2% to 37.4% over prior coarse-grained quantization methods — _support:_ stated experimental result in the abstract — _loc:_ Abstract
- **2021_Li_RaQu_TCAD#C2** — RaQu simultaneously improves model accuracy by 1.8% to 3.3% over prior coarse-grained quantization methods — _support:_ stated experimental result in the abstract — _loc:_ Abstract

## Results
- 29.2%-37.4% improvement in RRAM-based PIM resource utilization versus coarse-grained quantization baselines
- 1.8%-3.3% improvement in model accuracy versus coarse-grained quantization baselines

## Limitations
- Full text not available to this review; specific networks/datasets evaluated, the AutoML search method details, and search cost were not independently verified beyond the abstract
- Analysis based only on the abstract; the exact definition and measurement methodology for 'resource utilization' is unknown from the abstract alone

## Remarks
RaQu targets a specific and often-overlooked inefficiency in RRAM PIM deployment: crossbar resource under-utilization due to layer/array size mismatch, complementing more commonly studied accuracy-vs-bitwidth quantization work by jointly optimizing for hardware utilization. The framing is similar in spirit to other hardware-aware quantization/mapping work in this collection (e.g., Mixed Precision Quantization for ReRAM-based DNN Inference Accelerators). Full-text verification was not possible from this environment, so this entry is abstract-only.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019)
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2021_Li_RaQu_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2021.3061521
