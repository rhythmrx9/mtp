---
id: W4312949026
key: 2022_Shanbhag_IMCBenchmarking_OJSSCS
title: "Benchmarking In-Memory Computing Architectures"
short: "IMC-Benchmarking"
year: 2022
venue: "OJSSCS"
venue_full: "IEEE Open Journal of the Solid-State Circuits Society (2022)"
authors: "Naresh R. Shanbhag, Saion K. Roy"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-analog", "Generic-NVM"]
models: []
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["benchmarking", "energy-efficiency", "macro"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 3
citations_overall: 48
priority_score: 6.28
doi: "https://doi.org/10.1109/ojsscs.2022.3210152"
pdf: null
fulltext: null
---

# IMC-Benchmarking

**Benchmarking In-Memory Computing Architectures** — IEEE Open Journal of the Solid-State Circuits Society (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes a compositional benchmarking methodology and metric set for in-memory-computing (IMC) chips, then applies it to a database of more than 70 published IMC ICs since 2018 to show SRAM-based IMCs beat digital accelerators at the bank level but the gap shrinks at the processor level, eNVM-based IMCs lag both SRAM-IMCs and digital accelerators in compute density, and compute accuracy is widely under-reported.

## Summary
The paper observes that reported IMC energy-efficiency gains appear to be plateauing, but the field lacks a rigorous, consistent way to benchmark designs and identify bottlenecks. It proposes: (1) a compositional view that decomposes an IMC design into canonical components; (2) a set of standardized benchmarking metrics covering performance, energy efficiency, and compute accuracy; and (3) a strategy for analyzing reported data against these metrics. Applying this methodology to an extensive database of metrics extracted from over 70 published IMC IC designs since 2018, the authors find that SRAM-based IMCs have a clear energy-efficiency and compute-density advantage over digital accelerators at the bank level, but that advantage shrinks substantially at the full-processor level; that embedded-NVM (eNVM)-based IMCs lag SRAM-based IMCs in both energy efficiency and compute density, and even lag plain digital accelerators in compute density; and that bank-level compute accuracy -- despite being a critical metric -- and the inherent energy-vs-accuracy trade-off of IMC are rarely reported in the literature.

## Contributions
- A compositional framework that decomposes IMC architectures into canonical building-block components for apples-to-apples comparison
- A set of standardized benchmarking metrics for IMC performance, energy efficiency, and compute accuracy
- An analysis strategy applied to a database of metrics extracted from 70+ published IMC chips since 2018
- Identification of a bank-to-processor-level efficiency gap for SRAM-based IMCs, and of eNVM-based IMCs lagging both SRAM-IMCs and digital accelerators in compute density
- A call-out that compute accuracy and the energy-vs-accuracy trade-off are systematically under-reported in IMC publications

## Key claims (stable IDs)
- **2022_Shanbhag_IMCBenchmarking_OJSSCS#C1** — SRAM-based IMCs show a clear energy-efficiency and compute-density advantage over digital accelerators at the bank level, but this advantage shrinks dramatically at the processor level — _support:_ stated as a benchmarking finding across the >70-design database — _loc:_ Abstract
- **2022_Shanbhag_IMCBenchmarking_OJSSCS#C2** — eNVM-based IMCs lag SRAM-based IMCs in both energy efficiency and compute density — _support:_ stated finding from the benchmarking database — _loc:_ Abstract
- **2022_Shanbhag_IMCBenchmarking_OJSSCS#C3** — eNVM-based IMCs surprisingly lag digital accelerators in compute density — _support:_ stated finding from the benchmarking database — _loc:_ Abstract
- **2022_Shanbhag_IMCBenchmarking_OJSSCS#C4** — Bank-level compute accuracy, despite being a critical IMC metric, is pervasively neglected in publications, as is the energy-vs-accuracy trade-off — _support:_ stated as a benchmarking observation across the surveyed design database — _loc:_ Abstract

## Results
- Benchmarking database built from more than 70 published IMC IC designs since 2018
- SRAM-IMC vs. digital-accelerator energy-efficiency/compute-density gap found to be large at the bank level but much smaller at the processor level (magnitude not given in abstract)
- eNVM-based IMCs found to lag both SRAM-IMCs and digital accelerators in compute density (magnitude not given in abstract)

## Limitations
- Analysis is only as good as the self-reported metrics in the surveyed publications, many of which (per the paper's own finding) omit compute accuracy and energy-accuracy trade-off data
- This entry is based on the abstract only (no full text or PDF was located); specific benchmarking metric definitions, the full device/architecture breakdown, and exact quantitative gaps are not confirmed here
- Cross-paper comparison of chips built in different process nodes and measurement conditions carries inherent benchmarking caveats typical of literature meta-analyses

## Remarks
A methodology/meta-analysis paper rather than a new device or accelerator design; its value for a thesis on analog/IMC hardware is primarily as a critical, cross-cutting reference for what is and is not reported in the IMC chip literature, and its finding that eNVM-based IMCs lag both SRAM-IMCs and digital accelerators in compute density is a useful counterpoint to many individual eNVM/ReRAM/PCM papers that emphasize energy efficiency without equally emphasizing compute density or accuracy. Because only the abstract was available, the magnitude of the reported gaps and the precise definition of the proposed metrics could not be verified here and should be checked against the full text before citing specific numbers.

## Cites (in collection, 3)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)

## Cited by (in collection, 4)
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Previous review articles focusing on particular aspects of this technology are also available22–28, including those with a primary focus on unit-cell configurations22–24 and"
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _background_: "Recently, numerous researchers are exploring Compute-In-Memory (CIM) approaches [6, 7, 8] to increase energy-efficiency by performing Multiply-Accumuate (MAC) operations within ON-chip memory “Tiles,” thus markedly reducing the motion of model-weights and partial sums."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _background_: "Recently, numerous researchers are exploring Compute-In-Memory (CIM) approaches [7, 8, 9] to increase energy-efficiency by performing Multiply-Accumuate (MAC) operations within ON-chip memory “Tiles,” to greatly reduce the motion of model-weights and partial sums."
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2022_Shanbhag_IMCBenchmarking_OJSSCS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/ojsscs.2022.3210152
