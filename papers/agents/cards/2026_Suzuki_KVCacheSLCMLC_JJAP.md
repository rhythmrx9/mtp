---
id: W7118450172
key: 2026_Suzuki_KVCacheSLCMLC_JJAP
title: "Mapping strategy of quantized KV cache of LLMs into mixture of SLC and MLC ReRAM among various quantization methods"
short: "KVCacheSLCMLC"
year: 2026
venue: "JJAP"
venue_full: "Japanese Journal of Applied Physics, 2026"
authors: "Shota Suzuki, Naoko Misawa, Chihiro Matsui, Ken Takeuchi"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["GPT/LLM"]
lm_models: ["unspecified LLMs"]
param_scale: "unspecified"
slm: true
evidence: simulation
topics: ["kv-cache", "mixed-precision", "weight-mapping", "language-models", "quantization"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 1
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.35848/1347-4065/ae33cb"
pdf: null
fulltext: null
---

# KVCacheSLCMLC

**Mapping strategy of quantized KV cache of LLMs into mixture of SLC and MLC ReRAM among various quantization methods** — Japanese Journal of Applied Physics, 2026 (2026)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Splitting quantized KV values into upper bits in SLC and lower bits in MLC ReRAM gives 49.1% fewer cells with perplexity kept low across LLMs and quantizers.

## Summary
MLC ReRAM is denser than SLC but random telegraph noise causes false state detection. The authors analyze error robustness of the three components of a quantized KV cache and propose storing upper bits in SLC and lower bits in MLC. They report 49.1% fewer memory cells than the conventional method while keeping perplexity low regardless of LLM and quantization method. Abstract-only; details not checked.

## Language models evaluated
- Models: unspecified LLMs
- Scale: unspecified
- Note: Stores quantized LLM KV cache in a mix of SLC and MLC ReRAM (upper bits SLC, lower bits MLC) to save area under RTN-induced errors; ReRAM is dense storage, not analog compute. Specific LLMs not verified (abstract-only).

## Contributions
- Error-robustness analysis of KV-cache components
- Hybrid SLC/MLC bit-split mapping
- 49.1% cell reduction at maintained perplexity

## Key claims (stable IDs)
- **2026_Suzuki_KVCacheSLCMLC_JJAP#C1** — 49.1% fewer memory cells while maintaining perplexity — _support:_ stated in abstract — _loc:_ Abstract

## Results
- 49.1% fewer cells vs conventional mapping

## Limitations
- Abstract-only; models and noise levels unknown
- NVM used as storage, no in-memory compute
- Write endurance/latency for per-token KV writes not discussed in abstract

## Remarks
Relevant to KV caches on NVM and to reliability-aware bit mapping. Uncertain evidence strength without the paper; the bit-significance split is a sensible, reusable idea.

## Cites (in collection, 1)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2026_Suzuki_KVCacheSLCMLC_JJAP.pdf`)
- Full text: none
- DOI: https://doi.org/10.35848/1347-4065/ae33cb
