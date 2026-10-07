---
id: W3195461290
key: 2021_Kariyappa_NoiseResilientDNN_TED
title: "Noise-Resilient DNN: Tolerating Noise in PCM-Based AI Accelerators via Noise-Aware Training"
short: "Noise-Resilient DNN"
year: 2021
venue: "TED"
venue_full: "IEEE Transactions on Electron Devices (2021)"
authors: "Sanjay Kariyappa, Hsinyu Tsai, Katie Spoon, Stefano Ambrogio, Pritish Narayanan, Charles Mackin, An Chen, Moinuddin K. Qureshi, Geoffrey W. Burr"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["CNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["noise-injection", "conductance-drift", "hardware-aware-training", "recurrent-models"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 7
citations_overall: 46
priority_score: 8.1
doi: "https://doi.org/10.1109/ted.2021.3089987"
pdf: null
fulltext: null
---

# Noise-Resilient DNN

**Noise-Resilient DNN: Tolerating Noise in PCM-Based AI Accelerators via Noise-Aware Training** — IEEE Transactions on Electron Devices (2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes two training-time techniques -- drift regularization (DR) and multiplicative noise training (MNT) -- to make DNNs mapped onto PCM-based Analog-AI accelerators more resilient to PCM read noise and conductance drift, improving model accuracy by up to 12% after one month of drift.

## Summary
PCM-based 'Analog-AI' accelerators offer energy-efficient in-memory inference but suffer from device-inherent noise sources (read noise and long-term conductance drift) that corrupt DNN weight values stored as PCM conductances, degrading inference accuracy over time. This paper (from an IBM-affiliated author group including Ambrogio, Tsai, Narayanan, Burr et al., who are central to IBM's PCM Analog-AI research) proposes two noise-resiliency training techniques: drift regularization (DR), which regularizes training to reduce sensitivity to conductance drift, and multiplicative noise training (MNT), which injects multiplicative (rather than purely additive) noise during training to better match the statistics of PCM programming/read noise. The techniques are evaluated on convolutional networks for image classification and recurrent networks for language modeling, measuring accuracy as a function of elapsed time after programming (to capture drift effects). The combined techniques improve model accuracy by up to 12% after one month of drift compared to a non-noise-aware baseline.

## Contributions
- Proposes drift regularization (DR), a training-time regularizer targeting PCM conductance drift sensitivity
- Proposes multiplicative noise training (MNT), injecting multiplicative noise during training to better match PCM device noise statistics than standard additive noise injection
- Evaluates noise resiliency across both CNNs (image classification) and RNNs (language modeling), rather than CNNs alone
- Demonstrates accuracy improvement specifically as a function of time elapsed since weight programming, directly addressing long-term drift rather than only instantaneous read noise

## Key claims (stable IDs)
- **2021_Kariyappa_NoiseResilientDNN_TED#C1** — DR and MNT jointly improve long-term inference accuracy on PCM-based accelerators — _support:_ Up to 12% accuracy improvement over one month compared to baseline (non-noise-aware) training — _loc:_ Abstract

## Results
- Up to 12% accuracy improvement over a one-month drift period on PCM-based inference, combining drift regularization and multiplicative noise training, vs. a non-hardware-aware baseline

## Limitations
- Full text not available to this analysis (abstract-only basis); exact network architectures, datasets, drift/noise models, and baseline details could not be independently verified
- Evaluation appears simulation-based (noise/drift models applied to trained networks) rather than on physically fabricated PCM hardware, based on the abstract

## Remarks
This paper sits squarely in the hardware-aware noise-robust training literature alongside IBM's broader PCM Analog-AI line (Ambrogio et al. on drift compensation, Joshi et al. on computational PCM inference), and is cited by several later IBM Analog-AI papers (e.g., combined HW/SW drift mitigation, hardware-aware training for diverse workloads, the IBM AIHWKit paper) as an early reference for drift-aware regularization and multiplicative noise training. Because full text could not be retrieved (not on arXiv; aggregator APIs were rate-limited/blocked during this pass), this entry is abstract-only; a thesis-level treatment would benefit from obtaining the IEEE TED version to extract the specific drift model, noise injection formulation, and per-network/per-dataset accuracy-vs-time curves.

## Cites (in collection, 7)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 13)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "Drift mitigation will need a multi-pronged approach across device engineering [22], programming procedure, circuit slope correction [23] as well as algorithms, including drift-aware training approaches- [17], [24], [25]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "By subjecting the DNN to memory and circuit non-idealities during training22-25, HWA training clearly makes the DNN more resilient to the various hardware non-idealities, and significantly enhances network accuracy relative to floating-point training across the board."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "Prior work includes iso-accuracy studies for convolutional neural networks (CNNS) [16, 17, 18], recurrent neural networks (RNNs) [19, 17] and transformers [20]."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _uses-method-or-tool_: "To make the network more resilient to analog noise23–26, we retrained it while including weight and"
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _baseline/comparison_: "A few previous studies have attempted to improve the robustness of DNNs to nonidealities by noise-aware training, where multiplicative or additive Gaussian noise38,41 is added to weights or activations during training."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "These are added to increase the model robustness 21,22,55–59 , and can be specified using different RPUConfig parameters (as part of the InferenceRPUConfig class), which are discussed in the following subsections."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "Hardware-out-of-the-loop (HOL) methods, such as noise-injected training116 and quantization-aware training117, incorporate a hardware non-ideality model into the training loop to enhance robustness."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _contrasts/critiques_: "Previous works that study HWA training for AIMC-based hardware are limited to CNNs [35, 48, 49], RNNs [37], LSTMs [37, 49, 50], GANs [51] and small encoder-only transformers [37, 52]."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _contrasts/critiques_: "Prior studies on the impact of memory characteristics on AI tasks mostly focus on individual non-ideality [6, 10, 13], such as the effect of memory window or conductance drift on the inference accuracy."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2021_Kariyappa_NoiseResilientDNN_TED.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/ted.2021.3089987
