---
id: W4313254474
key: 2022_Haensch_CIMNVMCodesignReview_AdvMater
title: "Compute in‐Memory with Non‐Volatile Elements for Neural Networks: A Review from a Co‐Design Perspective"
short: "CIM-NVM-Codesign-Review"
year: 2022
venue: "AdvMater"
venue_full: "Advanced Materials (2022)"
authors: "Wilfried E. Haensch, Anand Raghunathan, Kaushik Roy, Bhaswar Chakrabarti, Charudatta Phatak, Cheng Wang, Supratik Guha"
category: "01 Surveys & Foundations"
devices: ["PCM", "ReRAM", "MRAM", "ECRAM", "FeFET", "SRAM-analog"]
models: ["CNN", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "crossbar-architecture", "analog-mvm", "bit-slicing", "adc-dac", "ir-drop-parasitics", "device-variation", "endurance-retention"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 21
citations_overall: 134
priority_score: 4.99
doi: "https://doi.org/10.1002/adma.202204944"
pdf: "../../01_Surveys_and_Foundations/2022_Haensch_CIMNVMCodesignReview_AdvMater.pdf"
fulltext: "../fulltext/2022_Haensch_CIMNVMCodesignReview_AdvMater.txt"
---

# CIM-NVM-Codesign-Review

**Compute in‐Memory with Non‐Volatile Elements for Neural Networks: A Review from a Co‐Design Perspective** — Advanced Materials (2022) (2022)

## TL;DR
Co-design review linking NVM material properties (PCM, RRAM, MRAM, ECRAM, FeFET/FTJ) to crossbar CIM sub-system requirements for digital-storage/analog-MAC and all-analog inference and training, concluding no device meets all targets and that cells should be about 1-2 bits because ADC cost grows exponentially.

## Summary
The review addresses the von Neumann memory wall for deep learning and asks what NVM material and device properties crossbar compute-in-memory actually needs. It distinguishes (b) digital (single/multi-bit) NVM storage with analog MVM and (c) all-analog CIM with a sliding conductance scale and in-array parallel weight update. Section 2 derives hardware considerations: crossbar as analog MAC engine, bit slicing of high-precision weights across lower-precision cells, partitioning large matrices over arrays of 10^3-10^4 devices, convolution-to-MVM mapping with tiling and partial-sum accumulation, energy bounds, and neuron/ADC peripherals. It enumerates non-idealities (IR drop, noise/drift, sensing margin, write linearity/endurance) and turns them into device targets such as LRS of 100-200 kOhm for 64x64/128x128 arrays and ON/OFF >= 5-10. Section 3 surveys PCM, filamentary/interfacial RRAM, ECRAM, ferroelectric (FTJ, FeFET) and MRAM with their maturity and demonstrations; Section 4 compares them against the requirements and Section 6 gives a summary table of single-device metrics. No new experiments or simulations are run; it is a literature synthesis with analytic estimates. Language models are not discussed.

## Contributions
- Frames CIM materials requirements per architecture option: digital-memory/analog-compute versus all-analog compute and update.
- Quantitative translation of crossbar non-idealities (IR drop, sensing margin, ADC overhead, write endurance) into device targets.
- Critical survey of PCM, RRAM, ECRAM, FTJ/FeFET and MRAM including reported crossbar demonstrations.
- Summary table of single-device properties and gap analysis versus SRAM.

## Key claims (stable IDs)
- **2022_Haensch_CIMNVMCodesignReview_AdvMater#C1** — ADC dominates crossbar CIM cost. — _support:_ ADC consumes about 60% of total energy and over 80% of chip area in CIM hardware — _loc:_ Sec. 2.2, Fig. 5
- **2022_Haensch_CIMNVMCodesignReview_AdvMater#C2** — Crossbar efficiency is optimal at about 1-2 bits per cell; more than 2 bits/cell is not worth the ADC overhead. — _support:_ ADC energy/area grow exponentially with bit precision; exceeding 2 bits/cell overshadows density gains — _loc:_ Sec. 2.5
- **2022_Haensch_CIMNVMCodesignReview_AdvMater#C3** — LRS of 100-200 kOhm minimises IR drop for 64x64 to 128x128 arrays. — _support:_ Cited from ref [36] — _loc:_ Sec. 2.5
- **2022_Haensch_CIMNVMCodesignReview_AdvMater#C4** — ON/OFF ratio of at least 5-10 suffices for CIM crossbars. — _support:_ Cited from ref [49] — _loc:_ Sec. 2.5
- **2022_Haensch_CIMNVMCodesignReview_AdvMater#C5** — No NVM candidate meets all requirements; payoff is larger for training than inference. — _support:_ Conclusion statement — _loc:_ Sec. 5

## Results
- Qualitative/analytic: ADC about 60% energy and over 80% area in CIM (Fig. 5).
- Optimal 1-2 bits/cell; high-precision weights handled by bit slicing across cells.
- MRAM most mature with endurance above 10^15 cycles but low ON/OFF; RRAM/PCM offer compact cells, large ON/OFF, multi-bit capability.
- Fully integrated PCM MVM demos [174][175] narrow the gap between experiment and theory once noise and drift are mitigated.

## Key numbers
- array_size: 64x64 to 128x128 (moderate); 10^3-10^4 devices per crossbar
- bits_weight: 1-2 bits/cell optimal
- bits_adc: 8-bit for 128 rows, 2-bit cells, 1-bit stream

## Limitations
- Review only: no new measurements or simulations.
- Training-time non-idealities and large-model (Transformer/LLM) mapping are treated shallowly; focus on CNN/MLP.
- Device table is single-device data, not array-level.

## Remarks
Useful as a materials-to-architecture bridge: it states why 1-2 bits/cell, bit slicing and ADC-aware design recur in the collection. It predates the LLM-on-AIMC wave and says nothing about language models, so its relevance to SLM deployment is indirect (device requirements, ADC bottleneck). Complements architecture-focused surveys and the PCM chip papers it cites.

## Cites (in collection, 21)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Compared to MRAM, RRAM and PCM offer the advantages of compact cell size, large ON/OFF ratio and multi-bit capability [78] [171] [178] [179]."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _data/numbers_: "In [169] a RRAM based cross-bar array with off-chip peripheral circuits was built with a Ta/HFO2/Pd stack as a switching element accessible through a select transistor... The demonstration vehicle was a one-layer (96 x 40) network for hand written digit classification (MNIST)... Classification error was 89.9% which was 2.5% shy of theoretical expectation for the same configuration."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _data/numbers_: "It has been shown that On-resistance in the range of 100-200 kΩ leads to minimal IR drop for moderate crossbar array sizes (such as 64 x 64 or 128 x 128) [36]."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "There have been an increasing number of experimental studies of all analog CIM that involve inference as well as training [58] [25] [53]."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "the most competitive candidates at present among emerging memories are resistive random-access memory (RRAM) [76] [77] [78] [79] [80] [81] [82] [83] [84] [37], phase-change memory (PCM) [85] [34] [86], and magnetic random-access memory (MRAM) [87] [88] [89] [90] [91]."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "the most competitive candidates at present among emerging memories are resistive random-access memory (RRAM) [76] [77] [78] [79] [80] [81] [82] [83] [84] [37]..."
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018) — _background_: "The mechanism and operation of all analog MAC has also been described in detail elsewhere [59] [52] [57]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "Due to the analog nature of the MVM operations with crossbar memory arrays, the illustrated in-situ computation of MVM is prone to errors caused by various sources of device and circuit non-idealities [43], [45]."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "Excellent recent reviews on these five types of memories, mentioned above, have been published earlier [94] [77] [95] [96] [97] [98] [99] [100] [101] [102] [103] [104]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "the most competitive candidates at present among emerging memories are resistive random-access memory (RRAM) ... phase-change memory (PCM) [85] [34] [86]..."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "A more complex network implantation using RRAM MVMs is presented in [171]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _data/numbers_: "As is illustrated in Figure 5, ADC consumes about 60% of the total energy, and over 80% of the chip area in CIM hardware [27]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "It has been shown, however, that individual direct write introduces errors that cannot easily be compensated [65]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "As discussed earlier, the weight transfer into an analog storage mode requires special considerations [182] [183]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _data/numbers_: "For example, a moderate array size containing 128 rows with 2-bit memory devices and 1-bit per stream already requires a 8bit ADC [41]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "It has been demonstrated that the IR drop leads to significant error due to the reduction of the output currents in the array, especially for larger array sizes [43]."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _motivation_: "Therefore, it is important to develop simulation tools that can capture these variations for relevant examples [47]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Potential for scalability was shown in [175] in which a convolutional network with 9 layers was demonstrated using the CIFAR10 dataset."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _background_: "In light of the variability and programmability issues with multibit devices, some recent demonstration of integrated RRAM CIM chips used binary weight storage (LRS and HRS), and partitioned high precision matrix elements to multiple memory cells [180] [181]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Recent work from Samsung has shown a 64 x 64 cross-bar array of STT-MRAMs integrated with 28nm CMOS technology to realize in-memory computing [164]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)

## Files
- PDF: [../../01_Surveys_and_Foundations/2022_Haensch_CIMNVMCodesignReview_AdvMater.pdf](../../01_Surveys_and_Foundations/2022_Haensch_CIMNVMCodesignReview_AdvMater.pdf)
- Full text: [../fulltext/2022_Haensch_CIMNVMCodesignReview_AdvMater.txt](../fulltext/2022_Haensch_CIMNVMCodesignReview_AdvMater.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1002/adma.202204944
