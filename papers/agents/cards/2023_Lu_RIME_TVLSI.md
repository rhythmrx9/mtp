---
id: W4390285480
key: 2023_Lu_RIME_TVLSI
title: "An RRAM-Based Computing-in-Memory Architecture and Its Application in Accelerating Transformer Inference"
short: "RIME"
year: 2023
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2023"
authors: "Zhaojun Lu, Xueyan Wang, Md Tanvir Arafin, Haoxiang Yang, Zhenglin Liu, Jiliang Zhang, Gang Qu"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "dataflow-pipelining", "nonlinear-functions", "crossbar-architecture", "analog-mvm"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 0
citations_overall: 34
priority_score: 7.01
doi: "https://doi.org/10.1109/tvlsi.2023.3345651"
pdf: null
fulltext: null
---

# RIME

**An RRAM-Based Computing-in-Memory Architecture and Its Application in Accelerating Transformer Inference** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2023 (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
RIME is an RRAM in-memory floating-point architecture (single-cycle NOR/NAND/minority logic) with pipelined MatMul and softmax, giving a transformer accelerator 2.3x faster and 1.7x more energy-efficient than a GPU without accuracy loss.

## Summary
Existing CIM designs lack floating-point support needed by NLP transformers and need costly peripherals. The paper proposes RIME, using RRAM cells as logic gates (NOR, NAND, minority) to perform floating-point operations in memory with a centralized control module and simplified peripherals. Pipelined MatMul and softmax implementations are built on RIME to form a transformer accelerator. Reported results are 2.3x timing and 1.7x energy-efficiency gains over a GPU implementation with no inference accuracy loss. (Abstract only; details not verified.)

## Language models evaluated
- Models: —
- Scale: —
- Note: Transformer (NLP) inference on RRAM using in-memory NOR/NAND/minority logic floating-point; digital stateful logic, not analog crossbar MVM. Specific LMs and scale not stated in abstract.

## Contributions
- RIME: scalable RRAM in-memory floating-point architecture
- Single-cycle NOR/NAND/minority-based FP operations
- Pipelined in-memory MatMul and softmax
- Transformer accelerator built on RIME

## Key claims (stable IDs)
- **2023_Lu_RIME_TVLSI#C1** — 2.3x time and 1.7x energy efficiency vs GPU, no accuracy loss — _support:_ abstract — _loc:_ Abstract

## Results
- 2.3x timing efficiency and 1.7x energy efficiency vs GPU

## Limitations
- Abstract only; models, datasets and baselines unknown
- Digital stateful logic is slow per-op and endurance-heavy; device non-idealities not discussed in abstract

## Remarks
Relevant to in-memory transformer inference but computes digitally in ReRAM, so it sidesteps analog noise and is not an analog SLM deployment. Gains over a GPU are modest. Treat as generic transformer accelerator (04).

## Cited by (in collection, 2)
- [2025_Xu_UniCAIM_DAC](2025_Xu_UniCAIM_DAC.md) UniCAIM (2025) — _background_: "Meanwhile, from the hardware perspective, the computing-in-memory (CIM) architecture which can perform the general matrix-vector multiplication (GEMV) operations within the memory array, has been proven to compute attention efficiently by reducing the data movement [9-12]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _contrasts/critiques_: "Meanwhile, RIME [20] and ReTransformer [23] are PIM-based architectures designed to accelerate conventional encoder-decoder transformers [28]."

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2023_Lu_RIME_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2023.3345651
