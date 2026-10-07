---
id: W4415179271
key: 2025_Zhu_PIMapping_TCAD
title: "PIMapping: A Tile-Level Dataflow Optimization Framework for PIM Architecture"
short: "PIMapping"
year: 2025
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025, early access)"
authors: "Ziqian Zhu, Yifei Zhou, Jinsen Zhu, Yuxuan Wang, Hongbing Pan"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["dataflow-pipelining", "tiling-partitioning", "compiler-software-stack", "scheduling"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 13
citations_overall: 0
priority_score: 4.5
doi: "https://doi.org/10.1109/tcad.2025.3621513"
pdf: null
fulltext: null
---

# PIMapping

**PIMapping: A Tile-Level Dataflow Optimization Framework for PIM Architecture** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025, early access) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
PIMapping is an analytical framework for tile-based PIM accelerators that uses a tile-level dataflow IR, a data-proximity mapping method and congestion-aware scheduling to cut inter-tile communication latency and bandwidth versus prior mapping frameworks.

## Summary
Hierarchical tile-based PIM accelerators exploit multi-layer parallelism, but existing dataflow analysis uses computational models and metrics that do not fit tile-level dataflows. PIMapping defines a general tile-level dataflow representation as an IR for multi-layer DNN mapping and scheduling. On top of it, a data-proximity-based mapping places layers/weight blocks on tiles to minimise inter-tile communication, and a congestion-aware scheduler reduces inter-tile communication conflicts. Case studies map common DNNs onto several PIM architectures and report improvements over the state-of-the-art mapping framework in communication latency, required inter-tile bandwidth and pipeline efficiency.

## Contributions
- General tile-level dataflow representation used as an IR for multi-layer mapping and scheduling
- Data-proximity-based tile mapping to minimise inter-tile communication
- Congestion-aware scheduling to reduce inter-tile communication conflicts
- Case studies across several tile-based PIM architectures

## Key claims (stable IDs)
- **2025_Zhu_PIMapping_TCAD#C1** — Existing dataflow analysis models/metrics are unsuitable for tile-level dataflows in tile-based PIM. — _support:_ Motivation stated in abstract — _loc:_ Abstract
- **2025_Zhu_PIMapping_TCAD#C2** — PIMapping improves communication latency, inter-tile bandwidth requirement and pipeline efficiency over the state-of-the-art mapping framework. — _support:_ Abstract states 'significant improvements'; magnitudes not given in abstract — _loc:_ Abstract

## Results
- Reported improvements in communication latency, inter-tile bandwidth and pipeline efficiency vs. state-of-the-art mapping framework (magnitudes not available from abstract)

## Limitations
- Abstract-only analysis; no numbers available
- Analytical model; no cycle-accurate or silicon validation indicated
- Focus on inter-tile communication; intra-crossbar effects (ADC cost, non-idealities, accuracy) out of scope
- Workloads described only as 'common DNN algorithms'

## Remarks
Addresses the NoC/inter-tile side of mapping, which ISAAC/PUMA-style designs largely abstract away and which becomes dominant once layers are pipelined across many tiles. It sits alongside PIMCOMP, CIM-MLC and AERO-style mappers; the lack of quantitative claims in the abstract makes it hard to judge its margin over them without the full text.

## Cites (in collection, 13)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020)
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023)
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2025_Zhu_PIMapping_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2025.3621513
