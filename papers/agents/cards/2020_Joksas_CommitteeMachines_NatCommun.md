---
id: W2972862238
key: 2020_Joksas_CommitteeMachines_NatCommun
title: "Committee machines—a universal method to deal with non-idealities in memristor-based neural networks"
short: "Committee Machines"
year: 2020
venue: "NatCommun"
venue_full: "Nature Communications 11, 4273 (2020)"
authors: "D. Joksas, P. Freitas, Z. Chai, W. H. Ng, M. Buckwell, C. Li, W. D. Zhang, Q. Xia, A. J. Kenyon, A. Mehonic"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["device-variation", "stuck-at-faults", "read-write-noise", "ir-drop-parasitics", "calibration-compensation", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 6
citations_overall: 76
priority_score: 5.25
doi: "https://doi.org/10.1038/s41467-020-18098-0"
pdf: "../../06_Nonidealities_and_Reliability/2020_Joksas_CommitteeMachines_NatCommun.pdf"
fulltext: "../fulltext/2020_Joksas_CommitteeMachines_NatCommun.txt"
---

# Committee Machines

**Committee machines—a universal method to deal with non-idealities in memristor-based neural networks** — Nature Communications 11, 4273 (2020) (2020)

## TL;DR
Ensemble-averaging committees of independently trained memristor-based networks, simulated using measured data from three RRAM technologies, recover accuracy lost to faulty devices, D2D variability, RTN and line resistance (e.g. Ta/HfO2: ~91.0% to ~95.7% median with 5 networks) and beat a single larger network with the same total memristor count.

## Summary
Non-idealities (stuck devices, D2D variability, random telegraph noise, line resistance) lower inference accuracy of memristor-based networks. The authors propose committee machines with ensemble averaging (EA): several independently trained networks (different random initialisations, same architecture) are each mapped to separate crossbars and their output vectors averaged, which runs in parallel and so adds no latency. Fully connected nets with one hidden layer (784+1:25+1:10, also 50/100/200 hidden neurons) are trained on MNIST offline, weights are mapped to conductance pairs by a proportional mapping (positive and negative weights in separate bit lines), and are then perturbed with experimental data: array-level pulse-programming data from a 128x64 Ta/HfO2 1T1R array (faulty and range-limited devices, D2D variability), RTN statistics (lognormal fits for 8 resistance states) from a Ta2O5 device and an aVMCO device, and a line-resistance model (0.35/0.32 ohm word/bit line) with weights split over seven 128x64 crossbars for the first layer. Accuracy is evaluated as a function of committee size and, controlling for total memristor count, against larger single networks. Committees consistently raise accuracy, with larger gains for more severe non-idealities and for replacing sufficiently large networks.

## Contributions
- First application of committee machines / ensemble averaging to mitigate memristor non-idealities during inference
- Simulations constrained by experimental data from Ta/HfO2, Ta2O5 and aVMCO RRAMs, covering faults, D2D variability, RTN and line resistance
- Equal-memristor-budget comparison showing committees of small networks outperform one large network
- Argument that modularity allows disabling degraded sub-networks and requires only few extra output neurons and an averaging unit

## Key claims (stable IDs)
- **2020_Joksas_CommitteeMachines_NatCommun#C1** — Committees raise accuracy of non-ideal Ta/HfO2 networks close to digital level — _support:_ individual digital ~95.9%, non-ideal ~91.0%, committee of 5 ~95.7% (median) — _loc:_ Sec. II-B3, Fig. 4
- **2020_Joksas_CommitteeMachines_NatCommun#C2** — Committee of 5 can exceed software baseline for Ta2O5 with RTN — _support:_ individual non-ideal ~94.1%; committee of 5 ~96.5% — _loc:_ Sec. II-C2, Fig. 6
- **2020_Joksas_CommitteeMachines_NatCommun#C3** — At fixed memristor count committees beat larger single networks — _support:_ 2x25 hidden neurons +0.9% vs 1x50; 2x100 +1.1% vs 1x200; 4x50 +1.5% — _loc:_ Sec. III, Fig. 9
- **2020_Joksas_CommitteeMachines_NatCommun#C4** — Method is technology- and non-ideality-agnostic — _support:_ gains across three RRAM types and four non-idealities — _loc:_ Sec. III

## Results
- Line resistance in seven 128x64 Ta/HfO2 crossbars reduces average output current by ~12% (near inputs) to ~16% (far bit lines) (Fig. 3b)
- Ta2O5 device (25-200 kOhm) mapped to only 8 states loses accuracy from mapping alone; RTN effect larger at higher resistance states (Fig. 5)
- Optimising committee weightings numerically gives effectively the same accuracy as plain averaging (Supp. Fig. 5)
- Neuron overhead small: 857 vs 846 neurons for two 25-hidden committees vs one 50-hidden network

## Key numbers
- tech_node: 2 um CMOS (Ta/HfO2 1T1R array)
- array_size: 128x64 (8,192 devices); 7+1 crossbars per 784:25:10 network
- accuracy: Ta/HfO2: 91.0% -> 95.7% median (5 networks); Ta2O5: 94.1% -> 96.5%
- bits_weight: analog conductance (8 states for Ta2O5)

## Datasets / benchmarks
MNIST

## Limitations
- Simulation with experimental distributions; no full committee implemented on hardware
- Only small one-hidden-layer MLPs on MNIST; CNNs and deeper networks only discussed
- RTN data from single devices; line-resistance gain slightly lower for high resistance
- Committee gain depends on individual network accuracy; for small networks and mild non-idealities committees may underperform one network at equal device count
- Extra peripherals and static power of replicated crossbars not quantified; averaging requires multiple output/ADC paths

## Remarks
Simple, hardware-friendly system-level redundancy that is orthogonal to hardware-aware training; the Ta/HfO2 array-level data make the simulations unusually well grounded. The tiny MNIST MLP workload leaves open whether ensembling is affordable for large models, where duplicating weights costs area; for language models it would multiply already large crossbar footprints. Later work in the collection (layer ensemble averaging, nonideality-aware training) builds on it.

## Cites (in collection, 6)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Although here we focus on ex-situ training, such systems have been successfully utilised for in-situ training too [10, 11]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Fortunately, this type of behaviour is more relevant for in-situ training where it is necessary to ensure linear adjustment of ANN's weights [27]."
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _contrasts/critiques_: "To mitigate the effects of these device non-idealities, it is often necessary to modify device structure [9], to use more advanced programming schemes [14] or to use additional circuitry [15] or high-precision processing units [16] in conjunction with memristive elements."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "Memristive devices, such as phase-change memories (PCMs) [6, 7] or resistive random-access memories (RRAMs) [8, 9], have been considered as candidates for such tasks."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "Although here we focus on ex-situ training, such systems have been successfully utilised for in-situ training too [10, 11]."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "These line resistance effects can be partially compensated for algorithmically [17] or partially mitigated by using multiple smaller crossbar arrays [18]."

## Cited by (in collection, 2)
- [2022_Joksas_NonidealityAwareTraining_AdvSci](2022_Joksas_NonidealityAwareTraining_AdvSci.md) Nonideality-Aware Training (2022) — _background_: "In the specific context of MNNs, multiple smaller nonideal networks may replace a large one and increase the accuracy in this way [29]."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _baseline/comparison_: "Contrary to existing related literature26,30 where neural network outputs are obtained by polling outputs of an ensemble of neural networks, not necessarily mapping the same solution, here ensemble outputs are polled at the level of each layer by mapping the same solution multiple times."

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2020_Joksas_CommitteeMachines_NatCommun.pdf](../../06_Nonidealities_and_Reliability/2020_Joksas_CommitteeMachines_NatCommun.pdf)
- Full text: [../fulltext/2020_Joksas_CommitteeMachines_NatCommun.txt](../fulltext/2020_Joksas_CommitteeMachines_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-020-18098-0
