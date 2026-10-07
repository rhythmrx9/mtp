---
id: W2625840880
key: 2017_Liu_DefectRescuing_DAC
title: "Rescuing Memristor-based Neuromorphic Design with High Defects"
short: "Defect Rescuing"
year: 2017
venue: "DAC"
venue_full: "Proceedings of the 54th Annual Design Automation Conference (DAC 2017)"
authors: "Chenchen Liu, Miao Hu, John Paul Strachan, Hai Helen Li"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["Memristor(generic)"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["stuck-at-faults", "device-variation", "hardware-aware-training", "chip-in-the-loop", "weight-mapping", "analog-mvm", "calibration-compensation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 14
cites_in_collection: 1
citations_overall: 260
priority_score: 7.71
doi: "https://doi.org/10.1145/3061639.3062310"
pdf: "../../06_Nonidealities_and_Reliability/2017_Liu_DefectRescuing_DAC.pdf"
fulltext: "../fulltext/2017_Liu_DefectRescuing_DAC.txt"
---

# Defect Rescuing

**Rescuing Memristor-based Neuromorphic Design with High Defects** — Proceedings of the 54th Annual Design Automation Conference (DAC 2017) (2017)

## TL;DR
Defect-rescuing flow for memristor crossbars (weight-significance classification, defect-aware retraining, remapping of the worst defects to redundancy columns) that, using measured TaOx 1T1M defect data, recovers 2-layer MNIST accuracy from 42.5% to 98.1% (normalized) at 20% stuck-at defects and to 99.3% with 5% remapping.

## Summary
Memristor crossbar matrix-vector multiplication (weights as conductances, TIA readout) is vulnerable to single-bit failures (SBF), i.e. cells stuck at high (stuck-on) or low (stuck-off) conductance. The authors show that 20% SBF drops a 784x10 MNIST classifier from 92.64% to 39.4%, and that sparsification-style penalties do not help because defects fall at arbitrary weights. Their flow: (S1) classify weights as significant or insignificant by effect on accuracy; (S2) retrain only the non-defective (adjustable) weights while defective weights are frozen at their measured stuck conductance, with constrained initialization and updates to speed convergence; (S3) remap defects falling on the most significant weights to redundancy columns. Defect statistics (stuck-on [300,1200] uS, stuck-off [0.01,1] uS, normal range [1,300] uS, 64 levels, yield as low as 84% in a 64x64 1T1M array) come from HPE-style TaOx device measurements. Evaluation is software simulation with measured defect distributions on 2-layer (784x10, 92.64%) and 3-layer (784x256, 256x10, 97.82%) MNIST networks over 1,000 random defect maps per setting.

## Contributions
- Measured-data characterisation of random SBF stuck-on/off defects in a TaOx memristor array
- Weight-significance classification showing insignificant weights tolerate defects (<1% degradation)
- Defect-aware retraining that treats stuck cells as fixed weights and retunes the rest, handling both defect types together
- Minimal redundancy-column remapping of only the most significant defects

## Key claims (stable IDs)
- **2017_Liu_DefectRescuing_DAC#C1** — 20% random SBF drops a two-layer MNIST network from 92.64% to 39.4% accuracy. — _support:_ 1,000 random defect maps; average 42.5% in Sec. 4.1 — _loc:_ Sec. 1; Fig. 3b, Fig. 7a
- **2017_Liu_DefectRescuing_DAC#C2** — Retraining recovers normalized accuracy to 98.8% (10% defects) and 98.1% (20% defects) with variation <0.4%; worst case 21.2% -> 97.9%. — _support:_ Acc_real/Acc_ideal — _loc:_ Sec. 4.1, Fig. 7b
- **2017_Liu_DefectRescuing_DAC#C3** — In the 3-layer net, W1 is more defect-sensitive than W2; retraining restores 94.5% from 10% (defects in both) at 20% SBF. — _support:_ W2 alone retained 99.6% — _loc:_ Sec. 4.2, Fig. 7c-d
- **2017_Liu_DefectRescuing_DAC#C4** — Remapping the 5% most significant defects to redundancy columns lifts recovery from 98.1% to 99.3%. — _support:_ gain flattens from 4% to 5% — _loc:_ Sec. 4.3, Fig. 10b

## Results
- Baseline software accuracy 92.64% (2-layer) and 97.82% (3-layer) on MNIST
- 10% SBF: normalized accuracy 59.7% (55.3% real) before rescue
- 20% SBF, 2-layer: 42.5% average (21.2%-63.7%) before; 98.1% after retraining; 99.3% with 5% remap
- 20% SBF, 3-layer: 10% before, 94.5% after retraining

## Key numbers
- array_size: 784x10; 784x256 and 256x10
- accuracy: 98.1% normalized (2-layer, 20% SBF after retraining); 99.3% with 5% remap
- bits_weight: 6b (64 conductance levels)

## Datasets / benchmarks
MNIST

## Limitations
- Tiny fully-connected MNIST networks only; no CNN/transformer
- Requires known per-chip defect map and per-chip retraining
- Redundancy columns add area; analog nonidealities other than SBF (noise, drift, IR drop) not modelled
- Evaluation is simulation using measured defect statistics, not an end-to-end hardware run
- Reported recovery percentages are normalized (Acc_real/Acc_ideal)

## Remarks
An early, heavily cited DAC paper establishing the 'know the fault map, then retrain and remap' recipe for memristor crossbars; later fault-tolerance works treat it as the reference retraining-based approach. The per-chip retraining requirement is its main weakness, motivating retraining-free remapping and noise-aware training. Not directly relevant to LM deployment, but its significance-aware protection of a few weights echoes layer-selective protection ideas for attention weights.

## Cites (in collection, 1)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Emerging technologies such as spin devices and memristor also create new opportunities to develop neuromorphic systems with high scalability and efficiency [8, 9, 10, 11, 12]."

## Cited by (in collection, 14)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "These include (i) (re-)training [16–21], (ii) optimized weight to conductance conversion [14], (iii) rank clipping to reduce the effects of non-idealities by lowering crossbar dimensions [25], (iv) schemes to alleviate the effect of hard failures [26], and (vi) hardware solutions to address low-voltage induced drift [15], programming errors [23], and IR drop [24]."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "the iterative nature of DNN training and careful re-training helps recover the accuracy loss from non-idealities [43], faults [44], and variations [45]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "An alternative way of capturing effects such as stuck-at-faults [14] or device variations [15] is to map the distribution of the variations or defects."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "For example, a defect map or variation distribution [153, 155, 157] of devices in the crossbar can aid the training process by mapping the sensitive cells to defect-free or low variation cells."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "To address this challenge, TIMELY not only leverages algorithm resilience of CNNs/DNNs to counter hardware vulnerability [9, 48, 81], but also minimize potential errors introduced by hardware"
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _contrasts/critiques_: "In [5], redundant columns of ReRAM crossbars are utilized as a substitution for the defect ReRAM columns. But this method not only introduces nontrivial area overhead, but also increases design complexity of peripheral circuit."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "The first one is retraining [100–103]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "The first category includes device defects (e.g., stuck-at-high or stuckat-low resistance [12]) and device reliability issues (e.g., retention failure [13] and resistance drift [14]) that are mostly deterministic in nature and have been addressed in prior work [15–20]."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _background_: "Potential solutions do exist but many of them introduce a number of trade-offs. [in-situ (re)training of weights (or just a subset of them) to recover from the effects of nonidealities [15–19]]"
- [2023_Ma_SAFVariationTolerantMapping_JETC](2023_Ma_SAFVariationTolerantMapping_JETC.md) SAF/Variation Remapping (2023) — _baseline/comparison_: "Although [15] can also reach 95% recovery accuracy, our proposed method doesn't need the retraining process which is a very costly process for platforms [27]."
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2022_Chen_WRAP_DATE](2022_Chen_WRAP_DATE.md) WRAP (2022)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2017_Liu_DefectRescuing_DAC.pdf](../../06_Nonidealities_and_Reliability/2017_Liu_DefectRescuing_DAC.pdf)
- Full text: [../fulltext/2017_Liu_DefectRescuing_DAC.txt](../fulltext/2017_Liu_DefectRescuing_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3061639.3062310
