---
id: W2803163155
key: 2018_Ambrogio_PCUAnalogueMemoryTraining_Nature
title: "Equivalent-accuracy accelerated neural-network training using analogue memory"
short: "PCM+Capacitor Analog Training"
year: 2018
venue: "Nature"
venue_full: "Nature, vol. 558, 2018"
authors: "Stefano Ambrogio, Pritish Narayanan, Hsinyu Tsai, Robert M. Shelby, Irem Boybat, Carmelo di Nolfo, Severin Sidler, Massimo Giordano, Martina Bodini, Nathan C. P. Farinha, Benjamin D. Killeen, Christina Cheng et al."
category: "10 On-chip & Analog Training"
devices: ["PCM", "Charge/Capacitor"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["on-chip-training", "analog-mvm", "calibration-compensation", "device-variation"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 34
cites_in_collection: 2
citations_overall: 1150
priority_score: 8.86
doi: "https://doi.org/10.1038/s41586-018-0180-5"
pdf: null
fulltext: null
---

# PCM+Capacitor Analog Training

**Equivalent-accuracy accelerated neural-network training using analogue memory** — Nature, vol. 558, 2018 (2018)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Mixed hardware-software training with up to 204,900 synapses (PCM for long-term storage, capacitors for near-linear updates, polarity inversion) reaches software-equivalent accuracy on MNIST, MNIST-backrand, CIFAR-10 and CIFAR-100.

## Summary
In-situ training on analog NVM had lagged software accuracy because of limited dynamic range and asymmetric weight updates. Ambrogio et al. pair a non-volatile PCM conductance pair (long-term storage) with a volatile capacitor-based 3T1C cell (near-linear, symmetric updates) in each synapse. Accumulated updates are periodically transferred to the PCM, using "polarity inversion" to cancel device-to-device variations. The mixed hardware-software experiments use up to 204,900 synapses and reach generalization accuracy equivalent to software training on MNIST, MNIST-backrand, CIFAR-10 and CIFAR-100. The authors project 28,065 GOPS/W and 3.6 TOPS/mm² for the design, about two orders of magnitude better than contemporary GPUs, mainly for fully connected layers.

## Contributions
- Two-tier synapse: volatile capacitor for linear updates plus PCM pair for non-volatile storage
- Polarity inversion to cancel device-to-device variations on weight transfer
- Software-equivalent in-situ training accuracy on four datasets with up to 204,900 synapses
- Energy and area-throughput projections against GPUs

## Key claims (stable IDs)
- **2018_Ambrogio_PCUAnalogueMemoryTraining_Nature#C1** — Analog in-situ training can reach software-equivalent generalization accuracy. — _support:_ Equivalent accuracy on MNIST, MNIST-backrand, CIFAR-10 and CIFAR-100 (transfer-learning setting for CIFAR) — _loc:_ Abstract
- **2018_Ambrogio_PCUAnalogueMemoryTraining_Nature#C2** — Combining volatile linear-update elements with non-volatile PCM storage overcomes update asymmetry and limited dynamic range. — _support:_ 3T1C capacitor + PCM pair synapse with polarity inversion — _loc:_ Abstract
- **2018_Ambrogio_PCUAnalogueMemoryTraining_Nature#C3** — The design is two orders of magnitude more efficient than GPUs. — _support:_ 28,065 GOPS/W and 3.6 TOPS/mm² (calculated, not measured end-to-end) — _loc:_ Abstract

## Results
- Up to 204,900 synapses in mixed hardware-software experiments
- Software-equivalent accuracy on MNIST, MNIST-backrand, CIFAR-10, CIFAR-100
- Projected 28,065 GOPS/W and 3.6 TOPS/mm²

## Limitations
- Mixed hardware-software: parts of the network/periphery emulated in software.
- Efficiency figures are calculated projections.
- Fully connected layers; CIFAR results rely on transfer learning with fixed conv features.
- Summary based on the abstract; the full text was not available here.

## Remarks
A landmark for analog training (category 10). It shows a device-level trick (multi-tier synapse) can close the accuracy gap that pure NVM updates cannot. It anchors the IBM line that leads to HERMES and the 14 nm chips. Its projected efficiency should not be compared with measured chip TOPS/W.

## Cites (in collection, 2)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)

## Cited by (in collection, 34)
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "One potential solution to this problem is to train the network fully on hardware9,10, such that all hardware non-idealities would be de facto included as constraints during training."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _background_: "Memristive devices, such as phase-change memories (PCMs) [6, 7] or resistive random-access memories (RRAMs) [8, 9], have been considered as candidates for such tasks."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Several experimental demonstrations (refs 4, 24-28) related to practical applications of in-memory computing have been reported as well."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "To this effect, researchers have explored Non Volatile Memory (NVM) [4, 5] based crossbar architectures to achieve higher on-chip storage density and efficient MVMs in the analog domain [6, 7]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Using multiple devices per synapse with a periodic carry can relax some of the device requirements, at the price of a costly reprogramming of the entire array every time the carry is performed110,111."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "In fact, researchers have been successful in experimentally demonstrating large-scale PCM crossbars for ML applications [21, 43]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "This involves using either arrays of capacitors [10] or resistive non-volatile memory (NVM) [11]-[18] for accelerating Multiply-ACcumulate (MAC) operations, which account for the vast majority of computations in several DNNs (see [9])."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _background_: "In this specific case, an alternative of faulty-devices [27] or line resistance [28]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _motivation_: "This approach was recently shown capable of 280x speedup in per-area throughput while providing 100x enhancement in energy-efficiency over state-of-the-art GPUs4."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "...thus eliminating power-hungry data movement between separate compute and memory2-5."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "There have been an increasing number of experimental studies of all analog CIM that involve inference as well as training [58] [25] [53]."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "Analog in-memory computing (analog-AI)3–7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "Although some promising, small-sized DNN prototype demonstrations exist43–49, it remains unclear how robust the AIMC deployment of realistically sized AI workloads will be."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "Ambrogio et al proposed to use memristive devices as the high significant weights and capacitor-based artificial synapses as the low significant weights [58–60]."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _contrasts/critiques_: "Previous works using self-designed analogue13 or MLC devices exceeding 2 bits per cell14,15 have achieved good results with relatively simple NN models and datasets; however, further assessments based on foundry-ready memristors will be required."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _contrasts/critiques_: "For example, a fully analogue solution based on a synaptic unit cell combining non-volatile phase change memory (PCM) with conventional CMOS-based capacitors (the PCM array was fabricated and the CMOS capacitors were simulated) has been explored16."
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2022_GarciaRedondo_SACA_DCIS](2022_GarciaRedondo_SACA_DCIS.md) SACA (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022)
- [2026_Sharma_HatFi_VTS](2026_Sharma_HatFi_VTS.md) HATFI (2026)

## Files
- PDF: not available locally (save as `papers/10_On_Chip_and_Analog_Training/2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.pdf`)
- Full text: none
- DOI: https://doi.org/10.1038/s41586-018-0180-5
