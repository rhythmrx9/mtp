---
id: W4416429527
key: 2025_Mai_CIMWise_ICCAD
title: "CIMWise: An IREE-based End-To-End AI Compiler with Auto-Tuning for CIM Processors"
short: "CIMWise"
year: 2025
venue: "ICCAD"
venue_full: "2025 IEEE/ACM International Conference on Computer Aided Design (ICCAD 2025)"
authors: "Bo Mai, Jin Wang, Zhen Zhai, Liang Zhang, Yufu Zhang, Longyang Lin"
category: "05 Mapping, Compilation & Dataflow"
devices: ["None"]
models: ["DNN (unspecified)"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["compiler-software-stack", "dataflow-pipelining", "scheduling", "nas-codesign"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 1
priority_score: 5.31
doi: "https://doi.org/10.1109/iccad66269.2025.11240989"
pdf: null
fulltext: null
---

# CIMWise

**CIMWise: An IREE-based End-To-End AI Compiler with Auto-Tuning for CIM Processors** — 2025 IEEE/ACM International Conference on Computer Aided Design (ICCAD 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
CIMWise is an IREE/MLIR-based end-to-end compiler for CIM processors whose auto-tuner searches hardware parameters and dataflow characteristics with a two-stage simulated annealing over an analytical cost model, reporting up to 58% lower energy and 19% lower latency than prior CIM compilers, validated with hardware measurements.

## Summary
Existing CIM compilers mostly parametrise hardware (array size, number of CIM units, buffer capacity) but ignore that different CIM architectures have different dataflow patterns (CIM parallelism, scheduling, buffer allocation). CIMWise builds on IREE: IREE's frontend performs graph-level optimisation and a custom backend performs operator-level optimisation. At its core is an auto-tuning framework with a search space covering both hardware parameters and dataflow characteristics, an analytical cost model with an adaptable on-chip memory model, and a two-stage simulated annealing search to find scheduling strategies per workload. The approach is validated through actual hardware measurements and achieves up to 58% energy reduction and 19% latency reduction over prior CIM compilers.

## Contributions
- IREE-based end-to-end compilation flow for CIM processors (graph-level via IREE frontend, operator-level via custom backend)
- Search space that includes dataflow characteristics in addition to hardware parameters
- Analytical cost model with adaptable on-chip memory model
- Two-stage simulated annealing auto-tuner; validation via hardware measurements

## Key claims (stable IDs)
- **2025_Mai_CIMWise_ICCAD#C1** — Prior CIM compilers neglect dataflow-pattern diversity across CIM architectures. — _support:_ Motivation stated in abstract — _loc:_ Abstract
- **2025_Mai_CIMWise_ICCAD#C2** — CIMWise reduces energy and latency relative to prior CIM compilers. — _support:_ 'up to a 58% reduction in energy consumption and a 19% decrease in latency compared to prior CIM compilers' — _loc:_ Abstract
- **2025_Mai_CIMWise_ICCAD#C3** — The compiler's results are validated on real hardware. — _support:_ 'validated through actual hardware measurements' — _loc:_ Abstract

## Results
- Up to 58% energy reduction vs. prior CIM compilers (abstract)
- Up to 19% latency reduction vs. prior CIM compilers (abstract)

## Limitations
- Abstract-only analysis; target CIM processor, its memory technology (analog vs. digital, SRAM vs. NVM), workloads and baseline compilers not verified
- 'Up to' figures are best cases
- Analytical cost model accuracy relative to hardware not quantified in abstract
- Device type left as 'None' (device-agnostic compiler) because the abstract does not specify it

## Remarks
Notable mainly for integrating CIM compilation into a mainstream MLIR stack (IREE) rather than a bespoke toolchain, and for claiming hardware-measured validation, which most CIM compilers (PIMCOMP, CIM-MLC, polyhedral flows) lack. The energy gains come from scheduling/buffer decisions rather than analog circuit changes, so they are likely orthogonal to non-ideality and ADC work.

## Cites (in collection, 7)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020)
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021)
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2025_Mai_CIMWise_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccad66269.2025.11240989
