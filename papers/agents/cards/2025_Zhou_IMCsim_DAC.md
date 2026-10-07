---
id: W4414198111
key: 2025_Zhou_IMCsim_DAC
title: "A Full-system, Programmable, and Extensible In-Memory Computing Simulation Framework for Deep Learning"
short: "IMCsim"
year: 2025
venue: "DAC"
venue_full: "ACM/IEEE Design Automation Conference (DAC 2025)"
authors: "Kaining Zhou, Jian Huang, Nam Sung Kim, Naresh R. Shanbhag"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["MRAM", "SRAM-analog", "Generic-NVM"]
models: ["ResNet", "GPT/LLM", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "compiler-software-stack", "dataflow-pipelining", "transformer-accelerator", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 0
priority_score: 3.5
doi: "https://doi.org/10.1109/dac63849.2025.11132463"
pdf: null
fulltext: null
---

# IMCsim

**A Full-system, Programmable, and Extensible In-Memory Computing Simulation Framework for Deep Learning** — ACM/IEEE Design Automation Conference (DAC 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IMCsim is a full-system in-memory-computing simulator with software runtime libraries, ISA extensions for tensor operators, and flexible mapping across eNVM/SRAM/digital IMC architectures, validated against measured 22nm MRAM and 28nm SRAM IMC prototype chips and used to explore ResNet-18/Llama/DiT design trade-offs and derive an efficient 28nm DiT chip layout.

## Summary
The paper addresses a gap in IMC tooling: designing programmable IMC platforms for today's large generative models (LLMs, diffusion transformers) requires a simulator that is simultaneously scalable and faithful to device/circuit-level IMC behavior, which existing tools reportedly lack. IMCsim is presented as a versatile full-system IMC simulation framework that integrates software runtime libraries for AI models, introduces a new set of ISA extensions to express common tensor operators, and flexibly maps these operators onto different IMC architectures, letting designers explore performance/energy/area/accuracy trade-offs across IMC design choices. The authors instantiate three IMC types in IMCsim -- embedded non-volatile memory (eNVM)-based, SRAM-based, and digital IMC -- and validate the simulator against measured data from two lab-tested prototype ICs (a 22nm MRAM-based IMC and a 28nm SRAM-based IMC) plus a digital IMC design in 28nm. They then use IMCsim to explore the architectural design space across ResNet-18, Llama, and a diffusion transformer (DiT) workload for the three IMC types, and finally use it as a design tool to derive an efficient chip architecture and layout in 28nm for a lightweight DiT.

## Contributions
- Presents IMCsim, a full-system IMC simulation framework combining scalability with device/circuit-level fidelity, addressing a gap for simulating large generative-AI workloads (LLMs, DiTs) on IMC hardware
- Introduces software runtime libraries for AI models plus new ISA extensions to express common tensor operators on IMC hardware
- Supports flexible mapping of tensor operators across multiple IMC architecture types (eNVM-based, SRAM-based, digital)
- Validates IMCsim against measured data from two lab-tested prototype ICs (22nm MRAM-based IMC, 28nm SRAM-based IMC) and a 28nm digital IMC design
- Uses IMCsim to explore architectural trade-offs for ResNet-18, Llama, and a DiT workload across the three IMC types, and to derive an efficient 28nm chip architecture/layout for a lightweight DiT

## Key claims (stable IDs)
- **2025_Zhou_IMCsim_DAC#C1** — IMCsim's simulation results are validated against real silicon across two different IMC device technologies — _support:_ Validated using measured data from two lab-tested prototype ICs: a 22nm MRAM-based IMC and a 28nm SRAM-based IMC, plus a digital IMC design in 28nm — _loc:_ Abstract
- **2025_Zhou_IMCsim_DAC#C2** — IMCsim can be used as a practical design tool to derive an efficient real chip architecture/layout for modern generative workloads — _support:_ Used to obtain an efficient chip architecture and layout in 28nm for a lightweight diffusion transformer (DiT) — _loc:_ Abstract

## Limitations
- Abstract does not report specific quantitative validation error margins (e.g. % error vs. measured silicon) for the simulator's predictions
- Only three IMC device/architecture types are modeled (eNVM, SRAM, digital); other analog device classes (PCM, ReRAM crossbars with analog MAC) are not mentioned as validated in the abstract
- Full text not available to this analysis; scope of the ISA extensions and runtime library coverage cannot be independently verified

## Remarks
A full-system simulator paper with a notably strong validation story (grounded in two measured prototype ICs rather than only literature-reported numbers), which is valuable for anyone needing to trust IMC-level performance/energy/accuracy predictions for LLM/DiT-scale workloads rather than just CNN-scale ones. Without the full text, the degree of validation accuracy and the breadth of the ISA-extension abstraction (how well it generalizes to analog crossbar-style MAC, as opposed to the eNVM/SRAM/digital IMC variants it demonstrates) remain open questions for this thesis's purposes.

## Cites (in collection, 7)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2025_Zhou_IMCsim_DAC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/dac63849.2025.11132463
