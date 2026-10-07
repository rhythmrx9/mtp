---
id: W4385679805
key: 2023_Cao_RRAMPoolFormer_ISCAS
title: "RRAM-PoolFormer: A Resistive Memristor-based PoolFormer Modeling and Training Framework for Edge-AI Applications"
short: "RRAM-PoolFormer"
year: 2023
venue: "ISCAS"
venue_full: "2023 IEEE International Symposium on Circuits and Systems (ISCAS 2023)"
authors: "Tiancheng Cao, Weihao Yu, Yuan Gao, Chen Liu, Shuicheng Yan, Wang Ling Goh"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["Transformer", "ViT"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "noise-injection", "ir-drop-parasitics", "device-variation", "weight-mapping", "transformer-accelerator", "edge-ai", "quantization"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 9
priority_score: 4.2
doi: "https://doi.org/10.1109/iscas46773.2023.10181612"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2023_Cao_RRAMPoolFormer_ISCAS.pdf"
fulltext: "../fulltext/2023_Cao_RRAMPoolFormer_ISCAS.txt"
---

# RRAM-PoolFormer

**RRAM-PoolFormer: A Resistive Memristor-based PoolFormer Modeling and Training Framework for Edge-AI Applications** — 2023 IEEE International Symposium on Circuits and Systems (ISCAS 2023) (2023)

## TL;DR
A 16-block, 0.26M-weight PoolFormer (pooling token mixer, LayerNorm replaced by channel scaling) is trained with RRAM non-idealities in the loop for 4-level 64x64 TaOx crossbars, reaching 85.86% CIFAR-10 accuracy (<4% below FP64) with 15% device variation and 0.5 Ohm line resistance.

## Summary
The paper adapts PoolFormer (MetaFormer with a parameter-free pooling token mixer instead of self-attention) to resistive crossbars for edge AI, since pooling removes the dynamic attention matmuls that are awkward on NVM. The network has 2 stages (12 and 4 blocks), embedding dims 32 and 64, token grids 16x16 and 8x8, patch embedding implemented as unfolded patches fed to a crossbar (3x3 patches, stride 2), channel MLP (C to 4C to C with ReLU) mapped directly on arrays, and LayerNorm replaced by learnable per-channel scaling. Signed weights use two cells per weight (G+ and G-) with differential current sensing. The training framework (Python/PyTorch) injects device non-idealities each training cycle: random programming-failure masks (failed cells forced to HRS), conductance variation and nonlinearity, plus array-level sneak path and line-resistance effects via a fast scaling-factor-matrix IR-drop model with O(mn) complexity (vs O(m2n2) for iterative solvers), and peripheral readout circuit effects. The device model uses measured TaOx 2T1R 64x64 crossbar data with 4 resistance levels from 5 kOhm to 30 kOhm. Training took 2.7 h on a 16-core CPU; results are compared with conventional offline training and with CNN-based memristor accelerators.

## Contributions
- Hardware-friendly PoolFormer for crossbars (pooling token mixer, channel scaling instead of LayerNorm)
- Non-ideality-aware training framework covering device, array and readout circuits
- Fast parasitic (IR-drop) model with O(mn) complexity
- Demonstration with measured 64x64 RRAM data: 0.26M weights, 85.86% CIFAR-10

## Key claims (stable IDs)
- **2023_Cao_RRAMPoolFormer_ISCAS#C1** — 85.86% CIFAR-10 accuracy with 4-level devices and 15% variation — _support:_ 64x64 array, 0.5 Ohm line resistance, within 500 epochs, <4% below FP64 — _loc:_ Sec. IV, Fig. 5
- **2023_Cao_RRAMPoolFormer_ISCAS#C2** — 2-bit weights lose only ~3% with non-ideality-aware training, unlike offline training — _support:_ Fig. 6 — _loc:_ Sec. IV
- **2023_Cao_RRAMPoolFormer_ISCAS#C3** — Line resistance up to 2 Ohm costs <1% accuracy with the proposed training — _support:_ conventional training drops substantially — _loc:_ Fig. 7
- **2023_Cao_RRAMPoolFormer_ISCAS#C4** — Network is at least 10x smaller than CNN memristor accelerators — _support:_ 0.26M vs 6.6M-13M weights (Table I) — _loc:_ Table I

## Results
- 85.86% CIFAR-10, 4 levels (5-30 kOhm), 64x64 array, 15% variation, 0.5 Ohm line resistance
- Weights 0.26M versus 7.66M, 6.6M, 13M, 13M for prior CNN works at similar accuracy (85.2%, 85.17%)
- Training time 2.7 h on a 16-core Ryzen 5800H CPU

## Key numbers
- array_size: 64x64
- accuracy: 85.86% CIFAR-10 (4-level weights; <4% below FP64)
- bits_weight: 4 levels (2b) per cell, differential pair

## Datasets / benchmarks
CIFAR-10

## Limitations
- Image classification on CIFAR-10 only; pooling token mixer is not self-attention, so no language-model or attention-on-crossbar evidence
- Pure simulation with a device model fitted to measured data; no chip
- Comparison against CNNs from different groups with differing device assumptions
- Accuracy (85.9%) well below modern ViT/CNN results on CIFAR-10
- Peripheral (ADC) quantisation effects are not detailed in the text

## Remarks
Shows one pragmatic route to put 'transformer-like' models on crossbars: drop attention and normalisation and train noise-aware. Useful as a contrast with attention-preserving approaches (ReTransformer, TReX); for SLMs it indicates that removing dynamic matmuls simplifies mapping but forfeits LM capability. Evidence is small-scale simulation.

## Cites (in collection, 6)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _uses-method-or-tool_: "The two-cell-one-weight method depicted is thus used [16]."
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020) — _baseline/comparison_: "The results of this study are summarized and compared to other recent memristor crossbar DNN solutions in Table I (including XB-SIM [27])."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _contrasts/critiques_: "For example, the self-attention operation is decomposed to reduce the frequency of intermediate results reloading and transfers the Softmax function to logical inference with lookup table [24]. However, these reported solutions still require considerable computation resources."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _baseline/comparison_: "The results of this study are summarized and compared to other recent memristor crossbar DNN solutions in Table I (including DNN+NeuroSim V2.0 [28])."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _background_: "The implementations of Transformer structure on memristor crossbar array have been reported in literature [23]."
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022) — _extends/builds-on_: "After the weight mapping to crossbar array, the non-idealities-aware training is carried out [31]."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2023_Cao_RRAMPoolFormer_ISCAS.pdf](../../07_Hardware_Aware_Training_and_Robustness/2023_Cao_RRAMPoolFormer_ISCAS.pdf)
- Full text: [../fulltext/2023_Cao_RRAMPoolFormer_ISCAS.txt](../fulltext/2023_Cao_RRAMPoolFormer_ISCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iscas46773.2023.10181612
