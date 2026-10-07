---
id: W7160842405
key: 2026_Jiang_HighAccuracyMemristorCIM_NatMater
title: "Strategies of high-accuracy memristor-based analogue computing in memory for artificial intelligence"
short: "High-Accuracy Memristor CIM Review"
year: 2026
venue: "NatMater"
venue_full: "Nature Materials"
authors: "Zhixing Jiang, H Zhao, Jianshi Tang, Yuyao Lu, Qi Qin, Ze Wang, Ruofei Hu, Ruihua Yu, Yuan He, Junyang Zhang, Mingcheng Shi, Ning Deng et al."
category: "01 Surveys & Foundations"
devices: ["Memristor(generic)", "ReRAM"]
models: ["CNN", "LSTM/RNN", "Transformer", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "device-variation", "read-write-noise", "ir-drop-parasitics", "write-verify-programming", "adc-dac", "heterogeneous-analog-digital", "hardware-aware-training", "calibration-compensation", "3d-integration"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 0
cites_in_collection: 16
citations_overall: 5
priority_score: 7.04
doi: "https://doi.org/10.1038/s41563-026-02600-y"
pdf: "../../01_Surveys_and_Foundations/2026_Jiang_HighAccuracyMemristorCIM_NatMater.pdf"
fulltext: "../fulltext/2026_Jiang_HighAccuracyMemristorCIM_NatMater.txt"
---

# High-Accuracy Memristor CIM Review

**Strategies of high-accuracy memristor-based analogue computing in memory for artificial intelligence** — Nature Materials (2026)

## TL;DR
Nature Materials review that dissects computing-error sources in memristor analogue CIM across device, array, architecture and algorithm levels and weighs each mitigation strategy against its hardware and energy overhead, ending with a roadmap towards >8-bit accuracy, >1 Gb integration and LLM-class workloads.

## Summary
The review argues that memristor analogue CIM gains in energy and density are undermined by computing errors from device fluctuations and array parasitics, and that mitigation techniques usually add overhead that erodes the same gains. It organizes the hierarchy into (i) memristor design and device optimization (material engineering such as interface capping and oxygen-vacancy control, structural innovations such as superlattice-like switching layers and sidewall passivation, CMOS compatibility, and a node-versus-bit-precision trade-off), (ii) array-level errors (parasitic wire resistance/IR drop, sneak paths, offset/gain/programming/weight-mapping errors, 2T2R and 1S1R selectors, charge-domain CIM) with programming schemes (write-verify, waveform engineering, weight mapping using groups of devices, compensation, parameter calibration), (iii) architecture-level mix-CIM that allocates sensitive weights, bits or cells to digital cores (layer-wise, bit-wise, cell-wise), and (iv) algorithm-level hardware-aware training (hardware-out-of-the-loop noise injection and QAT, hardware-in-the-loop in-situ and chip-in-the-loop fine-tuning) versus model-driven methods (matrix expansion, local quantization, matrix regularization). A three-stage historical view (<=1 kb arrays with 1-3 bit accuracy, 1-100 kb with 4-6 bit, ~100 kb-100 Mb SoCs) and an outlook on 3D integration and adaptive analogue/digital systems for LLMs and AGI close the paper.

## Contributions
- Hierarchical error taxonomy from device to algorithm for memristor analogue CIM
- Cost-aware evaluation of mitigation strategies (overhead tables in Supplementary)
- Classification of mix-CIM granularities and hardware-aware training modes
- Roadmap with future directions (3D integration, adaptive mixed analogue/digital CIM for LLMs)

## Key claims (stable IDs)
- **2026_Jiang_HighAccuracyMemristorCIM_NatMater#C1** — Practical analogue CIM systems use only 2-32 conductance states despite single devices reaching 2,048 and 16,520 states — _support:_ cited reports — _loc:_ Sec. Memristor design
- **2026_Jiang_HighAccuracyMemristorCIM_NatMater#C2** — Cell-wise mix-CIM (CNN kernels, LSTM gates or attention heads) balances accuracy and system overhead — _support:_ reported to reach floating-point precision on regression tasks — _loc:_ Mixed-CIM section
- **2026_Jiang_HighAccuracyMemristorCIM_NatMater#C3** — Matrix expansion cuts RNNT word error rate from 42% to 7.9% on LibriSpeech at extra array cost — _support:_ cited result — _loc:_ Algorithm-level optimizations
- **2026_Jiang_HighAccuracyMemristorCIM_NatMater#C4** — Chip-in-the-loop progressive fine-tuning gives 1.99% accuracy gain on CIFAR-10 ResNet-20 — _support:_ cited result — _loc:_ Algorithm-level optimizations

## Results
- Programming precision of memristors remains below 8 bits, limited by random telegraph noise
- Sensitivity to programming error, IR drop and ADC quantization error differs by orders of magnitude across networks
- Roadmap: >8-bit accuracy, >1 Gb integration density, >100 Mb/mm2 and >1 TB/s with 3D integration

## Key numbers
- bits_weight: practical 2-32 conductance states

## Datasets / benchmarks
MNIST, CIFAR-10, LibriSpeech (MLPerf RNNT)

## Limitations
- Review scope is memristor (mostly ReRAM) CIM; PCM and other devices only touched
- Overhead comparisons are rough estimates (Supplementary Table 4)
- LLM deployment treated only as a future direction; no language-model results
- Quantitative cross-paper normalization is limited

## Remarks
Useful map of where errors originate and what each fix costs; frames accuracy as a cost trade-off, not a hard limit. Highly relevant background for mapping transformers/SLMs to crossbars: cell-wise mix-CIM by attention head and bit-wise MSB/LSB splits are directly applicable ideas, though the review gives no LLM data.

## Use in the original review
- F9 (High confidence): Device non-idealities are the physical limit and span a hierarchy, not just the material: memory window, read noise, program noise and conductance drift act on different time scales while constraining manufacturability; errors originate at device, array, architecture and algorithm levels. NVM writes cost 1–2 orders of magnitude more latency and energy per bit than SRAM, with ~106–109 write endurance.
- R1 (Refuted 0–3): “Accuracy, not energy efficiency, is the binding constraint on memristor-based analogue CIM — high efficiency and high accuracy cannot be achieved simultaneously.”

## Cites (in collection, 16)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Substantial progress has been made in developing analogue CIM chips for AI, evolving from initial proof-of-concept arrays5 to board-level integrated systems6–9 and recently achieving full system-on-chip integration10,11."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "Substantial progress has been made in developing analogue CIM chips for AI, evolving from initial proof-of-concept arrays5 to board-level integrated systems6–9 and recently achieving full system-on-chip integration10,11."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _data/numbers_: "However, a trade-off emerges between the technology node advancement and the achievable bit precision of memristors7,8,39,44–59, as illustrated in Fig. 2i,j."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "The 2T2R configuration70 offers a distinct advantage by inherently reducing the accumulated source line current to mitigate IR drop while simultaneously enabling sign representation of synaptic weights, establishing it as a practical solution."
- [2021_Chen_CAP-RAM_JSSC](2021_Chen_CAP-RAM_JSSC.md) CAP-RAM (2021) — _background_: "Moreover, charge-domain CIM also offers an effective means to high energy efficiency and throughput110."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "Previous studies have indicated that incremental steps in write voltage pulse amplitude, particularly via the word line84,85, offer superior efficiency compared with incremental steps in pulse width86."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _background_: "Hardware-out-of-the-loop (HOL) methods, such as noise-injected training116 and quantization-aware training117, incorporate a hardware non-ideality model into the training loop to enhance robustness."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _motivation_: "Second, these errors could accumulate from devices to arrays8 and hence fundamentally limit the scalability and accuracy of analogue CIM, restricting its practical applications for deep neural networks (DNNs) and scientific computing."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Successful demonstrations across diverse domains including AI12,13, signal processing14,15 and scientific computing16 underscore the potential of this technology to fundamentally revolutionize hardware for those data-intensive applications."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _data/numbers_: "Matrix expansion13 introduces redundancy by expanding a small weight matrix into a larger one, reducing the word error rate from 42 to 7.9% on LibriSpeech with MLPerF RNNT13."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _data/numbers_: "Furthermore, the sensitivity to specific non-idealities, such as the programming error, IR drop and ADC quantization error, can differ by orders of magnitude depending on the specific neural network task77."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _contrasts/critiques_: "Whereas previous research studies and reviews4,17,18 have investigated the device innovations, crossbar architectures or hardware–algorithm co-optimization strategies, they rarely scrutinize the accuracy–overhead trade-off that is inherent to these solutions."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _data/numbers_: "Whereas single devices demonstrating up to 2,048 and 16,520 conductance states have been reported28,48, practical analogue CIM systems typically utilize only 2–32 states7–9,46."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "In practical scenarios, strategies of different granularities can be jointly used for achieving a better performance, such as combining both the layer-wise and cell-wise mix-CIM113 or utilizing both bit-wise and layer-wise approaches46."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)

## Files
- PDF: [../../01_Surveys_and_Foundations/2026_Jiang_HighAccuracyMemristorCIM_NatMater.pdf](../../01_Surveys_and_Foundations/2026_Jiang_HighAccuracyMemristorCIM_NatMater.pdf)
- Full text: [../fulltext/2026_Jiang_HighAccuracyMemristorCIM_NatMater.txt](../fulltext/2026_Jiang_HighAccuracyMemristorCIM_NatMater.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41563-026-02600-y
