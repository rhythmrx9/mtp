---
id: W3204737618
key: 2021_Han_PolyhedralPIMCompiler_JETC
title: "Polyhedral-Based Compilation Framework for In-Memory Neural Network Accelerators"
short: "Polyhedral PIM Compiler"
year: 2021
venue: "JETC"
venue_full: "ACM Journal on Emerging Technologies in Computing Systems"
authors: "Jianhui Han, Xiang Fei, Zhaolin Li, Youhui Zhang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Memristor(generic)", "ReRAM"]
models: ["MLP", "CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["compiler-software-stack", "weight-mapping", "tiling-partitioning", "dataflow-pipelining", "scheduling", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 11
citations_overall: 10
priority_score: 7.06
doi: "https://doi.org/10.1145/3469847"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2021_Han_PolyhedralPIMCompiler_JETC.pdf"
fulltext: "../fulltext/2021_Han_PolyhedralPIMCompiler_JETC.txt"
---

# Polyhedral PIM Compiler

**Polyhedral-Based Compilation Framework for In-Memory Neural Network Accelerators** — ACM Journal on Emerging Technologies in Computing Systems (2021)

## TL;DR
A polyhedral (isl/pet) source-to-source compiler that detects MV/MM/CONV and fused operators in C code, maps them to memristor-crossbar accelerators and generates pipelined code, giving up to 27.1x speedup (ResNet-50) over the same hardware without pipelining.

## Summary
Prior polyhedral PIM compilers (TC-CIM, TDO-CIM) only detect MM/MV, offload operator-by-operator and do not pipeline. This paper builds a source-to-source framework on isl and pet that runs several schedule-tree matching passes (fused MM/CONV+activation first, then bare MM/CONV/MV), inserts mark nodes, then rebuilds the AST from a whole-network perspective. CONV is reshaped (im2col-style, with data-layout transformation) to fit crossbars, and operators are tiled to crossbar size constraints. A resource-allocation algorithm (Algorithm 1) distributes available PEs across layers and replicates weights in bottleneck layers, then pipelined code over the batch and layer dimensions is generated. Code can be emitted at fine granularity (MM-with-activation API calls, ISAAC case) or coarse granularity (FPSA case, handed to its native toolchain). Evaluation uses synthetic kernels plus MLP-M, MLP-L, VGG-16 and ResNet-50, with ISAAC and FPSA performance models; correctness is checked with a behavioural model of the API. The focus is the compiler layer; no device non-idealities are modelled.

## Contributions
- Source-to-source NN compiler detecting and mapping MV, MM, CONV and MM/CONV-centric fused operators onto memristor accelerators
- PE resource allocation across operators and pipelined code generation exploiting batch and layer dimensions
- Selectable invocation granularity (fine-grained vs coarse-grained API calls) to integrate with native toolchains
- Case studies on ISAAC and FPSA showing generality and an order-of-magnitude gain from pipelining

## Key claims (stable IDs)
- **2021_Han_PolyhedralPIMCompiler_JETC#C1** — The framework detects all target operators in synthetic kernels, including cases TC-CIM misses — _support:_ All operators matched; TC-CIM missed the final MM in mlp-3-like kernel lacking an init statement — _loc:_ Sec. 4.2 / Table 2
- **2021_Han_PolyhedralPIMCompiler_JETC#C2** — Pipelined execution yields large speedups over non-pipelined execution on the same PEs — _support:_ VGG-16: 1.8-2.6x (batch 4), 4.4-6.3x (batch 16), 7.0-9.9x (batch 64); ResNet-50 2.6x to 27.1x — _loc:_ Sec. 4.4.5 / Fig. 11
- **2021_Han_PolyhedralPIMCompiler_JETC#C3** — Compiler-generated mapping reproduces hand-mapped ISAAC trends — _support:_ Synthetic layer reaches 352 GOPs/s/mm2 vs 479 reported for ISAAC (483 if only busy cycles counted) — _loc:_ Sec. 4.4.4 / Fig. 9

## Results
- Pipelining speedup on ISAAC model: 1.8-9.9x for VGG-16 and 2.6-27.1x for ResNet-50 depending on batch size 4-64 (Fig. 11)
- Optimized PE allocation (Algorithm 1) beats even allocation across layers under pipelined execution (Fig. 12)
- 352 GOPs/s/mm2 computation density vs 479 GOPs/s/mm2 reported by ISAAC for a perfectly matched layer (Sec. 4.4.4)
- Generated code verified correct against original code for all synthetic kernels and NN benchmarks (Sec. 4.3)

## Key numbers
- throughput: 352 GOPs/s/mm2 (ISAAC model, synthetic layer)
- bits_weight: 16b weights as 8 x 2b cells (ISAAC)

## Datasets / benchmarks
MLP-M, MLP-L, VGG-16, ResNet-50, synthetic kernels

## Limitations
- Inference only; training accelerators (PipeLayer, PANTHER) with different update strategies left as future work
- Evaluation via architecture performance models of ISAAC/FPSA, no real hardware or device non-idealities
- Targets host-controlled API accelerators; ISA-programmable designs (PUMA) are out of scope
- Benchmarks limited to MLPs, VGG-16, ResNet-50; no transformers or language models

## Remarks
Solid, clearly scoped compiler-layer work; the pipeline-speedup headline is relative to a deliberately non-pipelined baseline, so it quantifies necessity rather than absolute efficiency. It handles only static, regular loop nests, which suits CNN/MLP but not attention with dynamic operands that must be written into crossbars. Complements PUMA/ISAAC/PipeLayer (hardware) and later compilers like PIMCOMP and CIM-MLC in the collection.

## Cites (in collection, 11)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Another example, Pipelayer [35] computes partial derivatives with memristor crossbars and updates weights by reading them out, merging them with partial derivatives, and writing updated weights back."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _background_: "In addition, integrating multiple crossbars with different sizes instead of monolithic design has also been investigated [47]."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _background_: "Such reshaping strategies have been well investigated [13, 33, 35] and should be implemented in the compilation framework."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "For example, PUMA [5] has a lower area and energy efficiency than ISAAC [33], due to the overhead to achieve better programmability."
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019) — _contrasts/critiques_: "There are also some end-to-end frameworks for memristor-based architectures [27, 45]."
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019) — _background_: "Some memristor-based accelerators provide co-located MM and activation units [12, 33] to reduce the amount of data movement, and others directly implement fused operators to benefit from the efficient peripheral circuit design [18, 24]."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "Another accelerator design, Panther [4], updates weights with outer product accumulate operations, where input voltages are fed to memristor crossbars' bitlines and wordlines simultaneously."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "We conduct experiments with two memristor-based architectures, ISAAC [33] and FPSA [24], to evaluate the different invocation granularity of the compilation framework."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "A commonly adopted programming paradigm [12, 35] provides application programming interface (API) functions to improve the programmability of such architectures."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "important in NN processing, some studies propose to use memristor-based architectures to accelerate NN training [4, 11, 35]."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019)

## Cited by (in collection, 5)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _baseline/comparison_: "Han et al. [22] design a compilation tool to deploy DNNs on the ISAAC architecture [39] via an MVM-grained programming interface, but its optimization strategy stays at the computing graph level neglecting the opportunity to fine-control the crossbar resource allocation and MVM operation sequencing for better results."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _baseline/comparison_: "TC-CIM [19], TDO-CIM [20], CINM [23], OCC [21], Polyhedral [16], Co-Design [17], and PUMA [22] do not consider the interaction between weight replication and weight layout, and simply map computational tasks to PIM arrays."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2021_Han_PolyhedralPIMCompiler_JETC.pdf](../../05_Mapping_Compilation_and_Dataflow/2021_Han_PolyhedralPIMCompiler_JETC.pdf)
- Full text: [../fulltext/2021_Han_PolyhedralPIMCompiler_JETC.txt](../fulltext/2021_Han_PolyhedralPIMCompiler_JETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3469847
