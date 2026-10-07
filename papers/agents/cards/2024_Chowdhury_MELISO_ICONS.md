---
id: W4404915602
key: 2024_Chowdhury_MELISO_ICONS
title: "The Lynchpin of In-Memory Computing: A Benchmarking Framework for Vector-Matrix Multiplication in RRAMs"
short: "MELISO"
year: 2024
venue: "ICONS"
venue_full: "International Conference on Neuromorphic Systems (ICONS 2024)"
authors: "Md Tawsif Rahman Chowdhury, Huynh Quang Nguyen Vo, Paritosh Ramanan, Murat Yildirim, Gözde Tütüncüoğlu"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM"]
models: ["Other"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "benchmarking", "analog-mvm", "device-variation", "read-write-noise", "bit-slicing"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 3
priority_score: 3.92
doi: "https://doi.org/10.1109/icons62911.2024.00058"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2024_Chowdhury_MELISO_ICONS.pdf"
fulltext: "../fulltext/2024_Chowdhury_MELISO_ICONS.txt"
---

# MELISO

**The Lynchpin of In-Memory Computing: A Benchmarking Framework for Vector-Matrix Multiplication in RRAMs** — International Conference on Neuromorphic Systems (ICONS 2024) (2024)

## TL;DR
MELISO is a Python/Cython wrapper over MLP+NeuroSim that benchmarks error propagation in RRAM vector-matrix multiplication across four device chemistries (Ag:a-Si, TaOx/HfOx, AlOx/HfO2, EpiRAM) and fits parametric error distributions; EpiRAM (largest memory window, lowest non-linearity and C-to-C) gives the smallest VMM error.

## Summary
The paper argues that analog VMM error propagation caused by device non-idealities needs characterising independently of any network. MELISO (In-Memory Linear Solver) has a forward stage where matrices and vectors defined in Python are given device type, crossbar dimension and tolerances via MelisoPy and a Cython wrapper to the C++ MLP+NeuroSim engine, which encodes parameters, maps them to conductances and computes the crossbar VMM; a backward stage scales and transforms the output, collects statistics and performance information. Experiments use populations of 1000 random 32x32 matrices times 1000 random 32x1 vectors on 32x32 crossbars, comparing each result with the software dot product and concatenating 32,000 error terms per device. Ag:a-Si (modified to memory window 100, C-to-C and non-linearity off) is the model system for single-factor sweeps of weight bits (1 to 11 bits, up to 2048 states), memory window, weight-update non-linearity (0 to 5) and C-to-C variation (0% to 5%), with and without non-linearity. A comparison of four literature devices (Table I) is then run with and without non-idealities, and error distributions are fitted (Johnson Su, normal mixtures, SHASH) with skewness and kurtosis reported.

## Contributions
- MELISO: end-to-end VMM benchmarking framework for RRAM built on MLP+NeuroSim
- Systematic study of memory window, weight bits, non-linearity and C-to-C variation on VMM error magnitude and variance
- Benchmark of four state-of-the-art device chemistries with fitted heavy-tailed error distributions to guide error models for algorithm design

## Key claims (stable IDs)
- **2024_Chowdhury_MELISO_ICONS#C1** — VMM error and variance fall as weight bits increase (1 to 11 bits) and as memory window grows beyond 12.5 — _support:_ Error magnitude and variance decrease monotonically in the ideal setting — _loc:_ Fig. 2
- **2024_Chowdhury_MELISO_ICONS#C2** — Weight-update non-linearity and C-to-C variation substantially increase error; variance grows roughly exponentially with non-linearity — _support:_ Non-linearity swept 0-5, C-to-C 0-5%; even baseline 3.5% C-to-C gives substantial error — _loc:_ Figs. 3-4
- **2024_Chowdhury_MELISO_ICONS#C3** — EpiRAM performs best, AlOx/HfO2 worst, VMM errors are non-Gaussian — _support:_ EpiRAM MW 50.2, non-linearity 0.5/-0.5, C-to-C 2%; errors fit Johnson Su, normal mixtures or SHASH with skew and heavy tails — _loc:_ Fig. 5 / Table II

## Results
- Device metrics (Table I): Ag:a-Si 97 states, MW 12.5, NL 2.4/-4.88, C-to-C 3.5%; TaOx/HfOx 128, MW 10, 0.04/-0.63, 3.7%; AlOx/HfO2 40, MW 4.43, 1.94/-0.61, 5%; EpiRAM 64, MW 50.2, 0.5/-0.5, 2%
- With non-idealities, EpiRAM remains best and Ag:a-Si and TaOx/HfOx are similar, both better than AlOx/HfO2 (Fig. 5b)
- AlOx/HfO2 has the highest error variance; non-idealities slightly reduce its outlier span (Fig. 5)
- Error distributions are asymmetric and heavy-tailed, not normal (Table II)

## Key numbers
- array_size: 32x32
- bits_weight: 1-11 bits (up to 2048 conductance states)

## Datasets / benchmarks
random 32x32 VMM populations (1000 matrices x 1000 vectors)

## Limitations
- Random 32x32 matrices and vectors only; no neural network accuracy or LM workloads
- Inherits NeuroSim's exponential non-linear weight encoding; Ag:a-Si modified (memory window 100) for sweeps
- No wire resistance/IR drop, drift, ADC non-idealities or large array scaling studied
- Device parameters taken from literature, not measured; small paper (workshop-length)

## Remarks
Useful but narrow benchmarking study; it isolates which device metrics dominate VMM error and shows errors are heavy-tailed, which argues against simple Gaussian noise injection used in many hardware-aware training papers (including those for LMs). Lacks system-level or model-level evaluation, so its link to language models is only through error-model assumptions. Compare with NeuroSim and AIHWKit-style simulators in the collection.

## Cites (in collection, 6)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _motivation_: "As RRAMs critically suffer from device nonidealities, most prominently non-linear conductance tuning, C-to-C, and device-to-device variations, benchmarking frameworks need to incorporate these key issues [23, 24]."
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020) — _background_: "Extensive literature exists on benchmarking frameworks designed to evaluate RRAM device performance and integration with CMOS peripheral circuitry for a variety of computational tasks such as image classification with fully connected and convolutional neural networks [19-21], as well as dot product engines [22]."
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021) — _background_: "This mechanism underscores the computational efficiency inherent in the RRAM crossbar design for implementing VMM operations, with improved energy efficiency and reduced latency metrics [8-16]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Emerging non-volatile memory technologies, such as resistive random access memories (RRAMs) based crossbar arrays, provide a versatile solution to the challenges of data-intensive, large-scale computational tasks [6, 7]."
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023) — _background_: "This mechanism underscores the computational efficiency inherent in the RRAM crossbar design for implementing VMM operations, with improved energy efficiency and reduced latency metrics [8-16]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Emerging non-volatile memory technologies, such as resistive random access memories (RRAMs) based crossbar arrays, provide a versatile solution to the challenges of data-intensive, large-scale computational tasks [6, 7]."

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2024_Chowdhury_MELISO_ICONS.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2024_Chowdhury_MELISO_ICONS.pdf)
- Full text: [../fulltext/2024_Chowdhury_MELISO_ICONS.txt](../fulltext/2024_Chowdhury_MELISO_ICONS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/icons62911.2024.00058
