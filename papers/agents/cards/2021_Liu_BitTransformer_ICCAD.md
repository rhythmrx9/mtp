---
id: W4200477077
key: 2021_Liu_BitTransformer_ICCAD
title: "Bit-Transformer: Transforming Bit-level Sparsity into Higher Preformance in ReRAM-based Accelerator"
short: "Bit-Transformer"
year: 2021
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021)"
authors: "Fangxin Liu, Wenbo Zhao, Zhezhi He, Zongwu Wang, Yilong Zhao, Yongbiao Chen, Li Jiang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "quantization", "bit-slicing", "weight-mapping", "crossbar-architecture", "energy-efficiency", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 9
citations_overall: 25
priority_score: 5.58
doi: "https://doi.org/10.1109/iccad51958.2021.9643569"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Liu_BitTransformer_ICCAD.pdf"
fulltext: "../fulltext/2021_Liu_BitTransformer_ICCAD.txt"
---

# Bit-Transformer

**Bit-Transformer: Transforming Bit-level Sparsity into Higher Preformance in ReRAM-based Accelerator** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021) (2021)

## TL;DR
Bit-Transformer combines power-of-two quantization, 3-D inter-crossbar bit-wise mapping and a retraining-free bit-flip-and-compensation scheme on SLC ReRAM crossbars to shrink crossbar footprint, claiming up to 13x energy-efficiency, 35x area-efficiency and 67x throughput over prior sparse ReRAM accelerators.

## Summary
Prior ReRAM sparsity schemes (SRE, PIM-Prune, TraNNsformer) need retraining, complex peripherals for unstructured sparsity, and assume idealistic crossbars that can activate all rows at once, although IR drop and ADC limits restrict concurrently active rows (e.g. 9 rows x 8 columns active in a 512x256 65nm macro). Bit-Transformer quantizes weights into a sum of a limited number of power-of-two terms, stores each bit in single-level cells (SLC, HRS=0 / LRS=1), and maps the bits of each weight to different crossbars (inter-crossbar bit mapping) so each bit matrix has its own sparsity and significance. A bit-flip and compensation step limits the maximum number of '1's per column (raising concurrently executable rows) and prunes low-cost columns, compensating the value bias in other bits, without retraining. The architecture adds small modules (masks per block, per-bit-matrix shift/accumulate) to an ISAAC-like design; evaluation uses PyTorch for accuracy and a gem5-based simulator (20 MB ReRAM main memory, 8 crossbars per CU, 8 CUs per bank) on ResNet-18/50, VGG16, AlexNet, MobileNet-v2 on CIFAR-10 and ImageNet. Results include nearly 8x and 3x crossbar footprint reduction (Table II) at accuracy comparable to SmartExchange/PIM-Prune (e.g. CIFAR-10 93.60% for Bit-Transformer-W; ImageNet ResNet 70.91%), >31x area-efficiency on CIFAR-10 networks vs 20x PIM-Prune and 14x SRE, 11x energy-efficiency, and 31.3x-121.7x speedup on ResNet-50 vs SRE/PIM-Prune/ISAAC.

## Contributions
- 3-D bit-wise inter-crossbar mapping plus bit-flip/compensation giving crossbar-friendly bit sparsity without retraining.
- ReRAM accelerator architecture integrating the scheme with small overhead and cheap block-level masks.
- Evaluation across five CNNs and two datasets with up to 13x/35x/67x energy/area/throughput gains.

## Key claims (stable IDs)
- **2021_Liu_BitTransformer_ICCAD#C1** — Up to 13x energy-efficiency, 35x area-efficiency, 67x throughput over prior state-of-the-art designs. — _support:_ abstract — _loc:_ Abstract, Sec. V-B
- **2021_Liu_BitTransformer_ICCAD#C2** — Area-efficiency over 31x on CIFAR-10 networks vs 20x for PIM-Prune and 14x for SRE (128x128 crossbar). — _support:_ normalized to non-sparse — _loc:_ Fig. 10
- **2021_Liu_BitTransformer_ICCAD#C3** — 31.3x to 121.7x speedup on ResNet-50 vs SRE, PIM-Prune and ISAAC. — _support:_ cycle comparison — _loc:_ Fig. 11
- **2021_Liu_BitTransformer_ICCAD#C4** — On ImageNet the gains are smaller (about 3x energy, 5x area on average) because large datasets limit compressibility. — _support:_ text — _loc:_ Sec. V-B

## Results
- Crossbar footprint reduction nearly 8x and 3x relative to baselines (Table II).
- Accuracy: CIFAR-10 93.60% (Bit-Transformer-W) vs 93.23% PIM-Prune; ImageNet 70.91% vs 70.97% SmartExchange.
- Crossbar size 64 yields highest sparsification but lowest energy efficiency (Fig. 13).

## Key numbers
- array_size: 128x128 (default); 64-256 explored
- energy_eff: up to 13x vs prior sparse ReRAM designs
- throughput: up to 67x; 31.3-121.7x on ResNet-50
- accuracy: 93.60% CIFAR-10; 70.91% ImageNet ResNet
- bits_weight: power-of-two sum on SLC (1b/cell)

## Datasets / benchmarks
CIFAR-10, ImageNet, ResNet-18, ResNet-50, VGG16, AlexNet, MobileNet-v2

## Limitations
- Simulation (PyTorch + gem5) with an analytic error-rate model; no silicon and limited device non-ideality modeling.
- Only CNNs for image classification; no Transformers or language models.
- Gains are far smaller on ImageNet than on CIFAR-10.
- SLC-only storage increases cell count per weight.

## Remarks
Shows how bit-level sparsity can be turned into fewer crossbars and higher row-parallelism without retraining, but its headline multipliers are against ISAAC-derived sparse baselines and partly reproduced by the authors. The mapping idea (bit-plane per crossbar, limited active rows) is generic but not demonstrated on LMs where weight distributions have outliers.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "A certain number of ReRAM crossbar-based DNN accelerator designs are built in prior works, such as ISAAC [9], PRIME [4], PipeLayer [10], and CASCADE [6]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _motivation_: "Therefore, there are only 9 rows, and 8 columns of ReRAM cells on a 512 × 256 crossbar for concurrent execution of MACs in the macro of a state-of-theart ReRAM-crossbar acceleration [25] in 65nm process."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _contrasts/critiques_: "Existing works [12, 13, 17, 18] mainly focus on the structured compression (i.e., quantization and sparsification) for practical acceleration and the compression object is the numbers (i.e., weights)."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _motivation_: "For example, the IR drop caused by wire resistance lead to a huge voltage drop at the target cell and limits the number of columns that can be executed at the same time [8, 11, 24]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _background_: "ReRAM crossbar is emerging as a promising solution to mitigate problems such as memory wall, owing to its high memory accessing bandwidth and high density [4, 6, 9, 10, 19–23]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "ReRAM crossbar is emerging as a promising solution to mitigate problems such as memory wall, owing to its high memory accessing bandwidth and high density [4, 6, 9, 10, 19–23]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "ReRAM crossbar is emerging as a promising solution to mitigate problems such as memory wall, owing to its high memory accessing bandwidth and high density [4, 6, 9, 10, 19–23]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "Fig. 11 shows the speed up over the baseline accelerator (i.e., ISAAC), we compare the cycles of inference on various networks."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "A certain number of ReRAM crossbar-based DNN accelerator designs are built in prior works, such as ISAAC [9], PRIME [4], PipeLayer [10], and CASCADE [6]."

## Cited by (in collection, 4)
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _background_: "Recent works [7–10] have proposed compact, energy-efficient and lowlatency implementations of transformers on IMC architectures using efficiency-driven hardware optimizations and architectural modifications."
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Liu_BitTransformer_ICCAD.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Liu_BitTransformer_ICCAD.pdf)
- Full text: [../fulltext/2021_Liu_BitTransformer_ICCAD.txt](../fulltext/2021_Liu_BitTransformer_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccad51958.2021.9643569
