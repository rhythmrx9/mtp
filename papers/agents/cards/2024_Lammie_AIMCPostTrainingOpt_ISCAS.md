---
id: W4400233540
key: 2024_Lammie_AIMCPostTrainingOpt_ISCAS
title: "Improving the Accuracy of Analog-Based In-Memory Computing Accelerators Post-Training"
short: "AIMC Post-Training Optimization"
year: 2024
venue: "ISCAS"
venue_full: "IEEE International Symposium on Circuits and Systems (ISCAS 2024)"
authors: "Corey Lammie, Athanasios Vasilopoulos, Julian Büchel, Giacomo Camposampiero, Manuel Le Gallo, Malte J. Rasch, Abu Sebastian"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["Transformer", "BERT"]
lm_models: ["RoBERTa-base"]
param_scale: "125M"
slm: true
evidence: algorithm+simulation
topics: ["hardware-aware-training", "calibration-compensation", "adc-dac", "noise-injection", "conductance-drift", "language-models", "quantization"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 6
citations_overall: 10
priority_score: 8.53
doi: "https://doi.org/10.1109/iscas58744.2024.10558540"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2024_Lammie_AIMCPostTrainingOpt_ISCAS.pdf"
fulltext: "../fulltext/2024_Lammie_AIMCPostTrainingOpt_ISCAS.txt"
---

# AIMC Post-Training Optimization

**Improving the Accuracy of Analog-Based In-Memory Computing Accelerators Post-Training** — IEEE International Symposium on Circuits and Systems (ISCAS 2024) (2024)

## TL;DR
Two post-training procedures that set per-tile DAC input range and per-column conductance range cut HWA-training complexity: on a PCM-calibrated simulation of RoBERTa-base they lift the GLUE average from 76.3 to 81.6, within ~0.1% of learning the ranges during training.

## Summary
HWA training for AIMC normally learns input (DAC) ranges and per-column conductance ranges, which needs hardware-specific information and tile-aware training and is costly for large models. Inspired by post-training quantization, the authors propose (1) input range optimization, setting each tile's input range X_r to the K-th percentile of N collected input samples, which trades input clipping against effective ADC resolution; and (2) conductance range optimization, which per bit line estimates the output current statistics (mean + L standard deviations) on N=2 input samples, rescales the column's maximum conductance (G_BL_max) to avoid ADC saturation or to boost signal-to-noise. RoBERTa-base (124.6M parameters, 85.6M mapped, 486 tiles of 512x512, 61.57% average tile utilization) is fine-tuned per GLUE task for 20 epochs (AdamW, lr 5e-5) with additive weight noise 0.06 and output noise 0.1 in AIHWKit, symmetric weight mapping with unrolled layers distributed evenly. The hardware model is an experimentally calibrated PCM model from a 1M-device array: 8-bit PWM inputs, differential mapping with G_max=25 uS, 8-bit ADCs, programming, read, drift and output noise, IR drop with 0.35 ohm between cross-points; auxiliary ops in FP. Scores are averaged over 10 repetitions at t=1 h across configurations that toggle weight clipping, I/O quantization, learned versus post-training input and conductance ranges.

## Language models evaluated
- Models: RoBERTa-base
- Scale: 125M

## Contributions
- Post-training input (DAC) range optimization by percentile of collected inputs
- Post-training per-column conductance range optimization based on predicted ADC saturation current
- Ablation over learned vs post-training ranges on RoBERTa across eight GLUE tasks
- Baseline GLUE scores for RoBERTa on simulated PCM-based AIMC

## Key claims (stable IDs)
- **2024_Lammie_AIMCPostTrainingOpt_ISCAS#C1** — Post-training optimization recovers accuracy when ranges are not learned — _support:_ average +5.3% recovery vs only weight clipping and I/O quantization — _loc:_ Sec. VI, Table II
- **2024_Lammie_AIMCPostTrainingOpt_ISCAS#C2** — Post-training ranges nearly match learned ranges — _support:_ average score only 0.1% lower than learning both ranges vs 5.3% lower without PT optimization — _loc:_ Sec. VI
- **2024_Lammie_AIMCPostTrainingOpt_ISCAS#C3** — Further optimizing learned parameters post-training improves accuracy — _support:_ +0.9% average when both ranges learned and then PT-optimized — _loc:_ Sec. VI
- **2024_Lammie_AIMCPostTrainingOpt_ISCAS#C4** — Overall GLUE average improves with both methods — _support:_ 76.3 -> 81.6 average score — _loc:_ Sec. VII

## Results
- Ideal (FP, noise-free HWA-finetuned weights) GLUE average 85.9; best analog configuration (learned + PT optimized) average 82.6 at t=1h (Table II)
- PT-only configurations (clipping + I/O quant + both PT methods): ~80.9-81.7 average
- Accuracy decays over time due to PCM drift; RTE shown in Fig. 3 over time
- MVM L2 error ~14% at t=0, growing linearly in log time (Fig. 2)

## Key numbers
- array_size: 512x512 tiles (486 tiles for RoBERTa-base)
- accuracy: GLUE average 76.3 -> 81.6 (ideal 85.9)
- bits_weight: PCM differential mapping, G_max=25 uS
- bits_adc: 8b ADC, 8b PWM inputs

## Datasets / benchmarks
GLUE (MNLI, QNLI, QQP, RTE, SST-2, MRPC, CoLA, STS-B)

## Limitations
- Simulation only; no hardware experiments (future work)
- Single model (RoBERTa-base, 125M) and a single hardware configuration
- Significant gap to FP baseline remains (e.g., GLUE average 85.9 vs 82.6) since model not retrained on original corpora
- Auxiliary operations (softmax, layernorm) assumed FP; no regular-calibration study yet
- PT methods require representative calibration inputs and tile-level instrumentation

## Remarks
A practical, low-cost step toward deploying transformers on PCM AIMC without expensive HWA range learning; the calibration framing also suggests periodic range re-estimation to counter drift without reprogramming. Evidence is simulation but with a PCM model calibrated on measured silicon from the same IBM group. It is narrow (one model, one noise model), so scaling behaviour to billion-parameter models is untested; related to AnalogNAS and the IBM HWA-training papers in the collection.

## Cites (in collection, 6)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "To perform realistic hardware simulations, we used an experimentally verified model, calibrated based on extensive measurements performed on an array containing 1 million Phase-Change Memory (PCM) devices [24]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Analog-Based In-Memory Computing (AIMC) accelerators are one such type of accelerator, which have gained significant interest, due to their ability to execute Vector-Matrix Multiplications (VMMs) in O (1) time-complexity [6–8]."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "To perform HWA training, the IBM Analog Hardware Acceleration Kit (AIHWKIT) [19, 20] is used."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "dedicated accelerators are required to accelerate the inference workloads of these models in resource-contained environments [2]-[5]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "While some Hardware-Aware (HWA) training techniques, such as Quantization-Aware Training (QAT), are widely adopted [15], due to the proliferation of reduced precision digital accelerators and deterministic execution flows, others require instance specific information [16]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "To perform HWA training, the IBM Analog Hardware Acceleration Kit (AIHWKIT) [19, 20] is used."

## Cited by (in collection, 3)
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _uses-method-or-tool_: "Post-training optimizations58 are then performed to tune the (i) input range of each AIMC tile and the (ii) maximum conductance range of each column."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _background_: "Post-placement calibration methods42 help mitigate accuracy loss caused by mismatches between the assumed hardware during HWA model adaptations and the actual hardware used for deployment."
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2024_Lammie_AIMCPostTrainingOpt_ISCAS.pdf](../../07_Hardware_Aware_Training_and_Robustness/2024_Lammie_AIMCPostTrainingOpt_ISCAS.pdf)
- Full text: [../fulltext/2024_Lammie_AIMCPostTrainingOpt_ISCAS.txt](../fulltext/2024_Lammie_AIMCPostTrainingOpt_ISCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iscas58744.2024.10558540
