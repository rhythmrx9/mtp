---
id: W7133301734
key: 2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC
title: "31.1 A 14.08-to-135.69Token/s ReRAM-on-Logic Stacked Outlier-Free Large-Language-Model Accelerator with Block-Clustered Weight-Compression and Adaptive Parallel-Speculative-Decoding"
short: "ReRAM-on-Logic SD LLM Chip"
year: 2026
venue: "ISSCC"
venue_full: "IEEE International Solid-State Circuits Conference (ISSCC), 2026"
authors: "Pingcheng Dong, Yonghao Tan, Xuejiao Liu, Peng Luo, Yu Liu, Di Pang, Songchen Ma, Xijie Huang, Shih-Yang Liu, D. Zhang, Zhichao Lu, Luhong Liang et al."
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "SRAM-digital"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["LLaMA2-7B", "LLaMA3-8B"]
param_scale: "7B-8B target models plus small draft models"
slm: true
evidence: measured-silicon
topics: ["chip-demo", "language-models", "3d-integration", "quantization", "heterogeneous-analog-digital", "scheduling", "energy-efficiency", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 0
citations_overall: 1
priority_score: 8.81
doi: "https://doi.org/10.1109/isscc49663.2026.11409211"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC.pdf"
fulltext: "../fulltext/2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC.txt"
---

# ReRAM-on-Logic SD LLM Chip

**31.1 A 14.08-to-135.69Token/s ReRAM-on-Logic Stacked Outlier-Free Large-Language-Model Accelerator with Block-Clustered Weight-Compression and Adaptive Parallel-Speculative-Decoding** — IEEE International Solid-State Circuits Conference (ISSCC), 2026 (2026)

## TL;DR
A 55 nm speculative-decoding LLM accelerator with face-to-face bonded ReRAM-on-logic stacking (8 MB ReRAM, 25.6 GB/s) that reaches 14.08-135.69 token/s, 4.46-7.17x speedup and 3.74-4.85x energy saving over a BF16 speculative-decoding baseline, and 17.82 token/s at 123.41 mJ/token on LLaMA2-7B (MT-Bench).

## Summary
Autoregressive LLM decoding is bound by external memory access (EMA) of weights; speculative decoding (SD) uses a small draft LLM (DLM) and a large target LLM (TLM) but on edge devices still suffers from TLM EMA (>60% of latency), activation outliers that break low-bit PTQ, DLM weights that do not fit on-chip, and >90% draft rejection at long draft length. The chip adds three features: (1) a local rotation unit (LRU) approximating global Hadamard rotation by two overlapped lower-depth (depth 6 instead of 9) fast Walsh-Hadamard transforms for non-power-of-two dimensions (e.g. 14336 = 2^9 x 28 in LLaMA3-8B down_proj), enabling outlier-free W4A8 TLM quantisation with 92.7% less area than global rotation; (2) a ReRAM-stacked process-near-memory (RS-PNM) architecture where blockwise vector quantisation (BVQ, INT4 QAT with Gumbel-softmax learned block indices) stores DLM codebooks in 4 stacked ReRAM dies connected by 2048 bumps (25.6 GB/s, 8 MB), with a tile fusion unit so each codebook entry is fetched once; (3) adaptive parallel speculative decoding (APSD) with a workload-decoupled out-of-order scheduler using 4 instruction queues. The ReRAM thus acts as high-density read-mostly storage with near-memory weight reconstruction rather than analog compute. The logic die runs 63.5-285 MHz at 0.89-1.40 V (2.33 TOPS peak) and each ReRAM die 100 MHz at 1.1 V, 49.54 mW.

## Language models evaluated
- Models: LLaMA2-7B, LLaMA3-8B
- Scale: 7B-8B target models plus small draft models
- Note: Speculative-decoding LLM accelerator, 55nm, with 4 stacked ReRAM dies (8MB) storing codebooks of the small draft LM (DLM); target LLMs include LLaMA2-7B and LLaMA3-8B. Compute is digital (tile-fused tensor engine, INT MACs); ReRAM is NOT used for analog MVM, only as high-bandwidth NVM storage (processing-near-memory). Relevant because the draft LM is an SLM held in NVM.

## Contributions
- Local rotation unit enabling low-area outlier-free W4A8 quantisation of the target LLM
- ReRAM-on-logic face-to-face stacking with RS-PNM and blockwise vector quantisation for draft-model weights
- Adaptive parallel speculative decoding with out-of-order scheduler
- Fabricated 55 nm chip with 4 stacked ReRAM dies and a 4-chip system

## Key claims (stable IDs)
- **2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC#C1** — Chip achieves 14.08-135.69 token/s and 4.46-7.17x speedup / 3.74-4.85x energy saving over BF16 SD baseline — _support:_ across TLM/DLM pairs — _loc:_ Fig. 31.1.6, text
- **2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC#C2** — LRU gives 3.82-3.93x speedup over BF16 SD and saves 92.7% area versus global rotation — _support:_ decomposed FWHT depth 6 vs 9 — _loc:_ Fig. 31.1.3
- **2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC#C3** — RS-PNM with INT4 BVQ yields 1.1-1.46x speedup over W4A8 SD with LRU — _support:_ codebooks in stacked ReRAM; tile fusion halves CB read latency — _loc:_ Fig. 31.1.4
- **2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC#C4** — APSD with out-of-order scheduler gives 1.1-1.29x speedup and 10-14% lower rejected-token ratio — _support:_ 4 parallel instruction queues — _loc:_ Fig. 31.1.5
- **2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC#C5** — LLaMA2-7B on MT-Bench: 17.82 token/s, 123.41 mJ/token in a 4-chip system with LPDDR3 — _support:_ fair system-level comparison enhancing prior works with LPDDR3 — _loc:_ Fig. 31.1.6

## Results
- 55 nm; ReRAM-on-logic via 2048 face-to-face bumps; 4 ReRAM dies, 8 MB, 25.6 GB/s at 100 MHz; 4-chip system 32 MB and 102.4 GB/s
- Logic die 63.5-285 MHz at 0.89-1.40 V, 2.33 TOPS peak; ReRAM die 49.54 mW at 1.1 V
- 3.43 MB SRAM on chip (1 MB weight buffer, 2 MB token buffer, 64 KB ISA buffer)
- W4A8 quantisation gives perplexity comparable to a SOTA W8A16 LLM accelerator and better than 4b/sub-4b weight works
- Deep FWHT array would occupy 4.37x the area of a 4K INT8 MAC array; over 90% of draft tokens rejected at long draft length

## Key numbers
- tech_node: 55nm
- array_size: 4 stacked ReRAM dies, 8 MB, 2048 bumps
- energy_eff: 3.74-4.85x vs BF16 SD baseline; 123.41 mJ/token (LLaMA2-7B, 4-chip)
- throughput: 14.08-135.69 token/s; 17.82 token/s LLaMA2-7B MT-Bench
- accuracy: perplexity comparable to SOTA W8A16 accelerator (W4A8)
- bits_weight: INT4 (BVQ draft) / W4A8 (target)

## Datasets / benchmarks
MT-Bench

## Limitations
- ISSCC summary paper: limited detail, many results only in figures
- ReRAM is used for digital codebook storage, not analog MVM, so analog noise/drift issues are not tested
- Only draft-model weights are stored in ReRAM; target model weights still use external memory (EMA)
- Small on-chip ReRAM capacity (8 MB per chip, 32 MB for 4 chips)
- Quantisation quality reported only relative to other accelerators; exact perplexity values not given in text

## Remarks
A rare measured-silicon LLM chip using a stacked ReRAM die, showing a practical role for NVM in LLM inference: dense, fast read-only storage for compressed draft-model weights instead of analog compute. It is evidence that near-memory use of NVM is already viable for edge LLMs, while analog crossbar MVM for LLMs remains simulation-driven. The rotation-based outlier removal and speculative decoding ideas could carry over to analog LM mapping.

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC.pdf](../../11_Small_Language_Models_on_AIMC/2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC.pdf)
- Full text: [../fulltext/2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC.txt](../fulltext/2026_Dong_ReramOnLogicSpecDecodeLlm_ISSCC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isscc49663.2026.11409211
