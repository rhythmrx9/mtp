---
id: W7160523127
key: 2026_Wang_TriCIM_TVLSI
title: "TriCIM: A General CIM-Capacity-Aware Framework for Optimizing Model, Layer, and Tile-Stationary Dataflows in CIM Accelerators"
short: "TriCIM"
year: 2026
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2026)"
authors: "Yi-Xiang Wang, Yufu Zhang, Longyang Lin"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM", "SRAM-analog"]
models: ["DNN (unspecified)"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["dataflow-pipelining", "tiling-partitioning", "scheduling", "compiler-software-stack"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 0
priority_score: 4.5
doi: "https://doi.org/10.1109/tvlsi.2026.3688907"
pdf: null
fulltext: null
---

# TriCIM

**TriCIM: A General CIM-Capacity-Aware Framework for Optimizing Model, Layer, and Tile-Stationary Dataflows in CIM Accelerators** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2026) (2026)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
TriCIM splits the CIM dataflow space into model-, layer- and tile-stationary regions based on CIM capacity vs. model size and applies region-specific optimisations (load balancing, layer grouping, weight-update scheduling, tiling, inter-tile ordering), achieving 1.1x-13.2x runtime speedup over state-of-the-art frameworks.

## Summary
CIM dataflow frameworks tend to target a narrow range of architectures or dataflow types and often ignore CIM-specific features such as weight-update scheduling when weights do not fit. TriCIM introduces a CIM-capacity-aware formulation: depending on how the available CIM capacity compares with model size, a mapping falls into model-stationary (whole model resident), layer-stationary, or tile-stationary (weights must be reloaded per tile) regions. For each region it identifies the dominant bottleneck and applies tailored optimisations: load balancing, layer grouping, weight-update scheduling, tiling and inter-tile ordering. Evaluation across various CIM accelerators and representative NN models reports that TriCIM consistently finds optimal dataflows with 1.1x to 13.2x runtime speedup over state-of-the-art frameworks.

## Contributions
- CIM-capacity-aware taxonomy of the dataflow space into model-, layer- and tile-stationary regions
- Region-specific bottleneck analysis
- Optimisations: load balancing, layer grouping, weight-update scheduling, tiling, inter-tile ordering
- Evaluation across multiple CIM accelerator configurations and NN models

## Key claims (stable IDs)
- **2026_Wang_TriCIM_TVLSI#C1** — The CIM dataflow space can be partitioned by CIM capacity vs. model size into three regions with distinct bottlenecks. — _support:_ Core formulation in abstract — _loc:_ Abstract
- **2026_Wang_TriCIM_TVLSI#C2** — TriCIM outperforms state-of-the-art CIM dataflow frameworks in runtime. — _support:_ '1.1x to 13.2x runtime speedup compared to state-of-the-art frameworks' — _loc:_ Abstract
- **2026_Wang_TriCIM_TVLSI#C3** — TriCIM consistently finds optimal dataflows across diverse CIM accelerators. — _support:_ Stated in abstract — _loc:_ Abstract

## Results
- 1.1x-13.2x runtime speedup vs. state-of-the-art CIM dataflow frameworks (abstract)

## Limitations
- Abstract-only analysis; architectures, models and baselines not verified
- Device list is an inference (framework is device-agnostic; weight-update scheduling suggests capacity-limited, e.g. SRAM, CIM)
- 'Optimal' presumably relative to its own cost model
- Performance-only; no accuracy/non-ideality modelling indicated

## Remarks
The capacity-region framing is a clean way to reason about when the 'weights stay in the crossbar' assumption of ISAAC/PUMA-style mapping breaks, which is exactly the regime of large transformers on limited CIM capacity. Weight-update scheduling is especially relevant to NVM CIM where writes are slow/costly, though the abstract does not quantify write costs.

## Cites (in collection, 10)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Cui_ARES_ICCAD](2023_Cui_ARES_ICCAD.md) ARES (2023)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024)
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024)
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024)
- [2025_Zhang_ASiM_TVLSI](2025_Zhang_ASiM_TVLSI.md) ASiM (2025)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2026_Wang_TriCIM_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2026.3688907
