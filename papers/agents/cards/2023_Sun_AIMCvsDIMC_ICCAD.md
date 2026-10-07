---
id: W4389166767
key: 2023_Sun_AIMCvsDIMC_ICCAD
title: "Analog or Digital In-Memory Computing? Benchmarking Through Quantitative Modeling"
short: "AIMC-vs-DIMC (ZigZag-IMC)"
year: 2023
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2023)"
authors: "Jiacong Sun, Pouya Houshmand, Marian Verhelst"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-analog", "SRAM-digital"]
models: ["CNN", "MobileNet", "ResNet", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["benchmarking", "simulator", "adc-dac", "macro", "energy-efficiency", "dataflow-pipelining", "peripheral-circuits", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 4
cites_in_collection: 3
citations_overall: 33
priority_score: 8.66
doi: "https://doi.org/10.1109/iccad57390.2023.10323763"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2023_Sun_AIMCvsDIMC_ICCAD.pdf"
fulltext: "../fulltext/2023_Sun_AIMCvsDIMC_ICCAD.txt"
---

# AIMC-vs-DIMC (ZigZag-IMC)

**Analog or Digital In-Memory Computing? Benchmarking Through Quantitative Modeling** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2023) (2023)

## TL;DR
A silicon-validated analytical cost model for SRAM-based analog (AIMC) and digital (DIMC) in-memory macros, integrated into ZigZag, shows DIMC has higher compute density while large AIMC macros can be more energy efficient on conv/pointwise layers and small DIMC wins on depthwise layers.

## Summary
Published IMC designs differ in architecture, array size and technology and are typically compared by peak macro TOP/s/W. The paper builds a unified analytical model of IMC macros described by dimensions (Di rows, Do columns, Bw bits per weight, M cells per input), with per-component cost models: IMC cell array (CACTI-based RC model), registers, SAR ADC (area/delay/energy with fitted parameters for 28nm), DAC, adder trees (DIMC) and input/output logic. The model is validated against published 22-28nm AIMC chips ([2]-[4], max 11% energy mismatch except one chip with unreported sparsity; area mismatch from repeaters, 4.5x) and DIMC designs. It is integrated into ZigZag (zigzag-imc, open source) with a single macro (M=1), 256 KB on-chip cache, INT8, zero sparsity, weight-stationary dataflow, and benchmarked on macro-level peak and system-level performance across array sizes (32x32 to 1024x1024) and on MLPerf Tiny models (ResNet8, MobileNet, DS-CNN, AutoEncoder).

## Contributions
- Unified analytical performance model for AIMC and DIMC validated against several published designs
- Macro-level and system-level peak performance benchmarking across array sizes
- Workload-level (MLPerf Tiny) evaluation showing peak metrics mispredict effective efficiency
- Open-source ZigZag-IMC framework

## Key claims (stable IDs)
- **2023_Sun_AIMCvsDIMC_ICCAD#C1** — AIMC peak energy efficiency improves by an order of magnitude from 32x32 to 1024x1024 arrays as ADC/DAC cost is amortized, but higher-resolution ADCs reduce throughput and TOP/s/mm2 — _support:_ Fig. 7-8 — _loc:_ Sec. V-A
- **2023_Sun_AIMCvsDIMC_ICCAD#C2** — DIMC with array <=64x64 beats AIMC in TOP/s/W; for larger arrays AIMC wins; DIMC consistently has higher computational density — _support:_ Fig. 7 — _loc:_ Sec. V-A
- **2023_Sun_AIMCvsDIMC_ICCAD#C3** — System energy efficiency is at least 2x below macro efficiency for 32x32 arrays — _support:_ system vs macro peak — _loc:_ Sec. V-A / Fig. 8
- **2023_Sun_AIMCvsDIMC_ICCAD#C4** — Conv and pointwise layers are best suited to IMC; depthwise and FC layers are poorly suited (weight reload, limited unrolling) — _support:_ layer-level energy breakdown — _loc:_ Sec. V-B / Figs. 10-11
- **2023_Sun_AIMCvsDIMC_ICCAD#C5** — On MLPerf Tiny DIMC has higher average TOP/s/mm2 while system energy efficiency is similar to AIMC — _support:_ geometric mean across 4 models — _loc:_ Fig. 12

## Results
- Energy validation vs AIMC chips: max mismatch 11% (except one chip with unreported sparsity)
- Reported chip efficiency examples 7.3 fJ/MAC and 102.6 fJ/MAC on validation plot
- ResNet8 (all conv) achieves TOP/s/W closest to peak; FC-heavy AutoEncoder suffers weight reloading; MobileNet and DS-CNN under-utilize large macros
- Optimal array size per layer is the first point where in/out spatial unrolling ratio saturates

## Key numbers
- tech_node: 28nm (calibrated); validated 22-28nm
- array_size: 32x32 to 1024x1024 swept
- accuracy: max 11% energy mismatch vs published AIMC chips
- bits_weight: INT8
- bits_adc: SAR ADC, resolution scales with array size

## Datasets / benchmarks
MLPerf Tiny (ResNet8, MobileNet, DS-CNN, AutoEncoder)

## Limitations
- SRAM-based IMC only; no NVM (PCM/ReRAM) device models or non-idealities
- Sparsity not modeled; INT8 only
- Single macro with fixed 256 KB cache; no multi-macro tiling
- Validated on 22-28nm designs; model calibrated for 28nm
- CNN/MLPerf Tiny workloads only, no transformers or LMs

## Remarks
Important methodological caution that peak TOP/s/W is a poor predictor of workload performance; FC-heavy layers (the dominant shape in transformers/LMs) are exactly the ones this study finds weight-reload-bound for IMC. Not about NVM or noise, so use alongside CiMLoop and NeuroSim for energy and AIHWKit-type tools for accuracy.

## Use in the original review
- F8 (High confidence): ADC/DAC conversion is a first-order cost and it creates a scaling trap: up to 58% of energy and 81% of area, energy exponential in precision; AIMC only beats DIMC once that overhead is amortized over a large array, but larger arrays force higher-resolution ADCs that degrade throughput and computational density.

## Cites (in collection, 3)
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _contrasts/critiques_: "Similarly, for mapping space explorations, most of the focus has been dedicated to AIMC designs, while lacking DIMC assessment [18, 19, 22, 23]."
- [2022_GarciaRedondo_SACA_DCIS](2022_GarciaRedondo_SACA_DCIS.md) SACA (2022) — _contrasts/critiques_: "Published models however primarily focus on AIMC designs [1, 15–21], while there is a lack of DIMC modeling efforts."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _contrasts/critiques_: "Similarly, for mapping space explorations, most of the focus has been dedicated to AIMC designs, while lacking DIMC assessment [18, 19, 22, 23]."

## Cited by (in collection, 4)
- [2025_Zhang_ASiM_TVLSI](2025_Zhang_ASiM_TVLSI.md) ASiM (2025) — _background_: "Among CiM architectures, Analog Compute-in-Memory (ACiM) offers high computational density and energy efficiency by leveraging the analog properties of memory cells to perform Multiply-and-ACcumulate (MAC) operations directly in the analog domain [4]."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Previous review articles focusing on particular aspects of this technology are also available22–28, including those with a primary focus on unit-cell configurations22–24 and"
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _contrasts/critiques_: "Sun et al. [76] is a contemporaneous work that combines a parameterizable CiM macro model with a flexible architectural specification [77]."
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2023_Sun_AIMCvsDIMC_ICCAD.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2023_Sun_AIMCvsDIMC_ICCAD.pdf)
- Full text: [../fulltext/2023_Sun_AIMCvsDIMC_ICCAD.txt](../fulltext/2023_Sun_AIMCvsDIMC_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccad57390.2023.10323763
