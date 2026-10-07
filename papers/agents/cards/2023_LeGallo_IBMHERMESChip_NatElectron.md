---
id: W4385896568
key: 2023_LeGallo_IBMHERMESChip_NatElectron
title: "A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference"
short: "IBM HERMES 64-core"
year: 2023
venue: "NatElectron"
venue_full: "Nature Electronics"
authors: "Manuel Le Gallo, Riduan Khaddam-Aljameh, Miloš Stanisavljević, Athanasios Vasilopoulos, Benedikt Kersting, Martino Dazzi, Geethan Karunaratne, Matthias Brändli, Abhairaj Singh, Silvia M. Müller, Julian Büchel, Xavier Timoneda et al."
category: "02 Fabricated Chips & Macros"
devices: ["PCM"]
models: ["CNN", "ResNet", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "analog-mvm", "write-verify-programming", "conductance-drift", "adc-dac", "hardware-aware-training", "noise-injection", "heterogeneous-analog-digital", "energy-efficiency"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 27
cites_in_collection: 13
citations_overall: 300
priority_score: 13.17
doi: "https://doi.org/10.1038/s41928-023-01010-1"
pdf: "../../02_Fabricated_Chips_and_Macros/2023_LeGallo_IBMHERMESChip_NatElectron.pdf"
fulltext: "../fulltext/2023_LeGallo_IBMHERMESChip_NatElectron.txt"
---

# IBM HERMES 64-core

**A 64-core mixed-signal in-memory compute chip based on phase-change memory for deep neural network inference** — Nature Electronics (2023)

## TL;DR
IBM HERMES Project Chip: a 14nm CMOS, 64-core (256x256) PCM analog in-memory chip with on-chip digital activation/LSTM units that runs ResNet-9 (92.81% CIFAR-10), a PTB LSTM and a 4M-weight image-captioning LSTM near software accuracy, at 63.1 TOPS peak and 9.76 TOPS/W (1-phase).

## Summary
The paper addresses the gap between single-core AIMC demos and end-to-end inference: needed are many cores, on-chip digital operations/communication, and high accuracy without network-specific chip retuning. The chip has 64 cores each with a 256x256 array of unit-cells made of four mushroom-type PCM devices (two per polarity, differential), 256 time-based current-controlled-oscillator ADCs with PWM inputs, local digital processing units (LDPUs) for batch-norm/ReLU/bias/aggregation, global digital units (GDPU) for sigmoid/tanh/LSTM cell state, and an on-chip network. Weights are mapped via G = W*Gmax/Wmax per core and programmed with closed-loop iterative program-and-verify (max 30 iterations, 5 ADC-count margin) in either one-device (ODP) or two-device (TDP) mode. Networks are trained hardware-aware with weight-noise injection using IBM AIHWKit, large layers are split over cores with partial sums aggregated in LDPUs, and only max-pooling and embeddings run off-chip while activation vectors travel via an FPGA. Evaluation measures MVM error over all 64 cores (2,048 random vectors), drift over time, and inference accuracy on ResNet-9 (1.87M weights), PTB character LSTM (1.30M) and Flickr8k caption LSTM (4.08M, all 64 cores).

## Contributions
- First multi-core PCM AIMC chip (64 cores, >4M weights) with fully integrated ADC/DAC and digital units for ResNet and LSTM
- Application-independent calibration: no per-network chip re-tuning
- One- vs two-device-per-weight programming analysis (ODP/TDP) with measured MVM error decomposition
- Highest CIFAR-10 accuracy among multi-core resistive AIMC chips and >15x higher MVM throughput per area than prior multi-core resistive chips

## Key claims (stable IDs)
- **2023_LeGallo_IBMHERMESChip_NatElectron#C1** — ResNet-9 on chip reaches near-software accuracy — _support:_ 92.81% (TDP) vs 93.67% software; ODP 92.23% — _loc:_ Sec. V, Fig. 3c
- **2023_LeGallo_IBMHERMESChip_NatElectron#C2** — Weight precision equivalent to ~3-4 bits — _support:_ ODP ~3-bit, TDP between 3 and 4-bit equivalent weights with 8-bit I/O — _loc:_ Sec. IV, Fig. 2
- **2023_LeGallo_IBMHERMESChip_NatElectron#C3** — Peak throughput and efficiency — _support:_ 63.1 TOPS and 9.76 TOPS/W (1-phase), 16.1 TOPS / 2.48 TOPS/W (4-phase) — _loc:_ Sec. VI / Conclusions, Table I
- **2023_LeGallo_IBMHERMESChip_NatElectron#C4** — PCM yield high — _support:_ >99% unit-cells programmable on 63 of 64 cores; outlier core 98.4% — _loc:_ Fig. 2a
- **2023_LeGallo_IBMHERMESChip_NatElectron#C5** — Weight error dominates accuracy loss — _support:_ quantisation adds only 0.2-0.3% on top of weight error — _loc:_ Sec. V

## Results
- MVM throughput per area 400 GOPS/mm2 in 4-phase mode, >15x prior resistive multi-core AIMC chips; 1.55 TOPS/mm2 in 1-phase
- PTB LSTM: BPC less than 0.1 above the software 1.336 baseline
- ResNet-9 layer input processed in 1.52 us / 1.51 uJ; LSTM timestep 1.43 us / 5.24 uJ
- Image captioning BLEU scores on hardware essentially equal to software
- Total MVM error grows with time because of PCM drift (global drift compensation only partial) (Fig. 2d)

## Key numbers
- tech_node: 14nm CMOS + PCM BEOL
- array_size: 64 cores x 256x256
- energy_eff: 9.76 TOPS/W (1-phase), 2.48 TOPS/W (4-phase)
- throughput: 63.1 TOPS (1-phase), 16.1 TOPS (4-phase)
- accuracy: 92.81% CIFAR-10 ResNet-9 (software 93.67%)
- bits_weight: 4 PCM devices per unit-cell, ~3-4b equivalent
- bits_adc: 8b I/O (time-based CCO ADC)

## Datasets / benchmarks
CIFAR-10, Penn Treebank (character-level), Flickr8k

## Limitations
- Activations are routed between layers off-chip via FPGA; layer-to-layer on-chip transport and local activation SRAM left as future work
- Max-pooling and embeddings not supported on chip
- Weight density limited; only ~4M weights; effective ~3-4 bit weight precision
- Efficiency (9.76 TOPS/W) below SRAM AIMC chips that use off-chip weight buffers
- Small CNN/LSTM workloads, no attention or transformers

## Remarks
The reference PCM AIMC silicon in the collection: it validates the HW-aware-training plus noise-injection recipe and shows how drift and programming error define effective precision. The LSTM caption/PTB demos are closest to sequence models but are tiny; scaling to transformer/LLM layers needs the attention-capable follow-ons. Evidence is measured silicon with solid error decomposition.

## Use in the original review
- F2 (High confidence): Analog CIM has moved past simulation to fabricated, measured multi-core silicon in both PCM and RRAM: IBM's 14 nm chip, IBM's 64-core HERMES chip, and NeuRRAM. HERMES's 400 GOPS/mm² in 4-phase mode is more than 15× higher than previous multi-core resistive-memory AIMC chips.
- F3 (High confidence): Measured on-chip accuracy is close to software but not free, and the penalty grows with model scale — from full software-equivalence on keyword spotting, to <1 pp on ResNet-9, to 1.8 pp on ALBERT/GLUE, to a missed equivalence threshold on a 45M-weight RNN-T.
- F4 (High confidence): Hardware-aware training — injecting realistic device noise during training or fine-tuning — is the field's dominant and empirically validated mitigation, and it now scales to pre-trained LLMs. On under 1% of pre-training tokens, Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct retained accuracy comparable to 4-bit-weight / 8-bit-activation quantized baselines under hardware-realistic analog noise — a gap off-the-shelf LLMs cannot close on their own.

## Cites (in collection, 13)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "Early works on performing neural network inference with AIMC showed promising accuracy results in mixed hardware/software implementations, where functionalities such as digital-to-analog and analog-to-digital conversions, activation functions, and other necessary digital operations were implemented with off-chip software or hardware (refs 8-12)."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "Prior to being deployed on the chip, the networks are trained in a hardware-aware manner by injecting noise on the synaptic weights to improve their resilience to hardware nonidealities (ref 12), using the publicly available IBM Analog Hardware Acceleration Kit (ref 38)."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019) — _uses-method-or-tool_: "In order to make the model more robust to noise, we perturb the weights of each tile according to a model simulating two times the PCM programming noise derived experimentally in Ref. 46."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Early works on performing neural network inference with AIMC showed promising accuracy results in mixed hardware/software implementations, where functionalities such as digital-to-analog and analog-to-digital conversions, activation functions, and other necessary digital operations were implemented with off-chip software or hardware (refs 8-12)."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "Prior to being deployed on the chip, the networks are trained in a hardware-aware manner by injecting noise on the synaptic weights to improve their resilience to hardware nonidealities (ref 12), using the publicly available IBM Analog Hardware Acceleration Kit (ref 38)."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _baseline/comparison_: "Analog weight storage offers high weight density and the ability to operate more rows simultaneously (demonstrated up to 512) (refs 21, 25). However, this approach suffers from accuracy degradation because of the noisy analog weights and higher latency due to the need of slow high resolution analog-to-digital converters."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _extends/builds-on_: "Furthermore, the internal current mirror, which drives the attached current-controlled oscillator (CCO) unit, contains trimming registers that allow matching the gain between the different ADCs per core and compensating nonlinearity in their transfer function (ref 18)."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _baseline/comparison_: "Recently, multi-core chips supporting larger networks (> 1M weights) have demonstrated promising inference accuracy results on more difficult benchmarks, such as image recognition on the CIFAR dataset, and high MVM energy efficiency (refs 20-25)."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)

## Cited by (in collection, 27)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _data/numbers_: "For instance in a recent study54, a ResNet9 CNN was trained with a similar general HWA training approach yielding vastly improved AIMC accuracy in hardware."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _uses-method-or-tool_: "An experimental hardware accuracy validation study was performed using a 64-core IMC chip based on PCM [44]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "AIMC accelerators that are based on resistive memory device technologies such as Phase Change Memory (PCM)5–8 , Resistive Random Access Memory (ReRAM)9–12 , and Magnetic Random Access Memory (MRAM)13 , have shown great promise in accelerating and reducing the power consumption of deep learning systems."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Nonetheless, for full on-chip integration of memristive neural network, the impact of ADC resolution on VMM accuracy needs to be carefully evaluated to identify the lowest ADC resolution (and thereby required Silicon area) while preserving the neural network accuracy."
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _background_: "dedicated accelerators are required to accelerate the inference workloads of these models in resource-contained environments [2]-[5]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _data/numbers_: "In Fig. 6a we show that, for the MoE-based model, iso-performance is retained up to noise levels of 6.3%, which is within the range of noise values observed for previously published AIMC hardware22."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _uses-method-or-tool_: "To experimentally study the adversarial robustness, we employed a PCM-based AIMC chip with tiles comprising 256 × 256 synaptic unit cells29."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _contrasts/critiques_: "However, most previous works [11]–[13], [28] require hardware-aware training, which is non-trivial, if not prohibitive for LLMs with large number of parameters."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _background_: "IBM recently demonstrated two chips and one architectural extension using PCM-base AIMC on 14nm CMOS [12], [13], [19], as summarized in Table I."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "Demonstrator chips achieving low power massively parallel matrixvector multiplication (MVM) operations have been built using arrays of Resistive Random Access Memory (RRAM) [34] and Phase Change Memory (PCM) [20]."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _background_: "HWA training has been demonstrated on smaller networks, e.g., Convolutional Neural Network (CNN), LSTM7."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Techniques such as high-resistance weight encoding, adaptive reference drift compensation33,79 and program–verify using ADCs12,33 help mitigate these issues."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _background_: "High-performance silicon demonstrations of multi-core IMC accelerators using RRAM [16] and PCM [17] have been recently presented, finally grounding years of research in experimental measurements."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _motivation_: "Simulation results confirm that our method is effective on a 25.3M-parameter transformer model, a practical size suitable for deployment on currently available AIMC chips18,19."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "Successful demonstrations across diverse domains including AI12,13, signal processing14,15 and scientific computing16 underscore the potential of this technology to fundamentally revolutionize hardware for those data-intensive applications."
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _background_: "A wide range of devices have been explored for AIMC, including phasechange memory (PCM) [13], [14], resistive random-access memory (RRAM) [15], magnetoresistive random-access memory (MRAM) [16], and Flash [17], [18], showing promising results in terms of compute density and efficiency."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _data/numbers_: "On a second chip, we integrated CCO-based ADCs (one per integration-row) into PCM-based CIM-Tiles [21] (Fig. 5)."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _data/numbers_: "On a second chip, we integrated CCO-based ADCs (one per integration-row) into PCM-based CIM-Tiles [30] (Fig. 3)."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _background_: "The development of in-memory computing (IMC) accelerators, particularly those based on resistive memories, such as RRAM [1], Phase Change Memories (PCM) [2], and FeFET [3], stand out as one of the most promising solutions due to their potential for high energy efficiency and scalability."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _data/numbers_: "For instance, a 256×256 Phase Change Memory (PCM) crossbar is shown to perform a total of 65,536 MAC operations in 130ns in Le Gallo et al. [12]."
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024)
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2023_LeGallo_IBMHERMESChip_NatElectron.pdf](../../02_Fabricated_Chips_and_Macros/2023_LeGallo_IBMHERMESChip_NatElectron.pdf)
- Full text: [../fulltext/2023_LeGallo_IBMHERMESChip_NatElectron.txt](../fulltext/2023_LeGallo_IBMHERMESChip_NatElectron.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41928-023-01010-1
