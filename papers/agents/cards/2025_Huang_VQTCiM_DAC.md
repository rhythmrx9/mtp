---
id: W4414197154
key: 2025_Huang_VQTCiM_DAC
title: "VQT-CiM: Accelerating Vector Quantization Enhanced Transformer with Ferroelectric Compute-in-Memory"
short: "VQT-CiM"
year: 2025
venue: "DAC"
venue_full: "ACM/IEEE Design Automation Conference (DAC 2025)"
authors: "Xuchu Huang, Haonan Du, Min Zhou, Zheyu Yan, Cheng Zhuo, Xunzhao Yin"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["FeFET"]
models: ["Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "macro", "energy-efficiency", "hardware-aware-training"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 4
citations_overall: 3
priority_score: 5.42
doi: "https://doi.org/10.1109/dac63849.2025.11133264"
pdf: null
fulltext: null
---

# VQT-CiM

**VQT-CiM: Accelerating Vector Quantization Enhanced Transformer with Ferroelectric Compute-in-Memory** — ACM/IEEE Design Automation Conference (DAC 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
VQT-CiM is a FeFET-based CiM design that eliminates the runtime write operations dynamic attention VMMs otherwise require, by vector-quantizing keys/values (residual + product VQ) into static codebook VMMs, achieving 3.54x energy efficiency and 4.53x throughput over state-of-the-art NVM CiM transformer designs.

## Summary
The paper targets a specific obstacle to deploying non-volatile-memory (NVM) based compute-in-memory for Transformer self-attention: unlike the static weight matrices of feed-forward/projection layers, the attention mechanism's query-key and attention-weighted-value multiplications are dynamic (data-dependent), requiring runtime writes into the NVM crossbar, which is costly due to high write energy/latency, complex compute-write-compute dependencies, and limited device endurance. VQT-CiM, built on ferroelectric FET (FeFET) CiM crossbars, sidesteps this by applying vector quantization (VQ) to keys and values so that the inner-product and weighted-sum operations inside self-attention become static VMMs against fixed codebooks rather than dynamic per-token VMMs. Because plain VQ would limit representational capacity and hurt accuracy, the authors combine residual VQ (RVQ) and product VQ (PVQ) to expand representation capacity while retaining the static-VMM benefit. They present a hardware implementation with an optimized RVQ dataflow using FeFET CiM crossbars plus digital peripheral circuits, reporting large efficiency gains over prior NVM-based CiM Transformer accelerators.

## Contributions
- Identifies that dynamic (data-dependent) VMMs in Transformer self-attention are a poor fit for NVM-based CiM due to runtime write overhead, compute-write-compute dependencies, and limited endurance
- Proposes converting dynamic attention VMMs into static VMMs by vector-quantizing keys and values, enabling computation against fixed codebooks stored in CiM crossbars
- Introduces a combined residual-VQ + product-VQ (RVQ+PVQ) scheme to recover representational capacity lost to plain vector quantization
- Designs a FeFET-based CiM hardware implementation with an optimized dataflow for the RVQ computation plus digital peripheral circuits
- Reports 3.54x energy efficiency and 4.53x throughput improvement over state-of-the-art NVM-based CiM Transformer designs

## Key claims (stable IDs)
- **2025_Huang_VQTCiM_DAC#C1** — VQT-CiM substantially improves energy efficiency and throughput over prior NVM-based CiM Transformer accelerators by eliminating runtime write operations — _support:_ 3.54x energy efficiency improvement and 4.53x throughput improvement vs. state-of-the-art NVM-based CiM transformer designs — _loc:_ Abstract
- **2025_Huang_VQTCiM_DAC#C2** — Directly applying vector quantization to keys/values would hurt transformer accuracy due to limited representation capacity, motivating the combined RVQ+PVQ scheme — _support:_ Stated rationale in the abstract for introducing the residual+product VQ combination — _loc:_ Abstract

## Results
- 3.54x energy efficiency improvement vs. state-of-the-art NVM-based CiM transformer designs
- 4.53x throughput improvement vs. state-of-the-art NVM-based CiM transformer designs

## Limitations
- Vector quantization of keys/values is inherently an approximation; while RVQ+PVQ is intended to mitigate accuracy loss, the abstract gives no explicit accuracy-retention numbers
- Evaluation basis (simulation vs. measured FeFET devices) and which Transformer models/datasets were tested are not specified in the abstract
- Comparisons are against other NVM-based CiM transformer designs rather than GPU or SRAM-CiM baselines, which may understate or overstate relative gains depending on what is being targeted

## Remarks
This is a device/algorithm co-design approach to a well-known problem in CiM Transformer acceleration (dynamic attention VMMs vs. static-weight-friendly crossbars), using vector quantization as the bridge rather than analog-domain tricks or hybrid digital-SRAM designs (as in HARDSEA) or sparsity (as in CPSAA). The RVQ+PVQ combination is a sensible way to recover capacity, but the practical accuracy impact on real transformer benchmarks is the key open question that the abstract does not answer; the full paper should be checked for accuracy-vs-baseline numbers before citing this as an accuracy-neutral solution.

## Cites (in collection, 4)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2025_Huang_VQTCiM_DAC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/dac63849.2025.11133264
