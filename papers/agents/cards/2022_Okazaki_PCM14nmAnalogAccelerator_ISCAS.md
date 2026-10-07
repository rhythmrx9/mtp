---
id: W4312799098
key: 2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS
title: "Analog-memory-based 14nm Hardware Accelerator for Dense Deep Neural Networks including Transformers"
short: "PCM14nm"
year: 2022
venue: "ISCAS"
venue_full: "IEEE International Symposium on Circuits and Systems (ISCAS), 2022"
authors: "Atsuya Okazaki, Pritish Narayanan, Stefano Ambrogio, Kohji Hosokawa, Hsinyu Tsai, Akiyo Nomura, Takeo Yasuda, Charles Mackin, Alexander M. Friz, Masatoshi Ishii, Yasuteru Kohda, Katie Spoon et al."
category: "02 Fabricated Chips & Macros"
devices: ["PCM"]
models: ["LSTM", "BERT/Transformer"]
lm_models: ["BERT (projected)", "LSTM"]
param_scale: "~110M-340M (BERT, projected)"
slm: true
evidence: measured-silicon
topics: ["chip-demo", "conductance-drift", "calibration-compensation", "recurrent-models", "transformer-accelerator", "analog-mvm"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 6
citations_overall: 6
priority_score: 8.09
doi: "https://doi.org/10.1109/iscas48785.2022.9937292"
pdf: null
fulltext: null
---

# PCM14nm

**Analog-memory-based 14nm Hardware Accelerator for Dense Deep Neural Networks including Transformers** — IEEE International Symposium on Circuits and Systems (ISCAS), 2022 (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
14nm chip with multiple 512x512 PCM arrays gives software-equivalent accuracy on MNIST and LSTM using drift/noise compensation, and the paper projects BERT NLP accuracy on an extended version.

## Summary
Describes an IBM 14nm inference chip built from multiple 512x512 PCM arrays performing analog MAC via Ohm/Kirchhoff laws. Compensation techniques counter conductance drift and noise so that MNIST and recurrent LSTM benchmarks reach software-equivalent accuracy. The authors then project accuracy for NLP tasks with BERT mapped onto an extended version of the same architecture. Only the abstract was available, so details of mapping and numbers are not recorded here.

## Language models evaluated
- Models: BERT (projected), LSTM
- Scale: ~110M-340M (BERT, projected)
- Note: 14nm PCM chip with 512x512 arrays (true analog MVM) demonstrated on MNIST and LSTM; BERT (~110M-340M scale) accuracy only projected for an extended architecture. LM content is a projection, not measured.

## Contributions
- 14nm multi-array PCM analog inference chip
- Drift and noise compensation yielding software-equivalent accuracy on MNIST and LSTM
- Projection of BERT accuracy on an extended architecture

## Limitations
- BERT results are projections, not silicon measurements
- Abstract-only analysis

## Remarks
Important early step in the IBM analog-AI line toward Transformers, but LM evidence is a projection. Silicon validates only small DNN/LSTM workloads.

## Cites (in collection, 6)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)

## Cited by (in collection, 1)
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _background_: "Other works explore accelerating Transformer attention [39, 58, 77]."

## Files
- PDF: not available locally (save as `papers/02_Fabricated_Chips_and_Macros/2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iscas48785.2022.9937292
