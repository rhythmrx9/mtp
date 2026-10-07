---
id: W4400681289
key: 2024_Andrulis_CiMLoop_ISPASS
title: "CiMLoop: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool"
short: "CiMLoop"
year: 2024
venue: "ISPASS"
venue_full: "IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS 2024)"
authors: "Tanner Andrulis, Joel Emer, Vivienne Sze"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-analog", "ReRAM", "Generic-NVM"]
models: ["CNN", "ResNet", "ViT", "MobileNet", "GPT/LLM"]
lm_models: ["GPT-2"]
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["simulator", "benchmarking", "macro", "adc-dac", "dataflow-pipelining", "energy-efficiency", "crossbar-architecture", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 22
citations_overall: 30
priority_score: 7.07
doi: "https://doi.org/10.1109/ispass61541.2024.00012"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2024_Andrulis_CiMLoop_ISPASS.pdf"
fulltext: "../fulltext/2024_Andrulis_CiMLoop_ISPASS.txt"
---

# CiMLoop

**CiMLoop: A Flexible, Accurate, and Fast Compute-In-Memory Modeling Tool** — IEEE International Symposium on Performance Analysis of Systems and Software (ISPASS 2024) (2024)

## TL;DR
CiMLoop is an open-source full-stack CiM modeling tool (YAML container-hierarchy spec plus statistical data-value-dependent energy model) with 3% average / 7% max error vs NeuroSim on ResNet18 and orders-of-magnitude faster simulation.

## Summary
Existing CiM tools either target one layer of the stack or one fixed design (NeuroSim, MNSIM, Timeloop). CiMLoop addresses three challenges: flexibility, accuracy and speed. Users describe a system as a container hierarchy in YAML (circuits as components, architecture as containers, workloads as Timeloop-style einsums), with a plug-in library of components (including a NeuroSim plug-in) and encodings/slicing functions (offset, differential, XNOR, magnitude-only). Energy is data-value-dependent: DNN operand distributions per layer, hardware representation, and analog/digital circuit behaviour are combined in a statistical model that is amortized across many mappings. Validation: against NeuroSim on ResNet18/ImageNet and against four published macros (A-D, SRAM and ReRAM based) for voltage, input bits, energy and area breakdowns. Case studies explore output reuse, analog adders, array size, full-system weight-stationary execution (incl. GPT-2 and ResNet18), and cross-macro scaling to 7nm.

## Language models evaluated
- Models: GPT-2
- Scale: —

## Contributions
- Flexible specification describing circuits, architecture, workload and mapping in one input without changing simulator code
- Accurate data-value-dependent energy model capturing operand distributions, representation and circuit value dependence
- Fast statistical model giving orders-of-magnitude higher speed than NeuroSim and enabling mapping exploration
- Validation on four published macros plus case studies at mapping, circuit, architecture, full-system and cross-macro levels

## Key claims (stable IDs)
- **2024_Andrulis_CiMLoop_ISPASS#C1** — Data-value-dependent model has 3% average and 7% max full-macro energy error vs NeuroSim across ResNet18 layers, while a fixed-energy model has 28%/70% — _support:_ 3%/7% vs 28%/70% — _loc:_ Sec. IV-A / Fig. 6
- **2024_Andrulis_CiMLoop_ISPASS#C2** — CiMLoop is several orders of magnitude faster than NeuroSim — _support:_ Table II (mappings x layers)/s: 0.07 NeuroSim, 0.28 CiMLoop 1 core, 2.25 CiMLoop 16 cores at 1 mapping; 83 and 1076 at 5000 mappings (as extracted) — _loc:_ Sec. IV-B / Table II
- **2024_Andrulis_CiMLoop_ISPASS#C3** — Validation vs published macros: supply sweeps energy-eff/throughput errors 7%/2%; input-bit sweeps 6%/5%; discrete-component energy error 4%; area error 8% — _support:_ stated averages — _loc:_ Sec. V-B / Figs. 7-10
- **2024_Andrulis_CiMLoop_ISPASS#C4** — Data-value effects can change macro energy by up to 2.3x — _support:_ Macro B data-value sweep — _loc:_ Fig. 11
- **2024_Andrulis_CiMLoop_ISPASS#C5** — Larger arrays lower energy by amortizing ADC and output-sum energy for large-tensor workloads, but small-tensor workloads (MobileNetV3) favour smaller arrays — _support:_ array 64-1024 sweep — _loc:_ Fig. 14

## Results
- Fixed-energy model 28% avg / 70% max error vs CiMLoop 3% / 7% (Fig. 6)
- Speed-up over NeuroSim of several orders of magnitude (Table II; Xeon Gold 6444Y, 1-16 cores)
- Weight-stationary CiM saves significant energy for GPT-2 and ResNet18, but off-chip input/output movement between layers limits benefits; layer fusion needed (Fig. 15)
- Analog adders: more operands raise throughput/area but underutilize with fewer bits/weight; 8-operand never best (Fig. 13)
- Output reuse across columns lowers ADC energy but raises DAC energy; 3-column reuse best for variable-utilization workload (Fig. 12)

## Key numbers
- tech_node: 7nm (cross-macro scaling); macros at original nodes
- array_size: 64-1024 rows/cols swept
- accuracy: 3% avg / 7% max energy error vs NeuroSim (ResNet18)
- bits_adc: 8b ADC in cross-macro study

## Datasets / benchmarks
ResNet18/ImageNet, ViT, MobileNetV3, GPT-2

## Limitations
- Models energy/area/throughput only, not inference accuracy or device non-idealities
- Accuracy bounded by NeuroSim plug-in device models and by independence assumption in statistical tensor distributions
- Per-mapping evaluation assumes non-data-value-dependent action counts
- Macro D misc. energy/area under-modeled due to unmodeled components
- Evaluated on CNN/ViT/GPT-2 workloads in energy only; no LM accuracy under noise

## Remarks
A widely useful architecture-level tool that complements accuracy-oriented simulators (AIHWKit, CrossSim, MemTorch) by exposing circuit-vs-system trade-offs such as ADC energy and array-size scaling. For mapping LMs to crossbars it provides energy and utilization insight (e.g., array size vs tensor size) but nothing about noise or drift. Related collection tools: NeuroSim, MNSIM 2.0, and the analog-vs-digital benchmarking by Sun et al.

## Cites (in collection, 22)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "To store large DNNs, this may require a multi-chip pipeline [2, 67] or dense storage technologies [1]."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _baseline/comparison_: "Macro A [16] reuses analog outputs across different columns by summing them on wires."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _motivation_: "The second reason for full-stack modeling is that coexploring levels can find better systems [43–46]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "PUMA [74] provides a detailed model of a particular DNN system but does not explore the design space."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _baseline/comparison_: "Modeling Work Architecture Flexibility Circuit Flexibility Energy Accuracy Model Speed NeuroSim [3–6] MNSim [7, 8] Timeloop [9–14] This Work"
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Often, a CiM implementation is published as a macro [16–24], which we define as an array of memory cells plus the additional components needed to compute full MAC operations."
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020) — _background_: "Most commonly, CiM systems keep DNN weights in memory because they do not change during DNN inference [2, 18, 20, 29]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _uses-method-or-tool_: "The Library Plug-In models a library of components used in various CiM works [2, 6, 18, 29, 37, 38, 40, 44, 51, 57]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _contrasts/critiques_: "Unfortunately, prior CiM modeling tools are either inflexible [6, 8], or lack circuit-level modeling [9, 13]."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _contrasts/critiques_: "While CiMLoop models area/energy/throughput, IBM AI Hardware Kit [68], CrossSim [69], and MemTorch [70], model DNN accuracy."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _uses-method-or-tool_: "CiMLoop supports encoding and slicing functions from CiM implementations, including offset [2], differential [38], XNOR [16], and magnitudeonly [44]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "Published macros often use SRAM [17, 20], DRAM [31, 32], ReRAM [18, 30, 33], or STTRAM [34]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "2) Representation: How data values appear is determined by how the hardware represents operands [47]."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021) — _uses-method-or-tool_: "The Library Plug-In models a library of components used in various CiM works [2, 6, 18, 29, 37, 38, 40, 44, 51, 57]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The Library Plug-In models a library of components used in various CiM works [2, 6, 18, 29, 37, 38, 40, 44, 51, 57]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "CiM can reduce energy costs by computing directly within the memory arrays [29], which we define as two-dimensional grids of interconnected memory cells (e.g., SRAM bitcells or RRAM devices)."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Often, a CiM implementation is published as a macro [16–24], which we define as an array of memory cells plus the additional components needed to compute full MAC operations."
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023) — _contrasts/critiques_: "Unfortunately, some prior models may use inaccurate fixed-energy or fixed-power models [8, 9, 13] that do not model data-value-dependence."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _uses-method-or-tool_: "For more information, see the Titanium Law [38], which breaks down the factors that contribute to ADC energy and shows how ADC energy can be reduced."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _baseline/comparison_: "Modeling Work Architecture Flexibility Circuit Flexibility Energy Accuracy Model Speed NeuroSim [3–6] MNSim [7, 8] Timeloop [9–14] This Work"
- [2023_Sun_AIMCvsDIMC_ICCAD](2023_Sun_AIMCvsDIMC_ICCAD.md) AIMC-vs-DIMC (ZigZag-IMC) (2023) — _contrasts/critiques_: "Sun et al. [76] is a contemporaneous work that combines a parameterizable CiM macro model with a flexible architectural specification [77]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)

## Cited by (in collection, 6)
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _contrasts/critiques_: "The latest version of the Timeloop/Accelergy framework, called CiMLoop [3], extends the capabilities of the original framework to support CIM accelerators."
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _data/numbers_: "Specifically, CiMLoop achieves an average error of approximately 3% in hardware estimations [46]."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _uses-method-or-tool_: "NL-DPE and all baselines are simulated in 32nm using CiMLoop [10]."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2024_Andrulis_CiMLoop_ISPASS.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2024_Andrulis_CiMLoop_ISPASS.pdf)
- Full text: [../fulltext/2024_Andrulis_CiMLoop_ISPASS.txt](../fulltext/2024_Andrulis_CiMLoop_ISPASS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/ispass61541.2024.00012
