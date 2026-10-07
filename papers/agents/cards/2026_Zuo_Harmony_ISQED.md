---
id: W7162657777
key: 2026_Zuo_Harmony_ISQED
title: "Harmony: A Hardware-Mapping Co-Exploration Framework for Hybrid CIM-based Vision Transformer Accelerator"
short: "Harmony"
year: 2026
venue: "ISQED"
venue_full: "International Symposium on Quality Electronic Design (ISQED 2026)"
authors: "Yihang Zuo, Fu Zexin, Cong Wang, Yuchao Wu, Jiayi Huang, Yuzhe Ma"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["SRAM-analog", "Memristor(generic)"]
models: ["ViT", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["heterogeneous-analog-digital", "transformer-accelerator", "tiling-partitioning", "scheduling", "attention"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 13
citations_overall: 0
priority_score: 5.0
doi: "https://doi.org/10.1109/isqed69900.2026.11534775"
pdf: null
fulltext: null
---

# Harmony

**Harmony: A Hardware-Mapping Co-Exploration Framework for Hybrid CIM-based Vision Transformer Accelerator** — International Symposium on Quality Electronic Design (ISQED 2026) (2026)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Harmony is a hardware-mapping co-exploration framework for hybrid CIM-based vision transformer accelerators that uses a knowledge-guided grid search and an improved genetic algorithm to jointly search CIM macro hardware configuration and spatial mapping, reporting 48% area reduction, 13% latency reduction, 32% energy reduction and 1.27x average energy efficiency versus a baseline, while trading off accuracy against all-SRAM designs.

## Summary
The paper targets the difficulty of automating high-performance CIM-based transformer accelerator design: unlike CNNs, where CIM-based acceleration is mature, the design space for hybrid/heterogeneous CIM-based vision transformer (ViT) accelerators is extremely large due to complex model structure and dataflow, covering both hardware configuration (CIM macro parameters) and spatial mapping. Harmony defines a universal design-space representation for implementing ViTs on hybrid, heterogeneous CIM accelerators and proposes two search algorithms to navigate it efficiently: a knowledge-guided grid search (KGGS) that uses orthogonal-experiment and dominance analysis to find stable exploration probabilities for different parameters, and an improved genetic algorithm (IGA) with a unique order-crossover and swapping-mutation scheme that preserves relative order to avoid costly legalization steps during iteration. Performance experiments show Harmony's co-explored designs achieve notable area, latency, and energy improvements over a baseline, while accuracy experiments show the hybrid (non-all-SRAM) architecture trades some accuracy for these efficiency gains relative to all-SRAM CIM-based accelerators.

## Contributions
- A universal design-space representation for hybrid/heterogeneous CIM-based vision transformer accelerators (hardware configuration + spatial mapping)
- Knowledge-guided grid search (KGGS) using orthogonal experiment design and dominance analysis to efficiently explore parameter space
- Improved genetic algorithm (IGA) with order-crossover and swapping-mutation that preserves relative order to skip legalization steps
- Quantitative evaluation of area/latency/energy gains and an accuracy tradeoff analysis vs. all-SRAM CIM baselines

## Key claims (stable IDs)
- **2026_Zuo_Harmony_ISQED#C1** — Harmony's co-exploration achieves substantial area, latency and energy improvements over the baseline design — _support:_ 48% area reduction, 13% latency reduction, 32% energy reduction, and 1.27x energy efficiency on average compared with the baseline — _loc:_ Abstract
- **2026_Zuo_Harmony_ISQED#C2** — The hybrid CIM-based architecture trades off some accuracy relative to all-SRAM CIM-based accelerators — _support:_ Abstract: 'hybrid architecture achieves a trade-off between accuracy and performance compared with all-SRAM CIM-based accelerators' — _loc:_ Abstract

## Results
- 48% area reduction vs. baseline
- 13% latency reduction vs. baseline
- 32% energy reduction vs. baseline
- 1.27x average energy efficiency vs. baseline

## Limitations
- Full text not accessible to this reviewer (ISQED is not downloadable here and no arXiv preprint was found); baseline definition, benchmarked ViT models, and the exact accuracy tradeoff numbers could not be verified
- Accuracy is explicitly described as trading off against all-SRAM designs, implying the efficiency gains come partly from using lower-accuracy (presumably analog/ReRAM) macros alongside SRAM

## Remarks
Abstract-only assessment: ISQED proceedings are not downloadable here and no preprint was found. This is a mapping/design-space-exploration contribution much like other DSE frameworks in this collection (e.g., JADE, Gibbon/MNSIM-style co-exploration tools it cites), specifically targeting the harder, more heterogeneous design space created by hybrid CIM for ViTs; the explicit accuracy-vs-efficiency tradeoff disclosure is a useful honesty signal, but without the full text the real-world significance of the 13-48% gains relative to a possibly weak baseline cannot be judged.

## Cites (in collection, 13)
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024)
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2026_Zuo_Harmony_ISQED.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/isqed69900.2026.11534775
