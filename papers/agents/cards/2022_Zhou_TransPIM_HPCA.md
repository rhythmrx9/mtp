---
id: W4280496502
key: 2022_Zhou_TransPIM_HPCA
title: "TransPIM: A Memory-based Acceleration via Software-Hardware Co-Design for Transformer"
short: "TransPIM"
year: 2022
venue: "HPCA"
venue_full: "2022 IEEE International Symposium on High-Performance Computer Architecture (HPCA 2022)"
authors: "Minxuan Zhou, Weihong Xu, Jaeyoung Kang, Tajana Rosing"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["DRAM"]
models: ["Transformer", "BERT", "GPT/LLM"]
lm_models: ["RoBERTa", "Pegasus", "GPT-2-medium"]
param_scale: "~355M (GPT-2-medium); RoBERTa and Pegasus sizes not stated in the text"
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "dataflow-pipelining", "tiling-partitioning", "heterogeneous-analog-digital", "nonlinear-functions", "language-models", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 1
citations_overall: 142
priority_score: 9.44
doi: "https://doi.org/10.1109/hpca53966.2022.00082"
pdf: "../../04_Transformers_and_LLMs/2022_Zhou_TransPIM_HPCA.pdf"
fulltext: "../fulltext/2022_Zhou_TransPIM_HPCA.txt"
---

# TransPIM

**TransPIM: A Memory-based Acceleration via Software-Hardware Co-Design for Transformer** — 2022 IEEE International Symposium on High-Performance Computer Architecture (HPCA 2022) (2022)

## TL;DR
TransPIM maps Transformer inference onto HBM with a token-based data-sharding dataflow plus per-bank auxiliary compute units and ring-broadcast links, simulated at 22.1-114.9x faster than an RTX 2080Ti and 3.7x/9.1x faster than PIM-only/near-bank-only HBM baselines.

## Summary
Memory-based accelerators built for CNNs use layer-based dataflows, which the authors measure to spend about 60% of time on data movement for RoBERTa on an 8-stack HBM bit-serial PIM system, and bit-serial reductions take 23-32% of time (Sec. II-C, Fig. 3). TransPIM replaces the layer-based mapping by splitting the L input tokens into shards across HBM banks; each bank keeps Q/K/V and FFN intermediates for its own tokens through all layers, loads the full FC/FFN weights, computes local attention scores, then obtains remote K/V through a ring broadcast (Sec. III, Fig. 4). Hardware additions to commodity HBM2 are per-bank auxiliary compute units (ACUs; a 4-parallel bit-serial adder tree for reduction and Softmax support) plus data buffers and ring-broadcast links, costing 2.15 mm2 (4.0%) per 8 GB chip, synthesized at 65 nm and scaled (Table II). Evaluation is a cycle-level simulator with up to 8 HBM stacks (64 GB, 256 GB/s host link) against an RTX 2080Ti, TPUv3, a near-bank-processing baseline and original bit-serial PIM, on RoBERTa (IMDB, TriviaQA), Pegasus (PubMed, Arxiv) and GPT-2-medium language modelling (Sec. V). Results are 22.1-114.9x speedup and 138.1-666.6x energy efficiency over GPU, plus 2.0-3.3x peak throughput over A3/SpAtten ASICs; decoder-only GPT-2 gains are smaller (1.4x speed, 2.1x energy vs Layer-TransPIM) because only one token is processed per step.

## Language models evaluated
- Models: RoBERTa, Pegasus, GPT-2-medium
- Scale: ~355M (GPT-2-medium); RoBERTa and Pegasus sizes not stated in the text

## Contributions
- First end-to-end memory-based accelerator for the whole Transformer, not just attention.
- Token-based data-sharding dataflow, reported 4.6x faster than layer-based dataflow on memory-based architectures.
- Lightweight HBM modifications (per-bank ACUs and ring broadcast data path) enabling hybrid PIM/near-memory processing with 4.0% area overhead.
- Evaluation against GPU, TPU, NMC, PIM and ASIC baselines across encoder and decoder workloads and sequence lengths up to 32K (synthetic).

## Key claims (stable IDs)
- **2022_Zhou_TransPIM_HPCA#C1** — Layer-based dataflow wastes most time on data movement for Transformers on bit-serial HBM PIM. — _support:_ around 60% of execution time is data loading/reorganisation; reductions take 23-32% — _loc:_ Sec. II-C, Fig. 3
- **2022_Zhou_TransPIM_HPCA#C2** — TransPIM is much faster and more energy-efficient than GPU/TPU. — _support:_ 22.1x (8.7x) to 114.9x (57.4x) faster than GPU (TPU); 138.1x (39.5x) to 666.6x (376.7x) better energy efficiency — _loc:_ Sec. V, Fig. 10
- **2022_Zhou_TransPIM_HPCA#C3** — Combining PIM and near-memory ACUs beats either alone. — _support:_ 3.7x faster than PIM-only, 9.1x faster than NBP with token sharding — _loc:_ Sec. V, Fig. 10
- **2022_Zhou_TransPIM_HPCA#C4** — Speedup shrinks for decoder-only models. — _support:_ GPT-2 LM: 1.4x faster and 2.1x more energy efficient than Layer-TransPIM — _loc:_ Sec. V, decoder-only paragraph
- **2022_Zhou_TransPIM_HPCA#C5** — Area overhead is small. — _support:_ 2.15 mm2 per 8 GB HBM chip, 4.0% over DRAM — _loc:_ Table II

## Results
- 22.1-114.9x speedup and 138.1-666.6x energy-efficiency over RTX 2080Ti (batched, maximum supported batch size).
- 83.9x and 114.9x speedup on PubMed and Arxiv with Pegasus vs SpAtten's reported 35x generative-stage gain over GPU.
- 2.0-3.3x peak throughput of A3 (221 GOP/s) and SpAtten (360 GOP/s).
- Token-based dataflow reduces data movement; ring-broadcast data path gives 4.1x lower data-movement; ACU cuts reduction latency/energy by up to 10.8x and 5.7x.
- Compute utilisation 45.8% for Token-TransPIM vs 30.8% for Layer-TransPIM.

## Key numbers
- tech_node: 22nm (HBM area via CACTI-3DD), 65nm logic synthesis
- array_size: 512x512 subarray, 32k rows x 1KB
- energy_eff: 138.1-666.6x vs GPU
- throughput: 2.0-3.3x A3/SpAtten peak

## Datasets / benchmarks
IMDB, PubMed, Arxiv, TriviaQA, language modeling (GPT-2)

## Limitations
- Digital DRAM (HBM) bit-serial PIM, not analog or NVM crossbars, so device non-idealities and analog precision are out of scope.
- Cycle-level simulation only; ACU is synthesized in 65 nm and scaled, no fabricated hardware.
- GPU baseline is a single consumer RTX 2080Ti versus 8 HBM stacks (64 GB), so headline speedups are not iso-resource.
- Small energy advantage over near-bank baseline absent (about 0.2% less efficient with same dataflow); decoder-only/autoregressive gains are limited.
- Model sizes of RoBERTa/Pegasus are not reported in the text; only GPT-2-medium is a generative LM.

## Remarks
TransPIM is a well-executed architecture study but its transfer to analog crossbars is at the dataflow level: token-sharded execution and the cost of moving K/V between memory partitions recur in later NVM attention accelerators in this collection (e.g. HARDSEA, PRIMATE, JADE cite it). It is not an analog-IMC or small-LM-on-NVM result, since weights sit in DRAM and arithmetic is bit-serial digital. Treat the large GPU speedups cautiously given the unequal resources.

## Cites (in collection, 1)
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _contrasts/critiques_: "FloatPIM [17] supports reduction by organizing reduction data in a bit-serial way to avoid extra data movement. But this scheme sacrifices parallelism in Transformer which usually has long vectors for reduction."

## Cited by (in collection, 13)
- [2024_Pan_PRIMATE_ASP-DAC](2024_Pan_PRIMATE_ASP-DAC.md) PRIMATE (2024) — _baseline/comparison_: "Compared to baseline [27], the PRIMATE architecture achieves up to 30.6x, average 21x better throughput; up to 29.5x, average 18.9x better space efficiency, and up to 4.3x, average 3.8x better energy efficiency on W1 to W4."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "TransPIM is a DRAM-based PIM accelerator with compute units integrated within High Bandwidth Memory (HBM) banks to accelerate transformer inference [25]."
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _background_: "Some studies [15– 18] explore eNVM-friendly data access through techniques like matrix decomposition or fine-grained dataflow designs to accelerate the VMM primitive in attention computation."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _contrasts/critiques_: "Due to these accuracy concerns, a large body of work [32, 68, 79] has explored digital PIM solutions for processing Transformers while reducing data movement costs."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _baseline/comparison_: "Other CIM works focused on content addressable memories for softmax, ReRAMSRAM hybrid architecture, and processing in off-chip memory to facilitate efficient data communication during transformer inference [26, 32, 33]."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _contrasts/critiques_: "KV cache has been implemented either by dynamic random-access memories (DRAMs)21,23, which have limited parallelism requiring many digital sequential adders, or by SRAMs19,24, which are limited by their volatility and relatively low density25."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _baseline/comparison_: "These works include wafer-scale accelerators [14] and IMC-focused work [41], [42]. This work achieves better performance compared to the previous IMC-based works, thanks to the hybrid IMC-NMC design catered for both the dynamic and static data, as well as the dedicated router design."
- [2025_Malhotra_ReTern_TVLSI](2025_Malhotra_ReTern_TVLSI.md) ReTern (2025) — _background_: "Various CiM-based LLM accelerators have been proposed, showcasing sizeable benefits over conventional von-Neumann based platforms such as GPUs [2]-[5]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _baseline/comparison_: "As listed in Table III, TransPIM [18] presents several variations of its architecture, all achieving a GOPS/W below 200 on the GPT2 Medium model with a 4096 context length."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _baseline/comparison_: "For example, TransPIM [54] using bit-serial row parallel PIM operations substantially reduce data-movement overhead, which highlights the potential of PIM for LLM acceleration."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024)

## Files
- PDF: [../../04_Transformers_and_LLMs/2022_Zhou_TransPIM_HPCA.pdf](../../04_Transformers_and_LLMs/2022_Zhou_TransPIM_HPCA.pdf)
- Full text: [../fulltext/2022_Zhou_TransPIM_HPCA.txt](../fulltext/2022_Zhou_TransPIM_HPCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/hpca53966.2022.00082
