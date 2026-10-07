---
id: W2883149906
key: 2018_Liang_CrossbarAwarePruning_IEEEAccess
title: "Crossbar-Aware Neural Network Pruning"
short: "Crossbar-Aware Pruning"
year: 2018
venue: "IEEEAccess"
venue_full: "IEEE Access"
authors: "Ling Liang, Lei Deng, Yueling Jenny Zeng, Xing Hu, Yu Ji, Xin Ma, Guoqi Li, Yuan Xie"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Generic-NVM", "ReRAM", "PCM", "MRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "weight-mapping", "tiling-partitioning", "crossbar-architecture", "hardware-aware-training", "quantization", "device-variation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 7
citations_overall: 53
priority_score: 6.8
doi: "https://doi.org/10.1109/access.2018.2874823"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2018_Liang_CrossbarAwarePruning_IEEEAccess.pdf"
fulltext: "../fulltext/2018_Liang_CrossbarAwarePruning_IEEEAccess.txt"
---

# Crossbar-Aware Pruning

**Crossbar-Aware Neural Network Pruning** — IEEE Access (2018)

## TL;DR
An L0-constrained gradient descent pruning framework produces crossbar-grain and column-grain sparsity on top of semi-folded CNN mapping, saving 44%-72% of compute crossbars (VGG16, ResNet18, VGG8) with small accuracy loss.

## Summary
CNN mapping onto many-crossbar architectures either fully unfolds data reuse (hundreds of thousands of crossbars) or uses semi-folded mapping (SemiMap), which still costs many crossbars; generic fine-grained pruning cannot remove crossbars because irregular non-zeros remain. The paper defines two crossbar-friendly sparsity grains based on the semi-folded mapping: crossbar-grain (whole crossbar-sized blocks of the unrolled kernel matrix pruned, controlled by Kin/Kout) and column-grain sparsity where non-zero columns are recombined along the output dimension so empty crossbars disappear. Pruning is formulated as L0-norm constrained optimisation and solved by an L0-constrained gradient descent (LGD) with relaxant probabilistic projection (RPP) that toggles between dense and sparse space to build the mask; an input feature-map reorder clusters channels of similar importance to cut pruning error. A network-level step prunes layer by layer using three stop conditions (accuracy threshold, per-layer ratio, crossbar threshold Tc) followed by fine-tuning (30 epochs on ImageNet, 60 on CIFAR-10). Crossbar counts are from the semi-folded mapping compiler of SemiMap, comparing total and compute crossbars on VGG8 (CIFAR-10), and VGG16/ResNet18 (ImageNet). A small analysis adds quantization and multiplicative log-normal weight noise.

## Contributions
- Crossbar-grain and column-grain sparsity with output recombination tied to semi-folded mapping
- LGD solver with relaxant probabilistic projection that accurately controls sparsity
- Input feature-map reorder to improve post-pruning accuracy
- Network-level pruning-configuration procedure balancing accuracy and crossbar overhead

## Key claims (stable IDs)
- **2018_Liang_CrossbarAwarePruning_IEEEAccess#C1** — Crossbar-aware pruning saves 44.2%-72.1% compute crossbars with acceptable accuracy loss — _support:_ 59.8% VGG16, 44.2% ResNet18, 72.1% VGG8 — _loc:_ Sec. IV-E / Fig. 11, Table III
- **2018_Liang_CrossbarAwarePruning_IEEEAccess#C2** — ResNet18 is more sensitive to pruning than VGG — _support:_ Observed larger accuracy drop at same crossbar saving — _loc:_ Sec. IV-E
- **2018_Liang_CrossbarAwarePruning_IEEEAccess#C3** — On pruned VGG8 (50% sparsity), >0.1 variation or <5-bit quantization causes obvious accuracy loss — _support:_ Weight noise w*e^theta with sigma = device variation — _loc:_ Sec. V / Fig. 12

## Results
- Compute-crossbar savings: VGG16 59.8%, ResNet18 44.2%, VGG8 72.1% (Table III)
- Crossbar overhead reduction range 44%-72% across three networks (abstract)
- Column-grain gives better accuracy than crossbar-grain at equal sparsity (Conclusion)
- Quantization below 5 bits or variation above 0.1 gives obvious loss on pruned VGG8 (Fig. 12)

## Key numbers
- array_size: crossbar-size blocks with Kin 8-16, Kout 4
- accuracy: 44-72% crossbar reduction with insignificant accuracy degradation

## Datasets / benchmarks
CIFAR-10, ImageNet

## Limitations
- Only CNNs on CIFAR-10/ImageNet; no transformers
- Non-compute crossbars (buffers, reductions) are not reduced
- Accuracy loss from pruning deep layers not fixed by reorder
- Device non-idealities only briefly analysed (quantization and Gaussian-in-log variation) and not co-optimised
- Crossbar counts from compiler model, no hardware measurement

## Remarks
Early, widely cited work linking pruning granularity to physical crossbar utilisation; later bit-level sparsity papers (Bit-Transformer, ERA-BS) build on it. Sparse weight matrices in LMs are less pruning-friendly, so crossbar savings of this size are unlikely to transfer directly to transformer FFN/attention projections, but the principle of aligning sparsity structure with tiling stays valid.

## Cites (in collection, 7)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _uses-method-or-tool_: "For one-to-one comparison, we adopt the same semi-folded mapping compiler for the neural network chip in [29]."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _contrasts/critiques_: "With this guidance, previous work attempted to obtain crossbar-oriented pruning using iterative clustering method [39], but the fully-connected (FC) layer was the focus."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "It can achieve extremely throughput compared to the fully-folded mapping that reuses all the neurons and weights [1] cycle by cycle, however, this scheme consumes significantly huge crossbar resources."

## Cited by (in collection, 4)
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _motivation_: "One promising direction is to study the crossbar-aware sparsification like that in [43]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "Previous works have focused on structured sparsity [165-167]."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _contrasts/critiques_: "Existing works [12, 13, 17, 18] mainly focus on the structured compression (i.e., quantization and sparsification) for practical acceleration and the compression object is the numbers (i.e., weights)."
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2018_Liang_CrossbarAwarePruning_IEEEAccess.pdf](../../05_Mapping_Compilation_and_Dataflow/2018_Liang_CrossbarAwarePruning_IEEEAccess.pdf)
- Full text: [../fulltext/2018_Liang_CrossbarAwarePruning_IEEEAccess.txt](../fulltext/2018_Liang_CrossbarAwarePruning_IEEEAccess.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/access.2018.2874823
