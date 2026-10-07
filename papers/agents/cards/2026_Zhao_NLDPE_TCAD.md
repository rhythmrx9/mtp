---
id: W7162655367
key: 2026_Zhao_NLDPE_TCAD
title: "NL-DPE: An Analog In-memory Non-Linear Dot Product Engine for Efficient CNN and LLM Inference"
short: "NL-DPE"
year: 2026
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2026"
authors: "Lei Zhao, Luca Buonanno, Archit Gajjar, John Moon, Aishwarya Natarajan, Sergey Serebryakov, Ron M. Roth, Xia Sheng, Youtao Zhang, Paolo Faraboschi, Jim Ignowski, Giacomo Pedretti"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["CNN", "Transformer", "BERT", "GPT/LLM"]
lm_models: ["BERT-tiny", "BERT-base", "Llama-3.2-1B", "Llama-3.2-3B"]
param_scale: "4M-3B"
slm: true
evidence: simulation
topics: ["analog-mvm", "nonlinear-functions", "attention", "adc-dac", "noise-injection", "hardware-aware-training", "language-models", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/tcad.2026.3698009"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Zhao_NLDPE_TCAD.pdf"
fulltext: "../fulltext/2026_Zhao_NLDPE_TCAD.txt"
---

# NL-DPE

**NL-DPE: An Analog In-memory Non-Linear Dot Product Engine for Efficient CNN and LLM Inference** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2026 (2026)

## TL;DR
NL-DPE pairs RRAM crossbars with RRAM analog CAM (ACAM) decision-tree engines to compute non-linear functions and data-dependent matmuls in analog without ADCs, reporting 28x energy efficiency and 249x speedup over an H100 (about 100x for Llama-3.2-1B/3B) in simulation.

## Summary
Standard RRAM IMC accelerators handle only static VMMs; activations, Softmax and attention's data-dependent matmuls (DMMul) fall to digital VFUs behind power-hungry ADCs, which dominate energy for BERT (Fig. 1). NL-DPE adds an ACAM unit per crossbar column that evaluates per-bit decision trees: any 8-bit function (sigmoid, tanh, SiLU, GELU, ReLU) is learned as a DT mapped to ~130 ACAM cells (Table I), and DMMul and Softmax are decomposed into log/exp operations plus additions so attention runs without rewriting crossbars. Weights are stored in 256x256 crossbars (two for positive, two for negative weights, analog slicing), 8 cores per tile, with 8-bit precision and conductance range 0.01-150 uS. To handle RRAM noise they propose software Noise-Aware Fine-tuning (NAF): each DT is fine-tuned independently with noise models calibrated on fabricated TaOx RRAM devices, with no post-deployment calibration. Evaluation uses CiMLoop in 32nm (SPICE-based 16nm ACAM/crossbar models) against H100 (TensorRT INT8), Eyeriss, ISAAC, RAELLA and BRAHMS on CIFAR-10/ImageNet CNNs, BERT-tiny/base on GLUE, and Llama-3.2-1B/3B using multi-chip setups (3 and 8 chips). NL-DPE gives 112x speedup and 28x energy efficiency at batch size 1 and 249x speedup at large batch on BERT.

## Language models evaluated
- Models: BERT-tiny, BERT-base, Llama-3.2-1B, Llama-3.2-3B
- Scale: 4M-3B
- Note: RRAM crossbars for VMM plus RRAM analog CAM (decision-tree) units for non-linear functions, softmax and data-dependent matmul, removing ADCs; evaluated on BERT-tiny/base (GLUE) and Llama-3.2-1B/3B scalability (3 and 8 chips) via CiMLoop simulation. Genuinely analog in-memory compute including attention.

## Contributions
- ACAM-based analog engine that executes arbitrary non-linear functions and DMMul/Softmax via decision trees and log/exp decomposition, removing ADCs
- Per-DT Noise-Aware Fine-tuning using noise models from fabricated RRAM, no in-device calibration
- Gray-encoded compact ACAM and a flash-style non-linear ADC comparison (Table VI)
- System-level evaluation on CNNs, BERT and Llama-3.2 with multi-chip scaling

## Key claims (stable IDs)
- **2026_Zhao_NLDPE_TCAD#C1** — NL-DPE delivers large energy and latency gains over GPU and prior IMC accelerators — _support:_ 28x energy efficiency, 249x speedup vs GPU; 22x and 245x vs existing IMC accelerators — _loc:_ Abstract, Sec. VI-E, Fig. 11
- **2026_Zhao_NLDPE_TCAD#C2** — Scales to Llama-3.2 1B/3B with multi-chip deployment — _support:_ ~100x speedup and energy efficiency vs GPU; 3 chips (1B), 8 chips (3B); C2C energy share 18% (1B) and 35% (3B) — _loc:_ Sec. VI-F, Fig. 13(a)
- **2026_Zhao_NLDPE_TCAD#C3** — ACAM replaces ADC and activation units at much lower cost — _support:_ 98% lower power and 86x smaller area vs 8-bit ADC + FlexSFU at 16nm — _loc:_ Sec. VI-B, Table IV
- **2026_Zhao_NLDPE_TCAD#C4** — 8-bit precision is sufficient after NAF — _support:_ below 7 bits accuracy drops >50% even with NAF; 8-bit matches full precision for BERT-base — _loc:_ Sec. VI-A2, Fig. 10(b)
- **2026_Zhao_NLDPE_TCAD#C5** — Accuracy is robust to stuck-at faults up to 5% — _support:_ both mapping variants near-ideal up to 5% faults — _loc:_ Fig. 16

## Results
- BS=1: 112x faster and 28x more energy efficient than H100; 249x speedup for multi-batch BERT (Fig. 11)
- Llama-3.2-1B/3B: ~100x speedup and energy gain over GPU even with conservative 10 Gbps, 30 pJ/bit chip-to-chip links (Fig. 13a)
- ACAM cell: 0.72 um2, ~0.44 fJ/search, ~300 ps search (Sec. V)
- ACAM 8-bit multiplier vs digital: 5% less power and 27% smaller than fixed-point; 68% lower power and 98% smaller than floating-point (Table V)
- Ramp ADC of [18] is 20-24% better in Walden FOM; proposed flash ACAM ADC has 2.26x smaller area and 1 GS/s (Table VI)
- Accuracy tables show FP32-level accuracy after NAF for CNNs and BERT on GLUE; ACAM noise without NAF causes significant degradation (Table III)

## Key numbers
- tech_node: 16nm (ACAM/crossbar SPICE), 32nm (system, CiMLoop)
- array_size: 256x256 crossbars; 86x12 ACAM array
- energy_eff: 28x vs H100
- throughput: 249x speedup vs H100 (BERT)
- accuracy: software-equivalent after NAF for BERT-base GLUE (Table III)
- bits_weight: 8b
- bits_adc: ADC-less (ACAM, 8-bit)

## Datasets / benchmarks
CIFAR-10, ImageNet, GLUE

## Limitations
- Simulation only (CiMLoop, SPICE-derived component models); no fabricated NL-DPE chip
- Llama-3.2 evaluation reports speed/energy but no accuracy validation (accuracy shown for CNNs and BERT)
- NAF fine-tunes DTs on synthetic data; larger error from ACAM noise at >1.5x noise std (Fig. 15)
- Noise models from TaOx RRAM with negligible drift; drift-prone devices only discussed
- Layer norm needs a VFU (or Dynamic Tanh) and max pooling uses comparators; multi-chip needed for 1B+ models

## Remarks
One of the more complete proposals for performing attention fully in the analog domain, which matters for small language models because it avoids repeated crossbar reprogramming for QK^T and softmax. Gains are large but come from simulation with idealized baselines (GPU at BS=1) and the Llama results lack quality metrics, so the SLM claim is about efficiency, not accuracy. Related to RACE-IT and other ACAM/attention work in the collection, and complements ISAAC/RAELLA-style ADC-reduction.

## Cites (in collection, 8)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _motivation_: "While studies have shown that AI models exhibit inherent tolerance to various errors, including conductance noises, real hardware [1, 15, 16] demonstrate that resistance noises play a crucial role in determining the model's accuracy."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "The development of in-memory computing (IMC) accelerators, particularly those based on resistive memories, such as RRAM [1], Phase Change Memories (PCM) [2], and FeFET [3], stand out as one of the most promising solutions due to their potential for high energy efficiency and scalability."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _motivation_: "Unfortunately, ADCs are both energy- and area-inefficient, consuming more than 30% of the chip area and accounting for over 50% of the total power consumption [4, 5]."
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017) — _background_: "The development of in-memory computing (IMC) accelerators, particularly those based on resistive memories, such as RRAM [1], Phase Change Memories (PCM) [2], and FeFET [3], stand out as one of the most promising solutions due to their potential for high energy efficiency and scalability."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _baseline/comparison_: "To understand the inefficiency of RRAM-based IMC accelerators for evolving AI models, we analyze the energy consumption breakdown of ISAAC [4] and RAELLA [6]."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021) — _contrasts/critiques_: "Recently proposed IMC designs [7, 8] strive to eliminate ADCs but work only if the AI model contains ReLU-like non-linear functions, and thus lack the flexibility to adapt to evolving AI models."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _uses-method-or-tool_: "NL-DPE and all baselines are simulated in 32nm using CiMLoop [10]."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _extends/builds-on_: "To address this challenge, we propose a differentiable approximation of the DT computation based on its implementation in ACAM [21, 23, 24]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Zhao_NLDPE_TCAD.pdf](../../11_Small_Language_Models_on_AIMC/2026_Zhao_NLDPE_TCAD.pdf)
- Full text: [../fulltext/2026_Zhao_NLDPE_TCAD.txt](../fulltext/2026_Zhao_NLDPE_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2026.3698009
