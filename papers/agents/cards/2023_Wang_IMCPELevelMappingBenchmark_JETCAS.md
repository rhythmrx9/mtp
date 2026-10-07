---
id: W4388052862
key: 2023_Wang_IMCPELevelMappingBenchmark_JETCAS
title: "Benchmarking DNN Mapping Methods for the in-Memory Computing Accelerators"
short: "IMC PE-Level Mapping Benchmark"
year: 2023
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems"
authors: "Yi‐Min Wang, Xuanyao Fong"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["benchmarking", "weight-mapping", "tiling-partitioning", "dataflow-pipelining", "crossbar-architecture"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 7
citations_overall: 11
priority_score: 6.56
doi: "https://doi.org/10.1109/jetcas.2023.3328864"
pdf: null
fulltext: null
---

# IMC PE-Level Mapping Benchmark

**Benchmarking DNN Mapping Methods for the in-Memory Computing Accelerators** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A systematic loop-unrolling-based taxonomy of processing-element-level DNN-to-crossbar mapping methods, paired with a mapping-oriented architecture and benchmarking framework, shows large design-space tradeoffs and finds a hybrid mapping scheme improves minimum execution time by up to 30% across public DNN benchmarks.

## Summary
While many works study which-layer-to-which-core (tile-level) mapping for in-memory computing accelerators, PE-level mapping (how a convolution's loops are unrolled onto a crossbar's rows/columns) had not been systematically studied for IMC. This paper categorizes PE-level mapping methods from a loop-unrolling perspective, analyzing their implications for input data reuse and output (partial-sum) data reduction. It then proposes a mapping-oriented PE architecture whose input/output datapaths are designed to support the various mapping methods, evaluated at 45nm technology for area efficiency and scalability. An accompanying evaluation framework captures architecture-level behavior to benchmark mapping methods across different DNN workloads, main-memory bandwidth, and digital-compute throughput assumptions. The benchmarking reveals significant design-space tradeoffs between mapping choices and that no single mapping method is best across all conditions, motivating a hybrid-mapping scheme that switches mapping strategy to minimize execution time, improving it by up to 30% over the best single static mapping method across public DNN benchmarks.

## Contributions
- A loop-unrolling-based taxonomy of PE-level (within-crossbar) DNN mapping methods for in-memory computing, analyzed for input reuse and output reduction implications
- A mapping-oriented PE architecture with input/output datapaths designed to flexibly support multiple mapping methods, evaluated at 45nm for area efficiency/scalability
- An evaluation/benchmarking framework spanning DNN workloads, memory bandwidth, and digital-compute throughput to quantify mapping-method tradeoffs
- A hybrid-mapping scheme combining multiple PE-level mapping strategies, improving minimum execution time by up to 30% over public DNN benchmarks

## Key claims (stable IDs)
- **2023_Wang_IMCPELevelMappingBenchmark_JETCAS#C1** — No single static PE-level mapping method is best across all workloads/conditions; a hybrid-mapping scheme improves execution time — _support:_ hybrid-mapping scheme enhances minimum execution time by up to 30% for the publicly available DNN benchmarks — _loc:_ Abstract

## Results
- Up to 30% improvement in minimum execution time from hybrid mapping vs. single-mapping-method baselines across public DNN benchmarks
- Mapping-oriented PE architecture evaluated at 45nm technology shows good area efficiency and scalability

## Limitations
- Analysis based on abstract only (full text not accessible); the specific loop-unrolling taxonomy, benchmark networks, and quantitative tradeoff curves could not be verified
- 45nm technology node evaluation is relatively old relative to modern IMC chip demonstrations (e.g., 14nm PCM chips), which may limit direct comparability to state-of-the-art accelerators

## Remarks
This is a mapping/dataflow-focused systematization paper that fills a specific gap (PE-level, i.e., intra-crossbar loop-unrolling mapping) distinct from tile-/layer-level mapping studied elsewhere (e.g., AERO, Xbar-Partitioning in the same in-set reference list). It has already attracted forward citations from DNN-to-PIM compiler frameworks (PIMCOMP, PIMapping, JADE), indicating it is being used as a reference taxonomy for mapping-space exploration; full-text access would help confirm how its loop-unrolling categories map onto commonly used crossbar dataflow terms (weight-stationary, output-stationary, etc.).

## Cites (in collection, 7)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022)
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)

## Cited by (in collection, 3)
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "Furthermore, a reconfigurable architecture is introduced in [32] to support different unfolding strategies."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _contrasts/critiques_: "Existing memory-centric dataflow exploration frameworks [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25] are predominantly tailored for conventional neural networks (NNs) and fall short in addressing the design challenges of LLMs."
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2023_Wang_IMCPELevelMappingBenchmark_JETCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jetcas.2023.3328864
