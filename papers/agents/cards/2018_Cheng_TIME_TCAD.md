---
id: W2796472956
key: 2018_Cheng_TIME_TCAD
title: "TIME: A Training-in-Memory Architecture for RRAM-Based Deep Neural Networks"
short: "TIME"
year: 2018
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2018)"
authors: "Ming Cheng, Lixue Xia, Zhenhua Zhu, Yi Cai, Yuan Xie, Yu Wang, Huazhong Yang"
category: "10 On-chip & Analog Training"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["on-chip-training", "crossbar-architecture", "peripheral-circuits", "analog-mvm"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 12
cites_in_collection: 4
citations_overall: 66
priority_score: 6.11
doi: "https://doi.org/10.1109/tcad.2018.2824304"
pdf: null
fulltext: null
---

# TIME

**TIME: A Training-in-Memory Architecture for RRAM-Based Deep Neural Networks** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2018) (2018)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
TIME is a Training-in-Memory RRAM architecture and peripheral-circuit design supporting backpropagation and weight update (not just inference), reporting 5.3x higher energy efficiency than DaDianNao for supervised learning and up to 126x higher efficiency than GPU for deep reinforcement learning.

## Summary
Neural-network training is time- and resource-intensive, and while RRAM crossbars can efficiently perform the matrix-vector multiplications used in inference, existing RRAM architectures only support inference and cannot perform the backpropagation and weight-update steps needed for on-chip training; moreover, the iterative RRAM weight updates required for training incur large energy costs due to RRAM's non-ideal device behavior. The authors propose TIME, a Training-in-Memory RRAM architecture and accompanying peripheral circuit design that supports backpropagation and weight update directly on RRAM crossbars while maximizing reuse of the peripheral circuits already used for inference. They also design a set of optimization strategies that target RRAM's non-ideal factors to reduce the cost of tuning (writing) RRAM cells during training. They evaluate TIME on both supervised learning (SL) and deep reinforcement learning (DRL) workloads, including a specific DRL-oriented mapping method to further improve energy efficiency, using simulation. Reported results show TIME achieves 5.3x higher energy efficiency than DaDianNao (a CMOS ASIC) on average for supervised learning, and about 126x higher energy efficiency than GPU on average for deep reinforcement learning, with the authors projecting up to two further orders of magnitude improvement if RRAM tuning costs can be further reduced.

## Contributions
- TIME, an RRAM-based Training-in-Memory architecture that supports backpropagation and weight update in addition to inference, unlike prior RRAM accelerators limited to inference
- A peripheral circuit design that maximizes reuse of inference-time peripheral circuitry (ADCs/DACs, sense amps, etc.) for the training (BP/weight-update) datapath
- A set of optimization strategies specifically targeting RRAM non-ideal factors to reduce the energy/time cost of iterative weight tuning during training
- Evaluation across both supervised learning and deep reinforcement learning workloads, including a DRL-specific mapping method for improved energy efficiency

## Key claims (stable IDs)
- **2018_Cheng_TIME_TCAD#C1** — TIME achieves substantially higher energy efficiency than a CMOS ASIC baseline (DaDianNao) for supervised-learning training workloads — _support:_ 'TIME can achieve 5.3x higher energy efficiency on average compared with DaDianNao' — _loc:_ Abstract
- **2018_Cheng_TIME_TCAD#C2** — TIME achieves much higher energy efficiency than GPU for deep reinforcement learning workloads — _support:_ 'TIME can perform an average 126x higher than GPU in energy efficiency' in DRL — _loc:_ Abstract
- **2018_Cheng_TIME_TCAD#C3** — Further reductions in RRAM tuning (write) cost could allow TIME's energy-efficiency advantage over ASIC to grow by roughly two more orders of magnitude — _support:_ 'If the cost of tuning RRAM can be further reduced, TIME has the potential to boost the energy efficiency by two orders of magnitudes compared with ASIC' — _loc:_ Abstract

## Results
- 5.3x average energy-efficiency improvement over DaDianNao (ASIC) for supervised learning
- 126x average energy-efficiency improvement over GPU for deep reinforcement learning
- Up to ~2 further orders-of-magnitude projected improvement vs. ASIC if RRAM write/tuning cost is reduced

## Limitations
- Full text not available to this review (abstract-only basis); specific benchmark networks, crossbar sizes, and precision/accuracy assumptions underlying the reported speedups could not be independently verified
- Results are simulation-based rather than measured on fabricated silicon
- The large gains for deep reinforcement learning depend on a specific, workload-tailored mapping method, so the generality of the 126x figure across other DRL algorithms is unclear from the abstract alone
- The stated further two-orders-of-magnitude improvement is an explicitly conditional projection (contingent on reducing RRAM tuning cost), not an achieved result

## Remarks
TIME is an important and frequently cited RRAM training-in-memory architecture, built on the same Tsinghua group's prior inference-focused work (MNSIM), and is commonly used as a comparison baseline in later on-chip/analog training architecture papers (e.g., PANTHER, TxSim). Because the full text could not be retrieved, the headline efficiency numbers above are taken directly from the paper's own abstract; the practical significance of the DRL-specific 126x figure depends on workload and mapping details not verifiable here.

## Cites (in collection, 4)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 12)
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "This differential-pair data representation is frequently used in CIM design such as [5, 24]."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _background_: "Existing studies have proposed various memristor-based PIM architecture and realize 2-3 orders of magnitude energy efficiency improvement compared with GPU and CMOS-based ASIC solutions [3] [4] [6] [5] [23]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "Resistive crossbar based specialized hardware systems have been proposed for accelerating DNN inference [7–11] and training [12, 13]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Many machine learning accelerators have been proposed that leverage memristor crossbars [9, 10, 12, 22, 23, 53, 58, 66, 73, 88, 95, 100]."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _contrasts/critiques_: "For example, work in [25–27] extend the application of analog crossbar memory to accelerate training, but they still have expensive converter units and multi-bit devices."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "This approach is more flexible than the parallel weight update based on overlapping pulses because it can implement any learning rule, not only stochastic gradient descent, and the digital computation and accumulation of weight updates significantly relax the requirements on the device granularity and endurance116."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _contrasts/critiques_: "Other works [8] [9] try to train NN on the ReRAM crossbar hardware directly with stochastic gradient decent algorithm (online train)."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "important in NN processing, some studies propose to use memristor-based architectures to accelerate NN training [4, 11, 35]."
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)

## Files
- PDF: not available locally (save as `papers/10_On_Chip_and_Analog_Training/2018_Cheng_TIME_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2018.2824304
