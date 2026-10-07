---
id: W4412375723
key: 2025_Malhotra_ReTern_TVLSI
title: "ReTern: Exploiting Natural Redundancy and Sign Transformations for Enhanced Fault Tolerance in Compute-in-Memory-Based Ternary LLMs"
short: "ReTern"
year: 2025
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2025"
authors: "Akul Malhotra, Sumeet Kumar Gupta"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["SRAM-digital", "FeFET", "ReRAM"]
models: ["GPT/LLM", "Transformer"]
lm_models: ["BitNet b1.58 700M", "BitNet b1.58 3B"]
param_scale: "0.7B-3B"
slm: true
evidence: algorithm+simulation
topics: ["stuck-at-faults", "language-models", "quantization", "calibration-compensation", "peripheral-circuits", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/tvlsi.2025.3585043"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Malhotra_ReTern_TVLSI.pdf"
fulltext: "../fulltext/2025_Malhotra_ReTern_TVLSI.txt"
---

# ReTern

**ReTern: Exploiting Natural Redundancy and Sign Transformations for Enhanced Fault Tolerance in Compute-in-Memory-Based Ternary LLMs** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2025 (2025)

## TL;DR
ReTern combines fault-aware column sign flips (FAST) with zero-weight bitcell reprogramming (zero-fix) to tolerate stuck-at faults in ternary CiM, cutting Wikitext perplexity increase by ~35% (700M) / 25% (3B) at 10% SAF rate with <3% energy, <7% latency, <1% area overhead.

## Summary
Ternary LLMs (BitNet b1.58) map well to ternary CiM (TCiM) arrays that store each weight in two binary cells (W=M1-M2) and subtract two bitline results, but stuck-at faults (SAFs) corrupt weights. The prior method TFix only fixes zero weights using the unused (1,1)-state redundancy and relies on high sparsity; BitNet LLMs have low sparsity (37.05% and 37.55% for 700M and 3B) so TFix is weak. ReTern adds fault-aware sign transformations: per 64-row column, the stored weights are negated if that lowers unmasked faults on +1/-1 weights, a col_flip bit per column records this, and the output is negated through two 2:1 muxes before the existing subtractor. Zero-fix then rewrites zero weights hit by a SAF into the alternate zero encoding. Pretrained BitNet 700M/3B weights are tiled onto 64x64 TCiM arrays with SAFs injected uniformly at random (5% and 10%, 20 Monte Carlo runs); only feedforward weights are on CiM, attention stays on digital cores and is treated as fault-free. Metrics are Wikitext perplexity and PIQA / ARC-easy accuracy; overheads are estimated with NeuroSim for SRAM, FeFET and ReRAM TCiM, with 4-bit flash ADCs, 16-row activation and column peripherals shared across 8 columns.

## Language models evaluated
- Models: BitNet b1.58 700M, BitNet b1.58 3B
- Scale: 0.7B-3B
- Note: Ternary BitNet b1.58 700M and 3B on ternary CiM arrays (64x64, SRAM/ReRAM/FeFET bitcells, two binary cells per ternary weight, ADC readout); fault tolerance to stuck-at faults. Feed-forward layers in CiM, attention digital. Binary cells with analog bitline accumulation.

## Contributions
- Analysis of SAF impact and the limits of TFix on two ternary LLMs (low weight sparsity)
- Fault-aware sign transformations (FAST) via per-column flip bit plus post-processing negation
- ReTern = FAST + zero-fix, training-free and complementary
- Overhead estimates for SRAM, FeFET and ReRAM TCiM accelerators

## Key claims (stable IDs)
- **2025_Malhotra_ReTern_TVLSI#C1** — Baseline BitNet degrades notably under SAFs and larger model is more robust — _support:_ 10% SAF: 700M Wikitext PPL ~12 to ~26; 3B ~10 to ~15 — _loc:_ Sec. IV-B / Figs. 6-7
- **2025_Malhotra_ReTern_TVLSI#C2** — ReTern reduces perplexity degradation by ~35% (700M) and 25% (3B) at 10% SAF — _support:_ 5% SAF: 10% and 8% reduction; PIQA +4%/+2%, ARC-easy +6%/+5% at 10% SAF — _loc:_ Sec. IV-B
- **2025_Malhotra_ReTern_TVLSI#C3** — Overheads are small — _support:_ energy 2.0-2.2%, latency 3.2-6.6%, area <1% — _loc:_ Sec. IV-C / Table I

## Results
- 700M model, 10% SAF: baseline PPL ~26 vs ideal ~12; ReTern ~35% PPL reduction on average (Fig. 6)
- 3B model, 10% SAF: baseline PPL ~10 to ~15; ReTern ~25% PPL reduction (Fig. 7)
- TFix alone and FAST alone each give ~23% PPL improvement (700M) and ~15% (3B) at 10% SAF; combining them is better
- Overheads relative to unprotected TCiM: 2.0-2.2% energy, 3.2-6.6% latency, <1% area across SRAM/FeFET/ReRAM (Table I)

## Key numbers
- array_size: 64x64 TCiM arrays (16 rows active)
- accuracy: ~35% perplexity reduction at 10% SAF (700M)
- bits_weight: ternary (1.58b)
- bits_adc: 4b flash

## Datasets / benchmarks
Wikitext, PIQA, ARC-easy

## Limitations
- Simulation with random uniform SAF model; no measured hardware
- Attention layers assumed on digital cores and fault-free
- Only SAFs considered; no analog noise, drift or variation
- Residual PPL after mitigation still above ideal; effect of array row count on efficacy left to future work
- Only ternary binary-cell TCiM (not multilevel NVM)

## Remarks
A specific, credible study of a real SLM class (BitNet) under hardware faults, with a cheap hardware hook. The evidence is simulation-only and fault-only, but it highlights that LLM weight sparsity is much lower than CNNs so CNN-era fault tricks transfer poorly. Relevant to the collection's theme of deploying 0.7-3B models on NVM CiM and to fault-tolerance work like Fault-Free.

## Cites (in collection, 6)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "To estimate the energy, latency, and area of the TCiM array peripherals including the row decoder, flash ADC, and subtractor as well as the additional multiplexers (MUXes) and register required for ReTern, we use NeuroSim [42]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _background_: "Various CiM-based LLM accelerators have been proposed, showcasing sizeable benefits over conventional von-Neumann based platforms such as GPUs [2]-[5]."
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022) — _contrasts/critiques_: "The works in [17]-[19] show improved accuracies for inference with SAFs; however, these mapping strategies are not applicable to ternary weights."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _extends/builds-on_: "Thus, works like [33] utilize digital compute cores for the self-attention layers, while using CiM-based memory arrays for the feedforward layers."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _background_: "Various CiM-based LLM accelerators have been proposed, showcasing sizeable benefits over conventional von-Neumann based platforms such as GPUs [2]-[5]."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _background_: "Various CiM-based LLM accelerators have been proposed, showcasing sizeable benefits over conventional von-Neumann based platforms such as GPUs [2]-[5]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Malhotra_ReTern_TVLSI.pdf](../../11_Small_Language_Models_on_AIMC/2025_Malhotra_ReTern_TVLSI.pdf)
- Full text: [../fulltext/2025_Malhotra_ReTern_TVLSI.txt](../fulltext/2025_Malhotra_ReTern_TVLSI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tvlsi.2025.3585043
