---
id: W4379527483
key: 2023_Ye_WH2T1RRRAMCIM_JSSC
title: "A 28-nm RRAM Computing-in-Memory Macro Using Weighted Hybrid 2T1R Cell Array and Reference Subtracting Sense Amplifier for AI Edge Inference"
short: "WH-2T1R RRAM CIM Macro"
year: 2023
venue: "JSSC"
venue_full: "IEEE Journal of Solid-State Circuits"
authors: "Wang Ye, Linfang Wang, Zhidao Zhou, Junjie An, Weizeng Li, Hanghang Gao, Zhi Li, Jinshan Yue, Hongyang Hu, Xiaoxin Xu, Jianguo Yang, Jing Liu et al."
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["macro", "chip-demo", "weight-mapping", "adc-dac", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 8
citations_overall: 61
priority_score: 6.76
doi: "https://doi.org/10.1109/jssc.2023.3280357"
pdf: null
fulltext: null
---

# WH-2T1R RRAM CIM Macro

**A 28-nm RRAM Computing-in-Memory Macro Using Weighted Hybrid 2T1R Cell Array and Reference Subtracting Sense Amplifier for AI Edge Inference** — IEEE Journal of Solid-State Circuits (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A 28nm 2T1R RRAM compute-in-memory macro with a weighted hybrid cell array, redundant-sub-array MSB mapping, and a reference-subtracting current sense amplifier achieves 30.34-154.04 TOPS/W silicon-measured MAC efficiency and improves ResNet-18 CIFAR accuracy via its MSB scheme.

## Summary
The paper targets limitations of non-volatile compute-in-memory (nvCIM) macros: restricted input parallelism from parasitics, signal-margin loss from device non-idealities, and costly analog readout circuitry. It proposes a 2T1R RRAM macro with four elements: a macro architecture that decouples the memory and computing data paths; a weighted hybrid 2T1R (WH-2T1R) cell array; a redundant sub-array mapping scheme for the most-significant bit (RSM-MSB) to protect the MSB against variation; and a reference-subtracting current sense amplifier (RS-CSA) to improve readout margin. A test chip was fabricated in a 28nm HKMG logic process with foundry RRAM and silicon-verified, performing linear analog MAC over 32 accumulation channels with 1-bit input, 3-bit weight, 4-bit output. The chip achieves 30.34-154.04 TOPS/W. Using the chip's measured behavior/mapping scheme in evaluation with a ResNet-18 model, the RSM-MSB scheme improves CIFAR-10 and CIFAR-100 inference accuracy by 0.96% and 2.83%, respectively, versus a baseline without the MSB-protection scheme.

## Contributions
- A macro architecture with decoupled memory and computing datapaths to reduce parasitic/IR-drop related degradation of input parallelism
- A weighted hybrid 2T1R (WH-2T1R) cell array design for in-memory MAC
- A redundant sub-array MSB mapping scheme (RSM-MSB) that protects the most significant weight bit from device variation, improving downstream inference accuracy
- A reference-subtracting current sense amplifier (RS-CSA) to improve analog readout margin at lower hardware cost
- Silicon-verified 28nm test chip reporting 30.34-154.04 TOPS/W and quantified ResNet-18 CIFAR-10/100 accuracy gains from the MSB scheme

## Key claims (stable IDs)
- **2023_Ye_WH2T1RRRAMCIM_JSSC#C1** — The 28nm 2T1R RRAM CIM macro achieves 30.34-154.04 TOPS/W energy efficiency — _support:_ 30.34-154.04 TOPS/W reported for 1-bit input, 3-bit weight, 4-bit output over 32 accumulation channels — _loc:_ Abstract
- **2023_Ye_WH2T1RRRAMCIM_JSSC#C2** — The RSM-MSB scheme improves ResNet-18 inference accuracy on CIFAR-10 and CIFAR-100 — _support:_ 0.96% accuracy improvement on CIFAR-10 and 2.83% on CIFAR-100 — _loc:_ Abstract / Evaluation

## Results
- 30.34-154.04 TOPS/W measured energy efficiency (1-bit IN, 3-bit W, 4-bit O, 32 accumulation channels)
- 0.96% ResNet-18/CIFAR-10 accuracy improvement from RSM-MSB scheme
- 2.83% ResNet-18/CIFAR-100 accuracy improvement from RSM-MSB scheme

## Limitations
- Analysis based on abstract only (no full text available to this reviewer); architectural/circuit details (array size, ADC precision chain, area, throughput, comparison baselines) could not be independently verified
- ResNet-18 accuracy results appear to be evaluated via simulation/emulation of the mapping scheme using measured device characteristics rather than full end-to-end silicon inference of the whole network (unconfirmed without full text)

## Remarks
This is a measured-silicon compute-in-memory macro paper reporting strong energy efficiency (up to 154 TOPS/W) for low-precision (1b/3b/4b) MAC, with its main mapping-relevant contribution being the RSM-MSB redundancy scheme that specifically protects the most-significant weight bit from RRAM variability — a concrete, quantified instance of bit-significance-aware mapping for crossbar accuracy. Because only the abstract was available, the claimed efficiency numbers and accuracy deltas should be treated as reported headline figures pending verification against the full paper; no numbers beyond the abstract are given here.

## Cites (in collection, 8)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)

## Cited by (in collection, 1)
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026)

## Files
- PDF: not available locally (save as `papers/02_Fabricated_Chips_and_Macros/2023_Ye_WH2T1RRRAMCIM_JSSC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jssc.2023.3280357
