---
id: W3013407975
key: 2020_Ma_TinyButAccurate_ASPDAC
title: "Tiny but Accurate: A Pruned, Quantized and Optimized Memristor Crossbar Framework for Ultra Efficient DNN Implementation"
short: "P-RM Memristor Framework"
year: 2020
venue: "ASP-DAC"
venue_full: "25th Asia and South Pacific Design Automation Conference (ASP-DAC 2020)"
authors: "Xiaolong Ma, Geng Yuan, Sheng Lin, Caiwen Ding, Fuxun Yu, Tao Liu, Wujie Wen, Xiang Chen, Yanzhi Wang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["Memristor(generic)"]
models: ["MLP", "CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "quantization", "crossbar-architecture", "weight-mapping", "tiling-partitioning", "energy-efficiency", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 3
citations_overall: 53
priority_score: 5.54
doi: "https://doi.org/10.1109/asp-dac47756.2020.9045658"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2020_Ma_TinyButAccurate_ASPDAC.pdf"
fulltext: "../fulltext/2020_Ma_TinyButAccurate_ASPDAC.txt"
---

# P-RM Memristor Framework

**Tiny but Accurate: A Pruned, Quantized and Optimized Memristor Crossbar Framework for Ultra Efficient DNN Implementation** — 25th Asia and South Pacific Design Automation Conference (ASP-DAC 2020) (2020)

## TL;DR
ADMM-based structured pruning plus 8-bit distillation quantization with Network Purification and Unused Path Removal (P-RM) reaches 231.82x compression on LeNet-5 (0.4% drop after quantization) and 59.84x on ResNet-18 (CIFAR-10), shrinking crossbar area and power several-fold.

## Summary
Memristor crossbars suffer from limited array size and device imperfections, so model compression directly shrinks hardware cost. The paper formulates structured (column/filter/channel) weight pruning and quantization as a constrained non-convex problem solved by ADMM, with the quantization set Q constrained to the memristance range. Weights are mapped as GEMM matrices partitioned into 128x64 crossbar blocks with an ADC per crossbar column group and column-wise summation; pruned columns/filters shrink or remove blocks (Fig. 3). The authors observe ADMM is non-optimal and that pruned filters leave unused channels in the next layer, so Network Purification and Unused Path Removal (Algorithm 1; emptiness ratio eta and importance score sigma) post-process the model. Quantization to 8 bit uses knowledge distillation from a deeper teacher (Algorithm 2). Accuracy is measured in software models with hardware constraints (PyTorch, 8 GPUs); area and power come from a MATLAB memristor model and NVSim with 1R crossbars (Ron 1MOhm, Roff 10MOhm, 4-bit cells, two cells per 8-bit weight, 45nm peripherals).

## Contributions
- ADMM structured pruning with memristor-range quantization constraints
- Network Purification and Unused Path Removal post-processing for structured-pruned models
- Distillation-based 8-bit quantization of pruned models
- Area/power evaluation on LeNet-5, ConvNet, VGG-16, ResNet-18/50, AlexNet

## Key claims (stable IDs)
- **2020_Ma_TinyButAccurate_ASPDAC#C1** — 231.82x LeNet-5 compression with minor accuracy loss — _support:_ 99.17% baseline, 98.05% after 8-bit quantization at 231.82x — _loc:_ Table 1, Sec. 6
- **2020_Ma_TinyButAccurate_ASPDAC#C2** — ResNet-18 CIFAR-10 pruned 59.84x with ~no accuracy loss — _support:_ 93.22% with P-RM, 93.27% quantized (baseline 93.79%) — _loc:_ Table 1
- **2020_Ma_TinyButAccurate_ASPDAC#C3** — P-RM cuts crossbar area and power — _support:_ ResNet-18 5.83x model: 0.235mm2 and 3.359W to 0.042mm2 and 0.585W — _loc:_ Table 2

## Results
- Beats Group Scissor on ConvNet CIFAR-10 at equal 2.35x: 84.55% vs 82.09%
- AlexNet ImageNet 4.69x at 81.76% vs SSL 1.40x at 80.40% (Table 1)
- VGG-16 20.16x model: 0.113mm2/1.611W to 0.056mm2/0.824W with P-RM (Table 2)
- ResNet-50 ImageNet 2.70x at 92.27%

## Key numbers
- tech_node: 45nm peripherals
- array_size: 128x64
- accuracy: 93.22% CIFAR-10 ResNet-18 at 59.84x
- bits_weight: 8b (2x4-bit cells)

## Datasets / benchmarks
MNIST, CIFAR-10, ImageNet

## Limitations
- No analog non-idealities (noise, drift, IR-drop) simulated; only range/level constraints
- Hardware cost estimated by NVSim/MATLAB, no fabricated device
- Only CNN/MLP, no transformers or language models
- Results reported without retraining; compression gains on ImageNet modest

## Remarks
A compression paper where the crossbar mainly dictates structured pruning granularity and bit-levels; area/power numbers are model-based. Useful as an early example of mapping structured sparsity to crossbar blocks, relevant to later LM pruning-for-CIM work but no direct language-model evidence.

## Cites (in collection, 3)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _uses-method-or-tool_: "Due to the increasing reading/writing errors caused by expanding the memristor crossbar size, we limited our design by using multiple 128×64 [25] crossbars for all DNN layers."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _contrasts/critiques_: "[16] implemented weight pruning techniques on a neuromorphic computing system using irregular pruning caused unbalanced workload, greater circuits overheads and extra memory requirement on indices."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Due to its outstanding performance on computing matrix-vector multiplications (MVM), memristor crossbars are widely used as dot-product accelerator in recent neuromorphic computing designs [19]."

## Cited by (in collection, 5)
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _background_: "DNN Weight pruning [8], [28]-[31], as one of the DNN model compression techniques, has also been investigated to reduce the weight storage and improve performance for ReRAM-based acceleration designs [32], [33]."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _contrasts/critiques_: "The previous ReRAM-based accelerator designs [47, 48] apply structured pruning and aim to make the pruning ratio as high as possible while maintaining an acceptable accuracy loss."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "However, the negative side is that these are rather closed pieces of software, which has been partially solved by Ma et al. and Yuan et al., by using PyTorch instead of TensorFlow, focusing in this case on the weight pruning and quantization effects."
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2020_Ma_TinyButAccurate_ASPDAC.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2020_Ma_TinyButAccurate_ASPDAC.pdf)
- Full text: [../fulltext/2020_Ma_TinyButAccurate_ASPDAC.txt](../fulltext/2020_Ma_TinyButAccurate_ASPDAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/asp-dac47756.2020.9045658
