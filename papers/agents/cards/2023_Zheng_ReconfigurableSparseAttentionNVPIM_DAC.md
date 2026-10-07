---
id: W4386764227
key: 2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC
title: "Accelerating Sparse Attention with a Reconfigurable Non-volatile Processing-In-Memory Architecture"
short: "Reconfigurable Sparse-Attention NVPIM"
year: 2023
venue: "DAC"
venue_full: "60th ACM/IEEE Design Automation Conference (DAC 2023)"
authors: "Qilin Zheng, Shiyu Li, Yitu Wang, Ziru Li, Yiran Chen, Hai Helen Li"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["ViT", "Transformer", "BERT"]
lm_models: ["BERT"]
param_scale: "110M"
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "pruning-sparsity", "dataflow-pipelining", "weight-mapping", "peripheral-circuits", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 3
citations_overall: 14
priority_score: 6.75
doi: "https://doi.org/10.1109/dac56929.2023.10247908"
pdf: "../../04_Transformers_and_LLMs/2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.pdf"
fulltext: "../fulltext/2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.txt"
---

# Reconfigurable Sparse-Attention NVPIM

**Accelerating Sparse Attention with a Reconfigurable Non-volatile Processing-In-Memory Architecture** — 60th ACM/IEEE Design Automation Conference (DAC 2023) (2023)

## TL;DR
A reconfigurable ReRAM PIM bank adds inner-product and scalar-vector-multiply primitives (reusing readout circuitry) so dynamic unstructured sparse attention (SDDMM/SpMM) maps efficiently, giving 2.95-12.36x speedup and 1.2-3.4x energy gain over a ReTransformer-style NVPIM baseline.

## Summary
Dynamic, unstructured sparse attention (>85-90% sparsity) maps poorly to analog crossbar banks whose native primitive is a fixed MxN vector-matrix multiplication: the bank is fully used only when N contiguous mask entries are valid, so applying sparsity to ReTransformer yields only 1.59x speedup at 95% sparsity (1.0x at 67%; Fig. 1). The paper adds two vector primitives to the NVPIM bank by reusing the column multiplexers, multi-bit sense amplifiers (MBSA) and local PE: an inner-product (IP) mode computes one non-zero attention score per cycle between a q and a k vector (SDDMM), and a scalar-vector multiplication (SVM) mode multiplies one non-zero attention weight with a v vector (SpMM); the conventional analog VMM mode is retained for dense layers. A hybrid stationary dataflow splits the attention map into chunks and pipelines attention-map and output computation, buffering only two chunks. Precision gating (Sanger) produces the mask; linear/FFN layers are 8-bit quantized, vision models retrained 60 epochs and BERT fine-tuned per task. Evaluation uses a cycle-accurate simulator with array models from ISAAC, 28nm synthesized adders, transistor-level MBSA, CACTI buffers; a bank gives 9.14 GOPS with 128 kB, 72 banks/tile give 658 GOPS and 9 MB. Workloads are DeiT/PVT/PiT on ImageNet and BERT on GLUE, SQuAD v1.1 and CLOTH.

## Language models evaluated
- Models: BERT
- Scale: 110M

## Contributions
- Identified low bank utilization of VMM-based NVPIM for dynamic unstructured sparse attention
- Reconfigurable NVPIM bank with IP and SVM digital primitives reusing interface circuits
- Hybrid stationary, chunk-pipelined dataflow hiding SDDMM/SpMM latency and reducing attention-map storage
- Cycle-accurate evaluation vs ReTransformer(+SRE) and non-PIM Sanger/DOTA

## Key claims (stable IDs)
- **2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC#C1** — Reconfigurable bank improves performance over conventional NVPIM on sparse attention — _support:_ 2.95x-12.36x speedup, 1.2x-3.4x energy efficiency vs ReTransformer baseline — _loc:_ Sec. VI-A, Fig. 9
- **2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC#C2** — Better energy than non-PIM sparse-attention accelerators at similar latency — _support:_ up to 3.8x (Sanger) and 8.6x (DOTA) energy reduction; ReTransformer gets 3.71x/8.5x energy reduction but 4.8x/3.3x latency overhead — _loc:_ Sec. VI-C, Fig. 10
- **2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC#C3** — Sparse attention costs little accuracy — _support:_ <1% accuracy loss with >85% attention sparsity for most models — _loc:_ Sec. VI-A
- **2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC#C4** — Scales better with banks — _support:_ latency reduces ~50% from 8 to 24 banks vs 30% for baseline — _loc:_ Sec. VI-B, Fig. 10(b)

## Results
- Naive sparse mapping on ReTransformer: 1.59x speedup at 95% sparsity, 1.0x at 67%; with SRE 1.84x/1.11x (Fig. 1)
- Bank throughput 9.14 GOPS per 128 kB; tile of 72 banks: 658 GOPS, 9 MB
- Computation energy lower due to higher array utilization, but memory access energy higher due to less reuse (Fig. 11)
- Larger sparsity gives larger gains

## Key numbers
- tech_node: 28nm (adders)
- array_size: 512x512 (baseline design from [10]; 8 wordlines/64 bitlines per cycle)
- energy_eff: 1.2x-3.4x vs ReTransformer; up to 8.6x vs DOTA
- throughput: 9.14 GOPS per bank; 658 GOPS per 72-bank tile
- accuracy: <1% loss at >85% attention sparsity
- bits_weight: 8b

## Datasets / benchmarks
ImageNet, GLUE, SQuAD v1.1, CLOTH

## Limitations
- Architecture simulation only, no device noise or ADC/IR-drop accuracy modelling in analog mode
- Q/K/V must be written into ReRAM at runtime, with endurance and write cost not analyzed (contrast X-Former)
- IP/SVM modes are digital operations on ReRAM-stored data, reducing analog benefit
- Mostly vision transformers; BERT-base only for language
- Non-PIM baselines iso-throughput, optimistic assumption stated by authors

## Remarks
Shows that VMM-granularity analog banks mismatch dynamic fine-grained sparsity and that readout periphery can be repurposed as a digital vector unit. Evidence is architectural simulation; accuracy claims only concern the sparsity algorithm, not analog noise. It assumes cheap runtime writes of Q/K/V into ReRAM, which X-Former and similar designs avoid by using SRAM. Limited relevance to SLM decode, but sparse-attention handling on NVM is a useful design reference.

## Cites (in collection, 3)
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _baseline/comparison_: "For the baseline NVPIM accelerators, we quantitatively compare our design with ReTransformer [3], as implemented with our cycle-accurate simulator. ReTransformer is designed for dense attention computation, so we apply the method proposed in SRE [6] to support the sparse attention."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "For the NVPIM bank, we use the memory array model from [9]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "We select ReRAM as our target device because of its high density and energy efficiency, as shown in previous designs for other neural networks [8, 9]."

## Cited by (in collection, 2)
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _background_: "In-memory Computing (IMC) stands out as a promising solution to alleviate the computational and memory challenges posed by Transformer models [6–8]."
- [2025_Xu_UniCAIM_DAC](2025_Xu_UniCAIM_DAC.md) UniCAIM (2025) — _contrasts/critiques_: "Besides, there are emerging non-volatile memories (NVMs)-based CIM designs for dynamic pruning by utilizing approximate attention scores [17, 18], but suffering the trade-off between energy efficiency and accuracy."

## Files
- PDF: [../../04_Transformers_and_LLMs/2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.pdf](../../04_Transformers_and_LLMs/2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.pdf)
- Full text: [../fulltext/2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.txt](../fulltext/2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/dac56929.2023.10247908
