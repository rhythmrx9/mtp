---
id: W4312542636
key: 2022_Qu_CoordinatedPruningMapping_TCAD
title: "A Coordinated Model Pruning and Mapping Framework for RRAM-Based DNN Accelerators"
short: "Coordinated Pruning-Mapping"
year: 2022
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022)"
authors: "Songyun Qu, Bing Li, Shixin Zhao, Lei Zhang, Ying Wang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "weight-mapping", "crossbar-architecture", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 9
citations_overall: 9
priority_score: 5.6
doi: "https://doi.org/10.1109/tcad.2022.3221906"
pdf: null
fulltext: null
---

# Coordinated Pruning-Mapping

**A Coordinated Model Pruning and Mapping Framework for RRAM-Based DNN Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Jointly co-designs bit-wise pruning and crossbar mapping for RRAM DNN accelerators, using two's-complement bit-matrix decoupling and an RL-driven crossbar-granularity bit-pruning policy to free whole crossbars rather than leaving sparsity unexploited; reports up to 89.64% energy and 84.12% area reduction versus a PRIME-like baseline and 1.5x better energy reduction than SOTA bit-sparsity designs.

## Summary
RRAM-based DNN accelerators normally apply weight pruning and crossbar mapping as separate, independently-optimized steps, which leaves the random zeros produced by pruning irregularly scattered across crossbars so that computation parallelism is lost without any reduction in the number of crossbars actually needed. The paper proposes a coordinated framework that unifies pruning and mapping: weight matrices are decoupled bit-wise and mapped to separate crossbars, using two's-complement representation of signed weights to roughly halve the crossbars needed; pruning is then performed at crossbar granularity (pruning whole bit-slices rather than scattered individual weights) so that entire crossbars holding pruned bits can be physically freed rather than merely zeroed. A reinforcement-learning (RL) agent automatically searches for the optimal crossbar-aware bit-pruning policy per network, removing the need for hand-tuned pruning schedules. On a set of representative CNNs, the coordinated framework is compared against a PRIME-like architecture and against state-of-the-art bit-sparsity designs.

## Contributions
- Bit-wise decoupling of weight matrices with two's-complement signed representation to roughly halve the number of crossbars needed for weight storage
- Crossbar-granularity bit-pruning that prunes whole bit-slices so pruned crossbars can be physically freed (not just zeroed), recovering parallelism lost to irregular sparsity
- RL-based automatic search for the crossbar-aware bit-pruning strategy per network, avoiding manual tuning
- Joint pruning+mapping co-optimization framework evaluated against a PRIME-like baseline and SOTA bit-sparsity designs

## Key claims (stable IDs)
- **2022_Qu_CoordinatedPruningMapping_TCAD#C1** — Coordinating pruning and mapping (vs. optimizing them independently) substantially reduces energy and area on RRAM accelerators — _support:_ up to 89.64% energy reduction and 84.12% area overhead reduction compared to existing PRIME-like architecture — _loc:_ Abstract
- **2022_Qu_CoordinatedPruningMapping_TCAD#C2** — The framework outperforms state-of-the-art bit-sparsity accelerator designs — _support:_ 1.5x better energy reduction than the SOTA bit-sparsity design on the RRAM-based accelerator — _loc:_ Abstract

## Results
- Up to 89.64% energy reduction and 84.12% area overhead reduction vs. a PRIME-like RRAM accelerator baseline
- 1.5x energy reduction improvement over the state-of-the-art bit-sparsity design

## Limitations
- Abstract-only analysis: full text unavailable, so exact benchmark networks, accuracy impact of pruning, and RL search cost could not be verified
- Comparisons framed primarily against PRIME-like and bit-sparsity baselines; broader comparison against other mapping/compiler frameworks not stated in the abstract

## Remarks
This addresses a real and under-appreciated mismatch in RRAM accelerator design flows: pruning algorithms and crossbar mapping are usually developed independently, so irregular sparsity patterns fail to reduce the actual crossbar count. The bit-slice/two's-complement decoupling plus RL-driven crossbar-granularity pruning is a sensible hardware-aware co-design approach consistent with other works by the same group (RaQu). Reported gains are large (near 90% energy/area reduction) but are abstract-only claims relative to a PRIME-like baseline, so the margin over more modern mapping frameworks is unclear without the full text; it was later cited by CIM-MLC as part of the broader compilation-stack literature for CIM accelerators.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019)
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019)
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020)
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 1)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _background_: "Other works propose to decompose DNN operators and schedule MVM-grained operation in CIM crossbars [4, 19, 36, 43, 49]."

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2022_Qu_CoordinatedPruningMapping_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2022.3221906
