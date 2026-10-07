---
id: W4313138950
key: 2022_Gao_BRoCoM_TCAD
title: "BRoCoM: A Bayesian Framework for Robust Computing on Memristor Crossbar"
short: "BRoCoM"
year: 2022
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022)"
authors: "Di Gao, Zeyu Yang, Qingrong Huang, Grace Li Zhang, Xunzhao Yin, Bing Li, Ulf Schlichtmann, Cheng Zhuo"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["Memristor(generic)"]
models: []
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "device-variation", "noise-injection"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 11
priority_score: 4.26
doi: "https://doi.org/10.1109/tcad.2022.3215071"
pdf: null
fulltext: null
---

# BRoCoM

**BRoCoM: A Bayesian Framework for Robust Computing on Memristor Crossbar** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
BRoCoM is a unified Bayesian-inference framework that folds memristor process-variation and noise statistics into a prior weight distribution and reformulates robustness optimization as Bayesian neural network training, aiming to keep inference accuracy stable when a trained network's weights deviate from their programmed memristor conductances.

## Summary
Deploying a trained neural network on a memristor crossbar requires programming memristors to target conductance values, but device-based process variation and noise cause the realized weights to deviate from the trained values, degrading inference accuracy. BRoCoM proposes a unified Bayesian inference-based framework that connects device-level nonidealities to algorithmic training: it incorporates different levels of nonideality (variation, noise) into a prior distribution over weights, then casts the robustness-optimization problem as Bayesian neural network (BNN) training, so that the optimized network weights natively accommodate the expected uncertainty and minimize inference degradation. The authors report experimental results confirming that BRoCoM achieves stable inference performance while tolerating nonideal process-variation and noise effects on memristor crossbars.

## Contributions
- A unified Bayesian-inference-based framework (BRoCoM) linking memristor device nonidealities directly to the prior weight distribution used in training
- Reformulation of crossbar robustness optimization as Bayesian neural network (BNN) training rather than ad hoc noise-injection training
- Support for incorporating different levels/types of device nonideality (process variation, noise) into the same framework
- Experimental validation that the resulting networks maintain stable inference accuracy under nonideal memristor effects

## Key claims (stable IDs)
- **2022_Gao_BRoCoM_TCAD#C1** — Mapping a trained NN onto memristor crossbars without compensation causes inference accuracy degradation due to weight-programming deviations from process variation and noise — _support:_ motivating claim stated in the abstract — _loc:_ Abstract
- **2022_Gao_BRoCoM_TCAD#C2** — BRoCoM's Bayesian-training-based approach achieves stable inference performance despite nonideal process variation and noise — _support:_ experimental results reported to confirm stable inference performance under nonideal effects — _loc:_ Abstract

## Results
- Experimental results reported to confirm stable inference performance under process variation and noise (specific accuracy numbers not given in the abstract)

## Limitations
- This entry is based on the abstract only (no full text or PDF was located); the specific NN models, datasets, nonideality magnitudes, and quantitative accuracy results are not confirmed here
- Framework appears to be evaluated via simulation of device nonideality models rather than on fabricated memristor hardware (not confirmed from abstract alone)

## Remarks
BRoCoM belongs to the hardware-aware/noise-robust training literature (category 07) and its distinguishing idea -- folding device nonideality statistics directly into a Bayesian prior over weights rather than treating robustness as a separate regularization or noise-injection trick -- is conceptually appealing for connecting device physics to training theory. Because only the abstract was available, the magnitude of the reported robustness gains, the specific device/noise models used, and the benchmarks tested could not be verified here and should be checked in the full paper before citing specific numbers.

## Cites (in collection, 10)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2022_Gao_BRoCoM_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2022.3215071
