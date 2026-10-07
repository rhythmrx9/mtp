---
id: W4390017976
key: 2023_Liu_HARDSEA_TVLSI
title: "HARDSEA: Hybrid Analog-ReRAM Clustering and Digital-SRAM In-Memory Computing Accelerator for Dynamic Sparse Self-Attention in Transformer"
short: "HARDSEA"
year: 2023
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems"
authors: "Shiwei Liu, Chen Mu, Hao Jiang, Yunzhengmao Wang, Jinshan Zhang, Feng Lin, Keji Zhou, Qi Liu, Chixiao Chen"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-analog"]
models: ["Transformer", "BERT", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["heterogeneous-analog-digital", "attention", "transformer-accelerator", "pruning-sparsity", "3d-integration"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 16
cites_in_collection: 5
citations_overall: 38
priority_score: 9.3
doi: "https://doi.org/10.1109/tvlsi.2023.3337777"
pdf: null
fulltext: null
---

# HARDSEA

**HARDSEA: Hybrid Analog-ReRAM Clustering and Digital-SRAM In-Memory Computing Accelerator for Dynamic Sparse Self-Attention in Transformer** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
HARDSEA is a hybrid analog-ReRAM/digital-SRAM compute-in-memory accelerator for dynamic sparse self-attention in transformers, using product-quantization-based token-relevance prediction on noise-tolerant ReRAM and exact sparse computation on reorganized SRAM-CIM, reporting 13.5x-28.5x speedup and 291.6x-1894.3x energy efficiency over GPU.

## Summary
The paper targets the quadratic cost of self-attention in transformers (BERT, GPT-2) by exploiting dynamic sparsity while coping with the fact that analog ReRAM-CIM is noisy/imprecise but digital SRAM-CIM is precise but less energy-efficient. HARDSEA performs algorithm-architecture-circuit co-design: a product-quantization-based scheme predicts lightweight token relevance to dynamically determine which attention entries are important, exploiting the fact that only the relative ordering (monotonicity), not exact values, of relevance scores is needed -- a task well suited to noise-tolerant analog ReRAM-CIM. The exact (precision-sensitive) sparse attention computation is then performed on a digital SRAM-CIM array reorganized with an 'on-memory-boundary computing' scheme to flexibly handle the resulting irregular sparsity patterns. To avoid the area/energy cost of ADCs for the relevance-prediction ReRAM macro, the authors propose a time-domain winner-take-all (WTA) circuit that directly produces the needed ranking without full analog-to-digital conversion. Evaluated on BERT and GPT-2, HARDSEA prunes attention to 12%-33% sparsity without accuracy loss and achieves large speedup/energy-efficiency gains over GPU and over prior transformer accelerators.

## Contributions
- Algorithm-architecture-circuit co-design combining a product-quantization-based dynamic token-relevance predictor with a hybrid analog/digital CIM architecture
- Uses noise-tolerant analog ReRAM-CIM specifically for the relevance-prediction sub-task, which only needs correct ranking (monotonicity) rather than exact values, sidestepping ReRAM's precision limitations
- Reorganizes digital SRAM-CIM with an 'on-memory-boundary computing' scheme to handle irregular sparse attention access patterns efficiently
- Proposes a time-domain winner-take-all (WTA) circuit that replaces conventional ADCs in the ReRAM-CIM relevance-prediction macro, reducing peripheral circuit cost
- Demonstrates pruning BERT and GPT-2 self-attention to 12%-33% sparsity with no accuracy loss

## Key claims (stable IDs)
- **2023_Liu_HARDSEA_TVLSI#C1** — HARDSEA prunes BERT and GPT-2 attention to 12%-33% sparsity without accuracy loss. — _support:_ sparsity range reported in abstract/experiments — _loc:_ Experimental results section
- **2023_Liu_HARDSEA_TVLSI#C2** — HARDSEA achieves 13.5x-28.5x speedup over GPU. — _support:_ reported speedup range vs GPU baseline — _loc:_ Experimental results section
- **2023_Liu_HARDSEA_TVLSI#C3** — HARDSEA achieves 291.6x-1894.3x energy efficiency over GPU. — _support:_ reported energy-efficiency range vs GPU baseline — _loc:_ Experimental results section
- **2023_Liu_HARDSEA_TVLSI#C4** — HARDSEA achieves 1.2x-14.9x better energy efficiency than state-of-the-art transformer accelerators at the same throughput level. — _support:_ comparison against prior transformer accelerators (e.g., ReRAM-based attention accelerators) — _loc:_ Experimental results / comparison section
- **2023_Liu_HARDSEA_TVLSI#C5** — Replacing ADCs with a time-domain winner-take-all circuit in the ReRAM-CIM relevance-prediction macro is sufficient because only ranking information, not exact magnitude, is required downstream. — _support:_ circuit design rationale tied to the algorithm's use of relevance ranking only — _loc:_ Architecture/circuit design section

## Results
- 12%-33% self-attention sparsity on BERT/GPT-2 with no accuracy loss
- 13.5x-28.5x speedup vs GPU
- 291.6x-1894.3x energy efficiency vs GPU
- 1.2x-14.9x better energy efficiency than state-of-the-art transformer accelerators at equal throughput

## Limitations
- Full text not available for this analysis; all quantitative results above are taken from the abstract only and not independently checked against tables/figures
- ReRAM is used only for the noise-tolerant ranking/prediction sub-task, implying the authors judged ReRAM-CIM unsuitable for exact sparse-attention computation, which still has to run on digital SRAM-CIM -- i.e., analog compute coverage of the workload is partial
- Based on the abstract alone, it is unclear whether the reported numbers are from post-layout simulation, pure architectural simulation, or measured silicon

## Remarks
HARDSEA is a notable hybrid-analog/digital design pattern for transformer attention acceleration in the analog-CIM literature: rather than trying to make ReRAM compute attention scores exactly, it restricts analog compute to tasks that are inherently robust to noise (ranking/relevance prediction) while keeping exact computation digital. This hybrid strategy (and the ADC-avoiding time-domain WTA circuit) is a useful mapping/architecture pattern to compare against pure-ReRAM transformer accelerators (e.g., CPSAA, X-Former) in a mapping-focused thesis chapter. Because only the abstract was available, the specific experimental setup (baseline GPU model, precision assumptions, device variation modeling) could not be verified and should be checked against the full TVLSI 2023 paper before citing specific numbers.

## Cites (in collection, 5)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022)
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023)

## Cited by (in collection, 16)
- [2025_Dong_TopkimaFormer_TCAS-I](2025_Dong_TopkimaFormer_TCAS-I.md) Topkima-Former (2025) — _baseline/comparison_: "Compared to ELSA [22], ReTransformer [1], X-Former [4] and HARDSEA [23], Topkima-Former can achieve 1.8x-84x higher speed, and 1.3x-35x energy reduction, respectively."
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _contrasts/critiques_: "Alternative methods such as SPRINT [20] and HARDSEA [21] leverage dynamic sparse attention features to reduce ineffective computations."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _uses-method-or-tool_: "Hence, for transformer models, the self-attention is deployed on digital tiles or digital cores [9], [18], [20]."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _contrasts/critiques_: "KV cache has been implemented either by dynamic random-access memories (DRAMs)21,23, which have limited parallelism requiring many digital sequential adders, or by SRAMs19,24, which are limited by their volatility and relatively low density25."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _baseline/comparison_: "Prior research on heterogeneous-CIM-based Transformer accelerators aims to reduce computation amounts of DMM through algorithm co-design [8, 14, 15]."
- [2025_Malhotra_ReTern_TVLSI](2025_Malhotra_ReTern_TVLSI.md) ReTern (2025) — _background_: "Various CiM-based LLM accelerators have been proposed, showcasing sizeable benefits over conventional von-Neumann based platforms such as GPUs [2]-[5]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _baseline/comparison_: "In this work, we compare our approach with HARDSEA [26] and TransPIM [18]."
- [2026_Zheng_InterfaceKVQ_ICCAD](2026_Zheng_InterfaceKVQ_ICCAD.md) InterfaceKVQ (2026) — _contrasts/critiques_: "HARDSEA [12] prescreens token relevance in analog ReRAM and computes the exact sparse attention in digital SRAMCiM, with 8-bit keys and values in volatile SRAM."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _contrasts/critiques_: "Similarly, HARDSEA [32] utilizes analog RRAM PIM solely to predict token relevance."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "Among them, RRAM-SRAM hybrid architectures have attracted significant attention by combining the high energy efficiency of RRAM with accurate computation of SRAM [1, 54–56]."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _contrasts/critiques_: "In addition, although HARDSEA [34] and other methods can skip zero values, the array utilization is low."
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Huang_VQTCiM_DAC](2025_Huang_VQTCiM_DAC.md) VQT-CiM (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Xiong_ASMA_ICCD](2025_Xiong_ASMA_ICCD.md) ASMA (2025)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2023_Liu_HARDSEA_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2023.3337777
