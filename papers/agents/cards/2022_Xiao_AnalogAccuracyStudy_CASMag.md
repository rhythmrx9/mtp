---
id: W3198899759
key: 2022_Xiao_AnalogAccuracyStudy_CASMag
title: "On the Accuracy of Analog Neural Network Inference Accelerators"
short: "Analog Accuracy Study"
year: 2022
venue: "CASMag"
venue_full: "IEEE Circuits and Systems Magazine"
authors: "T. Patrick Xiao, Ben Feinberg, Christopher H. Bennett, Venkatraman Prabhakar, Prashant Saxena, Vineet Suresh Agrawal, Sapan Agarwal, Matthew J. Marinella"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["Flash", "ReRAM", "PCM", "Generic-NVM"]
models: ["CNN", "ResNet", "VGG", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["analog-mvm", "weight-mapping", "bit-slicing", "adc-dac", "device-variation", "ir-drop-parasitics", "quantization", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 18
citations_overall: 72
priority_score: 6.63
doi: "https://doi.org/10.1109/mcas.2022.3214409"
pdf: "../../06_Nonidealities_and_Reliability/2022_Xiao_AnalogAccuracyStudy_CASMag.pdf"
fulltext: "../fulltext/2022_Xiao_AnalogAccuracyStudy_CASMag.txt"
---

# Analog Accuracy Study

**On the Accuracy of Analog Neural Network Inference Accelerators** — IEEE Circuits and Systems Magazine (2022)

## TL;DR
A systematic simulation study on ResNet50/ImageNet shows that making analog quantities proportional to weight/dot-product values (differential cells, high On/Off, analog subtraction) gives most of the error resilience, bit slicing adds little accuracy at large energy/area cost, and a SONOS-based core loses only 2.17% ImageNet accuracy with direct weight transfer.

## Summary
Prior in-situ analog accelerators (ISAAC, PUMA, CASCADE, etc.) assume bit slicing and a 'full precision guarantee' (ADC resolves every possible MVM output) are needed for accuracy, but rarely evaluate end-to-end accuracy. The authors build an accuracy model of in-situ MVM at individual-MAC resolution that includes cell programming error (state-independent vs state-proportional), ADC quantization and array parasitic resistance, and evaluate ResNet50-v1.5 (plus Inception-v3, VGG-19, MobileNet-v1) on ImageNet with 8-bit weights/activations and direct weight transfer (no retraining). Weights are mapped to conductances either proportionally (differential cell pairs with analog current subtraction, high On/Off) or by offset subtraction, with or without bit slicing, and with ADC limits calibrated per design. They argue that dot-product error depends on the absolute conductance spread, not on state separation, so bit slicing is not a fundamental accuracy advantage, and that proportional mapping exploits the zero-peaked weight distribution to lower mean conductance and thus both programming and IR-drop errors. A case study uses characterized SONOS charge-trap flash arrays (40nm process energy/area estimates) to compare five core designs (A-E) in accuracy, energy and area. Design A (7 bits/cell, 1152 rows, differential, analog input-bit accumulation) is the most efficient at 8.4 fJ/op and 0.24 mm2, versus 902 fJ/op and 11.14 mm2 for offset-subtraction Design E.

## Contributions
- Reframes bit slicing and the 'full precision guarantee' as unnecessary for DNN inference accuracy, backed by end-to-end ImageNet evaluation rather than MVM-level precision proxies
- Identifies proportional mapping (weight and dot-product proportionality) as the key design principle for error resilience, requiring differential cells, high On/Off ratio and analog subtraction
- Quantifies sensitivity to cell programming error, ADC resolution and parasitic resistance across design choices (bits/cell, rows per MVM, differential vs offset)
- SONOS case study with measured cell error distributions showing energy, area and accuracy trade-offs for five core designs

## Key claims (stable IDs)
- **2022_Xiao_AnalogAccuracyStudy_CASMag#C1** — Bit slicing gives only a small accuracy benefit for the same device conductance precision and cannot rescue highly error-prone cells — _support:_ dot-product error <dI_j>^2 = N<dI_ij>^2 depends on absolute conductance spread, not state separation — _loc:_ Sec. 3.1, Sec. 5
- **2022_Xiao_AnalogAccuracyStudy_CASMag#C2** — Proportional mapping with differential cells lets the ADC resolution be set by the network (~8 bits) rather than by the full-precision guarantee — _support:_ differential cells tolerate low-resolution ADC; offset subtraction needs 8-bit ADC at only 72 rows — _loc:_ Sec. 3.2.2, Sec. 6
- **2022_Xiao_AnalogAccuracyStudy_CASMag#C3** — Direct weight transfer onto SONOS cells costs 2.17% ImageNet accuracy on ResNet50-v1.5, reduced to 0.86% with 4-bit QAT — _support:_ Design A: 74.296% vs 76.082% ideal cells; 75.294% with QAT — _loc:_ Table 5, Sec. 9.3
- **2022_Xiao_AnalogAccuracyStudy_CASMag#C4** — Offset-subtraction Design E uses 107x more energy and 46x more area than differential Design A and is far less accurate with SONOS errors — _support:_ Table 3: 902.0 vs 8.4 fJ/op; 11.14 vs 0.24 mm2; Table 4: 50.2% vs 74.0% — _loc:_ Tables 3-4, Sec. 9.3

## Results
- Design A (differential, 7b/cell, 1152 rows): 8.4 fJ/op, 0.24 mm2; Design B (1b slices) 63.1 fJ/op, 2.02 mm2; Design C (144 rows) 43.3 fJ/op; Design D 25.8 fJ/op; Design E (offset, 2b/cell, 72 rows) 902 fJ/op, 11.14 mm2 (Table 3)
- ResNet50-v1.5 on 1000 images with SONOS errors: A 74.0%, B 75.4%, C 73.6%, D 74.1%, E 50.2%+-5.3% (ideal cells 74.9-76.3%) (Table 4)
- Full 50k ImageNet: fully digital 76.466%, Design A ideal 76.082%, Design A SONOS 74.296%+-0.348%, with 4-bit QAT 75.294%+-0.192% (Table 5)
- PCM in Joshi et al. loses 7.8% ImageNet accuracy on ResNet34, attributed to state-independent error vs SONOS state-proportional error
- Analog input-bit accumulation gives 2-4x energy improvement and cuts ADC conversions 8x (Sec. 9.3)

## Key numbers
- tech_node: 40nm (SONOS embedded process, estimates)
- array_size: 1152 rows (Design A), 72-1152 rows swept
- energy_eff: 8.4 fJ/op (Design A)
- accuracy: 74.296% ImageNet top-1 (ResNet50-v1.5, SONOS, Design A); 76.466% digital
- bits_weight: 8b (7 bits/cell)
- bits_adc: 8b

## Datasets / benchmarks
ImageNet, MLPerf Inference ResNet50-v1.5, Inception-v3, VGG-19, MobileNet-v1

## Limitations
- Simulation only; SONOS error model comes from characterized arrays but no full-system silicon
- Vision CNNs only (ResNet50, Inception-v3, VGG-19, MobileNet-v1); no transformers or language models
- Analog subtraction and analog accumulation circuit costs are modeled, not fabricated
- Design E parasitic-resistance accuracy likely lower than reported in Table 4
- Focus on direct weight transfer; drift, read noise temporal effects and retraining are not deeply explored

## Remarks
A rigorous, widely cited end-to-end accuracy study whose main takeaway (proportional mapping, no mandatory bit slicing, ADC sized by the algorithm) directly critiques ISAAC/PUMA/CASCADE-style designs in this collection. Evidence is simulation with a realistic device model, which is stronger than abstract noise injection but still CNN-only. For mapping language models, its argument about zero-peaked weight distributions and proportional errors is relevant, though transformer outliers and activation dynamic range may change the ADC conclusions.

## Cites (in collection, 18)
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _background_: "Within an array, individual analog MACs can also be conducted at a lower energy, higher density, and greater parallelism than digital MACs [45]."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _contrasts/critiques_: "Error correcting codes can correct a fraction of the dot product errors [19], but the simplest and least costly method of reducing these errors is to proportionally map weights to conductances."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _contrasts/critiques_: "This can be achieved by using smaller arrays [43, 66], but this is inefficient as it amortizes the ADC energy cost over fewer MACs."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "Recent work has optimized the performance and energy of bit-sliced accelerators [6, 14, 42, 49], but rarely evaluates the effect of system-level design decisions on inference accuracy."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _background_: "A common approach is to add noise to weights and activations during forward propagation [28, 32, 34, 36, 44]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "To avoid the energy and area overheads of reading, digitizing and aggregating multiple bit-sliced arrays, the magnitude of a weight can also be fully encoded in one device [30, 34]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _contrasts/critiques_: "Recent work has optimized the performance and energy of bit-sliced accelerators [6, 14, 42, 49], but rarely evaluates the effect of system-level design decisions on inference accuracy."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _data/numbers_: "Some other ReRAM devices have properties that are closer to state-independent error [46, 67]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "In situ MVM has been demonstrated using a wide variety of memory cell technologies [55, 61, 68]."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _background_: "It is well known that parasitic resistance degrades MVM accuracy and some compensation methods have been proposed [30,32,33,71]."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Pruning is more difficult to exploit in analog accelerators, due to the rigid structure of a memory crossbar [62]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _contrasts/critiques_: "Recent work has optimized the performance and energy of bit-sliced accelerators [6, 14, 42, 49], but rarely evaluates the effect of system-level design decisions on inference accuracy."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _baseline/comparison_: "Comparison of data representation in selected prior work on analog in situ inference accelerators (Table 1), listing FORMS alongside ISAAC, PUMA, PRIME and others by bit-slicing, sign handling, array size and ADC/DAC bits."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _background_: "In situ MVM has been demonstrated using a wide variety of memory cell technologies [55, 61, 68]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "In bit slicing, the bit representation of each matrix element is divided into multiple slices, and the results of bit sliced MVMs are combined via shift-and-add (S&A) reduction [9, 21, 56]."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 5)
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _uses-method-or-tool_: "ISAAC's encoding strategy relies on an analog circuit that sums crossbar inputs [54]. This component has been shown to degrade accuracy under noise [73], so we replace it with a digital equivalent."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _data/numbers_: "ADCs with at least 8-bit resolution are necessary to achieve high (>90%) classification accuracy in a ResNET50-1.5 ANN used to classify the ImageNET database."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "2) Representation: How data values appear is determined by how the hardware represents operands [47]."
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)
- [2026_Sharma_HatFi_VTS](2026_Sharma_HatFi_VTS.md) HATFI (2026)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2022_Xiao_AnalogAccuracyStudy_CASMag.pdf](../../06_Nonidealities_and_Reliability/2022_Xiao_AnalogAccuracyStudy_CASMag.pdf)
- Full text: [../fulltext/2022_Xiao_AnalogAccuracyStudy_CASMag.txt](../fulltext/2022_Xiao_AnalogAccuracyStudy_CASMag.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/mcas.2022.3214409
