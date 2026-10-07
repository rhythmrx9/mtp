---
id: W4226247444
key: 2022_Joksas_NonidealityAwareTraining_AdvSci
title: "Nonideality‐Aware Training for Accurate and Robust Low‐Power Memristive Neural Networks"
short: "Nonideality-Aware Training"
year: 2022
venue: "AdvSci"
venue_full: "Advanced Science"
authors: "Dovydas Joksas, Erwei Wang, Nikolaos Barmpatsalos, Wing H. Ng, Anthony Joseph Kenyon, George Anthony Constantinides, Adnan Mehonić"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM", "Memristor(generic)"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "noise-injection", "weight-mapping", "device-variation", "stuck-at-faults", "energy-efficiency", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 7
citations_overall: 38
priority_score: 5.51
doi: "https://doi.org/10.1002/advs.202105784"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2022_Joksas_NonidealityAwareTraining_AdvSci.pdf"
fulltext: "../fulltext/2022_Joksas_NonidealityAwareTraining_AdvSci.txt"
---

# Nonideality-Aware Training

**Nonideality‐Aware Training for Accurate and Robust Low‐Power Memristive Neural Networks** — Advanced Science (2022)

## TL;DR
Nonideality-aware ex-situ training that models I-V nonlinearity in the layer function, maps non-negative weights to individual conductances and regularizes toward low conductance lets high-resistance, highly nonlinear memristors reach ~7-9% median MNIST error versus 41.6% for standard training, raising estimated VMM efficiency from 0.715 to 381 TOPS/W.

## Summary
Memristor crossbars suffer from I-V nonlinearity, stuck devices and device-to-device variability, and low-resistance (more linear) devices cost power. The authors redefine the synaptic layer output as y_j = f(sum_i g(x_i, w_ij)) with g a nonlinear (Poole-Frenkel-based) I-V model fitted to measured data from SiOx devices (low- and high-resistance states) and a 128x64 Ta/HfO2 crossbar. Weights are doubled, constrained non-negative and tied one-to-one to individual device conductances rather than conductance pairs, which allows L1 regularization to push devices toward low-conductance states and also lets conductance-dependent non-idealities be modelled. Validation during training is repeated several times at each checkpoint and an aggregate (median) used, to cope with stochastic non-idealities. Evaluation is simulation only: a 25-hidden-unit MLP on MNIST and a small CNN on CIFAR-10 with digital convolutions and crossbar fully-connected layers. Energy is estimated using P = IV per device. Networks trained this way transfer to different non-ideality setups without retraining and also handle uniform/lognormal D2D variability and stuck devices.

## Contributions
- Nonlinearity-aware training that places a measured non-ohmic I-V model inside the layer function
- One-to-one non-negative weight-to-conductance mapping enabling L1 regularization for power and conductance-dependent noise handling
- Aggregate (multi-sample median) validation metric for stochastic non-idealities
- Analysis showing high-resistance, high-nonlinearity devices become usable, with ~3 orders of magnitude better estimated energy efficiency
- Robustness study across a range of non-idealities (Fig. 8)

## Key claims (stable IDs)
- **2022_Joksas_NonidealityAwareTraining_AdvSci#C1** — Standard training on high I-V-nonlinearity SiOx devices gives unacceptable error while nonideality-aware training recovers near low-nonlinearity accuracy — _support:_ median error 41.6% (standard) vs 9.1% (aware) and 7.1% (aware + regularization) — _loc:_ Sec. 3 / Fig. 5
- **2022_Joksas_NonidealityAwareTraining_AdvSci#C2** — High-resistance devices with aware training raise energy efficiency by almost three orders of magnitude — _support:_ 0.715 TOPS/W (low-resistance) to 234 TOPS/W (non-regularized) and 381 TOPS/W (regularized) — _loc:_ Sec. 3 / Fig. 5
- **2022_Joksas_NonidealityAwareTraining_AdvSci#C3** — The approach extends to CNNs on CIFAR-10 with crossbar fully-connected layers — _support:_ lower inference error under high I-V nonlinearity vs standard training — _loc:_ Fig. 6

## Results
- Median MNIST inference error under high I-V nonlinearity: 41.6% standard vs 9.1% aware vs 7.1% aware+L1 (Fig. 5)
- Estimated efficiency: 0.715 -> 234 -> 381 TOPS/W (Sec. 3)
- Ideal / low-nonlinearity baselines about 4-5% median error in the robustness table (Fig. 8)
- CIFAR-10 CNN with crossbar FC layers: improved error under high nonlinearity (Fig. 6c, values not extracted)

## Key numbers
- array_size: 128x64 (Ta/HfO2 crossbar data)
- energy_eff: 381 TOPS/W (estimated, regularized)
- accuracy: 7.1% median error MNIST (high I-V nonlinearity, regularized)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Simulation only; device data are single-device I-V sweeps and a small crossbar, no full chip measurement
- Small networks (25-hidden-unit MLP; small CNN with digital convolutions)
- Energy estimate covers memristor power only; peripherals and ADC/DAC excluded
- Non-negative doubled weights double device count
- No transformers or language models

## Remarks
A careful, technology-agnostic ex-situ training study that is grounded in measured I-V data, and one of the few that tie training regularization to crossbar power. Evidence is limited to toy models, so applicability to large transformers is unproven, though the idea of conductance-aware regularization is relevant to LM mapping where power is dominated by many low-conductance cells. It complements noise-injection and committee-machine approaches in the collection.

## Cites (in collection, 7)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "The need to transfer data between memory and computing units in the von Neumann architecture is the main bottleneck in modern computers [7]; this is especially evident in machine learning where large amounts of data are utilized."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "Potential solutions do exist but many of them introduce a number of trade-offs. [in-situ (re)training of weights (or just a subset of them) to recover from the effects of nonidealities [15–19]]"
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "In this specific case, an alternative of faulty-devices [27] or line resistance [28]."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _data/numbers_: "Fabrication process is described in more detail in [48]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Alternatively, modifying ex-situ training has been proposed: altering the cost function [30] or injecting noise into the synaptic weights [31] can make MNNs more robust to the effects of nonidealities."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _background_: "In the specific context of MNNs, multiple smaller nonideal networks may replace a large one and increase the accuracy in this way [29]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _contrasts/critiques_: "Memristor-oriented ex-situ training is indeed a very promising method of making MNNs feasible. However, it has been applied by considering only a limited number of nonidealities, while the robustness of this technique is not well understood."

## Cited by (in collection, 1)
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _contrasts/critiques_: "The in-situ weight update process was either performed in the offline training scheme [13–15] or performed one by one and coordinated by external closed-loop control circuits [16, 17]."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2022_Joksas_NonidealityAwareTraining_AdvSci.pdf](../../07_Hardware_Aware_Training_and_Robustness/2022_Joksas_NonidealityAwareTraining_AdvSci.pdf)
- Full text: [../fulltext/2022_Joksas_NonidealityAwareTraining_AdvSci.txt](../fulltext/2022_Joksas_NonidealityAwareTraining_AdvSci.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1002/advs.202105784
