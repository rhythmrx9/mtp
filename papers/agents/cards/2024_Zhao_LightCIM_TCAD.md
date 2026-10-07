---
id: W4401070574
key: 2024_Zhao_LightCIM_TCAD
title: "Light-CIM: A Lightweight ADC/DAC-Fewer RRAM CIM DNN Accelerator With Fully Analog Tiles and Nonideality-Aware Algorithm for Consumer Electronics"
short: "Light-CIM"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)"
authors: "Chenyang Zhao, Jinbei Fang, Jingwen Jiang, Xiaoyong Xue, Xiaoyang Zeng"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["adc-dac", "peripheral-circuits", "hardware-aware-training", "energy-efficiency", "edge-ai"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 9
priority_score: 3.7
doi: "https://doi.org/10.1109/tcad.2024.3435690"
pdf: null
fulltext: null
---

# Light-CIM

**Light-CIM: A Lightweight ADC/DAC-Fewer RRAM CIM DNN Accelerator With Fully Analog Tiles and Nonideality-Aware Algorithm for Consumer Electronics** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024) (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Light-CIM is a lightweight RRAM CIM accelerator built from fully analog tiles (1T1R arrays plus all-analog peripheral circuits) that eliminates most intra-tile ADCs/DACs, cutting ADC power to 2.5% of total, and uses a nonideality-aware training algorithm to recover accuracy, reaching 3.91 TOPS/mm^2 and 3.08 TOPS/W.

## Summary
Most CIM accelerators need numerous ADCs/DACs for mixed-signal data conversion between analog compute and digital control/storage, which costs significant area and energy. Light-CIM instead builds 'fully analog tiles' (FANTs) from 1T1R RRAM arrays plus customized analog peripheral circuits so that intra-tile data computation, transfer, and buffering all stay in the analog domain (voltage, current, or resistance), removing the costly intermediate data conversions used in conventional CIM designs. To recover the accuracy lost to the resulting analog non-idealities (read nonlinearity, device mismatch, variation, noise), the authors use a nonideality-aware training algorithm that models these circuit non-idealities during software training so the deployed network is robust to them. The approach is evaluated on various NN models, reportedly reaching accuracy close to software (floating-point) performance, with ADC power reduced to only 2.5% of total chip power, and a compute density of 3.91 TOPS/mm^2 and energy efficiency of 3.08 TOPS/W, described as highly competitive versus other state-of-the-art CIM designs for consumer-electronics use.

## Contributions
- Fully Analog Tile (FANT) design based on 1T1R RRAM arrays with analog peripheral circuits, eliminating most intra-tile ADC/DAC conversions
- An architecture keeping data computation, transfer and buffering entirely in the analog domain (voltage/current/resistance) within a tile
- A nonideality-aware training algorithm modeling read nonlinearities, mismatches, variations and noise during software training to recover hardware accuracy
- Demonstration that ADC overhead can be cut to a small fraction (2.5%) of total power while retaining near-software accuracy
- A compute-density and energy-efficiency result (3.91 TOPS/mm^2, 3.08 TOPS/W) targeted at consumer-electronics-class CIM accelerators

## Key claims (stable IDs)
- **2024_Zhao_LightCIM_TCAD#C1** — Eliminating intra-tile ADC/DAC conversions via fully analog tiles drastically reduces ADC-related power overhead — _support:_ ADC accounts for only 2.5% of total power consumption (abstract) — _loc:_ Abstract
- **2024_Zhao_LightCIM_TCAD#C2** — Nonideality-aware training recovers accuracy close to ideal software performance despite the fully-analog, non-ideality-prone datapath — _support:_ 'accuracy close to software performance in various NN models' (abstract) — _loc:_ Abstract
- **2024_Zhao_LightCIM_TCAD#C3** — Light-CIM achieves highly competitive compute density and energy efficiency versus other state-of-the-art designs — _support:_ 3.91 TOPS/mm^2 compute density and 3.08 TOPS/W energy efficiency (abstract) — _loc:_ Abstract

## Results
- ADC power is only 2.5% of total power consumption
- Compute density: 3.91 TOPS/mm^2
- Energy efficiency: 3.08 TOPS/W

## Limitations
- Abstract-only analysis in this record: full text unavailable, so the exact analog peripheral-circuit design, training algorithm details, and benchmark models/datasets could not be verified
- Fully-analog intra-tile dataflow (no intermediate ADC/DAC) likely increases sensitivity to accumulated analog noise/drift across cascaded stages; the abstract does not quantify this beyond the single accuracy claim
- Unclear from abstract whether results are from fabricated silicon or simulation only

## Remarks
Light-CIM sits in the same design space as ReCAT/CASCADE-style cascaded-analog approaches that avoid ADC conversion between stages, but applied at the tile/peripheral-circuit level for a lightweight consumer-electronics accelerator rather than for Transformer matrix-matrix chaining. The headline ADC-power-fraction (2.5%) and efficiency numbers are compelling, but without the full text it is not possible to confirm whether these are measured-silicon or simulated results, nor to assess the training algorithm's non-ideality model fidelity.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2024_Zhao_LightCIM_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2024.3435690
