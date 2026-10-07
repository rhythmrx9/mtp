---
id: W2805362231
key: 2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron
title: "In-memory computing with resistive switching devices"
short: "Ielmini-Wong IMC review"
year: 2018
venue: "NatElectron"
venue_full: "Nature Electronics, vol. 1, pp. 333-343 (2018)"
authors: "Daniele Ielmini, H.‐S. Philip Wong"
category: "01 Surveys & Foundations"
devices: ["ReRAM", "PCM", "MRAM", "FeRAM", "Generic-NVM"]
models: ["Other"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "analog-mvm", "device-variation", "conductance-drift", "read-write-noise", "endurance-retention", "crossbar-architecture", "3d-integration"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 27
cites_in_collection: 2
citations_overall: 2281
priority_score: 12.18
doi: "https://doi.org/10.1038/s41928-018-0092-2"
pdf: "../../01_Surveys_and_Foundations/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.pdf"
fulltext: "../fulltext/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.txt"
---

# Ielmini-Wong IMC review

**In-memory computing with resistive switching devices** — Nature Electronics, vol. 1, pp. 333-343 (2018) (2018)

## TL;DR
Nature Electronics (2018) review of in-memory computing with two-terminal resistive switching devices (RRAM, PCM, MRAM, FeRAM), organised as digital stateful logic, analogue crosspoint MVM/CAM/PUF, cumulative-resistance (neuromorphic) computing and stochastic computing, plus scaling and variability challenges.

## Summary
The article motivates in-memory computing by the memory wall and the plateau of CMOS scaling, noting most energy/time in data-centric tasks goes to data movement. It first surveys computational memory technologies (RRAM filament/defect migration, PCM crystallisation, MRAM, FeRAM) and their switching physics. It then covers digital computing by binary resistive switching (V-R and R-R stateful logic such as IMP, Scouting-type gates with RRAM), computing by cumulative resistive changes (gradual PCM crystallisation for arithmetic summation and neuromorphic synapses/neurons, spike-based learning), stochastic computing (using cycle-to-cycle switching variation for true random number generators, stochastic neurons and PUFs), and analogue computing with crosspoint arrays where Ohm's and Kirchhoff's laws give I_i = sum_j G_ij V_j in one step, applied to image compression, sparse coding, ANNs (weights trained in hardware by pulse accumulation), content-addressable memory and sneak-path PUFs. The outlook discusses variability (verify-and-correct is hard in computing), RRAM instability and PCM drift (alleviated by higher read current or core-shell cells), the high energy of ADC/periphery, parasitic IR drop, the fact that crosspoint MVM is approximate and suited to error-tolerant tasks, and the need for scaling (4F2 cells, horizontal/vertical 3D stacking, interconnect and periphery scaling). It also argues that computational-memory devices will differ from storage-class devices.

## Contributions
- Unified taxonomy of digital, analogue, cumulative and stochastic in-memory computing with resistive devices
- Linking device switching physics to computing function and error sources
- Discussion of variability, drift, noise, IR drop and periphery cost as limits for analogue MVM
- Scaling roadmap for crosspoint arrays including 3D stacking

## Key claims (stable IDs)
- **2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron#C1** — Crosspoint arrays implement analogue MVM in one step via Ohm and Kirchhoff laws — _support:_ Eq. (1) I_i = sum_j G_ij V_j — _loc:_ Analogue computing with crosspoint arrays, Fig. 5
- **2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron#C2** — Crosspoint MVM is approximate and should target error-tolerant tasks — _support:_ pattern recognition, page ranking, data inference — _loc:_ Outlook
- **2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron#C3** — Energy of crosspoint MVM must include ADC/DAC periphery — _support:_ significant fraction spent in converters; fair comparison needs direct and periphery contributions — _loc:_ Analogue computing section
- **2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron#C4** — PCM drift and RRAM instability limit analogue accuracy — _support:_ drift alleviated by higher read current or core-shell cells — _loc:_ Outlook

## Results
- Qualitative review: no new measurements; compares device types (RRAM, PCM, MRAM, FeRAM) and computing schemes
- Crosspoint cell area 4F2 and 3D stacking multiply density roughly by number of layers (Fig. 6)

## Limitations
- 2018 snapshot: no coverage of transformers/LLMs or large multi-core chips
- Primarily device and circuit-level view; little on mapping, quantisation or compilation
- Broad scope means analogue DNN inference is only one of several sections

## Remarks
A foundational, device-oriented background reference for the whole collection: it states the core physics (Ohm/Kirchhoff MVM) and the standard list of obstacles (variation, drift, IR drop, ADC energy, scaling) that later chip and architecture papers address. It should be paired with later surveys for transformer/LLM-era context.

## Use in the original review
- F15 (High confidence): The shared motivation across this literature is the memory wall: data movement between separate processing and memory units is the dominant time and energy cost in von Neumann systems, aggravated by data-centric AI workloads. In-memory computing computes in place inside the array by exploiting device physics; two-terminal resistive switching devices are the favoured substrate.

## Cites (in collection, 2)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Crosspoint MVM can be adopted for a broad range of problems, including image compression, sparse coding, and implementation of artificial neural networks (ANNs), where Gij has the meaning of a synaptic weight, Vj is a pre-synaptic spike amplitude, and Ii is the input signal to the ith neuron (refs 69, 70)."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Crosspoint MVM can be adopted for a broad range of problems, including image compression, sparse coding, and implementation of artificial neural networks (ANNs), where Gij has the meaning of a synaptic weight, Vj is a pre-synaptic spike amplitude, and Ii is the input signal to the ith neuron (refs 69, 70)."

## Cited by (in collection, 27)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "The associated expenditure of chip area could be minimized in the future by employing high-density integration of memristors (refs 32, 33)."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "This led to a growing interest in exploring NVM technology as the substrate for the next generation of ML hardware [19, 25, 26]."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "Fig. 1. (b) Multilevel I - V characteristics of 1T1R RRAM device measured for increasing VG. [2]."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _background_: "Charge-based memory technologies (e.g. SRAM [10], DRAM, Flash) and non-volatile (NV) resistive memory technologies [11] (e.g. ReRAM [12] PCM [2] and MRAM [13]) both serve as computing substrates for analog in-memory computing."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "As resistive memory continues to scale towards offering tera-bits of on-chip memory50, such a co-optimization approach will equip CIM hardware on the edge with sufficient performance, efficiency and versatility to perform complex AI tasks that can only be done on the cloud today."
- [2022_Amin_ParasiticsPartitioning_ISCAS](2022_Amin_ParasiticsPartitioning_ISCAS.md) Parasitics-Partitioning (2022) — _background_: "With the increased computational demands of machine learning (ML) workloads, in-memory computing (IMC) [1] architectures have attracted considerable attention to address the processor-memory bottleneck in conventional von Neumann architectures."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "the most competitive candidates at present among emerging memories are resistive random-access memory (RRAM) [76] [77] [78] [79] [80] [81] [82] [83] [84] [37], phase-change memory (PCM) [85] [34] [86], and magnetic random-access memory (MRAM) [87] [88] [89] [90] [91]."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "By coordinating the applied read voltages and measurements of the output currents, the vector-matrix multiplications for information forwarding and error backpropagation can be done in one step [3, 4]."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _background_: "Another design is the single-bit memristor, where we need multiple memristors to store a single weight. Examples are [20, 21]."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _background_: "One such compute substrate which shows significant promise for adversarial robustness is that based on analog in-memory computing (AIMC)6–8."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _motivation_: "While the RRAM-only strategy suffers from inherent noise and complex write-verify operations [40], the SRAM-only strategy is limited by its volatility and low storage density [41]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Jiang_MINT_ISCAS](2020_Jiang_MINT_ISCAS.md) MINT (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025)
- [2024_Ahsan_SPICEenvmACIMFramework_ICCAD](2024_Ahsan_SPICEenvmACIMFramework_ICCAD.md) SPICE eNVM ACIM Framework (2024)
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2026_Sharma_HatFi_VTS](2026_Sharma_HatFi_VTS.md) HATFI (2026)

## Files
- PDF: [../../01_Surveys_and_Foundations/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.pdf](../../01_Surveys_and_Foundations/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.pdf)
- Full text: [../fulltext/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.txt](../fulltext/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41928-018-0092-2
