---
id: W4319990485
key: 2023_Antolini_PCMDriftHWSWMitigation_JETCAS
title: "Combined HW/SW Drift and Variability Mitigation for PCM-Based Analog In-Memory Computing for Neural Network Applications"
short: "PCM-Drift-HWSW-Mitigation"
year: 2023
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2023)"
authors: "Alessio Antolini, Carmine Paolino, Francesco Zavalloni, Andrea Lico, Eleonora Franchi Scarselli, Mauro Mangia, Fabio Pareschi, Gianluca Setti, Riccardo Rovatti, Mattia Luigi Torres, Marcella Carissimi, Marco Pasotti"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["PCM"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["conductance-drift", "calibration-compensation", "hardware-aware-training", "chip-demo", "noise-injection"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 10
citations_overall: 35
priority_score: 5.52
doi: "https://doi.org/10.1109/jetcas.2023.3241750"
pdf: null
fulltext: null
---

# PCM-Drift-HWSW-Mitigation

**Combined HW/SW Drift and Variability Mitigation for PCM-Based Analog In-Memory Computing for Neural Network Applications** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2023) (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A combined hardware/software approach mitigates PCM conductance drift in an analog in-memory-computing MAC prototype (90nm STMicroelectronics) by using a conductance-ratio circuit technique plus device-aware DNN training, achieving ~95% MAC accuracy under drift and up to a 36% classification-accuracy gain over conventional training on a LeNet-5/CIFAR-10 task.

## Summary
Matrix-vector multiplications dominate DNN training and inference cost, and phase-change-memory (PCM) based analog in-memory computing (AIMC) is a candidate for improving DNN accelerator energy efficiency, but PCM conductance drift over time can significantly degrade MVM precision and thus DNN accuracy. This paper proposes a combined hardware and software mitigation: at the circuit level, a conductance-ratio technique compensates for PCM cell conductance drift within the core MAC computation; at the software/training level, a model of PCM cell behavior is used to perform device-aware training of DNNs, with accuracy estimated on a CIFAR-10 classification task. The approach is validated with a PCM-based AIMC prototype designed in a 90nm STMicroelectronics process that performs multiply-and-accumulate (MAC) operations, the computational kernel of MVMs. The combined hardware drift compensation and device-aware training substantially improve robustness to PCM non-idealities relative to conventional training.

## Contributions
- A circuit-level conductance-ratio technique embedded in the MAC computation core to compensate for PCM conductance drift
- A device-aware DNN training methodology using a model of PCM cell behavior, evaluated on a CIFAR-10 classification task
- A PCM-based AIMC hardware prototype in 90nm STMicroelectronics technology performing MAC (the MVM kernel operation), used to validate the approach
- Quantification of MAC computation accuracy under drift, and of the classification-accuracy benefit from device-aware training with and without drift compensation

## Key claims (stable IDs)
- **2023_Antolini_PCMDriftHWSWMitigation_JETCAS#C1** — The combined circuit-level drift compensation keeps MAC computation accuracy high even under PCM conductance drift — _support:_ MAC computation accuracy around 95% even under the effect of cell drift — _loc:_ Abstract
- **2023_Antolini_PCMDriftHWSWMitigation_JETCAS#C2** — Device-aware DNN training makes networks substantially less sensitive to PCM weight variability than conventional training — _support:_ 15% increase in classification accuracy over a conventionally-trained LeNet-5 DNN from device-aware training alone — _loc:_ Abstract
- **2023_Antolini_PCMDriftHWSWMitigation_JETCAS#C3** — Combining device-aware training with drift compensation yields a larger accuracy improvement than either alone — _support:_ 36% classification-accuracy gain when drift compensation is applied on top of device-aware training — _loc:_ Abstract

## Results
- ~95% MAC computation accuracy under PCM cell conductance drift, measured on the 90nm PCM-based AIMC prototype
- 15% increase in CIFAR-10 classification accuracy from device-aware DNN training vs. conventionally-trained LeNet-5
- 36% classification-accuracy gain when drift compensation is additionally applied

## Limitations
- This entry is based on the abstract only (no full text or PDF was located); the exact conductance-ratio circuit mechanism, device model details, and full experimental protocol are not confirmed here
- Accuracy evaluation uses LeNet-5 on CIFAR-10, a relatively small network/dataset, so results may not generalize directly to larger modern DNNs
- Classification-accuracy estimates rely on a device behavior model for training rather than being directly measured end-to-end on the fabricated prototype (per the abstract's description)

## Remarks
This paper sits alongside the broader PCM drift-mitigation literature (e.g., Ambrogio's conductance-drift papers, HERMES-Core, Mackin's weight-programming work) by combining a circuit-level compensation technique with device-aware training, and backing the MAC-level claim with an actual 90nm fabricated prototype rather than simulation alone. Because only the abstract was available, the precise drift model, the time horizon over which the ~95% MAC accuracy and 36% gain were measured, and comparison to alternative drift-mitigation schemes could not be verified here and should be checked in the full paper.

## Cites (in collection, 10)
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018)
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022)
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022)

## Cited by (in collection, 2)
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "Analog IMC platforms are susceptible to various non-idealities arising from the device-to-device variations and temporal conductance drift of the memristive devices as well as from the parasitic resistances of the metallic interconnects in the crossbar-arrays [2, 6, 10, 22]."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _contrasts/critiques_: "Alternatively, noise estimated from a non-extensive chip characterization can be injected in off-chip training [19]-[24] to enhance the network's tolerance towards errors due to conductance variation. However, this approach fails to address the issue of reducing such errors, as memristors can still get mapped to high variation conductance states, rendering it ineffective."

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2023_Antolini_PCMDriftHWSWMitigation_JETCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jetcas.2023.3241750
