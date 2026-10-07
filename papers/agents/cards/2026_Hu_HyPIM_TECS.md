---
id: W7164181555
key: 2026_Hu_HyPIM_TECS
title: "HyPIM: LLM Acceleration with A Hybrid ReRAM/SRAM 3D-PIM Architecture"
short: "HyPIM"
year: 2026
venue: "TECS"
venue_full: "ACM Transactions on Embedded Computing Systems"
authors: "Xiaolong Hu, Chubo Liu, Yan Ding, Keqin Li, Kenli Li"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "SRAM-analog"]
models: ["Transformer", "BERT", "GPT/LLM"]
lm_models: ["BERT-base", "BERT-large", "BART-base", "BART-large"]
param_scale: "110M-406M"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "attention", "3d-integration", "heterogeneous-analog-digital", "pruning-sparsity", "dataflow-pipelining", "language-models", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1145/3820366"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Hu_HyPIM_TECS.pdf"
fulltext: "../fulltext/2026_Hu_HyPIM_TECS.txt"
---

# HyPIM

**HyPIM: LLM Acceleration with A Hybrid ReRAM/SRAM 3D-PIM Architecture** — ACM Transactions on Embedded Computing Systems (2026)

## TL;DR
HyPIM is a monolithic-3D hybrid architecture that puts static linear layers on ReRAM slices and attention matmuls on SRAM slices, plus a softmax-based early-termination and sparse mapping scheme, giving 1.27x-1.67x lower latency than Newton, TransPIM, HAIMA, HARDSEA and H3DAtten.

## Summary
Transformer blocks mix weight-stationary linear layers (QKV, output projection, FFN) with dynamic attention products QK^T and SV, which suit different memories: ReRAM is dense but has low endurance and slow writes, SRAM is fast and durable but low density. HyPIM stacks 4 ReRAM layers (16 tiles x 16 arrays x 16 256x256 subarrays) and 2 SRAM layers (arrays of 256x256, 256x128, 256x64 subarrays) via monolithic 3D integration with MIVs and a small-world NoC (SW-NoC). Weights are tiled into 256x256 sub-matrices with column/row splitting, partial sums accumulated across tiles, and weights can be replicated for token-level parallelism; attention tensors are divided by head across SRAM arrays. A mixed-granularity parallel strategy schedules module execution and dataflow. For attention, a bit-serial early-termination algorithm (in the spirit of A3) stops accumulating score entries once partial sums fall a threshold below the running maximum, with judge start time M and threshold T (selected M=n/2, T=5% of max, L=4); sparse SV products use SRAM arrays with extra BL/BLB lines and a data-aware mapping with index buffer. Evaluation uses 45 nm synthesis (Design Compiler, CACTI, NVSim, Destiny-3D, DSENT, Spice/Virtuoso, ISAAC-derived ReRAM parameters), 1-bit DAC, 8-bit ADC, a cycle-level simulator and BERT-base/large and BART-base/large fine-tuned on MNLI with 512-token max inputs, normalised against an NVIDIA V100.

## Language models evaluated
- Models: BERT-base, BERT-large, BART-base, BART-large
- Scale: 110M-406M
- Note: Only the abstract was available; it names no specific LLMs or scales, targeting hybrid ReRAM/SRAM 3D-PIM.

## Contributions
- 3D hybrid ReRAM/SRAM PIM architecture assigning linear layers to ReRAM and attention products to SRAM
- Mixed-granularity parallel execution and dataflow pipeline for transformer modules
- Early-termination approximation for QK^T and a sparse matrix multiplication co-design (SRAM arrays with index buffer) for SV
- Area/power/latency comparison against five PIM baselines with ablation and scalability study

## Key claims (stable IDs)
- **2026_Hu_HyPIM_TECS#C1** — HyPIM reduces latency 1.27x-1.67x versus Newton, TransPIM, HAIMA, HARDSEA and H3DAtten — _support:_ Abstract; 1.53x-1.76x vs HAIMA and TransPIM — _loc:_ Abstract / Sec. 5.3 / Fig. 10(a)
- **2026_Hu_HyPIM_TECS#C2** — HyPIM has the smallest total area, 15.78% below H3DAtten and >80% below others — _support:_ HyPIM 16.474 mm2 total in Table 3 sense; baselines 19.56-98.98 mm2 — _loc:_ Sec. 5.1 / Table 3
- **2026_Hu_HyPIM_TECS#C3** — 3D stacked hybrid storage gives 1.38x-1.47x, attention approximation 1.02x-1.05x, SW-NoC 1.08x-1.12x — _support:_ Ablation relative to baseline — _loc:_ Sec. 5.3-5.4 / Fig. 10(b)
- **2026_Hu_HyPIM_TECS#C4** — Per-task latency under 10 ms for BERT/BART — _support:_ BERT-base 0.54 ms (302K tokens/s), BERT-large 2 ms (81K), BART-base 1.46 ms (107K), BART-large 6.99 ms (22K) at ~156-162 token inputs — _loc:_ Sec. 5.3 / Fig. 11

## Results
- Latency 1.27x-1.67x better than Newton/TransPIM/HAIMA/HARDSEA/H3DAtten (abstract)
- Area 16.474 mm2 total, power 58.88 W-level figure in Table 3; baseline areas: Newton 88.37, TransPIM 83.08, HAIMA 98.98, HARDSEA 26.52, H3DAtten 19.56 mm2
- Area-power product 23.74% lower than H3DAtten and 27.71% lower than HARDSEA
- Array utilization up 10-20% and cell utilization up 20-30% (max ~80%) with the optimisation strategies (Fig. 11)
- Accuracy: higher judge start time or smaller threshold keeps MNLI accuracy high; M=n/2 and T=5% chosen (Fig. 9)

## Key numbers
- tech_node: 45nm (synthesis library)
- array_size: 256x256 ReRAM subarrays; SRAM 256x256/256x128/256x64
- throughput: 302K tokens/s (BERT-base); 22K tokens/s (BART-large)
- accuracy: MNLI accuracy preserved at M=n/2, T=5%
- bits_weight: 8b
- bits_adc: 8b (1b DAC)

## Datasets / benchmarks
MNLI

## Limitations
- Simulation only; ReRAM modelled with ISAAC parameters and 8-bit ADC, with no device noise, drift or IR-drop injected (only discussed qualitatively)
- Models are BERT/BART encoders at 110M-406M with MNLI classification, not generative decoder SLMs with KV cache
- Attention on SRAM assumes digital/SRAM-PIM, so evidence for analog attention is limited
- Absolute energy/efficiency vs GPU not the headline; Table 3 totals are partly garbled in extraction

## Remarks
Representative of the hybrid ReRAM-for-weights, SRAM-for-attention design pattern (cf. HARDSEA, H3DAtten, HAIMA), adding monolithic 3D stacking and a dynamic early-termination threshold. Gains over the nearest hybrid baselines are modest and come from a simulator the authors built, so treat as architecture-level estimates. Relevant to SLM deployment mainly as a design point; it does not study accuracy under analog non-idealities.

## Cites (in collection, 7)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The simulation parameters for the ReRAM, including tile configuration, area, and power, are derived from prior research [43]."
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023) — _baseline/comparison_: "H3DAtten [30] proposed the heterogeneous 3D-PIM architecture of ReRAM+SRAM and considered the hardware characteristics."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Some PIM architectures such as ISAAC [43], W2W-PIM [31], PRIME [6], and RENO [35] use ReRAM crossbar memory arrays to perform analog data computations."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _contrasts/critiques_: "In addition, although HARDSEA [34] and other methods can skip zero values, the array utilization is low."
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024) — _background_: "H3d-transformer [38] uses 3D technology to heterogeneous DRAM-PIM and TPU for diferent module characteristics of Transformer."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "ReRAM, a new non-volatile memory technology, comes into the field of PIM design because of its high storage density and high efficiency [46]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _baseline/comparison_: "For example, TransPIM [54] using bit-serial row parallel PIM operations substantially reduce data-movement overhead, which highlights the potential of PIM for LLM acceleration."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Hu_HyPIM_TECS.pdf](../../11_Small_Language_Models_on_AIMC/2026_Hu_HyPIM_TECS.pdf)
- Full text: [../fulltext/2026_Hu_HyPIM_TECS.txt](../fulltext/2026_Hu_HyPIM_TECS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3820366
