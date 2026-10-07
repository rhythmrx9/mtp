---
id: W3091895175
key: 2020_Qu_RaQu_DAC
title: "RaQu: An automatic high-utilization CNN quantization and mapping framework for general-purpose RRAM Accelerator"
short: "RaQu"
year: 2020
venue: "DAC"
venue_full: "57th ACM/IEEE Design Automation Conference (DAC 2020)"
authors: "Songyun Qu, Bing Li, Ying Wang, Dawen Xu, Xiandong Zhao, Lei Zhang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["quantization", "mixed-precision", "weight-mapping", "compiler-software-stack"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 3
citations_overall: 40
priority_score: 6.96
doi: "https://doi.org/10.1109/dac18072.2020.9218724"
pdf: null
fulltext: null
---

# RaQu

**RaQu: An automatic high-utilization CNN quantization and mapping framework for general-purpose RRAM Accelerator** — 57th ACM/IEEE Design Automation Conference (DAC 2020) (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
RaQu is an AutoML-based, array-aware mixed-precision quantization and mapping framework that uses a two-stage learning and array-aware grouping strategy to search fine-grained per-parameter bit-widths, improving RRAM crossbar resource utilization by 18.2%-36.1% and accuracy by 0.9%-3.3% over prior coarse-grained quantization methods.

## Summary
Mapping an arbitrary CNN architecture onto a general-purpose RRAM crossbar accelerator for edge inference often leads to severe underutilization of crossbar resources, because fixed/coarse-grained bit-widths do not match the network's actual parameter distribution. Manually tuning per-parameter bit-widths at scale is impractical. RaQu proposes an AutoML-based array-aware quantization and mapping framework that automatically generates fine-grained mixed-precision CNNs, using a two-stage learning process together with an array-aware grouping strategy to make the otherwise huge bit-width search space tractable. The framework targets both resource (crossbar) utilization and model accuracy jointly, reporting improvements over prior coarse-grained quantization/mapping methods.

## Contributions
- An AutoML-based array-aware quantization and mapping framework (RaQu) that generates fine-grained, mixed-precision CNNs tailored to RRAM crossbar resource utilization
- A two-stage learning strategy to make bit-width search tractable across a huge per-parameter search space
- An array-aware grouping strategy that aligns quantization granularity with the RRAM crossbar's physical array structure
- Demonstrated improvements in both resource utilization and model accuracy over prior coarse-grained quantization/mapping baselines

## Key claims (stable IDs)
- **2020_Qu_RaQu_DAC#C1** — RaQu substantially improves RRAM crossbar resource utilization over prior coarse-grained quantization methods — _support:_ 18.2%-36.1% improvement in resource utilization (abstract) — _loc:_ Abstract
- **2020_Qu_RaQu_DAC#C2** — RaQu simultaneously improves model accuracy over prior coarse-grained quantization methods — _support:_ 0.9%-3.3% increase in model accuracy (abstract) — _loc:_ Abstract
- **2020_Qu_RaQu_DAC#C3** — Automated (AutoML-based) bit-width search is necessary because manual per-parameter bit-width selection is impractical at scale — _support:_ Abstract: 'Selecting the bit-width for the vast parameters is impractically completed by human labor' — _loc:_ Abstract

## Results
- 18.2%-36.1% improvement in resource utilization versus prior coarse-grained quantization methods
- 0.9%-3.3% increase in model accuracy versus prior coarse-grained quantization methods

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Xplore/ACM DL are not downloadable here); specific networks, datasets, crossbar sizes, and search cost/runtime of the AutoML search could not be verified
- As a DAC conference paper, experimental breadth may be more limited than a journal-length treatment

## Remarks
Based on the abstract, RaQu sits in the mapping/compilation space alongside other quantization-and-mapping frameworks in this collection (e.g., the energy-efficient quantized training framework, the configurable multi-precision RRAM framework it cites), specifically targeting the mismatch between a trained CNN's natural per-layer/per-parameter precision needs and a general-purpose RRAM accelerator's crossbar granularity. The reported gains (resource utilization and accuracy) are both abstract-stated ranges rather than single numbers, so the actual operating point and cost of the AutoML search (a known concern for such frameworks) could not be assessed without the full text.

## Cites (in collection, 3)
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 5)
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "For example, RaQu [18] processes the layer-wise quantization and further finetunes the bit width of groups of weights."
- [2024_Chowdhury_MELISO_ICONS](2024_Chowdhury_MELISO_ICONS.md) MELISO (2024) — _background_: "Extensive literature exists on benchmarking frameworks designed to evaluate RRAM device performance and integration with CMOS peripheral circuitry for a variety of computational tasks such as image classification with fully connected and convolutional neural networks [19-21], as well as dot product engines [22]."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2020_Qu_RaQu_DAC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/dac18072.2020.9218724
