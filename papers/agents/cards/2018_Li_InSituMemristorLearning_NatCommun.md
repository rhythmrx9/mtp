---
id: W2807750997
key: 2018_Li_InSituMemristorLearning_NatCommun
title: "Efficient and self-adaptive in-situ learning in multilayer memristor neural networks"
short: "Li In-situ Memristor Learning"
year: 2018
venue: "NatCommun"
venue_full: "Nature Communications"
authors: "Can Li, Daniel Belkin, Yunning Li, Peng Yan, Miao Hu, Ning Ge, Hao Jiang, Eric Montgomery, Peng Lin, Zhongrui Wang, Wenhao Song, John Paul Strachan et al."
category: "10 On-chip & Analog Training"
devices: ["ReRAM", "Memristor(generic)"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["on-chip-training", "chip-demo", "analog-mvm", "write-verify-programming", "stuck-at-faults", "device-variation", "hardware-aware-training"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 22
cites_in_collection: 4
citations_overall: 935
priority_score: 8.26
doi: "https://doi.org/10.1038/s41467-018-04484-2"
pdf: "../../10_On_Chip_and_Analog_Training/2018_Li_InSituMemristorLearning_NatCommun.pdf"
fulltext: "../fulltext/2018_Li_InSituMemristorLearning_NatCommun.txt"
---

# Li In-situ Memristor Learning

**Efficient and self-adaptive in-situ learning in multilayer memristor neural networks** — Nature Communications (2018)

## TL;DR
First multilayer in-situ trained memristor network on a 128x64 Ta/HfO2/Pt 1T1R array integrated on a foundry transistor array: a 64-54-10 MLP trained with online SGD reaches 91.71% MNIST (8x8) despite 11% unresponsive devices, and simulation of a 1024x512 array projects 97.3%.

## Summary
In-situ learning on a multilayer memristor network had not been shown at scale because of conductance nonlinearity, variation and circuit integration. The authors monolithically integrate Ta/HfO2/Pt memristors with a foundry-made transistor array (1T1R, 6-inch wafer). A two-pulse programming scheme uses the series transistor's gate voltage to set the compliance current, giving linear, symmetric conductance increase/decrease with small cycle-to-cycle and device-to-device variation; the whole 128x64 array can be set (except stuck devices) to reasonable accuracy with two pulses per device. Each weight is the conductance difference of two memristors (inputs duplicated with negative polarity), and during inference transistors operate in the deep triode region so the array behaves as a pseudo-crossbar computing sums by Ohm and Kirchhoff laws. A two-layer perceptron (64 inputs from 8x8 downsampled MNIST, 54 hidden, 10 outputs, 7,992 memristors in one partitioned array) is trained with SGD, minibatch 50, 1,600 cycles over 80,000 samples. Forward MVMs, readout and weight programming run on the chip with custom circuit boards (64 parallel channels), while ReLU, backpropagation error computation (Eq. 2) and weight-update calculation (Eq. 1) are in software; the update is applied by the measurement system. A simulator calibrated with the measured unresponsive rate, update error and dynamic range reproduces the experiment, then predicts larger arrays and defect sensitivity.

## Contributions
- Monolithic integration of HfOx memristors with foundry transistors into a multilayer network on one 128x64 array
- Two-pulse transistor-compliance programming giving linear, symmetric conductance tuning
- In-situ online SGD training experiment (91.71% MNIST with 11% defective devices)
- Calibrated simulation of defect tolerance, deeper/larger networks (97.3%) and ex-situ vs in-situ comparison

## Key claims (stable IDs)
- **2018_Li_InSituMemristorLearning_NatCommun#C1** — In-situ trained 2-layer memristor MLP achieves 91.71% on 10,000 MNIST test images — _support:_ 8x8 inputs, 64-54-10, 7,992 memristors, 80,000 training samples — _loc:_ Fig. 3 / Results
- **2018_Li_InSituMemristorLearning_NatCommun#C2** — Training adapts to defects: >60% accuracy even with 50% of devices stuck low in simulation, whereas ex-situ loaded weights degrade quickly — _support:_ 11% unresponsive devices in experiment; Fig. 4b — _loc:_ Fig. 4b
- **2018_Li_InSituMemristorLearning_NatCommun#C3** — Larger arrays approach digital accuracy — _support:_ 1024x512 simulation, 484-502-10, 495,976 memristors, 97.3 +/- 0.4% with 11% stuck devices — _loc:_ Results / Fig. 4d
- **2018_Li_InSituMemristorLearning_NatCommun#C4** — Experiment is 2.4% below idealized simulation — _support:_ 91.71% measured — _loc:_ Discussion

## Results
- 91.71% test accuracy on MNIST (8x8) with 11% devices unresponsive
- Simulated 22x22 MNIST on 1024x512 array: 97.3 +/- 0.4% after 1.2M images (20 epochs)
- Two-layer network more defect-tolerant than single-layer on same images (Fig. 4c)
- Online training can compensate drift (Supplementary Fig. 13); speed-energy gains projected rather than measured

## Key numbers
- tech_node: foundry transistor array, Ta/HfO2/Pt memristors
- array_size: 128x64 1T1R (7,992 memristors used)
- accuracy: 91.71% MNIST (8x8), 97.3% simulated 1024x512
- bits_weight: analog (differential pair)

## Datasets / benchmarks
MNIST (8x8 downsampled)

## Limitations
- Small network, downsampled 8x8 MNIST; no CNN/LSTM/transformer
- Backpropagation error and weight updates computed in software; activation in software; external control electronics not optimised
- Speed and energy efficiency advantages only argued, not measured
- Sensitive to shorted devices (Supplementary Fig. 12)

## Remarks
Landmark experimental demonstration (935+ citations) that on-chip training can self-compensate for stuck and variable devices, which is the main argument for chip-in-the-loop and on-chip adaptation in later work. It is far from language-model scale: the array holds under 8k synapses. Relevant to LMs only as precedent for hardware-adaptive training of tiny fully-connected layers; compare with PCM-based training (Ambrogio) and 165k-synapse PCM work in the collection.

## Cites (in collection, 4)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _motivation_: "However, experimental demonstrations to date have been limited to discrete devices24,25 or small arrays and simplified problems26-31."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _motivation_: "However, experimental demonstrations to date have been limited to discrete devices24,25 or small arrays and simplified problems26-31."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _background_: "While the external control electronics we use in this work is not optimized for fast speed and low power consumption yet, previous literature on circuit design45,51 and architecture21,53 suggest an on-chip integrated system would yield significant advantages in speed-energy efficiency."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _contrasts/critiques_: "There are approaches to improve the robustness of ex situ training19,38, but most of them require that the parameters be tuned based on specific knowledge of the hardware (e.g., peripheral circuitry) and memristor array (e.g., device defects, wire resistance, etc.), while the in situ training adapts the weights and compensates them automatically."

## Cited by (in collection, 22)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _data/numbers_: "This has been experimentally confirmed recently17, implying that memristors with their intrinsic noise might be more suitable for neural computing rather than memory or storage applications."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _background_: "Although here we focus on ex-situ training, such systems have been successfully utilised for in-situ training too [10, 11]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _uses-method-or-tool_: "Identical SET and RESET pulse trains with a pulse width of 50 ns were employed in the closed-loop programming (ref 24) operations to reach a certain conductance state."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Another approach is a mixed analogue/digital weight update whereby ∆Wij is computed digitally and applied to the arrays row-by-row or column-by-column (Fig. 6c). ∆Wij can be applied either at every individual training example (online training) or batch of training examples113–115."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _contrasts/critiques_: "The general way is to use two ReRAM crossbars to hold the positive and negative magnitudes weights separately, doubling the ReRAM portion of hardware cost [17, 25-28]."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _background_: "The analog conductance modulation characteristics of two-terminal devices are usually achieved by controlling the current of devices during the programming process (22–24)."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _data/numbers_: "Fabrication process is described in more detail in [48]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "the most competitive candidates at present among emerging memories are resistive random-access memory (RRAM) [76] [77] [78] [79] [80] [81] [82] [83] [84] [37]..."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _contrasts/critiques_: "First, on-chip training inherently adapts the weights to conductance variation as the network is trained on the CIM chip [13], [14]. However, it is not scalable due to individual training necessity for each chip, high energy consumption, and endurance issues."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "The weight updates are performed in the memristive array after a single batch of training samples is processed [19–21]."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "Substantial progress has been made in developing analogue CIM chips for AI, evolving from initial proof-of-concept arrays5 to board-level integrated systems6–9 and recently achieving full system-on-chip integration10,11."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022)
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022)
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Ahsan_SPICEenvmACIMFramework_ICCAD](2024_Ahsan_SPICEenvmACIMFramework_ICCAD.md) SPICE eNVM ACIM Framework (2024)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2018_Li_InSituMemristorLearning_NatCommun.pdf](../../10_On_Chip_and_Analog_Training/2018_Li_InSituMemristorLearning_NatCommun.pdf)
- Full text: [../fulltext/2018_Li_InSituMemristorLearning_NatCommun.txt](../fulltext/2018_Li_InSituMemristorLearning_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-018-04484-2
