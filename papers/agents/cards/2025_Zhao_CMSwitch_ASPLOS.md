---
id: W4408893285
key: 2025_Zhao_CMSwitch_ASPLOS
title: "Be CIM or Be Memory: A Dual-mode-aware DNN Compiler for CIM Accelerators"
short: "CMSwitch"
year: 2025
venue: "ASPLOS"
venue_full: "Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2025)"
authors: "Shixin Zhao, Yuming Li, Bing Li, Yintao He, Mengdi Wang, Yinhe Han, Ying Wang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["DRAM"]
models: ["CNN", "ResNet", "VGG", "MobileNet", "BERT", "GPT/LLM"]
lm_models: ["BERT-large", "OPT-6.7B", "OPT-13B", "LLaMA 2-7B"]
param_scale: "340M-13B"
slm: false
evidence: simulation
topics: ["compiler-software-stack", "scheduling", "tiling-partitioning", "weight-mapping", "kv-cache", "language-models", "dataflow-pipelining"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 13
citations_overall: 2
priority_score: 4.83
doi: "https://doi.org/10.1145/3676641.3716248"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2025_Zhao_CMSwitch_ASPLOS.pdf"
fulltext: "../fulltext/2025_Zhao_CMSwitch_ASPLOS.txt"
---

# CMSwitch

**Be CIM or Be Memory: A Dual-mode-aware DNN Compiler for CIM Accelerators** — Proceedings of the 30th ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2025) (2025)

## TL;DR
CMSwitch is a CIM compiler that treats each array's compute/memory mode as a compile-time decision (DP network segmentation + MIP array allocation), giving 1.31x average (up to 2.03x) latency speedup over CIM-MLC, PUMA and OCC on a Dynaplasia-like dual-mode chip.

## Summary
Prior CIM compilers assume all arrays hold weights in compute mode, but real dual-mode CIM chips (e.g. Dynaplasia, an eDRAM-based design) can switch arrays between compute and memory (scratchpad) mode by changing the input-driver signals. The paper shows that CNNs (arithmetic intensity ~66 for ResNet50) want ~80% of arrays in compute mode while LLaMA2 (intensity ~2) peaks near 10% compute. CMSwitch adds a mode-switch attribute to the hardware abstraction (number of switchable arrays, array size 320x320, buffer, internal bandwidth, switch latency), partitions the network into segments with dynamic programming that includes switch overhead, and solves per-segment operator-to-array allocation and scheduling with mixed-integer programming. Output is a meta-operator flow including CM.switch(TOM/TOC, addr). Evaluation uses a functional simulator from CIM-MLC and a latency simulator built on open-source simulators, configured to Dynaplasia (96 switchable arrays, 320x320, 10KBx8 buffer, 32b/cycle, 1-cycle switch), with 8-bit weights/activations and sequence length 64 for transformers. Benchmarks are MobileNet, ResNet18, VGG16 (ImageNet), BERT-large, OPT and LLaMA 2.

## Language models evaluated
- Models: BERT-large, OPT-6.7B, OPT-13B, LLaMA 2-7B
- Scale: 340M-13B

## Contributions
- Identifies compute-memory mode switching as a missing dimension in CIM compilation and adds it to the hardware abstraction
- DP segmentation plus MIP array allocation/scheduling that jointly decides array modes and operator mapping
- Meta-operator code generation with a CM.switch operator for generality across backends
- Average 1.31x (max 2.03x) speedup over CIM-MLC across CNNs and transformers/LLMs

## Key claims (stable IDs)
- **2025_Zhao_CMSwitch_ASPLOS#C1** — Optimal compute-array fraction differs per model: ResNet50 ~80%, LLaMA2 ~10% — _support:_ arithmetic intensity 66 vs ~2 — _loc:_ Sec. 1, Fig. 1b, Fig. 5
- **2025_Zhao_CMSwitch_ASPLOS#C2** — Dual-mode-aware compilation gives 1.31x average speedup over CIM-MLC — _support:_ max 2.03x (OPT-13B) — _loc:_ Sec. 5.2, Fig. 14
- **2025_Zhao_CMSwitch_ASPLOS#C3** — Large models benefit most because weights cannot all be mapped on chip — _support:_ OPT-13B 1.20-2.03x (avg 1.73x) vs BERT-large avg 1.17x — _loc:_ Sec. 5.2

## Results
- BERT-large 1.02-1.25x (avg 1.17x) vs CIM-MLC
- LLaMA2-7B 1.13-1.30x (avg 1.24x); OPT-13B 1.20-2.03x (avg 1.73x)
- MobileNet 1.06-1.23x, ResNet18 1.07-1.23x, VGG16 1.32-1.48x
- Compiled schedules put 33%-67% of arrays in memory mode per operator (Sec. 5.3)

## Key numbers
- array_size: 320x320 (96 switchable arrays)
- throughput: 1.31x average speedup vs CIM-MLC
- bits_weight: 8b

## Datasets / benchmarks
ImageNet

## Limitations
- Latency-only, simulated; no accuracy, energy or analog noise
- Target is an SRAM/eDRAM-style digital dual-mode CIM (Dynaplasia), not analog NVM crossbars where writes are costly
- Static weights assumed; weight reloading cost for NVM not central
- Sequence length 64 only for main results; baselines re-implemented on same simulator

## Remarks
A useful compiler-level argument that LLM workloads are memory-bound and that fixing all CIM arrays as compute is wrong for transformers. The idea transfers to analog crossbars only partially because NVM arrays cannot be cheaply switched to scratchpad. Evidence is simulation-only; relevant to the collection as a mapping/compilation reference next to CIM-MLC, OCC, PIMCOMP and PUMA.

## Cites (in collection, 13)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "The Computing-In-Memory (CIM) architecture is highly regarded for enabling in-situ computation [3, 5, 8, 9, 15, 38, 41]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _baseline/comparison_: "PUMA [3] (focusing on operator duplication and pipeline scheduling), OCC [39] (optimizing operator mapping via tiling and loop unrolling), and CIM-MLC [33] (employing multi-grained pipelining and operator duplication for diverse architecture)."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "The dual-mode CIM array can operate as both a memory and compute unit when applying a slight enhancement on the input or output drivers [2, 10, 18, 24, 42, 48, 51, 53]."
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _baseline/comparison_: "To enhance efficiency and fully realize the potential of the CIM accelerators, researchers have explored various compilation optimization techniques, aimed at various CIM architectures such as resistant RAM and SRAM-based solutions [14, 16, 21, 33, 39, 44]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Compared to conventional architectures, CIM significantly mitigates persistent memory wall problem [49] and demonstrates strong competitiveness in data-intensive applications especially deep neural network (DNN) inference [38, 43, 52]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Compared to conventional architectures, CIM significantly mitigates persistent memory wall problem [49] and demonstrates strong competitiveness in data-intensive applications especially deep neural network (DNN) inference [38, 43, 52]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _background_: "With the increasing attention on CIM, there has been a significant surge in efforts to develop a compilation optimization stack aimed at facilitating the deployment of DNN algorithms across various CIM architectures [3, 33, 39, 44]."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _baseline/comparison_: "Compared with state-of-the-art compilation works [33], CMSwitch achieves average inference speed improvement by 1.31x."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2025_Zhao_CMSwitch_ASPLOS.pdf](../../05_Mapping_Compilation_and_Dataflow/2025_Zhao_CMSwitch_ASPLOS.pdf)
- Full text: [../fulltext/2025_Zhao_CMSwitch_ASPLOS.txt](../fulltext/2025_Zhao_CMSwitch_ASPLOS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3676641.3716248
