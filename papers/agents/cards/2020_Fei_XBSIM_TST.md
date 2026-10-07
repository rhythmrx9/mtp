---
id: W3107562138
key: 2020_Fei_XBSIM_TST
title: "XB-SIM∗: A simulation framework for modeling and exploration of ReRAM-based CNN acceleration design"
short: "XB-SIM*"
year: 2020
venue: "TST"
venue_full: "Tsinghua Science and Technology, 2020"
authors: "Xiang Fei, Youhui Zhang, Weimin Zheng"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "crossbar-architecture", "hardware-aware-training", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 4
citations_overall: 13
priority_score: 5.39
doi: "https://doi.org/10.26599/tst.2019.9010070"
pdf: null
fulltext: null
---

# XB-SIM*

**XB-SIM∗: A simulation framework for modeling and exploration of ReRAM-based CNN acceleration design** — Tsinghua Science and Technology, 2020 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
XB-SIM* is a configurable architecture-level simulation framework for ReRAM-crossbar CNN accelerators, bundling a ReRAM-aware training algorithm and a CNN-oriented mapper, validated against circuit-level simulation of a real chip, and sped up 5.02x-34.29x via a batch-processing mode on CPU/GPGPU.

## Summary
Designing ReRAM-crossbar CNN accelerators requires accounting for device imperfections while also running very large amounts of calculation to accurately simulate crossbar behavior, which is itself a major design challenge. XB-SIM* is presented as a flexible, configurable simulation framework that models an accelerator's structure and clock-driven behavior at the architecture level, bundled with a ReRAM-aware neural-network training algorithm and a CNN-oriented mapper so a network can be trained and efficiently mapped onto the simulated design. The simulator's behavior is validated against circuit-level simulation of an actual chip. To address the massive computation needed to mimic ReRAM-crossbar circuit behavior, the authors propose a batch-processing mode that exploits the mapping strategy's computational concurrency, reporting substantial simulation speedups on CPU and GPGPU platforms, and use the framework for architectural exploration and end-to-end evaluation.

## Contributions
- XB-SIM*: a configurable, architecture-level simulation framework for ReRAM-crossbar CNN accelerators modeling structure and clock-driven behavior
- An integrated ReRAM-aware NN training algorithm and CNN-oriented mapper for training and mapping networks onto the simulated design
- Validation of simulator behavior against circuit-level simulation of a real chip
- A batch-processing mode exploiting mapping-strategy concurrency to accelerate the massive calculations required for crossbar-circuit-accurate simulation
- Architectural exploration and end-to-end evaluation enabled by the framework

## Key claims (stable IDs)
- **2020_Fei_XBSIM_TST#C1** — The simulator's modeled behavior matches circuit-level simulation of a real chip — _support:_ Stated: 'Behavior of the simulator has been verified by the corresponding circuit simulation of a real chip' (abstract) — _loc:_ Abstract
- **2020_Fei_XBSIM_TST#C2** — The proposed batch-processing mode substantially speeds up the massive calculations required to simulate ReRAM-crossbar circuit behavior — _support:_ Up to 5.02x (CPU) or 34.29x (GPGPU) simulation speedup (abstract) — _loc:_ Abstract

## Results
- Simulation speedup of up to 5.02x on CPU and 34.29x on GPGPU via batch processing (per abstract)

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Xplore is not downloadable here); specific accuracy of the architecture-level model versus circuit simulation, supported device/non-ideality models, and benchmark networks could not be verified
- As a simulation/framework paper, its contribution is tooling rather than a new accelerator architecture or training algorithm per se, so its value depends on adoption/validation by other works

## Remarks
Based on the abstract, XB-SIM* belongs to the family of architecture-level ReRAM-crossbar CNN accelerator simulators (alongside tools like MNSIM and DNN+NeuroSim cited elsewhere in this collection), distinguished by its emphasis on simulation throughput (via batch processing) and validation against real-chip circuit simulation. Without full-text access, the fidelity of its device/non-ideality models and the breadth of architectural exploration it enables cannot be assessed beyond the abstract's claims; readers building or selecting a simulation framework for crossbar-based CNN accelerator design should compare it directly against MNSIM and NeuroSim-family tools in the full papers.

## Cites (in collection, 4)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 4)
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "They also provide a simplified estimation of power, area, and latency [141, 142]."
- [2023_Cao_RRAMPoolFormer_ISCAS](2023_Cao_RRAMPoolFormer_ISCAS.md) RRAM-PoolFormer (2023) — _baseline/comparison_: "The results of this study are summarized and compared to other recent memristor crossbar DNN solutions in Table I (including XB-SIM [27])."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Other architectural-level simulators proposed in the literature and following a very similar approach include CIM-SIM and XB-SIM."
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2020_Fei_XBSIM_TST.pdf`)
- Full text: none
- DOI: https://doi.org/10.26599/tst.2019.9010070
