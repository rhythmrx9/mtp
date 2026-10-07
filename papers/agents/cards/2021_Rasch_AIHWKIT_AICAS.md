---
id: W3148526109
key: 2021_Rasch_AIHWKIT_AICAS
title: "A Flexible and Fast PyTorch Toolkit for Simulating Training and Inference on Analog Crossbar Arrays"
short: "AIHWKit"
year: 2021
venue: "AICAS"
venue_full: "2021 IEEE 3rd International Conference on Artificial Intelligence Circuits and Systems (AICAS 2021)"
authors: "Malte J. Rasch, Diego Moreda, Tayfun Gokmen, Manuel Le Gallo, Fabio Carta, Cindy Goldberg, Kaoutar El Maghraoui, Abu Sebastian, Vijay Narayanan"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM", "PCM", "Generic-NVM"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "analog-mvm", "read-write-noise", "conductance-drift", "device-variation", "hardware-aware-training", "on-chip-training", "adc-dac"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 23
cites_in_collection: 5
citations_overall: 145
priority_score: 8.65
doi: "https://doi.org/10.1109/aicas51828.2021.9458494"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2021_Rasch_AIHWKIT_AICAS.pdf"
fulltext: "../fulltext/2021_Rasch_AIHWKIT_AICAS.txt"
---

# AIHWKit

**A Flexible and Fast PyTorch Toolkit for Simulating Training and Inference on Analog Crossbar Arrays** — 2021 IEEE 3rd International Conference on Artificial Intelligence Circuits and Systems (AICAS 2021) (2021)

## TL;DR
IBM Analog Hardware Acceleration Kit (aihwkit) is an open-source PyTorch toolkit with a C++/CUDA analog-tile core that simulates analog crossbar training and inference with configurable non-idealities and PCM-calibrated noise/drift models, with full pulsed analog training costing only 2-5x floating-point training time.

## Summary
The paper introduces aihwkit to give algorithm researchers a PyTorch-native simulator of analog crossbars. The central abstraction is an analog tile holding a 2D weight matrix, whose forward pass follows y_i = f_adc(sum_j (w_ij + sigma_w xi_ij)(f_dac(x_j) + sigma_inp xi_j) + sigma_out xi_i) with Gaussian input/weight/output noise, dynamic input scaling, clipping and linear ADC/DAC quantization; the backward pass can be noisy or ideal. For training chips, stochastic or deterministic pulse trains implement the rank-1 update in analog with device response curves, device-to-device and cycle-to-cycle variation, and ReRAM presets calibrated to measured data; unit cells with multiple devices and Tiki-Taka coupled-tile optimizers are supported. For inference chips, hardware-aware training adds reversible weight noise in forward/backward, and an inference tile adds conductance-dependent programming noise, read noise and drift with global drift compensation, calibrated on a 1M-device PCM array. Digital ops (activations) run in PyTorch FP. Hundreds of auto-tuned CUDA kernel templates give e.g. 60 s/epoch for VGG-8/CIFAR-10 pulsed update vs 15 s FP on a V100.

## Contributions
- Open-source PyTorch/C++/CUDA toolkit with AnalogLinear/AnalogConv layers
- Configurable analog tile model with noise, ADC/DAC, pulsed update and device presets
- PCM-calibrated programming noise, read noise and drift model with drift compensation for inference
- Support for Tiki-Taka and custom unit cells; GPU-accelerated at 2-5x FP training cost

## Key claims (stable IDs)
- **2021_Rasch_AIHWKIT_AICAS#C1** — Full analog-training simulation takes only 2-5x longer than FP training — _support:_ 60 s vs 15 s per epoch, VGG-8/CIFAR-10, V100 — _loc:_ Sec. 3, footnote 3
- **2021_Rasch_AIHWKIT_AICAS#C2** — DNN+NeuroSim underestimates update noise because gradient outer products accumulate in digital — _support:_ qualitative argument — _loc:_ Sec. 3
- **2021_Rasch_AIHWKIT_AICAS#C3** — Inference noise model matches PCM experimental conductance evolution — _support:_ Fig. 3C against 1M PCM array data — _loc:_ Sec. 5, Fig. 3

## Results
- Fig. 3B: simulated ReRAM pulse response vs measured (Gong et al.)
- Fig. 3C: simulated PCM conductance drift vs measured; small mismatch below 1000 s due to simultaneous-programming assumption

## Key numbers
- throughput: 60 s/epoch (VGG-8 pulsed) vs 15 s FP on V100

## Datasets / benchmarks
CIFAR-10

## Limitations
- Functional simulator only: not for latency/power estimation
- Only parallel read-out and linear ADC supported at time of writing
- Normalized-unit abstract model rather than circuit-level
- No end-to-end accuracy benchmark tables in this short paper; transformers/LMs not demonstrated

## Remarks
Foundational tool paper; its noise model and hardware-aware training hooks underpin many later analog-AI and analog-LLM studies. Strength is practicality and speed, weakness is abstraction level and lack of quantitative validation beyond figures.

## Cites (in collection, 5)
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018) — _background_: "One promising future technology is the use of memristive crossbar arrays for accelerating the ubiquitous matrix-vector multiply and rank-update operations in ANNs by employing in-memory computation of matrices stored as analog quantities in tunable resistive elements [1,7,8,13]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _contrasts/critiques_: "RxNN [9] is based on the rather outdated Caffe framework and only caters to analog chips dedicated to inference, lacking more advanced algorithms and pulse update schemes that are needed for training-enabled chip designs."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "Finally, we also provide a specific inference “tile” setting, which supports adding carefully calibrated, conductance-dependent programming noise, weight read noise and conductance drift onto a trained networks’ analog weights during inference time and provides automatic global drift compensation (see eg. [10])."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "One promising future technology is the use of memristive crossbar arrays for accelerating the ubiquitous matrix-vector multiply and rank-update operations in ANNs by employing in-memory computation of matrices stored as analog quantities in tunable resistive elements [1,7,8,13]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _contrasts/critiques_: "A recent PyTorch re-implementation of a subset of the MLP-NeuroSim package using PyTorch, called DNN+NeuroSim [12], is closest to our framework."

## Cited by (in collection, 23)
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "Incorporating hardware non-idealities within DNN training (i.e., 'hardware-aware' algorithmic training) has been shown effective in making analogue memory-based DNNs more resilient to hardware imperfections22-25."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "For works that support on-chip training and inference using realistic IMC crossbar platforms for forward and backward propagation stages, fine-tuning (or re-programming) the weights (or memristive conductances) of a pre-trained DNN on hardware to mitigate accuracy losses due to noise and quantization effects becomes highly compute- & memory-intensive [11, 17, 18]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _uses-method-or-tool_: "Prior to being deployed on the chip, the networks are trained in a hardware-aware manner by injecting noise on the synaptic weights to improve their resilience to hardware nonidealities (ref 12), using the publicly available IBM Analog Hardware Acceleration Kit (ref 38)."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "Functions for our standard evaluation process are provided in an open-source IBM Analog Hardware Acceleration Toolkit (AIHWKit)50, enabling future studies on noise robustness for AIMC to build seamlessly upon our work."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _uses-method-or-tool_: "Each sampled architecture is trained using different levels of weight noise and HWA training hyper-parameters using the AIHWKit [21]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _extends/builds-on_: "The AIHWKit toolkit itself is referenced to its earlier introductory conference paper describing a flexible and fast PyTorch toolkit for simulating training and inference on analog crossbar arrays."
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _uses-method-or-tool_: "To perform HWA training, the IBM Analog Hardware Acceleration Kit (AIHWKIT) [19, 20] is used."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _contrasts/critiques_: "While CiMLoop models area/energy/throughput, IBM AI Hardware Kit [68], CrossSim [69], and MemTorch [70], model DNN accuracy."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "Ambrogio et al proposed to use memristive devices as the high significant weights and capacitor-based artificial synapses as the low significant weights [58–60]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _uses-method-or-tool_: "For simulations, we use the PyTorch-based open source toolkit (AIHWKit)29, where we have implemented the proposed algorithms (see also Supplementary Fig. 4)."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _uses-method-or-tool_: "We use the analog in-memory hardware acceleration kit (AIHWKIT) [27] to evaluate model accuracy on Analog CIM tiles."
- [2025_Zhang_ASiM_TVLSI](2025_Zhang_ASiM_TVLSI.md) ASiM (2025) — _background_: "Fundamental architecture and MAC operation of ACiM. (a) Bit-serial ACiM. (b) Bit-parallel ACiM. inference accuracy [17–20]."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _uses-method-or-tool_: "The HWA fine-tuning of the ALBERT model was conducted with an internal tool and the same capability is available in the IBM Analog Hardware Acceleration Kit at https://github.com/IBM/aihwkit43,44."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _uses-method-or-tool_: "To accurately model the behavior and constraints of AIMC hardware, we used AIHWKIT, an opensource simulator for AIMC devices21."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _uses-method-or-tool_: "These FP models are then mapped to conductance values of NVM devices in the AIMC crossbar arrays using the AIHWKIT [32-34] simulation framework."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _motivation_: "Therefore, it is important to develop simulation tools that can capture these variations for relevant examples [47]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2023_Parvaresh_NlpAimcResilience_NANOARCH](2023_Parvaresh_NlpAimcResilience_NANOARCH.md) NLP-AIMC (2023)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2021_Rasch_AIHWKIT_AICAS.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2021_Rasch_AIHWKIT_AICAS.pdf)
- Full text: [../fulltext/2021_Rasch_AIHWKIT_AICAS.txt](../fulltext/2021_Rasch_AIHWKIT_AICAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/aicas51828.2021.9458494
