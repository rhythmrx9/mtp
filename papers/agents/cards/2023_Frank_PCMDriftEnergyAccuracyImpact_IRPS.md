---
id: W4376606760
key: 2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS
title: "Impact of Phase-Change Memory Drift on Energy Efficiency and Accuracy of Analog Compute-in-Memory Deep Learning Inference (Invited)"
short: "PCM Drift Energy-Accuracy Impact"
year: 2023
venue: "IRPS"
venue_full: "2023 IEEE International Reliability Physics Symposium (IRPS 2023), invited paper"
authors: "Martin M. Frank, Ning Li, Malte J. Rasch, Shubham Jain, Ching-Tzu Chen, R. Muralidhar, Jin‐Ping Han, Vijay Narayanan, Timothy M. Philip, Kevin W. Brew, Andrew H. Simon, Iqbal Saraf et al."
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["PCM"]
models: ["BERT", "Transformer", "CNN", "LSTM/RNN"]
lm_models: ["BERT"]
param_scale: ""
slm: true
evidence: simulation
topics: ["conductance-drift", "weight-mapping", "device-variation", "endurance-retention", "transformer-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 12
citations_overall: 7
priority_score: 7.06
doi: "https://doi.org/10.1109/irps48203.2023.10117874"
pdf: null
fulltext: null
---

# PCM Drift Energy-Accuracy Impact

**Impact of Phase-Change Memory Drift on Energy Efficiency and Accuracy of Analog Compute-in-Memory Deep Learning Inference (Invited)** — 2023 IEEE International Reliability Physics Symposium (IRPS 2023), invited paper (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IBM invited IRPS paper showing that projection-liner PCM with a two-pairs-of-varying-significance weight mapping keeps BERT accuracy loss minimal after long drift, and that drift actually raises peak VMM energy efficiency of a 14 nm heterogeneous CIM accelerator by 3-15% over one day to ten years (sustained gains <10% for CNN/LSTM/Transformer).

## Summary
Resistance drift in analog phase-change memory lowers conductances over time and threatens inference accuracy of compute-in-memory (CIM) accelerators. The paper first discusses mitigating drift and noise by integrating projection liners into mushroom-type PCM cells, including the tradeoff with reduced dynamic range. It then evaluates the resulting inference accuracy on the Transformer-based language model BERT, mapping each weight onto two pairs of liner PCM devices of differing significance, and reports minimal accuracy loss after extended drift with an optimized mapping. Finally, combining drift, circuit and architecture simulations of a previously proposed heterogeneous 14 nm CIM accelerator, it quantifies how drift-induced conductance decay reduces column currents and hence VMM energy, finding that peak VMM energy efficiency increases by 3-15% over one day to ten years for typical drift coefficients, and sustained efficiency for CNN, LSTM and Transformer benchmarks rises by less than 10%, most for analog-dominated models. Longer VMM integration times amplify the energy impact of drift.

## Language models evaluated
- Models: BERT
- Scale: —

## Contributions
- Discussion of drift/noise mitigation via projection-liner mushroom PCM and its dynamic-range tradeoff
- BERT inference-accuracy study under drift using a 2-pair (varying significance) liner-PCM weight mapping
- Joint drift + circuit + architecture simulation quantifying how drift changes VMM and end-to-end energy efficiency of a 14 nm heterogeneous CIM accelerator
- Benchmark-level energy analysis for CNN, LSTM and Transformer workloads

## Key claims (stable IDs)
- **2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS#C1** — With an optimized mapping onto two pairs of liner PCM devices of varying significance, BERT accuracy loss after extended drift can be minimal — _support:_ stated in abstract (no numbers available without full text) — _loc:_ Abstract
- **2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS#C2** — Drift increases peak VMM energy efficiency of a heterogeneous 14 nm CIM accelerator — _support:_ 3% to 15% increase from one day to ten years for a range of typical drift coefficients — _loc:_ Abstract
- **2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS#C3** — Sustained end-to-end energy-efficiency gain from drift is small and workload-dependent — _support:_ below 10% for CNN, LSTM and Transformer benchmarks; greatest for models dominated by analog computation — _loc:_ Abstract
- **2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS#C4** — Longer VMM integration times increase the energy impact of drift — _support:_ stated in abstract — _loc:_ Abstract

## Results
- Peak VMM energy efficiency rises 3-15% over 1 day to 10 years of drift (14 nm heterogeneous CIM accelerator, typical drift coefficients)
- Sustained energy-efficiency increase < 10% for CNN, LSTM and Transformer benchmarks

## Limitations
- Abstract-only analysis here: specific BERT accuracy numbers, drift coefficients and device data could not be verified
- Energy results are from simulation of a proposed (not fabricated) 14 nm heterogeneous accelerator
- Energy 'benefit' of drift comes from shrinking currents, which simultaneously reduces signal/SNR; it is not a design lever by itself
- Invited 4-page-style reliability-symposium paper; largely synthesizes prior IBM device and architecture work

## Remarks
Useful as a systems-level perspective linking a device non-ideality (PCM drift) to both accuracy and energy, with the counter-intuitive point that drift slightly improves energy efficiency rather than only hurting accuracy. The accuracy side builds on IBM's projection-liner PCM and multi-device significance mapping, and on hardware-aware training (Joshi et al. 2020; Rasch et al. 2023 AIHWKit) and the 14 nm heterogeneous accelerator architecture (Jain et al. 2022). Without full text the strength of the BERT accuracy evidence cannot be judged; treat numbers as simulation-based.

## Cites (in collection, 12)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022)
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)

## Cited by (in collection, 2)
- [2025_Xu_UniCAIM_DAC](2025_Xu_UniCAIM_DAC.md) UniCAIM (2025) — _background_: "In recent years, various emerging NVMs, such as resistive random-access memory (RRAM), magnetic tunnel junction (MTJ) and FeFET, have triggered lots of attention for CIM, due to the high storage density and efficient GEMV operation via analog computing within the memory array [26-28]."
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/irps48203.2023.10117874
