---
id: W3003151806
key: 2019_Nandakumar_PCMDeviceModels_ICECS
title: "Phase-Change Memory Models for Deep Learning Training and Inference"
short: "PCM Device Models"
year: 2019
venue: "ICECS"
venue_full: "IEEE International Conference on Electronics, Circuits and Systems (ICECS 2019)"
authors: "S. R. Nandakumar, Irem Boybat, Vinay Joshi, Christophe Piveteau, Manuel Le Gallo, Bipin Rajendran, Abu Sebastian, Evangelos S. Eleftheriou"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["PCM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["device-variation", "conductance-drift", "simulator", "read-write-noise"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 11
cites_in_collection: 1
citations_overall: 34
priority_score: 6.81
doi: "https://doi.org/10.1109/icecs46596.2019.8964852"
pdf: null
fulltext: null
---

# PCM Device Models

**Phase-Change Memory Models for Deep Learning Training and Inference** — IEEE International Conference on Electronics, Circuits and Systems (ICECS 2019) (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Statistically accurate PCM device models, built from characterization of over 10,000 devices and capturing state-dependent conductance update, drift, and read noise, are integrated into TensorFlow to let researchers realistically evaluate on-chip training and inference performance of PCM-based in-memory-computing DNN hardware.

## Summary
The paper addresses the need for computationally simple but statistically faithful PCM device models to evaluate deep-learning hardware based on in-memory computing, since PCM conductance states used as DNN synaptic weights exhibit non-ideal, state-dependent programming behavior, conductance drift, and read noise. The authors characterize more than 10,000 PCM devices and derive models that capture these effects (state-dependent conductance update variability, conductance drift over time, and read noise), designed to be computationally simple enough to integrate with deep-learning frameworks. They integrate the resulting models into TensorFlow so that both on-chip/analog training and one-time weight-programming inference scenarios for PCM-array-based DNN hardware can be evaluated realistically within standard ML training pipelines.

## Contributions
- Statistically accurate PCM device models derived from characterization of more than 10,000 devices
- Models capturing state-dependent conductance update variability, conductance drift, and read noise, rather than simplified generic noise assumptions
- Computationally simple model formulations suitable for integration with deep-learning frameworks
- Integration of the models into TensorFlow, enabling realistic evaluation of PCM-array-based training and inference hardware for DNNs

## Key claims (stable IDs)
- **2019_Nandakumar_PCMDeviceModels_ICECS#C1** — The proposed PCM models are statistically accurate because they are derived from large-scale device characterization — _support:_ models are based on the characterization of more than 10,000 devices and capture the state-dependent nature and variability of conductance update, conductance drift, and read noise — _loc:_ Abstract
- **2019_Nandakumar_PCMDeviceModels_ICECS#C2** — The models are computationally simple enough to be used for realistic DNN training/inference evaluation — _support:_ integrating the computationally simple device models with deep learning frameworks such as TensorFlow enables realistic evaluation of training and inference performance of PCM array based hardware implementations of DNNs — _loc:_ Abstract

## Limitations
- Analysis based on the abstract only; the precise functional form of the conductance-update, drift, and noise models, and the benchmark networks used to validate them, could not be verified from the full text
- As a device-modeling paper, it does not itself report new accelerator architecture or DNN accuracy results beyond validating the model's statistical fidelity

## Remarks
This paper is the device-modeling companion to the IBM group's PCM-based DNN work (e.g., the Joshi et al. Nature Communications paper in this collection, which cites it), and such statistically grounded PCM models (state-dependent update, drift, 1/f noise) became a standard ingredient in later PCM/analog-AI training and drift-mitigation papers. Because only the abstract was available here, the exact modeling equations and the scope of validation (device count per state, networks tested) should be checked against the full ICECS paper before relying on specific modeling details.

## Cites (in collection, 1)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)

## Cited by (in collection, 11)
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "To date, each type of analogue memory exhibits some form of non-ideal behaviour such as limited resistance contrast, significant non-linearity and stochasticity in conductance-vs-pulse characteristics, strong asymmetry during bidirectional programming, read noise, and conductance drift after programming to name a few15-19."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _uses-method-or-tool_: "In order to make the model more robust to noise, we perturb the weights of each tile according to a model simulating two times the PCM programming noise derived experimentally in Ref. 46."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "We mainly investigate the situation where all weight-related parameters have been carefully calibrated to existing PCM hardware31, however, the model can be adapted to other memory technologies as well (see Supplementary Notes B.2)."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "The low-frequency read noise is typically modelled using a normal distribution centered around zero with a standard deviation of σnG dependent on the time elapsed since programming, i.e., N (0, σnG (t))50 ."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _motivation_: "Analog devices are inherently non-deterministic and subject to temporal variations, impacting NN accuracy when deployed on AIMC-based accelerators7–10."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _uses-method-or-tool_: "The PCM device drift and noise are modeled with the PCM noise model [31], implemented via the IBM Analog Hardware Acceleration Kit (AIHWKIT) [32-34]."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "Dynamic weight noise sources whose magnitude vary as a function of time include read noise [28] – due to analog 1/f noise of devices and circuits – and temporal conductance drift, which is the decrease in device conductance over time that is notably observed in PCM devices [33]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2019_Nandakumar_PCMDeviceModels_ICECS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/icecs46596.2019.8964852
