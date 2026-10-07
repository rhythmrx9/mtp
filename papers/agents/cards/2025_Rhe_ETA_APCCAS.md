---
id: W7130560115
key: 2025_Rhe_ETA_APCCAS
title: "ETA: Efficient Transformer Attention Mapping for ReRAM-Based Compute-In-Memory Architectures"
short: "ETA"
year: 2025
venue: "APCCAS"
venue_full: "IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2025)"
authors: "Johnny Rhe, Juhong Park, Kang Eun Jeon, Jong Hwan Ko"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer", "ViT", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "weight-mapping", "dataflow-pipelining", "scheduling"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 5
citations_overall: 0
priority_score: 5.0
doi: "https://doi.org/10.1109/apccas67402.2025.11377506"
pdf: null
fulltext: null
---

# ETA

**ETA: Efficient Transformer Attention Mapping for ReRAM-Based Compute-In-Memory Architectures** — IEEE Asia Pacific Conference on Circuits and Systems (APCCAS 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ETA is a mapping strategy for transformer attention on ReRAM-based CIM that overlaps computation with the frequent memory writes attention requires and reduces array count via array-aware mapping, cutting waiting-for-write time by up to 66%, latency by up to 20%, and array count by up to 29% versus prior methods on DeiT-small and GPT2-small (64x64 arrays).

## Summary
The paper targets the mismatch between transformer attention mechanisms and compute-in-memory (CIM) architectures: unlike static weight matrices, attention involves dynamically generated Q/K/V and attention-score matrices that must be frequently written into ReRAM arrays, and compute-write dependencies force the accelerator to wait for writes to finish before computing, inflating latency and wasting resources. ETA (Efficient Transformer Attention mapping) addresses the compute-write bottleneck by enabling parallel execution of computation and memory writes, so that a new write can proceed while a different computation is still utilizing the array, and reduces the number of required ReRAM arrays via an array-aware mapping strategy. The combination of overlap-friendly scheduling and reduced array footprint is evaluated on DeiT-small (a vision transformer) and GPT2-small using 64x64 ReRAM arrays, where ETA reduces waiting-for-write (W4W) time, overall latency, and array count versus prior state-of-the-art mapping methods.

## Contributions
- Identifies compute-write dependency as a key bottleneck for mapping transformer attention onto ReRAM CIM
- Proposes parallel execution of computation and memory writes to hide write latency behind other arrays' computation
- Array-aware mapping strategy that reduces the number of ReRAM arrays required for attention computation
- Evaluation on DeiT-small and GPT2-small with 64x64 arrays against prior state-of-the-art attention-mapping methods

## Key claims (stable IDs)
- **2025_Rhe_ETA_APCCAS#C1** — ETA substantially reduces time spent waiting for crossbar writes during attention computation — _support:_ Reduces waiting-for-write (W4W) by up to 66% vs. previous state-of-the-art methods — _loc:_ Abstract
- **2025_Rhe_ETA_APCCAS#C2** — ETA's optimizations translate into end-to-end latency reduction — _support:_ Latency reduced by up to 20% — _loc:_ Abstract
- **2025_Rhe_ETA_APCCAS#C3** — ETA's array-aware mapping reduces hardware resource (array) requirements — _support:_ Fewer arrays by up to 29% — _loc:_ Abstract

## Results
- Up to 66% reduction in waiting-for-write (W4W) time vs. previous state-of-the-art
- Up to 20% latency reduction vs. previous state-of-the-art
- Up to 29% fewer arrays required vs. previous state-of-the-art
- Evaluated on DeiT-small and GPT2-small using 64x64 ReRAM arrays

## Limitations
- Full text not accessible to this reviewer (APCCAS is not downloadable here and no arXiv preprint was found); the identity/configuration of the 'previous state-of-the-art' baselines could not be verified
- Evidence basis is simulation; only two model families evaluated (DeiT-small, GPT2-small), both at a single array size (64x64)

## Remarks
Abstract-only assessment: APCCAS proceedings are not downloadable here and no preprint was found. The compute-write dependency problem for dynamic attention tensors on ReRAM CIM is a well-recognized challenge for mapping transformers to crossbars (since ReRAM writes are far slower/costlier than reads), and this paper's focus on overlapping writes with computation plus array-aware mapping is directly relevant to the mapping/compilation theme of this literature map; the magnitude of gains should be read against whatever specific baseline mapping schemes (e.g., ReTransformer/X-Former-style approaches) the full paper compares to.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2025_Rhe_ETA_APCCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/apccas67402.2025.11377506
