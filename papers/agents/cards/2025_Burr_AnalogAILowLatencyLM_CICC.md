---
id: W4410492466
key: 2025_Burr_AnalogAILowLatencyLM_CICC
title: "Analog-AI Hardware Accelerators for Low-Latency Transformer-Based Language Models (Invited)"
short: "Analog-AI LLM Accelerators (CICC)"
year: 2025
venue: "CICC"
venue_full: "IEEE Custom Integrated Circuits Conference (CICC), 2025"
authors: "Geoffrey W. Burr, Hsinyu Tsai, Irem Boybat, William Simon, Julian Büchel, A. Vasilopoulos, Pritish Narayanan, Andrea Fasoli, Kohji Hosokawa, Manuel Le Gallo, Masatoshi Ishii, Yasuteru Kohda et al."
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM", "ReRAM", "Flash", "SRAM-analog"]
models: ["Transformer", "BERT", "GPT/LLM", "MoE", "LSTM/RNN"]
lm_models: ["BERT-base", "BERT-large", "Llama-3.1-8B (architectural analysis)", "ALBERT"]
param_scale: "110M–8B"
slm: true
evidence: analytical
topics: ["language-models", "transformer-accelerator", "heterogeneous-analog-digital", "dataflow-pipelining", "kv-cache", "3d-integration", "hardware-aware-training", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 9
citations_overall: 1
priority_score: 9.11
doi: "https://doi.org/10.1109/cicc63670.2025.10983594"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Burr_AnalogAILowLatencyLM_CICC.pdf"
fulltext: "../fulltext/2025_Burr_AnalogAILowLatencyLM_CICC.txt"
---

# Analog-AI LLM Accelerators (CICC)

**Analog-AI Hardware Accelerators for Low-Latency Transformer-Based Language Models (Invited)** — IEEE Custom Integrated Circuits Conference (CICC), 2025 (2025)

## TL;DR
Invited overview from IBM arguing that Fully-Weight-Stationary (F-FWS) analog NVM accelerators give up to 9.75x lower latency, 5.21x better area efficiency and 33.3x higher throughput than a Partially-Weight-Stationary system on BERT-Large (simulation), and discussing latency factors (FC2 summation, QKV/KV-cache, GQA, 3D tiles) for scaling to Llama-3.1-8B.

## Summary
The paper reviews why large FC layers dominating Transformers suit analog NVM compute-in-memory tiles, defines Fully-Weight-Stationary (every trained weight has its own NVM location, no weight motion) versus Partially-Weight-Stationary systems, and refines the earlier IEDM 2023 study. It summarises chip demos: a 5-chip PCM system running an RNN-T speech model (45M weights, >140M PCM devices, <2% WER degradation on Librispeech, estimated 14x better system performance than GPU MLPerf submissions) and a 64-core 14 nm PCM chip with CCO-based ADCs running an LSTM image-captioning network. It describes the Analog Fabric architecture (CIM tiles, digital compute cores, SRAM scratchpads, circuit-switched 2D mesh with border-guard circuits; 40-140x more energy efficient than A100 at b=8 using tile assumptions of 100 TOPS/W at 40 ns integration time from 14 nm circuit simulation) and the use of hardware-aware training (HWA) to approach ~4-bit weight / 8-bit activation digital accuracy, e.g. fully software-equivalent GLUE accuracy on BERT-base up to one year of PCM drift. Using a detailed architectural simulator, F-FWS chiplet systems built for BERT-base/large (S=128, b=8) are compared against a VM-CIM PWS system with scratchpad weight reloading. For LLMs it discusses 3D NVM tiles with 4-hundreds of tiers, partial-sum aggregation of the 14,366-row FC2 matrix in Llama-3.1-8B, the attention (QKV) block with KV-cache and grouped-query attention (32 heads, 8 KV heads), and the output-embedding table (128,256 vocabulary) as an NVM CIM candidate.

## Language models evaluated
- Models: BERT-base, BERT-large, Llama-3.1-8B (architectural analysis), ALBERT
- Scale: 110M–8B
- Note: Invited overview of analog NVM (PCM) accelerators for Transformer language models; discusses fully vs partially weight-stationary systems and token-processing/generation latency. Specific models and scales not known from abstract.

## Contributions
- Quantifies benefits of Fully- versus Partially-Weight-Stationary analog CIM systems for encoder Transformers
- Summarises recent PCM chip demos (RNN-T 5-chip system, 64-core chip) and the Analog Fabric heterogeneous architecture
- Qualitative groundwork for F-FWS decoder-style LLMs: FC2 summation, QKV compute, KV-cache/GQA, 3D tiles, embedding table
- Reviews HWA training results across RNN, Transformer, CNN and MoE models

## Key claims (stable IDs)
- **2025_Burr_AnalogAILowLatencyLM_CICC#C1** — F-FWS gives up to 9.75x lower latency than a PWS system for BERT-Large — _support:_ architectural simulator, S=128, b=8, same tile characteristics (100 TOPS/W, 40 ns) — _loc:_ Sec. 6, Table 2, Fig. 5
- **2025_Burr_AnalogAILowLatencyLM_CICC#C2** — In continuous-input mode F-FWS improves area efficiency 5.21x (TOPS/seq/mm^2) and throughput 33.3x versus PWS — _support:_ does not need to choose a batch size — _loc:_ Sec. 6, Fig. 6
- **2025_Burr_AnalogAILowLatencyLM_CICC#C3** — Analog-AI Analog Fabric architecture can be 40x-140x more energy efficient than NVIDIA A100 (b=8) across LSTM, Transformer, CNN networks — _support:_ from prior work [18], PCM tile 100 TOPS/W at 40 ns from 14 nm simulation — _loc:_ Sec. 5
- **2025_Burr_AnalogAILowLatencyLM_CICC#C4** — HWA fine-tuning gives fully software-equivalent BERT-base GLUE accuracy until ~1 year of PCM drift; recurrent models are most robust, ALBERT (shared weights) least — _support:_ Ref. [32] — _loc:_ Sec. 4
- **2025_Burr_AnalogAILowLatencyLM_CICC#C5** — The FC2 block (14,366 rows in Llama-3.1-8B) and the QKV block are the two latency pain points; FC2 dominates for short sequences, QKV for long — _support:_ requires 14 (or 28) partial sums of 1024 (512) rows per token — _loc:_ Sec. 7, Fig. 7

## Results
- RNN-T on 5 PCM chips: 45M weights, >140M PCM devices, <2% WER degradation (Librispeech), ~14x estimated system-performance benefit vs GPU MLPerf submissions (Sec. 3)
- F-FWS vs PWS on BERT-Large: up to 9.75x lower latency; 5.21x area efficiency and 33.3x throughput in continuous-input mode (Sec. 6)
- Tile assumptions: 100 TOPS/W, 40 ns integration, 10.9 TOPS/mm^2 (Sec. 6)
- Llama-3.1-8B: 32 attention heads with 8 KV heads, hidden size 4096, vocabulary 128,256 (Sec. 7)
- F-FWS keeps KV-cache small by needing only batch b=2 locally per chip (Sec. 7, Fig. 8)

## Key numbers
- tech_node: 14nm (PCM tile simulation)
- array_size: 512x512 or 1024x1024 tiles
- energy_eff: 100 TOPS/W tile; 40x-140x vs A100 system (b=8)
- throughput: 33.3x vs PWS (continuous input)
- accuracy: <2% WER degradation (RNN-T on PCM chips); GLUE software-equivalent on BERT-base with HWA
- bits_weight: ~4-bit equivalent

## Datasets / benchmarks
Librispeech, GLUE, MLPerf (comparison)

## Limitations
- Invited short paper; most numbers come from simulation using tile characteristics assumed from 14 nm circuit simulations, not measured LLM silicon
- No end-to-end measured LLM on analog hardware; Llama-3.1-8B discussion is qualitative
- F-FWS needs enough silicon for every weight, so area for billion-parameter models may be infeasible; 3D NVM tiers not demonstrated here
- Attention/QKV and LayerNorm remain digital and are latency critical
- Detailed Table 2 values are not given in the extracted text beyond the quoted ratios

## Remarks
Authoritative statement of the IBM Analog-AI position that large NVM-based systems must be fully weight-stationary because of NVM endurance and write cost, which is directly relevant to how SLMs/LLMs map to crossbars (one unique tile per weight block, pipelined token flow). The quantitative case rests on a single architectural simulator and assumed tile specs, so it is a design argument rather than evidence of LM accuracy on chip; accuracy evidence is delegated to HWA-training papers (e.g. Analog Foundation Models, MoE+3D AIMC). Useful for identifying open issues for decoder LMs: KV-cache, long FC2 reductions and large vocabulary projection.

## Cites (in collection, 9)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "By exploiting such weight stationarity over short timespans with Volatile Memories (VMs) – SRAM or e-DRAM [7, 9] – or over longer timespans with slower, finite-endurance Non-Volatile Memories (NVMs) – Flash [10], Resistive-RAM [11], or phase-change memory (PCM) [12, 13] – such CIM approaches can offer high throughput, low latency, and high energy-efficiency [7, 8, 9]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Conversion is performed in parallel using dedicated Current-Controlled Oscillator (CCO)-based Analog-to-Digital Converters (ADCs) [13]."
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022) — _background_: "Recently, numerous researchers are exploring Compute-In-Memory (CIM) approaches [7, 8, 9] to increase energy-efficiency by performing Multiply-Accumuate (MAC) operations within ON-chip memory “Tiles,” to greatly reduce the motion of model-weights and partial sums."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _extends/builds-on_: "We recently introduced a highly programmable Analog-AI and Compute-In-Memory accelerator architecture [18], which utilizes a highly specialized set of Compute-cores and Tiles arranged within a common building block known as an Analog Fabric (AF) (Fig. 4), together with SRAM scratchpads, IO blocks, and a 2D Mesh on top of the building blocks."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _data/numbers_: "On a second chip, we integrated CCO-based ADCs (one per integration-row) into PCM-based CIM-Tiles [30] (Fig. 3)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _data/numbers_: "Recently, a large Recurrent Neural Network Tranducer (RNNT) model (Fig. 2a) was demonstrated [28], using 5 chips to encode 45M weights using >140M PCM devices."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _data/numbers_: "In contrast, using HWA training techniques to perform the fine-tuning for each GLUE classification-task can provide fully software-equivalent accuracy on BERT-base, at least until the accumulated effects of one year of PCM conductance-drift after programming [32]."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _extends/builds-on_: "Recently, we demonstrated that MoE-type LLMs scale favorably for NVM CIM-based systems, both in terms of latency as well as model accuracy for a given inference-OPs budget. Furthermore, HWA-trained MoEs can maintain this accuracy performance even in the presence of noise typical of analog computations [21]."
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024) — _background_: "Furthermore, by performing affine-scale and digital aggregation operations at the edge of the Tile, the number of post-integration data-transport steps involving the 2D data-transport mesh can be significantly reduced [34]."

## Cited by (in collection, 1)
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _background_: "Initial pipelining studies for networks such as BERT-base and BERTlarge have already been performed for such chips, showing the considerable throughput and latency benefits of “Full Weight Stationarity.”2,40"

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Burr_AnalogAILowLatencyLM_CICC.pdf](../../11_Small_Language_Models_on_AIMC/2025_Burr_AnalogAILowLatencyLM_CICC.pdf)
- Full text: [../fulltext/2025_Burr_AnalogAILowLatencyLM_CICC.txt](../fulltext/2025_Burr_AnalogAILowLatencyLM_CICC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/cicc63670.2025.10983594
