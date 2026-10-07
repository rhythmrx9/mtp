---
id: W3211973280
key: 2021_Nikam_PassiveRRAMLSTM_TED
title: "Long Short-Term Memory Implementation Exploiting Passive RRAM Crossbar Array"
short: "Passive RRAM LSTM"
year: 2021
venue: "TED"
venue_full: "IEEE Transactions on Electron Devices, vol. 69 (2022; published online Dec. 2021)"
authors: "Honey Nikam, Siddharth Satyam, Shubham Sahay"
category: "10 On-chip & Analog Training"
devices: ["ReRAM"]
models: ["LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["on-chip-training", "recurrent-models", "analog-mvm", "device-variation", "read-write-noise", "energy-efficiency", "3d-integration", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 21
priority_score: 2.94
doi: "https://doi.org/10.1109/ted.2021.3133197"
pdf: "../../10_On_Chip_and_Analog_Training/2021_Nikam_PassiveRRAMLSTM_TED.pdf"
fulltext: "../fulltext/2021_Nikam_PassiveRRAMLSTM_TED.txt"
---

# Passive RRAM LSTM

**Long Short-Term Memory Implementation Exploiting Passive RRAM Crossbar Array** — IEEE Transactions on Electron Devices, vol. 69 (2022; published online Dec. 2021) (2021)

## TL;DR
Simulation of in-situ Manhattan-rule training of a small LSTM on a selector-less (passive) 64x64 Pt/Al2O3/TiO2-x RRAM crossbar reports ~6.5x10^3 smaller footprint (921.6 um2 vs 6.041 mm2) and ~51.7x lower update energy than a 1T-1R memristor LSTM, with training energy of 3.0 uJ over 200 epochs.

## Summary
The paper argues that active 1T-1R arrays carry large area overhead and proposes implementing LSTM vector-matrix multiplications and in-situ backprop training on a passive RRAM crossbar. A hardware-aware simulator uses an experimentally calibrated phenomenological compact model (Nili et al., validated against >2 million data points from 324 devices) for the Pt/Al2O3/TiO2-x/Ti/Pt stack, including static noise, dynamic conductance change dependent on current state (non-linearity), device-to-device and temporal variations. A 64x64 passive crossbar is partitioned into a 34x60 array for the LSTM layer (four gates, weights as differential conductance pairs W = G+ - G-, conductance limited to 100-300 uS) and a 32x1 array for the dense output layer. Forward and backward VMMs happen in the array; the desired weight change is computed digitally with SGD+momentum (alpha 0.01, momentum 0.9, conductance-to-weight ratio 1e-4) and applied as a single fixed-amplitude pulse (+/-0.8 V) according to its sign (Manhattan rule); tanh/sigmoid are digital. The task is airline-passenger next-month regression (144 monthly points, 96 train / 48 test). Training energy is computed per pulse from V^2*G*t_p and area from cell pitch.

## Contributions
- First proposal of LSTM VMM plus in-situ training on a passive (selector-less) RRAM crossbar
- Hardware-aware simulation framework using a calibrated compact model with variation, noise and non-linearity
- Comparison with digital and active 1T-1R LSTM implementations in convergence, area and training energy

## Key claims (stable IDs)
- **2021_Nikam_PassiveRRAMLSTM_TED#C1** — Passive-crossbar LSTM footprint is ~6.5x10^3 smaller than the active 1T-1R implementation — _support:_ 921.6 um2 (40x64, 0.36 um2/cell) vs ~6.041 mm2 (2360 um2/cell) — _loc:_ Sec. III-C
- **2021_Nikam_PassiveRRAMLSTM_TED#C2** — Training energy is much lower than the 1T-1R design — _support:_ ~51.7x lower; 3.0 uJ with variation/noise vs 2.8 uJ ideal for 200 epochs — _loc:_ Sec. III-B / Figs. 11-12
- **2021_Nikam_PassiveRRAMLSTM_TED#C3** — The passive-crossbar LSTM converges faster and is robust to variation, noise and non-linearity — _support:_ converges within 200 epochs, predictions follow test data more closely than software and 1T-1R versions — _loc:_ Sec. III-A / Figs. 5, 9, 10

## Results
- Area: 921.6 um2 vs 6.041 mm2 for a 40x64 array (about 6.5x10^3 smaller)
- Training energy to convergence: 3.0 uJ (non-ideal) vs 2.8 uJ (ideal) in 200 epochs; ~51.7x lower than active 1T-1R
- Cell footprint 0.36 um2 (0.6x0.6 um) vs ~2360 um2 for the 1T-1R cell of the prior LSTM work
- Faster convergence than 1T-1R implementation (Fig. 5)

## Key numbers
- array_size: 64x64 passive (34x60 LSTM + 32x1 dense)
- energy_eff: 3.0 uJ training energy over 200 epochs
- bits_weight: analog conductance 100-300 uS

## Datasets / benchmarks
International airline passengers (1949-1960)

## Limitations
- Simulation only; no fabricated LSTM array
- Tiny task (airline passengers regression, 144 samples) and one small LSTM layer
- Comparison with 1T-1R uses a large-cell prior work (2360 um2 cell) which inflates the area ratio, and the 1T-1R energy is estimated with simplified assumptions
- Sneak paths, IR drop and peripheral/ADC/DAC energy and area not included; training energy covers only conductance updates
- Not a language model despite motivational mention of language modelling

## Remarks
A proof-of-concept that passive crossbars can in principle host recurrent-network in-situ training. The headline gains come mostly from comparing a selector-less minimum-pitch cell against a large 1T-1R cell and from excluding peripherals, so they should not be read as system-level results. Its relevance to language models is limited to the idea of recurrent/sequential workloads and dense passive arrays with 3D stacking for capacity.

## Cites (in collection, 6)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2021_Nikam_PassiveRRAMLSTM_TED.pdf](../../10_On_Chip_and_Analog_Training/2021_Nikam_PassiveRRAMLSTM_TED.pdf)
- Full text: [../fulltext/2021_Nikam_PassiveRRAMLSTM_TED.txt](../fulltext/2021_Nikam_PassiveRRAMLSTM_TED.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/ted.2021.3133197
