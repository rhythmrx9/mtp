---
id: W2736591611
key: 2017_Xia_MNSIM_TCAD
title: "MNSIM: Simulation Platform for Memristor-based Neuromorphic Computing System"
short: "MNSIM"
year: 2017
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2017/2018)"
authors: "Lixue Xia, Boxun Li, Tianqi Tang, Peng Gu, Pai-Yu Chen, Shimeng Yu, Yu Kevin Cao, Yu Wang, Yuan Xie, Huazhong Yang"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Memristor(generic)", "ReRAM"]
models: ["MLP", "CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "benchmarking", "crossbar-architecture", "ir-drop-parasitics", "device-variation", "peripheral-circuits", "energy-efficiency", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 24
cites_in_collection: 3
citations_overall: 171
priority_score: 8.25
doi: "https://doi.org/10.1109/tcad.2017.2729466"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2017_Xia_MNSIM_TCAD.pdf"
fulltext: "../fulltext/2017_Xia_MNSIM_TCAD.txt"
---

# MNSIM

**MNSIM: Simulation Platform for Memristor-based Neuromorphic Computing System** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2017/2018) (2017)

## TL;DR
MNSIM is a behavior-level simulator for memristor-crossbar neuromorphic accelerators with hierarchical architecture, area/power/latency models and a fast behavior-level accuracy model, achieving >7000x speed-up over SPICE with <10% error on power/latency and <1% on accuracy loss.

## Summary
MNSIM proposes a three-level hierarchy (accelerator, computation bank, computation unit) in which all design parameters (crossbar size, computation parallelism degree i.e. number of read circuits, interconnect technology node, device precision, CMOS node, etc.) are configurable through a configuration list (Table I). It provides a reference design for large-scale networks: weight matrices larger than a crossbar are split across multiple crossbars with peripheral adders, and CNN layers are mapped to computation banks in a pipeline. The behavior-level accuracy model decouples interconnect IR-drop and non-ideal device effects, fits SPICE-derived error-rate curves of output voltage versus crossbar size and interconnect node (Fig. 5), converts them to digital error via quantization levels, estimates average and worst cases, and accumulates error across layers. Validation compares against SPICE on a 3-layer 128x128 FC NN (90nm), JPEG encoding NN 64x16x64, and layout of a 32x32 1T1R crossbar with decoder in 130nm. Design-space exploration is done on a single layer (45nm reference) and VGG-16/ImageNet (8-bit data, 7-bit memristor).

## Contributions
- Hierarchical structure unifying memristor-based accelerators with design parameters at accelerator, bank and unit levels
- Reference design plus flexible interfaces for customization
- Behavior-level computing-accuracy model for average/worst-case error with >7000x speed-up over SPICE
- Design-space exploration of crossbar size, parallelism and interconnect technology with area/power/latency/accuracy trade-offs

## Key claims (stable IDs)
- **2017_Xia_MNSIM_TCAD#C1** — MNSIM is >7000x faster than SPICE for a single crossbar — _support:_ 16x16: 5.35 s vs 0.0007 s (7642x); 32x32: 12509x; 64x64: 13873x; 128x128: 8088x — _loc:_ Sec. VII-B / Table III
- **2017_Xia_MNSIM_TCAD#C2** — Power and latency errors <10% vs SPICE — _support:_ 2-layer 128x128 FC NN at 90nm — _loc:_ Sec. VII-A / Table II
- **2017_Xia_MNSIM_TCAD#C3** — Accuracy-model error <1% on JPEG-encoding 64x16x64 NN — _support:_ stated — _loc:_ Sec. VII-A
- **2017_Xia_MNSIM_TCAD#C4** — Larger crossbars reduce area/power but hurt accuracy; accuracy improves at the cost of area/power only when crossbar >64 at 45nm interconnect — _support:_ Tables IV-V — _loc:_ Sec. VII-C
- **2017_Xia_MNSIM_TCAD#C5** — All 10,220 designs simulated within 4 seconds enables traversal optimization — _support:_ crossbar 4-1024, parallelism 1-128, interconnect {18,22,28,36,45} nm — _loc:_ Sec. VII-C

## Results
- Area estimate for 32x32 1T1R crossbar layout (130nm) is 2251 um2 vs layout 3420 um2; validation coefficient introduced
- VGG-16 case: 8-bit data, 7-bit memristor, 45nm CMOS, error constraint 50%, interconnect up to 90nm
- PRIME simulated at 65nm (area 0.17 mm2, energy 0.08 uJ per task, latency 0.66 us) and ISAAC reproduced (Table VII, not directly comparable)
- Computation error from interconnect and read variation accumulates layer-by-layer

## Key numbers
- tech_node: 90nm/130nm validation; 45nm reference design
- array_size: 4 to 1024 swept
- throughput: >7000x faster than SPICE
- accuracy: <1% accuracy-model error; <10% power/latency error
- bits_weight: 7b memristor, 8b data

## Datasets / benchmarks
JPEG encoding NN, VGG-16/ImageNet

## Limitations
- Behavior-level, not circuit-accurate; average-case input/resistance assumption causes power error
- Accuracy model captures IR-drop/variation only, no drift or noise dynamics
- Only MLP/CNN workloads, no transformers or LMs
- Area model needs technology-specific coefficient
- Memristor-only; no PCM/FeFET specific models

## Remarks
A foundational simulator in this collection (MNSIM 2.0 and DNN+NeuroSim follow it) whose key idea, fitting SPICE-derived error curves versus crossbar size for fast accuracy estimation, remains relevant for deciding LM tile sizes. Evidence is validation versus SPICE rather than silicon, and the models are too coarse for modern noise-aware transformer evaluation.

## Cites (in collection, 3)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _motivation_: "In the future, we will further support the simulation for other structures like dynamic synaptic properties [22], on-chip Training method [51], and inner-layer pipeline structure [7]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "Two related designs [6], [7] are simulated using MNSIM to validate its scalability."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "This characteristic avoids the high-writing-cost problem [6] and the endurance limitation [16] of memristor devices."

## Cited by (in collection, 24)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _contrasts/critiques_: "Some circuit-level [1] and behavior-level [12] simulation platforms take the impact of hardware errors into consideration. However, the circuit-level tool [1] is hard to be integrated with various neural networks while the behavior-level tool [12] provides only imprecise analysis on inference accuracy."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _uses-method-or-tool_: "The work frequency of MISCA is set to 100MHz, and the whole system is simulated by MNSIM[17]."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _background_: "MNSIM [21] is a tool for early design space exploration of such architectures."
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020) — _uses-method-or-tool_: "We evaluate TOPAR, a thermal-aware optimization framework, based on the practical configuration of ReRAM-based DNN accelerator with 2bit cell resolution and 64x64 array size [2, 12]."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "A promising emerging technology is the recently discovered resistive random access memory (ReRAM) [14, 15] devices that are able to perform the inherently parallel insitu matrix-vector multiplication in the analog domain."
- [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) Area-Efficient Multi-Task BERT (2021) — _background_: "The ReRAM-based accelerators [3], [20], [27] are proposed to solve the data communication issue by adopting in-memory computation."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _background_: "Furthermore, they utilize PIM simulators, e.g., MNSIM [16] and NeuroSim [17], to evaluate the PIM-based NN accuracy and other hardware performance."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _uses-method-or-tool_: "We modify the MNSIM2.0 [33], a behavior-based PIM simulation platform, to evaluate the performance of the proposed ReRAM-based DNN accelerators."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "Therefore, many large-scale simulations encompassing device and circuit nonidealities have been performed to quantify their impact on DNN accuracy for training and inference21–28 ."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _contrasts/critiques_: "On the other hand, architectural models of resistive crossbars [27, 29] target design space exploration and use highly simplified error models that are reasonable for their context, but inadequate for evaluating application-level accuracy of DNNs."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _baseline/comparison_: "MNSIM[38] and NeuroSim[5] are two famous ReRAM crossbar simulators."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _baseline/comparison_: "Some aspects of our AIMC crossbar model have been investigated individually in earlier studies, such as the effect of ADC/DAC quantization, IR-drop, and general read noise55–57, as well as data-dependent long-term noise38."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "To overcome this challenge, Xia et al. presented MNSIM and Zhu et al. presented the successor MNSIM 2.0."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _baseline/comparison_: "Modeling Work Architecture Flexibility Circuit Flexibility Energy Accuracy Model Speed NeuroSim [3–6] MNSim [7, 8] Timeloop [9–14] This Work"
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2017_Xia_MNSIM_TCAD.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2017_Xia_MNSIM_TCAD.pdf)
- Full text: [../fulltext/2017_Xia_MNSIM_TCAD.txt](../fulltext/2017_Xia_MNSIM_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2017.2729466
