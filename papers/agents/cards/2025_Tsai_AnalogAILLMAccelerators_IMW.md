---
id: W4411233250
key: 2025_Tsai_AnalogAILLMAccelerators_IMW
title: "Analog AI Accelerators for Transformer-based Language Models: Hardware, Workload, and Power Performance"
short: "Analog AI for LLMs (IBM IMW'25)"
year: 2025
venue: "IMW"
venue_full: "IEEE International Memory Workshop (IMW 2025)"
authors: "Hsinyu Tsai, Hadjer Benmeziane, Irem Boybat, Julian Büchel, Pritish Narayanan, Manuel Le Gallo, Sameer H. Jain, A. Vasilopoulos, William Simon, Kohji Hosokawa, Masatoshi Ishii, Yasuteru Kohda et al."
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM"]
models: ["Transformer", "BERT", "GPT/LLM", "MoE", "CNN", "LSTM/RNN"]
lm_models: ["RoBERTa", "BERT-Large (architecture mapping)", "MobileBERT (architecture simulation)", "OPT (2.7B-13B family)", "Llama (up to 13B)", "Mistral (7B)"]
param_scale: "2.7B-13B (accuracy studies cited from NORA); 33M-weight edge fabric"
slm: true
evidence: survey
topics: ["language-models", "transformer-accelerator", "heterogeneous-analog-digital", "3d-integration", "moe", "kv-cache", "hardware-aware-training", "ir-drop-parasitics"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 11
citations_overall: 2
priority_score: 9.24
doi: "https://doi.org/10.1109/imw61990.2025.11026974"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Tsai_AnalogAILLMAccelerators_IMW.pdf"
fulltext: "../fulltext/2025_Tsai_AnalogAILLMAccelerators_IMW.txt"
---

# Analog AI for LLMs (IBM IMW'25)

**Analog AI Accelerators for Transformer-based Language Models: Hardware, Workload, and Power Performance** — IEEE International Memory Workshop (IMW 2025) (2025)

## TL;DR
Short IBM IMW 2025 overview of PCM-based analog in-memory computing for LLM inference: three 14 nm PCM chips/architectures (9.76 and 12.4 TOPS/W measured), hardware-aware training results, a 3D AIMC with MoE expert-per-tier mapping, and the digital self-attention/KV-cache bottleneck.

## Summary
The paper motivates AIMC for LLMs by the growth of Transformer size (8x per 2 years) and context length, and notes algorithmic mitigations (MoE, GQA, MLA, SSMs). It reviews IBM's PCM AIMC hardware: Chip 1 (64 tiles of 256x256, CCO-based ADCs, global digital units, 9.76 TOPS/W peak as given), Chip 2 (34 tiles of 512x512 with analog-duration 2D-mesh inter-tile links, 12.4 TOPS/W best chip), and a heterogeneous programmable 2D-mesh architecture (projected 40-140x better energy efficiency than A100 for one BERT-Large layer mapping; Fig. 1), plus an edge Transformer fabric with 33M PCM weights on 30 mm2 simulated on MobileBERT. Three LLM challenges are discussed: accuracy under noise and drift (AIHWKit, AIHWKit-Lightning HWA training giving iso-accuracy RoBERTa on GLUE, and post-training NORA-style study of OPT/Llama/Mistral 2.7-13B), scale-up (larger tiles limited by IR drop; 3D AIMC with one-tier-at-a-time MAC enabling fully weight-stationary and 'fully unrolled' pipelines, MoE experts on tiers), and the self-attention bottleneck (dynamic Q/K/V matrices computed in digital since NVM write speed and endurance are inadequate; KV-cache sizes in Fig. 3). Table II lists design considerations.

## Language models evaluated
- Models: RoBERTa, BERT-Large (architecture mapping), MobileBERT (architecture simulation), OPT (2.7B-13B family), Llama (up to 13B), Mistral (7B)
- Scale: 2.7B-13B (accuracy studies cited from NORA); 33M-weight edge fabric
- Note: Overview of IBM PCM-based analog AI accelerators for Transformer LLMs; the available text names no specific models or scales.

## Contributions
- Concise synthesis of IBM PCM AIMC chips and architecture studies relevant to LLMs
- Framing of three LLM challenges for AIMC: accuracy, capacity scale-up, self-attention
- 3D AIMC one-tier-at-a-time and MoE expert-to-tier mapping argument
- Design-consideration table linking analog tiles and compute units to technology/algorithm enablers

## Key claims (stable IDs)
- **2025_Tsai_AnalogAILLMAccelerators_IMW#C1** — IBM demonstrated PCM AIMC chips at 14 nm with measured efficiencies of 9.76 TOPS/W (peak) and 12.4 TOPS/W (best chip) — _support:_ Table I — _loc:_ Sec. III, Table I
- **2025_Tsai_AnalogAILLMAccelerators_IMW#C2** — Mapping one BERT-Large layer to the 2D-mesh heterogeneous AIMC architecture gives 40-140x energy-efficiency benefit vs A100 GPUs (projected) — _support:_ 'projected 40-140x energy efficiency benefits compared to A100 GPUs' — _loc:_ Sec. III, Fig. 1
- **2025_Tsai_AnalogAILLMAccelerators_IMW#C3** — Hardware-aware pre-training with AIMC noise reaches iso-accuracy on GLUE for RoBERTa — _support:_ AIHWKit-Lightning study [24] — _loc:_ Sec. IV
- **2025_Tsai_AnalogAILLMAccelerators_IMW#C4** — Self-attention remains digital in AIMC systems because dynamic activations are unsuited to NVM (write speed, endurance) — _support:_ attention compute scales O(s^2) in prefill and needs the KV cache in decode — _loc:_ Sec. IV
- **2025_Tsai_AnalogAILLMAccelerators_IMW#C5** — 3D AIMC makes systems fully weight stationary and suits MoE — _support:_ experts mapped to tiers of the same tile; One-Tier-at-a-Time computation — _loc:_ Sec. IV, Fig. 2

## Results
- Chip 2: 34 tiles of 512x512, 2D mesh with analog-duration transfer; keyword spotting fully in analog domain
- RNN-T with 45M weights demonstrated at low WER using 5 chips (~140M PCM devices)
- Edge Transformer fabric: 33M PCM weights on 30 mm2; MobileBERT simulation approaches high-end phone SoC throughput
- Projected 40-140x energy efficiency vs A100 for a BERT-Large layer (architecture simulation)

## Key numbers
- tech_node: 14nm
- array_size: 256x256 (Chip 1); 512x512 (Chip 2)
- energy_eff: 9.76 TOPS/W (peak, Chip 1); 12.4 TOPS/W (best, Chip 2); projected 40-140x vs A100
- accuracy: iso-accuracy RoBERTa on GLUE with HWA pre-training

## Datasets / benchmarks
GLUE

## Limitations
- Short invited overview; results are summarised from prior IBM papers rather than newly measured
- LLM-scale accuracy and efficiency numbers are simulated or projected; the largest measured demos are tens of millions of weights
- Table I extraction is garbled so per-chip weight counts are uncertain
- No new quantitative LLM benchmark data in the paper itself
- Attention and KV cache remain unaddressed in analog and are left to digital/GPU-style improvements

## Remarks
Useful roadmap-style statement from the leading PCM AIMC group of what blocks LLMs on analog hardware: noise/drift accuracy (handled by HWA training), capacity (3D, MoE), and digital attention/KV cache. It contains little new data but ties together the chip papers and the AIHWKit/NORA/MoE-3D works in the collection. Compared with gain-cell analog-attention work, it concedes attention to digital.

## Cites (in collection, 11)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "AIMC can be implemented in various ways, for example, using volatile memory [9] or non-volatile memory (NVM) for weight storage; storing one or multiple bits of weights per memory device; and reading memory arrays using analog read voltages [10] or a constant voltage with analog durations [11]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "AIMC can be implemented in various ways, for example, using volatile memory [9] or non-volatile memory (NVM) for weight storage; storing one or multiple bits of weights per memory device; and reading memory arrays using analog read voltages [10] or a constant voltage with analog durations [11]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _extends/builds-on_: "Combining insights from the 14nm hardware, we proposed a heterogeneous, programmable, and scalable system architecture with on-chip auxiliary operation support for CNN, LSTM, and Transformer [19]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "IBM recently demonstrated two chips and one architectural extension using PCM-base AIMC on 14nm CMOS [12], [13], [19], as summarized in Table I."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "IBM recently demonstrated two chips and one architectural extension using PCM-base AIMC on 14nm CMOS [12], [13], [19], as summarized in Table I."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "To study networks well beyond the scale of current hardware implementations, the AIHWKit [23] and AIHWKitLightning [24] were developed to model AIMC for DNNs and enable hardware-aware (HWA) training [25]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "To study networks well beyond the scale of current hardware implementations, the AIHWKit [23] and AIHWKitLightning [24] were developed to model AIMC for DNNs and enable hardware-aware (HWA) training [25]."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _extends/builds-on_: "By mapping experts in an MoE to different tiers of the same tile, all the experts remain weight-stationary, and data-vectors can be predictably delivered to the same Tile independent of which expert they need to address [28]."
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024) — _background_: "A similar analog fabric was designed for edge Transformer applications [22], hosting 33 million PCM weights on a 30mm2 chip."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _extends/builds-on_: "To study the impact of post-training optimization techniques, we used the full AIHWKit to study the accuracy and noise-resilience of OPT, Llama, and Mistral models ranging from 2.7-13B weights [26]."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _data/numbers_: "Figure 1 shows an example of mapping one BERT Large layer onto the architecture [21], with projected 40-140x energy efficiency benefits compared to A100 GPUs."

## Cited by (in collection, 1)
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _motivation_: "In contrast, the dynamic components of LLM inference pose significant challenges for AIMC [21]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Tsai_AnalogAILLMAccelerators_IMW.pdf](../../11_Small_Language_Models_on_AIMC/2025_Tsai_AnalogAILLMAccelerators_IMW.pdf)
- Full text: [../fulltext/2025_Tsai_AnalogAILLMAccelerators_IMW.txt](../fulltext/2025_Tsai_AnalogAILLMAccelerators_IMW.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/imw61990.2025.11026974
