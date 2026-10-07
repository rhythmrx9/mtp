---
id: W3015980402
key: 2020_Xue_22nm2MbReRAMCIM_ISSCC
title: "15.4 A 22nm 2Mb ReRAM Compute-in-Memory Macro with 121-28TOPS/W for Multibit MAC Computing for Tiny AI Edge Devices"
short: "22nm 2Mb ReRAM CIM Macro"
year: 2020
venue: "ISSCC"
venue_full: "2020 IEEE International Solid-State Circuits Conference (ISSCC), paper 15.4"
authors: "Cheng-Xin Xue, Tsung-Yuan Huang, Je-Syu Liu, Ting-Wei Chang, Hui-Yao Kao, Jinghong Wang, Ta-Wei Liu, Shih-Ying Wei, Sheng-Po Huang, Wei-Chen Wei, Yiren Chen, Tzu-Hsiang Hsu et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["macro", "chip-demo", "bit-slicing", "energy-efficiency", "edge-ai"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 21
cites_in_collection: 2
citations_overall: 233
priority_score: 9.78
doi: "https://doi.org/10.1109/isscc19947.2020.9063078"
pdf: null
fulltext: null
---

# 22nm 2Mb ReRAM CIM Macro

**15.4 A 22nm 2Mb ReRAM Compute-in-Memory Macro with 121-28TOPS/W for Multibit MAC Computing for Tiny AI Edge Devices** — 2020 IEEE International Solid-State Circuits Conference (ISSCC), paper 15.4 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A 22-nm 2-Mb ReRAM CIM macro, the first 4b-input nvCIM, reaching 9.8-18.3 ns access time and 121.3-28.9 TOPS/W from binary to 4b-in/4b-W/11b-out precision.

## Summary
Multi-bit CNNs need about 4b/4b input/weight precision, but earlier ReRAM nvCIM macros were limited by wide BL-current ranges, few parallel inputs, multi-cycle binary WL inputs, and costly positive/negative split weight mapping. This ISSCC macro proposes BL-IN-OUT multibit computing (BLIOMC), which uses a single WL-on with input-aware multibit BL clamping to keep BL current and its range small. It also uses scrambled 2's-complement weight mapping with input-aware SL biasing and a value combiner to cut array area and current, and a dual-bit small-offset current-mode sense amplifier to reduce reference currents and access time. The fabricated 22-nm 2-Mb macro is presented as the first 4b-input nvCIM.

## Contributions
- BLIOMC scheme with input-aware multibit BL clamping (inputs on BL, single WL on)
- Scrambled 2's-complement weight mapping (S2CWM) with IA-SLVB and S2C value combiner to reduce area overhead and BL current
- Dual-bit small-offset current-mode SA (DbSO-CSA) to reduce reference count and latency
- First 4b-input nonvolatile CIM macro in 22 nm

## Key claims (stable IDs)
- **2020_Xue_22nm2MbReRAMCIM_ISSCC#C1** — This is the first nvCIM macro supporting 4b inputs. — _support:_ 'first 4b-input nvCIM macro' — _loc:_ Abstract
- **2020_Xue_22nm2MbReRAMCIM_ISSCC#C2** — The macro reaches high efficiency across precisions. — _support:_ EF_MAC 121.3-28.9 TOPS/W from binary to 4bIN-4bW-11bOUT — _loc:_ Abstract
- **2020_Xue_22nm2MbReRAMCIM_ISSCC#C3** — The macro has short access time. — _support:_ tAC 9.8-18.3 ns — _loc:_ Abstract
- **2020_Xue_22nm2MbReRAMCIM_ISSCC#C4** — Positive/negative split weight mapping is area-costly. S2C mapping reduces area overhead and BL current. — _support:_ Prior split mapping needs 2x(m-1) cells per signed m-bit weight — _loc:_ Abstract

## Results
- 22-nm 2-Mb ReRAM-CIM macro
- tAC = 9.8-18.3 ns
- 121.3 TOPS/W (binary) to 28.9 TOPS/W (4b-in/4b-W/11b-out)

## Limitations
- Abstract-only analysis. Accuracy on CNN benchmarks was not verified
- Macro-level only. Number of rows activated in parallel is limited, so it is not a fully parallel crossbar MVM
- Efficiency numbers exclude system-level data movement and weight-update cost

## Remarks
This is the second step in the Chang-group ReRAM-CIM macro line (after Xue ISSCC 2019 at 55 nm), moving to 22 nm and 4b inputs. It is a common comparison point for NVM CIM efficiency (HERMES compares against it, for example), but its bit-serial/partial-row operation differs from the fully parallel analog MVM of PCM/ReRAM crossbar chips, so TOPS/W comparisons need care. The 8b-precision successor appeared at ISSCC 2021 and in Nature Electronics.

## Cites (in collection, 2)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)

## Cited by (in collection, 21)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "variation [18, 61]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "In a fabricated 22 nm 2 Mb ReRAM-CIM macro [65], the precision of input data was increased from binary to 4-bit."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _background_: "Other works show ReRAM-based IMC arrays as dense as 2Mb [24] or 4Mb [25], with peak energy efficiencies in the range of 120-200 TOPS/W within a power envelope of few milliwatts, suitable for tiny edge AI devices."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _motivation_: "The CPU-AIMC interplay nonetheless often is the run-time bottleneck in these systems, as AIMC tiles at competitive technology nodes typically operate on the order of hundreds of nanoseconds [12, 13]."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _motivation_: "It is demonstrated by several recent studies that for a practical ReRAM-based DNN accelerator to attain an acceptable level of inference accuracy, only nine WLs and eight BLs can be turned on concurrently [3, 11, 12]."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "Often, a CiM implementation is published as a macro [16–24], which we define as an array of memory cells plus the additional components needed to compute full MAC operations."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _motivation_: "A purely experimental approach is unfeasible since commercial tape-outs have long timelines and signiﬁcant design and fabrication costs4,20,21."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Bit significance can be managed via (1) analogue pre-processing, where scaled column currents or capacitors feed a mid-resolution ADC44,45, or (2) digital post-processing, where low-resolution ADC outputs are combined using shift-and-add logic13 (Fig. 3b)."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Although experimental results on ReRAM-based IMC systems have already been demonstrated [23]–[25], complete IMC systems based on PCM crossbar arrays had been lacking till recently [26], [27]."
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _background_: "Various MAC strategies have been reported to address this challenge [41–44]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Nikam_PassiveRRAMLSTM_TED](2021_Nikam_PassiveRRAMLSTM_TED.md) Passive RRAM LSTM (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022)
- [2022_Jiang_ENNA_TCAS-I](2022_Jiang_ENNA_TCAS-I.md) ENNA (2022)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)

## Files
- PDF: not available locally (save as `papers/02_Fabricated_Chips_and_Macros/2020_Xue_22nm2MbReRAMCIM_ISSCC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/isscc19947.2020.9063078
