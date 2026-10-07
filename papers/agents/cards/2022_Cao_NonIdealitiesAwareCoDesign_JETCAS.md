---
id: W4312081519
key: 2022_Cao_NonIdealitiesAwareCoDesign_JETCAS
title: "A Non-Idealities Aware Software–Hardware Co-Design Framework for Edge-AI Deep Neural Network Implemented on Memristive Crossbar"
short: "Non-Idealities Aware Co-Design"
year: 2022
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS 2022)"
authors: "Tiancheng Cao, Chen Liu, Weijie Wang, Tan‐Tan Zhang, Hock Koon Lee, Ming Hua Li, Wen‐Dong Song, Zhixian Chen, Victor Yi-Qian Zhuo, Nan Wang, Yao Hua Zhu, Yuan Gao et al."
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["Memristor(generic)", "ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "device-variation", "quantization", "edge-ai", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 7
citations_overall: 31
priority_score: 5.98
doi: "https://doi.org/10.1109/jetcas.2022.3214334"
pdf: null
fulltext: null
---

# Non-Idealities Aware Co-Design

**A Non-Idealities Aware Software–Hardware Co-Design Framework for Edge-AI Deep Neural Network Implemented on Memristive Crossbar** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS 2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Presents a unified software-hardware co-design/training framework that jointly models device-level (conductance variation, quantization, D2D variation, programming failure) and array-level (line resistance, sneak path) non-idealities, achieving 83% CIFAR-10 accuracy (within 3% of ideal) on a simplified VGG mapped to a measured 128x128 RRAM array with 3-level weights.

## Summary
The paper addresses the gap between ideal DNN training and real memristive-crossbar deployment by building a holistic non-ideality-aware training/evaluation framework implemented in Python/PyTorch. It models device-level non-idealities (conductance variation, nonuniform quantization levels, device-to-device variation, programming failure probability) together with array-level effects (line resistance and sneak-path leakage via a new fast/accurate line-resistance estimation model) and peripheral circuit non-linearity/offset. These factors are incorporated into the DNN training loop so that the network learns to compensate for them, rather than being evaluated only post-hoc on an ideally-trained network. The framework is validated on a simplified 5-layer VGG network mapped to a measured 128x128 RRAM array with only 3-level (not full precision) per-device weight resolution, targeting CIFAR-10 classification, and shown to substantially close the accuracy gap versus the ideal (non-quantized, noise-free) model.

## Contributions
- Unified software-hardware co-design framework combining device-level (conductance variation, quantization levels, D2D variation, programming failure) and array-level (line resistance, sneak path) non-ideality models
- A new fast and accurate line-resistance/IR-drop estimation model for array-level effects
- Incorporation of peripheral circuit non-linearity and offset into the unified model
- Non-ideality-aware training procedure (Python+PyTorch) that mitigates accuracy degradation rather than just measuring it
- Validation against a measured 128x128 RRAM array with 3-level weight resolution on a VGG/CIFAR-10 task

## Key claims (stable IDs)
- **2022_Cao_NonIdealitiesAwareCoDesign_JETCAS#C1** — The non-ideality-aware training process can mitigate accuracy degradation caused by device/array/peripheral non-idealities on real hardware — _support:_ 83% inference accuracy achieved on CIFAR-10 with less than 3% accuracy drop vs. the ideal model — _loc:_ Results (per abstract; exact section unknown without full text)
- **2022_Cao_NonIdealitiesAwareCoDesign_JETCAS#C2** — A 3-level (very low precision) per-device weight resolution on a measured 128x128 RRAM array is sufficient to reach competitive CIFAR-10 accuracy when the full non-ideality model is used in training — _support:_ 83% accuracy figure quoted in abstract for simplified VGG at 3-level resolution — _loc:_ Evaluation (per abstract)

## Results
- 83% inference accuracy on CIFAR-10 with a simplified 5-layer VGG mapped to a measured 128x128 RRAM array using 3-level weight resolution
- Less than 3% accuracy drop compared to the ideal (non-hardware-aware) model

## Limitations
- Abstract-only basis for this entry: the described numbers (83% accuracy, <3% drop) are taken directly from the abstract, but methodological/experimental detail (e.g., exact baseline, dataset split, number of trials) could not be verified from full text
- Evaluated on a simplified VGG (5 layers) and CIFAR-10 only — not validated on deeper networks or other datasets
- Very low per-device weight resolution (3 levels) implies many devices per weight bit, raising array-area/energy overhead questions not addressed in the abstract
- Single measured 128x128 array — scalability of the line-resistance/sneak-path model to much larger crossbars is untested here

## Remarks
This paper is representative of the hardware-aware-training literature (similar in spirit to IBM's hardware-aware training and TxSim/NeuroSim-style tools) but distinguishes itself by combining device, array (line resistance/sneak path) and peripheral circuit non-idealities into one PyTorch-based training loop validated against a real measured RRAM array rather than a purely simulated device model. The reported 83%/<3%-drop result is a reasonably strong, hardware-grounded data point for the value of non-ideality-aware training at very low (3-level) cell precision, though verification would require the full text; later citations (e.g., RRAM-PoolFormer, error-injected robustness metric papers) suggest the framework or its non-ideality modeling approach has been used as a baseline/building block in subsequent noise-robustness work.

## Cites (in collection, 7)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021)
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)

## Cited by (in collection, 2)
- [2023_Cao_RRAMPoolFormer_ISCAS](2023_Cao_RRAMPoolFormer_ISCAS.md) RRAM-PoolFormer (2023) — _extends/builds-on_: "After the weight mapping to crossbar array, the non-idealities-aware training is carried out [31]."
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jetcas.2022.3214334
