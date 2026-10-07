---
id: W4226111665
key: 2022_Li_40nmMLCRRAMCIMMacro_JSSC
title: "A 40-nm MLC-RRAM Compute-in-Memory Macro With Sparsity Control, On-Chip Write-Verify, and Temperature-Independent ADC References"
short: "40nm MLC-RRAM CIM Macro"
year: 2022
venue: "JSSC"
venue_full: "IEEE Journal of Solid-State Circuits (2022)"
authors: "Wantong Li, Xiaoyu Sun, Shanshi Huang, Hongwu Jiang, Shimeng Yu"
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["macro", "chip-demo", "write-verify-programming", "pruning-sparsity", "adc-dac", "mixed-precision"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 7
citations_overall: 77
priority_score: 8.45
doi: "https://doi.org/10.1109/jssc.2022.3163197"
pdf: null
fulltext: null
---

# 40nm MLC-RRAM CIM Macro

**A 40-nm MLC-RRAM Compute-in-Memory Macro With Sparsity Control, On-Chip Write-Verify, and Temperature-Independent ADC References** — IEEE Journal of Solid-State Circuits (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A fabricated 40-nm RRAM compute-in-memory macro combines multi-level-cell (MLC) RRAM, sparsity-aware input control, on-chip write-verify with periodic drift refresh, and temperature-independent on-chip ADC reference generation, reaching 97.8 GOPS/mm2 and 44.5 TOPS/W on a ternary-weight VGG-8 while sustaining 85.8% CIFAR-10 accuracy at 120 degC.

## Summary
Off-chip write-verify and off-chip ADC reference tuning, common in prior RRAM compute-in-memory (CIM) research chips, are impractical for real deployment, and single-level RRAM cells limit density/throughput. This chip integrates: (1) multi-level-cell (MLC) RRAM for higher density and compute throughput; (2) sparsity-aware input control that exploits high DNN activation sparsity; (3) on-chip write-verify circuitry that both speeds up initial weight programming and periodically refreshes cells to counter resistance drift; and (4) on-chip ADC reference generation with column-wise tunability that remains stable across temperature. Fabricated in TSMC 40-nm embedded-RRAM technology, the macro is evaluated on a VGG-8 network with ternary weights, achieving 97.8 GOPS/mm2 and 44.5 TOPS/W peak MAC performance while maintaining 85.8% CIFAR-10 classification accuracy even at 120 degC.

## Contributions
- Multi-level-cell (MLC) RRAM integration into a compute-in-memory macro for improved density and throughput over single-level-cell designs
- Sparsity-aware input control that leverages high DNN activation sparsity for efficiency gains
- On-chip write-verify circuitry that both accelerates initial weight programming and periodically refreshes cells to compensate resistance drift under stress, removing the need for off-chip write-verify
- On-chip, column-wise tunable ADC reference generation that is stable across a wide temperature range, removing the need for off-chip ADC reference tuning
- Full chip fabrication and measurement in TSMC 40-nm embedded-RRAM technology

## Key claims (stable IDs)
- **2022_Li_40nmMLCRRAMCIMMacro_JSSC#C1** — The macro sustains high classification accuracy even at elevated temperature thanks to on-chip, temperature-independent ADC reference generation and periodic write-verify refresh. — _support:_ 85.8% CIFAR-10 accuracy maintained at 120 degC — _loc:_ Abstract (full text not available)
- **2022_Li_40nmMLCRRAMCIMMacro_JSSC#C2** — The macro achieves high area- and energy-efficiency for MAC operations. — _support:_ 97.8 GOPS/mm2 and 44.5 TOPS/W peak performance on VGG-8 with ternary weights — _loc:_ Abstract (full text not available)

## Results
- 97.8 GOPS/mm2 peak macro-level performance for MAC operations
- 44.5 TOPS/W peak energy efficiency for MAC operations
- 85.8% CIFAR-10 accuracy on a ternary-weight VGG-8 network, maintained at 120 degC
- Fabricated in TSMC 40-nm process with embedded RRAM technology

## Limitations
- Analysis is abstract-only here (full text not accessible from this machine) -- die area/macro size, array dimensions, exact write-verify/refresh timing overhead, and comparison against other fabricated RRAM-CIM macros are not verifiable without the full text
- Reported accuracy/efficiency figures are for a single network (VGG-8, ternary weights) and dataset (CIFAR-10); generality to deeper networks or other precisions is not established from the abstract

## Remarks
A solid, fully fabricated measured-silicon RRAM-CIM macro (category 02) from the Shimeng Yu group addressing two practically important gaps in prior work -- the reliance on off-chip write-verify and off-chip ADC reference tuning -- which matters for any real deployment of RRAM CIM chips rather than lab-bench testing. The 120 degC accuracy-retention result is a notable reliability data point for thermal robustness, directly relevant to non-ideality/reliability questions in this collection; it is cited by several later fabricated-macro and transformer-attention CIM papers (e.g., H3DAtten, ROSETTA) as a representative on-chip-calibrated RRAM CIM baseline.

## Cites (in collection, 7)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)

## Cited by (in collection, 6)
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "Latest ReRAM technology advances in multi-level cell (MLC) design substantially improve the ReRAM density [10]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "For this reason, these approaches have been demonstrated mostly for the weight update of isolated devices, with just a few examples of on-chip integrated approaches."
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)

## Files
- PDF: not available locally (save as `papers/02_Fabricated_Chips_and_Macros/2022_Li_40nmMLCRRAMCIMMacro_JSSC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jssc.2022.3163197
