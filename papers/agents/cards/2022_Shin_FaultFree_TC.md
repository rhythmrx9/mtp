---
id: W4312457094
key: 2022_Shin_FaultFree_TC
title: "Fault-Free: A Framework for Analysis and Mitigation of Stuck-At-Fault on Realistic ReRAM-Based DNN Accelerators"
short: "Fault-Free"
year: 2022
venue: "TC"
venue_full: "IEEE Transactions on Computers (2022)"
authors: "Hyein Shin, Myeonggu Kang, Lee‐Sup Kim"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["stuck-at-faults", "calibration-compensation", "compiler-software-stack", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 7
citations_overall: 16
priority_score: 5.29
doi: "https://doi.org/10.1109/tc.2022.3227871"
pdf: null
fulltext: null
---

# Fault-Free

**Fault-Free: A Framework for Analysis and Mitigation of Stuck-At-Fault on Realistic ReRAM-Based DNN Accelerators** — IEEE Transactions on Computers (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes an offline-compilation plus lightweight online-compensation framework (Fault-Free) that mitigates stuck-at-fault errors in low-resolution ReRAM crossbars, recovering accuracy at only ~5% area and ~0.8% energy overhead versus an ideal (fault-free) accelerator.

## Summary
Low-resolution ReRAM cells used in energy-efficient DNN accelerators suffer severe stuck-at-fault (SAF) issues that corrupt a significant fraction of mapped weights and degrade inference accuracy. The paper analyzes how SAF impacts low-bit-resolution cells specifically, then proposes 'Fault-Free', a two-stage framework: an offline compilation stage that identifies indices of weights distorted by SAF and applies fault-aware weight decomposition plus closest-value mapping to minimize the resulting weight error, and an online stage that executes the DNN on the ReRAM accelerator with lightweight hardware compensation units applied selectively only to a small subset of affected weights (rather than globally), limiting hardware overhead. Evaluated across multiple DNN models on realistic ReRAM accelerator configurations, the framework restores near-ideal inference accuracy while adding only modest area (~5%) and energy (~0.8%) overhead relative to a hypothetical fault-free ReRAM accelerator.

## Contributions
- Analysis of how stuck-at-fault (SAF) severity scales with ReRAM cell bit-resolution, motivating the need for low-resolution-specific mitigation
- Offline compilation step: SAF-affected weight index extraction, fault-aware weight decomposition, and closest-value mapping to minimize mapping error before deployment
- Online lightweight compensation units applied selectively to only a small fraction of weights, reducing hardware cost versus full per-cell correction
- System-level evaluation showing accuracy recovery close to an ideal ReRAM accelerator with low area/energy overhead

## Key claims (stable IDs)
- **2022_Shin_FaultFree_TC#C1** — Fault-Free recovers near-ideal inference accuracy on ReRAM accelerators affected by stuck-at-faults — _support:_ average area overhead of 5% and energy overhead of 0.8% from an ideal ReRAM-based accelerator while preserving accuracy, across various DNN models — _loc:_ Abstract
- **2022_Shin_FaultFree_TC#C2** — Selective online compensation (applied to only a small portion of weights) is sufficient to control hardware overhead — _support:_ stated design choice reducing hardware overhead vs. full compensation — _loc:_ Abstract

## Results
- Average area overhead ~5% and energy overhead ~0.8% versus an ideal (fault-free) ReRAM-based DNN accelerator, across multiple DNN models

## Limitations
- Abstract-only analysis: full text unavailable, so exact SAF rates assumed, DNN models/datasets tested, and comparison baselines could not be independently verified
- Builds on the same group's prior thermal-aware ReRAM optimization work, suggesting the evaluation methodology/accelerator model may be shared/simulation-based rather than measured silicon

## Remarks
This targets a well-known, practically important non-ideality (stuck-at-faults in low-bit-resolution ReRAM cells) with a software/compilation-centric fix rather than pure redundancy, which is attractive because it avoids blanket hardware duplication. Without the full text the precise fault models and benchmark suite can't be checked, so the reported ~5%/~0.8% overhead figures should be treated as the authors' claim pending verification; it builds directly on Shin et al.'s earlier thermal-aware ReRAM optimization line and was followed up by at least one 2025 paper (Atleus) in the same space.

## Cites (in collection, 7)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 2)
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _contrasts/critiques_: "Existing approaches aimed at reducing the number of rewrites during training or fine-tuning incur significant performance overhead or necessitate redundant hardware [15] [16]."
- [2025_Malhotra_ReTern_TVLSI](2025_Malhotra_ReTern_TVLSI.md) ReTern (2025) — _contrasts/critiques_: "The works in [17]-[19] show improved accuracies for inference with SAFs; however, these mapping strategies are not applicable to ternary weights."

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2022_Shin_FaultFree_TC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tc.2022.3227871
