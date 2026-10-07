---
id: W3116577775
key: 2020_Guo_ATT_ICCD
title: "ATT: A Fault-Tolerant ReRAM Accelerator for Attention-based Neural Networks"
short: "ATT"
year: 2020
venue: "ICCD"
venue_full: "2020 IEEE 38th International Conference on Computer Design (ICCD 2020)"
authors: "Haoqiang Guo, Lu Peng, Jian Zhang, Qing Chen, Travis LeCompte"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer", "BERT"]
lm_models: ["BERT-Base", "XLNet", "XLM", "Transformer (base, 512-d)"]
param_scale: "~65M-110M+ (pre-trained attention NNs)"
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "stuck-at-faults", "dataflow-pipelining", "nonlinear-functions", "crossbar-architecture", "pruning-sparsity", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 3
citations_overall: 12
priority_score: 6.58
doi: "https://doi.org/10.1109/iccd50377.2020.00047"
pdf: "../../04_Transformers_and_LLMs/2020_Guo_ATT_ICCD.pdf"
fulltext: "../fulltext/2020_Guo_ATT_ICCD.txt"
---

# ATT

**ATT: A Fault-Tolerant ReRAM Accelerator for Attention-based Neural Networks** — 2020 IEEE 38th International Conference on Computer Design (ICCD 2020) (2020)

## TL;DR
ATT is a pipelined ReRAM-crossbar accelerator for attention-based NNs (Transformer, BERT, XLNet, XLM) with NuXG, a sparsity-aware non-uniform redundancy scheme that reaches ~60% of ideal power efficiency and ~2.5x the throughput of the uniform-redundancy RX scheme under 20% stuck-at faults.

## Summary
Existing ReRAM accelerators do not support attention, layer normalization and GELU, and stuck-at faults (SA0 at LRS, SA1 at HRS) corrupt programmed weights. ATT analyzes the Transformer data flow and builds an intra-layer pipeline with a Q-K-V engine, matrix-multiplication engine for Q.K^T and softmax(.).V, softmax, head-merge, layer-norm and GELU engines; weight-stationary products use 128x128 ReRAM crossbars with 1-bit DACs and ADCs (ISAAC-derived), while attention and nonlinear functions run on digital units scaled to 32nm. Fault tolerance: since layer-wise weight sparsity varies (later layers of BERT/XLNet are nearly 100% pruned, max accuracy loss 1.9%), layers are grouped into Low/Medium/High redundancy classes (sparsity thresholds 0.35 and 0.5; required fault-free cell fractions 0.9/0.95/0.99), and NuXG heuristically builds virtual crossbars from physical ones using a score table. Evaluation uses an in-house NVSim-based simulator (50.88 ns cycle) versus Ideal (no faults), RX (Xia et al., redundancy ratio 3 at 20% SAF) and an NVIDIA GTX 1080 Ti.

## Language models evaluated
- Models: BERT-Base, XLNet, XLM, Transformer (base, 512-d)
- Scale: ~65M-110M+ (pre-trained attention NNs)

## Contributions
- Pipelined ReRAM accelerator for attention-based NNs with hazard handling and GELU/LayerNorm/softmax modules
- NuXG non-uniform crossbar-grouping redundancy exploiting layer-wise sparsity
- Evaluation on Transformer, BERT-base, XLNet, XLM versus GPU and RX redundancy

## Key claims (stable IDs)
- **2020_Guo_ATT_ICCD#C1** — ATT improves throughput ~2.5x over RX for all benchmarks (least on XLNet) — _support:_ ATT stores ~2.5x the weight matrices of RX — _loc:_ Sec. VI-B / Fig. 6
- **2020_Guo_ATT_ICCD#C2** — ATT reaches ~60% of ideal power efficiency while RX reaches only 20-25% — _support:_ ~60% vs 20-25% — _loc:_ Sec. VI-B / Fig. 6
- **2020_Guo_ATT_ICCD#C3** — Average speedup over GPU: ATT 125.28x, Ideal 202.78x, RX 50.69x — _support:_ as stated — _loc:_ Sec. VI-C / Fig. 8
- **2020_Guo_ATT_ICCD#C4** — ATT energy only ~1.5x of ideal case while achieving near-same accuracy — _support:_ energy breakdown — _loc:_ Sec. VI-C / Fig. 7
- **2020_Guo_ATT_ICCD#C5** — Pruned layer sparsity varies strongly by depth; last BERT/XLNet layers near 100% — _support:_ max accuracy loss 1.9% (Transformer) — _loc:_ Fig. 5

## Results
- Throughput ~2.5x vs RX; RX gets one quarter of Ideal throughput
- Power efficiency ~60% of Ideal vs 20-25% for RX
- Speedup over GTX 1080 Ti: ATT 125.28x, RX 50.69x, Ideal 202.78x
- ATT energy ~1.5x Ideal; ADC/DAC dominate energy in all schemes
- Weight-sparsity grouping: required fault-free fraction 0.9/0.95/0.99 for Low/Medium/High classes

## Key numbers
- tech_node: 32nm (scaled)
- array_size: 128x128
- energy_eff: ~60% of ideal power efficiency (GOPs/W)
- throughput: ~2.5x vs RX
- accuracy: <2% accuracy loss (max 1.9% Transformer) with pruning
- bits_weight: 16-bit ops
- bits_adc: 1-bit DAC

## Datasets / benchmarks
Transformer, BERT-base, XLNet, XLM

## Limitations
- Simulation only with in-house NVSim-based model
- Only stuck-at faults considered (20% SAF); no analog noise, drift or IR drop
- Sparsity configuration not optimized; assumes pruned models with <2% accuracy loss
- Attention products Q.K^T and softmax(.).V computed in digital engines, not on crossbars
- Compared with GTX 1080 Ti, an old GPU; baselines limited to RX
- Transformer-scale models (up to ~110M-class), no SLM/LLM

## Remarks
Early (2020) ReRAM Transformer accelerator that identifies the key obstacles (dynamic attention, GELU, LayerNorm, SAF) later papers address. Its insight that redundancy requirements differ by layer sparsity is a transferable fault-tolerance idea, but accuracy under faults is only described qualitatively. Related to ReTransformer/X-Former and SAF handling by matrix transformation in the collection.

## Cites (in collection, 3)
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019) — _contrasts/critiques_: "Meanwhile, Zhang et al. [13], [41] also use similar methods to handle this issue."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Processing-in-Memory (PIM) platforms are more and more popular in accelerating neural network applications due to fewer data movements compared to FPGA and ASIC implementations [1–3]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Processing-in-Memory (PIM) platforms are more and more popular in accelerating neural network applications due to fewer data movements compared to FPGA and ASIC implementations [1–3]."

## Cited by (in collection, 3)
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _background_: "Some studies [15– 18] explore eNVM-friendly data access through techniques like matrix decomposition or fine-grained dataflow designs to accelerate the VMM primitive in attention computation."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _contrasts/critiques_: "For example, designs like iMCAT [19], ATT [21], ReBERT [22], iMTransformer [24], and X-Former [25] focus on smaller-scale, encoder-only models such as BERT variants."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _contrasts/critiques_: "ATT [16] customizes matrix-matrix multiplication circuits for these matrix multiplications in the digital domain to avoid writing K and V to ReRAM."

## Files
- PDF: [../../04_Transformers_and_LLMs/2020_Guo_ATT_ICCD.pdf](../../04_Transformers_and_LLMs/2020_Guo_ATT_ICCD.pdf)
- Full text: [../fulltext/2020_Guo_ATT_ICCD.txt](../fulltext/2020_Guo_ATT_ICCD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccd50377.2020.00047
