---
id: W7126184620
key: 2025_Xu_FeRAMKVCache3D_IEDM
title: "First Experimental Demonstration of Disturb-Free 3D Vertical 1T-nC-1T Ferroelectric-based KV Cache with Co-Optimization of Hybrid Analog-Digital CIM and Token-Wise Dynamic Pruning for Efficient Long-Context LLM Inference"
short: "FeRAM KV-cache"
year: 2025
venue: "IEDM"
venue_full: "IEEE International Electron Devices Meeting (IEDM), 2025"
authors: "Weikai Xu, Danyun Luo, Minyue Deng, Shuzhang Zhong, Shengjie Cao, Meng Li, Qianqian Huang, Ru Huang"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["FeRAM"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["OPT-125M (attention-sparsity measurement; system-level perplexity/long-context analysis)"]
param_scale: "125M (OPT-125M measured); long-context LLMs in system analysis"
slm: true
evidence: measured-silicon
topics: ["kv-cache", "attention", "3d-integration", "heterogeneous-analog-digital", "pruning-sparsity", "macro", "language-models", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 0
citations_overall: 2
priority_score: 8.93
doi: "https://doi.org/10.1109/iedm50572.2025.11353834"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Xu_FeRAMKVCache3D_IEDM.pdf"
fulltext: "../fulltext/2025_Xu_FeRAMKVCache3D_IEDM.txt"
---

# FeRAM KV-cache

**First Experimental Demonstration of Disturb-Free 3D Vertical 1T-nC-1T Ferroelectric-based KV Cache with Co-Optimization of Hybrid Analog-Digital CIM and Token-Wise Dynamic Pruning for Efficient Long-Context LLM Inference** — IEEE International Electron Devices Meeting (IEDM), 2025 (2025)

## TL;DR
First experimental ferroelectric KV cache: a fabricated 3D 3x32x32 HZO FeCap array (~10 ns switching, 10-year retention, 1e16 extrapolated endurance) used as analog 1T-nC CIM for top-k token selection plus digital nC-1T CIM for exact attention, claiming 6x performance and 315x energy efficiency over prior designs.

## Summary
Long-context LLM inference is bottlenecked by KV-cache storage and attention data movement from HBM, and static-weight NVMs (Flash, FeFET, RRAM) cannot sustain KV-cache write rates. The paper proposes a 3D vertical 1T-nC-1T FeRAM structure with orthogonal word/bit lines and shared FeCap strings that works in two modes: small-signal non-destructive read (NDR) as analog CIM (0.1 V read pulse, charge integrated on BL1 gives query-key similarity in O(1) time for top-k token selection) and destructive read (DR) as digital CIM (about 40x larger memory window) for exact attention scores on the selected tokens, with a multi-bit sense amplifier, adder tree and write-back. A differential encoding avoids overlap from the small HCS/LCS ratio, and replicating KV entries along the nC string with different input pulses provides input expansion, parallelism and disturb-free operation. A token-wise dynamic top-k algorithm adjusts k per layer/head using accumulated post-softmax attention. Cylindrical Hf0.5Zr0.5O2 (10 nm ALD) 3-layer FeCap arrays (3x32x32, 4F2/n density, 2Pr ~40 uC/cm2) are fabricated and measured. Similarity evaluation is demonstrated on OPT-125M attention, and a system-level analysis uses measured device-to-device variation for perplexity and long-context accuracy. Only KV cache and attention run in-memory; weight matmuls stay elsewhere.

## Language models evaluated
- Models: OPT-125M (attention-sparsity measurement; system-level perplexity/long-context analysis)
- Scale: 125M (OPT-125M measured); long-context LLMs in system analysis
- Note: 3D vertical 1T-nC-1T FeRAM KV cache with hybrid analog (similarity, O(1)) and digital CIM attention for long-context LLMs; 3x32x32 FeCap array fabricated. LM scale not stated in abstract.

## Contributions
- First ferroelectric (FeRAM) KV cache with hardware demonstration
- 3D vertical 1T-nC-1T structure supporting both analog NDR CIM and digital DR CIM
- Disturb-free data mapping via KV replication across nC strings with parallel computation
- Token-wise dynamic top-k pruning co-designed with hybrid analog-digital CIM

## Key claims (stable IDs)
- **2025_Xu_FeRAMKVCache3D_IEDM#C1** — Only a few tokens carry >90% of the attention score — _support:_ top-3/top-7 tokens reach 90% accumulated attention in OPT-125M layer 5 heads 0 and 1 — _loc:_ Fig. 12a-b
- **2025_Xu_FeRAMKVCache3D_IEDM#C2** — Hybrid CIM with dynamic pruning matches full attention accuracy and gains 25-100x overall performance — _support:_ system-level analysis with measured variation — _loc:_ Fig. 13g-h
- **2025_Xu_FeRAMKVCache3D_IEDM#C3** — 6x performance and 315x energy efficiency over SOTA designs — _support:_ 24 TOPS vs 4 TOPS (1x) effective baseline; 655.3 TOPS/W vs reference 1x set — _loc:_ Abstract, Table II
- **2025_Xu_FeRAMKVCache3D_IEDM#C4** — DR mode memory window ~40x larger than NDR — _support:_ Fig. 9c vs 9d — _loc:_ Sec. III-B

## Results
- FeCap: ~10 ns switching, >1e11 measured cycles extrapolated to 1e16 with re-wakeup, 10-year extrapolated retention, 2Pr ~40 uC/cm2
- Integrated charge linear in number of HCS cells and activated inputs (1x1x4 and 1x2x4 arrays)
- Table II: this work 24 TOPS (6x) and 655.3 TOPS/W (315x) vs GPU baseline numbers
- ACIM-only with NDR suffers poor sensing margin under variation and higher perplexity; DCIM-only costs excess power/latency

## Key numbers
- array_size: 3x32x32 FeCap (3D)
- energy_eff: 655.3 TOPS/W (315x vs baseline)
- throughput: 24 TOPS (6x)
- accuracy: comparable to full attention with proper k

## Datasets / benchmarks
OPT-125M attention maps, long-context tasks (system-level)

## Limitations
- Only a 3x32x32 test array measured; full LLM KV cache results are system-level extrapolations with measured variation statistics
- Model evidence limited to OPT-125M attention maps; long-context accuracy from simulation
- Short conference paper; no bibliography available and many figure details garbled in extraction
- Weights and FFN not handled; only KV storage/attention
- Destructive read requires write-back, adding energy/latency

## Remarks
One of the few demonstrations that targets the dynamic, write-heavy KV cache rather than static weights, directly addressing why NVM crossbars struggle with attention. The 315x energy claim is against specific baselines and combines device, architecture and pruning, so it is hard to attribute. For small LMs on analog hardware it is a complementary design point: keep weights static in analog crossbars and put KV cache in endurance-rich FeRAM.

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Xu_FeRAMKVCache3D_IEDM.pdf](../../11_Small_Language_Models_on_AIMC/2025_Xu_FeRAMKVCache3D_IEDM.pdf)
- Full text: [../fulltext/2025_Xu_FeRAMKVCache3D_IEDM.txt](../fulltext/2025_Xu_FeRAMKVCache3D_IEDM.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iedm50572.2025.11353834
