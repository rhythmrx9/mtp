---
id: W7117258492
key: 2025_Sun_DuoPIM_TCAD
title: "DuoPIM: RRAM–DRAM Hybrid PIM Acceleration for Flexible-Batch LLM Decoding"
short: "DuoPIM"
year: 2025
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Xiaotian Sun, Xinyu Wang, Wanqian Li, Xueqi Li, Chunmeng Dou, Yinhe Han, Xiaoming Chen"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "DRAM"]
models: ["Transformer", "GPT/LLM"]
lm_models: []
param_scale: "not specified"
slm: true
evidence: simulation
topics: ["heterogeneous-analog-digital", "transformer-accelerator", "language-models", "scheduling", "dataflow-pipelining"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 2
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/tcad.2025.3648674"
pdf: null
fulltext: null
---

# DuoPIM

**DuoPIM: RRAM–DRAM Hybrid PIM Acceleration for Flexible-Batch LLM Decoding** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
DuoPIM is a hybrid RRAM+DRAM processing-in-memory architecture for LLM decoding that maps weight-heavy FC layers to batch-insensitive RRAM in-situ compute and cache-dependent attention to DRAM-PIM, with architectural and scheduling innovations to keep both resource types well utilized across batch sizes.

## Summary
The paper targets the batch-size dilemma in LLM decoding: batching boosts FC-layer throughput on GPUs but inflates the KV-cache demands of attention layers, and existing DRAM-PIM accelerators for attention are underutilized at small batch sizes while RRAM-based in-situ compute for FC layers is insensitive to batch size because it avoids weight reloading. DuoPIM proposes a hybrid architecture that assigns RRAM to FC layers and DRAM-PIM to attention layers to escape the batch-size-throughput tradeoff, but notes that naively scaling existing RRAM designs misaligns with LLM compute/storage demands and that DRAM-PIM suffers from attention's irregular computational pattern. To address this, DuoPIM decouples RRAM's storage and compute into a hierarchical architecture, makes minimal DRAM-PIM modifications to support online softmax, and introduces scheduling strategies across multiple architectural levels to improve resource utilization in the hybrid system. Evaluations reportedly show DuoPIM can fully exploit computing capacity across a range of batch sizes, addressing the utilization problems of each memory technology used alone.

## Language models evaluated
- Models: —
- Scale: not specified
- Note: Only the abstract was available; it names no specific LLMs or scales, targeting RRAM (FC layers) plus DRAM-PIM (attention) decoding.

## Contributions
- Hybrid RRAM (for FC layers) + DRAM-PIM (for attention) architecture that targets batch-size-insensitive LLM decoding throughput
- Hierarchical RRAM architecture that decouples storage and compute capabilities to better match LLM compute/storage demands
- Minimal DRAM-PIM modifications to support online softmax computation for attention
- Multi-level scheduling strategies to coordinate the two PIM subsystems and improve resource utilization across batch sizes

## Key claims (stable IDs)
- **2025_Sun_DuoPIM_TCAD#C1** — RRAM-based FC-layer acceleration is insensitive to batch size because it avoids weight-loading overhead, unlike GPU-based approaches — _support:_ Abstract: 'emerging non-volatile RRAM technology offers batch size-insensitive acceleration for FC layers through highly parallel in-situ computations by eliminating weight loading overhead' — _loc:_ Abstract
- **2025_Sun_DuoPIM_TCAD#C2** — DuoPIM's hybrid design keeps computing capacity well utilized across various batch sizes, unlike pure DRAM-PIM attention accelerators — _support:_ Abstract: 'Evaluations demonstrate DuoPIM's ability to fully leverage computing capacity across various batch sizes' — _loc:_ Abstract

## Results
- No specific quantitative throughput/energy numbers available from the abstract alone; full text was not accessible

## Limitations
- Full text not accessible to this reviewer (TCAD is not downloadable here and no arXiv preprint was found); baselines and quantitative results could not be verified
- Evidence basis is simulation (architectural/system-level), not measured silicon

## Remarks
Abstract-only assessment: IEEE Xplore (TCAD) is not downloadable in this environment and no preprint was found. The core architectural insight — splitting the LLM decode workload so that weight-dominated FC layers go to batch-insensitive RRAM in-situ compute while cache-dependent attention goes to DRAM-PIM — is a sensible way to avoid the respective underutilization failure modes of each memory technology alone, and fits within the broader trend of heterogeneous/hybrid PIM designs for LLM inference (c.f. HyPIM, ASMA in this same batch). Without the full text, the magnitude of utilization/throughput gains and the realism of the cross-technology scheduling overhead cannot be assessed.

## Cites (in collection, 2)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2025_Sun_DuoPIM_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2025.3648674
