---
id: W4386763580
key: 2023_Sun_PIMCOMP_DAC
title: "PIMCOMP: A Universal Compilation Framework for Crossbar-based PIM DNN Accelerators"
short: "PIMCOMP"
year: 2023
venue: "DAC"
venue_full: "60th ACM/IEEE Design Automation Conference (DAC 2023)"
authors: "Xiaotian Sun, Xinyu Wang, Wanqian Li, Lei Wang, Yinhe Han, Xiaoming Chen"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["compiler-software-stack", "tiling-partitioning", "weight-mapping", "scheduling", "dataflow-pipelining", "crossbar-architecture", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 5
citations_overall: 19
priority_score: 7.44
doi: "https://doi.org/10.1109/dac56929.2023.10247928"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Sun_PIMCOMP_DAC.pdf"
fulltext: "../fulltext/2023_Sun_PIMCOMP_DAC.txt"
---

# PIMCOMP

**PIMCOMP: A Universal Compilation Framework for Crossbar-based PIM DNN Accelerators** — 60th ACM/IEEE Design Automation Conference (DAC 2023) (2023)

## TL;DR
PIMCOMP is a universal four-stage compiler (node partitioning, weight replicating, core mapping, dataflow scheduling) for NVM-crossbar PIM accelerators, using a genetic algorithm and two pipeline modes to gain 1.6x throughput and 2.4x latency over a PUMA-like compiler.

## Summary
Prior crossbar PIM accelerators rely on manual weight mapping and heuristic weight replication, and PUMA's compiler pipelines at inference granularity, which hurts latency. PIMCOMP defines an abstract accelerator (cores with PIM matrix unit of crossbars, vector functional unit, local memory, global memory; compatible with Crossbar/IMA/Tile/Chip) and an execution model with MVM, VEC, COMM and MEM operations whose parallelism is limited by structural conflicts, data dependencies and bandwidth. It loads ONNX models and (1) partitions conv/FC layers: kernels are flattened into a (Kh*Kw*Cin) x Cout matrix split into Array Groups (AG), each spanning ceil(Cout/Wxbar) crossbars so inputs can be broadcast; (2-3) weight replication and core mapping are optimized jointly by a genetic algorithm with genes encoding node index and AG count, four mutation operators (add/remove replica, spread/merge AGs) and mode-specific fitness (HT: max over cores of ideal time given on-chip bandwidth; LL: runtime estimated from provider/consumer waiting ratios); (4) dataflow scheduling generates HT (layer-by-layer, cross-inference pipelining) or LL (fine-grained, forward output as soon as enough input) instruction streams with ADD-reuse and AG-reuse memory reuse. Evaluation uses a cycle-accurate simulator instantiated with PUMA parameters (ReRAM 2-bit cells, 16-bit fixed point, 64 crossbars/core, 36 cores/chip, 62.92 mm2) on VGG-16, ResNet-18, SqueezeNet, GoogLeNet and Inception-v3.

## Contributions
- Abstract crossbar PIM architecture and execution model for studying DNN execution
- High-throughput and low-latency compilation modes with different inter-layer pipeline granularity
- Genetic algorithm jointly optimizing weight replication and core mapping with mode-specific fitness
- Scheduling algorithms for complex topologies and AG-reuse on-chip memory optimization

## Key claims (stable IDs)
- **2023_Sun_PIMCOMP_DAC#C1** — PIMCOMP outperforms PUMA-like compilation — _support:_ 1.6x throughput and 2.4x latency improvement on average — _loc:_ Abstract, Sec. V-B1, Fig. 8
- **2023_Sun_PIMCOMP_DAC#C2** — LL mode reduces static energy — _support:_ 58.3% static energy reduction by shortening runtime — _loc:_ Sec. V-B2, Fig. 9
- **2023_Sun_PIMCOMP_DAC#C3** — AG-reuse cuts memory traffic — _support:_ 47.8% average reduction of global memory accesses in HT mode; LL local memory usage stays within 64 kB — _loc:_ Sec. V-B3, Fig. 10
- **2023_Sun_PIMCOMP_DAC#C4** — Gains shrink with higher MVM parallelism and for light networks — _support:_ improvement decreases as parallelism grows; GoogLeNet and SqueezeNet limited in HT because memory/vector ops dominate — _loc:_ Sec. V-B1

## Results
- Up to 3.9x normalized HT throughput (VGG-16 at lowest parallelism) and 2.6x LL speed in Fig. 8 across five CNNs
- Dynamic energy similar to PUMA; static energy differs (slight increase in HT, -58.3% in LL)
- Chip: 36 cores, 64 crossbars per core, 62.92 mm2, 56.79 W (Table I)

## Key numbers
- array_size: 64 crossbars per core, 36 cores per chip
- energy_eff: -58.3% static energy (LL mode)
- throughput: 1.6x throughput, 2.4x latency vs PUMA-like
- bits_weight: 16b fixed point, 2-bit ReRAM cells

## Datasets / benchmarks
VGG-16, ResNet-18, SqueezeNet, GoogLeNet, Inception-v3

## Limitations
- Simulation only; crossbars treated as ideal MVM engines without noise or ADC accuracy modelling
- Assumes all model weights fit on chip across crossbars
- CNN benchmarks only; transformers and dynamic matmuls (attention) are not handled
- Benchmarked against a reimplemented PUMA-like dataflow rather than the original compiler
- Does not model detailed PIM matrix unit optimizations (mixed crossbar size, low-bit ADCs)

## Remarks
A compact, influential compiler paper that frames crossbar compilation as replication, mapping and scheduling, and introduces the Array Group abstraction used by follow-ups. Its static-weights-on-chip and CNN-only assumptions limit direct use for language models, where KV caches and dynamic matmuls require different mapping. Relevant to the collection as the mapping baseline for PUMA/ISAAC-style architectures.

## Cites (in collection, 5)
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _background_: "Nonetheless, related optimizations such as mixed size crossbars [13] and low-bit ADCs [14] are compatible with this abstract architecture."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _baseline/comparison_: "In the field of PIM, PUMA [10] is the first memristor-based ML inference accelerator that supports ISA with a compiler that can convert high-level languages into ISA code. Nonetheless, heuristic weight replicating and core mapping methods adopted by its compiler are difficult to guarantee high performance."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "The 2D crossbar structure formed by NVM devices has attracted growing interest due to its high memory density and parallel in-situ computing properties [4]."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021) — _contrasts/critiques_: "There are previous works (e.g., [5]–[9]) proposing NVM crossbar-based PIM DNN accelerators. However, they mainly focus on the design of specific architectures and lack consideration of the execution details of DNNs."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "Our proposed abstract architecture is compatible with the Crossbar/IMA/Tile/Chip structure widely adopted in previous work [5]."

## Cited by (in collection, 6)
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _extends/builds-on_: "A previous version of this work was published in [12], which provides an optimization scheme for resource allocation, task mapping, and pipeline dataflow through four stages: layer partitioning, weight replication, core mapping, and dataflow scheduling."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "With the increasing attention on CIM, there has been a significant surge in efforts to develop a compilation optimization stack aimed at facilitating the deployment of DNN algorithms across various CIM architectures [3, 33, 39, 44]."
- [2025_Park_COMPASS_DATE](2025_Park_COMPASS_DATE.md) COMPASS (2025) — _uses-method-or-tool_: "All partitioning schemes, including ours, are implemented by extending the open-source PIMCOMP framework [3]."
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2025_Xiong_ASMA_ICCD](2025_Xiong_ASMA_ICCD.md) ASMA (2025)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Sun_PIMCOMP_DAC.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Sun_PIMCOMP_DAC.pdf)
- Full text: [../fulltext/2023_Sun_PIMCOMP_DAC.txt](../fulltext/2023_Sun_PIMCOMP_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/dac56929.2023.10247928
