---
id: W4414758157
key: 2025_Krestinskaya_CIMNAS_TCASAI
title: "CIMNAS: A Joint Framework for Compute-In-Memory-Aware Neural Architecture Search"
short: "CIMNAS"
year: 2025
venue: "TCASAI"
venue_full: "IEEE Transactions on Circuits and Systems for Artificial Intelligence"
authors: "Olga Krestinskaya, Mohammed E. Fouda, Ahmed M. Eltawil, Khaled N. Salama"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM", "SRAM-analog"]
models: ["CNN", "MobileNet", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["nas-codesign", "mixed-precision", "quantization", "crossbar-architecture", "energy-efficiency", "simulator", "adc-dac", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 1
priority_score: 4.71
doi: "https://doi.org/10.1109/tcasai.2025.3617422"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2025_Krestinskaya_CIMNAS_TCASAI.pdf"
fulltext: "../fulltext/2025_Krestinskaya_CIMNAS_TCASAI.txt"
---

# CIMNAS

**CIMNAS: A Joint Framework for Compute-In-Memory-Aware Neural Architecture Search** — IEEE Transactions on Circuits and Systems for Artificial Intelligence (2025)

## TL;DR
CIMNAS jointly searches NN architecture, quantization and CIM device/circuit/architecture parameters (9.9e85 combinations) with an evolutionary algorithm, cutting MobileNet-on-RRAM EDAP by 90.1-104.5x at 73.81% ImageNet accuracy and ResNet50-on-SRAM EDAP by up to 819.5x.

## Summary
HW-NAS for CIM usually optimizes the model for fixed hardware or explores hardware for a fixed model. CIMNAS jointly searches (i) a MobileNetV2-based model space (5.9e38 configs), (ii) layer-wise weight/activation quantization, and (iii) a hierarchical CIM hardware space (1.4e7 configs: bits per cell, operating voltage, cycle time, crossbar size, ADC precision, macros per tile, tiles per router, tile groups per chip, global buffer size), totalling 9.9e85. An evolutionary (genetic) algorithm with feasibility-filtered initial population (P=150, G=70; 1.75-2.5 days on 64 CPU cores plus one GPU) is driven by a supernetwork-based accuracy predictor and per-layer hardware evaluation with the CiMLoop simulator (NeuroSim plug-in, Accelergy), at 32nm CMOS with RRAM devices and an 800 mm2 area constraint. Final accuracy comes from fine-tuning quantized models. It is compared to two baselines, a two-stage search and an XPert-like search, for EDAP, latency, and energy-area objectives. A SRAM 7nm ResNet50 experiment shows adaptability.

## Contributions
- Joint model-quantization-hardware search covering device, circuit and architecture parameters in a 9.9e85 space
- Evolutionary search with feasibility-aware sampling, accuracy predictor and CiMLoop-based hardware evaluation
- Large EDAP, TOPS/W and TOPS/mm2 gains without accuracy loss versus fixed baselines
- Comparison against two-stage and XPert-like searches, plus extension to SRAM ResNet50
- Open-source code

## Key claims (stable IDs)
- **2025_Krestinskaya_CIMNAS_TCASAI#C1** — EDAP-optimized CIMNAS reduces EDAP 90.1x-104.5x vs two baselines for MobileNetV2/RRAM — _support:_ 90.1-104.5x EDAP; 4.68-4.82x TOPS/W; 11.35-12.78x TOPS/mm2; 1.7-2.3x utilization; +0.81% accuracy; 73.81% ImageNet — _loc:_ Sec. V / Table III
- **2025_Krestinskaya_CIMNAS_TCASAI#C2** — Extension to SRAM-based ResNet50 at 7nm gives up to 819.5x EDAP reduction with ~0.6-0.8% accuracy drop — _support:_ 622.9-819.5x EDAP — _loc:_ Sec. V / Table I
- **2025_Krestinskaya_CIMNAS_TCASAI#C3** — Joint search beats two-stage and XPert-like sequential searches in balance of accuracy and hardware metrics, with greater design diversity — _support:_ XPert-like: 3.43% accuracy drop vs CIMNAS 1.5% in energy-area mode — _loc:_ Sec. V / Fig. 3
- **2025_Krestinskaya_CIMNAS_TCASAI#C4** — Latency-focused search cuts delay 2.5-4.7x while raising accuracy by 0.71% — _support:_ 2.5-4.7x — _loc:_ Sec. V

## Results
- EDAP down 90.1-104.5x, TOPS/W up 4.68-4.82x, TOPS/mm2 up 11.3-12.78x, 73.81% accuracy (MobileNet/ImageNet RRAM)
- Energy x area improved 68-313x with 1.5% accuracy reduction vs 3.43% for XPert-like search
- SRAM ResNet50: EDAP down up to 819.5x
- Search cost 1.75-2.5 days per run (64 cores + 1 GPU), 50 min per generation

## Key numbers
- tech_node: 32nm CMOS (RRAM); 7nm (SRAM ResNet50)
- array_size: searched parameter
- energy_eff: 4.68-4.82x TOPS/W improvement
- accuracy: 73.81% ImageNet (MobileNetV2)
- bits_weight: layerwise searched; 4-8 bits
- bits_adc: searched

## Datasets / benchmarks
ImageNet

## Limitations
- Simulated hardware metrics only (CiMLoop, ~3% error vs NeuroSim); no silicon
- Image classification CNNs only (MobileNetV2, ResNet50); no transformers or LMs
- Hardware non-idealities (noise, drift) not part of the objective
- Retraining/re-search needed when migrating to a new technology node; high search cost
- Baselines chosen by authors, so absolute multipliers depend on baseline quality

## Remarks
A strong demonstration of why joint co-design matters for CIM, but the evidence is simulation of CNNs. For SLM deployment the framework would need transformer search spaces, attention/KV mapping and noise-awareness. It builds on CiMLoop and positions itself against AnalogNAS, Gibbon, CoMN and XPert.

## Cites (in collection, 10)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Compute-In-Memory (CIM) neural network accelerators have emerged as promising architectures for achieving energyefficient AI processing [2–6]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _baseline/comparison_: "CiMLoop was selected for its relatively high simulation speed and accuracy close to that of NeuroSim [49], while 7 offering enhanced flexibility."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "Compute-In-Memory (CIM) neural network accelerators have emerged as promising architectures for achieving energyefficient AI processing [2–6]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _contrasts/critiques_: "In contrast, CIM-based design space exploration focuses on identifying the optimal CIM hardware parameters for deploying a fixed neural network model [18, 19, 23]."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _motivation_: "However, separately optimizing hardware parameters for high-accuracy models may result in suboptimal designs, as software-optimized models often lead to underutilized CIM-based hardware in deployment [25]."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _contrasts/critiques_: "Current state-of-the-art HW-NAS frameworks for CIM primarily focus on optimizing neural network models for hardware implementation [15–17], performing hardware design space exploration separately [9, 18, 19], or jointly optimizing model parameters with a limited set of hardware parameters [20, 21]."
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024) — _contrasts/critiques_: "In contrast, CIM-based design space exploration focuses on identifying the optimal CIM hardware parameters for deploying a fixed neural network model [18, 19, 23]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _motivation_: "To maximize the hardware efficiency of CIM accelerators and maintain high performance for neural network workloads, it is essential to co-optimize both neural network model parameters and CIM hardware parameters [7]."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _data/numbers_: "Specifically, CiMLoop achieves an average error of approximately 3% in hardware estimations [46]."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _background_: "Similarly, several frameworks optimize quantization policies to enhance the performance of CIM-based architectures [29–31]."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2025_Krestinskaya_CIMNAS_TCASAI.pdf](../../05_Mapping_Compilation_and_Dataflow/2025_Krestinskaya_CIMNAS_TCASAI.pdf)
- Full text: [../fulltext/2025_Krestinskaya_CIMNAS_TCASAI.txt](../fulltext/2025_Krestinskaya_CIMNAS_TCASAI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcasai.2025.3617422
