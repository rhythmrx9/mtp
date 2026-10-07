---
id: W4389082012
key: 2023_LeGallo_AIHWKit_APLMachLearn
title: "Using the IBM analog in-memory hardware acceleration kit for neural network training and inference"
short: "AIHWKit"
year: 2023
venue: "APLMachLearn"
venue_full: "APL Machine Learning"
authors: "Manuel Le Gallo, Corey Lammie, Julian Büchel, Fabio Carta, Omobayode I. Fagbohungbe, Charles Mackin, Hsinyu Tsai, Vijay Narayanan, Abu Sebastian, Kaoutar El Maghraoui, Malte J. Rasch"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["PCM", "ReRAM", "Generic-NVM"]
models: ["MLP", "CNN", "ResNet", "LSTM/RNN", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["simulator", "analog-mvm", "hardware-aware-training", "noise-injection", "conductance-drift", "on-chip-training", "adc-dac", "read-write-noise"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 23
citations_overall: 69
priority_score: 7.72
doi: "https://doi.org/10.1063/5.0168089"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2023_LeGallo_AIHWKit_APLMachLearn.pdf"
fulltext: "../fulltext/2023_LeGallo_AIHWKit_APLMachLearn.txt"
---

# AIHWKit

**Using the IBM analog in-memory hardware acceleration kit for neural network training and inference** — APL Machine Learning (2023)

## TL;DR
Tutorial on the open-source IBM Analog Hardware Acceleration Kit (AIHWKit), a PyTorch-based functional simulator of analog in-memory training and inference with hardware-calibrated PCM/ReRAM models, plus the cloud-hosted Analog AI Cloud Composer that also exposes a physical PCM chip.

## Summary
AIMC inference/training accuracy is limited by noisy, non-linear devices and non-ideal peripherals, so DNNs must be adapted, and a standard simulator is needed instead of fragmented, mostly closed-source tools. AIHWKit wraps PyTorch Linear/Conv layers into analog tile modules (convert_to_analog) whose physical behaviour is configured through an RPUConfig: DAC/ADC resolution and range clipping, additive/output noise, S-shaped output non-linearity, IR-drop, per-column digital output scales/bias, and a mapping of logical weight matrices onto physical tile sizes (Sec. III, Fig. 3, Tab. V, Fig. 4). Non-MVM layers (activations, batch norm, softmax) are assumed digital floating point. For inference it provides hardware-calibrated PCM programming noise, read noise and drift models (PCMLikeNoiseModel, Fig. 5) plus a calibrated ReRAM noise model, drift compensation, and hardware-aware (HWA) training with weight-noise modifiers, drop-connect and clipping (Sec. IV; ResNet-32/CIFAR-10 notebook, ~94% FP baseline). For training it simulates in-memory SGD and compound-device algorithms (Tiki-Taka, TTv2/c-TTv2, mixed-precision, AGAD) with device response curves (constant/linear/soft-bounds, ReRAM fit; Sec. V, Figs. 6-10). Examples (3-FC MNIST) show plain in-memory SGD performs poorly under update asymmetry while TT and MP algorithms are better, and ~70-120% of measured device-to-device variation is tolerable. The paper also describes the Analog AI Cloud Composer (no-code training/inference experiments, access to the PCM 'Fusion' chip) and three customization examples (Sec. VII).

## Contributions
- Comprehensive description of AIHWKit's design: analog tile abstraction, RPUConfig non-ideality parameters, and conversion utilities for PyTorch models (Sec. III).
- Best-practice recipes for AIMC inference evaluation (programming noise, drift, drift compensation) and hardware-aware training (Sec. IV).
- Walk-through of in-memory training algorithms and device response models, with hyperparameter and device-tolerance exploration (Sec. V).
- Overview of the Analog AI Cloud Composer, a managed cloud service with physical AIMC chip access (Sec. VI), and guidance on extending the toolkit (Sec. VII).
- Feature comparison against NeuroSim, CrossSim, MemTorch and XB-SIM (Tab. I) arguing for consolidating on one maintained toolkit.

## Key claims (stable IDs)
- **2023_LeGallo_AIHWKit_APLMachLearn#C1** — AIHWKit is the only actively maintained open-source AIMC toolkit among those compared that supports all listed features (network types, HW-calibrated noise, HWA training, in-memory gradient), though it lacks performance estimation. — _support:_ Tab. I; 'Despite its current lack of support for performance estimation, the AIHWKit is the only actively maintained tool which supports all the features listed' — _loc:_ Sec. I, Tab. I
- **2023_LeGallo_AIHWKit_APLMachLearn#C2** — Standard in-memory SGD trains poorly on asymmetric devices, whereas Tiki-Taka and mixed-precision updates perform clearly better. — _support:_ 3FC MNIST test error after 10 epochs vs algorithm — _loc:_ Sec. V, Fig. 8
- **2023_LeGallo_AIHWKit_APLMachLearn#C3** — Training tolerates about 120% of the measured device-to-device variation without significant accuracy drop; reducing variation below ~70% of baseline gives only small further gains. — _support:_ 99% of no-variation accuracy retained up to ~120% noise factor — _loc:_ Sec. V.D, Fig. 10
- **2023_LeGallo_AIHWKit_APLMachLearn#C4** — PCM statistical noise model reproduces measured conductance evolution; a 512x512 tile MVM at t=1 s has 13% relative L2 error with the example settings. — _support:_ 13% L2 error, 50% sparse inputs, clipped Gaussian weights sigma 0.246 — _loc:_ Sec. III, Figs. 4-5

## Results
- ResNet-32 / CIFAR-10 HWA-training notebook starts from ~94% digital baseline accuracy (Sec. IV.B).
- Non-ideal MVM example (512x512 tile, defaults) gives 13% L2 error at t=1 s after programming (Fig. 5).
- Device-to-device variation tolerance for in-memory training: ~120% of measured noise acceptable; steep degradation above ~70% sensitivity knee (Fig. 10b).
- Tiki-Taka and MP algorithms outperform plain stochastic-pulse SGD on 3-FC MNIST (Fig. 8).

## Key numbers
- array_size: 512x512 tile (example)
- accuracy: ~94% CIFAR-10 FP baseline (ResNet-32)
- bits_adc: out_res 254 steps default (~8b)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Functional (accuracy-only) simulator: no latency, energy or area estimation; digital layers assumed full-precision floating point.
- Tutorial with small illustrative workloads (MNIST 3-FC, CIFAR-10 ResNet-32); no benchmark across architectures or against silicon beyond the cited PCM calibration.
- Native bit-sliced / digital-style weight mapping and low-precision digital-op modelling not supported (Outlook).
- Not yet integrated with HuggingFace/DeepSpeed pipelines, so large language model workflows need extra effort (Outlook).

## Remarks
Reference tutorial for the most widely used open-source AIMC noise-injection simulator; its value is shared infrastructure rather than new results, and the numbers shown are illustrative. For mapping transformers/LMs to PCM or ReRAM crossbars, the RPUConfig abstractions (ADC/DAC, per-column scales, PCM drift and read-noise models, HWA modifiers) are the practical baseline that later LM-on-AIMC evaluations in the collection build on. The Outlook explicitly lists HuggingFace integration as future work, so LM support was not demonstrated here.

## Cites (in collection, 23)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "One approach is to perform a parallel weight update by sending deterministic or stochastic overlapping pulses from the rows and columns simultaneously to implement an approximate outer product and program the devices at the same time (Fig. 2(b))16,17,40 ."
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _baseline/comparison_: "In Tab. I, we compare key features of the AIHWKit to related open-source AIMC simulation toolkits."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "Therefore, many large-scale simulations encompassing device and circuit nonidealities have been performed to quantify their impact on DNN accuracy for training and inference21–28 ."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "The first IMC chip that we will expose is the Fusion PCM chip21 ."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019) — _uses-method-or-tool_: "The low-frequency read noise is typically modelled using a normal distribution centered around zero with a standard deviation of σnG dependent on the time elapsed since programming, i.e., N (0, σnG (t))50 ."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _baseline/comparison_: "The toolkits are compared against five key dimensions: ML library, supported network types, on-chip inference capabilities, on-chip training, and on-chip inference."
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _motivation_: "These inherent characteristics limit their accuracy and reliability to use in practical deep learning workloads18–20 ."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "In addition to traditional digital accelerators, including the Google Tensor Processing Unit, Amazon Inferentia, and IBM Artificial Intelligence Unit1 , accelerators based on Analog In-Memory Computing (AIMC) using Non-Volatile Memory (NVM) are being actively researched2–4 ."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Therefore, many large-scale simulations encompassing device and circuit nonidealities have been performed to quantify their impact on DNN accuracy for training and inference21–28 ."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _baseline/comparison_: "Framework comparison table lists NeuroSim, IBM Analog Hardware Acceleration Kit, CrossSim, XB-SIM, and MemTorch as the actively maintained/compared AIMC simulation toolkits, evaluated on ML library, network types supported (incl. Recurrent/Transformer), accuracy estimation, HW-calibration, and on-chip training/inference support."
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020) — _contrasts/critiques_: "However, the toolkit currently does not natively support a bit-wise ”digital” mapping of weights, where only 1 and 0 states are (approximately) represented by conductances, and multiple devices are used with different significances to approximate a digital MVM19 ."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _extends/builds-on_: "The AIHWKit toolkit itself is referenced to its earlier introductory conference paper describing a flexible and fast PyTorch toolkit for simulating training and inference on analog crossbar arrays."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _background_: "In addition to traditional digital accelerators, including the Google Tensor Processing Unit, Amazon Inferentia, and IBM Artificial Intelligence Unit1 , accelerators based on Analog In-Memory Computing (AIMC) using Non-Volatile Memory (NVM) are being actively researched2–4 ."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "When performing MVMs, the conductance of NVM elements are usually linearly mapped to a range of weight values, and it is assumed that a typical pulse-width modulation of the voltage input5,6 can be approximated by a time average (so that x corresponds to the mean voltage given)."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _background_: "These are added to increase the model robustness 21,22,55–59 , and can be specified using different RPUConfig parameters (as part of the InferenceRPUConfig class), which are discussed in the following subsections."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "AIMC accelerators that are based on resistive memory device technologies such as Phase Change Memory (PCM)5–8 , Resistive Random Access Memory (ReRAM)9–12 , and Magnetic Random Access Memory (MRAM)13 , have shown great promise in accelerating and reducing the power consumption of deep learning systems."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _motivation_: "These inherent characteristics limit their accuracy and reliability to use in practical deep learning workloads18–20 ."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _uses-method-or-tool_: "Some of these models, such as the PCMLikeNoiseModel50 and ReRamWan2022NoiseModel9 are hardware-calibrated."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _data/numbers_: "Such an architecture is projected to provide highly competitive throughput while offering 40x-140x higher energy efficiency than an NVIDIA A100 GPU14 ."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "AIMC accelerators that are based on resistive memory device technologies such as Phase Change Memory (PCM)5–8 , Resistive Random Access Memory (ReRAM)9–12 , and Magnetic Random Access Memory (MRAM)13 , have shown great promise in accelerating and reducing the power consumption of deep learning systems."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "AIMC accelerators that are based on resistive memory device technologies such as Phase Change Memory (PCM)5–8 , Resistive Random Access Memory (ReRAM)9–12 , and Magnetic Random Access Memory (MRAM)13 , have shown great promise in accelerating and reducing the power consumption of deep learning systems."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "Depending on the hardware customization it can also hold an affine transform (digital output scales and biases, global or column-wise), which is known to greatly improve the mapping of weights to conductances, and is needed for converting ADC-tics to meaningful quantities for the subsequent layers of the DNN (see also22 )."
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)

## Cited by (in collection, 13)
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _uses-method-or-tool_: "To perform HWA training, the IBM Analog Hardware Acceleration Kit (AIHWKIT) [19, 20] is used."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _uses-method-or-tool_: "For hardware-aware finetuning, we leveraged AIHWKIT54, an open-source framework used for hardware-aware training of neural networks."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _uses-method-or-tool_: "We refer the reader to Le Gallo et al.54 for a comprehensive tutorial on HWA training using IBM AIHWKIT."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _contrasts/critiques_: "Hence, the noise management and bound management in previous works [7], [14], [28] could become less effective in LLMs due to the input distribution, as shown in Figure 1, and will be further discussed in Section II and Section III."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _uses-method-or-tool_: "To study networks well beyond the scale of current hardware implementations, the AIHWKit [23] and AIHWKitLightning [24] were developed to model AIMC for DNNs and enable hardware-aware (HWA) training [25]."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _uses-method-or-tool_: "The HWA fine-tuning of the ALBERT model was conducted with an internal tool and the same capability is available in the IBM Analog Hardware Acceleration Kit at https://github.com/IBM/aihwkit43,44."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "Analog Hardware-Aware (AHWA) training techniques have been demonstrated to enhance model robustness under these constraints for various NN architectures, effectively mitigating accuracy losses by injecting Gaussian noise during forward-propagation and simulating circuit-non-idealities11–13."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _uses-method-or-tool_: "These FP models are then mapped to conductance values of NVM devices in the AIMC crossbar arrays using the AIHWKIT [32-34] simulation framework."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "To help make this even more straightforward, our standard AIMC crossbar model has now been incorporated into our open-source AIHWKIT50,58, which is based on the popular ML framework PyTorch59, and allows for automatic evaluation of any DNN on AIMC."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _uses-method-or-tool_: "We employ the open-source AIHWKIT toolkit [5] to expose these behaviours using systemlevel explorations in LionHeart, allowing both the realistic characterization of analog non-idealities and analog HWA retraining."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _uses-method-or-tool_: "Finally, to test the robustness to other types of noise, we conducted experiments where we inject read noise and apply conductance drift according to a publicly available noise model based on hardware [73]."
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2023_LeGallo_AIHWKit_APLMachLearn.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2023_LeGallo_AIHWKit_APLMachLearn.pdf)
- Full text: [../fulltext/2023_LeGallo_AIHWKit_APLMachLearn.txt](../fulltext/2023_LeGallo_AIHWKit_APLMachLearn.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1063/5.0168089
