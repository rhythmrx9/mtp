---
id: W4312993714
key: 2022_Jiang_ENNA_TCAS-I
title: "ENNA: An Efficient Neural Network Accelerator Design Based on ADC-Free Compute-In-Memory Subarrays"
short: "ENNA"
year: 2022
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers (2022)"
authors: "Hongwu Jiang, Shanshi Huang, Wantong Li, Shimeng Yu"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["macro", "adc-dac", "chip-demo", "dataflow-pipelining", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 35
priority_score: 4.19
doi: "https://doi.org/10.1109/tcsi.2022.3208755"
pdf: null
fulltext: null
---

# ENNA

**ENNA: An Efficient Neural Network Accelerator Design Based on ADC-Free Compute-In-Memory Subarrays** — IEEE Transactions on Circuits and Systems I: Regular Papers (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ENNA is an ADC-free compute-in-memory accelerator with a taped-out TSMC 40nm RRAM subarray prototype that performs inter-array data processing fully in the analog domain using a pulse-width-modulation input encoding, achieving 73.6-86.4 TOPS/W and 2.3-7 TOPS, with projected 3x-37x throughput gains via heterogeneous 3D integration.

## Summary
The paper targets the ADC bottleneck in compute-in-memory (CIM) accelerators, where analog-to-digital converters that digitize crossbar MAC outputs cause accuracy loss, power overhead, latency penalties, and area cost. ENNA proposes an ADC-free sub-array architecture that keeps inter-array data processing in the analog domain, paired with a lightweight pulse-width-modulation (PWM) input encoding scheme designed to raise throughput. The authors fabricated and taped out a prototype RRAM macro in TSMC 40nm process to validate the ADC-free sub-array design, then used the measured silicon data to project system-level performance for a full accelerator that partitions analog and digital processing at a level above the sub-array. They further project a heterogeneous 3D integration (H3D) variant of the design and compare it to a conventional 2D implementation.

## Contributions
- An ADC-free compute-in-memory sub-array architecture that performs inter-array data processing in the analog domain, avoiding per-sub-array ADC conversion
- A lightweight pulse-width-modulation (PWM) input encoding scheme to improve throughput under the ADC-free design
- A taped-out RRAM prototype macro in TSMC 40nm process validating the ADC-free sub-array concept on measured silicon
- System-level performance projections based on measured silicon data, exploring the analog/digital processing partition point above the sub-array level
- A projected heterogeneous 3D integration (H3D) variant showing further throughput and area benefits over a 2D implementation

## Key claims (stable IDs)
- **2022_Jiang_ENNA_TCAS-I#C1** — The ADC-free sub-array design achieves high energy efficiency validated on measured silicon — _support:_ 73.6-86.4 TOPS/W energy efficiency (normalized to binary operation), based on measured prototype macro data — _loc:_ Abstract
- **2022_Jiang_ENNA_TCAS-I#C2** — The design achieves meaningful throughput across various DNN models — _support:_ 2.3-7 TOPS throughput (normalized to binary operation) tested on various DNN models — _loc:_ Abstract
- **2022_Jiang_ENNA_TCAS-I#C3** — Heterogeneous 3D integration (H3D) substantially improves throughput over a 2D implementation with lower area overhead — _support:_ 3x-37x throughput improvement depending on task, with ~50% reduced area overhead compared to 2D design (projected) — _loc:_ Abstract

## Results
- 73.6-86.4 TOPS/W energy efficiency (normalized to binary operation), from measured TSMC 40nm prototype macro
- 2.3-7 TOPS throughput (normalized to binary operation) across various DNN models
- 3x-37x projected throughput improvement with heterogeneous 3D (H3D) integration vs. 2D design, depending on task
- ~50% projected area overhead reduction with H3D vs. 2D design

## Limitations
- This entry is based on the abstract only (no full text or PDF was located); the exact sub-array ADC-free mechanism, PWM encoding details, and system-level partitioning methodology are not independently verified here
- System-level and H3D performance figures are projections built on measured sub-array/macro data, not a fully fabricated and measured full accelerator or 3D-integrated chip
- Specific DNN models, datasets, and accuracy impact of the ADC-free design are not stated in the abstract

## Remarks
ENNA is notable within the ADC/peripheral-reduction literature (category 09) because it backs its ADC-free claim with a real taped-out RRAM macro rather than pure simulation, which strengthens confidence in the reported TOPS/W and TOPS figures for the sub-array itself. However, the headline H3D throughput and area projections (3x-37x, ~50% area reduction) are extrapolations rather than measurements, and because only the abstract was available here, the accuracy/robustness implications of eliminating ADCs entirely between sub-arrays could not be assessed and should be checked in the full paper.

## Cites (in collection, 6)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2022_Jiang_ENNA_TCAS-I.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcsi.2022.3208755
