---
id: W4414008085
key: 2025_Zhang_ASiM_TVLSI
title: "ASiM: Modeling and Analyzing Inference Accuracy of SRAM-Based Analog CiM Circuits"
short: "ASiM"
year: 2025
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems"
authors: "Wenlun Zhang, Shimpei Ando, Yung-Chin Chen, Kentaro Yoshioka"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-analog", "Charge/Capacitor"]
models: ["CNN", "ResNet", "Transformer", "ViT"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "benchmarking", "adc-dac", "read-write-noise", "noise-injection", "bit-slicing", "heterogeneous-analog-digital", "hardware-aware-training"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 5
citations_overall: 12
priority_score: 5.18
doi: "https://doi.org/10.1109/tvlsi.2025.3605286"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2025_Zhang_ASiM_TVLSI.pdf"
fulltext: "../fulltext/2025_Zhang_ASiM_TVLSI.txt"
---

# ASiM

**ASiM: Modeling and Analyzing Inference Accuracy of SRAM-Based Analog CiM Circuits** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2025)

## TL;DR
ASiM is an open-source PyTorch framework modelling ADC quantisation, bit-parallel encoding and analog noise of charge-domain SRAM analog CiM, showing that even 1 LSB of analog noise badly hurts ImageNet accuracy and that hybrid analog-digital MSB execution or majority voting restores it.

## Summary
Existing simulators (MLP/DNN+NeuroSim, CIMUFAS, AIHWKIT, Saikia's model) rarely target SRAM charge-domain ACiM and use Min-Max ADC ranges and uniform data assumptions that give optimistic accuracy. ASiM models SRAM charge-domain ACiM: bit-serial and bit-parallel execution, full-dynamic-range ADC quantisation, Gaussian analog noise injected per binary MAC cycle, nonlinearity, using actual weight/activation distributions to estimate CSNR. It integrates with PyTorch as a plug-and-play layer, supports QAT (8b/8b) and noise-aware training (NAT, O_noisy = O(1+eta) with Gaussian eta) and CNN and Transformer models. Workloads are ResNet-18 and ViT-B-32 on CIFAR-10 and ImageNet with a 256-row-parallel macro as the default. Analysis shows ADC precision requirements are higher for ViT than ResNet and for ImageNet than CIFAR-10, bit-parallel encoding trades energy for noise sensitivity, and the largest errors occur in MSB cycles. Two fixes are proposed: Hybrid CiM (MSB cycles processed digitally, rest analog) and majority voting by oversampling MSB cycles. ASiM is compared with real ACiM prototype error distributions (simulation-to-silicon correlation) and used to benchmark published ACiM designs under a common 8b/8b ResNet-18.

## Contributions
- Open-source PyTorch simulator for SRAM charge-domain ACiM accuracy with Transformer support
- Revised CSNR estimation using real data distributions instead of uniform assumptions
- Analysis of ADC precision, bit-parallel encoding and analog noise (random and nonlinear) on ResNet-18 and ViT-B-32
- Hybrid CiM and majority-voting techniques to protect MSB cycles
- Cross-comparison of state-of-the-art ACiM designs and simulator comparison table

## Key claims (stable IDs)
- **2025_Zhang_ASiM_TVLSI#C1** — ADC readout error of just 1 LSB in MSB cycles causes severe inference degradation — _support:_ MSB error 0->1 vs LSB error 18->19 illustration and noise sweeps — _loc:_ Sec. IV-C, Figs. 9-10
- **2025_Zhang_ASiM_TVLSI#C2** — Transformers and ImageNet are more sensitive to ADC precision than CNNs on CIFAR-10 — _support:_ ResNet-18/CIFAR-10 tolerates ADC 2 bits below boundary; ImageNet loses ~10% at 1 bit below; ViT-B-32 goes near random guessing — _loc:_ Sec. IV-B, Fig. 6
- **2025_Zhang_ASiM_TVLSI#C3** — Bit-parallel encoding improves energy efficiency but increases noise sensitivity — _support:_ Bit-serial vs Enc=2/Enc=4 accuracy tables for ResNet-18 and ViT-B-32 — _loc:_ Sec. IV, Fig. 10
- **2025_Zhang_ASiM_TVLSI#C4** — Hybrid CiM restores near-baseline accuracy with most cycles still analog — _support:_ Boundary level 3, noise 0.8 LSBrms; >40% analog cycles suffice for ViT-B-32 on ImageNet — _loc:_ Sec. V-A, Fig. 13
- **2025_Zhang_ASiM_TVLSI#C5** — NeuroSim's Min-Max ADC ranging gives overly optimistic accuracy — _support:_ ASiM models full dynamic range and actual variance — _loc:_ Sec. III-C, Table I

## Results
- ResNet-18 CIFAR-10 FP baseline 92.08%; ImageNet 65.49%; ViT-B-32 CIFAR-10 95.26%; ImageNet 68.17% (baselines in ADC tables)
- ResNet-18 ImageNet with ADC precision reduction: bit-serial 65.51 at higher precision, down to 16.26 for a low-precision encoded case
- HCiM gains 182%, 140%, 110%, 90% TOPS/W over full DCiM at the stated row-parallelisms (Sec. V-A)
- Hybrid ACiM energy-efficiency gain scales up to 7x as row-parallelism increases to 1024 (cited from [4])
- Models trained with NAT at 40-100% noise intensity per model/dataset (Fig. 9 Shmoo plots)

## Key numbers
- array_size: 256-row parallelism
- energy_eff: HCiM +90% to +182% TOPS/W over full DCiM
- accuracy: ResNet-18: 92.08% CIFAR-10 / 65.49% ImageNet; ViT-B-32: 95.26% / 68.17%
- bits_weight: 8b
- bits_adc: 8-12b swept

## Datasets / benchmarks
CIFAR-10, ImageNet

## Limitations
- SRAM charge-domain focus; not NVM crossbars, no drift or programming variation
- Only ResNet-18 and ViT-B-32 evaluated; no language models
- Noise models (random Gaussian per cycle, nonlinearity) calibrated to a few prototypes; limited silicon correlation data
- Mitigation techniques (HCiM, majority voting) add digital cycles and control complexity
- Arxiv preprint v4 text; some table values hard to parse from extraction

## Remarks
Useful cautionary evidence that analog noise at the LSB level in MSB cycles, not quantisation noise, dominates accuracy loss for harder tasks and Transformers. For NVM crossbar LMs the finding transfers conceptually (bit-significance-aware protection of MSBs, ADC precision scaling), but device-level effects are absent. Complements AIHWKIT-style NVM simulators in the collection.

## Cites (in collection, 5)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _extends/builds-on_: "Jia [24] used randomly generated weight and activation vectors, comparing the post-quantization output to the ideal full-precision output to measure the SQNR of a real device"
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _contrasts/critiques_: "NeuroSim [14, 31] quantizes ADC outputs based on the Min-Max range of MAC results, which leads to overly optimistic estimations of ADC rounding effects and the corresponding impact of analog noise."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _background_: "Fundamental architecture and MAC operation of ACiM. (a) Bit-serial ACiM. (b) Bit-parallel ACiM. inference accuracy [17–20]."
- [2023_Sun_AIMCvsDIMC_ICCAD](2023_Sun_AIMCvsDIMC_ICCAD.md) AIMC-vs-DIMC (ZigZag-IMC) (2023) — _background_: "Among CiM architectures, Analog Compute-in-Memory (ACiM) offers high computational density and energy efficiency by leveraging the analog properties of memory cells to perform Multiply-and-ACcumulate (MAC) operations directly in the analog domain [4]."
- [2024_Yoshioka_CRCIM_JSSC](2024_Yoshioka_CRCIM_JSSC.md) CR-CIM (2024) — _extends/builds-on_: "Yoshioka [25] extended this approach by introducing analog Gaussian noise into each binary MAC cycle to estimate the actual CSNR of ACiM chips."

## Cited by (in collection, 1)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2025_Zhang_ASiM_TVLSI.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2025_Zhang_ASiM_TVLSI.pdf)
- Full text: [../fulltext/2025_Zhang_ASiM_TVLSI.txt](../fulltext/2025_Zhang_ASiM_TVLSI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tvlsi.2025.3605286
