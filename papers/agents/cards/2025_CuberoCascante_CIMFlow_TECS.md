---
id: W4413633179
key: 2025_CuberoCascante_CIMFlow_TECS
title: "CIMFlow: Modelling Dataflow in Cross-Layer Compute-in-Memory Deep Learning Accelerators"
short: "CIMFlow"
year: 2025
venue: "TECS"
venue_full: "ACM Transactions on Embedded Computing Systems, Vol. 24, Issue 5s (2025)"
authors: "José Cubero-Cascante, Lenka Schneider, Rebecca Pelke, Arunkumar M. Vaidyanathan, Rainer Leupers, Jan Moritz Joseph"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM"]
models: ["CNN", "ResNet", "VGG", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["dataflow-pipelining", "scheduling", "tiling-partitioning", "simulator", "crossbar-architecture", "weight-mapping", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 0
priority_score: 4.5
doi: "https://doi.org/10.1145/3760780"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2025_CuberoCascante_CIMFlow_TECS.pdf"
fulltext: "../fulltext/2025_CuberoCascante_CIMFlow_TECS.txt"
---

# CIMFlow

**CIMFlow: Modelling Dataflow in Cross-Layer Compute-in-Memory Deep Learning Accelerators** — ACM Transactions on Embedded Computing Systems, Vol. 24, Issue 5s (2025) (2025)

## TL;DR
CIMFlow is a timed cyclo-static dataflow simulator for fully-weight-stationary multi-core CIM accelerators that shows cross-layer pipelined inference with weight duplication raises throughput up to 52x and that ignoring data-movement delays overestimates throughput by up to 308%.

## Summary
Multi-core CIM accelerators hold all weights on-chip (fully weight-stationary) and can run cross-layer inference, but no tool modelled data orchestration and memory timing for them. CIMFlow has three models: a Hardware Architecture Model of CIM cores (PEs of 512x512 arrays with 800 ns MVM latency, 16 PEs per core), digital SIMD/pool cores and buffets (token-based flow-controlled buffers) with per-level memory times from CACTI; an Array-OL Workload Model of CNN layers that supports hardware-aware transforms such as splitting kernel weight tensors to fit crossbar dimensions and slicing tensors for cross-layer execution; and an Execution Model that compiles both into a timed cyclo-static dataflow (TCSDF) graph that is simulated for latency, energy and core/buffer utilisation traces. Weight duplication uses the greedy CLSA-CIM algorithm (duplicate the slowest layer while PEs remain). Validation against CLSA-CIM on five workloads gives MAPE 0.77% (serial) and 3.07% (cross-layer). Case studies on AlexNet, VGG16/19, ResNet18/50/101, MobileNetv2/v3, TinyYOLOv3 sweep extra PEs (0-64) and buffer allocation (no_dm, buff_min, buff_max). Devices are abstracted, there is no analog non-ideality model.

## Contributions
- Array-OL based workload model with hardware-aware weight-splitting and tensor-slicing transformations
- TCSDF-based execution model for cross-layer inference in multi-core CIM with buffets for distributed flow control
- First tool modelling FWS cross-layer execution with explicit data-movement costs
- Case studies on weight duplication and a simple selective buffer-allocation strategy

## Key claims (stable IDs)
- **2025_CuberoCascante_CIMFlow_TECS#C1** — Cross-layer execution with weight duplication gives large throughput gains — _support:_ up to 52x (TinyYOLOv3, buff_max) — _loc:_ Sec. 8.3 / Fig. 12
- **2025_CuberoCascante_CIMFlow_TECS#C2** — Neglecting memory/data-transfer delay overestimates throughput gain from weight duplication — _support:_ up to 308% overestimation — _loc:_ Sec. 8.3 / Fig. 12
- **2025_CuberoCascante_CIMFlow_TECS#C3** — CIMFlow reproduces CLSA-CIM latency — _support:_ MAPE 0.77% serial, 3.07% cross-layer — _loc:_ Sec. 8.1 / Fig. 11
- **2025_CuberoCascante_CIMFlow_TECS#C4** — For residual networks buffer allocation matters more than weight duplication; small buffer increases give large throughput increases — _support:_ MobileNetv2: +7.54% buffer gives +120.1% throughput — _loc:_ Sec. 8.4 / Table 4

## Results
- Up to 52x throughput gain from cross-layer inference plus duplication (TinyYOLOv3)
- Up to 308% throughput overestimate when data movement is ignored
- Validation MAPE 0.77% / 3.07% vs CLSA-CIM
- MobileNetv2: +7.54% inter-layer buffer memory yields +120.1% throughput (Table 4)
- VGG16/19 show small buff_min vs buff_max delta; ResNet/MobileNet show large delta (Sec. 8.3)

## Key numbers
- tech_node: 32 nm (digital modules)
- array_size: 512x512 PE
- throughput: MVM latency 800 ns/PE; up to 52x gain
- accuracy: MAPE 0.77%/3.07% vs CLSA-CIM

## Datasets / benchmarks
AlexNet, VGG16, VGG19, ResNet18, ResNet50, ResNet101, MobileNetv2, MobileNetv3, TinyYOLOv3

## Limitations
- CNN workloads only; no transformer/attention (dynamic activation-activation products) or LLM support
- Device-agnostic: no analog noise, ADC or accuracy modelling, MVM latency taken from RAELLA
- Single-tile reference platform; interconnect topologies left for future work
- Energy modelling less developed than latency/throughput

## Remarks
A useful system-level cost model that complements macro-level tools (CiMLoop, NeuroSim) by capturing inter-core buffering and pipeline stalls, which are exactly the costs that matter when mapping deep, branchy models onto many crossbar cores. Because it handles only static CNN dataflow, it would need extension for KV-cache/attention traffic before being applied to small language models. Evidence is simulation-only but validated against CLSA-CIM.

## Cites (in collection, 8)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "PUMA [4] proposes an architecture based on a hierarchical interconnect, where shared memory buffers are present in each tile."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _background_: "Accelergy is basically a wrapper, providing a single interface to established energy estimation tools, including CACTI [23] and NeuroSim [30]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "ISAAC [31] presents multi-core CIM architectures and demonstrates the importance of cross-layer inference, which the authors refer to as pipelining."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Demonstrator chips achieving low power massively parallel matrixvector multiplication (MVM) operations have been built using arrays of Resistive Random Access Memory (RRAM) [34] and Phase Change Memory (PCM) [20]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _background_: "Previous CIM-based accelerator proposals have recognised the importance of cross-layer inference [4, 15, 31]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _background_: "RAELLA [2] is a more recent architecture proposal that also leverages a hierarchical interconnect."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Demonstrator chips achieving low power massively parallel matrixvector multiplication (MVM) operations have been built using arrays of Resistive Random Access Memory (RRAM) [34] and Phase Change Memory (PCM) [20]."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _contrasts/critiques_: "The latest version of the Timeloop/Accelergy framework, called CiMLoop [3], extends the capabilities of the original framework to support CIM accelerators."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2025_CuberoCascante_CIMFlow_TECS.pdf](../../05_Mapping_Compilation_and_Dataflow/2025_CuberoCascante_CIMFlow_TECS.pdf)
- Full text: [../fulltext/2025_CuberoCascante_CIMFlow_TECS.txt](../fulltext/2025_CuberoCascante_CIMFlow_TECS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3760780
