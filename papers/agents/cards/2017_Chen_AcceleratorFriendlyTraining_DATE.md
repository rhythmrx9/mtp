---
id: W2612375349
key: 2017_Chen_AcceleratorFriendlyTraining_DATE
title: "Accelerator-friendly neural-network training: Learning variations and defects in RRAM crossbar"
short: "Accelerator-friendly training"
year: 2017
venue: "DATE"
venue_full: "2017 Design, Automation and Test in Europe (DATE)"
authors: "Lerong Chen, Jiawen Li, Yiran Chen, Qiuping Deng, Jiyuan Shen, Xiaoyao Liang, Li Jiang"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "stuck-at-faults", "device-variation", "weight-mapping", "calibration-compensation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 31
cites_in_collection: 0
citations_overall: 246
priority_score: 9.18
doi: "https://doi.org/10.23919/date.2017.7926952"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2017_Chen_AcceleratorFriendlyTraining_DATE.pdf"
fulltext: "../fulltext/2017_Chen_AcceleratorFriendlyTraining_DATE.txt"
---

# Accelerator-friendly training

**Accelerator-friendly neural-network training: Learning variations and defects in RRAM crossbar** — 2017 Design, Automation and Test in Europe (DATE) (2017)

## TL;DR
Fault/variation-aware off-device training for 1R RRAM crossbars: a weighted bipartite-matching weight-to-memristor mapping plus retraining that keeps large weights off abnormal cells holds a two-layer MNIST MLP within about 1-5% of ideal accuracy versus 10-45% loss for the prior Vortex approach.

## Summary
Memristor resistance variation (lognormal, w' = w*exp(theta), theta~N(0,sigma^2)) and stuck-at faults (SA0 in the low-resistance state, SA1 in the high-resistance state; 1.75% and 9.04% device rates cited from a real chip) degrade crossbar accuracy and yield, and hardware fixes (disabling cells via transistors, redundancy) cost area and power. Assuming the per-crossbar fault and variation map is known by test (March-C, squeeze-search, sneak-path tests), the method (i) finds a weight-memristor mapping through weighted bipartite matching (permuting rows, optionally with redundant rows) so important weights land on healthy cells, and (ii) retrains the network with weights placed on abnormal cells reduced and fixed, in order of a sensitivity measure, exploiting the network's self-healing; reducing multiple independent weights per iteration cuts iterations from 2000 (N=1) to 205 (N=20) at ~89-90% test rate. Weights use two memristors (positive and negative) per weight in two 784x10 crossbars. Experiments: Monte-Carlo simulation of a two-layer MNIST network (~90% ideal accuracy) against Vortex and no mitigation, with sweeps of sigma and redundant rows.

## Contributions
- Per-crossbar bipartite-matching mapping of weights to memristors
- Accelerator-friendly retraining that fixes low-importance weights onto faulty devices
- Iteration-reduction strategy picking multiple independent weights per step
- Joint tolerance of resistance variation and stuck-at faults with fewer redundant rows

## Key claims (stable IDs)
- **2017_Chen_AcceleratorFriendlyTraining_DATE#C1** — Retraining after matching lifts accuracy under heavy variation — _support:_ 61.8% (bi-match only) -> 86.0% (bi-retrain) at sigma=2 — _loc:_ Sec. V-B, Fig. 4a
- **2017_Chen_AcceleratorFriendlyTraining_DATE#C2** — With both variation and SAFs the method stays near ideal — _support:_ 89.27% at sigma=0.5 and 71.02% at sigma=2 vs 55.87% for bi-match only; <5% loss in the largest Vortex variation set vs 45% for Vortex — _loc:_ Fig. 4b
- **2017_Chen_AcceleratorFriendlyTraining_DATE#C3** — Redundancy needs shrink — _support:_ bi-retrain keeps >85% with 20 redundant rows; no further gain beyond 40 — _loc:_ Fig. 4d

## Results
- Ideal MNIST accuracy ~90% (two-layer network), used as upper bound
- Prior work loses 10-45% accuracy under comparable variation (Vortex)
- Training-iteration reduction 2000 -> 634 -> 378 -> 205 for N=1,5,10,20 with test rate 89.7/90.5/90.3/89.3% (Table I)

## Key numbers
- array_size: 784x10 (two crossbars, differential)
- accuracy: 86.0% at sigma=2 (ideal ~90%); 71.02% with SAFs at sigma=2

## Datasets / benchmarks
MNIST

## Limitations
- Needs per-chip fault/variation map and per-chip (off-device) retraining
- Tiny two-layer MNIST MLP only; no CNN/transformer evidence
- Simulation (Monte-Carlo) with lognormal variation, SA0/SA1 models; no IR drop or drift
- Retraining cost grows with network size; scaling to LMs impractical without chip-specific training

## Remarks
An early example of fault-aware mapping and retraining: the same idea reappears as fault-aware training and permutation-based mapping in later work. For analog LMs the per-chip retraining requirement is the main obstacle, though bipartite permutation mapping is cheap and could be combined with generic noise-robust training. Evidence is small-scale simulation.

## Cited by (in collection, 31)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "These include (i) (re-)training [16–21], (ii) optimized weight to conductance conversion [14], (iii) rank clipping to reduce the effects of non-idealities by lowering crossbar dimensions [25], (iv) schemes to alleviate the effect of hard failures [26], and (vi) hardware solutions to address low-voltage induced drift [15], programming errors [23], and IR drop [24]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _contrasts/critiques_: "Software approach: Other recent works [2, 3, 9] have adopted different methods that all require retraining the weights of target DNN to be mapped in a crossbar array w.r.t various non-ideal effects for the specific device."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "Off-line variation-aware training schemes have also been proposed, where hardware non-idealities such as device-to-device variations13,14, defective devices14, or IR drop13 are first characterized and then fed into the training algorithm running in software."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "the iterative nature of DNN training and careful re-training helps recover the accuracy loss from non-idealities [43], faults [44], and variations [45]."
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020) — _background_: "In VAT [20, 21, 23], RRAM array is read to characterize device variations, and these statistical variations are then embedded to train the neural network."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Reference 209 proposes a scheme to assign the rows of the weight matrix to the crossbar rows in a way that minimizes the expected deviations on the column outputs due to cycle-to-cycle variability. Then, during a re-training phase, weights that remain particularly prone to errors are frozen and reduced to zero."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "For example, a defect map or variation distribution [153, 155, 157] of devices in the crossbar can aid the training process by mapping the sensitive cells to defect-free or low variation cells."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "To address this challenge, TIMELY not only leverages algorithm resilience of CNNs/DNNs to counter hardware vulnerability [9], [48], [81], but also minimize potential errors introduced by hardware, thereby achieving the optimal trade-off between energy efficiency and accuracy."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _contrasts/critiques_: "Weight compensation: Some works [5, 7] cooperate mask retraining and re-mapping methods to compensate the conductance deviation measured on a specific ReRAM crossbar."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _contrasts/critiques_: "At the algorithmic level, the weights are trained to enhance the tolerance of NNs to the resistance variations of ReRAMs [15]-[18]."
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _baseline/comparison_: "Several methods are proposed to address the stuck-at-fault defects, such as permuting the order of the crossbar rows and columns [4], retraining the network by considering the defect locations [5], [6]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "Matrix permutation [100, 103, 107, 108] can be based on row permutation [100, 107] and neuron permutation [100, 107]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "The first category includes device defects (e.g., stuck-at-high or stuckat-low resistance [12]) and device reliability issues (e.g., retention failure [13] and resistance drift [14]) that are mostly deterministic in nature and have been addressed in prior work [15–20]."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _background_: "The need to transfer data between memory and computing units in the von Neumann architecture is the main bottleneck in modern computers [7]; this is especially evident in machine learning where large amounts of data are utilized."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _baseline/comparison_: "[7, 24] utilize VAT based on known device variation (σ) characterized from RRAM devices, while [5] combines VAT with dynamic precision"
- [2023_Ma_SAFVariationTolerantMapping_JETC](2023_Ma_SAFVariationTolerantMapping_JETC.md) SAF/Variation Remapping (2023) — _contrasts/critiques_: "Some researchers propose to first measure variation distribution and then map the weight according to the measured distribution [4, 8, 14]. This process needs a large amount of computation which is intolerable for edge devices."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _contrasts/critiques_: "Moreover, some works [17], [18] prevent large weights from mapping to high variation memristors. This requires extensive chip characterization and does not address errors due to the accumulation of variations in small weights."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "Emerging memory devices such as PCM exhibit imperfect yield, and some fraction of the devices in a given crossbar array will simply not switch properly30,75."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _baseline/comparison_: "In Tab. I, we compare key features of the AIHWKit to related open-source AIMC simulation toolkits."
- [2023_Jang_VECOM_ICCAD](2023_Jang_VECOM_ICCAD.md) VECOM (2023) — _contrasts/critiques_: "Notably, software-based techniques [4], [6], [7] have aimed to lessen the impact of ReRAM's variation by retraining or fine-tuning the DNNs to adapt to the non-ideal distribution of ReRAM resistance."
- [2024_Chowdhury_MELISO_ICONS](2024_Chowdhury_MELISO_ICONS.md) MELISO (2024) — _motivation_: "As RRAMs critically suffer from device nonidealities, most prominently non-linear conductance tuning, C-to-C, and device-to-device variations, benchmarking frameworks need to incorporate these key issues [23, 24]."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _contrasts/critiques_: "Compared to other schemes in literature45,48, we map weight matrices as contiguous blocks instead of varying rows or lines on the crossbar."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _background_: "Similar to any other analog NVMs [19-21], PCM has its intrinsic nonidealities, such as read noise [12, 22, 23], device-to-device variations [24], conductance drift over time after programing [13, 25, 26], limited memory window [17, 27], which can adversely affect DNN inference accuracy."
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2017_Chen_AcceleratorFriendlyTraining_DATE.pdf](../../07_Hardware_Aware_Training_and_Robustness/2017_Chen_AcceleratorFriendlyTraining_DATE.pdf)
- Full text: [../fulltext/2017_Chen_AcceleratorFriendlyTraining_DATE.txt](../fulltext/2017_Chen_AcceleratorFriendlyTraining_DATE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.23919/date.2017.7926952
