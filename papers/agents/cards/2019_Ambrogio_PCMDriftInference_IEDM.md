---
id: W3005874416
key: 2019_Ambrogio_PCMDriftInference_IEDM
title: "Reducing the Impact of Phase-Change Memory Conductance Drift on the Inference of large-scale Hardware Neural Networks"
short: "PCM Drift Inference"
year: 2019
venue: "IEDM"
venue_full: "2019 IEEE International Electron Devices Meeting (IEDM 2019)"
authors: "Stefano Ambrogio, M. Gallot, Katherine Spoon, Hsinyu Tsai, Charles Mackin, M. Wesson, Sanjay Kariyappa, Pritish Narayanan, ChenKang Liu, Arvind Kumar, A. Chen, Geoffrey W. Burr"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["PCM"]
models: ["MLP", "ResNet", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["conductance-drift", "device-variation", "read-write-noise", "hardware-aware-training"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 16
cites_in_collection: 1
citations_overall: 76
priority_score: 7.5
doi: "https://doi.org/10.1109/iedm19573.2019.8993482"
pdf: null
fulltext: null
---

# PCM Drift Inference

**Reducing the Impact of Phase-Change Memory Conductance Drift on the Inference of large-scale Hardware Neural Networks** — 2019 IEEE International Electron Devices Meeting (IEDM 2019) (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IBM builds a statistical PCM conductance-drift model (including cycle-to-cycle variability of the drift coefficient nu) from large-array measurements, quantifies long-term accuracy loss for MLP, ResNet-10/18/34 and LSTM inference, and proposes slope correction plus DNN-architecture choices to suppress it.

## Summary
Phase-change memory conductance drifts over time (G ~ t^-nu), which degrades the accuracy of pre-trained DNNs whose weights are stored as PCM conductances. Starting from large-array characterisation of drift in partial-SET states, the authors build a statistical drift model that captures the empirically observed cycle-to-cycle variability of the drift coefficient nu. They simulate MLPs on MNIST, ResNet-10/18/34 on CIFAR-10 and a 2-layer LSTM on 'Alice in Wonderland' to show how drift plus nu-variability causes long-term accuracy degradation. Mitigations include 'slope correction' (compensating the average drift-induced scaling of outputs) and DNN architecture choices (squashing function, number of hidden units, hidden layers or convolution filters). They also show that 1/f noise, random telegraph noise and device-to-device heater-diameter variability complicate accurate drift measurement.

## Contributions
- Statistical PCM drift model from large-array partial-SET measurements including cycle-to-cycle nu variability
- Assessment of drift impact on MLP, ResNet-10/18/34 and LSTM inference
- Slope correction technique to compensate average drift
- DNN design guidelines (activation choice, width/depth, filter count) for drift tolerance
- Analysis of how 1/f noise, RTN and heater-diameter variability affect drift measurement

## Key claims (stable IDs)
- **2019_Ambrogio_PCMDriftInference_IEDM#C1** — The combination of drift and nu-variability causes long-term DNN accuracy degradation. — _support:_ Characterised across MLP/MNIST, ResNet/CIFAR-10 and LSTM workloads — _loc:_ Abstract
- **2019_Ambrogio_PCMDriftInference_IEDM#C2** — Slope correction and architectural choices can suppress drift-induced degradation. — _support:_ Stated in abstract; magnitudes not available — _loc:_ Abstract
- **2019_Ambrogio_PCMDriftInference_IEDM#C3** — Noise sources (1/f, RTN) and heater-diameter variability complicate accurate drift measurement. — _support:_ Stated in abstract — _loc:_ Abstract

## Results
- Drift + nu-variability degrades accuracy over time for MLP (MNIST), ResNet-10/18/34 (CIFAR-10) and 2-layer LSTM (abstract; numbers not available)
- Slope correction and network design choices mitigate the degradation (abstract)

## Limitations
- Abstract-only analysis; no quantitative accuracy-vs-time numbers verified
- Network-level results are simulations using a device-calibrated model, not on-chip inference
- Small-to-mid-size workloads (CIFAR-10 ResNets, small LSTM)
- Slope correction compensates mean drift but not the nu-variability-induced spread

## Remarks
A foundational IBM paper for drift-aware PCM inference: its statistical drift model and slope (global drift) correction underlie later IBM work, including the AIHWKit inference noise model, hardware-aware training studies and the 14nm analog chip demonstrations, many of which cite it in this collection. Its key lesson for mapping is that drift is mostly a correctable global scaling, while nu-variability sets the residual accuracy floor, motivating periodic recalibration and drift-robust training.

## Cites (in collection, 1)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)

## Cited by (in collection, 16)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "Drift mitigation will need a multi-pronged approach across device engineering [22], programming procedure, circuit slope correction [23] as well as algorithms, including drift-aware training approaches- [17], [24], [25]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _uses-method-or-tool_: "As mentioned earlier, this can be mitigated using a drift compensation technique32, where activations are amplified close to their original levels using drift compensation factor alpha, which may or may not be uniform along the column-wise dimension of the crossbar array."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "For evaluation times teval long after NVM programming, the conductance drift Eq. (8) can be compensated in the digital domain without any expensive re-programming36,73."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _motivation_: "These inherent characteristics limit their accuracy and reliability to use in practical deep learning workloads18–20 ."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "Read noise and conductance drift in long term could also degrade the accuracy of MAC calculation [35, 36]."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _background_: "PCM conductance drift effect and mitigation As the amorphous phase within programmed PCM devices relaxes, device-conductances decrease logarithmically over time38."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _background_: "Device engineering [36] and circuit-device co-design [37] can further alleviate effects, which is out of the scope of this work."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _contrasts/critiques_: "Prior studies on the impact of memory characteristics on AI tasks mostly focus on individual non-ideality [6, 10, 13], such as the effect of memory window or conductance drift on the inference accuracy."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2019_Ambrogio_PCMDriftInference_IEDM.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iedm19573.2019.8993482
