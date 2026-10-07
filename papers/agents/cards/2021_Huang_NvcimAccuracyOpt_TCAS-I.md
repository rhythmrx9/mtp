---
id: W3215634441
key: 2021_Huang_NvcimAccuracyOpt_TCAS-I
title: "Accuracy Optimization With the Framework of Non-Volatile Computing-In-Memory Systems"
short: "nvCIM Accuracy Opt"
year: 2021
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers"
authors: "Yuxuan Huang, Yifan He, Jinshan Yue, Huazhong Yang, Yongpan Liu"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["adc-dac", "quantization", "hardware-aware-training", "device-variation", "read-write-noise"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 10
priority_score: 3.23
doi: "https://doi.org/10.1109/tcsi.2021.3124553"
pdf: null
fulltext: null
---

# nvCIM Accuracy Opt

**Accuracy Optimization With the Framework of Non-Volatile Computing-In-Memory Systems** — IEEE Transactions on Circuits and Systems I: Regular Papers (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes the nvCIM framework for systematically analyzing how RRAM device, array, and ADC parameters affect DNN classification accuracy in computing-in-memory systems, and introduces circuit-level fixes (a program-verify RRAM programming scheme, a margin-enhanced sense amplifier, and an offset-reduction ADC) that reach 112.1 TOPS/W macro-level energy efficiency with under 3.51% accuracy loss versus an ideal baseline.

## Summary
The paper addresses the accuracy-loss problem in non-volatile RRAM-based computing-in-memory (nvCIM) systems, noting that prior work has mostly optimized computing performance while neglecting systematic accuracy analysis. It proposes the nvCIM framework to analyze the relationship between DNN classification accuracy and key analog factors (RRAM device characteristics, crossbar array properties, and ADC parameters). Building on this analysis, it proposes concrete optimizations: an adaptive voltage-controlled SET / pulse-controlled RESET (VSPR) program-verify scheme to achieve higher-resolution RRAM states, a margin-enhancement current-mode sense amplifier (MECSA), and an offset-reduction ADC (ORADC) to improve the fidelity of analog read-out. Experimental (simulation/design) results report macro-level energy efficiency of 112.1 TOPS/W and system-level 9.86 TOPS/W, with less than 3.51% accuracy loss relative to an ideal (non-degraded) baseline, which the authors state is 2.9x-25.9x more energy efficient than existing RRAM-based nvCIM accelerators.

## Contributions
- The nvCIM framework for systematically relating DNN classification accuracy to analog design factors (device, array, ADC) in RRAM-based computing-in-memory systems
- An adaptive voltage-controlled SET / pulse-controlled RESET (VSPR) program-verify scheme for higher-resolution RRAM cell programming
- A margin-enhancement current-mode sense amplifier (MECSA) to improve read-out accuracy
- An offset-reduction ADC (ORADC) design to reduce analog-to-digital conversion error
- System/macro-level energy efficiency and accuracy evaluation showing improvement over existing RRAM nvCIM accelerators

## Key claims (stable IDs)
- **2021_Huang_NvcimAccuracyOpt_TCAS-I#C1** — The proposed nvCIM optimizations achieve high energy efficiency with small accuracy loss relative to an ideal baseline — _support:_ Macro-level energy efficiency of 112.1 TOPS/W and system-level 9.86 TOPS/W with less than 3.51% accuracy loss vs. ideal — _loc:_ Abstract
- **2021_Huang_NvcimAccuracyOpt_TCAS-I#C2** — The proposed design is substantially more energy-efficient than existing RRAM-based nvCIM accelerators — _support:_ 2.9x-25.9x improvement in energy efficiency compared to existing RRAM-based nvCIM accelerators (abstract-level figure) — _loc:_ Abstract

## Results
- Macro-level energy efficiency: 112.1 TOPS/W
- System-level energy efficiency: 9.86 TOPS/W
- Accuracy loss: less than 3.51% versus the ideal (non-degraded) baseline
- 2.9x-25.9x energy-efficiency improvement over existing RRAM-based nvCIM accelerators (abstract-level comparison)

## Limitations
- Only the abstract was available for this analysis (paper is paywalled, no open-access copy found); circuit implementation details, benchmark networks/datasets, and the precise baseline accuracy could not be verified from the full text
- Reported efficiency numbers appear to be from design/simulation rather than confirmed fabricated-silicon measurement (unclear from abstract alone)
- No information on which DNN models/datasets were used to obtain the 3.51% accuracy-loss figure

## Remarks
Abstract-only analysis: this paper sits alongside other peripheral-circuit-and-accuracy-co-design work (TinyADC, Neural-PIM, On the Accuracy of Analog NN Inference Accelerators) in treating ADC/sense-amplifier/programming-scheme design as central levers for closing the accuracy gap in RRAM CIM systems, rather than relying purely on noise-aware retraining. Because no full text was accessible, the specific experimental methodology and the generality of the reported TOPS/W and accuracy-loss numbers could not be independently verified.

## Cites (in collection, 10)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2021_Huang_NvcimAccuracyOpt_TCAS-I.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcsi.2021.3124553
