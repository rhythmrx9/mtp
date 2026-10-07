---
id: W4381733878
key: 2023_Kang_MGen_TC
title: "MGen: A Framework for Energy-Efficient In-ReRAM Acceleration of Multi-Task BERT"
short: "MGen"
year: 2023
venue: "TC"
venue_full: "IEEE Transactions on Computers"
authors: "Myeonggu Kang, Hyein Shin, Junkyum Kim, Lee‐Sup Kim"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["BERT", "Transformer"]
lm_models: ["BERT (multi-task)"]
param_scale: "BERT-scale (size not specified)"
slm: true
evidence: algorithm+simulation
topics: ["nas-codesign", "scheduling", "transformer-accelerator", "language-models", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 3
priority_score: 7.92
doi: "https://doi.org/10.1109/tc.2023.3288749"
pdf: null
fulltext: null
---

# MGen

**MGen: A Framework for Energy-Efficient In-ReRAM Acceleration of Multi-Task BERT** — IEEE Transactions on Computers (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
MGen is a framework that generates reduced-redundancy multi-task BERT models and schedules their execution order to cut the energy (not just area) cost of running multi-task BERT on ReRAM-based accelerators, reporting up to 4.4x energy-efficiency gains.

## Summary
The paper addresses multi-task BERT deployment on ReRAM-based DNN accelerators: prior work reduced the area overhead of storing multiple task-specific BERT models in ReRAM crossbars, but computation volume (and hence energy) stays the same regardless of parameter-sharing, so energy consumption remains high. The authors analyze redundancies inherent to multi-task BERT together with the computational characteristics of ReRAM-based accelerators, then propose a 'model generator' that produces optimized BERT variants supporting multiple tasks while reducing the number of computations and preserving task accuracy. A companion 'task scheduler' reorders execution of multiple tasks' inference to better exploit the generated models' structure on the ReRAM accelerator. The framework is shown to be composable with prior area-reduction multi-task BERT techniques, jointly achieving smaller area and higher energy efficiency, with a reported maximum 4.4x energy-efficiency improvement over baseline.

## Language models evaluated
- Models: BERT (multi-task)
- Scale: BERT-scale (size not specified)
- Note: Multi-task BERT models on a ReRAM-based digital/analog accelerator model; specific BERT size not stated in the available text.

## Contributions
- Identifies that prior multi-task BERT work on ReRAM accelerators reduces area/parameter count but not computation volume or energy
- Model generator: produces optimized multi-task BERT models that reduce computation while preserving algorithmic (task) performance
- Task scheduler: reorders multi-task execution to better exploit the generated models' structure for energy efficiency on ReRAM hardware
- Shows the framework composes with prior area-efficient multi-task BERT accelerator work for combined area and energy gains

## Key claims (stable IDs)
- **2023_Kang_MGen_TC#C1** — The proposed framework achieves up to 4.4x higher energy efficiency than the baseline ReRAM multi-task BERT accelerator — _support:_ maximally 4.4x higher energy efficiency over baseline — _loc:_ Abstract

## Results
- Up to 4.4x energy-efficiency improvement over baseline multi-task BERT ReRAM acceleration

## Limitations
- Analysis based on abstract only (full text not accessible); specific benchmark tasks, accuracy deltas, and ReRAM simulator/architecture assumptions could not be verified
- Energy-efficiency gains are relative to the authors' own baseline multi-task BERT ReRAM setup, so absolute comparison to other accelerator families is unclear from the abstract alone

## Remarks
This is a software/mapping-level contribution (model generation + task scheduling) layered on top of ReRAM-based transformer accelerators, directly building on the same group's earlier area-efficient multi-task BERT framework (Kang et al., W4200149283) and the ReRAM transformer accelerator literature (ReTransformer, Kang's prior ReRAM transformer framework). Its significance for analog/PIM mapping is in treating energy, not just crossbar area, as the optimization target for multi-task LLM-style deployment — but with abstract-only access the specific mechanisms behind the 4.4x figure (e.g., which redundancies are exploited, what accuracy is preserved) could not be confirmed.

## Cites (in collection, 8)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) Area-Efficient Multi-Task BERT (2021)
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2023_Kang_MGen_TC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tc.2023.3288749
