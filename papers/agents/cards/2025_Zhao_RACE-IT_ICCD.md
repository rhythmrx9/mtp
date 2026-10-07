---
id: W7117584415
key: 2025_Zhao_RACE-IT_ICCD
title: "RACE-IT: A Reconfigurable Analog Computing Engine for In-Memory Transformer Acceleration"
short: "RACE-IT"
year: 2025
venue: "ICCD"
venue_full: "2025 IEEE 43rd International Conference on Computer Design (ICCD 2025)"
authors: "Lei Zhao, Aishwarya Natarajan, Luca Buonanno, Archit Gajjar, Ron M. Roth, Sergey Serebryakov, John Moon, Omar Eldash, Jim Ignowski, Giacomo Pedretti"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer", "BERT", "CNN", "GPT/LLM"]
lm_models: ["BERT-base", "LLaMA3.2-1B", "LLaMA3.2-3B"]
param_scale: "110M-3B"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "nonlinear-functions", "attention", "noise-injection", "hardware-aware-training", "peripheral-circuits", "language-models", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 9
citations_overall: 1
priority_score: 8.11
doi: "https://doi.org/10.1109/iccd65941.2025.00021"
pdf: "../../04_Transformers_and_LLMs/2025_Zhao_RACE-IT_ICCD.pdf"
fulltext: "../fulltext/2025_Zhao_RACE-IT_ICCD.txt"
---

# RACE-IT

**RACE-IT: A Reconfigurable Analog Computing Engine for In-Memory Transformer Acceleration** — 2025 IEEE 43rd International Conference on Computer Design (ICCD 2025) (2025)

## TL;DR
RACE-IT uses reprogrammable RRAM analog content-addressable memory (ACAM) arrays to compute activations, Softmax and data-dependent matmuls in the analog domain, reporting 453x speedup and 354x energy saving over GPUs and 15x/122x over prior Transformer IMC accelerators.

## Summary
Crossbar IMC accelerates VMMs but Transformers also need GeLU-like activations, Softmax and data-dependent matrix multiplications (DMMul), which ISAAC (fixed CMOS logic), PUMA (programmable digital VFUs) or ReTransformer (write inputs into crossbars, hitting RRAM write endurance) handle poorly. RACE builds on RRAM analog CAM: each row encodes one output bit of an arbitrary function as input ranges stored as conductances, so reprogramming the ranges changes the function (one-variable 8-bit and two-variable 4-bit comparison modes). A Gray-code output encoding with 'don't care' cells shrinks arrays (depth 3 minimises array size and EDP, giving 8x50 arrays). Weights sit in ISAAC-style RRAM crossbars (analog slicing, 0.1-150 uS conductance range, 22 nm CMOS with TaOx RRAM noise data), with each tile also holding a RACE unit (four 8x50 arrays) plus adders, registers and XOR Gray decoding. A noise-aware fine-tuning (NAF) method uses differentiable ReLU-product approximations of range comparisons so bounds stored in RACE cells can be trained under ACAM noise. Evaluation covers accuracy (EfficientNet CIFAR-10, BERT-base GLUE) and Timeloop+Accelergy performance/energy against H100, Eyeriss+Flex-SFU, PUMA and ReTransformer, plus scaling to LLaMA3.2 1B/3B using multi-chip setups.

## Language models evaluated
- Models: BERT-base, LLaMA3.2-1B, LLaMA3.2-3B
- Scale: 110M-3B

## Contributions
- RACE: reconfigurable ACAM-based analog engine supporting arbitrary functions
- Gray-code output encoding that reduces RACE array size and EDP
- 22 nm cell layout and SPICE validation of two-variable comparison
- Noise-aware fine-tuning with a new differentiable two-variable comparison formulation
- Full RACE-IT accelerator evaluated against GPU, systolic array and IMC baselines

## Key claims (stable IDs)
- **2025_Zhao_RACE-IT_ICCD#C1** — RACE-IT gives 453x speedup and 354x energy savings over H100 at batch size 1 — _support:_ average across models — _loc:_ Sec. VIII-C, Fig. 11(b,c)
- **2025_Zhao_RACE-IT_ICCD#C2** — 15x performance and 122x energy reduction over existing Transformer-specific IMC accelerators — _support:_ stated in abstract — _loc:_ Abstract
- **2025_Zhao_RACE-IT_ICCD#C3** — NAF recovers accuracy lost to RACE noise — _support:_ EfficientNet CIFAR-10 70.25 (RACE noise) -> 89.37 (NAF) vs FP32 91.15; BERT MNLI 77.42 -> 82.09 vs FP32 84.2 — _loc:_ Table III
- **2025_Zhao_RACE-IT_ICCD#C4** — Gray code depth 3 minimises array size and EDP; RACE arrays are 8x50 — _support:_ design-space exploration for 4-bit multiplication — _loc:_ Sec. VIII-B, Fig. 11(a)
- **2025_Zhao_RACE-IT_ICCD#C5** — Crossbar noise has negligible accuracy impact thanks to analog slicing — _support:_ BERT-base GLUE and EfficientNet unchanged in 'Crossbar noise' row — _loc:_ Sec. VIII-A, Table III

## Results
- BERT-base GLUE: MNLI 84.2 (FP32) / 77.42 (RACE noise) / 82.09 (NAF); SST-2 92.43 / 91.36 / 91.69; QQP 90.92 / 89.27 / 90.11; RTE 64.98 / 62.05 / 64.81
- EfficientNet CIFAR-10: 91.15 FP32, 89.32 8-bit quant, 70.25 RACE noise, 89.37 NAF
- BERT-base fits one chip; LLaMA3.2-1B needs 3 chips and 3B needs 8 chips; assumes 10 Gbps, 30 pJ/bit chip-to-chip links yet still hundreds-fold speedup/energy saving over GPU (Fig. 11(d))
- RACE unit = 4 arrays of 8x50, with XOR Gray decoding
- Quantising activations/Softmax/DMMul outputs to 8 bits is required because RACE outputs 8 bits (small accuracy cost)

## Key numbers
- tech_node: 22nm (GF22FDX) with TaOx RRAM
- array_size: RACE array 8x50
- energy_eff: 354x energy savings vs H100; 122x vs Transformer IMC accelerators
- throughput: 453x speedup vs H100 (BS=1); 15x vs Transformer IMC accelerators
- accuracy: BERT-base MNLI 82.09 with NAF (84.2 FP32); EfficientNet CIFAR-10 89.37%
- bits_weight: analog sliced weights, conductance 0.1-150 uS
- bits_adc: 8b outputs from RACE

## Datasets / benchmarks
GLUE, CIFAR-10

## Limitations
- Simulation only; ACAM noise models extrapolated from device data in earlier work
- LLaMA models only used for performance scaling, no LM accuracy results under noise
- Outputs limited to 8 bits; large lookup-style functions need many ranges
- Multi-chip needed for >100M-parameter models; 3-8 chips for 1B-3B LLaMA, with chip-to-chip cost assumed
- Comparison baselines augmented by the authors (Flex-SFU) and evaluated with the same Timeloop framework, so speedups depend on modelling choices

## Remarks
Addresses a genuine gap for analog LMs: the non-VMM operators (activations, Softmax, DMMul) that dominate once crossbars make VMM cheap. Using ACAM to compute them in the analog domain is novel, but evidence is simulation with noise models from prior device papers. Of note for the SLM theme: BERT-base GLUE degradation under RACE noise is measurable (MNLI -6.8 points) and NAF recovers most of it, while LLaMA 1B/3B results are only throughput/energy.

## Cites (in collection, 9)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "The second approach, adopted by architectures such as PUMA [13], introduces programmable digital Vector Functional Units (VFUs) to support a wide range of operations. However, this programmability comes at the cost of performance, particularly for DMMuls in Transformer models."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _contrasts/critiques_: "The third approach, as demonstrated in ReTransformer [6], directly computes DMMuls and Softmax within RRAM crossbars by programming the inputs into the array. While promising, it suffers from the inherent drawbacks of RRAM’s slow writes and limited endurance [19]."
- [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) Area-Efficient Multi-Task BERT (2021) — _background_: "In-memory Computing (IMC) stands out as a promising solution to alleviate the computational and memory challenges posed by Transformer models [6–8]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "The first is an adhoc strategy that integrates specialized CMOS-based units tailored to specific workloads, as exemplified by ISAAC [9]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "High-performance silicon demonstrations of multi-core IMC accelerators using RRAM [16] and PCM [17] have been recently presented, finally grounding years of research in experimental measurements."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "High-performance silicon demonstrations of multi-core IMC accelerators using RRAM [16] and PCM [17] have been recently presented, finally grounding years of research in experimental measurements."
- [2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC](2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.md) Reconfigurable Sparse-Attention NVPIM (2023) — _background_: "In-memory Computing (IMC) stands out as a promising solution to alleviate the computational and memory challenges posed by Transformer models [6–8]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _data/numbers_: "While the figure shows a small 3 × 3 crossbar for clarity, practical systems often use multiple much larger arrays (e.g., 512×256 [18]) to exploit massive parallelism."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Crossbar-based VMM Computing Engine RRAM is an emerging non-volatile memory technology with strong potential for accelerating VMMs when arranged in crossbar arrays [19]."

## Cited by (in collection, 1)
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _extends/builds-on_: "To address this challenge, we propose a differentiable approximation of the DT computation based on its implementation in ACAM [21, 23, 24]."

## Files
- PDF: [../../04_Transformers_and_LLMs/2025_Zhao_RACE-IT_ICCD.pdf](../../04_Transformers_and_LLMs/2025_Zhao_RACE-IT_ICCD.pdf)
- Full text: [../fulltext/2025_Zhao_RACE-IT_ICCD.txt](../fulltext/2025_Zhao_RACE-IT_ICCD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccd65941.2025.00021
