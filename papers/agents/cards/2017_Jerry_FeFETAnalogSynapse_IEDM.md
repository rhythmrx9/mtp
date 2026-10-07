---
id: W2787453651
key: 2017_Jerry_FeFETAnalogSynapse_IEDM
title: "Ferroelectric FET analog synapse for acceleration of deep neural network training"
short: "FeFET Analog Synapse"
year: 2017
venue: "IEDM"
venue_full: "2017 IEEE International Electron Devices Meeting (IEDM)"
authors: "Matthew Jerry, Pai-Yu Chen, Jianchi Zhang, Pankaj Sharma, Kai Ni, Shimeng Yu, Suman Datta"
category: "10 On-chip & Analog Training"
devices: ["FeFET"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["on-chip-training", "analog-mvm", "device-variation"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 9
cites_in_collection: 0
citations_overall: 590
priority_score: 6.43
doi: "https://doi.org/10.1109/iedm.2017.8268338"
pdf: null
fulltext: null
---

# FeFET Analog Synapse

**Ferroelectric FET analog synapse for acceleration of deep neural network training** — 2017 IEEE International Electron Devices Meeting (IEDM) (2017)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Demonstrates a 5-bit ferroelectric-FET (FeFET) analog synapse with symmetric potentiation/depression and a 45x tunable conductance range using 75ns update pulses, and benchmarks it via a circuit macro-model to show 10^3-10^6x faster on-chip learning latency than multi-state RRAM analog synapses.

## Summary
Deep neural network training is normally bottlenecked by off-chip storage and updating of synaptic weights (e.g., in DRAM), which limits energy efficiency and training time; on-chip analog non-volatile memory crossbars could remove this bottleneck if they can store and update weights with enough precision. The authors exploit voltage-controlled partial polarization switching dynamics in ferroelectric-FETs (FeFETs) to build an analog synapse and develop a transient Preisach model that accurately predicts minor-loop trajectories and remnant polarization charge for arbitrary pulse width, voltage and history. They experimentally demonstrate a FeFET-based analog synapse with 5-bit resolution, symmetric potentiation/depression characteristics, and a 45x tunable conductance range achieved with 75 ns update pulses. Using a circuit macro-model built on these device characteristics, they benchmark on-chip learning performance (area, latency, energy, accuracy) of a FeFET synaptic core and report a 10^3-10^6x improvement in online-learning latency compared to multi-state RRAM-based analog synapses.

## Contributions
- A transient Preisach model of FeFET partial polarization switching that predicts minor-loop trajectories and remnant polarization charge for arbitrary pulse width, voltage and programming history
- Experimental demonstration of a 5-bit FeFET analog synapse with symmetric potentiation and depression and a 45x conductance tuning range using fast (75 ns) update pulses
- A circuit macro-model benchmarking the area, latency, energy and accuracy of an on-chip learning core built from FeFET synapses
- Quantitative comparison showing large on-chip training-latency advantages of FeFET synapses over multi-state RRAM analog synapses

## Key claims (stable IDs)
- **2017_Jerry_FeFETAnalogSynapse_IEDM#C1** — FeFET devices can implement a 5-bit analog synapse with symmetric, well-controlled potentiation/depression behavior — _support:_ 'experimentally demonstrate a 5-bit FeFET synapse with symmetric potentiation and depression characteristics' — _loc:_ Abstract
- **2017_Jerry_FeFETAnalogSynapse_IEDM#C2** — The FeFET synapse supports fast weight updates with a wide dynamic range — _support:_ 45x tunable range in conductance achieved with a 75 ns update pulse — _loc:_ Abstract
- **2017_Jerry_FeFETAnalogSynapse_IEDM#C3** — A FeFET-based synaptic core offers dramatically faster on-chip learning than multi-state RRAM-based analog synapse cores — _support:_ circuit macro-model shows a 10^3-10^6x acceleration in online-learning latency over multi-state RRAM analog synapses — _loc:_ Abstract

## Results
- 5-bit (32-level) FeFET analog synapse resolution demonstrated experimentally
- 45x tunable conductance range with 75 ns update pulses
- 10^3 to 10^6x improvement in on-chip online-learning latency vs. multi-state RRAM analog synapses (circuit macro-model projection)

## Limitations
- Full text not available to this review (abstract-only basis); exact test-vehicle size, network benchmarks, and macro-model assumptions could not be independently verified
- Device-level demonstration appears to be at the single/few-device level, with array-level and full-chip integration performance only estimated via a circuit macro-model rather than measured directly
- The large (10^3-10^6x) latency advantage over RRAM synapses is a modeled/projected comparison rather than a head-to-head silicon measurement
- No neural-network task-level (e.g., classification) accuracy results are reported in the abstract; accuracy benchmarking in the macro-model appears to be at the circuit/synapse level rather than end-to-end

## Remarks
This is an early and influential device-level demonstration that FeFETs can serve as fast, symmetric, multi-bit analog synapses for on-chip DNN training, positioning FeFET as a competitive alternative to RRAM/PCM for analog training accelerators; it is frequently cited in later on-chip-training and device-comparison surveys (e.g., alongside DNN+NeuroSim benchmarking work). Because only the abstract was available, the strong latency-improvement claim versus RRAM synapses should be read as model-based projection grounded in measured single-device FeFET characteristics, not as a measured full-core or full-chip comparison.

## Cited by (in collection, 9)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "A recent experimental demonstration of analog FeFET synaptic devices used the gate last fabrication process flow of n-channel FeFETs [88], as shown in Fig. 6."
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018) — _background_: "If we assume a time between weight updates of the order of 200 ns, and a retention time in the order of seconds, the updated weight will decay according to w ←w 1− . τret (12) This has the same form as the weight decay produced by L2 regularization [59] which is a method to avoid overfitting."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _background_: "Among the available three-terminal synaptic devices, ferroelectric transistors based on zirconium-doped hafnium oxide (HfZrOx) are advantageous because they have CMOS compatibility, fast operation speed, low operation voltages, and high scalability (33–36)."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "These techniques can be more generally applied to other non-volatile resistive memory technologies such as phase-change memory8,17,21,23,24, magnetoresistive RAM48 and ferroelectric field-effect transistors49."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "Meanwhile, as emerging memories (such as resistive random access memory (RRAM) [2] and ferroelectric field-effect transistor (FeFET) [3]) offer high integration density and low operating energy costs, they are becoming promising candidates for CIM implementation."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _background_: "The development of in-memory computing (IMC) accelerators, particularly those based on resistive memories, such as RRAM [1], Phase Change Memories (PCM) [2], and FeFET [3], stand out as one of the most promising solutions due to their potential for high energy efficiency and scalability."
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)

## Files
- PDF: not available locally (save as `papers/10_On_Chip_and_Analog_Training/2017_Jerry_FeFETAnalogSynapse_IEDM.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iedm.2017.8268338
