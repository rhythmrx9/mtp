---
id: W2909715355
key: 2020_Jain_RxNN_TCAD
title: "RxNN: A Framework for Evaluating Deep Neural Networks on Resistive Crossbars"
short: "RxNN"
year: 2020
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2020)"
authors: "Shubham Jain, Abhronil Sengupta, Kaushik Roy, Anand Raghunathan"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Generic-NVM"]
models: ["CNN", "ResNet", "VGG", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["simulator", "ir-drop-parasitics", "device-variation", "adc-dac", "analog-mvm", "hardware-aware-training", "weight-mapping", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 18
cites_in_collection: 7
citations_overall: 136
priority_score: 7.82
doi: "https://doi.org/10.1109/tcad.2020.3000185"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2020_Jain_RxNN_TCAD.pdf"
fulltext: "../fulltext/2020_Jain_RxNN_TCAD.txt"
---

# RxNN

**RxNN: A Framework for Evaluating Deep Neural Networks on Resistive Crossbars** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2020) (2020)

## TL;DR
RxNN is a Caffe-based functional simulator built on a Fast Crossbar Model (FCM) that is 4-5 orders of magnitude faster than HSPICE and shows 9.6%-32% ImageNet accuracy loss for large CNNs on non-ideal 64x64 resistive crossbars.

## Summary
Circuit-level crossbar simulation is far too slow for ImageNet-scale DNNs, while architectural models use oversimplified error models that ignore dependence on inputs, programmed conductances and column position. FCM decomposes a crossbar VMM into three stages: a non-linear DAC model on inputs, an equivalent non-ideal conductance matrix G_non-ideal for the array obtained by pre-solving the Kirchhoff/Ohm equations (including driver, sensing, wire parasitics, device nonlinearity and variation) so that evaluation is a single matrix multiply, and a non-linear ADC model on outputs. RxNN modifies Caffe so that each conv/FC layer, expressed as matrix multiplication, is split across fixed-size crossbars (16x16, 32x32, 64x64), weights are virtually programmed, G_non-ideal matrices replace the weights and DAC/ADC models wrap each layer; re-training uses a crossbar-based forward pass and floating-point backward pass. Devices are an in-house LLG/NEGF-modelled synaptic element at 45nm CMOS with HSPICE-extracted parasitics. FCM deviates at most 0.28% from HSPICE (vs 3.51% for MNSIM) and is ~5 orders of magnitude faster; the model generation costs 0.038 s, 1.2 s and 61 s for 16x16, 32x32, 64x64 crossbars. On six ImageNet DNNs plus LeNet, ConvNet and others, accuracy degradation is minor for small networks but large for deep ones, and 150 retraining iterations only partly recover it.

## Contributions
- Characterization showing crossbar VMM errors depend on inputs, conductance state, column position and hardware instance
- Fast Crossbar Model: pre-solved equivalent non-ideal conductance matrix plus peripheral non-linear models, BLAS-realizable
- RxNN framework in Caffe for inference evaluation, energy estimation and non-ideality-aware re-training
- Application-level evaluation of 6 ImageNet DNNs showing 9.6%-32% accuracy loss

## Key claims (stable IDs)
- **2020_Jain_RxNN_TCAD#C1** — FCM is both accurate and extremely fast relative to circuit simulation — _support:_ max deviation 0.28% vs HSPICE (MNSIM 3.51%); ~5 orders of magnitude speedup — _loc:_ Sec. VIII-A, Figs. 10-11
- **2020_Jain_RxNN_TCAD#C2** — Non-ideality accuracy loss grows with network size and crossbar size — _support:_ 64x64: LeNet 0.05%, ConvNet 2.2%, VGG-16 25.6%, OverFeat 27.8%, ResNet-50 32% — _loc:_ Sec. VIII-B, Fig. 12(a)
- **2020_Jain_RxNN_TCAD#C3** — Re-training partly restores accuracy — _support:_ 150 iterations give ~9% (AlexNet), ~8% (VGG-16), ~26% (GoogleNet) improvement; a substantial gap remains — _loc:_ Sec. VIII-D, Fig. 15
- **2020_Jain_RxNN_TCAD#C4** — Smaller crossbars reduce error but cost energy — _support:_ Cross16 less degradation than Cross32 < Cross64, but higher energy since ADC/DAC dominate — _loc:_ Sec. VIII-B, Fig. 12(b), Fig. 13

## Results
- Simulation slowdown vs plain Caffe: 2.5x (inference) and 2.75x (re-training)
- Accuracy drops in two steps: FP32 to 6-bit ideal crossbar (limited precision) then to non-ideal 64x64 (device/circuit non-idealities) (Fig. 14)
- Computation energy is dominated by ADCs and DACs (Fig. 13)

## Key numbers
- tech_node: 45nm CMOS
- array_size: 16x16, 32x32, 64x64
- throughput: ~5 orders of magnitude faster than HSPICE
- accuracy: 9.6%-32% degradation for large DNNs (ResNet-50 32% at 64x64)
- bits_weight: 6b (Cross6)

## Datasets / benchmarks
ImageNet, CIFAR-10, MNIST

## Limitations
- Behavioral approximation calibrated to one device/technology (45nm CMOS, in-house synaptic model), not measured hardware
- Only CNNs/MLPs evaluated; no transformers or language models
- Model generation cost grows rapidly with crossbar size (61 s at 64x64)
- Static non-idealities assumed; no drift or temporal noise discussed

## Remarks
A foundational, carefully validated simulator that made ImageNet-scale non-ideality studies tractable; later called CxDNN in the Proc. IEEE review from the same group. Its key lesson, that errors compound with depth and array size, extrapolates to deep transformers, but the paper provides no evidence for attention or LM workloads. Comparable to MNSIM, TxSim and GENIEx for the simulation/modeling category.

## Cites (in collection, 7)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "These include (i) (re-)training [16–21], (ii) optimized weight to conductance conversion [14], (iii) rank clipping to reduce the effects of non-idealities by lowering crossbar dimensions [25], (iv) schemes to alleviate the effect of hard failures [26], and (vi) hardware solutions to address low-voltage induced drift [15], programming errors [23], and IR drop [24]."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "These include (i) (re-)training [16–21], (ii) optimized weight to conductance conversion [14], (iii) rank clipping to reduce the effects of non-idealities by lowering crossbar dimensions [25], (iv) schemes to alleviate the effect of hard failures [26], and (vi) hardware solutions to address low-voltage induced drift [15], programming errors [23], and IR drop [24]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Resistive crossbar based specialized hardware systems have been proposed for accelerating DNN inference [7–11] and training [12, 13]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Resistive crossbar based specialized hardware systems have been proposed for accelerating DNN inference [7–11] and training [12, 13]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "They may be designed using a range of emerging devices, including Resistive RAM (ReRAM), Phase Change Memory (PCM), and Spintronics [3–6]."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "Resistive crossbar based specialized hardware systems have been proposed for accelerating DNN inference [7–11] and training [12, 13]."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _contrasts/critiques_: "On the other hand, architectural models of resistive crossbars [27, 29] target design space exploration and use highly simplified error models that are reasonable for their context, but inadequate for evaluating application-level accuracy of DNNs."

## Cited by (in collection, 18)
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _contrasts/critiques_: "Prior efforts on functional modeling of crossbar-based DNN hardware can be broadly classified into efforts that model inference [14-16] and efforts that model training [12, 14]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "One such simulator, CxDNN [130], is a functional simulator that maps low-precision DNNs to resistive crossbars."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _contrasts/critiques_: "RxNN [9] is based on the rather outdated Caffe framework and only caters to analog chips dedicated to inference, lacking more advanced algorithms and pulse update schemes that are needed for training-enabled chip designs."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021) — _background_: "Most of the previous works [3, 7–10] have proposed strategies and frameworks to model and mitigate data-independent non-idealities (primarily resistive non-idealities and NVM device variations) pertaining to 1R crossbar arrays to improve on the accuracy of the mapped DNNs."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "Due to the analog nature of the MVM operations with crossbar memory arrays, the illustrated in-situ computation of MVM is prone to errors caused by various sources of device and circuit non-idealities [43], [45]."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _uses-method-or-tool_: "In recent years, several noise models [2, 19, 26] and crossbar-realistic DNN accuracy evaluation frameworks (Neurosim [17], RxNN [10], GenieX [6], Memtorch [13]) have been proposed that are integrated with hardware-aware re-training or fine-tuning of GPU-trained DNN weights, to mitigate performance losses during inference"
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _baseline/comparison_: "Some aspects of our AIMC crossbar model have been investigated individually in earlier studies, such as the effect of ADC/DAC quantization, IR-drop, and general read noise55–57, as well as data-dependent long-term noise38."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _uses-method-or-tool_: "These voltages interact with the synaptic device conductances (Gij), as shown in Fig. 3, resulting in the generation of a current (following Ohm's Law) [5, 22]."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _motivation_: "This leads to significant accuracy losses for neural networks mapped onto crossbars, especially for larger crossbars with more non-idealities [27], [29], [30]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _motivation_: "However, many non-ideal effects, such as wire resistance, Stuck-At-Fault (SAF), thermal noise, shot noise, random telegraph noise, etc. [9], are hampering the progress of real hardware implementation of large-scale deep neural network (DNN) on ReRAM crossbar-based accelerator."
- [2019_Angizi_AnalogVsDigitalPIM_ISVLSI](2019_Angizi_AnalogVsDigitalPIM_ISVLSI.md) Analog vs Digital PIM (2019) — _background_: "Many recent works have investigated such issues with either hardware or software solutions [11, 17]."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2020_Jain_RxNN_TCAD.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2020_Jain_RxNN_TCAD.pdf)
- Full text: [../fulltext/2020_Jain_RxNN_TCAD.txt](../fulltext/2020_Jain_RxNN_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2020.3000185
