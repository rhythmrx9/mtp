---
id: W4386293192
key: 2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun
title: "Hardware-aware training for large-scale and diverse deep learning inference workloads using in-memory computing-based accelerators"
short: "HWA Training for Large-scale AIMC"
year: 2023
venue: "NatCommun"
venue_full: "Nature Communications 14, 5282 (2023)"
authors: "Malte J. Rasch, Charles Mackin, Manuel Le Gallo, An Chen, Andrea Fasoli, Frédéric Odermatt, Ning Li, S. R. Nandakumar, Pritish Narayanan, Hsinyu Tsai, Geoffrey W. Burr, Abu Sebastian et al."
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM", "ReRAM"]
models: ["CNN", "ResNet", "LSTM/RNN", "Transformer", "BERT", "Speech"]
lm_models: ["BERT-base (GLUE, 8 tasks)", "ALBERT-base (GLUE, 8 tasks)", "LSTM PTB language model (13.3M mapped params)", "RNN-T (SWB300)"]
param_scale: "12M-108M (BERT-base 108M, ALBERT-base 12M)"
slm: true
evidence: algorithm+simulation
topics: ["hardware-aware-training", "noise-injection", "analog-mvm", "conductance-drift", "adc-dac", "language-models", "stuck-at-faults", "simulator"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 29
cites_in_collection: 22
citations_overall: 176
priority_score: 14.0
doi: "https://doi.org/10.1038/s41467-023-40770-4"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.pdf"
fulltext: "../fulltext/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.txt"
---

# HWA Training for Large-scale AIMC

**Hardware-aware training for large-scale and diverse deep learning inference workloads using in-memory computing-based accelerators** — Nature Communications 14, 5282 (2023) (2023)

## TL;DR
Defines a standard PCM-calibrated AIMC crossbar model (fixed I/O/weight ranges, 8-bit DAC/ADC, per-column digital scales, programming noise, drift, read/output noise, IR-drop) and a hardware-aware retraining recipe that brings 11 DNNs (CNNs, LSTMs, BERT/ALBERT, RNN-T) to >97% normalized accuracy at 1 h, with 5 of 11 iso-accurate (>99%).

## Summary
Naive mapping of FP32-trained DNNs onto analog in-memory computing (AIMC) loses much accuracy because of non-deterministic, nonlinear nonidealities, and earlier noise-aware training studies covered only one or two networks and a subset of nonidealities. The authors define a standardized AIMC MVM model (Eqs. 1-2): digital input scale alpha, DAC quantization to a fixed range, noisy PCM weights (programming error, drift, read noise) with fixed conductance range, dynamically approximated IR-drop, additive output (system) noise, fixed-range ADC (8-bit default) and per-column digital scale gamma_i and bias beta_i. Weights are mapped to a differential conductance pair on 512x512 tiles; alpha, gamma and beta are learned during HWA training and then frozen. Models are first trained in FP32 and then retrained with noise injection by SGD (once, with no chip-specific failure maps), then programmed multiple times in simulation (AIHWKit) and evaluated at 1 s, 1 h, 1 day and 1 year of drift. 11 benchmarks (0.3M-108M params; ResNet-32 to WideResNet-50, DenseNet-121, BERT/ALBERT on GLUE, LSTM-PTB, Speech-SWB300, RNN-T) are used. HWA training raises normalized accuracy at 1 h above 97% for all models and to iso-accuracy for 5 of 11 (incl. BERT-base and all LSTM workloads); a per-nonideality sensitivity study shows input/output noise (ADC/DAC resolution, additive output noise, ADC nonlinearity) matters more than weight noise, with CNNs most sensitive and RNNs least.

## Language models evaluated
- Models: BERT-base (GLUE, 8 tasks), ALBERT-base (GLUE, 8 tasks), LSTM PTB language model (13.3M mapped params), RNN-T (SWB300)
- Scale: 12M-108M (BERT-base 108M, ALBERT-base 12M)

## Contributions
- Standardized, open-source (AIHWKit) PCM-calibrated AIMC crossbar model including range limits, ADC/DAC, output noise, IR-drop and trainable digital scales
- HWA training recipe with learned input/output scales and noise injection, evaluated across 11 large DNNs of three topology families
- Sensitivity/tolerance analysis (Figs. 4-5) ranking nonidealities and DNN topologies by robustness
- Weight-distribution compactness (kurtosis) analysis explaining why column-wise scaling and HWA training reduce MVM error
- Layer-wise analysis showing that exempting 2-11% of parameters from PCM noise gives iso-accuracy for several ImageNet CNNs

## Key claims (stable IDs)
- **2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun#C1** — HWA training lifts all 11 benchmark DNNs to >97% normalized accuracy at 1 h after programming, and 5 of 11 to >99% (iso-accuracy) — _support:_ A*1h 97.2-100.3% (Table 3); direct mapping mostly 66.8-99.4% (Table 2) — _loc:_ Table 2, Table 3
- **2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun#C2** — Noise at inputs/outputs (ADC/DAC resolution, additive output noise, ADC nonlinearity) hurts accuracy more than weight-related noise at equal MVM error — _support:_ Fig. 4B at eps_M=20%; CNNs most sensitive, LSTM-PTB least — _loc:_ Fig. 4, Fig. 5
- **2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun#C3** — RNNs (LSTM) and transformers (BERT) are the most robust families; DAC precision can drop from 8 to 6 bits without retraining — _support:_ LSTM-PTB tolerates 3.3x PCM noise; ResNet-18 only 1.2x — _loc:_ Fig. 5B
- **2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun#C4** — HWA training yields more compact conductance distributions (lower kurtosis), which lowers MVM error — _support:_ MVM error decreases with higher beta / lower kurtosis — _loc:_ Fig. 6
- **2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun#C5** — Standard AIMC model MVM error (~15%) is roughly equivalent to 4-bit fixed-point quantization — _support:_ eps_M ~15% ~ 4 bit — _loc:_ Fig. 3D

## Results
- Direct mapping of FP32 weights: e.g. ResNet-50 ImageNet error 23.87% -> 36.51% at 1 h; BERT-base MRPC 14.60% -> 22.87%; ALBERT MRPC 15.08% -> 32.0% (Table 2)
- After HWA training: BERT-base GLUE8 error 17.47% (FP32) vs 17.55% at 1 h (A*1h 99.8%), ALBERT 19.46% vs 20.45% (97.8%) (Table 3)
- LSTM-PTB 72.90 vs 73.00 perplexity at 1 h (99.6%); RNN-T 11.80 vs 12.36% WER (99.3-99.4%)
- ImageNet CNNs after HWA: ResNet-50 24.83% vs 23.87% FP32; WideResNet-50 23.76% vs 21.53% (A*1h 97.2%)
- Exempting only 6.4%, 2% and 11.3% of parameters (most sensitive layers) from PCM noise gives iso-accuracy for ResNet-18, ResNet-50, DenseNet-121 (Fig. 7); WideResNet-50 needs lower system noise too
- Stuck-at-zero tolerance of 0.42% (least robust model) up to 3-4% for some RNNs; as little as 0.05% of devices stuck at random/g_max hurts large CNNs

## Key numbers
- array_size: 512x512 tiles
- accuracy: A*1h 97.2-100.3% for 11 DNNs; 5/11 iso-accurate (>99%)
- bits_weight: analog (differential PCM pair)
- bits_adc: 8b ADC/DAC default

## Datasets / benchmarks
CIFAR-10, CIFAR-100, ImageNet, GLUE (8 tasks, MRPC), Penn Treebank, Switchboard 300h

## Limitations
- Simulation only; iso-accuracy for large models is not verified on hardware (authors state this)
- Noise sources assumed Gaussian and calibrated mainly to PCM; other devices only discussed in supplementary notes (ReRAM)
- Static/systematic crossbar effects deliberately ignored (assumed handled by read-write-verify)
- One device pair per weight assumed; no redundancy or chip-in-the-loop compensation
- IR-drop uses a fast input-dependent approximation with ~3x safety margin
- Transformer sensitivity analysis uses only the MRPC GLUE task; BERT/ALBERT only (no decoder LLMs)

## Remarks
This is the reference HWA-training and AIMC-evaluation baseline from IBM; its crossbar model is the one shipped in AIHWKit and reused by later analog-LM studies. Evidence is simulation, but noise models are calibrated on PCM hardware and corroborated by the authors' chip work (HERMES). For language models its main message is that encoder transformers (BERT) reach iso-accuracy with HWA training while ALBERT (weight sharing) is harder, and that ADC/output noise rather than weight noise dominates, which foreshadows the sensitivity of LLMs to quantization/additive noise reported later (e.g., NORA). Models of 100M scale are the upper limit examined, so conclusions for billion-parameter SLMs are extrapolation.

## Use in the original review
- F14 (Medium confidence): The field's framing of its own open problem has shifted: since floating-point-level inference accuracy has been demonstrated via hardware-aware training, the question is no longer whether analog can match digital accuracy but what device specifications are required at what fabrication cost — motivating systematic methodologies for mapping the multidimensional device-specification space, with PCM as the representative platform.
- R3 (Refuted 0–3): “Direct mapping of FP-trained DNN weights onto realistic PCM crossbars causes accuracy losses of roughly 1.3% to 23.9% across 11 benchmark networks.”
- R4 (Refuted 1–2): “Hardware-aware training makes analog-deployable not just small CNNs but large-scale, diverse architectures including BERT, RoBERTa, ALBERT, RNN/LSTM and CNN families.”

## Cites (in collection, 22)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _motivation_: "Emerging memory devices such as PCM exhibit imperfect yield, and some fraction of the devices in a given crossbar array will simply not switch properly30,75."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _motivation_: "Although some promising, small-sized DNN prototype demonstrations exist43–49, it remains unclear how robust the AIMC deployment of realistically sized AI workloads will be."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _background_: "This enables approximate MVM computation directly in-memory, by applying activation vectors (as voltages or pulse durations) to the crossbar array, and then reading out analog physical quantities (instantaneous current or accumulated charge)16–18."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _baseline/comparison_: "Some aspects of our AIMC crossbar model have been investigated individually in earlier studies, such as the effect of ADC/DAC quantization, IR-drop, and general read noise55–57, as well as data-dependent long-term noise38."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _extends/builds-on_: "Our main contribution is to combine the long-term data-calibrated noise models of ref. 38 with a more realistic MVM-to-MVM noise model (e.g., quantization, system noise, and IR-drop), and to also include input, weight, and output range restrictions."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019) — _uses-method-or-tool_: "We mainly investigate the situation where all weight-related parameters have been carefully calibrated to existing PCM hardware31, however, the model can be adapted to other memory technologies as well (see Supplementary Notes B.2)."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _contrasts/critiques_: "Some prior works propose using on-chip or chip-in-the-loop training methods38,43,49,55,61, which can greatly increase the attainable accuracy by addressing the specific fabrication variations found on that particular chip."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _baseline/comparison_: "Some aspects of our AIMC crossbar model have been investigated individually in earlier studies, such as the effect of ADC/DAC quantization, IR-drop, and general read noise55–57, as well as data-dependent long-term noise38."
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _uses-method-or-tool_: "For evaluation times teval long after NVM programming, the conductance drift Eq. (8) can be compensated in the digital domain without any expensive re-programming36,73."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _contrasts/critiques_: "We chose to intentionally ignore static crossbar effects that would change the conductance value systematically55,60, since read–write-verify conductance programming can readily adapt to such effects."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "Functions for our standard evaluation process are provided in an open-source IBM Analog Hardware Acceleration Toolkit (AIHWKit)50, enabling future studies on noise robustness for AIMC to build seamlessly upon our work."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _contrasts/critiques_: "However, our analysis only assumes one pair of conductances per weight —since many existing AIMC designs provide multiple pairs of PCM devices per weight44,47, such additional redundancy can potentially counteract such stringent device yield requirements."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _baseline/comparison_: "A few previous studies have attempted to improve the robustness of DNNs to nonidealities by noise-aware training, where multiplicative or additive Gaussian noise38,41 is added to weights or activations during training."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _extends/builds-on_: "That said, our HWA training approach could readily be combined with more sophisticated online compensation methods, with on-chip or chip-in-the-loop training, or with more than one device pair used per weight, including optimization of how weights are assigned across these conductances62."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _motivation_: "Although some promising, small-sized DNN prototype demonstrations exist43–49, it remains unclear how robust the AIMC deployment of realistically sized AI workloads will be."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _background_: "In terms of AIMC workload execution latency and system mapping51, CNNs are already less well-suited for resistive crossbar arrays due to the uneven temporal reuse between layers and spatial underutilization of the large analog tiles by the small kernel matrices (see Table 1), although some optimization and mapping tricks52 are available."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _data/numbers_: "For instance in a recent study54, a ResNet9 CNN was trained with a similar general HWA training approach yielding vastly improved AIMC accuracy in hardware."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _uses-method-or-tool_: "Note that such ADC conversion using a scale and bias per column is already available in prototypes44 but has not previously been incorporated into studies on HWA training."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _baseline/comparison_: "Some aspects of our AIMC crossbar model have been investigated individually in earlier studies, such as the effect of ADC/DAC quantization, IR-drop, and general read noise55–57, as well as data-dependent long-term noise38."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "To help make this even more straightforward, our standard AIMC crossbar model has now been incorporated into our open-source AIHWKIT50,58, which is based on the popular ML framework PyTorch59, and allows for automatic evaluation of any DNN on AIMC."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020)

## Cited by (in collection, 29)
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _contrasts/critiques_: "This shows that resistive non-idealities, although can disrupt a DNN’s performance on crossbars, can be totally mitigated with the help of BN fine-tuning, without the need for parasitic noise-aware re-training of weights as proposed in [16, 19, 20]."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _uses-method-or-tool_: "The AIHWKit is an open-source Python toolkit for exploring and using the capabilities of in-memory computing devices in the context of artificial intelligence and has been used for HWA training of standard DNNs with hardware-calibrated device noise and drift models [22]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "Depending on the hardware customization it can also hold an affine transform (digital output scales and biases, global or column-wise), which is known to greatly improve the mapping of weights to conductances, and is needed for converting ADC-tics to meaningful quantities for the subsequent layers of the DNN (see also22 )."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "To avoid this loss of accuracy, hardware-aware training methods, in which device non-idealities are incorporated during training have been proposed in the literature."
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _motivation_: "While some Hardware-Aware (HWA) training techniques, such as Quantization-Aware Training (QAT), are widely adopted [15], due to the proliferation of reduced precision digital accelerators and deterministic execution flows, others require instance specific information [16]."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "For inference-only neuromorphic system, the degradation of the neural network performance due to the inaccuracy of MAC operation can be compensated by hardware-aware training [13]."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _background_: "These nonidealities primarily arise from the NVM devices (such as stochastic read and write noise), resulting in inaccurate MVMs in the crossbars and thereby, reduced inference accuracy for AI workloads [11], [13], [15]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _contrasts/critiques_: "For instance, it has recently been shown in simulation that with realistic MVM assumptions many large-scale DNNs can be deployed without significant accuracy drop on AIMC inference hardware when retrained properly32."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _motivation_: "Extensive research has shown that device variations and ADC quantization contribute significantly towards accuracy degradation and cannot be easily mitigated [28], [39]."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _background_: "However, Hardware-Aware (HWA) training, where the DNN is made robust via the injection of weight noise during the training process, has been found to recover much of the accuracy loss11,12."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _extends/builds-on_: "Prior studies on hardware-aware training consider a diverse set of non-idealities such as quantization noise, weight drifting, programming noise, IR drop, device non-linearity, and additive noise [11], [28]."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _uses-method-or-tool_: "To study networks well beyond the scale of current hardware implementations, the AIHWKit [23] and AIHWKitLightning [24] were developed to model AIMC for DNNs and enable hardware-aware (HWA) training [25]."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _background_: "although the effect of these on accuracy can be mitigated using different techniques (such as hardware-aware (HWA) training31, post-placement calibration methods and chip-in-the-loop retraining; Box 1), AIMC tiles remain unsuitable for particularly sensitive operations."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _motivation_: "However, the limited write endurance and high programming energy make them poorly suited for on-chip training, necessitating off-chip training and pre-programming for specific tasks11."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _motivation_: "In fact, previous work has shown that ALBERT is significantly more challenging for analog AI hardware than BERT-base model31 that implements unique weight-matrices for each of the 12 layers."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Hardware-aware training or fine-tuning of DNNs, which encapsulates some of these effects in the forward pass, can be used to make models resilient to deterministic (for example, IR drop) or random (for example, read noise) sources of noise and help preserve model accuracy21,57,58."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _contrasts/critiques_: "conventional AHWA training methodologies typically optimize performance for only one task at a time12."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _data/numbers_: "Furthermore, the sensitivity to specific non-idealities, such as the programming error, IR drop and ADC quantization error, can differ by orders of magnitude depending on the specific neural network task77."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _data/numbers_: "HWA training can greatly enhance the robustness of a variety of deep neural networks (DNNs) including recurrent neural networks (RNNs), and transformers (Table 2) as well as convolutional neural networks (CNNs) (not shown here, see Ref [18, 21])."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _data/numbers_: "In contrast, using HWA training techniques to perform the fine-tuning for each GLUE classification-task can provide fully software-equivalent accuracy on BERT-base, at least until the accumulated effects of one year of PCM conductance-drift after programming [32]."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _data/numbers_: "This is in agreement with prior work [30]."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _extends/builds-on_: "However, in contrast to many reduced-precision training papers that assume that the quantization ranges can be dynamically recomputed per-token [43, 44], AIMC typically uses static ranges [37, 45]."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _extends/builds-on_: "Our study starts with training three representative DNNs-ResNet [28] (a CNN-based architecture), LSTM [29] (an RNN-based architecture), and BERT [30] (a transformer-based architecture)-to iso-accuracy through noise injection and related techniques as described in Ref. [12]."
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.pdf](../../07_Hardware_Aware_Training_and_Robustness/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.pdf)
- Full text: [../fulltext/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.txt](../fulltext/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-023-40770-4
