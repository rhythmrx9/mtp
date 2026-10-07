---
id: W7127107108
key: 2026_Li_AHWA-LoRA_NeuromorphComputEng
title: "Efficient transformer adaptation for analog in-memory computing via low-rank adapters"
short: "AHWA-LoRA"
year: 2026
venue: "NeuromorphComputEng"
venue_full: "Neuromorphic Computing and Engineering (IOP Publishing), 2026"
authors: "Chen Li, Elena Ferro, Corey Lammie, Manuel Le Gallo, Irem Boybat, Bipin Rajendran"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM"]
models: ["BERT", "Transformer", "GPT/LLM"]
lm_models: ["MobileBERT (25M)", "BERT-Base (108M)", "BERT-Large (334M)", "Llama-3.1-8B"]
param_scale: "25M-8B"
slm: true
evidence: algorithm+simulation
topics: ["language-models", "llm-adapters-lora", "hardware-aware-training", "noise-injection", "conductance-drift", "heterogeneous-analog-digital", "transformer-accelerator", "weight-mapping"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 0
cites_in_collection: 14
citations_overall: 1
priority_score: 10.71
doi: "https://doi.org/10.1088/2634-4386/ae405e"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Li_AHWA-LoRA_NeuromorphComputEng.pdf"
fulltext: "../fulltext/2026_Li_AHWA-LoRA_NeuromorphComputEng.txt"
---

# AHWA-LoRA

**Efficient transformer adaptation for analog in-memory computing via low-rank adapters** — Neuromorphic Computing and Engineering (IOP Publishing), 2026 (2026)

## TL;DR
AHWA-LoRA keeps pretrained transformer weights fixed on PCM AIMC tiles and trains only digital LoRA adapters under simulated hardware noise, matching full hardware-aware training on MobileBERT/SQuAD (F1 85.36 vs 85.14 at 10-year drift) with 15x fewer trainable parameters and as little as 4% latency overhead when adapters run on RISC-V clusters.

## Summary
Hardware-aware (AHWA) training of transformers for AIMC requires retraining all weights, is memory heavy, is single-task, and any model update needs slow, costly device reprogramming. The paper proposes to program pretrained meta-weights once to PCM AIMC tiles and train only LoRA matrices (A in R^{m x r}, B in R^{r x n}) while the forward pass of the frozen weights includes simulated hardware constraints (Gaussian weight noise 6.7%, ADC noise 4.0%, 8-bit DAC/ADC, clipping, programming/read noise and drift via AIHWKIT's PCM model). Mapping: all static linear layers (QKV projections, FFN, embedding transform, output; 20.4M of MobileBERT's params, about 81%) go onto 512x512 AIMC tiles with differential channel-wise weight mapping (Gmax=25 uS) and a digital affine scale after ADC; attention score matrix products (dynamic) and the LoRA branch XAB plus addition run on digital RISC-V Snitch PMCAs with RedMulE. Evaluation covers SQuAD v1.1 and GLUE on MobileBERT, BERT-Base/Large scaling, and Llama-3.1-8B instruction tuning (Alpaca) and GRPO reinforcement learning (GSM8K), plus cycle-accurate RTL simulation of the PMCA for latency balancing. Results: comparable accuracy to full AHWA with ~1M vs 15x more trainable parameters, 13% less GPU memory, multi-task GLUE with 8 adapters (4x fewer total parameters than 8 programmed models), dynamic adaptation recovering F1 60.81 to 74.23 after ADC/DAC reduced to 6 bits, and 4% best-case latency overhead.

## Language models evaluated
- Models: MobileBERT (25M), BERT-Base (108M), BERT-Large (334M), Llama-3.1-8B
- Scale: 25M-8B
- Note: MobileBERT, BERT-Base/Large and LLaMA-3.1 8B (all <=10B) evaluated with simulated PCM analog in-memory computing (noise and 10-year drift) using low-rank adapters; no hardware chip.

## Contributions
- AHWA-LoRA: freeze analog meta-weights, train digital LoRA adapters for hardware and task adaptation.
- Multi-task inference and on-chip adaptation on a single programmed AIMC chip by swapping adapters.
- Scalability evidence from MobileBERT to BERT-Large and Llama-3.1-8B (SFT and RL).
- Hybrid AIMC + RISC-V PMCA latency balancing study showing as little as 4% per-layer overhead.

## Key claims (stable IDs)
- **2026_Li_AHWA-LoRA_NeuromorphComputEng#C1** — AHWA-LoRA matches full AHWA on MobileBERT/SQuAD under drift. — _support:_ 10-year drift F1 85.36 vs 85.14, EM 76.92 vs 76.40 — _loc:_ Table I
- **2026_Li_AHWA-LoRA_NeuromorphComputEng#C2** — Trainable parameters reduced more than 15x and GPU memory by 13% (over 4 GB). — _support:_ about 1M LoRA params vs 24.67M — _loc:_ Table II
- **2026_Li_AHWA-LoRA_NeuromorphComputEng#C3** — Llama-3.1-8B analog GSM8K accuracy improves from 37.98% to 70.74% via RL with AHWA-LoRA (digital post-LoRA 85.06%). — _support:_ 3.0% noise during RL — _loc:_ Table V
- **2026_Li_AHWA-LoRA_NeuromorphComputEng#C4** — Best-case latency overhead of LoRA on PMCAs is 4% vs pure AIMC. — _support:_ balanced AIMC/PMCA pipeline; up to 2.72x at 128 ns for 512x128 layers — _loc:_ Fig. 4c
- **2026_Li_AHWA-LoRA_NeuromorphComputEng#C5** — Larger encoders are more robust to 10-year drift. — _support:_ BERT-Base -0.63 and BERT-Large -0.48 F1 vs about 4 points for MobileBERT — _loc:_ Fig. 3b

## Results
- MobileBERT SQuAD v1.1 baseline F1 89.47 / EM 82.42; AHWA-LoRA 89.06 at t=0 and 85.36 at 10 years (Table I).
- LoRA rank 8 chosen; 1.6M LoRA params (6.6%) for MobileBERT; BERT-Base 1.3M, BERT-Large 3.5M (about 1%).
- Eight GLUE tasks with 8 x 1.6M adapters: 38.1M total params vs (8x20.4+4.9)M for separate models.
- Llama-3.1-8B zero-shot HellaSwag gain up to 38.23 points after AHWA-LoRA vs pre-tuning analog (LoRA rank 16, 0.52% params).
- Dynamic adaptation: ADC/DAC 8->6 bit dropped F1 by about 25%; LoRA reload restored 60.81 to 74.23 at 10 years (Fig. 3a).
- PMCA memory need 8.2-21 KiB (128x128) and 70-172 KiB (512x128) vs 128 KiB TCDM (Fig. 4b).

## Key numbers
- array_size: 512x512 AIMC tiles
- throughput: AIMC tile integration time 128/256/512 ns
- accuracy: F1 85.36 SQuAD v1.1 at 10-year drift (MobileBERT); GSM8K 70.74% Llama-3.1-8B analog
- bits_weight: PCM differential, LoRA in FP
- bits_adc: 8b ADC/DAC

## Datasets / benchmarks
SQuAD v1.1, GLUE, Alpaca, GSM8K, HellaSwag, BoolQ, PIQA, WinoGrande, ARC, SciQ, COPA, OpenBookQA

## Limitations
- All accuracy results are simulation (AIHWKIT PCM model, Gaussian noise abstraction); no silicon.
- LLaMA experiments omit explicit ADC/DAC modeling and weight clipping, and RL uses reduced noise (3.0%).
- Analog-digital gap for Llama GSM8K remains about 15 points (2.5 at reduced evaluation noise).
- LoRA branch and attention remain digital; latency overhead depends on tile integration time and token parallelism and may need larger TCDM.

## Remarks
A practical weight-stationary deployment recipe: program once, absorb noise/drift and task changes in small digital adapters, which sidesteps PCM write cost and endurance. Evidence is strong for BERT-class models with a calibrated PCM simulator and weaker for the 8B LLM, where noise is abstracted. Complements full-model approaches such as Analog Foundation Models and mapping work like LionHeart in the collection.

## Use in the original review
- F5 (Medium confidence): Full-model analog retraining is not necessary. Analog hardware-aware LoRA freezes the analog-programmed weights as fixed meta-weights and trains only small external digital low-rank adapters, matching full HWA retraining within 1% F1/EM on SQuAD v1.1 and beating it after 10 years of simulated PCM drift (F1 85.36 vs 85.14; EM 76.92 vs 76.40). Adapter-swapping also mitigates the reprogramming problem: one analog base model serves many tasks, avoiding the error accumulation of repeated programming, with adapters refreshed off-chip and drift handled by global drift compensation.

## Cites (in collection, 14)
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "Analog In-Memory Computing (AIMC) has emerged as a promising computing paradigm to tackle these challenges, offering improved performance and energy-efficiency through computation directly within the memory array4,5."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "We used global drift compensation22 to mitigate temporal variations."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019) — _motivation_: "Analog devices are inherently non-deterministic and subject to temporal variations, impacting NN accuracy when deployed on AIMC-based accelerators7–10."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Analog devices are inherently non-deterministic and subject to temporal variations, impacting NN accuracy when deployed on AIMC-based accelerators7–10."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "To accurately model the behavior and constraints of AIMC hardware, we used AIHWKIT, an opensource simulator for AIMC devices21."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _motivation_: "Simulation results confirm that our method is effective on a 25.3M-parameter transformer model, a practical size suitable for deployment on currently available AIMC chips18,19."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _contrasts/critiques_: "conventional AHWA training methodologies typically optimize performance for only one task at a time12."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "Analog Hardware-Aware (AHWA) training techniques have been demonstrated to enhance model robustness under these constraints for various NN architectures, effectively mitigating accuracy losses by injecting Gaussian noise during forward-propagation and simulating circuit-non-idealities11–13."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _motivation_: "Simulation results confirm that our method is effective on a 25.3M-parameter transformer model, a practical size suitable for deployment on currently available AIMC chips18,19."
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024) — _background_: "Analog In-Memory Computing (AIMC) has emerged as a promising computing paradigm to tackle these challenges, offering improved performance and energy-efficiency through computation directly within the memory array4,5."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _background_: "Analog Hardware-Aware (AHWA) training techniques have been demonstrated to enhance model robustness under these constraints for various NN architectures, effectively mitigating accuracy losses by injecting Gaussian noise during forward-propagation and simulating circuit-non-idealities11–13."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _background_: "This challenge represents a typical resource allocation problem34."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _background_: "However, distinct properties of AIMC, namely device noise and circuit non-idealities, introduce additional complexity to NN training and deployment6."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _uses-method-or-tool_: "During inference, we evaluated model robustness against Gaussian noise applied to weights, following methodologies established in prior studies22,28."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Li_AHWA-LoRA_NeuromorphComputEng.pdf](../../11_Small_Language_Models_on_AIMC/2026_Li_AHWA-LoRA_NeuromorphComputEng.pdf)
- Full text: [../fulltext/2026_Li_AHWA-LoRA_NeuromorphComputEng.txt](../fulltext/2026_Li_AHWA-LoRA_NeuromorphComputEng.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1088/2634-4386/ae405e
