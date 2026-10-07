---
id: W2945592020
key: 2019_Cai_LBCNN_TCAD
title: "Low Bit-Width Convolutional Neural Network on RRAM"
short: "LB-CNN"
year: 2019
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2019/2020"
authors: "Yi Cai, Tianqi Tang, Lixue Xia, Boxun Li, Yu Wang, Huazhong Yang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["quantization", "tiling-partitioning", "weight-mapping", "cnn-accelerator", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 5
citations_overall: 68
priority_score: 5.62
doi: "https://doi.org/10.1109/tcad.2019.2917852"
pdf: null
fulltext: null
---

# LB-CNN

**Low Bit-Width Convolutional Neural Network on RRAM** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2019/2020 (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes a low bit-width RRAM crossbar CNN (LB-CNN) accelerator with a matrix-splitting strategy for oversized weight matrices, a line-buffer pipeline for inference, and a splitting-and-quantizing-while-training method, achieving roughly 6x pipeline speedup on ResNet-18 and ~55% energy / ~48% area savings versus a multi-bit RRAM VGG-8.

## Summary
High-precision RRAM-based computing is limited by resistance-level and ADC/DAC interface constraints, motivating low bit-width CNNs that use low bit-width RRAM devices and interfaces. The paper (per its abstract) addresses three open system-design problems for such low bit-width RRAM-based CNN systems (RCS): how to split a weight matrix across multiple crossbars when it does not fit in one, how to pipeline inference using a line-buffer structure, and how to limit the accuracy drop introduced by splitting and quantization. It proposes an RRAM crossbar-based low-bit-width CNN (LB-CNN) accelerator with matrix-splitting strategies for scalability, a pipelined line-buffer implementation to accelerate inference, and a 'splitting and quantizing while training' method that bakes the hardware constraints into training. Reported results (from the abstract) include low bit-width LeNet-5 on RRAM showing better robustness to device variation than multi-bit models, about 6.0x per-image speedup from the pipeline strategy on ResNet-18, and for low-bit VGG-8 on CIFAR-10, 54.9% energy and 48.3% area savings versus a multi-bit VGG-8 implementation.

## Contributions
- Matrix-splitting strategies for mapping CNN weight matrices too large for a single crossbar onto multiple crossbars with improved scalability
- A pipelined inference architecture based on line-buffer structures to accelerate CNN inference on the low bit-width RRAM system
- A 'splitting and quantizing while training' method that incorporates the actual hardware splitting/quantization constraints directly into network training to reduce accuracy drop
- System-level design and evaluation of an RRAM crossbar-based low bit-width CNN (LB-CNN) accelerator across LeNet-5, ResNet-18 and VGG-8

## Key claims (stable IDs)
- **2019_Cai_LBCNN_TCAD#C1** — Low bit-width CNNs mapped to RRAM are more robust to device variation than multi-bit CNN models. — _support:_ Low bit-width LeNet-5 on RRAM shows much better robustness than multi-bit models with device variation (per abstract). — _loc:_ Abstract
- **2019_Cai_LBCNN_TCAD#C2** — The proposed line-buffer pipeline substantially accelerates per-image inference. — _support:_ Approximately 6.0x speedup to process each image on ResNet-18. — _loc:_ Abstract
- **2019_Cai_LBCNN_TCAD#C3** — The LB-CNN accelerator reduces energy and area versus a multi-bit RRAM implementation of the same network. — _support:_ For low-bit VGG-8 on CIFAR-10, saves 54.9% of energy consumption and 48.3% of area compared with the multi-bit VGG-8 structure. — _loc:_ Abstract

## Results
- ~6.0x per-image inference speedup on ResNet-18 from the pipelined line-buffer strategy (vs. non-pipelined baseline, per abstract)
- 54.9% energy savings and 48.3% area savings for low-bit VGG-8 on CIFAR-10 vs. a multi-bit VGG-8 RRAM structure
- Improved robustness to device variation for low bit-width LeNet-5 vs. multi-bit models (no exact figure given in abstract)

## Limitations
- Analysis based on the paper's abstract only -- no verified open-access full text was found (IEEE Xplore only; no arXiv/author-page copy located), so method details (exact matrix-splitting algorithm, precise bit-widths, full benchmark table) could not be independently checked
- Reported numbers are quoted from the abstract and should be treated as headline figures rather than fully contextualized results

## Remarks
This paper sits in the same Tsinghua RRAM-mapping lineage as SemiMap, Crossbar-Aware Pruning and the Mixed-Size-Crossbar paper in this collection, tackling a genuinely practical problem (splitting oversized weight matrices across crossbars plus a hardware-aware training loop) rather than a purely algorithmic quantization trick. Because only the abstract was accessible, the specific matrix-splitting algorithm and the quantitative accuracy-vs-compression trade-off curves could not be verified here; the headline 6x pipeline speedup and ~50% area/energy savings for VGG-8 are self-reported and should be cross-checked against the published TCAD version when available.

## Cites (in collection, 5)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 5)
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020) — _baseline/comparison_: "In the software level, researchers design the low bit-width CNN for PIM architectures to reduce the resolution requirement of ADCs, which introduce additional accuracy loss overhead [7]."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _baseline/comparison_: "And [13, 14] try to incorporate quantization with training to eliminate the quantization error."
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022) — _contrasts/critiques_: "Previous works tried to reduce the mean-square-error (MSE) of partial-sum quantization and relied on the min/max values or standard deviation (σ) of the partial sum distributions to decide the quantization range [1, 12, 17]."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023)
- [2023_Bai_CIMQ_TCAD](2023_Bai_CIMQ_TCAD.md) CIMQ (2023)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2019_Cai_LBCNN_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2019.2917852
