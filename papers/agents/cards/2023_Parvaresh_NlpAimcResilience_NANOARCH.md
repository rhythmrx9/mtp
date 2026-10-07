---
id: W4391213160
key: 2023_Parvaresh_NlpAimcResilience_NANOARCH
title: "Resilience and Precision Assessment of Natural Language Processing Algorithms in Analog In-Memory Computing: A Hardware-Aware Study"
short: "NLP-AIMC"
year: 2023
venue: "NANOARCH"
venue_full: "Proceedings of the 18th ACM International Symposium on Nanoscale Architectures (NANOARCH 2023)"
authors: "Amirhossein Parvaresh, Shima Hosseinzadeh, Dietmar Fey"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["generic analog crossbar (PCM-style via AIHWKit, assumed)"]
models: ["RNN", "CNN"]
lm_models: ["GRU", "LSTM", "CNN text models"]
param_scale: "small (unspecified)"
slm: false
evidence: simulation
topics: ["hardware-aware-training", "noise-injection", "recurrent-models", "language-models", "device-variation"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 2
citations_overall: 1
priority_score: 3.71
doi: "https://doi.org/10.1145/3611315.3633266"
pdf: null
fulltext: null
---

# NLP-AIMC

**Resilience and Precision Assessment of Natural Language Processing Algorithms in Analog In-Memory Computing: A Hardware-Aware Study** — Proceedings of the 18th ACM International Symposium on Nanoscale Architectures (NANOARCH 2023) (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Evaluates NLP networks (GRU, LSTM, CNN) under analog in-memory computing non-idealities with and without hardware-aware training; GRU is most robust (3.97% avg error), CNN least (13.34%).

## Summary
The paper asks how well NLP algorithms tolerate analog in-memory computing non-idealities such as noise. It runs hardware-aware simulation of several NLP networks, with and without hardware-aware training. GRUs reach 3.97% average test error after HWA training relative to full precision, LSTMs 5.67%, CNNs 13.34% relative error. It also analyses sensitivity to individual non-idealities. Based on the abstract only; mapping details are not available.

## Language models evaluated
- Models: GRU, LSTM, CNN text models
- Scale: small (unspecified)
- Note: Studies GRU, LSTM and CNN-based NLP models (small recurrent/convolutional text models), not transformer language models, under AIMC non-idealities (likely via the IBM AIHWKit, which it cites). Analog compute in memory is simulated. Only loosely 'language model' relevant; no BERT/GPT-style models mentioned in the abstract.

## Contributions
- Comparative resilience study of GRU, LSTM, CNN NLP models on simulated AIMC
- Quantifies benefit of hardware-aware training
- Per-non-ideality sensitivity profiles

## Key claims (stable IDs)
- **2023_Parvaresh_NlpAimcResilience_NANOARCH#C1** — GRU is more noise-resilient than LSTM and CNN under AIMC — _support:_ 3.97% vs 5.67% vs 13.34% avg error — _loc:_ Abstract

## Results
- GRU 3.97% avg test error after HWA training; LSTM 5.67%; CNN 13.34% relative error (baseline: full precision)

## Limitations
- No transformer/LLM models
- Abstract-only analysis; details of noise model unverified

## Remarks
Early, small-model NLP robustness study; useful as a baseline for non-ideality sensitivity but predates transformer-based SLM work. Metrics defined loosely (error relative to full precision). Weakly relevant to SLMs.

## Cites (in collection, 2)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2023_Parvaresh_NlpAimcResilience_NANOARCH.pdf`)
- Full text: none
- DOI: https://doi.org/10.1145/3611315.3633266
