---
id: W4411233189
key: 2025_Chen_EdramRramZoFinetune_IMW
title: "Analog Multilevel eDRAM-RRAM CIM for Zeroth-Order Fine-tuning of LLMs"
short: "eDRAMRRAMZO"
year: 2025
venue: "IMW"
venue_full: "IEEE International Memory Workshop (IMW), 2025"
authors: "Mufeng Chen, Luqi Zheng, Jian-Yu Lin, Peide D. Ye, Haitong Li"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["RRAM", "eDRAM (MOM, In2O3 FET gain cell)"]
models: ["GPT/LLM"]
lm_models: []
param_scale: "unspecified (language-model fine-tuning)"
slm: true
evidence: simulation
topics: ["on-chip-training", "llm-adapters-lora", "language-models", "peripheral-circuits", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 0
citations_overall: 3
priority_score: 8.42
doi: "https://doi.org/10.1109/imw61990.2025.11026966"
pdf: null
fulltext: null
---

# eDRAMRRAMZO

**Analog Multilevel eDRAM-RRAM CIM for Zeroth-Order Fine-tuning of LLMs** — IEEE International Memory Workshop (IMW), 2025 (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Reliability-aware analog MLC eDRAM-RRAM CIM for zeroth-order LM fine-tuning, with 12x bit density over prior MLC eDRAM and further 5x density, 2x retention from In2O3 FETs.

## Summary
Zeroth-order fine-tuning avoids backpropagation and lowers memory overhead, suiting on-device LLM fine-tuning, but existing memory-centric accelerators trade off density, CIM capability and endurance/retention. The paper presents an RRAM-assisted MLC eDRAM programming scheme and a PVT-robust large-window time-to-digital converter. Two-finger MOM MLC-eDRAM gives 12x bit density over state of the art; BEOL In2O3 FETs add 5x density and 2x retention. Evidence type (measured vs simulated) is not clear from the truncated abstract.

## Language models evaluated
- Models: —
- Scale: unspecified (language-model fine-tuning)
- Note: Analog multi-level eDRAM-RRAM CIM co-designed with zeroth-order optimisation for on-device LM fine-tuning; analog in-memory compute with RRAM-assisted MLC eDRAM and BEOL In2O3 FETs. Specific LMs and parameter sizes not stated in the abstract.

## Contributions
- RRAM-assisted MLC eDRAM programming
- PVT-robust large-window TDC
- Co-design with zeroth-order optimisation for LM fine-tuning
- In2O3 BEOL FET gain cell for density/retention

## Key claims (stable IDs)
- **2025_Chen_EdramRramZoFinetune_IMW#C1** — MLC-eDRAM with two-finger MOM gives 12x bit density over SOTA MLC — _support:_ 12x — _loc:_ Abstract

## Results
- 12x bit density vs state-of-the-art MLC eDRAM
- additional 5x density and 2x retention with BEOL In2O3 FETs

## Limitations
- Abstract-only; LM sizes and accuracy not seen
- Unclear if silicon or simulation

## Remarks
Interesting because it targets training/fine-tuning, which is rare in analog IMC literature. Without the full text the LM-level evidence is unverified.

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2025_Chen_EdramRramZoFinetune_IMW.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/imw61990.2025.11026966
