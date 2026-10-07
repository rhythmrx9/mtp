---
id: W4225637124
key: 2022_Zheng_PIMulatorNN_TCAD
title: "PIMulator-NN: An Event-Driven, Cross-Level Simulation Framework for Processing-In-Memory-Based Neural Network Accelerators"
short: "PIMulator-NN"
year: 2022
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022)"
authors: "Qilin Zheng, Xingchen Li, Yijin Guan, Zongwei Wang, Yimao Cai, Yiran Chen, Guangyu Sun, Ru Huang"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "dataflow-pipelining", "crossbar-architecture", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 8
citations_overall: 12
priority_score: 5.58
doi: "https://doi.org/10.1109/tcad.2022.3160947"
pdf: null
fulltext: null
---

# PIMulator-NN

**PIMulator-NN: An Event-Driven, Cross-Level Simulation Framework for Processing-In-Memory-Based Neural Network Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
PIMulator-NN is an event-driven, cross-level simulator for PIM-based neural network accelerators that couples architecture-level event simulation with circuit-level modeling of analog compute units, revealing that memory access and interconnect effects (often missed by performance-model-based estimators) substantially impact system-level latency and energy.

## Summary
Existing performance-model-based estimators for processing-in-memory (PIM) neural-network accelerators often cannot capture fine architectural details such as interconnect and memory-access behavior. PIMulator-NN addresses this with an event-driven simulation engine that models architecture-level timing/behavior while integrating a mainstream circuit-level simulation framework to accurately estimate the area, latency, and energy of analog computation units. The authors implement several representative PIM accelerator designs as templates within PIMulator-NN and run detailed simulations, finding that memory access and interconnects have considerable, sometimes counter-intuitive ('anti-common-sense') effects on system-level performance and energy that conventional performance-model estimators fail to capture. The framework's templates let users quickly assemble and explore their own PIM architecture design space (dataflow, interconnect topology, data parallelism, etc.).

## Contributions
- An event-driven, cross-level (architecture + circuit) simulation framework specifically for PIM-based neural-network accelerators
- Integration of a mainstream circuit-level simulator to accurately model area, latency, and energy of analog compute units within the architectural simulation
- Several implemented architecture templates reproducing representative PIM accelerator designs for quick design-space exploration
- Empirical demonstration that memory access and interconnect effects materially (and sometimes counter-intuitively) affect system-level performance/energy, beyond what conventional performance models capture

## Key claims (stable IDs)
- **2022_Zheng_PIMulatorNN_TCAD#C1** — Conventional performance-model-based estimations fail to capture the system-level impact of memory access and interconnects in PIM accelerators. — _support:_ PIMulator-NN simulations reveal 'anti-common-sense' results for memory access/interconnect impact on performance and energy not visible in performance-model estimates — _loc:_ Abstract (full text not available)
- **2022_Zheng_PIMulatorNN_TCAD#C2** — PIMulator-NN enables users to quickly build and explore PIM architecture design choices (dataflow, interconnect, data parallelism). — _support:_ Several architecture templates implemented and demonstrated for rapid PIM design-space exploration — _loc:_ Abstract (full text not available)

## Results
- Demonstrated on several implemented PIM accelerator designs, showing memory access and interconnects considerably affect system-level performance and energy, with some results contradicting intuitive/common-sense expectations (per abstract; no specific quantitative figures given)

## Limitations
- Analysis is abstract-only (full text not accessible from this machine) -- validation methodology (e.g., comparison against measured chips or other simulators such as NeuroSim/MNSIM), supported device models, and quantitative accuracy of the circuit-level integration are not verifiable here
- As a simulation-framework paper, its own claims are inherently about relative/architectural insights rather than absolute measured-hardware numbers

## Remarks
Part of the family of cross-level PIM simulation/benchmarking tools (alongside MNSIM, DNN+NeuroSim, RxNN) that this collection's category 08 depends on; its event-driven architecture-plus-circuit coupling is positioned to capture interconnect/memory-access effects that coarser performance-model-based estimators miss, which is an important methodological point for anyone using simulators to make hardware design or mapping decisions for crossbar/PIM accelerators. Without the full text, the specific validation evidence for its circuit-level accuracy claims could not be assessed here; cited later by ALPINE and MNSIM 2.0, suggesting continued relevance to the simulation/benchmarking sub-literature.

## Cites (in collection, 8)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 3)
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _contrasts/critiques_: "Zheng et al. also use the ONNX framework as the front end for their event-driven cross-level simulation of processing-in-memory accelerators, while also incorporating elements for simulating memory access and interconnects [24]."
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2022_Zheng_PIMulatorNN_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2022.3160947
