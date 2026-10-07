---
id: W4388893898
key: 2023_Pelke_MultiCoreCNNMapping_VLSI-SoC
title: "Mapping of CNNs on multi-core RRAM-based CIM architectures"
short: "Multi-core RRAM CNN Mapping"
year: 2023
venue: "VLSI-SoC"
venue_full: "31st IFIP/IEEE International Conference on Very Large Scale Integration (VLSI-SoC 2023)"
authors: "Rebecca Pelke, Nils Bosbach, Jose Cubero, Felix Staudigl, Rainer Leupers, Jan Moritz Joseph"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "MobileNet", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "tiling-partitioning", "dataflow-pipelining", "scheduling", "compiler-software-stack", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 9
priority_score: 4.7
doi: "https://doi.org/10.1109/vlsi-soc57769.2023.10321873"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.pdf"
fulltext: "../fulltext/2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.txt"
---

# Multi-core RRAM CNN Mapping

**Mapping of CNNs on multi-core RRAM-based CIM architectures** — 31st IFIP/IEEE International Conference on Very Large Scale Integration (VLSI-SoC 2023) (2023)

## TL;DR
Decentralized, register-based linear and cyclic synchronization lets cores of a multi-core RRAM CIM system compute partial sums of one conv2D layer in parallel, reaching more than 99% of the theoretical speedup with under 4% extra bus traffic.

## Summary
Splitting a conv2D layer's im2col kernel matrix over several crossbars/cores creates data dependencies because cores in the same horizontal group accumulate partial results into the same output feature map (OFM) vectors in shared memory. Prior sequential scheduling serialises them, and PUMA's centralized attribute buffer needs large synchronization memory. The authors assign each core horizontal-group and vertical-group IDs, treat each OFM vector as a resource owned by one core at a time, and add a single sequence-number register per core written by neighbours via CALL and checked via WAIT. Linear synchronization has all cores process outputs in the same order; cyclic synchronization rotates the starting offset so bias add and activation are spread evenly. A Python compiler lowers TensorFlow conv2D/dense layers to per-core instructions (MVM, LOAD, STORE, MOV, CALL, WAIT) and cfg files; a SystemC/TLM-2.0 approximately-timed simulator with an AXI4 bus runs them. Evaluation uses MobileNet and ResNet-18 conv2D layers with 32x32 to 128x128 crossbars, bus widths 4-64 B and up to 1024 cores, comparing speedup to the sequential scheme and to the upper bound PV (number of conflicting cores). Accuracy is not evaluated since synchronization does not change results.

## Contributions
- Architecture extension: one sequence-number register per core for decentralized event-based synchronization
- Linear and cyclic synchronization compiler algorithms for parallel conv2D partial-sum accumulation
- Cycle-approximate SystemC/TLM simulator and design-space guidance on crossbar size, core count and bus width

## Key claims (stable IDs)
- **2023_Pelke_MultiCoreCNNMapping_VLSI-SoC#C1** — Synchronization schemes reach >99% of theoretical speedup limit — _support:_ Speedup approaches PV; max 16x for MobileNet layer 5 — _loc:_ Sec. V-B / Fig. 5
- **2023_Pelke_MultiCoreCNNMapping_VLSI-SoC#C2** — Synchronization traffic overhead is small — _support:_ <4% extra bus traffic for 32x32 crossbars, <2% for 64x64 — _loc:_ Sec. V-E / Fig. 7, Table II
- **2023_Pelke_MultiCoreCNNMapping_VLSI-SoC#C3** — Synchronization memory reduced by at least 87.5% versus PUMA's attribute buffer — _support:_ 4 kB (1024 cores x 4 B) vs 32K attributes for 64 kB data — _loc:_ Sec. V-D

## Results
- Cyclic slightly faster than linear but linear preferred for simplicity (Sec. V-B)
- 4 B bus supports <=16 cores for >90% of speedup limit; 64 B supports up to 512 cores (Fig. 6)
- Halving crossbar dimension quadruples core count and calls for at least doubling bus width (Sec. V-C)
- Reducing crossbar 64x64 to 32x32 gives up to 2x more speedup vs sequential at up to 4x more cores (Fig. 5)

## Key numbers
- array_size: 32x32 to 128x128 crossbars; up to 1024 cores
- throughput: >99% of theoretical speedup; up to 16x vs sequential

## Datasets / benchmarks
MobileNet conv2D layers, ResNet-18 conv2D layers

## Limitations
- Single-layer, conv2D/dense only; inter-layer dependencies and full-network integration left to future work
- Abstract simulator (approximately timed); no device non-idealities, ADC or energy modelling
- Evaluated on MobileNet and ResNet-18 layers only; no attention or LM layers

## Remarks
A focused mapping/scheduling paper whose contribution is low-cost synchronization rather than accuracy or energy; credibility is moderate (simulation, high abstraction). The multi-core partial-sum accumulation problem also arises for transformer weight matrices tiled across crossbars, but dynamic attention operands are not covered. Directly builds on PUMA's multi-core architecture.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "RRAM-based CIM architectures Several RRAM-based CIM architectures have been presented [6-8, 18]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _extends/builds-on_: "We improve on this idea by proposing a decentralized synchronization scheme that requires significantly less memory."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _background_: "Multiple RRAM devices can be arranged in crossbar structures to enable in-memory computing [16]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Previous works presented accelerator architectures that use RRAM crossbars as matrix-vector multiplication (MVM) units [5-8]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "RRAM-based CIM architectures Several RRAM-based CIM architectures have been presented [6-8, 18]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Previous works presented accelerator architectures that use RRAM crossbars as matrix-vector multiplication (MVM) units [5-8]."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.pdf)
- Full text: [../fulltext/2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.txt](../fulltext/2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/vlsi-soc57769.2023.10321873
