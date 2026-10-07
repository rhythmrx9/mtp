---
id: W3209892756
key: 2021_Kang_WindowSelfAttentionReRAM_TCAD
title: "A Framework for Accelerating Transformer-Based Language Model on ReRAM-Based Architecture"
short: "Window Self-Attention ReRAM"
year: 2021
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Myeonggu Kang, Hyein Shin, Lee‐Sup Kim"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["transformer-accelerator", "attention", "dataflow-pipelining", "language-models", "scheduling"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 5
citations_overall: 28
priority_score: 8.95
doi: "https://doi.org/10.1109/tcad.2021.3121264"
pdf: null
fulltext: null
---

# Window Self-Attention ReRAM

**A Framework for Accelerating Transformer-Based Language Model on ReRAM-Based Architecture** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes window self-attention plus a window-size search algorithm to resolve the pipeline-hazard bottleneck of running transformer-based language models on ReRAM in-situ accelerators, reporting up to 39.2x speedup and 643.2x energy efficiency over GPU.

## Summary
Transformer-based language models are increasingly the de-facto NLP workload, but running them on ReRAM-based in-situ compute accelerators (which help avoid the memory wall) creates a pipeline hazard: the self-attention mechanism's data dependencies stall the ReRAM accelerator's processing pipeline, inflating execution time. The authors analyze the properties of self-attention and propose 'window self-attention,' which restricts the computation scope of attention to a window around each token to reduce the dependency chain that causes the hazard. They then design a window-size search algorithm that selects window sizes per layer/head to balance the target application's accuracy/performance against hazard reduction. A hardware design is proposed to exploit this algorithmic optimization on a general ReRAM-based accelerator template. The approach is reported to deliver a 5.8x speedup over a provisioned (un-optimized) ReRAM baseline, and up to 39.2x speedup / 643.2x energy efficiency over GPU execution of the same transformer language models.

## Contributions
- Identification and analysis of a pipeline-hazard problem specific to running self-attention on ReRAM-based in-situ accelerators
- Window self-attention: an algorithmic restriction of attention computation scope designed to reduce the hazard-causing data-dependency chain
- A window-size search algorithm that selects per-layer/head window sizes to trade off algorithmic (accuracy) performance against hardware hazard mitigation
- A ReRAM accelerator hardware design that exploits the window self-attention optimization
- Reported large speedups (5.8x over baseline ReRAM accelerator; up to 39.2x/643.2x over GPU in speed/energy efficiency)

## Key claims (stable IDs)
- **2021_Kang_WindowSelfAttentionReRAM_TCAD#C1** — Window self-attention combined with the proposed hardware design resolves the pipeline hazard while maintaining algorithmic performance, giving a 5.8x speedup over the provisioned (non-optimized) ReRAM baseline. — _support:_ 5.8x speedup over provisioned baseline (abstract) — _loc:_ Abstract
- **2021_Kang_WindowSelfAttentionReRAM_TCAD#C2** — The proposed framework delivers up to 39.2x speedup and 643.2x higher energy efficiency versus GPU. — _support:_ up to 39.2x / 643.2x speedup/energy-efficiency over GPU (abstract) — _loc:_ Abstract

## Results
- 5.8x speedup over the provisioned (hazard-unmitigated) ReRAM baseline accelerator (abstract)
- Up to 39.2x speedup and up to 643.2x higher energy efficiency vs. GPU (abstract; exact GPU model and benchmark set not verifiable from abstract alone)

## Limitations
- Full text was not accessible (IEEE TCAD paywalled; no legitimate open preprint found); this entry is based on abstract and metadata only, so details of the window-size search algorithm, hardware microarchitecture, and benchmark/accuracy trade-offs could not be verified
- Windowed/local attention is a lossy approximation of full self-attention; the accuracy impact across different transformer model sizes and tasks is not quantifiable from the abstract

## Remarks
This is one of the earlier works specifically targeting the transformer self-attention bottleneck on ReRAM crossbar accelerators (alongside ReTransformer), framing the problem as a pipeline-hazard issue rather than purely an ADC/crossbar-capacity issue, and addressing it with an algorithm-hardware co-design (sparsity-like windowing) rather than new device technology. Later in-set citing works (e.g., CPSAA, HARDSEA, ETA) continue this line of attention-sparsification/scheduling for ReRAM transformer acceleration, suggesting the hazard problem identified here remained an active research target. Because the full text was unavailable, the magnitude and robustness of the reported speedups (particularly the 643.2x energy-efficiency figure) should be treated as a headline claim pending verification against baseline and benchmark details.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 13)
- [2023_Cao_RRAMPoolFormer_ISCAS](2023_Cao_RRAMPoolFormer_ISCAS.md) RRAM-PoolFormer (2023) — _background_: "The implementations of Transformer structure on memristor crossbar array have been reported in literature [23]."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _baseline/comparison_: "These solutions use high parallel ReRAM arrays to significantly reduce the latency of DDMM operations [11, 36]."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _baseline/comparison_: "We evaluate the inference performance and the energy efficiency for different Transformer models, and compare ReCAT with two state-of-the-art ReRAM-based PIM architectures designed for Transformer networks–ReTransformer [50] and ReBert [23]."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "Similarly, another work introduces a hardware-software co-design framework for transformer acceleration on ReRAM-based architecture [23]."
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _contrasts/critiques_: "Some approaches [24, 25] reduce on-chip memory occupancy of partial feature vectors by confining attention windows or blocks. However, this comes at the sacrifice of the model’s accuracy."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _contrasts/critiques_: "For example, designs like iMCAT [19], ATT [21], ReBERT [22], iMTransformer [24], and X-Former [25] focus on smaller-scale, encoder-only models such as BERT variants."
- [2026_Xiao_RoboPIM_TCAD](2026_Xiao_RoboPIM_TCAD.md) RoboPIM (2026) — _baseline/comparison_: "We compare RoboPIM with the state-of-the-art design for four typical platform: ... 3) ReBERT [38], a state-of-the-art ReRAM-based accelerator for transformer-based LLMs; and 4) RoboShape [13], a state-of-the-art FPGA accelerator for robotics applications."
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Huang_VQTCiM_DAC](2025_Huang_VQTCiM_DAC.md) VQT-CiM (2025)
- [2025_Xiong_ASMA_ICCD](2025_Xiong_ASMA_ICCD.md) ASMA (2025)
- [2025_Rhe_ETA_APCCAS](2025_Rhe_ETA_APCCAS.md) ETA (2025)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2021_Kang_WindowSelfAttentionReRAM_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2021.3121264
