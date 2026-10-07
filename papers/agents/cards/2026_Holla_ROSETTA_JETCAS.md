---
id: W7129625181
key: 2026_Holla_ROSETTA_JETCAS
title: "ROSETTA: ROM-Overlaid STT-MRAM for Efficient MVM and Softmax Operations Toward Accelerating Transformer Inference"
short: "ROSETTA"
year: 2026
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems"
authors: "Amod Holla, Mainakh Mukherjee, Anish Mukherjee, Kaushik Roy"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["MRAM"]
models: ["Transformer", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "macro", "nonlinear-functions", "analog-mvm", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 0
priority_score: 5.0
doi: "https://doi.org/10.1109/jetcas.2026.3665635"
pdf: null
fulltext: null
---

# ROSETTA

**ROSETTA: ROM-Overlaid STT-MRAM for Efficient MVM and Softmax Operations Toward Accelerating Transformer Inference** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2026)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ROSETTA is a 3T-2R STT-MRAM compute-in-memory array using series-resistance sensing with time-to-digital conversion and palindromic input/weight encoding, adding a ROM word line for in-array softmax lookup tables; it reports ~47% less area and 3.1x less MVM energy than an equivalent 8T-SRAM ROM-overlaid macro and 11.7-14.5x energy efficiency over 1T-1R MRAM CiM at the system level.

## Summary
The paper addresses two bottlenecks for transformer inference on compute-in-memory (CiM) hardware: matrix-vector multiplication (MVM) energy efficiency and the non-linear softmax operations that MVM-centric CiM arrays don't natively support. Conventional 1T-1R STT-MRAM CiM has lower MVM energy efficiency than 8T-SRAM CiM due to the low resistance of MRAM devices, with line parasitics and low ON/OFF ratios further limiting row-level parallelism. ROSETTA proposes a CiM array built from 3T-2R STT-MRAM bit-cells using series-resistance sensing and time-to-digital conversion (TDC) for low-power MVM, plus an added word line that stores a ROM bit to enable in-array lookup tables for fast softmax without extra bit-cell area. A novel palindromic encoding of inputs and weights is introduced to counteract the data-dependent nonlinearity inherent to TDC-based STT-MRAM sensing, enabling 8x higher row-level parallelism than standard 1T-1R MRAM CiM and better scalability to larger arrays. The macro-level design is compared against an equivalent ROM-overlaid 8T-SRAM macro and system-level spatial architectures using 1T-1R MRAM and 8T-SRAM ROM-overlaid CiM macros.

## Contributions
- 3T-2R STT-MRAM bit-cell CiM array using series-resistance sensing with time-to-digital conversion (TDC) for low-power MVM
- In-array ROM word line enabling fast softmax lookup tables without added bit-cell area
- Palindromic input/weight encoding scheme that mitigates data-dependent nonlinearity of TDC-based STT-MRAM sensing, enabling 8x higher row-level parallelism than standard 1T-1R MRAM CiM
- System-level spatial architecture evaluation comparing ROSETTA macros against 1T-1R MRAM and 8T-SRAM ROM-overlaid CiM macros

## Key claims (stable IDs)
- **2026_Holla_ROSETTA_JETCAS#C1** — ROSETTA's palindromic encoding enables substantially higher row-level parallelism than standard 1T-1R MRAM CiM — _support:_ 8x higher row-level parallelism than standard 1T-1R MRAM CiM — _loc:_ Abstract
- **2026_Holla_ROSETTA_JETCAS#C2** — ROSETTA macro is more area- and energy-efficient than an equivalent ROM-overlaid 8T-SRAM macro at similar latency/accuracy — _support:_ ~47% less area and 3.1x less MVM energy than an equivalent ROM-overlaid 8T-SRAM macro, at similar latency and accuracy — _loc:_ Abstract
- **2026_Holla_ROSETTA_JETCAS#C3** — At the system level, ROSETTA-based architectures are substantially more energy efficient than equivalent MRAM/SRAM CiM architectures — _support:_ 11.7-14.5x higher energy efficiency vs. 1T-1R MRAM CiM architectures, and 1.44-1.5x vs. 8T-SRAM ROM-overlaid CiM architectures — _loc:_ Abstract

## Results
- ~47% less area than an equivalent ROM-overlaid 8T-SRAM macro
- 3.1x less MVM energy than an equivalent ROM-overlaid 8T-SRAM macro (similar latency/accuracy)
- 8x higher row-level parallelism than standard 1T-1R MRAM CiM
- 11.7-14.5x higher system-level energy efficiency vs. equivalent 1T-1R MRAM CiM architectures
- 1.44-1.5x higher system-level energy efficiency vs. equivalent 8T-SRAM ROM-overlaid CiM architectures

## Limitations
- Full text not accessible to this reviewer (no open preprint found); device-level noise/variation modeling, benchmarked transformer models, and accuracy validation details could not be verified beyond the abstract
- Evidence basis is simulation/macro-design analysis rather than measured silicon

## Remarks
Abstract-only assessment: JETCAS is not downloadable here and no arXiv preprint was found. This is a device/circuit-level contribution (MRAM is comparatively underexplored for CiM relative to ReRAM/PCM/SRAM) that tackles both the MVM-energy weakness of 1T-1R STT-MRAM and the softmax bottleneck for transformers via an in-array ROM table — a nice complement to papers that only address MVM efficiency. The reliance on a time-to-digital conversion scheme introduces data-dependent nonlinearity that the palindromic encoding is designed to counteract; how robust this is in practice (process variation, temperature) cannot be judged without the full paper.

## Cites (in collection, 9)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025)
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025)
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2026_Holla_ROSETTA_JETCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jetcas.2026.3665635
