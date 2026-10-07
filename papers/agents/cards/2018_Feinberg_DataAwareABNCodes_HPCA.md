---
id: W2795127895
key: 2018_Feinberg_DataAwareABNCodes_HPCA
title: "Making Memristive Neural Network Accelerators Reliable"
short: "Data-aware AN codes (Feinberg)"
year: 2018
venue: "HPCA"
venue_full: "2018 IEEE International Symposium on High Performance Computer Architecture (HPCA 2018)"
authors: "Ben Feinberg, Shibo Wang, Engin İpek"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM", "Memristor(generic)"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["read-write-noise", "stuck-at-faults", "calibration-compensation", "bit-slicing", "peripheral-circuits", "device-variation", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 12
cites_in_collection: 3
citations_overall: 134
priority_score: 7.33
doi: "https://doi.org/10.1109/hpca.2018.00015"
pdf: "../../06_Nonidealities_and_Reliability/2018_Feinberg_DataAwareABNCodes_HPCA.pdf"
fulltext: "../fulltext/2018_Feinberg_DataAwareABNCodes_HPCA.txt"
---

# Data-aware AN codes (Feinberg)

**Making Memristive Neural Network Accelerators Reliable** — 2018 IEEE International Symposium on High Performance Computer Architecture (HPCA 2018) (2018)

## TL;DR
First error-correction scheme for in-situ memristive MVM: data-aware AN (ABN) arithmetic codes correct random-telegraph-noise and stuck-at errors with <4.5% area and <4.7% energy overhead and cut MNIST/AlexNet misclassification by 1.5x and 1.1x.

## Summary
Analog in-situ MVM accelerators (ISAAC, PRIME, PipeLayer, Memristive Boltzmann Machine) use bit slicing over multibit cells but the same electrical properties that give efficiency make them error-prone (resistance noise such as RTN, state-dependent errors, stuck cells); existing memory ECC corrects data before computation, whereas errors here occur during computation. The scheme multiplies operands by an integer A (AN code) so addition survives the distributive property; after the shift-and-add reduction a modulus detects errors and a correction-table lookup repairs them. Naive AN codes are improved by data-aware encoding (ABN) that exploits the observation that physical rows with fewer 1s (low-conductance cells) are less error-prone and by weighting error criticality by bit significance, and uncorrectable errors are handled by zeroing results. The accelerator is an ISAAC-like design with 1-5 bit cells, 128x128 arrays, 16-bit fixed-point weights, 128-bit coded operands and 7-10 check bits. A Monte-Carlo simulator uses an error model from Hu et al. and Ielmini's NiO RTN parameters (dR/R of 2.8% for RLO and 50% for RHI) and a stuck-at term; the error-correction unit is synthesised with FreePDK45 scaled to 32 nm, with CACTI for the table. Workloads are MNIST MLP1, MLP2, CNN1 and a pre-trained AlexNet (evaluated at a single 2-bit cell, 9 check-bit point).

## Contributions
- First error-correction scheme for errors that occur during in-situ analog MVM
- Data-aware AN (ABN) codes using state-dependence of errors and bit-criticality
- Hardware design of a pipelined error-correction unit with correction-table lookup
- Evaluation with RTN and stuck-at faults on MLPs, CNN and AlexNet plus RTN parameter sensitivity

## Key claims (stable IDs)
- **2018_Feinberg_DataAwareABNCodes_HPCA#C1** — Uncorrected analog noise raises MNIST misclassification from 1-2% (software) to 3-4% for MLPs and 2-3% for CNN — _support:_ Fig. 10 — _loc:_ Sec. VIII-A
- **2018_Feinberg_DataAwareABNCodes_HPCA#C2** — ABN codes recover most of the loss, more than half of array-noise-induced errors eliminated with modest check bits — _support:_ ABN-7 to ABN-10; 9-bit code with 4-bit cells comparable accuracy — _loc:_ Sec. VIII-A / Fig. 10
- **2018_Feinberg_DataAwareABNCodes_HPCA#C3** — Overheads are modest — _support:_ ECU 3.4% area per ISAAC tile; total tile area 6.3% (5.3% IC), tile power ECU 2.1% / 5.8% chip-wide; no throughput loss — _loc:_ Sec. VIII-B / Table IV
- **2018_Feinberg_DataAwareABNCodes_HPCA#C4** — AlexNet top-1 misclassification recovered from 48.3% to 43.9% (software 42.96%) — _support:_ Top-5: 21.3% to 20.1% (software 19.74%) — _loc:_ Table (AlexNet accuracy)

## Results
- AlexNet (2-bit cells, ABN-9): top-1 misclassification 42.96% software, 48.3% no ECC, 43.9% ABN-9; top-5 19.74%, 21.3%, 20.1%
- Misclassification reduced 1.5x (MNIST) and 1.1x (ILSVRC-2012) per abstract, with <4.5% area and <4.7% energy overhead
- Accuracy more sensitive to RLO dR/R than to RTN error probability; ABN-10 fully restores accuracy for less aggressive RTN parameters (Fig. 12)

## Key numbers
- tech_node: 32nm (scaled from FreePDK45)
- array_size: 128x128
- energy_eff: <4.7% energy overhead
- throughput: no throughput loss (pipelined ECU)
- accuracy: AlexNet top-1 misclass. 43.9% (ABN-9) vs 48.3% uncorrected, 42.96% software
- bits_weight: 16b fixed point, 1-5 bit cells

## Datasets / benchmarks
MNIST, ILSVRC-2012 (AlexNet)

## Limitations
- Simulation-only with a custom Monte-Carlo error model, no silicon
- Small MNIST models and one AlexNet design point; no large or transformer models
- Error model covers RTN and stuck-at faults, not IR drop, drift or ADC non-linearity
- Correction capability is limited to few errors per codeword; uncorrectable cases are zeroed

## Remarks
Seminal and widely cited (134+ cites) HPCA paper that opened ECC for analog MVM; the data-aware insight (error rate depends on stored value) is reusable. Its detect/correct-after-compute approach costs check bits and table lookups and was evaluated on tiny models, so applicability to billion-parameter language models with outlier activations is unproven, but later LM-on-CiM robustness works in the collection cite it as the starting point for error-correction approaches.

## Cites (in collection, 3)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "This capability has lead to significant interest in implementing the dot product in the analog domain, thereby improving the speed and energy efficiency of prediction with neural networks [1-3, 9-11]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "We evaluate a memristive accelerator similar to ISAAC [9], wherein each layer of the neural network is placed in one or more tiles."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Without loss of generality, we focus on four of these recent proposals in the rest of this paper: 1) the Memristive Boltzmann Machine (MBM) [1], 2) ISAAC [9], 3) PRIME [10], and 4) PipeLayer [11]."

## Cited by (in collection, 12)
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "Possible avenues are improving the memristive device characteristics with respect to variability and conductance noise33, mapping a single column of the matrix to multiple physical columns of an array encoding different bits, and using error-correction techniques within the computational memory unit41."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _motivation_: "Even if none of cells in a bitline is in error, the sum-of-products result read out by the sense amplifier may be incorrect [5] mainly due to (1) the accumulation of read noise from each activated cell in the bitline and (2) the imperfect sense amplifier with limited resolution."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Further, recent research have explored coding schemes for reliable memristor computation at high precision [38, 92]."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Noise and cycle-to-cycle variability in the readout currents of the individual memory elements can cause random errors in a VMM computation, while endurance failures, manufacturing defects, and programming errors can lead to persistent errors.164"
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _contrasts/critiques_: "Error correcting codes can correct a fraction of the dot product errors [19], but the simplest and least costly method of reducing these errors is to proportionally map weights to conductances."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _uses-method-or-tool_: "We convert the change in current to the equivalent conductance change and model these two noise sources using Gaussian distributions [22]"
- [2023_Jang_VECOM_ICCAD](2023_Jang_VECOM_ICCAD.md) VECOM (2023) — _contrasts/critiques_: "There are also studies that use Error Correcting Code (ECC) to increase the variation-tolerability of the ReRAM-based PIM accelerators. [15]-[17] have used ECC such as AN code, Low Density Parity Check (LDPC) or successive error correction to lessen variation in the ReRAM-based PIM."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _data/numbers_: "Simulation results show that the environmental noise contributes less than 5% to the signal level, which is typical for real devices [44]."
- [2024_Qin_RoCR_ICCAD](2024_Qin_RoCR_ICCAD.md) RoCR (2024) — _background_: "Temporal variations are typically independent from device to device and are irrelevant to the value to be programmed [20]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2018_Feinberg_DataAwareABNCodes_HPCA.pdf](../../06_Nonidealities_and_Reliability/2018_Feinberg_DataAwareABNCodes_HPCA.pdf)
- Full text: [../fulltext/2018_Feinberg_DataAwareABNCodes_HPCA.txt](../fulltext/2018_Feinberg_DataAwareABNCodes_HPCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/hpca.2018.00015
