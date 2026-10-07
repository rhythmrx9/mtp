---
id: W2925767305
key: 2019_Liu_XB-Sim_CAL
title: "A Unified Framework for Training, Mapping and Simulation of ReRAM-Based Convolutional Neural Network Acceleration"
short: "XB-Sim"
year: 2019
venue: "CAL"
venue_full: "IEEE Computer Architecture Letters (2019)"
authors: "He Liu, Jianhui Han, Youhui Zhang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["simulator", "compiler-software-stack", "weight-mapping", "hardware-aware-training", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 6
citations_overall: 8
priority_score: 5.97
doi: "https://doi.org/10.1109/lca.2019.2908374"
pdf: null
fulltext: null
---

# XB-Sim

**A Unified Framework for Training, Mapping and Simulation of ReRAM-Based Convolutional Neural Network Acceleration** — IEEE Computer Architecture Letters (2019) (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Presents XB-Sim, a unified open-source framework combining ReRAM-aware NN training, a CNN-oriented mapper, and a micro-architecture simulator for end-to-end evaluation of ReRAM-based neural network accelerators (RNAs), with core components verified against circuit simulation of a real chip design.

## Summary
The paper notes that despite growing interest in ReRAM-based neural network accelerators (RNAs), there was no open, end-to-end software tool spanning training, mapping, and architectural simulation for broad design-space exploration. It presents a unified simulation framework (released as XB-Sim) consisting of three coupled components: a ReRAM-aware training algorithm that accounts for crossbar/device characteristics during NN training, a CNN-oriented mapper that places trained weights onto crossbar arrays, and a configurable micro-architecture simulator that models ReRAM and peripheral circuit behavior. The framework's core components are validated against circuit simulation of a real chip design, giving it a degree of fidelity beyond purely architectural models. The tool targets comprehensive architectural exploration and end-to-end (training-to-hardware) evaluation of CNN inference on ReRAM accelerators, and a preliminary version was released publicly on GitHub.

## Contributions
- A unified, open-source (preliminary) simulation framework spanning ReRAM-aware training, CNN mapping, and micro-architecture simulation in one pipeline
- A customized ReRAM-aware training algorithm that incorporates device/circuit characteristics
- A CNN-oriented mapper for placing trained weights onto ReRAM crossbar arrays
- Validation of the simulator's core components against circuit-level simulation of a real chip design

## Key claims (stable IDs)
- **2019_Liu_XB-Sim_CAL#C1** — The simulator's core components accurately reflect real hardware behavior — _support:_ function of core components verified by corresponding circuit simulation of a real chip design — _loc:_ abstract
- **2019_Liu_XB-Sim_CAL#C2** — The framework enables comprehensive, end-to-end architectural exploration of ReRAM-based NN accelerators — _support:_ combines ReRAM-aware training tool, CNN-oriented mapper, and micro-architecture simulator in one framework — _loc:_ abstract

## Results
- Preliminary framework released publicly (github.com/CRAFT-THU/XB-Sim)
- Core simulator components cross-checked against circuit simulation of a real chip design (no further quantitative figures available from abstract)

## Limitations
- Only abstract was accessible; specific benchmark networks, accuracy/throughput/energy numbers, and crossbar configurations evaluated are not verifiable here
- Described as a 'preliminary version', suggesting the released tool and evaluation may be limited in scope at time of publication
- As a short Computer Architecture Letters paper, depth of validation and breadth of benchmarks is likely limited relative to a full conference paper

## Remarks
This is a tool/infrastructure paper rather than a novel accelerator or algorithm, aiming to fill a gap for an open, end-to-end (training-mapping-architecture) ReRAM accelerator simulator, which is valuable for reproducibility in this subfield. It is itself cited by later mapping/compilation and simulator papers in this collection (e.g. ERA-LSTM, a polyhedral-based compilation framework, and IBM's analog hardware acceleration kit paper), suggesting some adoption. Since only the abstract could be reviewed here, the claim of chip-level validation (an important differentiator from purely behavioral simulators like MNSIM) could not be independently assessed for rigor.

## Cites (in collection, 6)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 3)
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _contrasts/critiques_: "There are also some end-to-end frameworks for memristor-based architectures [27, 45]."
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2019_Liu_XB-Sim_CAL.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/lca.2019.2908374
