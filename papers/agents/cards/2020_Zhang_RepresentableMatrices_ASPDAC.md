---
id: W3013896150
key: 2020_Zhang_RepresentableMatrices_ASPDAC
title: "Representable Matrices: Enabling High Accuracy Analog Computation for Inference of DNNs using Memristors"
short: "Representable Matrices"
year: 2020
venue: "ASP-DAC"
venue_full: "25th Asia and South Pacific Design Automation Conference (ASP-DAC 2020)"
authors: "Baogang Zhang, Necati Uysal, Deliang Fan, Rickard Ewetz"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Memristor(generic)"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["weight-mapping", "ir-drop-parasitics", "write-verify-programming", "tiling-partitioning", "analog-mvm", "adc-dac", "calibration-compensation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 3
citations_overall: 3
priority_score: 3.92
doi: "https://doi.org/10.1109/asp-dac47756.2020.9045101"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2020_Zhang_RepresentableMatrices_ASPDAC.pdf"
fulltext: "../fulltext/2020_Zhang_RepresentableMatrices_ASPDAC.txt"
---

# Representable Matrices

**Representable Matrices: Enabling High Accuracy Analog Computation for Inference of DNNs using Memristors** — 25th Asia and South Pacific Design Automation Conference (ASP-DAC 2020) (2020)

## TL;DR
A five-step crossbar mapping flow jointly optimizes a peripheral scaling factor alpha and memristor conductances/state variables (via Newton's method on non-ideal 1T1M models) to balance IR-drop value-range errors against programming-precision errors, giving 4x-9x smaller MVM error than the dot-product-engine mapping and lifting a 7-layer CNN on CIFAR-10 from 20.5% to 71.8% (software 75.2%).

## Summary
Mapping an arbitrary weight matrix W to a memristor crossbar array (MCA) while accounting for IR-drop, input/output/wire resistance and limited programmable states is hard; the state-of-the-art dot-product-engine mapping (Hu et al., DAC'16) only guarantees correct outputs for the zero vector and one calibration vector and fails on a 7-layer CNN. The authors observe that the conductance matrix G only needs to be proportional to W, with W_r = G/alpha realized by peripheral scaling, and define a space of representable matrices in which the value range (upper bound from IR-drop, lower bound from sneak paths) and precision (distinguishable states) depend on position in the array and on alpha. A small alpha causes precision errors, a large alpha causes IR-drop value-range errors, and total error is near-minimal when the two are equal. The flow (Fig. 5) (1) replaces each non-ideal memristor plus access transistor with an ideal conductance in [gmin,gmax]; (2) iteratively updates alpha by factors (1 +/- beta) until value-range and precision errors balance; (3) sets conductances g by steepest descent minimizing ||W - W_r||_F^2 using Modified Nodal Analysis and then updates the target W_t so ||(W-W_r) v_cal|| = 0; (4) solves Newton's method to obtain device state variables s; (5) closed-loop programming. Evaluation is SPICE-level in MATLAB with 128x128 arrays, 1 ohm wire resistance, 100 ohm input/output resistance, 2 kOhm-3 MOhm conductance range and 8-bit memristor accuracy; DNN weights are partitioned over a grid of 128x128 MCAs (convolution kernel mapping as in PipeLayer).

## Contributions
- Concept of the space of representable matrices and the dependence of value range and precision on array position and scaling factor alpha
- Mapping technique that optimizes alpha, conductances g and state variables s jointly, replacing non-ideal devices with ideal conductors then converting back via Newton's method
- 4x-9x lower MVM error than the dot-product-engine mapping across wire resistance, array size, devices-per-weight and device-model sweeps
- DNN-level validation on MNIST (784x500x300x10 MLP) and a 7-layer CIFAR-10 CNN with DAC/ADC and random telegraph noise studies

## Key claims (stable IDs)
- **2020_Zhang_RepresentableMatrices_ASPDAC#C1** — The mapping gives 4x-9x smaller computational error than Hu et al. [5] — _support:_ Fig. 7 sweeps of wire resistance, size, devices per weight, device models — _loc:_ Abstract, Sec. VI-A, Fig. 7
- **2020_Zhang_RepresentableMatrices_ASPDAC#C2** — CIFAR-10 accuracy of a 7-layer CNN on SPICE-simulated MCAs rises from 20.5% to 71.8% versus 75.2% software accuracy — _support:_ 1000 random test images, 128x128 MCAs, one memristor per weight — _loc:_ Sec. VI-B, Fig. 9b
- **2020_Zhang_RepresentableMatrices_ASPDAC#C3** — MNIST MLP reaches 98.3% (vs 96.3% for [5]) without DAC/ADC quantization; software upper bound 98.4% — _support:_ Fig. 9a — _loc:_ Sec. VI-B
- **2020_Zhang_RepresentableMatrices_ASPDAC#C4** — Accuracy degrades gracefully with up to 20% random telegraph noise — _support:_ Fig. 10a — _loc:_ Sec. VI-B
- **2020_Zhang_RepresentableMatrices_ASPDAC#C5** — Mapping run-time is a limitation: MNIST 6.17 h versus 0.28 h for prior method — _support:_ Fig. 10b table (CIFAR-10 0.93 h vs 0.61 h; FC1 mapped using [5]) — _loc:_ Sec. VI-B

## Results
- MVM error 4x-9x lower than [5]; per-MVM errors 6x smaller as explanation for DNN gain
- CIFAR-10 7-layer CNN: 71.8% (this work) vs 20.5% ([5]) vs 75.2% software
- MNIST 4-layer MLP: 98.3% vs 96.3% vs 98.4% software (no converter quantization)
- Mapping time: CIFAR-10 0.93 h vs 0.61 h; MNIST 6.17 h vs 0.28 h

## Key numbers
- array_size: 128x128 (default); 64x64 in alpha study
- accuracy: 71.8% CIFAR-10 (7-layer CNN) vs 20.5% prior; 98.3% MNIST
- bits_weight: 8b memristor accuracy
- bits_adc: swept (Fig. 9)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Run-time of mapping is high (hours) and implemented in MATLAB; authors plan to reduce it
- Small-scale networks (MLP and 7-layer CNN), arrays of 128x128; FC1 of CNN mapped with the older technique to limit run-time
- Device models limited to Ta2O5 1T1M from prior work; programming modelled as equidistant quantization
- Requires per-array calibration vector and closed-loop programming; no drift or read-noise modelling beyond RTN
- No transformers or language models

## Remarks
A useful reminder that the matrix-to-conductance mapping step alone can account for a 50-point accuracy swing under IR-drop, independent of training. The idea of choosing a per-array scale to balance range versus precision resembles per-column scaling (gamma_i) and learned input ranges in later HWA training work (Rasch et al.), though here it is analytic and per-matrix. Run-time and the SPICE-level setting restrict it to small crossbars; for large language-model matrices tiled over hundreds of arrays the approach would need fast approximations.

## Cites (in collection, 3)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Moreover, the use of MCAs allow matrices to be stored inplace, which reduces data fetching and communication costs that fundamentally bounds the performance of any computing system that processes large amounts of data [8, 2, 9]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Moreover, the use of MCAs allow matrices to be stored in-place, which reduces data fetching and communication costs that fundamentally bounds the performance of any computing system that processes large amounts of data [8, 2, 9]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Moreover, the use of MCAs allow matrices to be stored in-place, which reduces data fetching and communication costs that fundamentally bounds the performance of any computing system that processes large amounts of data [8, 2, 9]."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2020_Zhang_RepresentableMatrices_ASPDAC.pdf](../../05_Mapping_Compilation_and_Dataflow/2020_Zhang_RepresentableMatrices_ASPDAC.pdf)
- Full text: [../fulltext/2020_Zhang_RepresentableMatrices_ASPDAC.txt](../fulltext/2020_Zhang_RepresentableMatrices_ASPDAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/asp-dac47756.2020.9045101
