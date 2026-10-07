---
id: W4386352784
key: 2023_Benmeziane_AnalogNAS_EDGE
title: "AnalogNAS: A Neural Network Design Framework for Accurate Inference with Analog In-Memory Computing"
short: "AnalogNAS"
year: 2023
venue: "EDGE"
venue_full: "2023 IEEE International Conference on Edge Computing and Communications (EDGE 2023)"
authors: "Hadjer Benmeziane, Corey Lammie, Irem Boybat, Malte J. Rasch, Manuel Le Gallo, Hsinyu Tsai, R. Muralidhar, Smaïl Niar, Hamza Ouarnoughi, Vijay Narayanan, Abu Sebastian, Kaoutar El Maghraoui"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["nas-codesign", "hardware-aware-training", "conductance-drift", "noise-injection", "weight-mapping", "edge-ai", "cnn-accelerator", "chip-demo"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 7
citations_overall: 12
priority_score: 5.71
doi: "https://doi.org/10.1109/edge60047.2023.00045"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2023_Benmeziane_AnalogNAS_EDGE.pdf"
fulltext: "../fulltext/2023_Benmeziane_AnalogNAS_EDGE.txt"
---

# AnalogNAS

**AnalogNAS: A Neural Network Design Framework for Accurate Inference with Analog In-Memory Computing** — 2023 IEEE International Conference on Edge Computing and Communications (EDGE 2023) (2023)

## TL;DR
AnalogNAS combines an XGBoost ranking surrogate trained on ~1,000 HWA-trained ResNet-like networks with evolutionary search to find drift-robust CNNs for analog IMC; the 417K-parameter T500 model reaches 92.07% on a 64-core PCM chip vs 89.55% for ResNet32.

## Summary
Standard NAS search spaces (e.g., depthwise-separable MobileNet blocks) suit digital hardware but lose accuracy on analog PCM IMC because of noise and conductance drift. AnalogNAS defines a ResNet-like search space (first-layer channels and kernel, 1-5 main blocks, 1-16 residual blocks, 1-12 branches, 4 conv-block types, widening factor 1-4; Table I). Candidate networks are HWA-trained with IBM AIHWKit under weight-noise levels 0.1-5.0 and 256/512 tiles; a surrogate trained with pairwise hinge ranking loss predicts the ranking by 1-day accuracy plus the accuracy variation over one month (AVM) and 1-day accuracy standard deviation (XGBoost wins in Kendall's tau, Fig. 5). An evolutionary search (population 200, 200 iterations, Latin hypercube init, top-50% selection, depth/width/other mutations) maximizes accuracy/sigma under constraints on parameter count T_p and AVM <= T_AVM. Weights of conv and linear layers map to PCM tiles via differential weight mapping; DAC/ADC are included in AIHWKit simulations and the hardware experiment runs MVMs on IBM's 64-core PCM chip (256x256 cores) with other ops on a host via FPGA. Tasks are CIFAR-10, Visual Wake Words and Keyword Spotting. Searches take ~17 minutes after surrogate training.

## Contributions
- Analog-IMC-oriented ResNet-like search space with tunable width, depth, branches
- HWA-trained architecture dataset and XGBoost ranking surrogate predicting 1-day accuracy and drift robustness
- Constrained evolutionary search over parameters and tile count with noise/drift in the loop
- Hardware validation on a 64-core PCM IMC chip and analysis of why wide/shallow nets suit analog tiles

## Key claims (stable IDs)
- **2023_Benmeziane_AnalogNAS_EDGE#C1** — AnalogNAS T500 beats ResNet32 in simulated accuracy and drift robustness at fewer parameters — _support:_ +1.86% 1-day accuracy and 1.8% drop after one month vs 5.04% for ResNet32 — _loc:_ Sec. VI-B, Fig. 7
- **2023_Benmeziane_AnalogNAS_EDGE#C2** — Hardware accuracy confirms simulated ranking — _support:_ 92.07% (T500) vs 89.55% (ResNet32) mean over five repetitions on PCM chip; text reports 92.05% vs 89.87% — _loc:_ Sec. VII-A, Table IV
- **2023_Benmeziane_AnalogNAS_EDGE#C3** — AnalogNAS finds more accurate models than hand-designed tiny networks on VWW and KWS — _support:_ VWW T200: +2.44% over AnalogNet-VWW and +5.1% over Micronets-VWW; KWS: 96.8% with 2.3% drop vs 4.72% average drop for SOTA — _loc:_ Sec. VI-B
- **2023_Benmeziane_AnalogNAS_EDGE#C4** — Wider, shallower networks are more efficient on analog IMC — _support:_ T500 uses 27 tiles and 0.108 ms vs 43 tiles and 0.434 ms for ResNet32; 54,502 vs 43,956.7 inferences/s/W (simulated) — _loc:_ Sec. VII-B, Table IV

## Results
- T100 (CIFAR-10): +7.98% accuracy with 5.14% one-month drop vs 10.1% for ResNet-V1 (MLPerf Tiny), at 1.23x its size (Sec. VI-B)
- T1M outperforms Wide-ResNet by +0.86% 1-day accuracy with 1.16% vs 6.33% drop; ~86x smaller than 36.5M-parameter WRN
- Average std over drift times 0.43 (AnalogNAS) vs 0.97 (SOTA) on CIFAR-10
- Beats random search (4h) and FLASH / mu-nas baselines in accuracy and search time (Fig. 8)
- T_AVM 3-5% gives 93.71% with 17.65-28.12 min search; T_AVM=1% gives 88.7% (Table III)

## Key numbers
- array_size: 256x256 PCM cores (64-core chip); simulated 512x512 tiles
- energy_eff: 54,502 inferences/s/W (T500, simulated)
- throughput: 0.108 ms execution (T500, simulated)
- accuracy: 92.07% CIFAR-10 on PCM chip (T500) vs 89.55% ResNet32

## Datasets / benchmarks
CIFAR-10, Visual Wake Words, Google Speech Commands (KWS)

## Limitations
- Image/audio CNN tasks only; no transformers or language models
- Surrogate and search are specific to a hardware configuration (tile size, noise level) and task
- Hardware validation uses only two networks, with non-MVM operations executed on a host
- Tile utilization is poor for both networks and left as future work
- Minor inconsistency between hardware accuracies in text and Table IV

## Remarks
A useful demonstration that architecture is a lever for analog robustness beyond HWA training, validated on a real PCM chip. The wide-and-shallow lesson mirrors tile-utilization arguments for crossbars, but scaling surrogate-based NAS to billion-parameter language models would be very costly. Builds on IBM's AIHWKit and HWA-training work and is complementary to post-training methods such as Lammie 2024.

## Cites (in collection, 7)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Many types of memory devices, including Flash memory, PCM, and Resistive Random Access Memory (RRAM), can be used for IMC [2]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Analog IMC [1] can provide radical improvements in performance and power efficiency, by leveraging the physical properties of memory devices to perform computation and storage at the same physical location."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "Each sampled architecture is trained using different levels of weight noise and HWA training hyper-parameters using the AIHWKit [21]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _uses-method-or-tool_: "We conducted power performance simulations for AnalogNAS T500 and ResNet32 models using a 2D-mesh based heterogeneous analog IMC system with the simulation tool presented in [46]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _uses-method-or-tool_: "An experimental hardware accuracy validation study was performed using a 64-core IMC chip based on PCM [44]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "The AIHWKit is an open-source Python toolkit for exploring and using the capabilities of in-memory computing devices in the context of artificial intelligence and has been used for HWA training of standard DNNs with hardware-calibrated device noise and drift models [22]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _uses-method-or-tool_: "Each core comprises a crossbar array of 256x256 PCM-based unit-cells along with a local digital processing unit [45]."

## Cited by (in collection, 2)
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _contrasts/critiques_: "Current state-of-the-art HW-NAS frameworks for CIM primarily focus on optimizing neural network models for hardware implementation [15–17], performing hardware design space exploration separately [9, 18, 19], or jointly optimizing model parameters with a limited set of hardware parameters [20, 21]."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _background_: "The rationale behind this approach is that larger layers have more redundancy and, hence, more leeway to compensate for the perturbations induced by analog computing [5, 6]."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2023_Benmeziane_AnalogNAS_EDGE.pdf](../../07_Hardware_Aware_Training_and_Robustness/2023_Benmeziane_AnalogNAS_EDGE.pdf)
- Full text: [../fulltext/2023_Benmeziane_AnalogNAS_EDGE.txt](../fulltext/2023_Benmeziane_AnalogNAS_EDGE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/edge60047.2023.00045
