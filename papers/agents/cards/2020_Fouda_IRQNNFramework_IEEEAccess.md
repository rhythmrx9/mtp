---
id: W3111367661
key: 2020_Fouda_IRQNNFramework_IEEEAccess
title: "IR-QNN Framework: An IR Drop-Aware Offline Training of Quantized Crossbar Arrays"
short: "IR-QNN Framework"
year: 2020
venue: "IEEEAccess"
venue_full: "IEEE Access, vol. 8, 2020"
authors: "Mohammed E. Fouda, Sugil Lee, Jongeun Lee, Gun Hwan Kim, Fadi Kurdahi, Ahmed M. Eltawil"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["ir-drop-parasitics", "quantization", "hardware-aware-training", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 9
citations_overall: 41
priority_score: 5.44
doi: "https://doi.org/10.1109/access.2020.3044652"
pdf: null
fulltext: null
---

# IR-QNN Framework

**IR-QNN Framework: An IR Drop-Aware Offline Training of Quantized Crossbar Arrays** — IEEE Access, vol. 8, 2020 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IR-QNN is a fast offline training/validation framework that incorporates interconnect IR-drop into quantized DNN training using a fabricated 4-bit Au/Al2O3/HfO2/TiN device model and efficient system-level IR-drop estimation (avoiding full SPICE during training), achieving near-baseline accuracy (2% drop on MNIST MLP, 4% drop on CIFAR-10 VGG/AlexNet) while also studying stuck-at-faults, variability and aging.

## Summary
Resistive crossbar arrays (RCAs) accelerate the matrix-vector multiplication at the core of DNNs in O(1) time, but interconnect wire resistance causes an IR-drop problem that degrades computational accuracy and is costly to simulate accurately via SPICE during training. IR-QNN proposes a fast and efficient training and validation framework that incorporates wire resistance into quantized DNN training without requiring full SPICE simulation in the training loop, instead using efficient system-level IR-drop estimation methods. The framework uses a device model derived from a fabricated four-bit Au/Al2O3/HfO2/TiN memristive device and two mapping schemes to realize quantized weights on the crossbar. SPICE is used only for final validation, confirming the system-level estimation captures the IR-drop effect well. The paper also studies other non-idealities (stuck-at-fault defects, variability, aging) and discusses neuronal/driver circuit design considerations.

## Contributions
- A fast offline training/validation framework (IR-QNN) that incorporates crossbar interconnect IR-drop into quantized DNN training without requiring computationally expensive SPICE simulation during training
- Use of a fabricated four-bit Au/Al2O3/HfO2/TiN memristive device model with two weight-mapping schemes to realize quantized weights on the crossbar
- Efficient system-level IR-drop estimation methods validated against SPICE simulation for accuracy
- Extension of the robustness study to other non-idealities: stuck-at-fault defects, device variability, and aging
- Discussion of neuronal and driver circuit design considerations for IR-drop-aware crossbar accelerators

## Key claims (stable IDs)
- **2020_Fouda_IRQNNFramework_IEEEAccess#C1** — The proposed system-level IR-drop estimation during training achieves accuracy close to the baseline (no IR-drop) when validated with SPICE — _support:_ 2% accuracy drop (worst case) for MNIST on an MLP network; 4% accuracy drop (worst case) for CIFAR-10 on modified VGG and AlexNet networks, relative to baseline — _loc:_ Abstract
- **2020_Fouda_IRQNNFramework_IEEEAccess#C2** — The device model used is grounded in a real fabricated device rather than a purely theoretical model — _support:_ 'A fabricated four-bit Au/Al2O3/HfO2/TiN device is modelled and used within the framework' (abstract) — _loc:_ Abstract
- **2020_Fouda_IRQNNFramework_IEEEAccess#C3** — The framework is efficient enough to avoid computationally extensive SPICE simulations during the training process itself — _support:_ Abstract: 'without the need for computationally extensive SPICE simulations during the training process'; SPICE used only for validation — _loc:_ Abstract

## Results
- 2% worst-case accuracy drop on MNIST (MLP network) versus baseline accuracy
- 4% worst-case accuracy drop on CIFAR-10 (modified VGG and AlexNet networks) versus baseline accuracy
- SPICE validation confirms the system-level IR-drop estimation effectively captures the IR-drop problem

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Access article appears gold open access but the PDF is hosted on IEEE Xplore's delivery system, which is not reachable from this environment); exact mapping schemes, IR-drop estimation method, and quantitative variability/aging/SAF results could not be verified
- Device model is based on a single fabricated device type (Au/Al2O3/HfO2/TiN), so generalization to other RRAM material stacks is unclear from the abstract alone

## Remarks
Based on the abstract, this paper directly targets a core non-ideality (interconnect IR-drop) that many architecture and mapping papers in this collection acknowledge but do not always model rigorously, using a real fabricated-device model for credibility, and explicitly trades off training-time cost (via fast system-level estimation) against the gold-standard but expensive SPICE accuracy. It is a useful companion to mapping/representability papers (e.g., Representable Matrices, W3013896150) that also address IR-drop, but from an offline-training-robustness angle rather than a mapping-optimization angle. Despite the IEEE Access venue being nominally open access, the PDF could not be retrieved from this machine (IEEE Xplore delivery is blocked here), so this entry remains abstract-only.

## Cites (in collection, 9)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2018_Kim_NonlinearIVAwareDNN_JETC](2018_Kim_NonlinearIVAwareDNN_JETC.md) Nonlinear-IV NN (2018)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 3)
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "However, even the small value of the wire resistance has a significant effect on the weights stored in RCA [112–114]."
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2020_Fouda_IRQNNFramework_IEEEAccess.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/access.2020.3044652
