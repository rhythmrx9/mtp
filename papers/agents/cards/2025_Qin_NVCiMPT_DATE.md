---
id: W4410582659
key: 2025_Qin_NVCiMPT_DATE
title: "NVCiM-PT: An NVCiM-Assisted Prompt Tuning Framework for Edge LLMs"
short: "NVCiM-PT"
year: 2025
venue: "DATE"
venue_full: "Design, Automation & Test in Europe Conference & Exhibition (DATE 2025)"
authors: "Ruiyang Qin, Pengyu Ren, Zheyu Yan, Liu Liu, Dancheng Liu, Amir Nassereldine, Jinjun Xiong, Kai Ni, Xiaobo Sharon Hu, Yiyu Shi"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "FeFET"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["Gemma-2B", "Mistral-7B-GPTQ", "Phi-2"]
param_scale: "2B-7B"
slm: true
evidence: algorithm+simulation
topics: ["language-models", "llm-adapters-lora", "noise-injection", "device-variation", "write-verify-programming", "edge-ai", "energy-efficiency", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 4
citations_overall: 2
priority_score: 8.33
doi: "https://doi.org/10.23919/date64628.2025.10993249"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Qin_NVCiMPT_DATE.pdf"
fulltext: "../fulltext/2025_Qin_NVCiMPT_DATE.txt"
---

# NVCiM-PT

**NVCiM-PT: An NVCiM-Assisted Prompt Tuning Framework for Edge LLMs** — Design, Automation & Test in Europe Conference & Exhibition (DATE 2025) (2025)

## TL;DR
NVCiM-PT stores per-sample optimal prompt-tuning virtual tokens (OVTs) in NVM crossbars with noise-aware training and retrieves them by an in-memory scaled search, improving edge-LLM performance on NVM devices by up to 36.7% and cutting retrieval latency up to 120x and energy up to 60x versus a Jetson Orin CPU.

## Summary
Edge LLMs personalize via prompt tuning, but one-for-all virtual tokens suffer under user domain shift, while per-sample optimal virtual tokens (OVTs) grow in storage and incur DRAM/SSD data movement. The framework has three parts: representative data selection from a small buffer, noise-aware prompt training so OVTs tolerate NVM device variation, and storing OVTs in NVM crossbars (after autoencoder reshaping) and retrieving them by a Scaled Search Algorithm (SSA), a weighted multi-scale (L=1,2,4; weights 1,0.8,0.6) pooled dot-product similarity that reduces to matrix-matrix multiplication on the crossbar. Note the LLM itself is not on the crossbar: only the OVT store/search is. Device variation is modelled for RRAM and FeFET devices abstracted from published chips (RRAM1, RRAM4, FeFET2 plus two synthesized FeFET variants), x-level devices with per-level variance. Evaluation uses Gemma-2B, Mistral-7B-GPTQ, Phi-2 on LaMP-1/2/3/5/7 (accuracy and ROUGE-1) against SWV, CxDNN, CorrectNet and MIPS retrieval; latency/energy via NeuroSim at 22nm vs Jetson Orin CPU.

## Language models evaluated
- Models: Gemma-2B, Mistral-7B-GPTQ, Phi-2
- Scale: 2B-7B
- Note: Gemma-2B, Mistral-7B-GPTQ and Phi-2 (edge SLMs) personalized by prompt tuning with virtual tokens stored/searched on simulated NVM crossbars (RRAM/FeFET) versus Jetson Orin CPU.

## Contributions
- First NVCiM-assisted prompt-tuning framework for edge LLMs
- Noise-aware training of OVTs resilient to NVM device variation
- Scaled search algorithm for retrieving noisy NVM-stored OVTs
- Latency/energy evaluation on RRAM and FeFET CiM

## Key claims (stable IDs)
- **2025_Qin_NVCiMPT_DATE#C1** — Improves edge-LLM performance by up to 36.7% across NVM devices — _support:_ vs noise-mitigation baselines at sigma=0.1 — _loc:_ Sec. I, Table I
- **2025_Qin_NVCiMPT_DATE#C2** — Up to 120x latency and 60x energy improvement over Jetson Orin CPU for retrieval — _support:_ NeuroSim 22nm, RRAM and FeFET — _loc:_ Fig. 5
- **2025_Qin_NVCiMPT_DATE#C3** — SSA and noise-aware training each contribute — _support:_ NVP*(MIPS) and No-Miti(MIPS) lower than NVCiM-PT in all LLM/NVM combinations — _loc:_ Table I

## Results
- Table I (25 samples/buffer, sigma 0.1): NVCiM-PT beats SWV, CxDNN, CorrectNet, No-Miti(MIPS), NVP*(MIPS) for all 3 LLMs and 5 NVM devices
- Table IV: robustness swept over sigma 0.025-0.125 on NVCiM-3 with Phi-2, LaMP-5

## Key numbers
- tech_node: 22nm (NeuroSim)
- energy_eff: up to 60x vs Jetson Orin CPU
- throughput: up to 120x lower latency
- accuracy: up to 36.7% improvement

## Datasets / benchmarks
LaMP-1, LaMP-2, LaMP-3, LaMP-5, LaMP-7

## Limitations
- LLM weights are not mapped to the crossbar; only OVT storage/search
- Latency/energy from NeuroSim simulation, compared with CPU not a GPU
- Device variation abstracted/synthesized, not measured on this task
- Short paper; limited detail on array dimensions and ADC settings

## Remarks
An unusual NVCiM use for LLMs: associative memory of prompts rather than weight MVM, so it complements rather than substitutes the weight-mapping literature. Accuracy gains come from algorithmic robustness under modelled variation; hardware numbers are simulated. Same group as the RAG-on-CiM paper in the collection.

## Cites (in collection, 4)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "We also evaluate the latency and energy of retrieval of the appropriate data by our scaled search algorithm on NVCiM via NeuroSim [36]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "RRAM stores data by changing the resistance across a dielectric material [18], while FeFET utilizes ferroelectric materials to maintain data through polarization states [19]."
- [2024_Qin_RoCR_ICCAD](2024_Qin_RoCR_ICCAD.md) RoCR (2024) — _background_: "Under the constraint of memory capacity and computational power on edge devices, existing works mainly take two types of approaches to enable LLM learning on edge: retrieval-augmented generation (RAG) [8] and low-rank adaption (LoRA) [9]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _data/numbers_: "The specific parameters are abstracted and then simplified from three representative NVM devices, two of them are resistive random-access memory (RRAM) devices extracted from [29], [30], and the other is a ferroelectric field effect transistor (FeFET) device extracted from [31]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Qin_NVCiMPT_DATE.pdf](../../11_Small_Language_Models_on_AIMC/2025_Qin_NVCiMPT_DATE.pdf)
- Full text: [../fulltext/2025_Qin_NVCiMPT_DATE.txt](../fulltext/2025_Qin_NVCiMPT_DATE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.23919/date64628.2025.10993249
