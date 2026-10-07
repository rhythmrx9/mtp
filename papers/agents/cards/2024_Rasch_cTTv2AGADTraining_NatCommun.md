---
id: W4401729360
key: 2024_Rasch_cTTv2AGADTraining_NatCommun
title: "Fast and robust analog in-memory deep neural network training"
short: "c-TTv2/AGAD"
year: 2024
venue: "NatCommun"
venue_full: "Nature Communications, vol. 15, article 7133 (2024)"
authors: "Malte J. Rasch, Fabio Carta, Omobayode I. Fagbohungbe, Tayfun Gokmen"
category: "10 On-chip & Analog Training"
devices: ["ReRAM", "ECRAM", "Charge/Capacitor", "Generic-NVM"]
models: ["MLP", "CNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["on-chip-training", "analog-mvm", "device-variation", "endurance-retention", "calibration-compensation", "read-write-noise", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 12
citations_overall: 39
priority_score: 4.52
doi: "https://doi.org/10.1038/s41467-024-51221-z"
pdf: "../../10_On_Chip_and_Analog_Training/2024_Rasch_cTTv2AGADTraining_NatCommun.pdf"
fulltext: "../fulltext/2024_Rasch_cTTv2AGADTraining_NatCommun.txt"
---

# c-TTv2/AGAD

**Fast and robust analog in-memory deep neural network training** — Nature Communications, vol. 15, article 7133 (2024) (2024)

## TL;DR
Two in-memory training algorithms, Chopped-TTv2 and Analog Gradient Accumulation with Dynamic reference (AGAD), remove Tiki-Taka v2's need for precisely programmed zero-reference conductances (c-TTv2 tolerates ~25% offset, AGAD any offset and symmetric devices) while keeping O(1)-per-update runtime, ~2 orders of magnitude faster updates than digital-gradient mixed-precision training in estimates.

## Summary
Analog in-memory training needs the gradient accumulation and update to be as fast as the O(1) analog forward/backward MVM. Mixed-precision training accumulates gradients digitally, costing O(N^2) FP operations per update; plain in-memory SGD with coincident pulse trains (Gokmen) requires unrealistically symmetric devices. Tiki-Taka v2 (TTv2) accumulates gradients in a separate array A against a reference array R (differential read), low-pass filters digitally, and periodically transfers to the weight array W, needing only O(N) digital ops but needing the reference to match the device symmetry point (SP) within a few percent. c-TTv2 adds the chopper technique (periodic/random sign flips) to cancel residual offsets, relaxing reference error to ~25%. AGAD instead computes the reference on the fly as a running estimate of the recent conductance dynamics using modest digital compute, so no reference array or differential read is needed and both symmetric and asymmetric devices work. Simulations use AIHWKit with device models parameterised by number of states (20 states for ReRAM-like noisy devices up to many for ECRAM-like), reference offset sigma_r, and asymmetry; benchmarks are a 3-layer FC net and LeNet on MNIST and a 2-layer LSTM on War and Peace. Runtime (Table 1), endurance and retention requirements are analysed analytically.

## Contributions
- c-TTv2: chopper-stabilised gradient accumulation tolerant to reference errors up to ~25%
- AGAD: dynamic on-the-fly reference removing the need for reference conductance programming and differential read
- Analysis of requirements on device noise (states), asymmetry, endurance and retention
- Dynamic learning-rate scheme for diverse DNNs and per-sample runtime estimates vs mixed-precision and in-memory SGD

## Key claims (stable IDs)
- **2024_Rasch_cTTv2AGADTraining_NatCommun#C1** — TTv2 fails with small reference errors: weight error rises from ~5% to ~9% (20 states) once reference offset sigma_r >= 0.1 (5% of weight range), while weight programming errors are typically at least 5-10%. — _support:_ Fig. 4A-B — _loc:_ Results
- **2024_Rasch_cTTv2AGADTraining_NatCommun#C2** — c-TTv2 maintains weight error for large offsets (sigma_r up to 0.5) with few states; AGAD is invariant to reference offsets. — _support:_ Fig. 4C-D, Fig. 5 — _loc:_ Results
- **2024_Rasch_cTTv2AGADTraining_NatCommun#C3** — AGAD's weight error is independent of device asymmetry, unlike TTv2/c-TTv2 which require some asymmetry. — _support:_ Fig. 6 (asymmetry varied by saturation bounds) — _loc:_ Results
- **2024_Rasch_cTTv2AGADTraining_NatCommun#C4** — Devices holding the accumulation array need ~4 orders of magnitude more endurance (0.5-4 pulses per sample) than the weight array (2e-4 to 4e-4 pulses per sample). — _support:_ LeNet/MNIST pulse counts — _loc:_ Endurance paragraph
- **2024_Rasch_cTTv2AGADTraining_NatCommun#C5** — Both algorithms keep TTv2's fast runtime with ~two orders of magnitude update-time improvement versus digital gradient accumulation (mixed precision). — _support:_ Table 1 assuming 0.7 TFLOPS shared by 4 crossbars, N=512, 40 ns MVM, 5 ns pulse — _loc:_ Runtime estimates

## Results
- MNIST FC-3 and LeNet and War & Peace LSTM trained to near-FP accuracy by c-TTv2 and AGAD across reference offsets; TTv2 degrades
- In-memory SGD gives weight error >25% vs TTv2 ~5% at 20 states
- c-TTv2 tolerates reference drift up to 25% (sigma_r=0.5) versus ~5% for TTv2
- Per-sample update time dominated by digital compute: O(N) ops for TTv2/c-TTv2/AGAD vs O(2N^2+N) for mixed precision

## Key numbers
- array_size: N=512 assumed for runtime
- throughput: ~2 orders of magnitude faster update than mixed-precision (estimate)
- accuracy: near-FP accuracy on MNIST (FC-3, LeNet) and LSTM text prediction under reference offsets
- bits_weight: 20 device states (ReRAM-like) to many (ECRAM)

## Datasets / benchmarks
MNIST, War and Peace (character-level text)

## Limitations
- Simulation only (AIHWKit) with parameterised device models, not measured arrays
- Small benchmarks (MNIST, LeNet, small LSTM); no transformers or large-scale training
- Runtime figures are analytical estimates with assumed digital throughput
- AGAD needs extra digital compute and on-chip memory for the dynamic reference
- Retention/endurance targets are model-derived

## Remarks
Methodologically solid algorithmic advance from the IBM analog-AI group (Tiki-Taka/AIHWKit lineage) targeting a practical blocker for fully analog training: precise reference programming. It bridges device properties (asymmetry, states, retention, endurance) with algorithm requirements, but lacks hardware validation. Relevance to LM deployment is indirect: it addresses training rather than inference, and benchmarks are far below transformer scale.

## Cites (in collection, 12)
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018) — _background_: "Analog in-memory computing AIMC is a promising future hardware technology for accelerating deep-learning workloads. Great energy efficiency is achieved by representing weight matrices in resistive elements of crossbar arrays and using basic physical laws of electrostatics (Kirchhoff's and Ohm's laws) to compute ubiquitous matrix-vector multiplications (MVMs) directly in memory in essentially constant time O(1)1-5."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Analog in-memory computing AIMC is a promising future hardware technology for accelerating deep-learning workloads. Great energy efficiency is achieved by representing weight matrices in resistive elements of crossbar arrays and using basic physical laws of electrostatics (Kirchhoff's and Ohm's laws) to compute ubiquitous matrix-vector multiplications (MVMs) directly in memory in essentially constant time O(1)1-5."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "For simulations, we use the PyTorch-based open source toolkit (AIHWKit)29, where we have implemented the proposed algorithms (see also Supplementary Fig. 4)."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _data/numbers_: "For approximate numbers, we assume that a single update pulse would take approximately 5 ns, a single MVM about 40 ns39, and that the memory operations can be hidden behind the compute40."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _contrasts/critiques_: "Note that this in-memory training approach is radically different from hardware-aware training typically employed when using analog crossbar arrays for DNN inference only (e.g.,32,41,42)."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _contrasts/critiques_: "For instance, it has recently been shown in simulation that with realistic MVM assumptions many large-scale DNNs can be deployed without significant accuracy drop on AIMC inference hardware when retrained properly32."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Using resistive crossbar arrays to compute an MVM in-memory has been suggested early on46, and multiple prototype chips where MVMs of DNNs during inference are accelerated have been recently described6-9,11,47."

## Cited by (in collection, 1)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2024_Rasch_cTTv2AGADTraining_NatCommun.pdf](../../10_On_Chip_and_Analog_Training/2024_Rasch_cTTv2AGADTraining_NatCommun.pdf)
- Full text: [../fulltext/2024_Rasch_cTTv2AGADTraining_NatCommun.txt](../fulltext/2024_Rasch_cTTv2AGADTraining_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-024-51221-z
