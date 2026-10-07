---
id: W3013080934
key: 2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol
title: "Memory devices and applications for in-memory computing"
short: "Sebastian IMC Review"
year: 2020
venue: "NatNanotechnol"
venue_full: "Nature Nanotechnology, vol. 15, pp. 529-544 (2020)"
authors: "Abu Sebastian, Manuel Le Gallo, Riduan Khaddam-Aljameh, Evangelos S. Eleftheriou"
category: "01 Surveys & Foundations"
devices: ["SRAM-analog", "DRAM", "Flash", "ReRAM", "PCM", "MRAM", "FeFET"]
models: ["MLP", "CNN", "LSTM/RNN", "SNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "analog-mvm", "bit-slicing", "weight-mapping", "adc-dac", "peripheral-circuits", "on-chip-training", "device-variation", "conductance-drift", "mixed-precision"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 53
cites_in_collection: 16
citations_overall: 2277
priority_score: 13.04
doi: "https://doi.org/10.1038/s41565-020-0655-z"
pdf: "../../01_Surveys_and_Foundations/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.pdf"
fulltext: "../fulltext/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.txt"
---

# Sebastian IMC Review

**Memory devices and applications for in-memory computing** — Nature Nanotechnology, vol. 15, pp. 529-544 (2020) (2020)

## TL;DR
IBM Zurich Nature Nanotechnology review of charge-based (SRAM/DRAM/Flash) and resistance-based (RRAM/PCM/MRAM) memories for in-memory computing: computational primitives (logic, MVM, bit slicing, mixed-precision), applications from linear solvers to DNN inference/training, SNNs and stochastic computing, with a Table of chip-level DNN-inference demos reporting >=10 TOPS/W.

## Summary
The review defines in-memory computing as computation inside a computational-memory unit (devices, array organisation, periphery, control) and contrasts it with near-memory computing. It surveys charge-based devices (SRAM, DRAM, Flash) and resistive devices (RRAM, PCM, MRAM) and the primitives they enable: logic, associative/content-addressable operations, and analog MVM via Ohm's and Kirchhoff's laws. Precision techniques are covered: bit slicing with shift-and-add reduction, and mixed-precision iterative refinement (5,000 linear equations solved using 998,752 PCM devices). In the deep-learning section a DNN is mapped layer-per-crossbar across multiple arrays connected by an on-chip network, with nonlinearities at the periphery; differential device pairs encode signed weights and bit slicing raises precision. Table 1 lists chip-level inference demos (SRAM 65nm 139-658 TOPS/W at 1-bit, Flash, RRAM macros ~10-11 TOPS/W). Training approaches (parallel pulse outer-product update vs mixed analog/digital update with digital accumulation), SNNs/STDP, stochastic computing and PUFs follow. The outlook discusses device challenges (write variability, PCM drift, projected PCM), ADC/DAC requirements (>=4 bits needed), hierarchical core architectures and software stack. No language models are discussed.

## Contributions
- Taxonomy of charge-based versus resistance-based memory devices for in-memory computing and their computational primitives
- Overview of precision-enhancing schemes (bit slicing, mixed-precision iterative refinement, differential pairs)
- Table 1 of chip-level inference demonstrations with technology node, precision, accuracy and TOPS/W
- Discussion of DNN training styles on crossbars and of challenges in devices, peripherals and system architecture

## Key claims (stable IDs)
- **2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol#C1** — State-of-the-art chip demos of IMC DNN inference report >=10 TOPS/W for reduced-precision MVM, but all need custom training and/or on-chip retraining to cope with non-idealities. — _support:_ 'custom training and/or on-chip retraining of the network is needed to mitigate the effect of defects, and device and circuit level non-ideality' — _loc:_ Deep learning section; Table 1
- **2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol#C2** — At least four bits (including sign) ADC precision has so far been needed for DNN inference. — _support:_ refs 21, 22, 98 — _loc:_ Opportunities, challenges and perspective
- **2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol#C3** — Mixed-precision IMC solved a 5,000-equation system with ~1M PCM devices at arbitrary accuracy, but needs data stored in both crossbar and digital memory. — _support:_ 998,752 PCM devices (ref 64) — _loc:_ Computational primitives / Applications
- **2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol#C4** — Digitally accumulated weight updates relax device granularity and endurance requirements versus parallel overlapping-pulse updates. — _support:_ ref 116 (Nandakumar mixed-precision training) — _loc:_ Deep learning: training

## Results
- Table 1 lists SRAM-based IMC chips in 65nm with ~139 and 658 TOPS/W (1-bit) and nvm chips (Flash, RRAM) at ~10-11 TOPS/W (Table text garbled in extraction; values as listed)
- Mixed-precision linear solver: 5,000 equations with 998,752 PCM devices
- SRAM IMC demonstrations: >100 TOPS/W for 1-bit arithmetic

## Key numbers
- tech_node: 65nm (SRAM chips in Table 1)
- energy_eff: >=10 TOPS/W NVM; up to 658 TOPS/W 1-bit SRAM
- bits_adc: >=4 bits needed for inference

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Review, no unified benchmark; chip comparison depends on differing precisions and operation counting (1 MAC = 2 OPs)
- Published 2020: no transformer or language-model coverage
- Table 1 values are partly garbled in the text extraction
- Broad scope gives limited depth on architecture/mapping

## Remarks
Arguably the standard general IMC review for the charge- vs resistance-based taxonomy and IBM's PCM viewpoint (drift, mixed precision, hardware-aware training). For a thesis on mapping models onto analog crossbars it is the best single overview to cite, complemented by circuit/architecture-oriented reviews and silicon-macro surveys. Its statement that every chip demo needs hardware-aware or on-chip retraining anticipates later work on noise-robust training of language models.

## Use in the original review
- F15 (High confidence): The shared motivation across this literature is the memory wall: data movement between separate processing and memory units is the dominant time and energy cost in von Neumann systems, aggravated by data-centric AI workloads. In-memory computing computes in place inside the array by exploiting device physics; two-terminal resistive switching devices are the favoured substrate.

## Cites (in collection, 16)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Another approach is a mixed analogue/digital weight update whereby ∆Wij is computed digitally and applied to the arrays row-by-row or column-by-column (Fig. 6c). ∆Wij can be applied either at every individual training example (online training) or batch of training examples113–115."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "One approach is to perform a parallel weight update by sending deterministic or stochastic overlapping pulses from the rows and columns simultaneously to implement an approximate outer product and program the devices at the same time (Fig. 6b)107–111."
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _extends/builds-on_: "The adaptation of this concept for in-memory computing and experimental demonstration of solving a system of 5,000 linear equations using 998,752 PCM devices with arbitrarily high accuracy was presented in ref. 64."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "This results in stringent requirements on the device granularity, asymmetry and linearity to obtain accurate training109,112, and high device endurance is critical."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "Using multiple devices per synapse with a periodic carry can relax some of the device requirements, at the price of a costly reprogramming of the entire array every time the carry is performed110,111."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "Another approach is a mixed analogue/digital weight update whereby ∆Wij is computed digitally and applied to the arrays row-by-row or column-by-column (Fig. 6c). ∆Wij can be applied either at every individual training example (online training) or batch of training examples113–115."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "There is significant on-going research on defining such hierarchical organizations of in-memory computing cores to tackle a range of applications58,167,168."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _background_: "For digitizing the crossbar output, most works have employed analogue-to-digital converters (ADCs)21,22 or sense amplifiers98."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _motivation_: "Nonetheless, for all these implementations, custom training103–105 and/or on-chip retraining25,100 of the network is needed to mitigate the effect of defects, and device and circuit level non-ideality on the network accuracy."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "This approach is more flexible than the parallel weight update based on overlapping pulses because it can implement any learning rule, not only stochastic gradient descent, and the digital computation and accumulation of weight updates significantly relax the requirements on the device granularity and endurance116."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018)
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 53)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _background_: "One promising future technology is the use of memristive crossbar arrays for accelerating the ubiquitous matrix-vector multiply and rank-update operations in ANNs by employing in-memory computation of matrices stored as analog quantities in tunable resistive elements [1,7,8,13]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "In situ MVM has been demonstrated using a wide variety of memory cell technologies [55, 61, 68]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "In-memory computing (IMC) is an emerging non-von Neumann paradigm where computation is performed in the memory array itself [1], [2]."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _background_: "To overcome these limitations, compute-in-memory (CIM) has been suggested as alternative hardware for CNNs because it enables parallel data processing (5–9)."
- [2022_Lin_DNAT_JETCAS](2022_Lin_DNAT_JETCAS.md) D-NAT (2022) — _background_: "Recently, computingin-memory (CIM) [5, 6] mechanism has been proposed as a promising solution to the von-Neumann bottleneck through the integration of computational units and memories."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "Introducing such redundancy has been shown to offer accuracy benefits by effectively countering some of the variability present in analogue memory26,37,38."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _background_: "Several demonstrations of AIMC-based architectures have appeared in the field of Deep Neural Network (DNN) inference acceleration, showing outstanding peak energy efficiency in the order of hundreds of TOPS/W [1, 2]."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "With analog in-memory computing (AIMC) certain computations directly take place where the data is located, exploiting device physics and circuit laws [5]."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "In-Memory Computing (IMC) systems, such as analog crossbar-arrays that alleviate the ‘memory-wall’ bottleneck of von-Neumann architectures are gaining popularity [21]."
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _background_: "In recent years, Analog InMemory Computing (AIMC) has been a widely studied computing paradigm since it promises outstanding performance and energy efficiency on MVM operations [1]."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _background_: "It uses emerging non-volatile memory technologies such as memristors, also called resistive random access memories (RRAMs), which are highly scalable and compatible with CMOS technology [11]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _background_: "Analog IMC [1] can provide radical improvements in performance and power efficiency, by leveraging the physical properties of memory devices to perform computation and storage at the same physical location."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "In addition to traditional digital accelerators, including the Google Tensor Processing Unit, Amazon Inferentia, and IBM Artificial Intelligence Unit1 , accelerators based on Analog In-Memory Computing (AIMC) using Non-Volatile Memory (NVM) are being actively researched2–4 ."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: ""To avoid this loss of accuracy, hardware-aware training methods, in which device non-idealities are incorporated during training have been proposed in the literature." (co-cited with Joshi et al. computational PCM paper)"
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _background_: "Analog-Based In-Memory Computing (AIMC) accelerators are one such type of accelerator, which have gained significant interest, due to their ability to execute Vector-Matrix Multiplications (VMMs) in O (1) time-complexity [6–8]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Analog in-memory computing AIMC is a promising future hardware technology for accelerating deep-learning workloads. Great energy efficiency is achieved by representing weight matrices in resistive elements of crossbar arrays and using basic physical laws of electrostatics (Kirchhoff's and Ohm's laws) to compute ubiquitous matrix-vector multiplications (MVMs) directly in memory in essentially constant time O(1)1-5."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _background_: "Memristor crossbars are widely considered strong competitors for traditional machine learning accelerators [3]."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _motivation_: "Therefore, a compiler that can adapt to various PIM architectures and automatically complete DNN model deployment is indispensable to improve the usability of PIM accelerators, which also helps build a PIM ecosystem [11]."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _background_: "A promising alternative to the von-Neumann architecture that has risen in popularity is in-memory computing using non-volatile memory (NVM) devices18-21."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _background_: "One such compute substrate which shows significant promise for adversarial robustness is that based on analog in-memory computing (AIMC)6–8."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _background_: "There are a broad range of DPU types, from general-purpose core-based units that accelerate a wide range of operations to more specialized units, for certain specific operations, that are optimized for lower latency9,13,29."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _background_: "IMC is particularly beneficial when using non-volatile memories to store stationary weights in linear layers22."
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _background_: "Compute-In-Memory (CIM) neural network accelerators have emerged as promising architectures for achieving energyefficient AI processing [2–6]."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "IMC inference chips consist of multiple IMC tiles9 (Fig. 1c)."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "Analog devices are inherently non-deterministic and subject to temporal variations, impacting NN accuracy when deployed on AIMC-based accelerators7–10."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _background_: "By reducing data movement, AIMC can deliver significant improvements in energy efficiency and throughput, making it attractive for both resource-constrained edge devices and high-performance data centers [1, 2]."
- [2025_Xu_UniCAIM_DAC](2025_Xu_UniCAIM_DAC.md) UniCAIM (2025) — _background_: "In recent years, various emerging NVMs, such as resistive random-access memory (RRAM), magnetic tunnel junction (MTJ) and FeFET, have triggered lots of attention for CIM, due to the high storage density and efficient GEMV operation via analog computing within the memory array [26-28]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _background_: "The crossbars carry out MVM operations in parallel, applying Kirchhoff’s and Ohm’s Laws for analog computation [14, 16]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "They may be designed using a range of emerging devices, including Resistive RAM (ReRAM), Phase Change Memory (PCM), and Spintronics [3–6]."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _uses-method-or-tool_: "To accomplish 8-bit precision, we rely on the bit-slicing technique, which allows increasing accuracy by combining modules of smaller bit width [7]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "A Reconfigurable 4T2R ReRAM Computing In-Memory Macro on a 40 nm process [67] utilized a 4T2R cell, which allowed for row-wise memory access."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "Recent work from Samsung has shown a 64 x 64 cross-bar array of STT-MRAMs integrated with 28nm CMOS technology to realize in-memory computing [164]."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _data/numbers_: "The crossbar energy, delay and area values are obtained based on IMC implementations of SRAM and FeFET crossbars of size 64x64 [33], [40]."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "Analog in-Memory Computing (AIMC) addresses both compute efficiency and data movement by performing fully-parallel Matrix-Vector Multiplications (MVMs) in the analog domain [13, 14] on stored weight matrices, without having to move the weight data to an external processor (see figure 1)."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _background_: "Crossbar-based VMM Computing Engine RRAM is an emerging non-volatile memory technology with strong potential for accelerating VMMs when arranged in crossbar arrays [19]."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _motivation_: "While the RRAM-only strategy suffers from inherent noise and complex write-verify operations [40], the SRAM-only strategy is limited by its volatility and low storage density [41]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Nikam_PassiveRRAMLSTM_TED](2021_Nikam_PassiveRRAMLSTM_TED.md) Passive RRAM LSTM (2021)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024)
- [2023_Parvaresh_NlpAimcResilience_NANOARCH](2023_Parvaresh_NlpAimcResilience_NANOARCH.md) NLP-AIMC (2023)
- [2026_Suzuki_KVCacheSLCMLC_JJAP](2026_Suzuki_KVCacheSLCMLC_JJAP.md) KVCacheSLCMLC (2026)

## Files
- PDF: [../../01_Surveys_and_Foundations/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.pdf](../../01_Surveys_and_Foundations/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.pdf)
- Full text: [../fulltext/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.txt](../fulltext/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41565-020-0655-z
