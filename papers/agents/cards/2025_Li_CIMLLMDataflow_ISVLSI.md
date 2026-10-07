---
id: W4413755433
key: 2025_Li_CIMLLMDataflow_ISVLSI
title: "CIM for Transformer Models: Enhancing Large Language Model Inference Efficiency"
short: "CIM-LLM Dataflow"
year: 2025
venue: "ISVLSI"
venue_full: "IEEE Computer Society Annual Symposium on VLSI (ISVLSI 2025)"
authors: "Miao Li, Jung-Fang Ke, En-Ming Huang, Zhiwei Liu, Yuguang Chen, Chun‐Yi Lee"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["Generic-NVM"]
models: ["GPT/LLM", "Transformer"]
lm_models: []
param_scale: "not specified"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "dataflow-pipelining", "attention", "language-models", "macro"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/isvlsi65124.2025.11130222"
pdf: null
fulltext: null
---

# CIM-LLM Dataflow

**CIM for Transformer Models: Enhancing Large Language Model Inference Efficiency** — IEEE Computer Society Annual Symposium on VLSI (ISVLSI 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes a Compute-in-Memory dataflow and memory hierarchy that performs LLM attention-score and feed-forward computation directly in CIM instead of offloading KV cache to the CPU, reporting 0.026x latency and ~1.2e-3x energy relative to a CPU-based implementation.

## Summary
The paper addresses the memory and compute bottleneck of LLM inference when GPU memory cannot hold the full KV cache and no high-bandwidth inter-GPU link (e.g. NVLink) is available: the usual fallback is to offload the KV cache to the CPU for storage/attention computation and ship results back to the GPU, which the authors note is costly both because attention-score computation is demanding on the CPU and because it requires heavy data movement between KV caches and memory. They propose computing attention scores and even the feed-forward layers directly on Compute-in-Memory (CIM) hardware instead, presenting a tailored CIM-based dataflow and memory hierarchy design for this purpose. The authors position this as an early (first, per the abstract) exploration of integrating CIM specifically into the LLM inference pipeline for attention and FFN computation, reporting large latency and energy reductions relative to a CPU-based baseline.

## Language models evaluated
- Models: —
- Scale: not specified
- Note: Only the abstract was available; it names no specific LLMs or scales, offloading KV-cache attention to CIM versus CPU.

## Contributions
- Identifies KV-cache CPU-offloading (needed when GPU memory and inter-GPU links are insufficient) as a major latency/energy bottleneck for LLM inference
- Proposes computing both attention-score and feed-forward-layer computation directly on Compute-in-Memory (CIM) hardware rather than offloading to CPU
- Designs a tailored CIM-based dataflow and memory hierarchy for this attention + FFN computation
- Reports large latency and energy reductions versus a CPU-based implementation

## Key claims (stable IDs)
- **2025_Li_CIMLLMDataflow_ISVLSI#C1** — The proposed CIM-based dataflow substantially reduces LLM inference latency and energy versus a CPU-based implementation — _support:_ 0.026x inference latency and 1.199x10^-3x energy compared to a CPU-based implementation — _loc:_ Abstract

## Results
- 0.026x inference latency (~38x speedup) vs. CPU-based implementation
- 1.199x10^-3x energy consumption (~834x energy reduction) vs. CPU-based implementation

## Limitations
- Baseline comparison is only against a CPU-based implementation, not a GPU baseline, which likely inflates the reported speedup/energy-reduction multipliers relative to what a GPU-vs-CIM comparison would show
- Abstract does not specify the memory device technology used for the CIM arrays
- Evidence basis (simulation vs. prototype) and model/benchmark scale are not stated in the abstract

## Remarks
The framing (CPU-offloaded KV cache as the bottleneck being replaced by CIM) is a reasonable motivation, but the headline 38x/834x figures should be read cautiously since they are measured against a CPU baseline rather than the GPU-based baselines most LLM-serving systems actually use; a fairer comparison for assessing real-world impact would also include GPU-only and GPU+NVLink multi-GPU baselines. Still, the idea of using CIM for both attention-score and FFN computation (rather than attention alone, as in several ReRAM-attention accelerators) is a relevant mapping contribution for full-pipeline LLM-on-CIM designs.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020)
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2025_Li_CIMLLMDataflow_ISVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/isvlsi65124.2025.11130222
