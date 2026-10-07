---
id: W4360831836
key: 2023_Kim_INCA_HPCA
title: "INCA: Input-stationary Dataflow at Outside-the-box Thinking about Deep Learning Accelerators"
short: "INCA"
year: 2023
venue: "HPCA"
venue_full: "IEEE International Symposium on High-Performance Computer Architecture (HPCA 2023)"
authors: "Bokyung Kim, Shiyu Li, Hai Helen Li"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "dataflow-pipelining", "weight-mapping", "on-chip-training", "3d-integration", "adc-dac", "energy-efficiency", "device-variation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 11
citations_overall: 28
priority_score: 5.02
doi: "https://doi.org/10.1109/hpca56546.2023.10070992"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Kim_INCA_HPCA.pdf"
fulltext: "../fulltext/2023_Kim_INCA_HPCA.txt"
---

# INCA

**INCA: Input-stationary Dataflow at Outside-the-box Thinking about Deep Learning Accelerators** — IEEE International Symposium on High-Performance Computer Architecture (HPCA 2023) (2023)

## TL;DR
INCA is the first input-stationary RRAM crossbar accelerator (2T1R cells in 3D RRAM storing activations, streaming weights), giving up to 20.6x/260x energy efficiency and 4.8x/18.6x speedup over a weight-stationary baseline for inference/training, and 86% vs 15% accuracy under high noise.

## Summary
Weight-stationary (WS) PIM accelerators keep weights in RRAM and activations in buffers/DRAM, which the authors argue leads to heavy buffer/DRAM traffic, many extra RRAMs for transposed weights and training intermediates, coarse arrays needing high-bit ADCs and poorly utilised for depthwise/pointwise layers, and high sensitivity to noisy weights. INCA flips the dataflow: activations are written into RRAM and weights are applied as voltages, so only weights are loaded. To support kernel sliding, each cell is a two-transistor-one-RRAM (2T1R) with perpendicular word controls enabling direct convolution (write 4x4 windows, read 2x2 kernel windows, all columns tied for one-shot accumulation). Parallelism for batch training comes from a 3D horizontally-stacked RRAM architecture (16x16x64 per 3D array, 8 stacked layers, 1-bit ADC, 65nm, 8-bit data). The evaluation uses a customised simulator based on circuit simulation and NeuroSim+, against an ISAAC/PipeLayer-style WS baseline with 128x128 crossbars, 8GB HBM2, on VGG16/19, ResNet18/50, MobileNetV2 and MNasNet (ImageNet). Noise is modelled as zero-mean Gaussian added to weights or activations (sigma 0.5%-5%) in 10-epoch fine-tuning of ResNet18.

## Contributions
- Analysis of four fundamental limitations of WS dataflow in PIM designs
- First input-stationary PIM implementation using 2T1R cells and direct convolution
- 3D RRAM architecture exploiting batch parallelism for training
- Quantified energy, speed, area and noise-robustness gains over a WS baseline

## Key claims (stable IDs)
- **2023_Kim_INCA_HPCA#C1** — IS dataflow cuts energy by up to 20.6x (inference) and 260x (training) vs WS — _support:_ VGG16 20.6x/260x; VGG19 15.9x/202x; ResNet18 8.7x/103x; ResNet50 8.0x/152x — _loc:_ Sec. V-B, Fig. 11
- **2023_Kim_INCA_HPCA#C2** — IS is far more robust to RRAM noise than WS — _support:_ ResNet18 at sigma=5%: weight noise 15.17% vs activation noise 85.59% — _loc:_ Table VI
- **2023_Kim_INCA_HPCA#C3** — IS reduces buffer accesses — _support:_ VGG16 buffer accesses 1,544,496 -> 460,000 — _loc:_ Table III
- **2023_Kim_INCA_HPCA#C4** — 2T1R 3D layout is area-neutral or better — _support:_ one 128x128 baseline crossbar 491.52 um2 vs 49.152 um2 for the 16x16x64 INCA array — _loc:_ Sec. V-B6

## Results
- Speedup 4.8x (inference) and 18.6x (training) vs WS baseline
- Energy 8.0-20.6x (inference) and 103-260x (training) on four heavy CNNs
- Accuracy under noise sigma 0.005-0.05: weights 82.13 -> 15.17%, activations 89.21 -> 85.59%
- Light models (MobileNetV2, MNasNet) discussed separately with larger gains due to depthwise/pointwise utilisation

## Key numbers
- tech_node: 65nm
- array_size: 16x16x64 (3D), 128x128 baseline
- energy_eff: up to 20.6x (inference), 260x (training) vs WS
- throughput: 4.8x inference / 18.6x training speedup
- accuracy: 86% vs 15% (INCA vs WS) under high noise
- bits_weight: 8b
- bits_adc: 1b

## Datasets / benchmarks
ImageNet

## Limitations
- Simulation only (customised simulator over NeuroSim+); no fabricated 2T1R 3D array
- Noise study is additive Gaussian on a single network (ResNet18) over ten epochs
- Endurance of RRAM for frequent activation writes is acknowledged as future work (Sec. VI)
- IS dataflow requires writing activations to NVM each layer; costly for slow/low-endurance devices and for transformers with long sequences (not evaluated)

## Remarks
A provocative dataflow argument: storing activations in NVM reduces sensitivity to device noise because noise on activations is much more benign than on weights. The endurance and write-energy of writing every activation is the major practical risk, and the paper defers it. The CNN-only scope means no direct transfer to LMs, though the WS vs IS question is relevant for attention (dynamic operands) as in X-Former/ReTransformer.

## Cites (in collection, 11)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "PipeLayer [48] in the baseline design for training."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _uses-method-or-tool_: "We chose the zero-centered normal distribution to model the noise caused by nonideal properties like variation, nonlinearity, and asymmetry, following [65]."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _contrasts/critiques_: "Fine-grained WS accelerators demand extra processing but do not resolve light models' utilization [67], [71]."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _baseline/comparison_: "Because of the different disposition of elements, previous crossbar designs should separately hold transposed weight matrices in addition to the original weight [20, 48]."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "For the evaluation, a customized simulator was implemented based on our circuit simulation results and NeuroSim+ [38], [39]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "For the evaluation, a customized simulator was implemented based on our circuit simulation results and NeuroSim+ [38], [39]."
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021) — _data/numbers_: "According to [66], a WS system with TaOx/HfOx RRAM shows an 11% accuracy drop in VGG8 on CIFAR10 when compared to GPU with floating-point arithmetic."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _motivation_: "It is well-known that ADCs exponentially undermine performance and energy efficiency [67], [71]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Specifically, PIM hardware with resistive random-access memory (RRAM, ReRAM, a.k.a. memristor) has been explored to build accelerators for deep learning models in numerous works [6], [10], [20], [42], [48]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "Prior PIM-based designs [9], [10], [42], [48] have been built upon the WS dataflow, especially by unrolling the weight values."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Kim_INCA_HPCA.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Kim_INCA_HPCA.pdf)
- Full text: [../fulltext/2023_Kim_INCA_HPCA.txt](../fulltext/2023_Kim_INCA_HPCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/hpca56546.2023.10070992
