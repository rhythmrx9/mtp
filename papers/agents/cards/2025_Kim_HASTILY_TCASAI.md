---
id: W4413553738
key: 2025_Kim_HASTILY_TCASAI
title: "HASTILY: Hardware-Software Co-Design for Accelerating Transformer Inference Leveraging Compute-in-Memory"
short: "HASTILY"
year: 2025
venue: "TCASAI"
venue_full: "IEEE Transactions on Circuits and Systems for Artificial Intelligence (2025)"
authors: "Dong Eun Kim, Tanvi Sharma, Kaushik Roy"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["SRAM-analog"]
models: ["Transformer", "BERT"]
lm_models: ["BERT-Base", "BERT-Large"]
param_scale: "110M-340M"
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "nonlinear-functions", "dataflow-pipelining", "macro", "compiler-software-stack", "energy-efficiency", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 8
citations_overall: 3
priority_score: 6.32
doi: "https://doi.org/10.1109/tcasai.2025.3601975"
pdf: "../../04_Transformers_and_LLMs/2025_Kim_HASTILY_TCASAI.pdf"
fulltext: "../fulltext/2025_Kim_HASTILY_TCASAI.txt"
---

# HASTILY

**HASTILY: Hardware-Software Co-Design for Accelerating Transformer Inference Leveraging Compute-in-Memory** — IEEE Transactions on Circuits and Systems for Artificial Intelligence (2025) (2025)

## TL;DR
HASTILY is an 8T-SRAM analog-CIM transformer accelerator whose arrays double as exponential lookup tables (UCLMs), plus multi-core softmax reduction and fine-grained row pipelining, reaching 158/263 TOPS and ~8 TOPS/W on BERT-Base/Large (4.4-9.8x TOPS over an A40 GPU) in PUMA-based cycle-level simulation.

## Summary
Attention needs dynamic MatMuls (QK^T, softmax(.)V) and a softmax whose cost and O(l^2) intermediate storage limit weight-stationary CIM accelerators. HASTILY replaces the ReRAM MVMUs of the PUMA spatial architecture (chip, tiles, cores, MVMUs, VFU) with unified compute-and-lookup modules: 8T-SRAM arrays (TSMC 65nm, 64x64 per UCLM) with an extra source line so one array does either analog MVM or a 16-bit exponential LUT lookup, at no measured area overhead. Softmax maxima and partial exponential sums are computed per core and gathered in a binary tree across cores (O(log n)). A fine-grained pipeline processes one input vector per stage across attention and FFN, reducing intermediate-matrix memory from quadratic to linear in sequence length. A compiler for attention and a PUMASim-based cycle simulator (32nm, ~330 mm2, INT-8 inputs/weights) evaluate BERT-Base/Large versus PUMA and an Nvidia A40 (8-bit via bitsandbytes, power via nvidia-smi minus idle). No accuracy/noise experiments: errors are assumed recoverable with hardware-aware training.

## Language models evaluated
- Models: BERT-Base, BERT-Large
- Scale: 110M-340M

## Contributions
- UCLM: 8T-SRAM array performing concurrent MVM and exponential lookup with no area overhead
- Multi-core reduce-and-gather softmax (max and sum) with O(log n) latency
- Fine-grained vector-level pipelining that makes on-chip intermediate memory linear in sequence length
- Compiler and cycle-level CIM simulator for transformer inference (to be open-sourced)
- End-to-end evaluation vs GPU and baseline CIM on BERT-Base/Large

## Key claims (stable IDs)
- **2025_Kim_HASTILY_TCASAI#C1** — Softmax latency at l=8192 drops from 22.13 us (PUMA) to 6 us with UCLM and 1.36 us with multi-core support (ALU width 16). — _support:_ numbers in text — _loc:_ Sec. VI-A, Fig. 7
- **2025_Kim_HASTILY_TCASAI#C2** — End-to-end throughput reaches 158 TOPS (BERT-Base) and 263 TOPS (BERT-Large), up to 9.8x over A40. — _support:_ GPU 19 TOPS vs PUMA 26 TOPS at batch 1 for BERT-Base — _loc:_ Sec. VI-C, Fig. 12
- **2025_Kim_HASTILY_TCASAI#C3** — Energy efficiency is ~8 TOPS/W regardless of model/layers/batch versus 0.3-0.9 TOPS/W for the GPU. — _support:_ Fig. 13 text — _loc:_ Sec. VI-C
- **2025_Kim_HASTILY_TCASAI#C4** — Energy vs PUMA is nearly unchanged because ADC energy dominates. — _support:_ 'ADC energy dominates the overall energy consumption' — _loc:_ Sec. VI-B, Fig. 11

## Results
- Throughput 4.4x-9.8x over Nvidia A40 and 1.7x-5.9x over baseline CIM (PUMA) for BERT, INT-8 (abstract)
- Energy efficiency 16x-36x over A40, similar to PUMA baseline (abstract)
- Encoder layer: 3x-13x faster than GPU with pipelining; 4.47x over PUMA at d=768, l=1024 (softmax acceleration +37%, pipelining +96%)
- Softmax share of runtime at l=1024 falls from 38% (PUMA) to 13%
- Dynamic energy 10x-68x lower than GPU per encoder layer (Fig. 11); area ~330 mm2 at 32nm vs A40 628.4 mm2 (8nm)

## Key numbers
- tech_node: TSMC 65nm (UCLM); 32nm (system simulation)
- array_size: 64x64 UCLM
- energy_eff: ~8 TOPS/W (BERT)
- throughput: 158 TOPS (BERT-Base), 263 TOPS (BERT-Large)
- bits_weight: 8b

## Datasets / benchmarks
BERT-Base, BERT-Large (throughput/energy only)

## Limitations
- Pure architectural simulation (PUMASim modified); only the UCLM macro was designed in 65nm, no silicon
- No accuracy, noise or non-ideality analysis; assumes hardware-aware training fixes analog errors
- Encoder-only BERT; decoder GPT-like models memory-bound so gains would be limited
- SRAM-based; dynamic-weight MatMuls would be costly on NVM crossbars
- Weights assumed to fit on-chip; fine-grained pipelining supports batch up to 2

## Remarks
Clean architectural idea: reuse CIM arrays as LUTs for nonlinear functions and pipeline at vector granularity to avoid O(l^2) storage. It fits the SRAM-analog camp, as writing K^T and V into NVM would be expensive, unlike ReRAM attention designs. Gains come from latency and pipelining since ADC energy dominates, and it says nothing about analog fidelity or language-model accuracy.

## Cites (in collection, 8)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "The initial works on analog CIM based accelerators focused on convolutional and fully connected networks [30, 51-53]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _uses-method-or-tool_: "To maximize the throughput, CIM based spatial accelerators constitute of a hierarchical architecture as proposed in a previous work, PUMA [52]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _motivation_: "We assume that such errors can be reduced during transformer inference using hardware-aware training [60]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _motivation_: "While emerging memories offer a high-density memory solution, they typically suffer from issues such as resistance drift, write endurance and/or low on-off distinguishability [50]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "In the past, compute-in-memory (CIM) has shown great promise in accelerating convolutional and fully-connected layers by leveraging their weight stationary nature, as their feature maps are known before runtime [29-31]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "The initial works on analog CIM based accelerators focused on convolutional and fully connected networks [30, 51-53]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _baseline/comparison_: "Other CIM works focused on content addressable memories for softmax, ReRAMSRAM hybrid architecture, and processing in off-chip memory to facilitate efficient data communication during transformer inference [26, 32, 33]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _baseline/comparison_: "Other CIM works focused on content addressable memories for softmax, ReRAMSRAM hybrid architecture, and processing in off-chip memory to facilitate efficient data communication during transformer inference [26, 32, 33]."

## Cited by (in collection, 1)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)

## Files
- PDF: [../../04_Transformers_and_LLMs/2025_Kim_HASTILY_TCASAI.pdf](../../04_Transformers_and_LLMs/2025_Kim_HASTILY_TCASAI.pdf)
- Full text: [../fulltext/2025_Kim_HASTILY_TCASAI.txt](../fulltext/2025_Kim_HASTILY_TCASAI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcasai.2025.3601975
