---
id: W4414659772
key: 2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun
title: "Demonstration of transformer-based ALBERT model on a 14nm analog AI inference chip"
short: "ALBERT on 14nm PCM Chip"
year: 2025
venue: "NatCommun"
venue_full: "Nature Communications 16:8661 (2025)"
authors: "An Chen, Stefano Ambrogio, Pritish Narayanan, Atsuya Okazaki, Charles Mackin, Andrea Fasoli, Malte J. Rasch, Alexander M. Friz, Jose Luquin, Takeo Yasuda, Masatoshi Ishii, Takuto Kanamori et al."
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM"]
models: ["Transformer", "BERT"]
lm_models: ["ALBERT-base"]
param_scale: "~7M unique weights (shared across 12 layers)"
slm: true
evidence: measured-silicon
topics: ["chip-demo", "language-models", "hardware-aware-training", "conductance-drift", "calibration-compensation", "weight-mapping", "tiling-partitioning", "transformer-accelerator"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 1
cites_in_collection: 10
citations_overall: 6
priority_score: 12.59
doi: "https://doi.org/10.1038/s41467-025-63794-4"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.pdf"
fulltext: "../fulltext/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.txt"
---

# ALBERT on 14nm PCM Chip

**Demonstration of transformer-based ALBERT model on a 14nm analog AI inference chip** — Nature Communications 16:8661 (2025) (2025)

## TL;DR
First fully weight-stationary analog-hardware demonstration of a meaningfully large Transformer: ALBERT-base fully-connected layers (7.1M unique weights, 28.3M PCM devices) run on a 14nm 34-tile PCM chip with only 1.8% average GLUE accuracy loss versus FP; HWA fine-tuning adds 4.4% and recalibration holds 30-day drift loss under 1%.

## Summary
ALBERT-base shares one set of weights across 12 encoder layers, so a single analog chip can hold the whole model and be iterated 12 times. The four weight layer-blocks (inProj for QKV, outProj, FC1, FC2; >99% of weights) are mapped across the 34 analog tiles (512x512 weights per tile with 4 PCM devices per weight, positive/negative PCM pairs) of IBM's 14nm PCM inference chip, with closed-loop programming and 2D-mesh routing via six input and six output landing pads; 79.4% of chip weight capacity is used. Attention compute (QK^T, softmax), layernorm, activations, pooler and classifier run off-chip in software on a control computer. Weights are fine-tuned with hardware-aware (noise-injection) training per GLUE task, programmed, and evaluated on seven GLUE tasks (full validation for RTE, MRPC, CoLA, SST-2; 1000-sample subsets for QNLI, MNLI, QQP). Experiments cover accuracy vs FP/SW, error margin and MAC error analysis, early exit, noise-scale ablation, a 30-day drift test with and without recalibration, and a speed/energy projection combining measured analog energy with 14nm digital simulation.

## Language models evaluated
- Models: ALBERT-base
- Scale: ~7M unique weights (shared across 12 layers)
- Note: ALBERT-base (7.1M unique weights) run on a real 14nm PCM analog AI inference chip (34 tiles), with attention/LayerNorm etc. in digital; GLUE tasks.

## Contributions
- Largest fully weight-stationary analog CIM demonstration of a Transformer (ALBERT) with measured GLUE accuracy
- Multi-tile mapping of 4 layer-blocks onto a single chip with mesh routing
- First hardware demonstration of HWA training benefit on a large Transformer
- 30-day PCM drift measurement and recalibration-based drift compensation
- Power/throughput analysis vs sequence length

## Key claims (stable IDs)
- **2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun#C1** — Average GLUE hardware accuracy only 1.8% below FP — _support:_ 1.79% FP-to-HW gap; SW is 0.5% below FP, HW another 1.29% below SW; MRPC and QNLI reach iso-accuracy (>99% of FP) — _loc:_ Fig. 3, Results
- **2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun#C2** — HWA fine-tuning improves HW accuracy by 4.4% on average — _support:_ optimal noise scale typically 1.0-2.0 — _loc:_ Fig. 4a-b
- **2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun#C3** — Recalibration limits 30-day drift loss to <1% versus ~5% without — _support:_ MRPC measured over 30 days — _loc:_ Fig. 4c
- **2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun#C4** — System efficiency over 3 TOPS/W on all GLUE tasks with analog >95% of energy — _support:_ tile ~20 TOPS/W vs 14nm digital 5-7 TOPS/W — _loc:_ Fig. 5

## Results
- RTE and CoLA lowest at 95.5% and 96.7% of FP accuracy
- Early exit after layer 11 costs only 0.4% average accuracy (Fig. 3f)
- FC2 (3072x768, six-tile summation, 7-bit OLP quantization) shows highest MAC variation; FC1 lowest
- Analog operations >99% of ops for short sequences, ~98% for long (Fig. 5b)
- Simulated weight quantization: ~4-bit effective precision sufficient for almost all GLUE tasks (Fig. 1e)

## Key numbers
- tech_node: 14nm
- array_size: 512x512 weights per tile (4 PCM/weight), 34 tiles
- energy_eff: >3 TOPS/W system level; ~20 TOPS/W tile
- accuracy: 1.8% below FP on average GLUE (7 tasks)
- bits_weight: ~4b effective
- bits_adc: 7b at output landing pads

## Datasets / benchmarks
GLUE (RTE, MRPC, CoLA, SST-2, QNLI, MNLI, QQP)

## Limitations
- Attention matrices, layernorm, softmax, pooler, classifier run in software off-chip
- Non-pipelined dataflow limited by landing-pad throughput; efficiency numbers are projections
- Encoder-only ~7M-unique-weight model, not a decoder LLM; GLUE sequences up to 128 tokens
- Drift measured at room temperature for 30 days on one task (MRPC); QNLI/MNLI/QQP evaluated on 1000-sample subsets
- Text states both 7.1M (abstract) and 7.7M (introduction) unique weights

## Remarks
Strongest measured-silicon evidence to date that encoder transformers run near iso-accuracy on analog PCM tiles, validating HWA training and drift compensation recipes previously shown only in simulation. The scope is the weight layers only; dynamic attention compute stays digital, which is exactly the bottleneck for scaling to decoder LLMs and KV-cache. Weight sharing makes ALBERT a convenient but not fully representative test.

## Use in the original review
- F1 (High confidence): Transformers now run on real analog PCM silicon at near-iso-accuracy: ALBERT-base on a single 14 nm PCM chip across 28.3M devices, averaging only 1.8% below the floating-point reference on 7 GLUE tasks, with several tasks at full iso-accuracy.
- F3 (High confidence): Measured on-chip accuracy is close to software but not free, and the penalty grows with model scale — from full software-equivalence on keyword spotting, to <1 pp on ResNet-9, to 1.8 pp on ALBERT/GLUE, to a missed equivalence threshold on a 45M-weight RNN-T.
- F4 (High confidence): Hardware-aware training — injecting realistic device noise during training or fine-tuning — is the field's dominant and empirically validated mitigation, and it now scales to pre-trained LLMs. On under 1% of pre-training tokens, Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct retained accuracy comparable to 4-bit-weight / 8-bit-activation quantized baselines under hardware-realistic analog noise — a gap off-the-shelf LLMs cannot close on their own.

## Cites (in collection, 10)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _background_: "PCM conductance drift effect and mitigation As the amorphous phase within programmed PCM devices relaxes, device-conductances decrease logarithmically over time38."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "The HWA fine-tuning of the ALBERT model was conducted with an internal tool and the same capability is available in the IBM Analog Hardware Acceleration Kit at https://github.com/IBM/aihwkit43,44."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _uses-method-or-tool_: "In this work, we map the weights of one ALBERT layer onto a single PCM-based analog inference chip that we have demonstrated recently34."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Analog accelerators based on CIM have been demonstrated using various NVM technologies, e.g., Flash3–5, PCM6–9, RRAM10–13, MRAM14–16, ECRAM17–19, or ferroelectric devices20–22."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _background_: "In a more advanced design where digital compute units are distributed on-chip amongst the tiles, fine-grained pipelining within each layer can be expected to keep all resources continuously busy, leading to significant improvements in both energy-efficiency and throughput36."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "HWA training has been demonstrated on smaller networks, e.g., Convolutional Neural Network (CNN), LSTM7."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _baseline/comparison_: "The prior work on the demonstration of the Recurrent Neural Network Transducer (RNNT) model in this analog accelerator achieved the efficiency of 6-7 TOPS/W, a 14 × improvement over conventional digital accelerators8."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "In fact, previous work has shown that ALBERT is significantly more challenging for analog AI hardware than BERT-base model31 that implements unique weight-matrices for each of the 12 layers."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "The HWA fine-tuning of the ALBERT model was conducted with an internal tool and the same capability is available in the IBM Analog Hardware Acceleration Kit at https://github.com/IBM/aihwkit43,44."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _background_: "Initial pipelining studies for networks such as BERT-base and BERTlarge have already been performed for such chips, showing the considerable throughput and latency benefits of “Full Weight Stationarity.”2,40"

## Cited by (in collection, 1)
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _background_: "This makes them a natural fit for NVM-based AIMC, where weights can be programmed once and reused across many inferences [19], [20]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.pdf](../../11_Small_Language_Models_on_AIMC/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.pdf)
- Full text: [../fulltext/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.txt](../fulltext/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-025-63794-4
