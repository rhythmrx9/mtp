---
id: W3003821665
key: 2020_Yao_FullyHardwareMemristorCNN_Nature
title: "Fully hardware-implemented memristor convolutional neural network"
short: "Tsinghua mCNN"
year: 2020
venue: "Nature"
venue_full: "Nature, vol. 577, pp. 641-646 (2020)"
authors: "Peng Yao, Huaqiang Wu, Bin Gao, Jianshi Tang, Qingtian Zhang, Wenqiang Zhang, J. Joshua Yang, He Qian"
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "analog-mvm", "hardware-aware-training", "write-verify-programming", "device-variation", "weight-mapping", "tiling-partitioning", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 49
cites_in_collection: 7
citations_overall: 2205
priority_score: 11.53
doi: "https://doi.org/10.1038/s41586-020-1942-4"
pdf: "../../02_Fabricated_Chips_and_Macros/2020_Yao_FullyHardwareMemristorCNN_Nature.pdf"
fulltext: "../fulltext/2020_Yao_FullyHardwareMemristorCNN_Nature.txt"
---

# Tsinghua mCNN

**Fully hardware-implemented memristor convolutional neural network** — Nature, vol. 577, pp. 641-646 (2020) (2020)

## TL;DR
First fully hardware-implemented five-layer memristor CNN: eight 2,048-cell (128x16) 1T1R TiN/TaOx/HfOx/TiN arrays with hybrid ex-situ plus FC in-situ training and replicated parallel convolvers reach 96% MNIST accuracy (95.83% in the parallel configuration) at 11,014 GOPS/W, ~110x a Tesla V100.

## Summary
Prior memristor demonstrations covered MLPs; CNNs suffer from poor array yield, device variation, drift/state locking, and a speed mismatch between sequentially sliding convolutions and parallel FC VMMs. The authors fabricate 1T1R memristor arrays in a CMOS-compatible BEOL process with 32 distinguishable conductance states (closed-loop programming with 50 ns pulses) and build a system of eight memristor PE chips on a custom PCB with FPGA, ADC, shift-add, accumulator, activation, pooling and an ARM control core. A five-layer CNN (C1: 1x3x3x8, C3: 8x3x3x12, two pooling layers, FC 192x10) is trained ex-situ in TensorFlow (97.99% software baseline), weights are rescaled to the conductance window and quantised to 15 levels, signed weights map to differential memristor pairs (positive and negative rows driven with positive and negative input pulse trains), and inputs are encoded by pulse count (8-bit). Convolutions run as memristor convolvers where each kernel is a column group and input patches slide. After transfer, only the FC layer weights are tuned in situ on a small training subset (hybrid training) to compensate mapping errors. To remove the conv/FC speed mismatch, kernels are replicated onto three parallel convolver groups, each processing one third of the image, feeding shared FC PEs. Performance is estimated from measured 130-nm devices plus the XPEsim simulator with a 128x128 core and shared 8-bit ADCs.

## Contributions
- First full memristor CNN hardware system with multiple crossbar PEs, convolution and FC layers on-chip
- Hybrid training: ex-situ conv weights plus in-situ FC tuning to absorb device variation
- Parallel convolution via weight replication across memristor arrays
- High-uniformity 1T1R array fabrication with 32 resolved conductance states

## Key claims (stable IDs)
- **2020_Yao_FullyHardwareMemristorCNN_Nature#C1** — Hybrid training recovers accuracy lost to device non-idealities — _support:_ error 4.93% -> 3.81% (single convolver); 93.86% -> 95.83% accuracy in 3-parallel-convolver setup — _loc:_ Fig. 3f, Fig. 4g, Sec. Results
- **2020_Yao_FullyHardwareMemristorCNN_Nature#C2** — >100x better energy efficiency than a GPU — _support:_ 11,014 GOPS/W and 1,164 GOPS/mm2 vs Tesla V100 (110x, 30x) — _loc:_ Sec. Results, Extended Data Tables 1-2
- **2020_Yao_FullyHardwareMemristorCNN_Nature#C3** — Scalable to ResNet — _support:_ ResNet-56 on CIFAR-10 with compact memristor model: 1.49% drop vs 95.57% software — _loc:_ Extended Data Fig. 6

## Results
- Software baseline 97.99% on MNIST; hardware >96% accuracy
- Parallel configuration error rates after hybrid training: G1 4.79->3.41%, G2 6.60->4.86%, G3 6.20->3.86%
- Weight-transfer error maps per PE group (Fig. 4b-d); training-set error 4.82% -> 3.21%
- 1,024 cells across 32 conductance states without overlap (Fig. 1c)
- Energy efficiency 11,014 GOPS/W, performance density 1,164 GOPS/mm2 (excluding pooling, activation, routing, buffering)

## Key numbers
- tech_node: 130nm (devices)
- array_size: 128x16 1T1R (2,048 cells) x 8 PEs; 128x128 macro core assumed for benchmark
- energy_eff: 11,014 GOPS/W
- throughput: 1,164 GOPS/mm2
- accuracy: >96% MNIST (95.83% parallel mCNN)
- bits_weight: 15 levels (differential pairs)
- bits_adc: 8b

## Datasets / benchmarks
MNIST, CIFAR-10 (ResNet-56, simulated)

## Limitations
- Small MNIST CNN; ResNet-56 result is simulation with a compact device model
- Efficiency comparison omits pooling, activation, routing and data buffering and uses estimated macro numbers
- Hybrid training requires fetching training data and extra memory/data-transfer modules
- Only FC weights adapted; conductance drift and state locking remain open (Extended Data Fig. 3)
- Discrete PE chips on a PCB with FPGA, not a monolithic chip; weights quantised to 15 levels

## Remarks
A landmark early demonstration of multi-array memristor CNN inference and of the partial in-situ fine-tuning idea (retrain only a late digital-readable layer to absorb mapping error), which recurs in later chip-in-the-loop work. It predates transformer or LM workloads and uses toy MNIST, so its relevance to SLMs is as a methodological ancestor of chip-in-the-loop calibration. Evidence is measured hardware with energy estimates partly simulated.

## Cites (in collection, 7)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Several experimental demonstrations (refs 4, 24-28) related to practical applications of in-memory computing have been reported as well."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Several experimental demonstrations (refs 4, 24-28) related to practical applications of in-memory computing have been reported as well."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "Several experimental demonstrations (refs 4, 24-28) related to practical applications of in-memory computing have been reported as well."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "The associated expenditure of chip area could be minimized in the future by employing high-density integration of memristors (refs 32, 33)."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _uses-method-or-tool_: "Identical SET and RESET pulse trains with a pulse width of 50 ns were employed in the closed-loop programming (ref 24) operations to reach a certain conductance state."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "Studies on memristor-based neuromorphic computing have covered a broad range of topics, from device optimization to system implementation (refs 6, 17-23)."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)

## Cited by (in collection, 49)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _motivation_: "Nonetheless, for all these implementations, custom training103–105 and/or on-chip retraining25,100 of the network is needed to mitigate the effect of defects, and device and circuit level non-ideality on the network accuracy."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "Among PIM accelerators on various memory technologies [14, 42, 43, 56, 58, 62, 66, 78], resistive-random-access-memory-(ReRAM)-based PIM (R2 PIM) accelerators have gained extensive research interest"
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _background_: "Moreover, several ReRAM-based chips have been fabricated to accelerate NN computing using Multi-Level Cells (MLCs) [7] [8]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "This involves using either arrays of capacitors [10] or resistive non-volatile memory (NVM) [11]-[18] for accelerating Multiply-ACcumulate (MAC) operations, which account for the vast majority of computations in several DNNs (see [9])."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _data/numbers_: "Some other ReRAM devices have properties that are closer to state-independent error [46, 67]."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _background_: "ReRAM crossbar is emerging as a promising solution to mitigate problems such as memory wall, owing to its high memory accessing bandwidth and high density [4, 6, 9, 10, 19–23]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _contrasts/critiques_: "In addition, voltage-based A/D converters (ADCs) are mostly used [31] that require a voltage to current conversion, usually employing a large capacitor for integration [23], [32]."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _background_: "To overcome these limitations, compute-in-memory (CIM) has been suggested as alternative hardware for CNNs because it enables parallel data processing (5–9)."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _contrasts/critiques_: "Memristor-oriented ex-situ training is indeed a very promising method of making MNNs feasible. However, it has been applied by considering only a limited number of nonidealities, while the robustness of this technique is not well understood."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "...thus eliminating power-hungry data movement between separate compute and memory2-5."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "A more complex network implantation using RRAM MVMs is presented in [171]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Early works on performing neural network inference with AIMC showed promising accuracy results in mixed hardware/software implementations, where functionalities such as digital-to-analog and analog-to-digital conversions, activation functions, and other necessary digital operations were implemented with off-chip software or hardware (refs 8-12)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "Analog-AI HW avoids these inefficiencies by leveraging arrays of non-volatile memory (NVM) to perform the ‘multiply and accumulate computation’ (MAC) operations which dominate these workloads directly in the memory3–7."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _contrasts/critiques_: "Some prior works propose using on-chip or chip-in-the-loop training methods38,43,49,55,61, which can greatly increase the attainable accuracy by addressing the specific fabrication variations found on that particular chip."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _contrasts/critiques_: "A memristor-CIM core with in-lab 32-level cell and multiple discrete components on a printed circuit board (9) has been demonstrated to classify images from the Modified National Institute of Standards and Technology database (MNIST) and the Canadian Institute for Advanced Research (CIFAR-10)."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "Read-write-verify The accuracy of conductance tuning of memristive devices could be greatly improved if the read-write-verify method is employed, which suppresses the non-linear weight update and write variation effects [16, 17, 56]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _contrasts/critiques_: "Previous works using self-designed analogue13 or MLC devices exceeding 2 bits per cell14,15 have achieved good results with relatively simple NN models and datasets; however, further assessments based on foundry-ready memristors will be required."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "As an alternative solution, memory-centric processing architectures have been emerging, specifically processing-in-memory (PIM) [48, 74, 80]."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _background_: "Among the memory types suitable for integration into advanced commercial processes, filamentary memristors have been extensively studied for analogue in-memory neural network inference7,8,23."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _data/numbers_: "However, a trade-off emerges between the technology node advancement and the achievable bit precision of memristors7,8,39,44–59, as illustrated in Fig. 2i,j."
- [2024_Qin_RoCR_ICCAD](2024_Qin_RoCR_ICCAD.md) RoCR (2024) — _data/numbers_: "The specific parameters are abstracted and then simplified from three representative NVM devices, two of them are resistive random-access memory (RRAM) devices extracted from [27, 41] and the other is a ferroelectric field effect transistor (FeFET) device extracted from [42]."
- [2025_Qin_NVCiMPT_DATE](2025_Qin_NVCiMPT_DATE.md) NVCiM-PT (2025) — _data/numbers_: "The specific parameters are abstracted and then simplified from three representative NVM devices, two of them are resistive random-access memory (RRAM) devices extracted from [29], [30], and the other is a ferroelectric field effect transistor (FeFET) device extracted from [31]."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _data/numbers_: "For the analog RRAM macros, based on noise levels reported in published RRAM chip studies [51, 52], the standard deviation of the injected Gaussian noise can be set within the range of 0.01 to 0.02."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Nikam_PassiveRRAMLSTM_TED](2021_Nikam_PassiveRRAMLSTM_TED.md) Passive RRAM LSTM (2021)
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_Wen_RRAMReadDisturb_DFT](2022_Wen_RRAMReadDisturb_DFT.md) RRAM Read Disturb (2022)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2020_Yao_FullyHardwareMemristorCNN_Nature.pdf](../../02_Fabricated_Chips_and_Macros/2020_Yao_FullyHardwareMemristorCNN_Nature.pdf)
- Full text: [../fulltext/2020_Yao_FullyHardwareMemristorCNN_Nature.txt](../fulltext/2020_Yao_FullyHardwareMemristorCNN_Nature.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41586-020-1942-4
