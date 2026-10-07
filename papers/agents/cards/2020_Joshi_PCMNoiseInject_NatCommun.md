---
id: W2948661249
key: 2020_Joshi_PCMNoiseInject_NatCommun
title: "Accurate deep neural network inference using computational phase-change memory"
short: "Joshi PCM Inference"
year: 2020
venue: "NatCommun"
venue_full: "Nature Communications"
authors: "Vinay Joshi, Manuel Le Gallo, Simon Haefeli, Irem Boybat, S. R. Nandakumar, Christophe Piveteau, Martino Dazzi, Bipin Rajendran, Abu Sebastian, Evangelos Eleftheriou"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["PCM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["hardware-aware-training", "noise-injection", "conductance-drift", "read-write-noise", "calibration-compensation", "write-verify-programming", "weight-mapping", "adc-dac"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 47
cites_in_collection: 9
citations_overall: 472
priority_score: 9.9
doi: "https://doi.org/10.1038/s41467-020-16108-9"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2020_Joshi_PCMNoiseInject_NatCommun.pdf"
fulltext: "../fulltext/2020_Joshi_PCMNoiseInject_NatCommun.txt"
---

# Joshi PCM Inference

**Accurate deep neural network inference using computational phase-change memory** — Nature Communications (2020)

## TL;DR
Gaussian weight-noise-injection training plus a batch-norm statistics recalibration (AdaBS) gives ResNet-32 93.75% CIFAR-10 accuracy with all 361,722 weights programmed on real PCM (>=93.5% over one day) and 71.6% ImageNet top-1 (ResNet-34, PCM model).

## Summary
The work trains ResNet CNNs once in software so they tolerate PCM write/read noise and drift without chip-specific retraining. Weights are mapped to differential pairs of PCM devices (G = G+ - G-, scaled by layer maximum weight to Gmax = 25 uS); conv filters are flattened into columns, and batch norm, ReLU and softmax run digitally. Training adds Gaussian noise to the weights in the forward pass only, with relative magnitude eta_tr set from a one-time hardware characterization (sigma 0.94 uS median, eta_tr = 3.8%), plus pretrained initialization, weight clipping at alpha*sigma_W (alpha 2.0-2.5) and a tuned learning-rate schedule. A prototype 1-million-device PCM chip (90nm CMOS) is programmed with iterative programming (converging on 99.1% of nonzero devices); conductances are read over one day and inference is run in software, with a behavioral model (drift exponent ~0.06, 1/f^1.21 noise) to extrapolate to one year. Global drift compensation (GDC) rescales layer outputs; AdaBS updates BN running mean/variance using few calibration images (2,600 for CIFAR-10, 1,300 for ImageNet). ADC/DAC quantization is analyzed separately (8-bit adequate).

## Contributions
- Weight-noise-injection training calibrated by one-time hardware characterization, giving near-FP32 accuracy on PCM for ResNets
- Experimental validation: all 361,722 ResNet-32 weights on PCM devices of a 1M-device chip
- AdaBS: periodic batch-norm statistics recalibration improving accuracy retention beyond global drift compensation
- Comparison to ternary/4-bit training and other noise-injection variants (inputs, pre-activations, multiplicative)

## Key claims (stable IDs)
- **2020_Joshi_PCMNoiseInject_NatCommun#C1** — Noise-injection training reaches 93.7% CIFAR-10 on PCM, less than 0.2% below the FP32 baseline (93.87%). — _support:_ eta_tr = 3.8%; FP32/4-bit/ternary training perform worse after transfer (4-bit loses >1%, ternary <0.5% drop but lower base) — _loc:_ Sec. II C, Fig. 3c
- **2020_Joshi_PCMNoiseInject_NatCommun#C2** — Hardware ResNet-32 retains >92.6% for one day with GDC and >93.5% with AdaBS (+0.9% over GDC, +1.8% extrapolated to one year). — _support:_ 93.75% at 25 s; without compensation accuracy falls to 10% within ~1000 s — _loc:_ Sec. II D-E, Fig. 4d, 5b
- **2020_Joshi_PCMNoiseInject_NatCommun#C3** — ResNet-34 reaches 71.6% top-1 ImageNet on PCM (about 6% over FP32/4-bit training); with first/last layers digital, 71.9% and >71% over one year. — _support:_ AdaBS improves 1-year accuracy by 7% over GDC (1300 calibration images) — _loc:_ Fig. 3d, Fig. 5c
- **2020_Joshi_PCMNoiseInject_NatCommun#C4** — Precise noise modelling in training is not essential: input-noise augmentation also yields resilience. — _support:_ Supplementary Note 4 — _loc:_ Discussion

## Results
- CIFAR-10 ResNet-32: 93.75% after programming (hardware), baseline 93.87%; weights per device: 2 PCM in differential configuration
- PCM programming sigma <1.2 uS for all 11 levels, >2x lower than prior PCM arrays
- ImageNet ResNet-34 (PCM model): 71.6%; more than 0.5% drop at ~1.2% relative noise on all layers, so first/last layers kept noiseless
- Training converges within ~8 epochs on ImageNet; accuracy within 0.5% of baseline for eta up to 5% on CIFAR-10

## Key numbers
- tech_node: 90nm CMOS (PCM chip)
- array_size: 1M PCM devices on chip
- accuracy: 93.75% CIFAR-10 (ResNet-32, hardware); 71.6% ImageNet top-1 (ResNet-34, PCM model)
- bits_weight: 2 PCM devices per weight (differential); ~4-bit effective
- bits_adc: 8b adequate

## Datasets / benchmarks
CIFAR-10, ImageNet, ResNet-32, ResNet-34

## Limitations
- Only the CIFAR-10 network was physically programmed; ImageNet results use a fitted PCM model
- Inference executed in software after reading hardware conductances, not on a fully integrated chip (IR drop, circuit offsets not captured)
- AdaBS needs periodic calibration with data and extra digital compute (~52% of BN cost on the CIFAR-10 test set)
- CNNs only; no transformers or language models
- Relies on one-time noise characterization of one chip family

## Remarks
One of the more rigorous experimental demonstrations that software noise-injection training, calibrated from real device statistics, makes PCM inference competitive with digital baselines at non-trivial scale. Batch-norm-based drift compensation and global drift compensation became recurring techniques. For LM mapping, the lesson that retraining mainly adapts normalization statistics hints at why LayerNorm-containing transformers need different recipes, but this paper shows no transformer results.

## Cites (in collection, 9)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Off-line variation-aware training schemes have also been proposed, where hardware non-idealities such as device-to-device variations13,14, defective devices14, or IR drop13 are first characterized and then fed into the training algorithm running in software."
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "Both charge-based storage devices, such as Flash memory4, and resistance-based (memristive) storage devices, such as metal-oxide resistive random-access memory (ReRAM)5,6 and phase-change memory (PCM)7-9 are being investigated for this."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "Both charge-based storage devices, such as Flash memory4, and resistance-based (memristive) storage devices, such as metal-oxide resistive random-access memory (ReRAM)5,6 and phase-change memory (PCM)7-9 are being investigated for this."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _contrasts/critiques_: "One potential solution to this problem is to train the network fully on hardware9,10, such that all hardware non-idealities would be de facto included as constraints during training."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "In order to reduce the data transfers to a minimum in inference accelerators, a promising avenue is to employ in-memory computing using non-volatile memory devices3."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)

## Cited by (in collection, 47)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "Finally, we also provide a specific inference “tile” setting, which supports adding carefully calibrated, conductance-dependent programming noise, weight read noise and conductance drift onto a trained networks’ analog weights during inference time and provides automatic global drift compensation (see eg. [10])."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _background_: "Memristor crossbars, in particular, have attracted significant interest due to their ability to efficiently perform matrix-matrix and matrix-vector multiplications-the dominant computational kernels in deep neural networks [6]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "Drift mitigation will need a multi-pronged approach across device engineering [22], programming procedure, circuit slope correction [23] as well as algorithms, including drift-aware training approaches- [17], [24], [25]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "To avoid the energy and area overheads of reading, digitizing and aggregating multiple bit-sliced arrays, the magnitude of a weight can also be fully encoded in one device [30, 34]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _contrasts/critiques_: "Long et al. [25] injected Gaussian noise during training to mimic programming noise, and Joshi et al. [26] incorporated device programming variation extracted from experiments during training."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _uses-method-or-tool_: "Prior to mapping the networks onto analog IMC cores, it is essential to perform a hardware-aware custom training in software as described in [30]."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _background_: "In previous studies, several CIM devices with a crossbar structure have been demonstrated using two-terminal devices, such as phase-change and resistive-switching memories, as synaptic devices (13–18)."
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _background_: "Alternatively, modifying ex-situ training has been proposed: altering the cost function [30] or injecting noise into the synaptic weights [31] can make MNNs more robust to the effects of nonidealities."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "It has been shown that hardware-aware training in software is crucial for improving accuracy for analogue inference19,24,25,39."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _background_: "Note that typically 2 PCM devices are used to denote a signed weight [32]."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _motivation_: "However, RRAM device suffers from several non-idealities such as limited resistance levels, device-to-device write variations, stuck-at-faults, and limited Roff /Ron ratio, posing a signiﬁcant challenge to designing reliable RRAM-based IMC architectures [5–12]."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "PCM-based implementations hence offer high performance densities (TOp/s/mm2 ), where a pair of PCM devices can represent signed multi-bit weights [16]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "the most competitive candidates at present among emerging memories are resistive random-access memory (RRAM) ... phase-change memory (PCM) [85] [34] [86]..."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _extends/builds-on_: "Drift noiseaware BN adaptation can maintain the accuracy of crossbar-mapped DNNs till a retention time T beyond which the accuracy dramatically decreases [12]."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _contrasts/critiques_: "Alternatively, noise estimated from a non-extensive chip characterization can be injected in off-chip training [19]-[24] to enhance the network's tolerance towards errors due to conductance variation. However, this approach fails to address the issue of reducing such errors, as memristors can still get mapped to high variation conductance states, rendering it ineffective."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _uses-method-or-tool_: "Prior to being deployed on the chip, the networks are trained in a hardware-aware manner by injecting noise on the synaptic weights to improve their resilience to hardware nonidealities (ref 12), using the publicly available IBM Analog Hardware Acceleration Kit (ref 38)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _uses-method-or-tool_: "To make the network more resilient to analog noise23–26, we retrained it while including weight and"
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _extends/builds-on_: "Our main contribution is to combine the long-term data-calibrated noise models of ref. 38 with a more realistic MVM-to-MVM noise model (e.g., quantization, system noise, and IR-drop), and to also include input, weight, and output range restrictions."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _background_: "Many types of memory devices, including Flash memory, PCM, and Resistive Random Access Memory (RRAM), can be used for IMC [2]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "The first IMC chip that we will expose is the Fusion PCM chip21 ."
- [2023_Jang_VECOM_ICCAD](2023_Jang_VECOM_ICCAD.md) VECOM (2023) — _background_: "Processing-In Memory (PIM) architecture, utilizing Resistive Random Access Memory (ReRAM), offers a promising solution to address the limitations of conventional von Neumann architecture [1-3]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "To avoid this loss of accuracy, hardware-aware training methods, in which device non-idealities are incorporated during training have been proposed in the literature."
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _uses-method-or-tool_: "To perform realistic hardware simulations, we used an experimentally verified model, calibrated based on extensive measurements performed on an array containing 1 million Phase-Change Memory (PCM) devices [24]."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _contrasts/critiques_: "Unfortunately, most of the recent works focus on the demonstration of the neural network acceleration for inference on edge applications which only consists of the information forwarding process [5–12]."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _uses-method-or-tool_: "To make the models robust to noise, we follow the standard procedure51 of first training the FP-32 base model, followed by hardware-aware finetuning on the same dataset."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _background_: "However, Hardware-Aware (HWA) training, where the DNN is made robust via the injection of weight noise during the training process, has been found to recover much of the accuracy loss11,12."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _contrasts/critiques_: "However, most previous works [11]–[13], [28] require hardware-aware training, which is non-trivial, if not prohibitive for LLMs with large number of parameters."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _motivation_: "We assume that such errors can be reduced during transformer inference using hardware-aware training [60]."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Hardware-aware training or fine-tuning of DNNs, which encapsulates some of these effects in the forward pass, can be used to make models resilient to deterministic (for example, IR drop) or random (for example, read noise) sources of noise and help preserve model accuracy21,57,58."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _uses-method-or-tool_: "We used global drift compensation22 to mitigate temporal variations."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _contrasts/critiques_: "Previous works that study HWA training for AIMC-based hardware are limited to CNNs [35, 48, 49], RNNs [37], LSTMs [37, 49, 50], GANs [51] and small encoder-only transformers [37, 52]."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _contrasts/critiques_: "Prior studies on the impact of memory characteristics on AI tasks mostly focus on individual non-ideality [6, 10, 13], such as the effect of memory window or conductance drift on the inference accuracy."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_GarciaRedondo_SACA_DCIS](2022_GarciaRedondo_SACA_DCIS.md) SACA (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022)
- [2026_Sharma_HatFi_VTS](2026_Sharma_HatFi_VTS.md) HATFI (2026)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2020_Joshi_PCMNoiseInject_NatCommun.pdf](../../07_Hardware_Aware_Training_and_Robustness/2020_Joshi_PCMNoiseInject_NatCommun.pdf)
- Full text: [../fulltext/2020_Joshi_PCMNoiseInject_NatCommun.txt](../fulltext/2020_Joshi_PCMNoiseInject_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-020-16108-9
