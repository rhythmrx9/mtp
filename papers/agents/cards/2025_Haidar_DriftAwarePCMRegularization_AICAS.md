---
id: W4414499786
key: 2025_Haidar_DriftAwarePCMRegularization_AICAS
title: "Drift-Aware Regularization for Long-Term Stability in Phase-Change Memory Based Neural Network Implementations"
short: "Drift-Aware PCM Regularization"
year: 2025
venue: "AICAS"
venue_full: "IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS 2025)"
authors: "Adnan Haidar, Vasileios G. Ntinas, Ronald Tetzlaff"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["conductance-drift", "hardware-aware-training", "noise-injection", "endurance-retention"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 11
citations_overall: 1
priority_score: 4.21
doi: "https://doi.org/10.1109/aicas64808.2025.11173140"
pdf: null
fulltext: null
---

# Drift-Aware PCM Regularization

**Drift-Aware Regularization for Long-Term Stability in Phase-Change Memory Based Neural Network Implementations** — IEEE International Conference on Artificial Intelligence Circuits and Systems (AICAS 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A drift-aware regularization framework with attention-based feature prioritization, layered on top of hardware-aware training, cuts a simulated 5-year PCM conductance-drift classification error on MNIST from 9.14% (standard HWA training) to 3.75%, and to 2.12% when combined with global drift compensation.

## Summary
PCM crossbars suffer conductance drift that degrades inference accuracy over months to years, a key obstacle to long-term deployment of PCM-based analog in-memory computing (AIMC). The paper proposes a drift-aware regularization framework that stabilizes weight drift during training, complemented by an attention-based mechanism that prioritizes critical features, going beyond standard hardware-aware (HWA) training. Evaluated with a 5-year drift simulation on a benchmark two-layer perceptron trained on MNIST, the method reduces classification error from 9.14% (standard HWA training) to 3.75%; combining it with global drift compensation further reduces error to 2.12%.

## Contributions
- Proposes a drift-aware regularization framework that stabilizes PCM weight drift during training, beyond standard hardware-aware (HWA) training
- Adds an attention-based mechanism that prioritizes critical features to further improve drift resilience
- Shows the method can be combined with global drift compensation for additional improvement
- Quantifies long-term (5-year simulated) robustness on a benchmark MNIST two-layer-perceptron task

## Key claims (stable IDs)
- **2025_Haidar_DriftAwarePCMRegularization_AICAS#C1** — Drift-aware regularization substantially reduces long-term classification error versus standard hardware-aware training — _support:_ 5-year drift simulation: 3.75% classification error with drift-aware regularization vs. 9.14% with standard HWA training on a two-layer perceptron for MNIST — _loc:_ Abstract
- **2025_Haidar_DriftAwarePCMRegularization_AICAS#C2** — Combining drift-aware regularization with global drift compensation further improves long-term accuracy — _support:_ Error further reduced to 2.12% when combined with global drift compensation — _loc:_ Abstract

## Results
- 5-year simulated PCM drift: 9.14% classification error with standard HWA training vs. 3.75% with drift-aware regularization (two-layer perceptron, MNIST)
- 2.12% classification error when drift-aware regularization is combined with global drift compensation

## Limitations
- Evaluated on a single small benchmark (two-layer perceptron on MNIST); generalization to deeper/larger networks or other tasks is not demonstrated in the abstract
- Drift evaluation is a simulation over 5 (simulated) years rather than a measured long-term PCM hardware study
- Abstract does not specify the PCM drift model or hyperparameters used for the regularization, limiting independent assessment of mechanism novelty versus existing drift-compensation literature

## Remarks
This is a companion piece to the same group's ISCAS paper (Attention-driven PCM-based In-Memory Computing for Smart Vision Systems) and builds directly on the existing PCM drift-compensation and HWA-training literature (Ambrogio's global drift compensation, Rasch's HWA training/AIHWKit, Kariyappa's noise-aware training). The reported error reduction (9.14%->3.75%, and to 2.12% with global drift compensation) is a meaningful relative improvement if confirmed by the full paper, and the idea of an attention-style feature-prioritizing regularizer as an add-on to standard HWA training is a lightweight, architecture-agnostic way to target drift specifically rather than noise in general -- useful context for comparing drift-mitigation strategies in a mapping-focused thesis.

## Cites (in collection, 11)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023)
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2025_Haidar_DriftAwarePCMRegularization_AICAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/aicas64808.2025.11173140
