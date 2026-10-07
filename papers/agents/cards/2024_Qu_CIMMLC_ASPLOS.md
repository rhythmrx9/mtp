---
id: W4394998365
key: 2024_Qu_CIMMLC_ASPLOS
title: "CIM-MLC: A Multi-level Compilation Stack for Computing-In-Memory Accelerators"
short: "CIM-MLC"
year: 2024
venue: "ASPLOS"
venue_full: "ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2024)"
authors: "Songyun Qu, Shixin Zhao, Bing Li, Yintao He, Xuyi Cai, Lei Zhang, Ying Wang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM", "SRAM-digital", "Generic-NVM"]
models: ["CNN", "ResNet", "VGG", "ViT"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["compiler-software-stack", "weight-mapping", "tiling-partitioning", "scheduling", "dataflow-pipelining", "crossbar-architecture", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 11
citations_overall: 11
priority_score: 7.58
doi: "https://doi.org/10.1145/3620665.3640359"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2024_Qu_CIMMLC_ASPLOS.pdf"
fulltext: "../fulltext/2024_Qu_CIMMLC_ASPLOS.txt"
---

# CIM-MLC

**CIM-MLC: A Multi-level Compilation Stack for Computing-In-Memory Accelerators** — ACM International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS 2024) (2024)

## TL;DR
CIM-MLC is a multi-level compilation stack with a hierarchical hardware abstraction (chip/core/crossbar) that schedules DNNs at computing-graph, MVM and VVM granularity, giving up to 3.2x speedup over a prior CIM compiler and 2.3x/3.7x speedups plus 75% peak-power cut on three existing CIM designs.

## Summary
Existing CIM designs either hand-map networks or ship ad-hoc compilers bound to one architecture, and open stacks like TVM lack CIM architectural support. CIM-MLC abstracts a CIM accelerator by its architecture parameters (chip/core/crossbar tiers, crossbar size and count, device precision) and its computing mode (core-level CM, crossbar-level XBM, wordline-level WLM) through a Virtual Crossbar (VXB). A multi-level scheduler then optimizes at computing-graph (CG, operator duplication and pipelining), MVM (crossbar allocation and MVM sequencing) and VVM (row-level remapping so partial row groups compute in parallel) granularity, emitting a meta-operator flow and CIM instructions. Evaluation uses a Python functional simulator checked against PyTorch and a performance simulator extended from PUMA-related open simulators; the baseline is ISAAC-like (Table 3), benchmarks are VGG, ResNet and ViT with 8-bit quantization on ImageNet. Generality is shown on PUMA (ReRAM), Jia et al. (SRAM CIM, 16 CIMUs of 1152x256) and Jain et al. (SRAM macro with <=32 rows active).

## Contributions
- Hardware abstraction of CIM hierarchy (Abs-arch) and computing mode (Abs-com) covering ReRAM/SRAM and other devices
- Multi-level scheduling (CG, MVM, VVM) avoiding intractable single-level fine-grained scheduling
- Verification on three published CIM accelerators and comparison to a CIM compiler (Poly-Schedule)

## Key claims (stable IDs)
- **2024_Qu_CIMMLC_ASPLOS#C1** — Up to 3.2x faster than the prior compiler Poly-Schedule — _support:_ 95% vs 84% cycle reduction — _loc:_ Sec. 4.2, Fig. 20(d)
- **2024_Qu_CIMMLC_ASPLOS#C2** — 2.3x and 3.7x speedup on Jain et al. and Jia et al. macros; 75% peak-power reduction on PUMA — _support:_ VGG7 / CG-grained P&D — _loc:_ Sec. 1, Fig. 20
- **2024_Qu_CIMMLC_ASPLOS#C3** — Pipelining speedup grows with depth — _support:_ CG-Pipeline 2.3x to 4.7x from ResNet18 to ResNet101; MVM-grained cuts peak power up to 85% on ResNet101 — _loc:_ Sec. 4.3, Fig. 21

## Results
- CG-grained optimization speedup 15x to 30x as on-chip crossbar count grows (Fig. 22)
- VVM-grained gives ~10% extra speedup on ResNet50 (Fig. 21c)
- MVM-grained gives no benefit when crossbars per core are few (Jain macro)

## Key numbers
- array_size: 1152x256 (Jia CIMU), <=32 active rows (Jain)
- energy_eff: 75% peak power reduction (PUMA)
- throughput: 3.2x vs Poly-Schedule
- bits_weight: 8b

## Datasets / benchmarks
ImageNet

## Limitations
- Non-explicated architecture parameters treated as ideal (infinite buffer bandwidth)
- Simulation only; no analog noise or accuracy modelling
- Evaluated mainly on CNNs plus ViT; no language models or dynamic MatMul/KV-cache handling

## Remarks
Solid systems paper establishing a general CIM compiler abstraction; its tiers map neatly onto crossbar mapping of transformers, but attention's dynamic operands and non-ideality-aware mapping are absent. Latency-focused and ideal-peripheral assumptions limit realism.

## Cites (in collection, 11)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _extends/builds-on_: "To accommodate different CIM designs for executing MVM on crossbars [4, 39, 42, 51], we introduce the concept of VXB (Virtual Crossbar) as the computational unit rather than physical crossbars to facilitate the computing scheduling in the compiler."
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018) — _background_: "We sort out the designs of recent CIM accelerators from three dimensions: memory device, architecture hierarchy, and programming interface, and summarize them in Figure 1 [4, 6, 13, 18, 19, 21, 23, 28, 29, 33, 34, 39, 43, 46–51]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "Ambrosi et al. [2] propose a compilation tool that schedules matrix-vector computation (MVM) on a ReRAM-based architecture, but its performance degrades when the CIM architecture and computing granularity change."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _extends/builds-on_: "To accommodate different CIM designs for executing MVM on crossbars [4, 39, 42, 51], we introduce the concept of VXB (Virtual Crossbar) as the computational unit rather than physical crossbars to facilitate the computing scheduling in the compiler."
- [2019_Angizi_AnalogVsDigitalPIM_ISVLSI](2019_Angizi_AnalogVsDigitalPIM_ISVLSI.md) Analog vs Digital PIM (2019) — _background_: "For example, when comparing SRAM[26] and ReRAM, although both have similar latency for read operations, the cost of writing data is considerably higher in ReRAM [3]."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _contrasts/critiques_: "Relatively, OCC [40] is a comprehensive compilation that encompasses abundant device types as well as numerous programming interfaces."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "We sort out the designs of recent CIM accelerators from three dimensions: memory device, architecture hierarchy, and programming interface, and summarize them in Figure 1 [4, 6, 13, 18, 19, 21, 23, 28, 29, 33, 34, 39, 43, 46–51]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _baseline/comparison_: "Han et al. [22] design a compilation tool to deploy DNNs on the ISAAC architecture [39] via an MVM-grained programming interface, but its optimization strategy stays at the computing graph level neglecting the opportunity to fine-control the crossbar resource allocation and MVM operation sequencing for better results."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "Some works manually deployed the model on CIMs [39] with customized mapping and scheduling policies that are hard to generalize to other CIMs."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Thus, SRAM-based CIM supports flexible data read and write updates on CIM memory [6], while ReRAM-based CIM usually assumes that weights are frozen in the crossbar, avoiding the penalty of frequent writes [13, 39]."
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022) — _background_: "Other works propose to decompose DNN operators and schedule MVM-grained operation in CIM crossbars [4, 19, 36, 43, 49]."

## Cited by (in collection, 5)
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _baseline/comparison_: "Compared with state-of-the-art compilation works [33], CMSwitch achieves average inference speed improvement by 1.31x."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2024_Qu_CIMMLC_ASPLOS.pdf](../../05_Mapping_Compilation_and_Dataflow/2024_Qu_CIMMLC_ASPLOS.pdf)
- Full text: [../fulltext/2024_Qu_CIMMLC_ASPLOS.txt](../fulltext/2024_Qu_CIMMLC_ASPLOS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3620665.3640359
