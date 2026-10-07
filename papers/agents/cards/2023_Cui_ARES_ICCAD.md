---
id: W4389166698
key: 2023_Cui_ARES_ICCAD
title: "ARES: A Mapping Framework of DNNs Towards Diverse PIMs with General Abstractions"
short: "ARES"
year: 2023
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2023)"
authors: "Xiuping Cui, Size Zheng, Tianyu Jia, Le Ye, Yun Liang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["compiler-software-stack", "weight-mapping", "cnn-accelerator", "dataflow-pipelining"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 4
citations_overall: 3
priority_score: 5.32
doi: "https://doi.org/10.1109/iccad57390.2023.10323777"
pdf: null
fulltext: null
---

# ARES

**ARES: A Mapping Framework of DNNs Towards Diverse PIMs with General Abstractions** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2023) (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ARES is a general mapping framework for deploying DNNs on diverse processing-in-memory (PIM) architectures using a hardware-abstraction and mapping-space-search approach, reported to give up to 70% speedup on single operators and 50% on whole networks versus prior mapping methods.

## Summary
The paper targets the fragmentation problem in PIM mapping tools: existing DNN-to-PIM mapping approaches are hand-tailored to a specific accelerator architecture and do not generalize across the diversity of PIM memory types, compute functions, and memory-mapping constraints seen across recent designs (e.g., ReRAM crossbar accelerators like PipeLayer, PUMA, ISAAC, PRIME). ARES introduces a hardware abstraction that represents DNN computation on PIM as a tensorized compute function together with data-layout constraints imposed by the memory array, and uses this abstraction to build a unified mapping space spanning both compute and memory constraints. The framework then explores this mapping space to automatically derive efficient, architecture-specific mapping strategies without requiring per-architecture hand engineering. The authors evaluate ARES across four distinct PIM hardware configurations and compare against state-of-the-art mapping methods, reporting speed improvements for both individual operator mapping and full-network mapping.

## Contributions
- Proposes a general hardware abstraction for PIM architectures expressing DNN computation as a tensorized compute function plus array data-layout constraints
- Builds a unified mapping space covering both compute scheduling and memory/array placement constraints from this abstraction
- Provides a mapping-space exploration/search procedure that derives efficient, hardware-specific mapping strategies automatically rather than via per-architecture hand design
- Evaluates the framework across four distinct PIM hardware architectures to demonstrate generality
- Reports speedups over state-of-the-art, architecture-specific mapping methods for both single-operator and whole-network mapping

## Key claims (stable IDs)
- **2023_Cui_ARES_ICCAD#C1** — ARES achieves up to 70% speed improvement for single operator mapping versus state-of-the-art mapping methods. — _support:_ reported speedup figure in abstract — _loc:_ Abstract
- **2023_Cui_ARES_ICCAD#C2** — ARES achieves up to 50% speedup for overall network mapping versus state-of-the-art mapping methods. — _support:_ reported speedup figure in abstract — _loc:_ Abstract
- **2023_Cui_ARES_ICCAD#C3** — A single general hardware-abstraction-based mapping framework can be applied across architecturally diverse PIM hardware without per-architecture redesign. — _support:_ evaluation across four distinct hardware architectures — _loc:_ Abstract / evaluation section (not verified in full text)

## Results
- Up to 70% speedup for single-operator mapping vs. state-of-the-art mapping methods (abstract)
- Up to 50% speedup for overall network mapping vs. state-of-the-art mapping methods (abstract)
- Evaluated across four distinct PIM hardware architectures (abstract; specific architectures not confirmed from full text)

## Limitations
- Full text was not available for this analysis; numbers above are taken verbatim from the abstract only, not independently verified against tables/figures
- Abstract does not specify which four hardware architectures were used, exact baselines compared against, or whether results are simulation-only
- No device-level or non-ideality modeling is evident from the abstract; this appears to be a compiler/dataflow-mapping contribution orthogonal to analog device accuracy concerns

## Remarks
Positioned similarly to other general PIM mapping/compilation frameworks (e.g., CIM-MLC) in this collection, addressing the practical software-stack gap between diverse crossbar/PIM hardware and DNN deployment. Because only the abstract was available, the critical assessment here is necessarily shallow; the claimed 50-70% speedups should be read as reported by the authors and not independently checked. This is useful background for the mapping/compilation thread of the thesis but should be followed up with the full text (ICCAD 2023 proceedings) before relying on specific numbers.

## Cites (in collection, 4)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 1)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2023_Cui_ARES_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccad57390.2023.10323777
