---
id: W4407751056
key: 2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun
title: "The inherent adversarial robustness of analog in-memory computing"
short: "AIMC-Adversarial-Robustness"
year: 2025
venue: "NatCommun"
venue_full: "Nature Communications"
authors: "Corey Lammie, Julian Büchel, Athanasios Vasilopoulos, Manuel Le Gallo, Abu Sebastian"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["CNN", "ResNet", "Transformer"]
lm_models: ["RoBERTa-base (~125M, MNLI; simulation)"]
param_scale: "~125M"
slm: true
evidence: device-experiment
topics: ["security-robustness", "read-write-noise", "hardware-aware-training", "noise-injection", "chip-demo", "language-models", "attention", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 8
citations_overall: 12
priority_score: 8.21
doi: "https://doi.org/10.1038/s41467-025-56595-2"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.pdf"
fulltext: "../fulltext/2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.txt"
---

# AIMC-Adversarial-Robustness

**The inherent adversarial robustness of analog in-memory computing** — Nature Communications (2025)

## TL;DR
Experiments on the IBM HERMES PCM AIMC chip show that intrinsic stochastic noise lowers adversarial success rate (PGD, Square, OnePixel) versus digital 4b/8b and FP32 baselines for a ResNet9 on CIFAR-10, and chip-model simulations show the effect persists for a ~125M-parameter RoBERTa on MNLI under GBDA text attacks.

## Summary
The paper tests the conjecture that stochastic analog hardware is inherently more robust to evasion adversarial attacks. A ResNet9-style CNN (CIFAR-10) is hardware-aware (HWA) trained with noise injection and deployed on a 64-core HERMES PCM chip with 256x256 tiles (four PCM per unit cell, two per signed weight); five targets are compared: original FP32, HWA-retrained FP32, a digital accelerator (8-bit activations, 4-bit weights), a PCM chip model (programming noise as polynomial-fit Gaussian, read noise as conductance-dependent LUT, additive Gaussian output noise), and the real chip. Attacks (PGD, Square, OnePixel) are generated on the chip model and evaluated on hardware, measured with Adversarial Success Rate over attack iteration/magnitude 'envelopes'. A modified chip model isolates noise source properties (type = input-dependence, magnitude, location, recurrence), and hardware-in-the-loop attacks with chip access are studied using representative-weight inference to counter conductance drift. For NLP, a RoBERTa model fine-tuned on MNLI with HWA training is simulated with the chip model (it exceeds chip capacity) under GBDA with BERTScore semantic constraints.

## Language models evaluated
- Models: RoBERTa-base (~125M, MNLI; simulation)
- Scale: ~125M

## Contributions
- First experimental validation of adversarial robustness of a PCM AIMC chip
- Analysis showing noise type and magnitude (not recurrence/location) drive robustness; output noise gives most robustness, weight noise least
- Hardware-in-the-loop attack methodology accounting for drift and noise
- Simulation extension to a ~125M-parameter transformer on MNLI
- Standardized, extendable ASR-based evaluation methodology

## Key claims (stable IDs)
- **2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun#C1** — HWA retraining improves robustness over the original FP32 model; digital accelerator even more; AIMC chip yields further robustness — _support:_ ASR envelopes ordering — _loc:_ Fig. 2d-f
- **2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun#C2** — Type and magnitude of stochastic noise dominate adversarial robustness; location and recurrence have negligible influence — _support:_ model with only output noise most robust; only weight noise least robust — _loc:_ Sec. noise analysis / Fig. 3c-e
- **2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun#C3** — AIMC chip model and chip at 84.85% and 84.31% test accuracy (drops of 3.57% and 4.11%) are more robust than weight-noise-only model but less than output-noise-only model — _support:_ stated — _loc:_ Fig. 3c-e
- **2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun#C4** — Hardware-in-the-loop attacks are less effective on stochastic hardware, though attacks generated on chip are more effective than those from the chip model — _support:_ Fig. 4 — _loc:_ Fig. 4
- **2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun#C5** — Additional robustness persists for RoBERTa (~125M) on MNLI under GBDA text attacks — _support:_ ASR envelope vs digital — _loc:_ Fig. 5

## Results
- Noise-matched comparisons at 5% and 10% test-accuracy drop with n=1000 repetitions
- ASR averaged over n=10 repetitions for non-deterministic platforms
- AIMC chip: 256x256 tiles, four PCM per unit cell; digital baseline 8b activations/4b weights
- RoBERTa exceeds HERMES chip capacity so was only simulated (HWA fine-tuned on MNLI; 393K train / 20K test)

## Key numbers
- tech_node: 14nm (HERMES chip)
- array_size: 256x256 tiles, 64 cores
- accuracy: 84.31% CIFAR-10 on chip (84.85% chip model)
- bits_weight: PCM analog (2 devices/weight); digital baseline 4b
- bits_adc: 8-bit activations

## Datasets / benchmarks
CIFAR-10, MNLI (GLUE)

## Limitations
- Hardware experiments only for the ResNet9 CIFAR-10 model; transformer results are simulation with a calibrated chip model
- Only evasion attacks; no poisoning, backdoor or side-channel
- Robustness expected to shrink as noise is reduced by better devices/circuits
- Hardware-in-the-loop attacks assume representative-weight inference and drift counter-measures
- Robustness stems from accuracy-reducing noise (3-4% drop), so it is a trade-off, not free

## Remarks
Shows a security-relevant side effect of analog noise, with the useful nuance that input-independent output noise helps most. It is one of few works to touch transformer NLP on a PCM chip model, although only ~125M-scale RoBERTa classification, not generative LMs. The chip-model fidelity (polynomial programming noise, LUT read noise) matters for extrapolating to larger LMs.

## Cites (in collection, 8)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "One such compute substrate which shows significant promise for adversarial robustness is that based on analog in-memory computing (AIMC)6–8."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "However, Hardware-Aware (HWA) training, where the DNN is made robust via the injection of weight noise during the training process, has been found to recover much of the accuracy loss11,12."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _contrasts/critiques_: "While automated ML-based in-the-loop modeling40 approaches can be utilized, they require a significant amount of data, which is instance-specific."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "One such compute substrate which shows significant promise for adversarial robustness is that based on analog in-memory computing (AIMC)6–8."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _uses-method-or-tool_: "To experimentally study the adversarial robustness, we employed a PCM-based AIMC chip with tiles comprising 256 × 256 synaptic unit cells29."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "However, Hardware-Aware (HWA) training, where the DNN is made robust via the injection of weight noise during the training process, has been found to recover much of the accuracy loss11,12."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "We refer the reader to Le Gallo et al.54 for a comprehensive tutorial on HWA training using IBM AIHWKIT."
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _uses-method-or-tool_: "Post-training optimizations58 are then performed to tune the (i) input range of each AIMC tile and the (ii) maximum conductance range of each column."

## Cited by (in collection, 2)
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "Analog Hardware-Aware (AHWA) training techniques have been demonstrated to enhance model robustness under these constraints for various NN architectures, effectively mitigating accuracy losses by injecting Gaussian noise during forward-propagation and simulating circuit-non-idealities11–13."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.pdf](../../07_Hardware_Aware_Training_and_Robustness/2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.pdf)
- Full text: [../fulltext/2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.txt](../fulltext/2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-025-56595-2
