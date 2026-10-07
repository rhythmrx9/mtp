---
id: W4411725113
key: 2025_Haidar_CSPCMVisionSystem_ISCAS
title: "Attention-driven PCM-based In-Memory Computing for Smart Vision Systems"
short: "CS-PCM Vision System"
year: 2025
venue: "ISCAS"
venue_full: "IEEE International Symposium on Circuits and Systems (ISCAS 2025)"
authors: "Adnan Haidar, Amir Khan, Vasileios G. Ntinas, Jorge Fernández‐Berni, Ricardo Carmona‐Galán, Ronald Tetzlaff"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["edge-ai", "attention", "analog-mvm", "hardware-aware-training", "conductance-drift"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 2
priority_score: 4.33
doi: "https://doi.org/10.1109/iscas56072.2025.11044041"
pdf: null
fulltext: null
---

# CS-PCM Vision System

**Attention-driven PCM-based In-Memory Computing for Smart Vision Systems** — IEEE International Symposium on Circuits and Systems (ISCAS 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
An energy-efficient edge vision system combining compressed sensing for on-sensor dimensionality reduction with a single-layer ANN on PCM crossbars, using attention-regularized hardware-aware training to keep face-recognition accuracy stable under PCM conductance drift.

## Summary
The paper targets low-power edge vision, proposing a system that pairs compressed sensing (CS) for dimensionality reduction at the sensor with a single-layer artificial neural network implemented on Phase-Change-Memory (PCM) crossbars for inference. CS produces a low-dimensional feature vector fed directly into the PCM-based ANN, avoiding the cost of processing full-resolution images. To counter PCM hardware non-idealities, the authors apply hardware-aware (HWA) training augmented with an attention-based regularization mechanism intended to prioritize critical features, improving both inference stability and resilience to long-term conductance drift. On a face-recognition task, the attention-enhanced HWA training reduces overfitting and sustains accuracy under simulated PCM drift conditions.

## Contributions
- Integrates compressed sensing (on-sensor dimensionality reduction) with a PCM-crossbar-based single-layer ANN for an end-to-end low-power edge inference pipeline
- Introduces an attention-based regularization mechanism added to standard hardware-aware (HWA) training to prioritize critical features and improve drift resilience
- Evaluates the approach on a face-recognition task, showing improved inference stability and reduced overfitting under PCM drift versus standard HWA training

## Key claims (stable IDs)
- **2025_Haidar_CSPCMVisionSystem_ISCAS#C1** — Attention-enhanced hardware-aware training mitigates overfitting and maintains face-recognition accuracy under PCM conductance drift better than standard HWA training — _support:_ Qualitative claim stated in the abstract; no specific numeric accuracy values given — _loc:_ Abstract

## Limitations
- Abstract gives no specific quantitative accuracy/drift numbers, so the magnitude of improvement over standard HWA training cannot be verified from the abstract alone
- Evaluated on a single-layer ANN and a single task (face recognition); generalization to deeper networks or other tasks is untested per the abstract
- Likely simulation-based (PCM device/drift models) rather than measured on fabricated PCM hardware; full text not available to confirm

## Remarks
This is one of two related papers in this batch (with the Haidar/Ntinas/Tetzlaff Drift-Aware Regularization AICAS paper) from the same group exploring attention-based regularization for PCM drift resilience; together they suggest a developing research thread on using feature-importance-style regularization during hardware-aware training as a lightweight alternative/complement to global drift-compensation techniques. Without the full text, the practical significance (effect size, comparison baselines) cannot be assessed here.

## Cites (in collection, 7)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2025_Haidar_CSPCMVisionSystem_ISCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iscas56072.2025.11044041
