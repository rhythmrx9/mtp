---
id: W4400230160
key: 2024_Cai_MemristorLSHAttention_ISCAS
title: "In-Memory Transformer Self-Attention Mechanism Using Passive Memristor Crossbar"
short: "Memristor LSH Attention"
year: 2024
venue: "ISCAS"
venue_full: "IEEE International Symposium on Circuits and Systems (ISCAS 2024)"
authors: "Jack Cai, Muhammad Ahsan Kaleem, Roman Genov, Mostafa Rahimi Azghadi, Amirali Amirsoleimani"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["Memristor(generic)"]
models: ["Transformer", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["attention", "analog-mvm", "transformer-accelerator", "energy-efficiency", "nonlinear-functions"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 1
citations_overall: 2
priority_score: 6.24
doi: "https://doi.org/10.1109/iscas58744.2024.10558182"
pdf: null
fulltext: null
---

# Memristor LSH Attention

**In-Memory Transformer Self-Attention Mechanism Using Passive Memristor Crossbar** — IEEE International Symposium on Circuits and Systems (ISCAS 2024) (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes performing locality-sensitive-hashing (LSH) self-attention using stochastic vector-matrix multiplication on low-resolution, semi-passive 0T1R memristor crossbars, showing via circuit-level simulation that it can approximate LLM self-attention with no evaluation-metric degradation.

## Summary
Transformer self-attention has quadratic time/memory complexity in sequence length, which is especially costly for both conventional and in-memory computing hardware. Prior algorithmic work (LSH attention) reduces this to O(L log L), and this paper proposes implementing LSH attention's underlying computation on semi-passive memristor crossbar arrays using low-resolution, energy-efficient 0T1R stochastic vector-matrix multiplication (VMM), rather than purely in conventional digital or full in-memory arithmetic. Using circuit-level simulation, the authors claim the hardware-level LSH approximation can be substituted as a drop-in replacement for exact attention in large language models (LLMs) without degrading evaluation metrics. The work positions itself as an early building block toward eventually computing the entire transformer architecture in-memory.

## Contributions
- Proposes mapping the hashing step of LSH self-attention onto low-resolution, semi-passive 0T1R memristor crossbar arrays
- Uses stochastic VMM on memristor arrays to perform the approximate nearest-neighbor hashing needed for LSH attention
- Demonstrates via circuit-level simulation that the hardware-approximated LSH attention is a feasible drop-in replacement in LLMs with no reported degradation in evaluation metrics
- Frames the approach as a stepping stone toward fully in-memory transformer computation

## Key claims (stable IDs)
- **2024_Cai_MemristorLSHAttention_ISCAS#C1** — Low-resolution, energy-efficient 0T1R memristor arrays can perform the stochastic VMM needed for LSH attention — _support:_ circuit-level simulation results (abstract); full quantitative details not available without full text — _loc:_ abstract
- **2024_Cai_MemristorLSHAttention_ISCAS#C2** — The proposed in-memory LSH approximation can replace exact self-attention in LLMs without degrading evaluation metrics — _support:_ stated in abstract as a simulation-based finding; specific benchmark numbers not available without full text — _loc:_ abstract

## Results
- No full-text access; abstract reports qualitative claims of feasibility and 'no degradation in evaluation metrics' for LLMs under the proposed memristor-based LSH attention scheme, without specific quantitative figures

## Limitations
- Full text unavailable; this analysis is based on the abstract only, so quantitative results, exact benchmark models, and simulation parameters (array size, bit precision, noise models) could not be verified
- Evidence is circuit-level simulation only, not device/silicon measurement
- Addresses only the attention/hashing sub-block of transformers, not the full transformer pipeline (as the paper itself notes as future work)

## Remarks
A short (ISCAS) paper exploring a specific, narrow idea: using low-precision stochastic memristor VMM to accelerate the approximate hashing step of LSH attention. Without full text, the strength of evidence and generality of the 'no degradation' claim cannot be independently assessed; this should be treated as a preliminary feasibility study rather than a complete system demonstration. It is one of relatively few works targeting the attention mechanism specifically for passive/semi-passive memristor crossbars rather than only dense matrix multiplication.

## Cites (in collection, 1)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 1)
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _baseline/comparison_: "Prior research on heterogeneous-CIM-based Transformer accelerators aims to reduce computation amounts of DMM through algorithm co-design [8, 14, 15]."

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2024_Cai_MemristorLSHAttention_ISCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iscas58744.2024.10558182
