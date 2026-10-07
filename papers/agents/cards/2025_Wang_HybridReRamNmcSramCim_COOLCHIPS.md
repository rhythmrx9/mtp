---
id: W4411204550
key: 2025_Wang_HybridReRamNmcSramCim_COOLCHIPS
title: "Hybrid ReRAM-NMC & SRAM-CiM Matrix Multiplication for Large Language Model"
short: "HybridReRAMNMC"
year: 2025
venue: "COOLCHIPS"
venue_full: "2025 IEEE Symposium on Low-Power and High-Speed Chips and Systems (COOL CHIPS)"
authors: "Tao Wang, Daqi Lin, Kenshin Yamauchi, Naoko Misawa, Chihiro Matsui, Ken Takeuchi"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "SRAM"]
models: ["GPT/LLM"]
lm_models: ["Llama2-7B"]
param_scale: "7B"
slm: true
evidence: algorithm+simulation
topics: ["heterogeneous-analog-digital", "language-models", "transformer-accelerator", "peripheral-circuits", "quantization"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 0
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/coolchips65488.2025.11018598"
pdf: null
fulltext: null
---

# HybridReRAMNMC

**Hybrid ReRAM-NMC & SRAM-CiM Matrix Multiplication for Large Language Model** — 2025 IEEE Symposium on Low-Power and High-Speed Chips and Systems (COOL CHIPS) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Splits activations so <1% go to SRAM-CiM and the rest to ReRAM-NMC, keeping Llama2-7B perplexity increase under 2 for Gaussian and shift ReRAM errors at 6-bit precision.

## Summary
ReRAM nonidealities (conductance shift) hinder LLM deployment on ReRAM CiM. The proposed hybrid places a small fraction of sensitive activations on error-free SRAM-CiM and the remaining on ReRAM-NMC, improving robustness. A hardware architecture with MAC circuit and hybrid-core pipeline is outlined. With 6-bit quantization, Llama2-7B perplexity increases by less than 2 for both error models with SRAM share below 1%. (Abstract only.)

## Language models evaluated
- Models: Llama2-7B
- Scale: 7B
- Note: Llama2-7B with 6-bit weights/activations under ReRAM conductance error (Gaussian and shift); outlier activations routed to SRAM-CiM, rest on ReRAM near-memory computing (ReRAM-NMC). ReRAM used with NMC, so analog-compute status unclear; robustness to device error is the focus.

## Contributions
- Hybrid ReRAM-NMC and SRAM-CiM matrix multiplication
- Activation separation to improve robustness
- Hybrid-core pipeline and MAC circuit design

## Key claims (stable IDs)
- **2025_Wang_HybridReRamNmcSramCim_COOLCHIPS#C1** — Perplexity rise <2 for Llama2-7B with SRAM share <1% — _support:_ abstract — _loc:_ Abstract

## Results
- Llama2-7B, W6A6: perplexity increase <2 under Gaussian and shift errors, SRAM <1%

## Limitations
- Abstract only
- Error models simplified; no silicon
- Absolute perplexity and energy numbers unknown

## Remarks
Directly on target: a 7B LLM under ReRAM error with a cheap mitigation. Perplexity increase of up to 2 is not negligible. Needs real device validation.

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2025_Wang_HybridReRamNmcSramCim_COOLCHIPS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/coolchips65488.2025.11018598
