---
id: W4417052206
key: 2025_Li_HARMONY_TCAD
title: "HARMONY: A Hardware-Aware Mapping and Optimizing Framework for Computing-in-Memory Accelerators"
short: "HARMONY"
year: 2025
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025, early access)"
authors: "Xinmo Li, Weidong Yang, Naifeng Jing, Qin Wang, Zhigang Mao, Weiguang Sheng"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM"]
models: ["DNN (unspecified)"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["compiler-software-stack", "weight-mapping", "dataflow-pipelining", "nas-codesign"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 12
citations_overall: 0
priority_score: 4.5
doi: "https://doi.org/10.1109/tcad.2025.3641044"
pdf: null
fulltext: null
---

# HARMONY

**HARMONY: A Hardware-Aware Mapping and Optimizing Framework for Computing-in-Memory Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025, early access) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
HARMONY is a CIM compiler built on a hardware IR unifying compute and memory abstractions; it automatically identifies CIM-offloadable operators, builds a hybrid SW/HW IR and uses reinforcement learning to search a joint space of general-purpose and CIM-specific scheduling primitives.

## Summary
Model and hardware diversity make CIM accelerators hard to exploit, and existing approaches rely on manual mapping or limited automation that does not combine general-purpose compiler optimisations with CIM-specific features. HARMONY introduces a hardware intermediate representation that unifies computational and memory abstractions. An automatic mapping algorithm identifies operators that can be offloaded to CIM and constructs a hybrid software-hardware IR, which lets general-purpose and CIM-specific scheduling primitives coexist in one search space. The space is explored with reinforcement learning. Evaluations report support for a broader set of operators than existing CIM compilers and consistent performance and energy improvements across diverse DNN workloads.

## Contributions
- Hardware IR unifying computational and memory abstractions of CIM accelerators
- Automatic offloadable-operator identification and hybrid SW-HW IR construction
- Unified search space combining general-purpose and CIM-specific scheduling primitives
- RL-based exploration of the scheduling space

## Key claims (stable IDs)
- **2025_Li_HARMONY_TCAD#C1** — HARMONY supports a broader set of operators than existing CIM compilers. — _support:_ Stated in abstract; no operator counts given — _loc:_ Abstract
- **2025_Li_HARMONY_TCAD#C2** — HARMONY consistently improves performance and energy across diverse DNN workloads. — _support:_ Stated qualitatively in abstract — _loc:_ Abstract

## Results
- Performance and energy improvements over existing CIM compilers across diverse DNN workloads (magnitudes not available from abstract)

## Limitations
- Abstract-only analysis; no quantitative results, target architectures or baselines verified
- RL search cost/compile time not characterised in abstract
- Likely evaluated with simulators/cost models rather than silicon
- Accuracy effects of analog non-idealities presumably out of scope

## Remarks
Positions itself against PIMCOMP, OCC and polyhedral CIM compilers by merging TVM-like general scheduling with CIM-specific primitives; the hybrid IR idea (deciding what runs on CIM vs. digital units) is important for transformer-style models with many non-MVM ops. Without the full text, the size of the gains and the realism of the hardware model cannot be assessed.

## Cites (in collection, 12)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021)
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023)
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2025_Li_HARMONY_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2025.3641044
