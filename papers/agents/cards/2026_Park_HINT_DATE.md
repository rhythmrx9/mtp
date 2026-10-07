---
id: W7163529284
key: 2026_Park_HINT_DATE
title: "HINT: A Hybrid SRAM–MRAM Compute-In-Memory with INput-aware Skipping SAR-ADC for Energy Efficient Ternary LLMs"
short: "HINT"
year: 2026
venue: "DATE"
venue_full: "2026 Design, Automation & Test in Europe Conference (DATE)"
authors: "Jaebeom Park, Seung-Eon Hwang, Jongsun Park"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["MRAM", "SRAM"]
models: ["GPT/LLM"]
lm_models: ["BitNet b1.58 700M"]
param_scale: "700M"
slm: true
evidence: simulation
topics: ["macro", "heterogeneous-analog-digital", "transformer-accelerator", "language-models", "adc-dac", "quantization"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 0
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.23919/date69613.2026.11539338"
pdf: null
fulltext: null
---

# HINT

**HINT: A Hybrid SRAM–MRAM Compute-In-Memory with INput-aware Skipping SAR-ADC for Energy Efficient Ternary LLMs** — 2026 Design, Automation & Test in Europe Conference (DATE) (2026)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Hybrid SRAM-MRAM ternary bitcell and sparsity-skipping SAR-ADC give 1.85x bitcell density and up to 2.67x energy efficiency on BitNet b1.58 700M.

## Summary
Targets ternary LLM CIM, where existing ternary bitcells are low-density and cut-off ADCs hurt accuracy. HINT uses a hybrid ternary bitcell combining SRAM reliability and MRAM density, plus an input-aware SAR-ADC that skips conversion cycles using input sparsity. On BitNet b1.58 700M it improves density 1.85x and energy efficiency up to 2.67x over SRAM/eDRAM CIM, skipping up to 21% of cycles for 1.27x ADC efficiency without accuracy loss. Abstract-only.

## Language models evaluated
- Models: BitNet b1.58 700M
- Scale: 700M
- Note: Hybrid SRAM-MRAM ternary CIM with input-aware skipping SAR-ADC, evaluated on BitNet b1.58 700M (ternary SLM). Analog MAC with ADC readout; MRAM provides density.

## Contributions
- Hybrid SRAM-MRAM ternary bitcell
- Input-aware skipping SAR-ADC

## Results
- 1.85x bitcell density
- up to 2.67x energy efficiency vs SRAM/eDRAM CIM
- up to 21% ADC cycles skipped, 1.27x ADC efficiency

## Limitations
- Circuit simulation likely; abstract-only
- Baselines are volatile CIMs, not NVM

## Remarks
Directly on target for ternary SLMs on MRAM-assisted CIM. The ADC skipping idea is generic. Needs full text to verify accuracy and device modeling.

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2026_Park_HINT_DATE.pdf`)
- Full text: none
- DOI: https://doi.org/10.23919/date69613.2026.11539338
