---
id: W4392240059
key: 2024_Luo_H3DTransformer_TODAES
title: "H3D-Transformer: A Heterogeneous 3D (H3D) Computing Platform for Transformer Model Acceleration on Edge Devices"
short: "H3DTransformer"
year: 2024
venue: "TODAES"
venue_full: "ACM Transactions on Design Automation of Electronic Systems, 2024"
authors: "Yandong Luo, Shimeng Yu"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["FeFET"]
models: ["BERT/Transformer", "GPT/LLM"]
lm_models: ["BERT", "GPT-2"]
param_scale: "~100M-1.5B"
slm: true
evidence: simulation
topics: ["heterogeneous-analog-digital", "3d-integration", "transformer-accelerator", "edge-ai", "dataflow-pipelining"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 2
citations_overall: 27
priority_score: 11.34
doi: "https://doi.org/10.1145/3649219"
pdf: null
fulltext: null
---

# H3DTransformer

**H3D-Transformer: A Heterogeneous 3D (H3D) Computing Platform for Transformer Model Acceleration on Edge Devices** — ACM Transactions on Design Automation of Electronic Systems, 2024 (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Heterogeneous 3D interposer design pairing mixed-signal CIM cubes and digital TPUs for transformer MatMuls reaches 10 TOPS/W on BERT/GPT-2, 2.6-3.1x above a 7nm TPU + stacked FeFET baseline.

## Summary
Argues GB-class NLP transformers exceed single-chip CIM accelerators. Proposes an interposer with several 3D memory/logic hybrid cubes optimized for different MatMul workloads, and an approximate computing scheme splitting work between mixed-signal CIM and digital TPUs. System-level evaluation on BERT and GPT-2 gives about 10 TOPS/W. Abstract-only.

## Language models evaluated
- Models: BERT, GPT-2
- Scale: ~100M-1.5B
- Note: Evaluates BERT and GPT-2 on a heterogeneous 3D system combining mixed-signal CIM (FeFET-based per abstract) with digital TPUs; some MatMuls are in-memory approximate compute, others digital. Model scale up to GPT-2 (hundreds of millions of params).

## Contributions
- Heterogeneous 3D interposer accelerator for transformers
- Approximate scheme mixing mixed-signal CIM and digital TPU
- System evaluation on BERT and GPT-2

## Results
- ~10 TOPS/W on BERT and GPT-2
- 2.6x-3.1x over 7nm TPU with stacked FeFET memory

## Limitations
- System-level simulation only
- Accuracy impact of approximation not known from abstract

## Remarks
Relevant as an architectural study placing LM weights in stacked NVM with partial analog CIM; results are simulated and baseline-dependent.

## Cites (in collection, 2)
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020)
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022)

## Cited by (in collection, 5)
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _contrasts/critiques_: "Likewise, H3D-Transformer proposes a hybrid architecture consisting of FeFET, SRAM, and TPU cores stacked vertically via TSVs in a 16-tier system [27]."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _baseline/comparison_: "Some studies have developed specific modules to leverage the varying sparsity, precision, and weight writing needs of operators [10, 12]."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _background_: "This necessitates a joint utilization of IMC and NMC architectures [5], [6], [7], [8], [9], [10], and a tightly-coupled IMC/NMC design becomes essential to effectively support the hybrid data-stationarity patterns inherent in LLM workloads."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _background_: "H3d-transformer [38] uses 3D technology to heterogeneous DRAM-PIM and TPU for diferent module characteristics of Transformer."
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2024_Luo_H3DTransformer_TODAES.pdf`)
- Full text: none
- DOI: https://doi.org/10.1145/3649219
