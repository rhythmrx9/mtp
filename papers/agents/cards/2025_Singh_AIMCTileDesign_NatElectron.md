---
id: W4417492578
key: 2025_Singh_AIMCTileDesign_NatElectron
title: "The design of analogue in-memory computing tiles"
short: "AIMC Tile Design"
year: 2025
venue: "NatElectron"
venue_full: "Nature Electronics"
authors: "Abhairaj Singh, Manuel Le Gallo, Athanasios Vasilopoulos, Jose Luquin, Pritish Narayanan, Geoffrey W. Burr, Abu Sebastian"
category: "01 Surveys & Foundations"
devices: ["PCM", "ReRAM", "Flash", "SRAM-analog", "SRAM-digital", "Generic-NVM"]
models: []
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "analog-mvm", "adc-dac", "peripheral-circuits", "bit-slicing", "weight-mapping", "energy-efficiency", "ir-drop-parasitics"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 1
cites_in_collection: 22
citations_overall: 13
priority_score: 8.2
doi: "https://doi.org/10.1038/s41928-025-01537-5"
pdf: "../../01_Surveys_and_Foundations/2025_Singh_AIMCTileDesign_NatElectron.pdf"
fulltext: "../fulltext/2025_Singh_AIMCTileDesign_NatElectron.txt"
---

# AIMC Tile Design

**The design of analogue in-memory computing tiles** — Nature Electronics (2025)

## TL;DR
Nature Electronics Perspective from IBM dissecting non-volatile memristive AIMC tile design (weight/input/output encoding, ADC families, device comparison); a 256x256, 8-bit analysis puts the output-encoding block at 60-70% of AIMC tile energy and shows AIMC tiles incur 6-15% MVM error versus ~1% for a digital IMC tile.

## Summary
The Perspective argues that the AIMC tile is the key unit of IMC DNN accelerators and decomposes it into a unit-cell crossbar (weight encoding), an input encoding block (DAC) and an output encoding block (pre-conversion, ADC, digital post-processing) (Figs. 2-3). Weights are mapped either by analogue differential storage (a positive and a negative sub-cell per weight, optionally several devices per sign) or by digital bit-slicing in two's complement, one SLC device per bit. Inputs use bit-serial, bit-parallel (pulse-width) or bit-hybrid encoding, with sign handled by differential source-line voltages or extra phases. The paper then surveys voltage-based ADCs (flash, SAR, voltage-sense-amp, voltage-to-time) and current-based ADCs (integrate-and-fire, current-controlled oscillator, current-sense-amp) and their area/energy/latency scaling with resolution (Fig. 4). Three tiles (analogue-leaning AIMC Tile1, digital-leaning AIMC Tile2, and an SRAM DIMC tile) are compared at 256x256 and 8-bit precision using area/energy estimates from published chips and a Monte-Carlo MVM error model (Fig. 5, Supp. Notes 1-3). It closes with trends in tile figure of merit, weight capacity and density, and technology-scaling projections (Fig. 6), arguing memristive and 3D flash can hold large models fully on chip.

## Contributions
- Unified taxonomy of AIMC tile components and of weight, input and output encoding schemes for signed multibit MVM.
- Qualitative and quantitative comparison of ADC architectures for AIMC (pitch matching, sharing, latency/energy/area vs. resolution).
- Component-wise area/energy split and MVM-error comparison of two memristive AIMC tiles versus a digital IMC tile (Fig. 5).
- Survey of published IMC tile trends (FoM, weight capacity, bit-cell area) and technology-scaling projections for AIMC vs DIMC (Fig. 6).

## Key claims (stable IDs)
- **2025_Singh_AIMCTileDesign_NatElectron#C1** — Output encoding (ADC, pre/post-conversion) is the dominant energy consumer of AIMC tiles. — _support:_ 60-70% of tile energy in AIMC tiles, over 80% in the DIMC tile; memory array only 15-20% in AIMC — _loc:_ Fig. 5b
- **2025_Singh_AIMCTileDesign_NatElectron#C2** — Analogue weight encoding with one device per sign gives noticeably larger MVM error than digital IMC; multiple devices per sign reduce it at a density cost. — _support:_ AIMC Tile1 error 2% ideal to 15% non-ideal, below 10% with two devices per sign; Tile2 6% ideal; DIMC 1% — _loc:_ Fig. 5c
- **2025_Singh_AIMCTileDesign_NatElectron#C3** — Memristive unit cells give about an order of magnitude higher weight density than SRAM on the same CMOS node. — _support:_ 22-nm MLC RRAM cell (53F2) is about the size of a 3-nm 6T SRAM cell, i.e. ~2x density — _loc:_ Fig. 6c, Technology scaling section
- **2025_Singh_AIMCTileDesign_NatElectron#C4** — DIMC wins on efficiency at advanced nodes but is limited by on-chip weight capacity. — _support:_ up to tenfold efficiency gains reported but capacity <100 KB, forcing reloading for models >1 MB — _loc:_ Fig. 6a-b

## Results
- In dense PCM 256x256 arrays ADCs and support circuits consume over 40% of area and 50-60% of energy (ADC discussion).
- AIMC tile scaling projected at up to 1.2x area and 1.1x power gain per CMOS node beyond 22 nm vs 1.4x density and 1.2x energy for DIMC per node.
- PCM/RRAM on-off current ratio 10-100 vs ~1000 for 6T SRAM and <2 for STT-MRAM, limiting sensing margins.
- Program-and-verify on ADC needs ~12-bit resolution for 256 4-bit weights.

## Key numbers
- tech_node: 22nm RRAM vs 3nm SRAM bitcell comparison; 14nm PCM chips cited
- array_size: 256x256 (analysis tile)
- energy_eff: output encoding 60-70% of AIMC tile energy
- accuracy: MVM error 2-15% (AIMC Tile1), 6% ideal (Tile2), ~1% (DIMC)
- bits_weight: 8b
- bits_adc: mid-resolution (~8b) ADCs

## Limitations
- Perspective, not a measurement paper: tile comparison relies on numbers extrapolated from different chips and nodes to 256x256/8-bit.
- MVM error model is a Monte-Carlo estimate in the Supplementary Notes, not validated on one common silicon platform.
- Integer precision only; floating-point IMC and system-level (inter-tile communication, attention/KV-cache) aspects are barely treated; LLMs are mentioned only as a motivation.
- Authors are IBM Research, whose PCM analogue-differential approach is a focus.

## Remarks
A useful design reference for anyone mapping models to crossbars: weight-encoding (differential vs bit-sliced), input encoding and ADC choice set the accuracy/efficiency of every mapping. Its Fig. 5 numbers are a good sanity check for simulator ADC/DAC assumptions. It positions NVM AIMC as weight-stationary and suited to LLM inference, citing IBM's MoE/3D analog work, but offers no language-model evaluation itself. The conclusion that SRAM-AIMC and hybrid memristor-SRAM designs may dominate near term connects to the fusion chip in this collection.

## Use in the original review
- N1 (Not adjudicated): The December 2025 IBM Research perspective (Nature Electronics) frames the AIMC tile as the building block, buildable from volatile charge-based or non-volatile memristive memory; no single memory technology has been settled on, and signed multi-bit weight encoding and output conversion remain open design axes.

## Cites (in collection, 22)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "Like the VSA ADC, the CSA ADC converts multiphase analogue outputs of varying bit significance through successive current comparisons with tunable resolution44,77,78."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _background_: "Recent studies employing capacitor-based unit cells have demonstrated that such architectures exhibit strong robustness against process and device-level variations23,47."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _data/numbers_: "While 6T SRAM offers a read current ratio near 1,000, those of PCM and RRAM range from 10 to 100 (refs. 50,51), and that of spin-transfer torque MRAM often falls below 2 (ref. 52)."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Hardware-aware training or fine-tuning of DNNs, which encapsulates some of these effects in the forward pass, can be used to make models resilient to deterministic (for example, IR drop) or random (for example, read noise) sources of noise and help preserve model accuracy21,57,58."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "IMC inference chips consist of multiple IMC tiles9 (Fig. 1c)."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Bit significance can be managed via (1) analogue pre-processing, where scaled column currents or capacitors feed a mid-resolution ADC44,45, or (2) digital post-processing, where low-resolution ADC outputs are combined using shift-and-add logic13 (Fig. 3b)."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "The SAR ADC performs successive comparisons of analogue values using a binary search and an adaptive reference set based on previous decisions41,63–67."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "In the digital bit-slicing weight-storage approach, weights are typically mapped using a two’s complement format36."
- [2021_Chen_CAP-RAM_JSSC](2021_Chen_CAP-RAM_JSSC.md) CAP-RAM (2021) — _background_: "The SAR ADC performs successive comparisons of analogue values using a binary search and an adaptive reference set based on previous decisions41,63–67."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "In some scenarios involving simple activation functions such as ReLU, the generated time pulse can be clipped and consumed downstream as the pulse-width input for the next NN layer, avoiding the intermediate analogue-to-digital and digital-to-time steps entirely33,72."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _data/numbers_: "Programming memristive devices typically requires high voltages (~2 V for PCM, 3–4 V for RRAM) and 100–500-μA currents, necessitating thick oxide drivers and large select transistors43, which further limits array size."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "If multiple devices are available to encode the weight magnitude, additional options for distributing the weight magnitude across these devices become available as well, allowing optimization for placement accuracy, long-term conductance stability and other considerations34,35."
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022) — _background_: "Previous review articles focusing on particular aspects of this technology are also available22–28, including those with a primary focus on unit-cell configurations22–24 and"
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Techniques such as high-resistance weight encoding, adaptive reference drift compensation33,79 and program–verify using ADCs12,33 help mitigate these issues."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "In some scenarios involving simple activation functions such as ReLU, the generated time pulse can be clipped and consumed downstream as the pulse-width input for the next NN layer, avoiding the intermediate analogue-to-digital and digital-to-time steps entirely33,72."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "Hardware-aware training or fine-tuning of DNNs, which encapsulates some of these effects in the forward pass, can be used to make models resilient to deterministic (for example, IR drop) or random (for example, read noise) sources of noise and help preserve model accuracy21,57,58."
- [2023_Sun_AIMCvsDIMC_ICCAD](2023_Sun_AIMCvsDIMC_ICCAD.md) AIMC-vs-DIMC (ZigZag-IMC) (2023) — _background_: "Previous review articles focusing on particular aspects of this technology are also available22–28, including those with a primary focus on unit-cell configurations22–24 and"
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _extends/builds-on_: "Hybrid designs combining SRAM and memristive devices may also offer a compelling trade-off between robustness, density and energy efficiency, paving the way for practical and scalable AIMC solutions31,100."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _motivation_: "Consequently, NVM-based AIMC accelerators are predominantly investigated within the context of weight-stationary models that could meet the requirements of edge devices19 and large language model inference20."
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024) — _background_: "Consequently, NVM-based AIMC accelerators are predominantly investigated within the context of weight-stationary models that could meet the requirements of edge devices19 and large language model inference20."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Although some works on SRAM-based IMC have explored floating-point precision of inputs and weights, by handling the exponent and mantissa representations separately using a combination of time, digital and voltage (analogue) domain computing blocks29–31, this requires considerably higher memory capacity and computation energy than the more conventional designs using integer precision31."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)

## Cited by (in collection, 1)
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _background_: "Broadly, AIMC can be categorized based on the underlying memory technology into volatile and nonvolatile approaches [7]."

## Files
- PDF: [../../01_Surveys_and_Foundations/2025_Singh_AIMCTileDesign_NatElectron.pdf](../../01_Surveys_and_Foundations/2025_Singh_AIMCTileDesign_NatElectron.pdf)
- Full text: [../fulltext/2025_Singh_AIMCTileDesign_NatElectron.txt](../fulltext/2025_Singh_AIMCTileDesign_NatElectron.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41928-025-01537-5
