---
id: W2794288888
key: 2018_Chen_65nm1MbReRAMMacro_ISSCC
title: "A 65nm 1Mb nonvolatile computing-in-memory ReRAM macro with sub-16ns multiply-and-accumulate for binary DNN AI edge processors"
short: "65nm 1Mb ReRAM nvCIM Macro"
year: 2018
venue: "ISSCC"
venue_full: "2018 IEEE International Solid-State Circuits Conference (ISSCC)"
authors: "Wei-Hao Chen, Kaixiang Li, Wei‐Yu Lin, Kuo-Hsiang Hsu, Pinyi Li, Cheng‐Han Yang, Cheng-Xin Xue, En-Yu Yang, Yen-Kai Chen, Yun-Sheng Chang, Tzu-Hsiang Hsu, Ya‐Chin King et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "peripheral-circuits", "adc-dac", "weight-mapping", "energy-efficiency", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 32
cites_in_collection: 1
citations_overall: 334
priority_score: 10.41
doi: "https://doi.org/10.1109/isscc.2018.8310400"
pdf: "../../02_Fabricated_Chips_and_Macros/2018_Chen_65nm1MbReRAMMacro_ISSCC.pdf"
fulltext: "../fulltext/2018_Chen_65nm1MbReRAMMacro_ISSCC.txt"
---

# 65nm 1Mb ReRAM nvCIM Macro

**A 65nm 1Mb nonvolatile computing-in-memory ReRAM macro with sub-16ns multiply-and-accumulate for binary DNN AI edge processors** — 2018 IEEE International Solid-State Circuits Conference (ISSCC) (2018)

## TL;DR
First megabit nonvolatile ReRAM computing-in-memory macro (65nm 1T1R, 512k ternary weights, up to 8k MACs per CIM cycle) with a distance-racing current sense amplifier and input-aware dynamic reference, achieving measured CIM access times of 14.8 ns (3x3 CNN) and 15.6 ns (FCN) for binary-input ternary-weight DNNs.

## Summary
AI edge processors with NVM weight storage face a memory I/O bottleneck even with binary DNNs, and prior ReRAM CIM was only a 32x32 macro. This work proposes a hardware-driven binary-input ternary-weight (BITW) network: two pseudo-binary macros, nvCIM-P storing +1 weights as LRS and nvCIM-N storing -1 weights as LRS (0 weights as HRS), with digital 0/1 inputs applied on wordlines so the summed bitline current equals the MAC value. All binary weights of an n x n kernel or an m-input FCN neuron lie on the same bitline; multi-level current sense amplifiers (ML CSA) resolve j-bit MAC values, and subtraction, activation and max-pooling are performed in an in-house digital flow after the P and N macros. The macro includes a dual-mode wordline driver, a distance-racing current-mode sense amplifier (DR-CSA) that compares I_BL to two references to roughly double the sensing margin, and an input-aware dynamic reference generation scheme (IA-REF) using replica rows chosen from an input counter to track the number of active wordlines. Fabricated in a 65nm logic process with contact-ReRAM 1T1R cells, the 1 Mb macro stores 512k weights; evaluation is by silicon measurement of access time, offset and sensing margin plus MNIST accuracy for a binary DNN.

## Contributions
- First megabit nvCIM ReRAM macro for CNN/FCN, 1000x capacity of the prior 32x32 ReRAM CIM [6]
- Binary-input ternary-weight (BITW) network using two pseudo-binary macros (nvCIM-P, nvCIM-N)
- Distance-racing current-mode sense amplifier (DR-CSA) with ~2x sensing margin and <1.54% area overhead on a 1 Mb macro
- Input-aware dynamic reference generation (IA-REF) tracking input pattern and R-ratio overlap; fastest (<16 ns) CIM operation for NVMs at publication

## Key claims (stable IDs)
- **2018_Chen_65nm1MbReRAMMacro_ISSCC#C1** — Measured CIM access time (excluding path delay) is 14.8 ns for 3x3 CNN kernels and 15.6 ns for FCN with 25 inputs — _support:_ shmoo plot, 65nm — _loc:_ Fig. 31.4.6
- **2018_Chen_65nm1MbReRAMMacro_ISSCC#C2** — The macro stores 512k weights and executes up to 8k MAC operations in one CIM cycle — _support:_ 1 Mb array, s x n^2 MACs per cycle — _loc:_ Text, Fig. 31.4.2
- **2018_Chen_65nm1MbReRAMMacro_ISSCC#C3** — DR-CSA gives 5-6x lower input offset than a conventional CSA at I_BL > 40 uA and tolerates a 4x smaller minimum R-ratio — _support:_ measured/simulated comparison — _loc:_ Fig. 31.4.5
- **2018_Chen_65nm1MbReRAMMacro_ISSCC#C4** — IA-REF improves worst-case signal margin from -27.9 uA to 7.8 uA, and together with DR-CSA improves binary-DNN MNIST accuracy by 50x versus conventional CIM — _support:_ MNIST inference — _loc:_ Fig. 31.4.5
- **2018_Chen_65nm1MbReRAMMacro_ISSCC#C5** — Compared with the prior ReRAM nvCIM, speed is 2x and capacity 1000x — _support:_ vs 32x32 macro [6] — _loc:_ Text, Fig. 31.4.6

## Results
- 14.8 ns (CNN 3x3) / 15.6 ns (FCN) CIM access time, 65nm
- 1 Mb macro: 512k ternary weights, 8k parallel MACs per cycle
- DR-CSA: ~2x sensing margin, 5-6x input offset reduction, 4x smaller tolerable R-ratio, <1.54% area overhead
- IA-REF: worst-case signal margin -27.9 uA to +7.8 uA; MNIST accuracy up 50x vs conventional CIM (binary DNN)

## Key numbers
- tech_node: 65nm
- array_size: 1Mb (512k ternary weights; 8k MACs per cycle)
- accuracy: MNIST accuracy improved 50x vs conventional CIM (binary DNN); absolute value not stated in text
- bits_weight: ternary (+1,0,-1) via two binary macros
- bits_adc: j-bit multi-level current sense amplifier (j=3 example)

## Datasets / benchmarks
MNIST

## Limitations
- Binary input and ternary weights only; no multibit MAC or analog ADC resolution (later work from the group extends to multibit)
- Two-macro structure (P and N) doubles storage for signed weights
- Only small workloads (MNIST binary DNN) and no energy-efficiency figure in the digest text extracted
- Short two-page ISSCC digest: system-level results, endurance and variability across dies are not detailed in the available text; figures (die photo, summary table) are images not extracted

## Remarks
A landmark measured-silicon ReRAM CIM macro (NTHU) frequently used as a baseline in architecture and simulation papers (e.g., DL-RSIM adopts its S_OU=9 operating point and dual-reference sensing; the heterogeneous IMC cluster cites it for 8k parallel MACs). Its main lesson is that sensing margin, not the array, limits parallelism when R-ratio is small, which motivates operation-unit restrictions. The binary/ternary regime is far from the multi-bit precision needed by transformers or language models.

## Cites (in collection, 1)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _extends/builds-on_: "To achieve a smaller energy-hardware cost, this work proposes a hardware-driven binary-input ternary-weighted (BITW) network using our pseudo-binary nvCIM macros and a two-macro (nvCIM-P and nvCIM-N) DNN structure [5]: the nvCIM–P macro stores positive weights while the nvCIM-N stores negative weights."

## Cited by (in collection, 32)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _uses-method-or-tool_: "Based on a practical ReRAM-based accelerator chip [2], we choose SOU = 9, WLD resolution=1, and single-level cell as our baseline configuration in the following evaluation."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _motivation_: "Meanwhile, in the current tape-out chip of ReRAM based computing systems, the size of fabricated ReRAM crossbar is quite small, like 32 × 32 or 64 × 64 [13, 14]."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _extends/builds-on_: "Previous ReRAM CIM macros demonstrated MAC operations for 1b-input, ternaryweighted, 3b-output CNNs [1] or 1b-input, 8b-weighted, 1b-output fully-connected networks with limited accuracy [2]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _background_: "In order to achieve high reliable and accurate CNN computing, researchers and chip designers also proposed several CNN accelerators based on single bit RRAM [2, 17, 18, 21]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _uses-method-or-tool_: "Our evaluations were done using a 65nm technology and a 65nm RRAM model from [8]."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "To overcome the decreasing cost effectiveness of transistor scaling and the intrinsic inefficiency of data-shuttling in the von-Neumann architecture, CIM is proposed to realize high-speed and low-power system with parallel multiplication accumulation (MAC) computing [1][2]."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "The recent demonstration of embedded RRAM devices at Mbit capacity [8] enables the design and integration of IMC circuits [9]-[11], thus paving the way for energy efficient RRAM-based accelerators of artificial intelligence (AI)."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "A 65 nm ReRAm macro was designed to accelerate a binary convolution neural network (CNN) [39]."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _motivation_: "Therefore, there are only 9 rows, and 8 columns of ReRAM cells on a 512 × 256 crossbar for concurrent execution of MACs in the macro of a state-of-theart ReRAM-crossbar acceleration [25] in 65nm process."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _background_: "Considering ReRAM-based IMC, Chen et al. [12] demonstrate significant computing parallelism, performing 8k MAC operations simultaneously."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _motivation_: "In practice, the accumulated current deviation of ReRAM cells would severely hurt model inference accuracy [2]."
- [2023_Jang_VECOM_ICCAD](2023_Jang_VECOM_ICCAD.md) VECOM (2023) — _background_: "Several works have been proposed to ensure reliable operations with a low Rratio ReRAM device [5], [9]-[12]."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _data/numbers_: "Several studies have demonstrated that, in practice, an OU can accommodate a block with only nine WLs and eight BLs [3, 11]."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Like the VSA ADC, the CSA ADC converts multiphase analogue outputs of varying bit significance through successive current comparisons with tunable resolution44,77,78."
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _background_: "Various MAC strategies have been reported to address this challenge [41–44]."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _data/numbers_: "While the figure shows a small 3 × 3 crossbar for clarity, practical systems often use multiple much larger arrays (e.g., 512×256 [18]) to exploit massive parallelism."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)
- [2022_Jiang_ENNA_TCAS-I](2022_Jiang_ENNA_TCAS-I.md) ENNA (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2018_Chen_65nm1MbReRAMMacro_ISSCC.pdf](../../02_Fabricated_Chips_and_Macros/2018_Chen_65nm1MbReRAMMacro_ISSCC.pdf)
- Full text: [../fulltext/2018_Chen_65nm1MbReRAMMacro_ISSCC.txt](../fulltext/2018_Chen_65nm1MbReRAMMacro_ISSCC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isscc.2018.8310400
