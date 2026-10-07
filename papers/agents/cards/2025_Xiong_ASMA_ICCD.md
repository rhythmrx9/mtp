---
id: W7117549365
key: 2025_Xiong_ASMA_ICCD
title: "ASMA: An Anisotropy Scaling Memristor-Based Accelerator for LLM Inference"
short: "ASMA"
year: 2025
venue: "ICCD"
venue_full: "IEEE International Conference on Computer Design (ICCD 2025)"
authors: "Zijian Xiong, Xiangrui Yang, Yuhang Zhang, Yue Zhou, Jianguo Yang, Yaoyu Tao, Xiangshui Miao, Yu He"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["Memristor(generic)"]
models: ["Transformer", "GPT/LLM"]
lm_models: []
param_scale: "not specified"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "language-models", "weight-mapping", "energy-efficiency", "hardware-aware-training"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/iccd65941.2025.00086"
pdf: null
fulltext: null
---

# ASMA

**ASMA: An Anisotropy Scaling Memristor-Based Accelerator for LLM Inference** — IEEE International Conference on Computer Design (ICCD 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ASMA is a memristor-based CIM accelerator for LLM FFN layers that exploits the 'anisotropic' (additive/concatenative/sequential) scaling structure of LLM computations, using a Subtile hierarchy, a hierarchical anisotropic NoC, and a co-designed compiler to cut communication overhead versus isotropic CIM designs, reporting up to 81.7% latency and 91.5% energy improvement in a transaction-level simulator.

## Summary
The paper argues that naively scaling isotropic (uniform) CIM architectures to handle LLM feed-forward network (FFN) layers introduces severe new communication overheads, because LLM FFN computations actually scale anisotropically along different dimensions (categorized as additive, concatenative, and sequential). ASMA is proposed as an Anisotropy Scaling Memristor-based Accelerator that is co-designed around this observation: it introduces a Subtile hierarchy for optimized pipelining, a hierarchical anisotropic Network-on-Chip with distinct channels for broadcast versus localized communication, and a co-designed compiler that maps LLM computations onto the architecture by exploiting these anisotropic scaling characteristics. Evaluation with a transaction-level simulator shows latency improvements up to 81.7% and energy improvements up to 91.5% versus conventional hierarchical CIM designs, which the authors frame as a new design paradigm for LLM-specific CIM accelerators that embrace rather than ignore workload anisotropy.

## Language models evaluated
- Models: —
- Scale: not specified
- Note: Only the abstract was available; it names no specific LLMs or scales, targeting memristor CIM accelerator for LLM FFN layers.

## Contributions
- Identifies and categorizes LLM FFN layer scaling as anisotropic (additive, concatenative, sequential dimensions), unlike the isotropic assumption in prior CIM designs
- Subtile hierarchy for optimized pipelining matched to this anisotropic structure
- Hierarchical anisotropic Network-on-Chip with distinct broadcast and localized-communication channels
- Co-designed compiler that maps LLM computation onto the anisotropic architecture
- Transaction-level simulator evaluation showing large latency/energy gains over conventional hierarchical CIM

## Key claims (stable IDs)
- **2025_Xiong_ASMA_ICCD#C1** — ASMA substantially reduces latency versus conventional hierarchical CIM designs by exploiting workload anisotropy — _support:_ Abstract: 'latency improvement up to 81.7% ... compared to conventional hierarchical CIM designs' — _loc:_ Abstract
- **2025_Xiong_ASMA_ICCD#C2** — ASMA substantially reduces energy versus conventional hierarchical CIM designs — _support:_ Abstract: 'energy improvement up to 91.5% compared to conventional hierarchical CIM designs' — _loc:_ Abstract

## Results
- Up to 81.7% latency improvement vs. conventional hierarchical CIM designs
- Up to 91.5% energy improvement vs. conventional hierarchical CIM designs

## Limitations
- Full text not accessible to this reviewer (ICCD is not downloadable here and no arXiv preprint was found); exact baselines, benchmarked LLMs, and simulator assumptions could not be verified beyond the abstract
- Evidence basis is a transaction-level simulator, not measured silicon or cycle-accurate hardware emulation

## Remarks
Abstract-only assessment: ICCD proceedings are not downloadable here and no preprint was found. The anisotropy framing (additive/concatenative/sequential scaling of FFN dimensions) is a genuinely architecture-relevant observation for mapping LLM FFN layers onto tiled memristor CIM systems, distinguishing this from CNN-era CIM accelerators that assumed more uniform/isotropic tiling; the claimed 80-90%+ improvements are large and would need the full paper's baseline definitions to assess credibility.

## Cites (in collection, 6)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2025_Xiong_ASMA_ICCD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccd65941.2025.00086
