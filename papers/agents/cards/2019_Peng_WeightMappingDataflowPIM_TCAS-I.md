---
id: W2997869757
key: 2019_Peng_WeightMappingDataflowPIM_TCAS-I
title: "Optimizing Weight Mapping and Data Flow for Convolutional Neural Networks on Processing-in-Memory Architectures"
short: "Weight Mapping Dataflow PIM"
year: 2019
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers (2019)"
authors: "Xiaochen Peng, Rui Liu, Shimeng Yu"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "dataflow-pipelining", "cnn-accelerator", "tiling-partitioning"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 19
cites_in_collection: 4
citations_overall: 100
priority_score: 8.8
doi: "https://doi.org/10.1109/tcsi.2019.2958568"
pdf: null
fulltext: null
---

# Weight Mapping Dataflow PIM

**Optimizing Weight Mapping and Data Flow for Convolutional Neural Networks on Processing-in-Memory Architectures** — IEEE Transactions on Circuits and Systems I: Regular Papers (2019) (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A kernel-splitting weight-mapping and dataflow scheme that assigns input data to processing elements by spatial location (instead of unrolling whole 3D kernels into crossbar columns) improves ResNet-34 throughput/energy efficiency by ~1.4x, and by 1.96x with an optimal pipeline architecture reaching 132,476 FPS and 20.1 TOPS/W on a 32nm RRAM PIM design.

## Summary
The paper addresses inefficient input-data reuse in prior PIM accelerators, which typically unroll each 3D convolutional kernel into a vertical column of a large weight matrix mapped onto a crossbar, forcing the same input data to be accessed multiple times. The authors propose a new weight-mapping method and corresponding dataflow that divides kernels and assigns input data to different processing elements (PEs) according to their spatial location, maximizing both weight and input data reuse for PIM architectures. As a case study, they benchmark an 8-bit RRAM-based PIM design at 32 nm technology. They further propose an optimal pipeline architecture (with added area overhead) to improve throughput and energy efficiency beyond what the new mapping/dataflow alone achieves.

## Contributions
- A novel weight-mapping method that splits convolutional kernels and assigns input data to PEs by spatial location, rather than unrolling whole 3D kernels into crossbar columns
- A corresponding dataflow that maximizes both weight reuse and input-data reuse for PIM-based CNN inference
- A case-study benchmark of an 8-bit RRAM-based PIM design at 32 nm incorporating the new mapping and dataflow
- An optimal pipeline architecture (with ~50% area overhead) that further improves throughput and energy efficiency over the mapping/dataflow optimization alone

## Key claims (stable IDs)
- **2019_Peng_WeightMappingDataflowPIM_TCAS-I#C1** — The new mapping/dataflow improves speed and efficiency over conventional kernel-unrolling mapping — _support:_ ~2.03x speedup and ~1.4x improvement in throughput and energy efficiency for ResNet-34, compared with the prior design based on conventional mapping — _loc:_ Abstract
- **2019_Peng_WeightMappingDataflowPIM_TCAS-I#C2** — Adding an optimal pipeline architecture yields large further throughput/energy gains at a bounded area cost — _support:_ with ~50% area overhead, achieves overall 913x and 1.96x improvement in throughput and energy efficiency, reaching 132,476 FPS and 20.1 TOPS/W — _loc:_ Abstract

## Results
- ~2.03x speedup and ~1.4x throughput/energy-efficiency improvement for ResNet-34 vs. conventional kernel-unrolling mapping
- With optimal pipelining (~50% area overhead): 913x throughput improvement and 1.96x energy-efficiency improvement overall
- Final design reaches 132,476 FPS and 20.1 TOPS/W (8-bit RRAM-based PIM, 32 nm)

## Limitations
- Analysis based on the abstract only; details of the non-ideality assumptions, crossbar size, and ADC configuration used in the 32nm case study could not be verified from the full text
- The 913x throughput figure appears to combine the mapping/dataflow gain with the pipeline architecture's gain, so the marginal contribution of each technique individually needs the full paper to disentangle

## Remarks
This paper (from the Georgia Tech group behind DNN+NeuroSim) is a useful, mapping-and-dataflow-centric companion to that benchmarking framework: its core insight -- that naive kernel-to-column unrolling forces redundant input reads, and that spatially-aware kernel splitting plus PE-level dataflow can reclaim significant reuse -- is a recurring theme in later PIM dataflow/compiler papers (it is cited by DNN+NeuroSim V2.0, several mapping-method and tile-level dataflow optimization works). Because only the abstract was available here, the specific crossbar/ADC configuration and the breakdown between mapping-only and mapping+pipeline gains should be confirmed against the full TCAS-I text before being used as precise baselines.

## Cites (in collection, 4)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 19)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _extends/builds-on_: "To realize the input data reuse practically, we have proposed a novel mapping method and data flow for CIM inference in prior work [16], where the weights at different spatial location of each kernel are mapped into different sub-matrices."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _uses-method-or-tool_: "The ReRAM crossbar and peripheral configurations are adopted from [52]."
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _background_: "Reference [53] proposes an optimized weight mapping and dataflow in computing convolutional neural networks on ReRAM-based PIM."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _uses-method-or-tool_: "The area and power of the IMC core, featuring a 128 × 128 RRAM crossbar array, are adopted from [36]."
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _background_: "This helps in reduction of intermediate result storage space as well as speeding up execution [6]."
- [2023_Sun_AIMCvsDIMC_ICCAD](2023_Sun_AIMCvsDIMC_ICCAD.md) AIMC-vs-DIMC (ZigZag-IMC) (2023) — _contrasts/critiques_: "Similarly, for mapping space explorations, most of the focus has been dedicated to AIMC designs, while lacking DIMC assessment [18, 19, 22, 23]."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "To reuse input data and reduce loading overhead, (I, O, K 2 ) is adopted in [30], requiring further accumulation of results from K 2 parallel weight matrices to obtain the complete result."
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Rhe_ETA_APCCAS](2025_Rhe_ETA_APCCAS.md) ETA (2025)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2019_Peng_WeightMappingDataflowPIM_TCAS-I.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcsi.2019.2958568
