---
id: W3174812964
key: 2021_Huang_IRDropFaultMitigation_JEDS
title: "Efficient and Optimized Methods for Alleviating the Impacts of IR-Drop and Fault in RRAM Based Neural Computing Systems"
short: "IR-Drop Fault Mitigation RRAM"
year: 2021
venue: "JEDS"
venue_full: "IEEE Journal of the Electron Devices Society"
authors: "Chenglong Huang, Nuo Xu, Keni Qiu, Yujie Zhu, Desheng Ma, Liang Fang"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["ir-drop-parasitics", "stuck-at-faults", "peripheral-circuits", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 7
citations_overall: 44
priority_score: 5.06
doi: "https://doi.org/10.1109/jeds.2021.3093478"
pdf: null
fulltext: null
---

# IR-Drop Fault Mitigation RRAM

**Efficient and Optimized Methods for Alleviating the Impacts of IR-Drop and Fault in RRAM Based Neural Computing Systems** — IEEE Journal of the Electron Devices Society (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes two circuit-level mitigation methods -- an additional tunable RRAM row and a trans-impedance-amplifier (TIA) based RRAM scheme -- to recover computation accuracy lost to IR-drop and stuck-at-faults in RRAM crossbar-array DNN accelerators, evaluated via simulation on LeNet-5/MNIST and VGG16/CIFAR-10 across different crossbar sizes and resistance levels.

## Summary
The paper addresses two coupled non-idealities in RRAM crossbar array (RRAM CBA) based DNN accelerators: IR-drop (voltage/current variation along crossbar rows/columns due to wire and device resistance) and stuck-at-faults (SAF), both of which are often ignored during direct weight-to-crossbar mapping but which significantly degrade computation accuracy via multiplication-and-accumulation errors that violate the ideal Kirchhoff's-law-based MAC assumption. The authors propose two optimized methods: (1) adding an extra tunable RRAM row to compensate for output column current variation, and (2) a trans-impedance-amplifier (TIA) based RRAM scheme to reduce variation in output voltage per column. Both methods are evaluated across different RRAM crossbar array sizes and RRAM resistance levels, using LeNet-5 on MNIST and VGG16 on CIFAR-10 as benchmark networks, showing suppressed accuracy degradation from IR-drop and SAF effects.

## Contributions
- Joint consideration of IR-drop and stuck-at-fault (SAF) non-idealities together in RRAM crossbar array DNN accelerator design, rather than treating them in isolation
- An additional-tunable-RRAM-row method to reduce output column current variation caused by IR-drop/SAF
- A trans-impedance-amplifier (TIA) based RRAM scheme to reduce output voltage variation per column
- Evaluation of both methods across varying crossbar array sizes and RRAM resistance levels on two benchmark networks (LeNet-5/MNIST, VGG16/CIFAR-10)

## Key claims (stable IDs)
- **2021_Huang_IRDropFaultMitigation_JEDS#C1** — Direct mapping of DNN weights onto RRAM crossbar arrays without accounting for IR-drop and SAF is unrealistic due to resulting computation-accuracy degradation — _support:_ motivating analysis in the abstract — _loc:_ Abstract
- **2021_Huang_IRDropFaultMitigation_JEDS#C2** — The two proposed optimized methods (tunable RRAM row; TIA-based RRAM) further suppress computing-accuracy degradation induced by IR-drop and SAF — _support:_ simulation results across different crossbar sizes and resistance levels for LeNet-5/MNIST and VGG16/CIFAR-10 — _loc:_ Abstract / simulation results

## Results
- Simulation-based demonstration that both proposed methods reduce accuracy degradation from IR-drop and SAF for LeNet-5 on MNIST and VGG16 on CIFAR-10 across varying crossbar sizes and resistance levels (specific accuracy/overhead percentages not given in the abstract)

## Limitations
- Full text not available to this review (open-access PDF exists only via IEEE Xplore, which is outside this environment's accessible sources); specific quantitative accuracy and hardware-overhead numbers could not be captured beyond the abstract
- Analysis based only on the abstract; the exact circuit overhead (area/energy) of the additional tunable row and TIA-based scheme relative to baseline is unknown from the abstract alone
- Evaluated only on two relatively small/older benchmark networks (LeNet-5, VGG16), not on modern Transformer or large-CNN workloads

## Remarks
This paper addresses IR-drop and stuck-at-fault jointly, which is a useful complement to papers in this set that treat these non-idealities separately (e.g., the unary-coding/variation-aware mapping paper, the Milo et al. program/verify paper). It is cited by at least one later IR-drop-mitigation training paper (Offline Training-Based Mitigation of IR Drop for ReRAM-Based DNN Accelerators) in this collection's forward citations. The paper is gold open access (CC-BY) but hosted only on IEEE Xplore, which per this review's sourcing rules could not be downloaded, so this entry remains abstract-only despite being technically open access.

## Cites (in collection, 7)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 1)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2021_Huang_IRDropFaultMitigation_JEDS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jeds.2021.3093478
