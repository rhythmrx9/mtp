---
id: W4400937214
key: 2024_Wang_LearningInMemoryReview_NeuromorphComputEng
title: "Difficulties and approaches in enabling learning-in-memory using crossbar arrays of memristors"
short: "Learning-in-Memory Review"
year: 2024
venue: "NeuromorphComputEng"
venue_full: "Neuromorphic Computing and Engineering (2024)"
authors: "Wei Juan Wang, Yang Li, Ming Wang"
category: "10 On-chip & Analog Training"
devices: ["Memristor(generic)", "ReRAM", "PCM"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["on-chip-training", "survey", "write-verify-programming", "device-variation", "analog-mvm", "crossbar-architecture", "hardware-aware-training"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 16
citations_overall: 4
priority_score: 2.99
doi: "https://doi.org/10.1088/2634-4386/ad6732"
pdf: "../../10_On_Chip_and_Analog_Training/2024_Wang_LearningInMemoryReview_NeuromorphComputEng.pdf"
fulltext: "../fulltext/2024_Wang_LearningInMemoryReview_NeuromorphComputEng.txt"
---

# Learning-in-Memory Review

**Difficulties and approaches in enabling learning-in-memory using crossbar arrays of memristors** — Neuromorphic Computing and Engineering (2024) (2024)

## TL;DR
Review of how to realise all three deep-learning operations (forward VMM, error backpropagation, weight update) in memristor crossbars, concluding that only forwarding is well solved and that periodical-carry style updates with separated gradient accumulation are the most promising way to tolerate nonlinear, noisy conductance updates.

## Summary
The paper contrasts computing-in-memory (inference with offline-trained weights) with learning-in-memory (LiM), where forwarding, error backpropagation and weight update all occur in the crossbar. Section 2 formalises the three operations (forward VMM, delta propagation by the transpose, outer-product update; 3xmxn MACs per layer per sample) and sizes the computational load (e.g. 784-500-250-10 MLP: 519,500 weights, ~1.5M MACs per image, ~9x10^12 MACs for 100 epochs on MNIST; ResNet-50: 4.1G MACs forward, ~9.4x10^18 MACs for full ImageNet training). Section 3 and 4 review forward and backward VMM through the same crossbar, the unrolling of convolutions into column vectors, the difficulty of backpropagating through convolution layers on crossbars, and ways to bypass backprop (RBM/deep belief nets with contrastive divergence, feedback alignment). Section 5 reviews weight-update schemes under device plasticity non-idealities: the ideal case, Manhattan (sign) rule, stochastic streams, read-write, read-write-verify and periodical carry (multi-device weights incl. Agarwal, Ambrogio and tiki-taka, with optional separate high-precision digital gradient accumulation). The discussion argues that blind writes are most efficient but need ideal devices, closed-loop read-write-verify tolerates non-ideality but is too expensive for in-situ learning, and periodical carry variants are most promising but need hardware validation. The work is qualitative; it provides no new experiments.

## Contributions
- Frames the transition from computing-in-memory to learning-in-memory and the extra operations required
- Quantifies the MAC load of forward, backward and update steps for small and large networks
- Systematic comparison of weight-update schemes (Manhattan, stochastic, read-write, read-write-verify, periodical carry) against device non-idealities
- Identifies difficulties of backpropagation in convolutional layers and algorithmic bypasses (RBM/DBN, feedback alignment)

## Key claims (stable IDs)
- **2024_Wang_LearningInMemoryReview_NeuromorphComputEng#C1** — Only information forwarding is well studied on crossbars; error backpropagation and weight updates have no clear implementation path — _support:_ most chip demos [5-12] are inference-only; updates are offline or closed-loop — _loc:_ Sec. 1 and Sec. 6
- **2024_Wang_LearningInMemoryReview_NeuromorphComputEng#C2** — Training one layer needs 3 x m x n MACs per sample (forward, backward, update) — _support:_ 784-500-250-10 MLP: 519,500 weights, ~1.5M MACs/image — _loc:_ Sec. 2.4
- **2024_Wang_LearningInMemoryReview_NeuromorphComputEng#C3** — Periodical carry (and separate gradient accumulation) tolerates nonlinear and noisy updates with low peripheral complexity and fewer writes — _support:_ cited Agarwal, Ambrogio (PCM+capacitor) and tiki-taka — _loc:_ Sec. 5.3.5, Sec. 6
- **2024_Wang_LearningInMemoryReview_NeuromorphComputEng#C4** — Closed-loop read-write-verify tolerates most non-idealities but is too expensive for practical in-situ learning — _support:_ qualitative cost argument — _loc:_ Sec. 6

## Results
- Qualitative review - no new measurements
- Compute-load examples: MNIST MLP ~9x10^12 MACs for 100 epochs; ResNet-50 ~9.4x10^18 MACs (1.28M images, 128 epochs) (Sec. 2.4)
- Comparison of five update schemes by circuit complexity, write count and tolerance to nonlinearity/write variation (Sec. 5.3, Sec. 6)

## Datasets / benchmarks
MNIST

## Limitations
- No new experiments or quantitative benchmark across schemes; largely a qualitative synthesis
- Focus on MLP/CNN and fully connected layers; no treatment of transformers, attention or language-model training/fine-tuning
- Most cited update-scheme evidence is simulation-level; real-hardware validation is called for by the authors
- Weighted toward memristors; limited coverage of PCM/other devices

## Remarks
Useful primer on why on-chip analog training remains largely unsolved: the bottleneck is non-ideal, asymmetric conductance updates and the cost of peripheral write circuitry, not forward MVMs. The advice to separate gradient accumulation into digital memory and update analog arrays sparsely is consistent with the tiki-taka line implemented in AIHWKIT. For LM work, the review is background only - no discussion of adapter/LoRA-style on-chip fine-tuning, which is where analog training could become relevant for SLMs.

## Cites (in collection, 16)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Manhattan update rule In the Manhattan learning rule, the amount of weight changes is disregarded, leaving only the direction of weight changes [33, 48, 49]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _motivation_: "The non-uniform conductance change under identical write pulses would be a major problem of the online training [50, 54]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _motivation_: "Thus it is of great interest to enable online training or online learning, which refers to the scheme that conducts all three essential operations of a deep neural network in memristive crossbar arrays [18]."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "Ambrogio et al proposed to use memristive devices as the high significant weights and capacitor-based artificial synapses as the low significant weights [58–60]."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "By coordinating the applied read voltages and measurements of the output currents, the vector-matrix multiplications for information forwarding and error backpropagation can be done in one step [3, 4]."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "The weight updates are performed in the memristive array after a single batch of training samples is processed [19–21]."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "By coordinating the applied read voltages and measurements of the output currents, the vector-matrix multiplications for information forwarding and error backpropagation can be done in one step [3, 4]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "Unfortunately, most of the recent works focus on the demonstration of the neural network acceleration for inference on edge applications which only consists of the information forwarding process [5–12]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Read-write-verify The accuracy of conductance tuning of memristive devices could be greatly improved if the read-write-verify method is employed, which suppresses the non-linear weight update and write variation effects [16, 17, 56]."
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _background_: "Read noise and conductance drift in long term could also degrade the accuracy of MAC calculation [35, 36]."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _contrasts/critiques_: "Unfortunately, most of the recent works focus on the demonstration of the neural network acceleration for inference on edge applications which only consists of the information forwarding process [5–12]."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _background_: "Ambrogio et al proposed to use memristive devices as the high significant weights and capacitor-based artificial synapses as the low significant weights [58–60]."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _contrasts/critiques_: "The in-situ weight update process was either performed in the offline training scheme [13–15] or performed one by one and coordinated by external closed-loop control circuits [16, 17]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _contrasts/critiques_: "Unfortunately, most of the recent works focus on the demonstration of the neural network acceleration for inference on edge applications which only consists of the information forwarding process [5–12]."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _contrasts/critiques_: "The in-situ weight update process was either performed in the offline training scheme [13–15] or performed one by one and coordinated by external closed-loop control circuits [16, 17]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "For inference-only neuromorphic system, the degradation of the neural network performance due to the inaccuracy of MAC operation can be compensated by hardware-aware training [13]."

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2024_Wang_LearningInMemoryReview_NeuromorphComputEng.pdf](../../10_On_Chip_and_Analog_Training/2024_Wang_LearningInMemoryReview_NeuromorphComputEng.pdf)
- Full text: [../fulltext/2024_Wang_LearningInMemoryReview_NeuromorphComputEng.txt](../fulltext/2024_Wang_LearningInMemoryReview_NeuromorphComputEng.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1088/2634-4386/ad6732
