---
id: W4409282487
key: 2024_Qin_RoCR_ICCAD
title: "Robust Implementation of Retrieval-Augmented Generation on Edge-based Computing-in-Memory Architectures"
short: "RoCR"
year: 2024
venue: "ICCAD"
venue_full: "43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024)"
authors: "Ruiyang Qin, Zheyu Yan, Dewen Zeng, Zhenge Jia, Dancheng Liu, Jianbo Liu, Ahmed Abbasi, Zhi Zheng, Ningyuan Cao, Kai Ni, Jinjun Xiong, Yiyu Shi"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "FeFET"]
models: ["Transformer", "Other"]
lm_models: ["all-MiniLM-L6-v2 (sentence embedding, stored on CiM)", "Gemma-2B", "Phi-2", "Llama-2-3B", "Mistral-7B-GPTQ (generators)"]
param_scale: "22M embedding model; 2B-7B generators"
slm: true
evidence: algorithm+simulation
topics: ["language-models", "noise-injection", "hardware-aware-training", "device-variation", "edge-ai", "quantization", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 3
citations_overall: 10
priority_score: 9.63
doi: "https://doi.org/10.1145/3676536.3676674"
pdf: "../../11_Small_Language_Models_on_AIMC/2024_Qin_RoCR_ICCAD.pdf"
fulltext: "../fulltext/2024_Qin_RoCR_ICCAD.txt"
---

# RoCR

**Robust Implementation of Retrieval-Augmented Generation on Edge-based Computing-in-Memory Architectures** — 43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024) (2024)

## TL;DR
RoCR trains a sentence-embedding model with contrastive learning and noise-aware training so that CiM-based max-inner-product retrieval for edge RAG tolerates RRAM/FeFET variation, improving MIPS accuracy from ~0.45 to ~0.93 on Citation (sigma=0.1) and RAG quality by up to 35%.

## Summary
Edge LLMs personalise via RAG, but retrieval (MIPS) over a growing profile database is slow on edge hardware; the authors put document embeddings in NVM crossbars and perform MIPS as an in-memory vector-matrix multiplication, with top-k and shift-and-add in digital logic. Device variation corrupts the stored embeddings and collapses retrieval accuracy toward random (Fig. 2). RoCR has three parts: a data construction module producing positive/negative pairs (CDE and CDI variants, using dropout rates 0.1 for positives and 0.9 for negatives in CDI, k=5, 2000 anchor documents), contrastive (triplet) loss to push dissimilar embeddings apart, and flexible noise-aware training that injects the measured per-level Gaussian device noise and a reshape module that quantises embeddings to e.g. 64 dimensions at int8, mapped across parallel arrays (a uint8 element uses four 2-bit devices). Noise models come from RRAM and FeFET measurements (sigma 0.0026-0.0155 depending on level, Table 2) and synthetic extrapolated FeFETs. Evaluation is simulated on a GPU on five LaMP-style datasets (Citation, Movie, Rating, News, DBLP) with Gemma-2B, Phi-2, Llama-2-3B and Mistral-7B generators and baselines SWV, CxDNN, CorrectNet and vanilla RAG.

## Language models evaluated
- Models: all-MiniLM-L6-v2 (sentence embedding, stored on CiM), Gemma-2B, Phi-2, Llama-2-3B, Mistral-7B-GPTQ (generators)
- Scale: 22M embedding model; 2B-7B generators
- Note: RAG for edge LLMs: the all-MiniLM-L6-v2 sentence-embedding matrix is stored in NVM CiM (RRAM/FeFET models) and max-inner-product search runs in-memory with device noise. Generator LLMs (Gemma-2B, Phi-2, Mistral-7B, Llama-2-3B) run digitally and are only the downstream consumer; the analog part is the retriever, not the LM.

## Contributions
- First work using CiM to accelerate RAG retrieval for edge LLMs
- Contrastive-learning plus noise-aware training of the embedding model for NVM variation
- Flexible framework that adapts to multiple NVM devices and precision/dimension constraints
- Up to 35% RAG performance improvement across five CiM devices

## Key claims (stable IDs)
- **2024_Qin_RoCR_ICCAD#C1** — Under device-1 variation (sigma=0.1) RoCR sharply raises MIPS accuracy over baselines — _support:_ Citation 0.9231 (CDE) / 0.9344 (CDI) vs vanilla 0.4547, SWV 0.4200 — _loc:_ Table 3
- **2024_Qin_RoCR_ICCAD#C2** — MIPS accuracy under plain Gaussian noise decays toward random guessing as noise grows — _support:_ Fig. 2 across five datasets — _loc:_ Fig. 2
- **2024_Qin_RoCR_ICCAD#C3** — RoCR beats baselines on all five CiM devices and four LLMs — _support:_ Fig. 6 (Citation, Movie) — _loc:_ Sec. 4.2, Fig. 6

## Results
- MIPS accuracy Movie 0.4639/0.4355 vs vanilla 0.1694; Rating 0.1583/0.1266 vs 0.0933; News 0.1921/0.1708 vs 0.0649 (Table 3)
- Up to 35% RAG performance gain on multiple CiM devices (abstract)
- Baselines SWV, CxDNN, CorrectNet vary widely across devices, RoCR more consistent
- CiM retrieval stated to take ~50 ms for a given document set (cited from NeuroSim work), vs 5 min MIPS on Raspberry Pi 4B for 21M documents

## Key numbers
- array_size: 64x64 (assumed CiM array)
- throughput: ~50 ms retrieval on CiM (cited)
- accuracy: MIPS accuracy 0.9344 vs 0.4547 vanilla (Citation, sigma=0.1)
- bits_weight: int8 embeddings, 64 dims, 2-bit/cell for FeFET

## Datasets / benchmarks
LaMP Citation Identification, Movie Tagging, Product Rating, News Headline Generation, DBLP-Citation-network V14

## Limitations
- Simulation only; no CiM hardware, latency or energy measured by the authors
- Only the retriever embeddings sit on CiM; LLMs run digitally, so it says nothing about executing LLM layers in analog
- Only temporal (programming) variation modelled, Gaussian per level; no drift, IR-drop or ADC noise
- Noise in embedding is 0.0026-0.0155 sigma, small relative to some real devices; absolute MIPS accuracy remains low on Rating/News/DBLP
- Baselines were designed for DNN weights, not retrieval, so comparison is somewhat strawman

## Remarks
A different slice of the SLM-on-NVM story: rather than mapping the LLM, it maps the retrieval index (embedding matrix) onto crossbars and trains the embedding model to survive variation. The transferable idea is that embedding/retrieval workloads are a natural fit for noisy analog MVM when representations are trained for margin. Evidence is simulation with measured-device noise parameters, limited to MIPS accuracy.

## Cites (in collection, 3)
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "Temporal variations are typically independent from device to device and are irrelevant to the value to be programmed [20]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _data/numbers_: "The specific parameters are abstracted and then simplified from three representative NVM devices, two of them are resistive random-access memory (RRAM) devices extracted from [27, 41] and the other is a ferroelectric field effect transistor (FeFET) device extracted from [42]."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _data/numbers_: "Given the same amount of documents, CiM can finish computation within 50ms [15], which is negligible compared to the computation latency on normal edge devices."

## Cited by (in collection, 1)
- [2025_Qin_NVCiMPT_DATE](2025_Qin_NVCiMPT_DATE.md) NVCiM-PT (2025) — _background_: "Under the constraint of memory capacity and computational power on edge devices, existing works mainly take two types of approaches to enable LLM learning on edge: retrieval-augmented generation (RAG) [8] and low-rank adaption (LoRA) [9]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2024_Qin_RoCR_ICCAD.pdf](../../11_Small_Language_Models_on_AIMC/2024_Qin_RoCR_ICCAD.pdf)
- Full text: [../fulltext/2024_Qin_RoCR_ICCAD.txt](../fulltext/2024_Qin_RoCR_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3676536.3676674
