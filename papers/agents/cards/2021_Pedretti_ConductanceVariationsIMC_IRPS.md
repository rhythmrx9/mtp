---
id: W3157191380
key: 2021_Pedretti_ConductanceVariationsIMC_IRPS
title: "Conductance variations and their impact on the precision of in-memory computing with resistive switching memory (RRAM)"
short: "Conductance Variations IMC"
year: 2021
venue: "IRPS"
venue_full: "2021 IEEE International Reliability Physics Symposium (IRPS 2021)"
authors: "Giacomo Pedretti, Elia Ambrosi, Daniele Ielmini"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: []
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["device-variation", "read-write-noise", "analog-mvm", "endurance-retention"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 6
citations_overall: 36
priority_score: 5.9
doi: "https://doi.org/10.1109/irps46558.2021.9405130"
pdf: null
fulltext: null
---

# Conductance Variations IMC

**Conductance variations and their impact on the precision of in-memory computing with resistive switching memory (RRAM)** — 2021 IEEE International Reliability Physics Symposium (IRPS 2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A reliability-physics perspective on RRAM conductance variation in in-memory computing: characterizes conductance variation/stability and its impact on matrix-vector-multiplication accuracy, then compares mapping strategies (multilevel, binary, unary, redundancy, slicing) for robustness, concluding there is a fundamental accuracy-vs-area tradeoff requiring co-design of precise/stable devices with error-tolerant mapping schemes.

## Summary
The paper examines RRAM reliability from the specific angle of conductance variation and its impact on in-memory computing (IMC) accuracy, given that matrix-vector multiplication (MVM) executed in the analog domain is inherently sensitive to imprecision in the stored conductance weights. Focusing on RRAM as the representative IMC device, the authors describe conductance variation and time-stability behavior and relate it to computation error. They then survey and compare several coefficient-mapping strategies used to represent synaptic weights in RRAM arrays -- multilevel, binary, unary, redundancy, and slicing schemes -- evaluating their robustness to conductance error. The paper's central conclusion is that a tradeoff exists between IMC accuracy and memory array area, implying that accurate IMC circuits require co-design of highly-precise/stable devices together with error-tolerant mapping and computing schemes.

## Contributions
- A characterization of RRAM conductance variation and stability over time and its direct link to MVM computation error in IMC
- A comparative discussion of weight-mapping/coding strategies (multilevel, binary, unary, redundancy, slicing) in terms of their robustness to conductance variation
- Articulation of a general accuracy-vs-area tradeoff principle for IMC circuit design, arguing for co-design across device, mapping, and application levels

## Key claims (stable IDs)
- **2021_Pedretti_ConductanceVariationsIMC_IRPS#C1** — A tradeoff exists between IMC accuracy and memory area occupation, depending on the chosen weight-mapping/coding scheme — _support:_ comparative analysis of multilevel, binary, unary, redundancy and slicing mapping schemes — _loc:_ Abstract
- **2021_Pedretti_ConductanceVariationsIMC_IRPS#C2** — Accurate IMC circuits require co-design of highly precise, highly stable devices together with error-tolerant mapping/computing schemes — _support:_ overall conclusion of the comparative mapping analysis — _loc:_ Abstract / Conclusion

## Limitations
- Full text not available to this review; the quantitative basis for the accuracy-vs-area tradeoff claims and the detail of each mapping scheme's evaluation could not be verified beyond the abstract
- Analysis based only on the abstract; it is unclear whether new experimental/simulation data or only a synthesis of prior results is presented for each mapping scheme
- No specific neural network benchmark or quantitative error/accuracy numbers appear in the abstract

## Remarks
This paper functions as a reliability-physics-oriented overview connecting RRAM conductance variation/stability to the full landscape of weight-mapping strategies used across the crossbar-accelerator literature (multilevel vs. unary vs. redundancy vs. slicing), and is cited by the companion Milo et al. program/verify paper (also in this collection) and later variation-tolerant mapping work. Its value is primarily as a conceptual/comparative framework for the accuracy-area-robustness tradeoff space rather than a single new result; full-text verification was not possible from this environment, so this entry is abstract-only.

## Cites (in collection, 6)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 3)
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _motivation_: "However, partial reset was shown to lead to higher conductance variation compared to gradual set [30], suggesting that combined algorithms based on partial set/reset pulses need further studies."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _data/numbers_: "(b) Measurements in [31]."
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2021_Pedretti_ConductanceVariationsIMC_IRPS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/irps46558.2021.9405130
