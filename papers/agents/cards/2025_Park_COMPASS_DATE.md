---
id: W4410583474
key: 2025_Park_COMPASS_DATE
title: "COMPASS: A Compiler Framework for Resource-Constrained Crossbar-Array Based In-Memory Deep Learning Accelerators"
short: "COMPASS"
year: 2025
venue: "DATE"
venue_full: "Design, Automation & Test in Europe Conference & Exhibition (DATE 2025)"
authors: "Jihoon Park, Jeongin Choe, Dohyun Kim, Jae‐Joon Kim"
category: "05 Mapping, Compilation & Dataflow"
devices: ["SRAM-analog"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["compiler-software-stack", "tiling-partitioning", "scheduling", "dataflow-pipelining", "weight-mapping", "energy-efficiency", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 4
citations_overall: 3
priority_score: 4.92
doi: "https://doi.org/10.23919/date64628.2025.10993229"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2025_Park_COMPASS_DATE.pdf"
fulltext: "../fulltext/2025_Park_COMPASS_DATE.txt"
---

# COMPASS

**COMPASS: A Compiler Framework for Resource-Constrained Crossbar-Array Based In-Memory Deep Learning Accelerators** — Design, Automation & Test in Europe Conference & Exhibition (DATE 2025) (2025)

## TL;DR
COMPASS is a compiler that partitions DNNs larger than on-chip crossbar capacity into sequentially executed, weight-reloaded partitions using a genetic algorithm that jointly handles weight replication and batching, giving 1.78x throughput and 1.28x EDP over greedy/layerwise partitioning.

## Summary
Existing PIM compilers (PUMA, PIMCOMP) assume all weights fit on chip, but prototype macros hold only hundreds of KB to a few MB. COMPASS targets a Macro-Core-Chip template (as in PIMCOMP/PUMA) extended with a weight-replacement phase: a partition of the model is mapped and executed in a pipelined manner (weight-reuse phase), then the core loads new weights from global memory (DRAM) and broadcasts them to crossbars for writing before the next partition. The compiler has a partition generator (smallest core-mapping units combined into partition groups), a partition optimizer (genetic algorithm where a gene is a partition and a chromosome a partition group; fitness is throughput or EDP via a latency estimator extended from PIMCOMP to include weight load and intermediate load/store; four mutation schemes) and a scheduler generating weight-write and activation load/store instructions. Weight replication per partition balances pipeline stages and is optimized jointly. Evaluation is simulation on 256x256 crossbars with power from a 16 nm SRAM IMC prototype (Jia et al.) including ADC, DRAM energy via DRAMsim3, three chip sizes S/M/L, 4b weights/activations, VGG16/ResNet18/SqueezeNet, GA population 100 for 30 generations. Results: 1.78x average throughput over baselines (1.80x/1.71x/2.24x vs greedy and 1.56x/1.31x/1.98x vs layerwise on VGG16/ResNet/SqueezeNet), EDP better by 1.28x vs greedy and 2.08x vs layerwise; batch size 16 amortizes weight-replacement energy while at batch 1 weight load dominates.

## Contributions
- First compiler framework for analog/crossbar PIM that accounts for communication with external memory when the model exceeds on-chip capacity.
- Network partitioning with weight reloading and multi-endpoint dependency checks (residual connections).
- Genetic algorithm with a fitness function optimizing throughput and EDP including weight replication.
- Extension of open-source PIMCOMP to support partitioned execution.

## Key claims (stable IDs)
- **2025_Park_COMPASS_DATE#C1** — 1.78x average throughput over greedy and layerwise partitioning. — _support:_ 1.80/1.71/2.24x vs greedy; 1.56/1.31/1.98x vs layerwise on VGG16/ResNet18/SqueezeNet — _loc:_ Sec. IV-B1, Fig. 6
- **2025_Park_COMPASS_DATE#C2** — EDP improvement of 1.28x vs greedy and 2.08x vs layerwise on average. — _support:_ energy rises due to more DRAM traffic but joint optimum wins — _loc:_ Sec. IV-B2, Fig. 8
- **2025_Park_COMPASS_DATE#C3** — Existing compilers can only map SqueezeNet on resource-constrained chips, COMPASS maps all three models. — _support:_ evaluation text — _loc:_ Sec. IV-A2
- **2025_Park_COMPASS_DATE#C4** — Batch size 16 sufficiently amortizes weight replacement; at batch 1 weight-load energy dominates compute. — _support:_ energy normalized to MVMUL — _loc:_ Sec. IV-B3, Fig. 9

## Results
- 1.78x throughput; 1.28x EDP over baseline partitioning (abstract).
- GA converges to its optimal partition count by generation 9-10 for ResNet18-M-16 (Fig. 10).
- Latency-optimized solutions use more replication, reducing pipeline depth and increasing DRAM communication energy (Fig. 8).

## Key numbers
- tech_node: 16nm (scaled from SRAM IMC prototype)
- array_size: 256x256
- energy_eff: 1.28x EDP improvement
- throughput: 1.78x
- bits_weight: 4b

## Datasets / benchmarks
VGG16, ResNet18, SqueezeNet

## Limitations
- Evaluated only on an SRAM-based IMC model; NVM (ReRAM endurance, MRAM write cost) applicability argued but not evaluated.
- CNNs only (VGG16, ResNet18, SqueezeNet); no Transformers or LMs.
- Pure simulation with latency/energy estimator; no analog non-ideality or accuracy evaluation (4b precision assumed).
- Weight rewriting is assumed cheap enough; endurance-limited NVM would punish frequent replacement.

## Remarks
Directly relevant to LM deployment because billion-parameter models far exceed on-chip crossbar capacity, forcing weight replacement; COMPASS gives a partition/reload formulation but only for CNNs and with SRAM write costs. For ReRAM/PCM the write energy, latency and endurance would change the optimum drastically. Complements PIMCOMP and PUMA in the collection.

## Cites (in collection, 4)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Recognizing these challenges, attention to Processing-In-Memory (PIM) architectures has been rapidly increasing as an alternative to traditional architecture [1–4]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "PIM-aware compilers like PUMA [13] and PIMCOMP [3] have their primary focus on mapping all the weights on chip, but it is not possible to map large networks on chip when PIM memory footprint is constrained to tens of MBs at most."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Recognizing these challenges, attention to Processing-In-Memory (PIM) architectures has been rapidly increasing as an alternative to traditional architecture [1–4]."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _uses-method-or-tool_: "All partitioning schemes, including ours, are implemented by extending the open-source PIMCOMP framework [3]."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2025_Park_COMPASS_DATE.pdf](../../05_Mapping_Compilation_and_Dataflow/2025_Park_COMPASS_DATE.pdf)
- Full text: [../fulltext/2025_Park_COMPASS_DATE.txt](../fulltext/2025_Park_COMPASS_DATE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.23919/date64628.2025.10993229
