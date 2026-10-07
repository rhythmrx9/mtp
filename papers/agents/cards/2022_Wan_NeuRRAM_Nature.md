---
id: W4292121737
key: 2022_Wan_NeuRRAM_Nature
title: "A compute-in-memory chip based on resistive random-access memory"
short: "NeuRRAM"
year: 2022
venue: "Nature"
venue_full: "Nature, vol. 608 (2022)"
authors: "Weier Wan, Rajkumar Chinnakonda Kubendran, Clemens Schaefer, Sukru Burc Eryilmaz, Wenqiang Zhang, Dabin Wu, Stephen R. Deiss, Priyanka Raina, He Qian, Bin Gao, Siddharth Joshi, Huaqiang Wu et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "LSTM/RNN", "Other"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "analog-mvm", "weight-mapping", "noise-injection", "chip-in-the-loop", "write-verify-programming", "peripheral-circuits", "energy-efficiency"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 39
cites_in_collection: 14
citations_overall: 922
priority_score: 13.97
doi: "https://doi.org/10.1038/s41586-022-04992-8"
pdf: "../../02_Fabricated_Chips_and_Macros/2022_Wan_NeuRRAM_Nature.pdf"
fulltext: "../fulltext/2022_Wan_NeuRRAM_Nature.txt"
---

# NeuRRAM

**A compute-in-memory chip based on resistive random-access memory** — Nature, vol. 608 (2022) (2022)

## TL;DR
NeuRRAM is a 130-nm, 48-core, 3M-RRAM CIM chip with a voltage-mode neuron/ADC and bidirectional transposable array that achieves 1.6-2.3x lower EDP than prior RRAM-CIM chips while giving hardware-measured accuracy comparable to 4-bit software models (99.0% MNIST, 85.7% CIFAR-10, 84.7% speech commands).

## Summary
Prior RRAM-CIM chips trade off energy efficiency, model versatility and software-comparable accuracy, and many benchmark results came from software emulation of device data. NeuRRAM co-optimizes device, circuit, architecture and algorithm: each of 48 CIM cores contains a 256x256 RRAM transposable neurosynaptic array (TNSA, 16x16 corelets) with 256 interleaved CMOS neuron circuits that act as ADC plus activation, performing voltage-mode sensing (charge sampled from the floating output line onto an integration capacitor, then charge-decrement ADC). The TNSA lets one array do forward, backward and recurrent MVM without duplicated ADCs. Weights are stored as differential pairs of analogue RRAM conductances (two cells per weight, write-verify programmed), inputs are applied as pulses (multi-bit via repeated pulses), and layers are mapped with data-parallel duplication, model-parallel pipelining and splitting of oversized layers across cores; buffers and partial-sum accumulation are done in an FPGA on the board. Models are trained with Gaussian noise injected into high-precision weights, with chip-in-the-loop progressive fine-tuning for deep CNNs (ResNet-20). Fully hardware-measured inference is reported for CNNs (MNIST, CIFAR-10), a 4-cell LSTM (Google speech commands) and an RBM (MNIST image recovery).

## Contributions
- Voltage-mode neuron circuit performing in-memory MVM sensing and ADC, enabling full row and column parallelism with 1.6-2.3x lower EDP and 7-13x higher computational density than prior RRAM-CIM chips
- Transposable neurosynaptic array (TNSA) giving reconfigurable dataflow direction (forward, backward, recurrent) with minimal area/energy overhead
- 48-core reconfigurable chip supporting multiple weight-mapping strategies (data and model parallelism)
- Hardware-algorithm co-optimization: noise-injection training, analogue write-verify programming and chip-in-the-loop progressive fine-tuning
- Fully hardware-measured results across CNN, LSTM and probabilistic-graphical-model workloads

## Key claims (stable IDs)
- **2022_Wan_NeuRRAM_Nature#C1** — NeuRRAM achieves lower EDP and higher compute density than prior RRAM-CIM chips despite an older node — _support:_ 1.6x-2.3x lower EDP, 7x-13x higher computational density per million RRAMs — _loc:_ Fig. 1d, Extended Data Table 1, Efficient voltage-mode neuron circuit section
- **2022_Wan_NeuRRAM_Nature#C2** — Measured accuracy is comparable to 4-bit-weight software models using only 2 RRAM cells per weight — _support:_ 0.98% error on MNIST, 14.34% error CIFAR-10 (ResNet-20), 15.34% error speech commands, 70% L2 reconstruction-error reduction on RBM — _loc:_ Fig. 1e
- **2022_Wan_NeuRRAM_Nature#C3** — Noise-injection training greatly improves robustness to RRAM conductance relaxation — _support:_ CIFAR-10 accuracy 25.34% without vs 85.99% with noise injection (simulation) — _loc:_ Fig. 5a
- **2022_Wan_NeuRRAM_Nature#C4** — Chip-in-the-loop progressive fine-tuning recovers accuracy lost to nonlinear non-idealities without reprogramming — _support:_ Multi-core ResNet-20 measured 83.67% vs 87.03% software 4-bit; fine-tuning gives +1.99% cumulative accuracy — _loc:_ Fig. 4d, Fig. 5b

## Results
- 1.6-2.3x lower EDP and 7-13x higher computational density (throughput per million RRAMs) than prior RRAM-CIM chips across MVM input/output bit-precisions (Fig. 1d)
- MNIST 99.0% (7-layer CNN), CIFAR-10 85.7% (ResNet-20), Google speech command 84.7% (4 parallel LSTM cells), 70% image-reconstruction error reduction (RBM)
- Measured ResNet-20 before fine-tuning 83.67% vs 87.03% for 4-bit software baseline; progressive fine-tuning adds 1.99% (Fig. 5b)
- Simulation vs measurement gap of 2.32% for CIFAR-10 (Fig. 5a), showing that emulation misses hardware non-idealities
- Core utilization 4.5%-24.2% across demonstrated models (Table 1); ResNet-20 uses 48 cores, ~553k RRAMs

## Key numbers
- tech_node: 130nm
- array_size: 256x256 per core, 48 cores
- energy_eff: 1.6-2.3x lower EDP than prior RRAM-CIM
- throughput: 7-13x higher compute density
- accuracy: 85.7% CIFAR-10 (ResNet-20); 99.0% MNIST; 84.7% speech commands
- bits_weight: 4b-equivalent (2 RRAM cells/weight)
- bits_adc: variable via charge-decrement neuron ADC

## Datasets / benchmarks
MNIST, CIFAR-10, Google Speech Commands

## Limitations
- Peak EDP numbers assume 100% array utilization and exclude intermediate data transfer; reported utilization is only 4.5-24.2%
- Intermediate buffers and partial-sum accumulators live in an FPGA, not on-chip
- Only small edge models (MLPerf Tiny scale); no transformers or language models
- Deep CNN needs chip-in-the-loop fine-tuning per chip; accuracy still below full-precision digital
- Voltage drop and shared bias voltages across cores give nonlinear errors that accumulate with depth
- 130-nm technology; scaling to 7 nm is only projected (Methods)

## Remarks
A landmark, rigorously measured demonstration; evidence is strong for CNN/LSTM-class edge workloads, and the paper is a key reference for noise-injection training plus chip-in-the-loop fine-tuning. For language models the lessons are the need for high-precision analog weight storage with noise-aware training and for NoC/inter-array pipelining, which the authors flag as next challenges; none of this is tested on attention or large weight matrices. Related to the 2020-2021 ReRAM/PCM macros (Liu ISSCC 2020, Xue ISSCC 2019, Narayanan 2021) that it benchmarks against.

## Use in the original review
- F2 (High confidence): Analog CIM has moved past simulation to fabricated, measured multi-core silicon in both PCM and RRAM: IBM's 14 nm chip, IBM's 64-core HERMES chip, and NeuRRAM. HERMES's 400 GOPS/mm² in 4-phase mode is more than 15× higher than previous multi-core resistive-memory AIMC chips.
- F3 (High confidence): Measured on-chip accuracy is close to software but not free, and the penalty grows with model scale — from full software-equivalence on keyword spotting, to <1 pp on ResNet-9, to 1.8 pp on ALBERT/GLUE, to a missed equivalence threshold on a 45M-weight RNN-T.

## Cites (in collection, 14)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Compute-in-memory (CIM) based on resistive random-access memory (RRAM) promises to meet such demand... thus eliminating power-hungry data movement between separate compute and memory [refs 2-5]."
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017) — _background_: "These techniques can be more generally applied to other non-volatile resistive memory technologies such as phase-change memory8,17,21,23,24, magnetoresistive RAM48 and ferroelectric field-effect transistors49."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "...thus eliminating power-hungry data movement between separate compute and memory2-5."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "As resistive memory continues to scale towards offering tera-bits of on-chip memory50, such a co-optimization approach will equip CIM hardware on the edge with sufficient performance, efficiency and versatility to perform complex AI tasks that can only be done on the cloud today."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Multi-core architecture design with network-on-chip that realizes efficient and versatile data transfers and inter-array pipelining is likely to be the next major challenge for RRAM-CIM [ISAAC, PUMA]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "...thus eliminating power-hungry data movement between separate compute and memory2-5."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _baseline/comparison_: "More recent studies have demonstrated fully integrated RRAM complementary metal–oxide–semiconductor (CMOS) chips capable of performing in-memory matrix-vector multiplication (MVM)6–17."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Network-on-chip and program scheduling need to be carefully designed to achieve good end-to-end application-level energy efficiency [ISAAC, PUMA]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)

## Cited by (in collection, 39)
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "For example, Wan et al. [25] use a differential pair in their weight encoding, but instead of dividing the positive and negative to separate arrays, the subtraction is directly done in the adjacents cells using inputs with opposite orientations."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _baseline/comparison_: "Recently, multi-core chips supporting larger networks (> 1M weights) have demonstrated promising inference accuracy results on more difficult benchmarks, such as image recognition on the CIFAR dataset, and high MVM energy efficiency (refs 20-25)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "Analog-AI HW avoids these inefficiencies by leveraging arrays of non-volatile memory (NVM) to perform the ‘multiply and accumulate computation’ (MAC) operations which dominate these workloads directly in the memory3–7."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "Although some promising, small-sized DNN prototype demonstrations exist43–49, it remains unclear how robust the AIMC deployment of realistically sized AI workloads will be."
- [2023_Pelke_MultiCoreCNNMapping_VLSI-SoC](2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.md) Multi-core RRAM CNN Mapping (2023) — _background_: "Previous works presented accelerator architectures that use RRAM crossbars as matrix-vector multiplication (MVM) units [5-8]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "Some of these models, such as the PCMLikeNoiseModel50 and ReRamWan2022NoiseModel9 are hardware-calibrated."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "Often, a CiM implementation is published as a macro [16–24], which we define as an array of memory cells plus the additional components needed to compute full MAC operations."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _contrasts/critiques_: "Unfortunately, most of the recent works focus on the demonstration of the neural network acceleration for inference on edge applications which only consists of the information forwarding process [5–12]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _background_: "Recent publications of large-scale integrated AIMC chips, using phase change memory (PCM) 22,23, resistive RAM (ReRAM)24-26 and Flash27, show the viability of the technology."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _background_: "Diverse technologies including resistive randomaccess memory (ReRAM) and phase change memory are being considered as promising crossbar candidates to implement the multiply and accumulate operations representing the standard synaptic weights model used in most neural networks11–19."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2025_Qin_NVCiMPT_DATE](2025_Qin_NVCiMPT_DATE.md) NVCiM-PT (2025) — _background_: "RRAM stores data by changing the resistance across a dielectric material [18], while FeFET utilizes ferroelectric materials to maintain data through polarization states [19]."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _background_: "AIMC can be implemented in various ways, for example, using volatile memory [9] or non-volatile memory (NVM) for weight storage; storing one or multiple bits of weights per memory device; and reading memory arrays using analog read voltages [10] or a constant voltage with analog durations [11]."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "Demonstrator chips achieving low power massively parallel matrixvector multiplication (MVM) operations have been built using arrays of Resistive Random Access Memory (RRAM) [34] and Phase Change Memory (PCM) [20]."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _background_: "To mitigate this issue, charge-based integration is an energy-efficient alternative35,36."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _background_: "Among the memory types suitable for integration into advanced commercial processes, filamentary memristors have been extensively studied for analogue in-memory neural network inference7,8,23."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _background_: "Analog accelerators based on CIM have been demonstrated using various NVM technologies, e.g., Flash3–5, PCM6–9, RRAM10–13, MRAM14–16, ECRAM17–19, or ferroelectric devices20–22."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _background_: "High-performance silicon demonstrations of multi-core IMC accelerators using RRAM [16] and PCM [17] have been recently presented, finally grounding years of research in experimental measurements."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _motivation_: "Second, these errors could accumulate from devices to arrays8 and hence fundamentally limit the scalability and accuracy of analogue CIM, restricting its practical applications for deep neural networks (DNNs) and scientific computing."
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _background_: "A wide range of devices have been explored for AIMC, including phasechange memory (PCM) [13], [14], resistive random-access memory (RRAM) [15], magnetoresistive random-access memory (MRAM) [16], and Flash [17], [18], showing promising results in terms of compute density and efficiency."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _motivation_: "While studies have shown that AI models exhibit inherent tolerance to various errors, including conductance noises, real hardware [1, 15, 16] demonstrate that resistance noises play a crucial role in determining the model's accuracy."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "The recent demonstration of embedded RRAM devices at Mbit capacity [8] enables the design and integration of IMC circuits [9]-[11], thus paving the way for energy efficient RRAM-based accelerators of artificial intelligence (AI)."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "The efficacy of these methods has been successfully validated on recently developed AIMC chips [19–21] for small CNNs and RNNs with less than 50 million parameters."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "In practical CIM deployment, input-related errors are typically managed at the circuit or architecture level using techniques like dynamic range scaling or error-compensating ADCs [68]."
- [2026_Zheng_InterfaceKVQ_ICCAD](2026_Zheng_InterfaceKVQ_ICCAD.md) InterfaceKVQ (2026) — _background_: "A compute-in-memory (CiM) accelerator performs the multiplyaccumulate inside the memory array: weights are cell conductances in a crossbar, inputs drive the rows as voltages, and each column’s accumulated current yields one dot product in the analog domain [29]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2024_Ahsan_SPICEenvmACIMFramework_ICCAD](2024_Ahsan_SPICEenvmACIMFramework_ICCAD.md) SPICE eNVM ACIM Framework (2024)
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2022_Wan_NeuRRAM_Nature.pdf](../../02_Fabricated_Chips_and_Macros/2022_Wan_NeuRRAM_Nature.pdf)
- Full text: [../fulltext/2022_Wan_NeuRRAM_Nature.txt](../fulltext/2022_Wan_NeuRRAM_Nature.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41586-022-04992-8
