---
id: W3112740243
key: 2020_Peng_DNNNeuroSimV2_TCAD
title: "DNN+NeuroSim V2.0: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators for On-Chip Training"
short: "DNN+NeuroSim V2.0"
year: 2020
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Xiaochen Peng, Shanshi Huang, Hongwu Jiang, Anni Lu, Shimeng Yu"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-digital", "ReRAM", "FeFET", "PCM", "ECRAM", "Generic-NVM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "benchmarking", "on-chip-training", "device-variation", "read-write-noise", "adc-dac", "energy-efficiency", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 25
cites_in_collection: 6
citations_overall: 308
priority_score: 8.48
doi: "https://doi.org/10.1109/tcad.2020.3043731"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2020_Peng_DNNNeuroSimV2_TCAD.pdf"
fulltext: "../fulltext/2020_Peng_DNNNeuroSimV2_TCAD.txt"
---

# DNN+NeuroSim V2.0

**DNN+NeuroSim V2.0: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators for On-Chip Training** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2020)

## TL;DR
DNN+NeuroSim V2.0 extends the PyTorch-wrapped NeuroSim benchmark to on-chip training by modelling weight-update nonlinearity, asymmetry, device-to-device and cycle-to-cycle variation, and uses it to derive analog-synapse specs (C2C variation <1%, Ron >100 kOhm, write pulse <1 us, nonlinearity within +3/-3) for VGG-8/CIFAR-10.

## Summary
The inference-only DNN+NeuroSim V1.x estimated area, energy, latency and accuracy impact of ADC quantisation and retention. V2.0 adds training: a Python wrapper (WAGE low-precision training, default VGG-8 on CIFAR-10, ResNet-18 supported) injects nonlinear/asymmetric conductance update (LTP/LTD exponential model with parameter A and P/Pmax pulses), D2D and C2C variation and optional momentum, while NeuroSim core adds peripheral circuits for error and weight-gradient computation. Weights and errors use transposable arrays; weight gradients are computed in SRAM-based CIM arrays; chip floorplanning uses weight duplication. Real traces of weights and activations are passed per epoch, with a pseudo-traced estimate of weight-gradient hardware cost (fraction of ones). Benchmarks are 128x128 arrays with 6-bit non-linear flash ADCs, one device per weight (5-7 bit by device levels), for SRAM (sequential/parallel read, 7nm and 32nm) and eNVMs (RRAM, PCM, EpiRAM, ECRAM, FeFET at 32nm).

## Contributions
- Training-capable end-to-end CIM benchmark (accuracy plus area/energy/latency per epoch)
- Behavioural models of update nonlinearity/asymmetry, D2D and C2C variation with momentum optimisation
- Weight-gradient computation architecture using SRAM CIM arrays and transposable arrays for error computation
- Technology benchmark yielding device specs for analog synapses in training

## Key claims (stable IDs)
- **2020_Peng_DNNNeuroSimV2_TCAD#C1** — Momentum optimisation recovers training accuracy under large asymmetric nonlinearity — _support:_ ~85% at NL=+3/-3, ~77% at NL=+6/-6 (VGG-8, 8-bit) — _loc:_ Sec. IV-A, Fig. 10
- **2020_Peng_DNNNeuroSimV2_TCAD#C2** — C2C variation is the critical device factor for in-situ training — _support:_ preferred <1%; sigma 1/3/5% of conductance range degrade accuracy — _loc:_ Sec. IV-A, Fig. 12, Sec. IV-D
- **2020_Peng_DNNNeuroSimV2_TCAD#C3** — Weight-gradient computation dominates training latency and energy — _support:_ off-chip memory access plus SRAM writes; weight update amortised over batch 200 — _loc:_ Sec. IV-B, Fig. 13-14
- **2020_Peng_DNNNeuroSimV2_TCAD#C4** — FeFET design reaches ~91% accuracy with 32 levels — _support:_ with momentum and low C2C variation — _loc:_ Sec. IV-D, Table I

## Results
- Device specs derived: C2C <1%, Ron >100 kOhm, write pulse <1 us, nonlinearity < +3/-3
- With D2D sigma=0.5 and momentum, D2D variation does not hurt (even helps at high nonlinearity)
- 6-bit ADC (flash) is the dominant area component; buffer latency and DRAM energy are bottlenecks (FeFET, 100th epoch, Fig. 13)
- Parallel-read 7nm SRAM still shows superior energy efficiency and throughput versus 32nm eNVM designs (Table I)

## Key numbers
- tech_node: 7nm and 32nm
- array_size: 128x128
- accuracy: ~91% (FeFET, 32 levels, VGG-8 CIFAR-10); ~85% at NL +3/-3
- bits_weight: 5-7b (one device per weight)
- bits_adc: 6b

## Datasets / benchmarks
CIFAR-10

## Limitations
- CNN (VGG-8/CIFAR-10) only; no transformer or language models
- Pseudo-traced approximation for weight-gradient cost
- Behavioural device models, not measured silicon; one device per weight assumption
- Digital SRAM-based weight-gradient units add area/off-chip traffic

## Remarks
Widely used infrastructure for CIM benchmarking and the main reference for how update non-idealities limit analog on-chip training. For SLM/LLM deployment its relevance is the methodology (device-spec derivation, ADC dominance) rather than the CNN results; training LLMs on analog arrays is far beyond what it covers.

## Cites (in collection, 6)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "To solve the bottleneck of extensive data transfer in the conventional von Neumann architectures, compute-in-memory (CIM) has emerged as a promising paradigm for designing the machine learning hardware accelerator [1]."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _extends/builds-on_: "To realize the input data reuse practically, we have proposed a novel mapping method and data flow for CIM inference in prior work [16], where the weights at different spatial location of each kernel are mapped into different sub-matrices."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _extends/builds-on_: "As what has been proposed in prior framework V1.0 [7], the NeuroSim core is wrapped by python library, to support flexible network topologies, the default model is VGG-8 for CIFAR-10 based on low precision training method WAGE [9]."
- [2020_Jiang_MINT_ISCAS](2020_Jiang_MINT_ISCAS.md) MINT (2020) — _extends/builds-on_: "In CIM accelerators, to support on-chip training, we also implement extra peripheral circuits to calculate error and weight gradient in back-propagation (design as done in other works [14][15])."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017)

## Cited by (in collection, 25)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _contrasts/critiques_: "A recent PyTorch re-implementation of a subset of the MLP-NeuroSim package using PyTorch, called DNN+NeuroSim [12], is closest to our framework."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _data/numbers_: "For an efficient CIM array, Gmax needs to be lower than 10 μS (12, 56)."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _data/numbers_: "Besides, as illustrated in previous work [30], the ADC contributes a large portion of total energy consumption and latency in CIM design, becoming more severe with increasing ADC precision."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _uses-method-or-tool_: "For the evaluation, a customized simulator was implemented based on our circuit simulation results and NeuroSim+ [38], [39]."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _contrasts/critiques_: "However, NACIM utilizes a time-consuming PIM simulator (i.e., NeuroSim [17]) as the performance evaluator, resulting in a tremendous search time cost (~59 GPU hours)."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _uses-method-or-tool_: "DAC, input driver, and crossbar area/energy are generated using a modified NeuroSim [2, 44]."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _motivation_: "However, this hardware-integrated re-training can lead to a huge increase in the overall training cost in terms of GPUhours [16, 17, 20]."
- [2023_Cao_RRAMPoolFormer_ISCAS](2023_Cao_RRAMPoolFormer_ISCAS.md) RRAM-PoolFormer (2023) — _baseline/comparison_: "The results of this study are summarized and compared to other recent memristor crossbar DNN solutions in Table I (including DNN+NeuroSim V2.0 [28])."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _baseline/comparison_: "Framework comparison table lists NeuroSim, IBM Analog Hardware Acceleration Kit, CrossSim, XB-SIM, and MemTorch as the actively maintained/compared AIMC simulation toolkits, evaluated on ML library, network types supported (incl. Recurrent/Transformer), accuracy estimation, HW-calibration, and on-chip training/inference support."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _contrasts/critiques_: "Unfortunately, prior CiM modeling tools are either inflexible [6, 8], or lack circuit-level modeling [9, 13]."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _baseline/comparison_: "Fig. 1(a) presents a radar chart that compares a ViT model inferred on analog RRAM crossbars against digital SRAM-based IMC arrays [14] (devoid of read and write non-idealities)."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _uses-method-or-tool_: "Following prior works, we assume that multiple tiles can map one layer but not vice-versa [7], [33]."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _uses-method-or-tool_: "SCALE-Sim is utilized for the systolic array cores and a modified NeuroSim is employed to obtain the latency of all on-chip buffers, and peripheral circuits in ReRAM cores [47] [32]."
- [2025_Dong_TopkimaFormer_TCAS-I](2025_Dong_TopkimaFormer_TCAS-I.md) Topkima-Former (2025) — _uses-method-or-tool_: "The overall system simulation, conducted using the NeuroSim framework [5], comprises chip, tile, processing element (PE) and array hierarchies."
- [2025_Qin_NVCiMPT_DATE](2025_Qin_NVCiMPT_DATE.md) NVCiM-PT (2025) — _uses-method-or-tool_: "We also evaluate the latency and energy of retrieval of the appropriate data by our scaled search algorithm on NVCiM via NeuroSim [36]."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _baseline/comparison_: "CiMLoop was selected for its relatively high simulation speed and accuracy close to that of NeuroSim [49], while 7 offering enhanced flexibility."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _uses-method-or-tool_: "We modify NeuroSim v2.1 [30] to evaluate the non-ideal effects."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2020_Peng_DNNNeuroSimV2_TCAD.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2020_Peng_DNNNeuroSimV2_TCAD.pdf)
- Full text: [../fulltext/2020_Peng_DNNNeuroSimV2_TCAD.txt](../fulltext/2020_Peng_DNNNeuroSimV2_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2020.3043731
