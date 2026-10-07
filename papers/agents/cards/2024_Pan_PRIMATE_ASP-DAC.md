---
id: W4393168980
key: 2024_Pan_PRIMATE_ASP-DAC
title: "PRIMATE: Processing in Memory Acceleration for Dynamic Token-pruning Transformers"
short: "PRIMATE"
year: 2024
venue: "ASP-DAC"
venue_full: "29th Asia and South Pacific Design Automation Conference (ASP-DAC 2024)"
authors: "Yue Pan, Minxuan Zhou, Chonghan Lee, Zheyu Li, Rishika Kushwah, Vijaykrishnan Narayanan, Tajana Rosing"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["DRAM"]
models: ["Transformer", "BERT", "ViT"]
lm_models: ["BERT (SST-2)", "RoBERTa (Hyperpartisan)"]
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "pruning-sparsity", "dataflow-pipelining", "scheduling", "tiling-partitioning", "energy-efficiency", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 3
citations_overall: 3
priority_score: 5.42
doi: "https://doi.org/10.1109/asp-dac58780.2024.10473968"
pdf: "../../04_Transformers_and_LLMs/2024_Pan_PRIMATE_ASP-DAC.pdf"
fulltext: "../fulltext/2024_Pan_PRIMATE_ASP-DAC.txt"
---

# PRIMATE

**PRIMATE: Processing in Memory Acceleration for Dynamic Token-pruning Transformers** — 29th Asia and South Pacific Design Automation Conference (ASP-DAC 2024) (2024)

## TL;DR
PRIMATE is an HBM2E bit-serial PIM framework for dynamic token-pruning Transformers that adds near-channel Top-k Engines and a pipelined memory-partitioning optimizer (PrimateOpt), reaching up to 30.6x throughput, 29.5x space efficiency and 4.3x energy efficiency over TransPIM in simulation.

## Summary
Dynamic token pruning progressively drops unimportant tokens (importance from attention scores) but existing PIM Transformer accelerators such as TransPIM lack in-memory top-k selection (sorting is offloaded to the host CPU) and suffer memory underutilization as pruning shrinks the token count. PRIMATE builds on HBM2E with bit-serial processing-using-memory (SIMDRAM-style AAP operations, about 7n^2 AAPs per n-bit multiply) plus near-bank logic; it adds 16 channel-level Top-k Engines (accumulator, segmented top-k buffer with 4 KB reserved memory, bitonic sorter/merger) costing 2.53 mm^2 (2.3% of one HBM2E stack) and 1.3 W. Software side: a token-based dataflow with weights preallocated per bank, a pipelined layer-wise memory partitioning (PrimateOpt: layer-wise exploration, global adjustments, layer merging) that gives each layer a memory block sized to its pruned token count. Models are quantized to 8-bit and evaluated with an in-house Ramulator-like simulator using latency/energy from prior work and Verilog synthesis (32 nm scaled to 10 nm) on 8 stacks of 16 GB. Workloads: two ViTs (Stanford Dogs, CUB-200-2011), BERT on SST-2 and RoBERTa on Hyperpartisan News, with 39% (W1) or 20%-per-layer pruning and accuracies 91.1/89.6/92.7/87.1%. Results: up to 30.6x (avg 21x) throughput, 29.5x (avg 18.9x) space efficiency, 4.3x (avg 3.8x) energy efficiency versus TransPIM; sorting overhead cut from 2.8-25.2% to 0.14% (up to 90x standalone).

## Language models evaluated
- Models: BERT (SST-2), RoBERTa (Hyperpartisan)
- Scale: —

## Contributions
- In-memory Top-k Engine (near-channel accumulation and token selection) for HBM-based PIM.
- PrimateOpt pipelined per-layer memory-partitioning optimization to address utilization loss from pruning.
- Software-hardware co-design on HBM2E with minor modifications.
- Evaluation on ViT, BERT and RoBERTa workloads showing up to 30.6x/29.5x/4.3x gains.

## Key claims (stable IDs)
- **2024_Pan_PRIMATE_ASP-DAC#C1** — Up to 30.6x throughput, 29.5x space efficiency and 4.3x energy efficiency over TransPIM. — _support:_ avg 21x, 18.9x, 3.8x on W1-W4 — _loc:_ Sec. VI-B, Fig. 8-9
- **2024_Pan_PRIMATE_ASP-DAC#C2** — In-memory top-k reduces sorting overhead from 9.2/25.2/2.8/5.4% to average 0.14%. — _support:_ up to 90x better standalone sorting cost — _loc:_ Sec. VI-C
- **2024_Pan_PRIMATE_ASP-DAC#C3** — Top-k hardware overhead is 2.53 mm^2 (2.3% of an HBM2E stack) and 1.3 W. — _support:_ synthesis — _loc:_ Sec. VI-E

## Results
- Throughput up to 30.6x (avg 21x), space efficiency up to 29.5x (avg 18.9x), energy efficiency up to 4.3x (avg 3.8x) vs TransPIM.
- Accuracy of pruned models 91.1%, 89.6%, 92.7%, 87.1% (W1-W4), comparable to unpruned.
- Also claimed superior to ASIC accelerators A3 and SpAtten and GPU solutions (by way of beating TransPIM).

## Key numbers
- tech_node: HBM2E 10nm (logic synthesized 32nm scaled)
- energy_eff: up to 4.3x vs TransPIM
- throughput: up to 30.6x vs TransPIM
- accuracy: 91.1/89.6/92.7/87.1% on W1-W4
- bits_weight: 8b

## Datasets / benchmarks
SST-2, Stanford Dogs, CUB-200-2011, Hyperpartisan News

## Limitations
- Digital DRAM/HBM PIM, not analog or NVM in-memory computing; relevance to AIMC is as a contrast.
- Simulation with scaled component models; no silicon.
- Only encoder models (ViT, BERT, RoBERTa) and classification; no autoregressive LLM decoding or KV cache.
- Baseline is a single prior PIM design (TransPIM) re-modeled by the authors.

## Remarks
Gives a digital-PIM point of comparison for transformer accelerators: it argues DRAM PIM offers capacity, bandwidth and numerical stability that ReRAM designs lack. Token pruning and in-memory top-k are algorithmic ideas that could apply to analog designs where attention remains digital. Evidence is simulation-based and limited to small encoder classification workloads.

## Cites (in collection, 3)
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _contrasts/critiques_: "This work focuses on DRAM-based (HBM) PIM technologies which can support larger capacity than SRAM [23] with high bandwidth, lower latency, and higher numerical stability than nonvolatile memory designs [6], [24]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _baseline/comparison_: "Compared to baseline [27], the PRIMATE architecture achieves up to 30.6x, average 21x better throughput; up to 29.5x, average 18.9x better space efficiency, and up to 4.3x, average 3.8x better energy efficiency on W1 to W4."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Previous works [19, 27] have shown a software-hardware co-designed PIM architecture can provide better throughput and power consumption than GPU and TPU for Transformers."

## Files
- PDF: [../../04_Transformers_and_LLMs/2024_Pan_PRIMATE_ASP-DAC.pdf](../../04_Transformers_and_LLMs/2024_Pan_PRIMATE_ASP-DAC.pdf)
- Full text: [../fulltext/2024_Pan_PRIMATE_ASP-DAC.txt](../fulltext/2024_Pan_PRIMATE_ASP-DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/asp-dac58780.2024.10473968
