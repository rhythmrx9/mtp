---
id: W4411486499
key: 2025_Song_HyFlexPIM_ISCA
title: "Hybrid SLC-MLC RRAM Mixed-Signal Processing-in-Memory Architecture for Transformer Acceleration via Gradient Redistribution"
short: "HyFlexPIM"
year: 2025
venue: "ISCA"
venue_full: "ACM/IEEE 52nd Annual International Symposium on Computer Architecture (ISCA 2025)"
authors: "Chang Eun Song, Priyansh Bhatnagar, Zihan Xia, Nam Sung Kim, Tajana Rosing, Mingu Kang"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "SRAM-digital"]
models: ["Transformer", "BERT", "GPT/LLM", "ViT"]
lm_models: ["BERT-Base", "BERT-Large", "GPT-2 (small)", "Llama-3.2-1B"]
param_scale: "110M-1.2B"
slm: true
evidence: algorithm+simulation
topics: ["transformer-accelerator", "heterogeneous-analog-digital", "mixed-precision", "noise-injection", "weight-mapping", "pruning-sparsity", "adc-dac", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 12
citations_overall: 4
priority_score: 8.49
doi: "https://doi.org/10.1145/3695053.3731109"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Song_HyFlexPIM_ISCA.pdf"
fulltext: "../fulltext/2025_Song_HyFlexPIM_ISCA.txt"
---

# HyFlexPIM

**Hybrid SLC-MLC RRAM Mixed-Signal Processing-in-Memory Architecture for Transformer Acceleration via Gradient Redistribution** — ACM/IEEE 52nd Annual International Symposium on Computer Architecture (ISCA 2025) (2025)

## TL;DR
HyFlexPIM maps static transformer weights onto reconfigurable SLC/2-bit-MLC analog RRAM (digital PIM for dynamic attention) and uses SVD-based gradient redistribution so only 5-20% of weights need protective SLC, giving up to 1.86x speedup and 1.24x linear-layer energy efficiency over ASADI with <1% accuracy loss on encoders.

## Summary
Analog RRAM PIM gives large efficiency gains for transformers but is noisy; most prior works use SLC only, wasting MLC density, while naive hybrid mapping leaves too little weight mass in MLC. HyFlexPIM is mixed-signal: static linear-layer weights (QKV, output projection, FFN) go to analog RRAM modules (64x128 arrays, 1-bit or 2-bit cells, 1-bit wordline drivers, reconfigurable 6/7-bit ADC) that can switch SLC/MLC with <1% area and energy overhead; dynamic operands (QK^T, attention-V, which need frequent writes) and high-precision operations run on digital RRAM PIM (NOR-logic) and a special function unit. 2-bit MLC was chosen because measured RRAM chips show 3/4-bit MLC has 7x higher bit error rate than SLC. On the software side, weights are SVD-decomposed (W = U Sigma V^T), truncated, hard-thresholded and fine-tuned so loss gradients concentrate on a small subset of singular components; the top-k% by absolute gradient are stored in SLC and the rest in MLC. Accuracy is evaluated with circuit-level error models from measured MLC RRAM chips on BERT-Base/Large (GLUE), GPT-2 (WikiText-2), Llama-3.2-1B (PTB) and ViT-Base (CIFAR-10); energy/latency simulated at 1 GHz with Cadence Genus synthesis for digital parts against ASADI, SPRINT, NMP and a non-PIM baseline.

## Language models evaluated
- Models: BERT-Base, BERT-Large, GPT-2 (small), Llama-3.2-1B
- Scale: 110M-1.2B
- Note: BERT-Base/Large, GPT-2 small, Llama-3.2-1B (and ViT-Base) evaluated with simulated hybrid SLC/MLC RRAM analog+digital PIM noise and 65 nm energy/latency models; all SLM-scale.

## Contributions
- Mixed-signal hybrid SLC-MLC RRAM PIM architecture with reconfigurable ADC
- Gradient redistribution (SVD truncation + fine-tuning) to concentrate sensitivity into 5-10% (encoder) / 5-20% (decoder) of weights
- Accuracy analysis with realistic RRAM error models on encoder, decoder and vision transformers
- Comparison with ASADI, SPRINT and near-memory baselines

## Key claims (stable IDs)
- **2025_Song_HyFlexPIM_ISCA#C1** — Up to 1.86x throughput and 1.24x linear-layer energy efficiency over ASADI — _support:_ ASADI uses SLC only with token pruning — _loc:_ Sec. 1, Fig. 14-16
- **2025_Song_HyFlexPIM_ISCA#C2** — 5% SLC rate keeps BERT-Base accuracy within 1% of the INT8 baseline on MRPC/QNLI/STS-B; 10-30% needed for CoLA/QQP/SST-2/RTE — _support:_ Fig. 12(a) — _loc:_ Sec. 6.1
- **2025_Song_HyFlexPIM_ISCA#C3** — 20% SLC keeps GPT-2 and Llama-3.2-1B loss increase under 10% vs 100% SLC — _support:_ WikiText-2 / PTB loss — _loc:_ Sec. 6.1, Fig. 12(b)
- **2025_Song_HyFlexPIM_ISCA#C4** — Gradient-based protection beats weight-magnitude and rank-based selection — _support:_ BERT-Base MRPC and CoLA — _loc:_ Fig. 13

## Results
- Vs SPRINT: up to 5.4x linear-layer energy reduction, 4.94x/4.69x end-to-end energy efficiency (GLUE/WikiText-2), 10.6x/46x speedup at N=128
- Average at 20% SLC: 5.34x linear-layer energy reduction and 10.1x/44x speedup vs SPRINT on GLUE/WikiText-2
- Vs NMP baseline: up to 3.31x linear energy efficiency
- ViT-Base on CIFAR-10 needs only 5% SLC for <1% accuracy drop
- ADC takes 64.2% of analog-module area and 55% of power (Table 2)

## Key numbers
- array_size: 64x128 analog RRAM arrays
- energy_eff: 1.24x vs ASADI (linear layers); 5.4x vs SPRINT
- throughput: 1.86x vs ASADI; 10.1x/44x vs SPRINT
- accuracy: <1% loss encoder/ViT at 5-30% SLC; <10% loss increase decoder at 20% SLC
- bits_weight: INT8, 1b SLC / 2b MLC cells
- bits_adc: 6b/7b

## Datasets / benchmarks
GLUE (7 tasks), WikiText-2, PTB, CIFAR-10

## Limitations
- Simulation with error models; no fabricated chip
- Dynamic attention operands run on digital PIM, limiting analog fraction and costing writes/endurance
- Noise model derived from measured MLC chips but static (no drift or temperature)
- Decoder LLM evaluated only at 1B with loss increase (<10%) rather than task accuracy
- Abstract and introduction quote different energy gains (1.45x vs 1.24x)

## Remarks
Strong co-design paper in which the model is reshaped to be analog-friendly rather than relying on passive noise tolerance; the SVD gradient redistribution gives an explicit demarcation of critical weights. Evidence is simulation only but with measured-chip error models and includes a 1B decoder, making it one of the more directly SLM-relevant architecture papers.

## Cites (in collection, 12)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Out of these efforts, RRAM is one of the most widely explored devices for PIM acceleration due to its non-volatile memory (NVM) nature, high storage density, fast read operation, low energy consumption, and excellent analog programmability for the multi-level cell (MLC) [23, 42, 46, 58, 60, 74, 78, 80]."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _background_: "Digital PIM, which has been extensively studied [22, 31, 72], achieves data movement reduction with reliable computation through simple bit-wise operations (e.g., NOR, INV, and others) but suffers from limited parallelism compared to analog PIM."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "As an alternative solution, memory-centric processing architectures have been emerging, specifically processing-in-memory (PIM) [48, 74, 80]."
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020) — _data/numbers_: "The noise level was derived from the studies by Wan et al. [61] and Fan et al. [15], utilizing the non-idealities measured from the fabricated real MLC RRAM chips."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _contrasts/critiques_: "However, it has shown limited improvement due to less parallelism in General matrix-vector multiplications (GEMV) operations than analog PIMs [72], falling short of fully leveraging the substantial potential for energy and delay efficiency offered by lowswing analog operations."
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021) — _data/numbers_: "Specifically, the RRAM features an on-state resistance (RON) of 6 kΩ with an on/off ratio of 150 [77]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "The pioneering works, ISAAC [50] and [20] demonstrate a pipelined RRAM crossbar and hybrid RRAM capable of efficiently executing CNNs."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "PRIME [11] introduces a reconfigurable RRAM PIM architecture, where the same PIM hardware can be configured as both regular memory and computing elements."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _contrasts/critiques_: "Due to these accuracy concerns, a large body of work [32, 68, 79] has explored digital PIM solutions for processing Transformers while reducing data movement costs."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _background_: "In particular, both digital and analog PIM approaches have shown significant efficiency improvements - digital PIM reduces data movement costs while maintaining the accuracy for high bit-precision operations [16, 24, 32, 58, 60, 68, 79], and analog PIM demonstrates dramatic efficiency improvement, achieving more than two orders of magnitude benefit [5, 9, 17, 24] through low-voltage swing operations."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _background_: "In particular, both digital and analog PIM approaches have shown significant efficiency improvements - digital PIM reduces data movement costs while maintaining the accuracy for high bit-precision operations [16, 24, 32, 58, 60, 68, 79], and analog PIM demonstrates dramatic efficiency improvement, achieving more than two orders of magnitude benefit [5, 9, 17, 24] through low-voltage swing operations."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _contrasts/critiques_: "Similarly, HARDSEA [32] utilizes analog RRAM PIM solely to predict token relevance."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Song_HyFlexPIM_ISCA.pdf](../../11_Small_Language_Models_on_AIMC/2025_Song_HyFlexPIM_ISCA.pdf)
- Full text: [../fulltext/2025_Song_HyFlexPIM_ISCA.txt](../fulltext/2025_Song_HyFlexPIM_ISCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3695053.3731109
