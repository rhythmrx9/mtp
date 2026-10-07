---
id: W7162404347
key: 2026_Vasilopoulos_AIMCforLLMInference_IMW
title: "Analog In-Memory Computing for Large Language Model Inference: Opportunities and Challenges"
short: "AIMC for LLM Inference (IMW 2026)"
year: 2026
venue: "IMW"
venue_full: "IEEE International Memory Workshop (IMW 2026)"
authors: "A. Vasilopoulos, H. Benmeziane, J. Büchel, W. Simon, A. Singh, I. Boybat, J. Luquin, P. Narayanan, H. Tsai, G. W. Burr, A. Rahimi, M. Le Gallo et al."
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM", "ReRAM", "MRAM", "Flash", "SRAM-analog", "Gain-cell", "Generic-NVM"]
models: ["Transformer", "GPT/LLM", "MoE"]
lm_models: []
param_scale: "not specified"
slm: false
evidence: analytical
topics: ["language-models", "heterogeneous-analog-digital", "kv-cache", "attention", "3d-integration", "hardware-aware-training", "moe", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 0
priority_score: 6.0
doi: "https://doi.org/10.1109/imw68301.2026.11532624"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Vasilopoulos_AIMCforLLMInference_IMW.pdf"
fulltext: "../fulltext/2026_Vasilopoulos_AIMCforLLMInference_IMW.txt"
---

# AIMC for LLM Inference (IMW 2026)

**Analog In-Memory Computing for Large Language Model Inference: Opportunities and Challenges** — IEEE International Memory Workshop (IMW 2026) (2026)

## TL;DR
Perspective from IBM Research arguing that AIMC suits the static, high-reuse MVMs of LLMs (weights programmed once in dense, 3D NVM) but its system benefit shrinks with sequence length because dynamic attention/KV-cache work cannot be pre-programmed, so AIMC should be a co-processor in heterogeneous analog+digital inference systems.

## Summary
The paper decomposes modern LLMs (Transformers, MoE, SSM/hybrid such as Mamba-2) into static parameterised MVMs (input/output projections, FFN, MoE experts, LM head) and dynamic sequence-dependent operations (attention with KV-cache, SSM state updates). It reviews AIMC progress: volatile SRAM (charge/voltage-domain) and gain-cell designs are flexible but density-limited and need weight reloading, while NVM AIMC (PCM, RRAM, MRAM, Flash) offers high density but asymmetric read/write cost (iterative read-write-verify programming), hence weight-stationary use. Static MVMs map to NVM AIMC (weights programmed once, reused across tokens and users); dynamic attention does not, since operands depend on the sequence and the KV-cache has little reuse. Profiling on 8 NVIDIA A100 GPUs (Fig. 4) shows the static-computation fraction falling with sequence length. Opportunities: 3D NVM density scaling (3D NAND) with multi-tier mapping acting as cheap weight reload (prior work: up to 3 orders of magnitude energy gain for MoE LLMs), noise handled by analog hardware-aware training and post-training adaptation (Analog Foundation Models, NORA), and decoupled heterogeneous systems in which AIMC stores/executes static weights while digital accelerators handle attention and KV-cache (edge: lightweight digital processor; data center: shared statically programmed weights). The paper reports no new experiments beyond the profiling figure.

## Language models evaluated
- Models: —
- Scale: not specified
- Note: Perspective paper on AIMC for LLM inference; names no specific models or scales.

## Contributions
- Static-versus-dynamic decomposition of LLM and SSM workloads and its mapping to volatile vs non-volatile AIMC
- Argument that accuracy is not the fundamental barrier (hardware-aware training / post-training adaptation) while attention/KV-cache limits system-level benefit
- Proposal of decoupled heterogeneous analog (static weights) plus digital (attention, KV-cache) systems for edge and data-center deployments
- Discussion of 3D NVM density scaling as a way to host large models with minimal weight movement

## Key claims (stable IDs)
- **2026_Vasilopoulos_AIMCforLLMInference_IMW#C1** — LLM inference splits into static high-reuse MVMs (suited to NVM AIMC) and dynamic sequence-dependent operations (attention, SSM updates) that are poorly suited to AIMC — _support:_ KV-cache has limited reuse and grows with sequence length; NVM programming is slow and energy-hungry — _loc:_ Sec. III, Fig. 1
- **2026_Vasilopoulos_AIMCforLLMInference_IMW#C2** — The fraction of computation that AIMC can accelerate decreases with sequence length — _support:_ latency profiling on 8 A100 GPUs for representative LLMs — _loc:_ Sec. IV, Fig. 4
- **2026_Vasilopoulos_AIMCforLLMInference_IMW#C3** — 3D AIMC can give up to 3 orders of magnitude energy-efficiency gains for MoE LLM inference — _support:_ cited prior study [22] — _loc:_ Sec. IV
- **2026_Vasilopoulos_AIMCforLLMInference_IMW#C4** — Analog hardware-aware training and post-training adaptation can mitigate noise, so accuracy is not the fundamental barrier — _support:_ cites Analog Foundation Models [23] and NORA [24] — _loc:_ Sec. IV
- **2026_Vasilopoulos_AIMCforLLMInference_IMW#C5** — AIMC is unlikely to be a standalone LLM solution; it should be a specialised co-processor in heterogeneous systems — _support:_ decoupled analog/digital architecture for edge and data center — _loc:_ Sec. IV-V

## Results
- No new quantitative hardware results; one profiling figure (Fig. 4) showing static-compute fraction declining with sequence length
- Cites up to 3 orders of magnitude energy gain for MoE LLMs on 3D AIMC (from [22])
- Fig. 3 shows NVM density scaling driven by 3D NAND and multi-level cells

## Key numbers
- energy_eff: up to 3 orders of magnitude (MoE, 3D AIMC, cited)

## Limitations
- Perspective paper: claims rely on cited prior work rather than new experiments; only one GPU-profiling figure
- No quantitative co-design analysis of the proposed heterogeneous analog+digital system
- Does not provide numbers for accuracy of specific LLMs on analog hardware or for 3D tile compute density (3D increases capacity, not TOPS/mm2)
- SSM/Mamba discussion is qualitative

## Remarks
Concise, current roadmap from the IBM Zurich/Almaden group that states clearly why attention and the KV-cache, not accuracy, are the central obstacle for LLM-on-AIMC, and justifies the weight-stationary + digital attention split used by most papers in this collection (Analog Foundation Models, NORA, MoE 3D AIMC). Since it contains no new results, treat it as framing rather than evidence. Particularly relevant to small language models at the edge where short sequences keep the static fraction high.

## Cites (in collection, 10)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "A wide range of devices have been explored for AIMC, including phasechange memory (PCM) [13], [14], resistive random-access memory (RRAM) [15], magnetoresistive random-access memory (MRAM) [16], and Flash [17], [18], showing promising results in terms of compute density and efficiency."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "A wide range of devices have been explored for AIMC, including phasechange memory (PCM) [13], [14], resistive random-access memory (RRAM) [15], magnetoresistive random-access memory (MRAM) [16], and Flash [17], [18], showing promising results in terms of compute density and efficiency."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "A wide range of devices have been explored for AIMC, including phasechange memory (PCM) [13], [14], resistive random-access memory (RRAM) [15], magnetoresistive random-access memory (MRAM) [16], and Flash [17], [18], showing promising results in terms of compute density and efficiency."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _data/numbers_: "In [22], we studied LLMs inference on 3D AIMC hardware and observed significant energy efficiency improvements, especially for MoE-based architectures – up to 3 orders of magnitude– which can exploit increased capacity without proportionally increasing computation."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _extends/builds-on_: "In recent works, we have shown that analog hardware-aware training [23] and posttraining adaptation [24] can effectively mitigate these effects, suggesting that accuracy is not the fundamental barrier to deploying AIMC for LLM inference."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _motivation_: "In contrast, the dynamic components of LLM inference pose significant challenges for AIMC [21]."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _background_: "Emerging alternatives such as gain-cell-based designs aim to improve density relative to SRAM while retaining the flexibility of reprogramming, but remain at an early stage of development and have not yet demonstrated large-scale AIMC systems [11]."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _background_: "This makes them a natural fit for NVM-based AIMC, where weights can be programmed once and reused across many inferences [19], [20]."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Broadly, AIMC can be categorized based on the underlying memory technology into volatile and nonvolatile approaches [7]."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _extends/builds-on_: "In recent works, we have shown that analog hardware-aware training [23] and posttraining adaptation [24] can effectively mitigate these effects, suggesting that accuracy is not the fundamental barrier to deploying AIMC for LLM inference."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Vasilopoulos_AIMCforLLMInference_IMW.pdf](../../11_Small_Language_Models_on_AIMC/2026_Vasilopoulos_AIMCforLLMInference_IMW.pdf)
- Full text: [../fulltext/2026_Vasilopoulos_AIMCforLLMInference_IMW.txt](../fulltext/2026_Vasilopoulos_AIMCforLLMInference_IMW.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/imw68301.2026.11532624
