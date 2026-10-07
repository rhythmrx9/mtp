---
id: W4409285506
key: 2024_Ahsan_SPICEenvmACIMFramework_ICCAD
title: "Accurate, Yet Scalable: A SPICE-based Design and Optimization Framework for eNVM based Analog In-memory Computing"
short: "SPICE eNVM ACIM Framework"
year: 2024
venue: "ICCAD"
venue_full: "Proceedings of the 43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024)"
authors: "S M Mojahidul Ahsan, Muhammad Sakib Shahriar, Mrittika Chowdhury, Tanvir Hossain, Md Sakib Hasan, Tamzidul Hoque"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Generic-NVM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "ir-drop-parasitics", "analog-mvm", "peripheral-circuits"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 2
priority_score: 3.83
doi: "https://doi.org/10.1145/3676536.3676827"
pdf: null
fulltext: null
---

# SPICE eNVM ACIM Framework

**Accurate, Yet Scalable: A SPICE-based Design and Optimization Framework for eNVM based Analog In-memory Computing** — Proceedings of the 43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024) (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A scalable SPICE-based simulation framework automates SPICE-level netlist generation for eNVM analog compute-in-memory (ACIM) DNN accelerators, speeding up simulation by up to 35x and enabling convergent SPICE simulation of large crossbars (e.g., an 800,000-parameter MLP on MNIST) that contemporary SPICE simulators cannot handle, with under 3.8% accuracy drop versus software inference.

## Summary
Simulating analog compute-in-memory (ACIM) architectures built from emerging non-volatile resistive memories (eNVM) accurately requires circuit-level (SPICE) simulation because these crossbars are highly sensitive to process, voltage, temperature variation and analog noise, but standard SPICE simulators do not scale to the large netlists needed for realistic DNNs and often fail to converge. The paper introduces a scalable SPICE-based tool infrastructure that automates generation of SPICE-level ACIM circuit descriptions for DNNs, and speeds up simulation runtime by up to 35x for large models while preserving SPICE-level accuracy, also improving convergence for large netlists. The framework is validated by simulating inference of MLPs with over 800,000 parameters trained on MNIST, a scale that the authors state is impractical for contemporary SPICE simulators, and the simulated inference accuracy is shown to be within 3.8% of software-based inference. The framework is also integrated with an architectural simulator to enable combined circuit-to-system-level simulation.

## Contributions
- Proposes a scalable SPICE-based simulation framework specifically for eNVM-based analog compute-in-memory (ACIM) architectures
- Automates generation of SPICE-level ACIM circuit netlists directly from DNN model descriptions
- Achieves up to 35x simulation speedup for large DNN models while retaining SPICE-level circuit accuracy
- Solves convergence failures that prevent contemporary SPICE simulators from handling large eNVM crossbar netlists
- Integrates the circuit-level simulator with an architectural simulator for combined system-level evaluation

## Key claims (stable IDs)
- **2024_Ahsan_SPICEenvmACIMFramework_ICCAD#C1** — The framework substantially accelerates SPICE-accurate simulation of large ACIM designs — _support:_ Simulation runtime speedup of up to 35x for large DNN models while maintaining the same SPICE-level accuracy — _loc:_ Abstract
- **2024_Ahsan_SPICEenvmACIMFramework_ICCAD#C2** — The framework enables SPICE simulation of eNVM crossbar DNNs at scales infeasible for standard SPICE tools — _support:_ Simulates inference using netlists for MLPs with over 800,000 parameters trained on MNIST within acceptable runtime, where contemporary SPICE simulators do not converge — _loc:_ Abstract
- **2024_Ahsan_SPICEenvmACIMFramework_ICCAD#C3** — Simulated (circuit-level) inference accuracy closely matches software inference despite analog non-idealities — _support:_ Less than 3.8% accuracy drop compared to software-based inference results — _loc:_ Abstract

## Results
- Up to 35x simulation runtime speedup for large DNN models at SPICE-level accuracy
- Successfully simulates an MLP with >800,000 parameters on MNIST, where contemporary SPICE simulators fail to converge
- Less than 3.8% inference accuracy drop versus software-based inference

## Limitations
- Analysis is based on the abstract only; full text was not accessible (not found via arXiv or other legitimate open-access sources), so the specific SPICE automation techniques, device models, and benchmark details beyond the MNIST MLP could not be verified
- Demonstrated scale (MLP, MNIST, ~800K parameters) is still modest relative to modern CNN/transformer workloads

## Remarks
This is a simulation/EDA-tooling contribution addressing a real bottleneck in the field: circuit-accurate (SPICE) evaluation of eNVM crossbars is the gold standard for capturing non-idealities but does not scale, forcing most mapping/architecture papers in this collection to rely on faster but less accurate behavioral models (e.g., NeuroSim-style). A 35x speedup with SPICE-level fidelity and architectural-simulator integration, if it generalizes beyond the MNIST MLP case demonstrated in the abstract, would be a useful bridge between device-accurate and system-level crossbar simulation frameworks elsewhere in this collection.

## Cites (in collection, 6)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2024_Ahsan_SPICEenvmACIMFramework_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1145/3676536.3676827
