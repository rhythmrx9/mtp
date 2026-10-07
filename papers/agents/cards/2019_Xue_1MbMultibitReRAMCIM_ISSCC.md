---
id: W2921329602
key: 2019_Xue_1MbMultibitReRAMCIM_ISSCC
title: "24.1 A 1Mb Multibit ReRAM Computing-In-Memory Macro with 14.6ns Parallel MAC Computing Time for CNN Based AI Edge Processors"
short: "1Mb Multibit ReRAM CIM Macro"
year: 2019
venue: "ISSCC"
venue_full: "2019 IEEE International Solid-State Circuits Conference (ISSCC), paper 24.1"
authors: "Cheng-Xin Xue, Wei-Hao Chen, Je-Syu Liu, Jia-Fang Li, Wei‐Yu Lin, Wei-En Lin, Jinghong Wang, Wei-Chen Wei, Ting-Wei Chang, Tung-Cheng Chang, Tsung-Yuan Huang, Hui-Yao Kao et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "peripheral-circuits", "adc-dac", "energy-efficiency", "cnn-accelerator", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 24
cites_in_collection: 1
citations_overall: 293
priority_score: 10.01
doi: "https://doi.org/10.1109/isscc.2019.8662395"
pdf: "../../02_Fabricated_Chips_and_Macros/2019_Xue_1MbMultibitReRAMCIM_ISSCC.pdf"
fulltext: "../fulltext/2019_Xue_1MbMultibitReRAMCIM_ISSCC.txt"
---

# 1Mb Multibit ReRAM CIM Macro

**24.1 A 1Mb Multibit ReRAM Computing-In-Memory Macro with 14.6ns Parallel MAC Computing Time for CNN Based AI Edge Processors** — 2019 IEEE International Solid-State Circuits Conference (ISSCC), paper 24.1 (2019)

## TL;DR
A 55nm 1Mb 1T1R SLC ReRAM CIM macro, the first supporting multibit input/weight/output MAC for CNNs, achieving 14.6 ns tMAC (2b-in, 3b-weight, 4b-out) and 53.17 TOPS/W peak in binary mode.

## Summary
The paper targets the limits of earlier ReRAM CIM macros (1b input, ternary weight, 3b output) by supporting multibit inputs, weights and MAC outputs for higher-accuracy CNNs. Three circuit techniques are proposed: a serial-input non-weighted product (SINWP) structure, a down-scaling weighted current translator (DSWCT) with a positive-negative current subtractor (PN-ISUB), and a triple-margin small-offset current-mode sense amplifier (TMCSA). Weights are mapped to SLC cells: each 3b signed weight (1b sign + 2b data) uses 4 SLC cells in a positive or negative column group (even BL = MSB, odd BL = LSB), and an n x n kernel occupies n^2 consecutive rows. A 2b input is applied as two sequential 1b wordline pulses within one CIM cycle; bitline currents are summed in the array, scaled by a current mirror (reduction ratio p=4), sampled and recombined by SINWP-SC, then the positive/negative paths are subtracted and digitised by TMCSA in 3 sequential phases against 3 reference currents to give a 4b output (3b data + sign). The macro was fabricated in 55nm CMOS and demonstrated with an FPGA host system on CIFAR-10. Measurements give tMAC of 14.6 ns (2b-in, 3b-w, 4b-out, excluding path delay), 11.75 ns in 1b-input mode, 88.52% CIFAR-10 accuracy, and 53.17 / 21.9 TOPS/W in binary / multibit modes. This is a 2-page ISSCC digest, so many quantitative details live in figures not available in the extracted text.

## Contributions
- SINWP structure optimising the area / tMAC / EMAC tradeoff for multibit-input MAC (FoM 1.4-6x better than SIPW and PIPW structures)
- DSWCT + PN-ISUB: current down-scaling and positive/negative subtraction, shortening delay and shrinking the read path; 3.6-3.8x reduction in MAC-value current
- TMCSA: triple-margin, small-offset current-mode sense amplifier tolerating small sensing margin; 6x and 1.7x lower input offset than conventional CSA and DR-CSA
- First fabricated ReRAM CIM macro to support CNN MAC with multibit input/weight/output

## Key claims (stable IDs)
- **2019_Xue_1MbMultibitReRAMCIM_ISSCC#C1** — Lowest ReRAM-CIM MAC access time among existing designs at multibit precision — _support:_ tMAC = 14.6 ns for 2b-IN, 3b-weight, 4b-MAC-OUT — _loc:_ Fig. 24.1.6
- **2019_Xue_1MbMultibitReRAMCIM_ISSCC#C2** — High peak energy efficiency in binary mode — _support:_ 53.17 TOPS/W (1b-IN, 3b-W, 4b-OUT); 21.9 TOPS/W in multibit mode — _loc:_ Fig. 24.1.6
- **2019_Xue_1MbMultibitReRAMCIM_ISSCC#C3** — Improvement over the authors' 2018 macro — _support:_ 3.4x energy efficiency, 1.3x faster tMAC vs [1] — _loc:_ Fig. 24.1.6
- **2019_Xue_1MbMultibitReRAMCIM_ISSCC#C4** — TMCSA triples the effective sensing margin — _support:_ VLQ-LQB proportional to 3*(IIN-IREF)*TPH3 — _loc:_ Fig. 24.1.4

## Results
- tMAC 14.6 ns for 2b-input/3b-weight/4b-output 3x3 kernels; 11.75 ns/cycle at typical VDD for 1b-input/3b-weight (shmoo)
- 88.52% CIFAR-10 inference accuracy in system test with FPGA host (1b input, 3b weight)
- Peak 53.17 TOPS/W (binary) and 21.9 TOPS/W (multibit); 3.4x better efficiency and 1.3x faster tMAC than the 65nm 1Mb macro [1]
- DSWCT reduces worst-case current 3.6x for 3x3 kernels; DSWCT+PN-ISUB give 3.6-3.8x MACV-current reduction
- TMCSA input offset 6x lower than conventional CSA and 1.7x lower than DR-CSA at 70 uA input current

## Key numbers
- tech_node: 55nm
- array_size: 1Mb (1T1R SLC)
- energy_eff: 53.17 TOPS/W binary; 21.9 TOPS/W multibit
- throughput: tMAC 14.6 ns (2b-in, 3b-w, 4b-out)
- accuracy: 88.52% CIFAR-10
- bits_weight: 3b (1b sign + 2b)
- bits_adc: 4b MAC output (TMCSA, 3 phases)

## Datasets / benchmarks
CIFAR-10

## Limitations
- Uses SLC cells only (4 cells per 3b weight), so density is limited; MLC variation avoided rather than solved
- Only 2b input / 3b weight / 4b output, far below typical DNN precision; 88.52% CIFAR-10 is for a small network, network details not given in the digest
- Output sensed with 3 sequential TMCSA phases, adding latency per MAC
- Short digest: tables and figures not captured in extracted text; tMAC excludes path delay

## Remarks
Solid measured-silicon evidence for a digital-output current-mode ReRAM macro; the ISSCC format means little accuracy or network detail. It is the second in the NTHU/TSMC ReRAM CIM lineage, extending the 2018 binary macro and followed by the 22nm 2Mb macro. Its limited precision and small networks mean it is relevant to mapping small CNNs, not language models, onto NVM-CIM, but it illustrates the sense-amplifier and bit-slicing tradeoffs that bound MAC precision.

## Cites (in collection, 1)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _extends/builds-on_: "Previous ReRAM CIM macros demonstrated MAC operations for 1b-input, ternaryweighted, 3b-output CNNs [1] or 1b-input, 8b-weighted, 1b-output fully-connected networks with limited accuracy [2]."

## Cited by (in collection, 24)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _background_: "The latest PIM chips, including the ones based on SRAM [3, 14, 47] and the ones based on RRAM [45], chose to digitize only the most significant bits (MSBs) to reduce the cost of A/D conversion."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "For digitizing the crossbar output, most works have employed analogue-to-digital converters (ADCs)21,22 or sense amplifiers98."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _contrasts/critiques_: "In the SW-2T2R array, the positive weight and negative weight in a differential device pair are connected on the same output column, which is different from Ref. [2] or [3]."
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020) — _motivation_: "Furthermore, according to our observation, the thermal problems get more severe in ReRAM with low cell resolution (1-4bit), which is regarded as a realistic ReRAM compared to ideal ReRAM with high cell resolution (7-8bit) [2, 3, 11, 18]."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "The recent demonstration of embedded RRAM devices at Mbit capacity [8] enables the design and integration of IMC circuits [9]-[11], thus paving the way for energy efficient RRAM-based accelerators of artificial intelligence (AI)."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Among various types of CIM implementation, non-volatile CIM (nvCIM)9-15,23-47 provides the high-density on-chip non-volatile memory (NVM) required to store the neural network (NN) model to eliminate data transfer after power-up; however, it lacks robust accuracy owing to process variation, particularly in MLC operations."
- [2022_Kim_PIMCircuitsOverview_JETCAS](2022_Kim_PIMCircuitsOverview_JETCAS.md) PIM Circuits Overview (2022) — _uses-method-or-tool_: "In general, for PIM architectures based on digital ReRAM, the multiplication of multi-bit inputs and weights can be implemented in two different ways named ‘Parallel-Input-Parallel-Weight (PIPW)’ and ‘Serial-Input-Parallel-Weight (SIPW)’ [42]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "In light of the variability and programmability issues with multibit devices, some recent demonstration of integrated RRAM CIM chips used binary weight storage (LRS and HRS), and partitioned high precision matrix elements to multiple memory cells [180] [181]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2020_Jiang_MINT_ISCAS](2020_Jiang_MINT_ISCAS.md) MINT (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2022_Chen_WRAP_DATE](2022_Chen_WRAP_DATE.md) WRAP (2022)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022)
- [2022_Jiang_ENNA_TCAS-I](2022_Jiang_ENNA_TCAS-I.md) ENNA (2022)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2019_Xue_1MbMultibitReRAMCIM_ISSCC.pdf](../../02_Fabricated_Chips_and_Macros/2019_Xue_1MbMultibitReRAMCIM_ISSCC.pdf)
- Full text: [../fulltext/2019_Xue_1MbMultibitReRAMCIM_ISSCC.txt](../fulltext/2019_Xue_1MbMultibitReRAMCIM_ISSCC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isscc.2019.8662395
