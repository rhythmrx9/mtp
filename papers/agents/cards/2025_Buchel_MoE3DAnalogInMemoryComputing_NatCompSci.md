---
id: W4406178148
key: 2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci
title: "Efficient scaling of large language models with mixture of experts and 3D analog in-memory computing"
short: "MoE on 3D AIMC"
year: 2025
venue: "NatCompSci"
venue_full: "Nature Computational Science"
authors: "Julian Büchel, Athanasios Vasilopoulos, William Simon, Irem Boybat, Hsinyu Tsai, Geoffrey W. Burr, Hernan Castro, B. Filipiak, Manuel Le Gallo, Abbas Rahimi, Vijay Narayanan, Abu Sebastian"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM", "Generic-NVM"]
models: ["Transformer", "GPT/LLM", "MoE"]
lm_models: ["Mixtral 8x7B (architecture basis)", "GPT-2 (300M, 700M, 1B)", "Megatron 1B", "decoder-only Switch Transformer MoE (small, base)", "MoE and dense LMs trained on WikiText-103"]
param_scale: "300M-1B simulated for GPU comparison; Mixtral-8x7B (47B) architecture studied for scaling"
slm: true
evidence: simulation
topics: ["moe", "language-models", "3d-integration", "transformer-accelerator", "hardware-aware-training", "noise-injection", "energy-efficiency", "scheduling"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 8
cites_in_collection: 8
citations_overall: 40
priority_score: 11.99
doi: "https://doi.org/10.1038/s43588-024-00753-x"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.pdf"
fulltext: "../fulltext/2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.txt"
---

# MoE on 3D AIMC

**Efficient scaling of large language models with mixture of experts and 3D analog in-memory computing** — Nature Computational Science (2025)

## TL;DR
Simulating decoder-only MoE and dense LLMs on an abstract 3D-NVM analog in-memory computing accelerator shows MoEs form the throughput/energy/area Pareto front, reach up to 6x throughput and 20x area efficiency over an A100 for large MoEs (up to ~3 orders of magnitude energy efficiency), and keep FP32 iso-perplexity up to 6.3% Gaussian weight noise with hardware-aware training.

## Summary
Parameter storage and fetching dominates LLM inference on GPUs, while AIMC keeps weights stationary but 2D chips are orders of magnitude too small for LLMs. The authors argue that conditional computation in MoE (only top-k experts active) matches 3D AIMC, where weight matrices are written to tiers of 3D NVM tiles and each MVM selects a tier, subject to a one-tier-at-a-time (OTT) constraint that forbids parallel MVMs across tiers of one tile. A simulator traces and prunes the compute graph of one generated token (with KV cache), concatenates graphs for autoregressive loops and batches, and schedules it on a parameterised accelerator of 3D AIMC tiles (512x512 tile-shaped weight chunks, experts stacked vertically across tiers, greedy in-order mapping to lowest-utilisation tiles), digital processing units for activations/normalisation, multi-head-attention units (digital, with scratchpad SRAM) and an interconnect with constant time/energy per bit; area assumptions are 1 mm2 per tile, 5 mm2 per MHA unit, 1.25 mm2 per DPU. Dense models (GPT-2 300M-1B, Megatron 1B) and decoder-only switch-transformer MoEs are compared against an NVIDIA A100 (upper-bound throughput from memory bandwidth, 400 W at 100% MFU), and scaling laws for dense and MoE models relate FLOP budget to accuracy to build the accuracy versus system-performance Pareto front. Noise robustness is tested by hardware-aware fine-tuning of a dense and an MoE LM on WikiText-103 with additive Gaussian weight noise, reporting perplexity and ROUGE-1.

## Language models evaluated
- Models: Mixtral 8x7B (architecture basis), GPT-2 (300M, 700M, 1B), Megatron 1B, decoder-only Switch Transformer MoE (small, base), MoE and dense LMs trained on WikiText-103
- Scale: 300M-1B simulated for GPU comparison; Mixtral-8x7B (47B) architecture studied for scaling
- Note: Dense GPT-2 (300M-1B) and Megatron-1B compared with MoE models scaling up to ~51B total parameters, mapped to 3D analog (PCM) in-memory computing in simulation/projection; the largest MoE models exceed the SLM range, although per-token active compute is smaller.

## Contributions
- Argument and simulation that MoE conditional compute suits 3D NVM AIMC (weights stationary, only activations move)
- Abstract 3D AIMC accelerator simulator with OTT constraint, tracer/scheduler and mapping algorithms
- Comparison with A100 across dense and MoE LMs, and accuracy-versus-system-performance Pareto analysis using scaling laws
- Noise-robustness study showing MoE iso-performance at noise comparable to PCM AIMC chips

## Key claims (stable IDs)
- **2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci#C1** — MoEs form the Pareto front of accuracy versus throughput, energy and area efficiency on 3D AIMC — _support:_ For any accuracy MoE gives better system performance than dense — _loc:_ Fig. 5
- **2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci#C2** — For large MoEs 3D AIMC outperforms A100 in throughput and area efficiency — _support:_ Up to 6x throughput, up to 20x area efficiency; energy efficiency up to three orders of magnitude (A100 at 400 W / 301.93 W) — _loc:_ Fig. 4 / Comparison against GPUs
- **2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci#C3** — MoE retains FP32-equivalent accuracy under analog noise with hardware-aware training — _support:_ Iso-performance up to 6.3% Gaussian noise; PCM chip programming noise equals ~4.75% for this network — _loc:_ Fig. 6a / Robustness section
- **2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci#C4** — Active activation memory is small — _support:_ Peak memory ~1 MB (~1.18 MB for dmodel 1024, seq length 72, int8) — _loc:_ Fig. 3c

## Results
- For small models, A100 throughput is generally one order of magnitude higher than 3D AIMC (Fig. 4a)
- Large MoEs: A100 lower-bounded by DRAM fetch at 1,555 GB/s (~250 GB for dmodel 1024, 128 experts, 48 layers, 8 iterations, ~0.16 s); 3D AIMC up to 6x higher throughput
- For MoE (dec-only base) at batch >=32 the GPU has higher throughput but 3D AIMC keeps orders-of-magnitude better energy efficiency (Supplementary Note 4)
- Inference time jumps from dmodel 512 to 768 because a 768x768 layer occupies four tiers versus one and total OTT conflicts rise (Fig. 3d)
- MoE slightly outperforms the dense LM in WikiText-103 perplexity across noise levels (Fig. 6b)

## Key numbers
- array_size: 512x512 tile-shaped chunks; tiers stacked per tile
- energy_eff: up to ~3 orders of magnitude over A100
- throughput: up to 6x A100 (large MoEs)
- accuracy: iso-perplexity up to 6.3% Gaussian weight noise
- bits_weight: 5b (0.625 B) for GPU weight-fetch estimate; int8 activations

## Datasets / benchmarks
WikiText-103, ROUGE-1

## Limitations
- Abstract architecture; no circuit-level design, interconnect contention not modelled, no real 3D AIMC hardware exists
- Noise modelled as additive Gaussian on weights, not device-specific (drift, IR-drop, ADC) and noise level for 3D NVM is unknown
- Accuracy-performance Pareto uses published scaling laws, not trained models
- Attention executed in digital MHA units; KV-cache and external memory hierarchy left open
- GPU advantage at large batch sizes (>=32) and small models

## Remarks
Influential Nature-family study that frames MoE as the natural LLM architecture for NVM-based AIMC and quantifies the OTT scheduling constraint; evidence is simulation with optimistic, abstract assumptions (hypothetical 3D devices, area numbers fixed by assumption). The SLM relevance is indirect: the comparison models are 0.3B-1B and noise tests use a small WikiText-103 LM. Complements ReTern/H3D works in the collection and IBM analog-AI chip papers cited for noise calibration.

## Cites (in collection, 8)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "To make the models robust to noise, we follow the standard procedure51 of first training the FP-32 base model, followed by hardware-aware finetuning on the same dataset."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "A promising alternative to the von-Neumann architecture that has risen in popularity is in-memory computing using non-volatile memory (NVM) devices18-21."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Recent publications of large-scale integrated AIMC chips, using phase change memory (PCM) 22,23, resistive RAM (ReRAM)24-26 and Flash27, show the viability of the technology."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _data/numbers_: "In Fig. 6a we show that, for the MoE-based model, iso-performance is retained up to noise levels of 6.3%, which is within the range of noise values observed for previously published AIMC hardware22."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "Notable progress has already been made in addressing these issues through large-scale demonstrations of 2D AIMC architectures22,23, and these solutions are expected to be applicable to 3D AIMC as well."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "For hardware-aware finetuning, we leveraged AIHWKIT54, an open-source framework used for hardware-aware training of neural networks."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Recent publications of large-scale integrated AIMC chips, using phase change memory (PCM) 22,23, resistive RAM (ReRAM)24-26 and Flash27, show the viability of the technology."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)

## Cited by (in collection, 8)
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _extends/builds-on_: "By mapping experts in an MoE to different tiers of the same tile, all the experts remain weight-stationary, and data-vectors can be predictably delivered to the same Tile independent of which expert they need to address [28]."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _motivation_: "Consequently, NVM-based AIMC accelerators are predominantly investigated within the context of weight-stationary models that could meet the requirements of edge devices19 and large language model inference20."
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _data/numbers_: "In [22], we studied LLMs inference on 3D AIMC hardware and observed significant energy efficiency improvements, especially for MoE-based architectures – up to 3 orders of magnitude– which can exploit increased capacity without proportionally increasing computation."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _extends/builds-on_: "Recently, we demonstrated that MoE-type LLMs scale favorably for NVM CIM-based systems, both in terms of latency as well as model accuracy for a given inference-OPs budget. Furthermore, HWA-trained MoEs can maintain this accuracy performance even in the presence of noise typical of analog computations [21]."
- [2025_Malhotra_ReTern_TVLSI](2025_Malhotra_ReTern_TVLSI.md) ReTern (2025) — _background_: "Various CiM-based LLM accelerators have been proposed, showcasing sizeable benefits over conventional von-Neumann based platforms such as GPUs [2]-[5]."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _motivation_: "This can yield up to three orders of magnitude higher energy efficiency compared to state-of-the-art GPUs when running Mixture of Experts (MoE)-based LLMs [26]."
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.pdf](../../11_Small_Language_Models_on_AIMC/2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.pdf)
- Full text: [../fulltext/2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.txt](../fulltext/2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s43588-024-00753-x
