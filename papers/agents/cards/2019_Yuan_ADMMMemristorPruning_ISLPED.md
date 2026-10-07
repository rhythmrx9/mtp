---
id: W2971533524
key: 2019_Yuan_ADMMMemristorPruning_ISLPED
title: "An Ultra-Efficient Memristor-Based DNN Framework with Structured Weight Pruning and Quantization Using ADMM"
short: "ADMM Memristor Prune+Quant"
year: 2019
venue: "ISLPED"
venue_full: "IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED 2019)"
authors: "Geng Yuan, Xiaolong Ma, Caiwen Ding, Sheng Lin, Tianyun Zhang, Zeinab S. Jalali, Yilong Zhao, Li Jiang, Sucheta Soundarajan, Yanzhi Wang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["Memristor(generic)", "ReRAM"]
models: ["CNN", "VGG", "ResNet", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "quantization", "weight-mapping", "tiling-partitioning", "hardware-aware-training", "adc-dac", "energy-efficiency", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 3
citations_overall: 58
priority_score: 5.57
doi: "https://doi.org/10.1109/islped.2019.8824944"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2019_Yuan_ADMMMemristorPruning_ISLPED.pdf"
fulltext: "../fulltext/2019_Yuan_ADMMMemristorPruning_ISLPED.txt"
---

# ADMM Memristor Prune+Quant

**An Ultra-Efficient Memristor-Based DNN Framework with Structured Weight Pruning and Quantization Using ADMM** — IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED 2019) (2019)

## TL;DR
A three-step ADMM framework (regularised optimisation, masked mapping, retraining) jointly applies crossbar-structured pruning and memristor-state-constrained quantization, giving 29.81x (VGG-16) and 20.88x (ResNet-18) weight compression with 0.5-0.76% accuracy loss and ~96-98% power and area reduction.

## Summary
Memristor pruning and quantization had been studied separately, without joint treatment of crossbar constraints. This work builds a unified framework using ADMM in DNN training. Structured pruning removes whole crossbar columns/blocks: a weight matrix W (n filters x k weights) is tiled into blocks of j filters spread over at least k/j crossbars, each crossbar output goes through an ADC and column outputs are summed, so pruning is aligned with crossbar granularity (128x64 for ResNet-18/VGG-16, 32x32 for LeNet-5/ConvNet). Quantization constrains weights to the conductance range [cond_min, cond_max] and to discrete state levels set to the mean of each device state level (zero-symmetric levels, no zero-state mapping) to reduce write imprecision; weights are mapped with positive and negative crossbars, with 4-bit cells and multiple crossbars bundled for higher precision (e.g. 9-bit weight = 8-bit positive and 8-bit negative blocks, each from two 4-bit crossbars). Experiments use a MATLAB memristor/peripheral model (Rmin 1 MOhm, Rmax 10 MOhm, 45 nm peripherals) on LeNet-5 and ConvNet (MNIST, CIFAR-10), VGG-16 and ResNet-18 (CIFAR-10), compared with Group Scissor. Fewer weight bits cut ADC/DAC overhead and mitigate state drift and process variation.

## Contributions
- First unified memristor-oriented framework combining structured pruning and quantization via ADMM (per authors)
- Hardware constraints in training: crossbar block pruning, conductance range and discrete state levels
- Masked mapping and retraining pipeline
- Compression, power and area results on LeNet-5, ConvNet, VGG-16, ResNet-18 versus Group Scissor

## Key claims (stable IDs)
- **2019_Yuan_ADMMMemristorPruning_ISLPED#C1** — LeNet-5: 17.69x weight reduction without accuracy loss, 37.06x with negligible loss, 105.52x within 1% accuracy loss — _support:_ crossbar area shrunk by more than 94% — _loc:_ Sec. IV, Table I
- **2019_Yuan_ADMMMemristorPruning_ISLPED#C2** — VGG-16 and ResNet-18 compressed 29.81x and 20.88x with <=0.5% and 0.76% loss respectively — _support:_ parameters reduced by 13.98M (VGG-16) and 10.46M (ResNet-18) — _loc:_ Abstract, Table I
- **2019_Yuan_ADMMMemristorPruning_ISLPED#C3** — Higher accuracy than Group Scissor at the same compression ratio on ConvNet/CIFAR-10 — _support:_ 2.35x ratio; same accuracy at 2.93x — _loc:_ Sec. IV-A, Table I
- **2019_Yuan_ADMMMemristorPruning_ISLPED#C4** — 5-bit quantization gives up to 98.38% power and 98.28% area reduction on VGG-16 — _support:_ ResNet-18: 96.95%/97.46%; ConvNet 95.91%/89.74%; LeNet5 96.96%/93.97% — _loc:_ Sec. IV-B, Fig. 8
- **2019_Yuan_ADMMMemristorPruning_ISLPED#C5** — Crossbar area reduced 96.65% (VGG-16) and 95.21% (ResNet-18) versus Group Scissor-style baseline — _support:_ structured pruning — _loc:_ Sec. IV

## Results
- Original LeNet-5 99.17% accuracy, 99.15% after structured pruning (MNIST)
- 6-bit quantization: 0.1% accuracy loss on LeNet-5 17.69x model, 0.2% on 105.52x
- CIFAR-10: ConvNet ~1.0% loss at 2.35x and 2.0% at 5.88x; VGG-16 ~0.1% at 9.31x and 0.8% at 29.81x; ResNet-18 0.5% at 11.75x and 0.6% at 20.88x
- Power (area) reduction with 5-bit weights: ResNet-18 96.95% (97.46%), VGG-16 98.38% (98.28%), ConvNet 95.91% (89.74%), LeNet5 96.96% (93.97%)

## Key numbers
- tech_node: 45nm (peripherals)
- array_size: 128x64 (VGG-16/ResNet-18); 32x32 (LeNet-5/ConvNet)
- energy_eff: 96.95-98.38% power reduction (5-bit, ResNet-18/VGG-16)
- accuracy: VGG-16 0.5% loss at 29.81x; ResNet-18 0.76% loss at 20.88x
- bits_weight: 5-6b (4-bit cells)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Simulation with a MATLAB model; no silicon and no stochastic device variation, IR drop or read noise evaluated
- Only CNNs on MNIST/CIFAR-10; no ImageNet, transformers or language models
- Power/area savings include dropping entire crossbars of higher-bit representations, so baselines (9-bit models) are generous
- Model weights shared via an anonymous link in the paper; reproducibility depends on it
- Linear conductance-level assumption; nonlinearity only illustrated

## Remarks
Shows that pruning aligned to crossbar blocks plus state-aware quantization yields large nominal area/power savings, but the evidence is system-level estimation on small CNNs. For LM deployment, structured block pruning and conductance-level quantization are conceptually applicable, though transformer weight/activation outliers and large matrices would stress both the ADMM training and the crossbar tiling assumptions.

## Cites (in collection, 3)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _uses-method-or-tool_: "Row Decoder design is no larger than 128×64 [36] and is identical for all DNN layers."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _background_: "Ankit et al. [22] implemented weight pruning techniques to NC systems using memristor crossbar arrays, which reduces the area (energy) consumption compared to the original network."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "To ensure a relatively high accuracy, usually two (or more) memristors are bundled to represent weights with high resolution (more bits) [39]."

## Cited by (in collection, 5)
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _background_: "DNN Weight pruning [8], [28]-[31], as one of the DNN model compression techniques, has also been investigated to reduce the weight storage and improve performance for ReRAM-based acceleration designs [32], [33]."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _contrasts/critiques_: "The previous ReRAM-based accelerator designs [47, 48] apply structured pruning and aim to make the pruning ratio as high as possible while maintaining an acceptable accuracy loss."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "However, the negative side is that these are rather closed pieces of software, which has been partially solved by Ma et al. and Yuan et al., by using PyTorch instead of TensorFlow, focusing in this case on the weight pruning and quantization effects."
- [2021_Li_RaQu_TCAD](2021_Li_RaQu_TCAD.md) RaQu (2021)
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2019_Yuan_ADMMMemristorPruning_ISLPED.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2019_Yuan_ADMMMemristorPruning_ISLPED.pdf)
- Full text: [../fulltext/2019_Yuan_ADMMMemristorPruning_ISLPED.txt](../fulltext/2019_Yuan_ADMMMemristorPruning_ISLPED.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/islped.2019.8824944
