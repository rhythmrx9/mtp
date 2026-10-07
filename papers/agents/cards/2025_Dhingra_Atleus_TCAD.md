---
id: W4406521098
key: 2025_Dhingra_Atleus_TCAD
title: "Atleus: Accelerating Transformers on the Edge Enabled by 3D Heterogeneous Manycore Architectures"
short: "Atleus"
year: 2025
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025)"
authors: "Pratyush Dhingra, Janardhan Rao Doppa, Partha Pratim Pande"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-digital"]
models: ["Transformer", "BERT", "GPT/LLM"]
lm_models: ["RoBERTa-base", "BERT-large", "GPT-2 Medium", "BLOOM-560m"]
param_scale: "110M-560M"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "llm-adapters-lora", "3d-integration", "heterogeneous-analog-digital", "noise-injection", "quantization", "dataflow-pipelining", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 12
citations_overall: 9
priority_score: 9.5
doi: "https://doi.org/10.1109/tcad.2025.3531255"
pdf: "../../04_Transformers_and_LLMs/2025_Dhingra_Atleus_TCAD.pdf"
fulltext: "../fulltext/2025_Dhingra_Atleus_TCAD.txt"
---

# Atleus

**Atleus: Accelerating Transformers on the Edge Enabled by 3D Heterogeneous Manycore Architectures** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025) (2025)

## TL;DR
Atleus is a 3D heterogeneous edge accelerator that keeps frozen pre-trained transformer weights on ReRAM crossbars and runs dynamic attention products and LoRA fine-tuning on systolic arrays, claiming up to 56x speedup and 64.5x energy efficiency over a GPU for fine-tuning and inference of 110M-560M models.

## Summary
Standalone NVM PIM cannot support transformer fine-tuning and inference because attention needs dynamic operand products (many NVM writes) and fine-tuning updates weights, hitting endurance limits. Atleus splits work by operand type: matrix multiplies with static pre-trained weights (MHA projections and FFN, about 12 x O(d_model^2 n) work) go to ReRAM (16 tiles per core, 128x128 crossbars, 2 bit/cell, 8-bit ADCs, 1-bit DACs, 32 nm), while dynamic Q.K^T and A.V, softmax/layer-norm and the trainable LoRA low-rank matrices (rank 32 on W_Q and W_V) run on a systolic-array tier (128x32 PEs per core, 10 nm), with HBM2 off-chip. The tiers are stacked in 3D with TSVs and a heterogeneous 3D NoC designed with BookSim2, and a four-stage intra-layer pipeline (three ReRAM stages, one systolic stage) is balanced. Because LoRA weights sit in digital cores, noise-aware fine-tuning injects Gaussian weight noise into the frozen ReRAM weights while training LoRA so the adapters compensate ReRAM non-idealities. A crossbar-wise (block-wise, QLoRA-style) quantization removes the GPU's dequantization cost by using fewer cells per weight, with extra shift-and-add scale units per tile. Evaluation uses synthesis (Design Compiler), SCALE-Sim for systolic arrays, modified NeuroSim for ReRAM peripherals, and BookSim2; models are fine-tuned on SQuAD, SWAG and WikiText and compared with HAIMA, a 3D-TPU and a GPU.

## Language models evaluated
- Models: RoBERTa-base, BERT-large, GPT-2 Medium, BLOOM-560m
- Scale: 110M-560M

## Contributions
- 3D heterogeneous ReRAM plus systolic-array architecture targeting both transformer fine-tuning (LoRA) and inference at the edge
- 3D NoC and an intra-layer pipelined design across heterogeneous cores
- Noise-aware LoRA fine-tuning where adapters run on noise-free digital cores to absorb ReRAM noise in frozen weights
- Crossbar-wise quantization avoiding dequantization overhead

## Key claims (stable IDs)
- **2025_Dhingra_Atleus_TCAD#C1** — Atleus outperforms GPU and prior accelerators by up to 56x in performance and 64.5x in energy efficiency — _support:_ Abstract and conclusion (versus GPU) — _loc:_ Abstract / Fig. 11
- **2025_Dhingra_Atleus_TCAD#C2** — ReRAM handles ~92% of the compute but a minority of the energy — _support:_ 91.9% of operations on ReRAM; ReRAM about 12x more operations than systolic array (GPT-2 Medium, seq 1024) — _loc:_ Sec. V-C / Fig. 7
- **2025_Dhingra_Atleus_TCAD#C3** — Noise-aware LoRA fine-tuning restores accuracy under ReRAM noise — _support:_ <0.5% accuracy loss vs ideal (RoBERTa-base, BERT-large on SQuAD and SWAG) — _loc:_ Sec. V-E / Fig. 9
- **2025_Dhingra_Atleus_TCAD#C4** — Energy falls near-linearly with quantization bits — _support:_ slope alpha<1 due to dequantization overhead; M8F4 saves more than M4F8 — _loc:_ Sec. V-F / Fig. 12

## Results
- Up to 56x execution-time and 64.5x energy-efficiency advantage over baselines (GPU-referenced) (Fig. 11)
- 91.9% of operations executed on ReRAM tier (Fig. 7a)
- Noise-aware fine-tuning accuracy within 0.5% of ideal-device accuracy for RoBERTa-base and BERT-large (Fig. 9)
- HAIMA suffers high communication delay and HBM bank-parallelism limits during fine-tuning pipeline (Fig. 10)
- Inference: Atleus still outperforms accelerators; HAIMA slightly better than in fine-tuning (Sec. V-G)

## Key numbers
- tech_node: 32nm ReRAM tier; 10nm systolic tier
- array_size: 128x128 ReRAM crossbars (16 cores x 16 tiles x 96 crossbars); 128x32 systolic PE arrays
- energy_eff: up to 64.5x vs GPU
- throughput: up to 56x speedup
- accuracy: <0.5% loss with noise-aware fine-tuning
- bits_weight: 2b/cell, block-wise quantization (M8F4 etc.)
- bits_adc: 8b

## Datasets / benchmarks
SQuAD, SWAG, WikiText

## Limitations
- Simulation only with Gaussian weight noise on pre-trained weights; no drift, IR drop or ADC non-linearity
- Models of 110M-560M, not billion-parameter LLMs; datasets SQuAD, SWAG, WikiText
- Headline 56x/64.5x relative to GPU and strongly depends on baseline configuration
- Dynamic attention products and LoRA on digital systolic arrays, so only about 8% of operations use analog CIM; cost of 3D integration (thermal, yield) analysed only at a modelling level
- Pre-trained weights assumed pre-mapped to crossbars (write cost excluded)

## Remarks
Notable for treating fine-tuning (LoRA) as a first-class workload on ReRAM and for the neat trick of letting noise-free digital LoRA adapters compensate analog noise in frozen weights; that idea is directly relevant to adapting small language models on NVM CIM. Evidence is architectural simulation with large relative claims, so absolute credibility is moderate. Compare with HyPIM/HARDSEA hybrid designs and ReTern (faults) in the collection.

## Cites (in collection, 12)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _uses-method-or-tool_: "In our performance evaluation, we assume that the pre-trained model parameters are mapped to ReRAM crossbars prior to inferencing or fine-tuning consistent with prior work [38]."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "Processing-in-Memory (PIM) has emerged as a promising approach to accelerate the training/inference of machine learning (ML) workloads [9]."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _background_: "ReTransformer proposes a ReRAM-based PIM architecture to accelerate transformer inference [21]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "SCALE-Sim is utilized for the systolic array cores and a modified NeuroSim is employed to obtain the latency of all on-chip buffers, and peripheral circuits in ReRAM cores [47] [32]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _uses-method-or-tool_: "For this purpose, we follow existing work and utilize a noise injection approach to improve the robustness of the finetuned model to ReRAM non-idealities [54] [55]."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _background_: "Similarly, another work introduces a hardware-software co-design framework for transformer acceleration on ReRAM-based architecture [23]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _extends/builds-on_: "We facilitate dequantization by integrating additional shift-and-add (S&A) units into the previously proposed ReRAM tile architecture [20]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _background_: "TransPIM is a DRAM-based PIM accelerator with compute units integrated within High Bandwidth Memory (HBM) banks to accelerate transformer inference [25]."
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022) — _contrasts/critiques_: "Existing approaches aimed at reducing the number of rewrites during training or fine-tuning incur significant performance overhead or necessitate redundant hardware [15] [16]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Hence, standalone NVM-based PIM architectures are not suitable for transformer fine-tuning and inference [12]."
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024) — _contrasts/critiques_: "Likewise, H3D-Transformer proposes a hybrid architecture consisting of FeFET, SRAM, and TPU cores stacked vertically via TSVs in a 16-tier system [27]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _background_: "NVM devices are susceptible to non-idealities arising from various factors including process variations, temperature fluctuations, conductance drift, and IR drop, among others [13] [14]."

## Cited by (in collection, 3)
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "In this paper, we propose deploying finetuned LLMs on hybrid CIM, leveraging both the energy efficiency and computational density of RRAM and the noise-free computation of SRAM [64, 65]."
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../04_Transformers_and_LLMs/2025_Dhingra_Atleus_TCAD.pdf](../../04_Transformers_and_LLMs/2025_Dhingra_Atleus_TCAD.pdf)
- Full text: [../fulltext/2025_Dhingra_Atleus_TCAD.txt](../fulltext/2025_Dhingra_Atleus_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2025.3531255
