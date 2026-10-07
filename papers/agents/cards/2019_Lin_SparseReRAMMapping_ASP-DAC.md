---
id: W2910506572
key: 2019_Lin_SparseReRAMMapping_ASP-DAC
title: "Learning the sparsity for ReRAM"
short: "Learning-Sparsity-ReRAM"
year: 2019
venue: "ASP-DAC"
venue_full: "24th Asia and South Pacific Design Automation Conference (ASP-DAC 2019)"
authors: "Jilan Lin, Zhenhua Zhu, Yu Wang, Yuan Xie"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet", "LSTM/RNN", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "weight-mapping", "tiling-partitioning", "crossbar-architecture", "quantization", "bit-slicing", "energy-efficiency", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 5
citations_overall: 79
priority_score: 5.86
doi: "https://doi.org/10.1145/3287624.3287715"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2019_Lin_SparseReRAMMapping_ASP-DAC.pdf"
fulltext: "../fulltext/2019_Lin_SparseReRAMMapping_ASP-DAC.txt"
---

# Learning-Sparsity-ReRAM

**Learning the sparsity for ReRAM** — 24th Asia and South Pacific Design Automation Conference (ASP-DAC 2019) (2019)

## TL;DR
K-means column-clustering maps sparse NN weights onto small ReRAM crossbars and crossbar-grained pruning removes low-utilization crossbars, giving 3-5x energy efficiency and >5x speedup vs a dense PRIME baseline with <1% accuracy loss.

## Summary
Dense mapping of sparse NN matrices wastes ReRAM crossbar area because zeros still occupy cells to keep O(1) MVM. The paper proposes a mapping that clusters weight columns with recursive k-means (taking the L most concentrated columns per crossbar-size cluster, pre-splitting huge matrices such as 25088x4096 with an interpolated split function), exchanging columns so that all-zero blocks vanish; extra indexing units are added to PRIME's flow. Crossbar-grained pruning then removes crossbars with low valid-cell utilization, with gradual retraining. Since devices have limited precision, they study 4-bit/8-bit/float quantization under sparsity (8-bit suffices) and propose analog tree-style precision composition circuits to combine multiple 2-bit cells' outputs in the analog domain, reducing ADC/interface cost. Energy is simulated with NVSim on a modified PRIME (baseline 256x256, 4-bit); crossbar size sweeps 16-128 favour 32x32. Benchmarks are LeNet-5, AlexNet, VGG-16, ResNet-18/20, 5-layer bi-LSTM.

## Contributions
- Sparse NN mapping based on k-means column clustering/exchange to raise crossbar utilization
- Crossbar-grained pruning algorithm removing low-utilization crossbars
- Analysis of quantization precision for sparse NNs plus analog precision-composing periphery circuits
- Crossbar-size design-space exploration (16 to 128)

## Key claims (stable IDs)
- **2019_Lin_SparseReRAMMapping_ASP-DAC#C1** — Sparse mapping plus crossbar pruning gives 3-5x energy-efficiency over dense-mapped PRIME — _support:_ 3-5x normalized to PRIME — _loc:_ Sec. VI-B / Fig. 9
- **2019_Lin_SparseReRAMMapping_ASP-DAC#C2** — More than 5x speedup for most NNs, weaker on ResNet (conv layers harder to prune) — _support:_ >5x — _loc:_ Sec. VI-B / Fig. 10
- **2019_Lin_SparseReRAMMapping_ASP-DAC#C3** — 8-bit precision is enough for sparse NNs: no accuracy loss up to 90% pruning, <1% to 95%; 4-bit degrades badly past 90% pruning — _support:_ VGG-16 CIFAR-10 — _loc:_ Sec. V / Fig. 6
- **2019_Lin_SparseReRAMMapping_ASP-DAC#C4** — Crossbar pruning loses <1% accuracy — _support:_ VGG-16 93.64->93.72%, ResNet-18 92.37->91.78%, LSTM-5 89.24->88.01%, LeNet-5 99.23->99.15% — _loc:_ Table II
- **2019_Lin_SparseReRAMMapping_ASP-DAC#C5** — 32x32 crossbars are the best energy trade-off; 16x16 costs more energy due to interfaces — _support:_ crossbar-size sweep on VGG-16 — _loc:_ Fig. 8

## Results
- Energy 3-5x better than PRIME for popular NNs after crossbar-grained pruning (Fig. 9)
- Speedup >5x for most NNs from reuse of saved crossbars and faster cycles for small arrays (Fig. 10)
- Accuracy after crossbar pruning: LeNet-5 99.15%, VGG-16 93.72%, ResNet-18 91.78%, LSTM-5 88.01% vs original 99.23/93.64/92.37/89.24 (Table II)
- Pruning a small share of parameters saves a large share of crossbars (Fig. 11)

## Key numbers
- array_size: 256x256 baseline; 32x32 chosen (16-128 swept)
- energy_eff: 3-5x vs PRIME
- throughput: >5x speedup vs PRIME
- accuracy: 93.72% VGG-16 CIFAR-10 after crossbar pruning
- bits_weight: 8b (2-bit ReRAM cells composed)

## Datasets / benchmarks
MNIST, CIFAR-10, LibriSpeech, LeNet-5, AlexNet, VGG-16, ResNet-18

## Limitations
- Simulation only (NVSim-based energy, modified PRIME); no silicon
- No device non-idealities (variation, drift, IR drop) modeled
- Convolutional layers gain less; benefits depend on NN redundancy
- Indexing overhead and k-means runtime for large matrices only partially discussed
- CNN/LSTM only, no transformers or language models

## Remarks
Representative early work on irregular-sparsity-aware crossbar mapping; relevant to LM mapping because transformer weight matrices are large and mostly dense, so structured crossbar-level pruning is the more transferable idea. Evidence is simulation-only against a PRIME baseline, and small-array preference (32x32) reflects interface cost assumptions. Complements crossbar-aware pruning and TraNNsformer in the collection.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Therefore, designing ReRAM based NN accelerators attracts lots of researchers’ attentions [2–4]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _motivation_: "Meanwhile, in the current tape-out chip of ReRAM based computing systems, the size of fabricated ReRAM crossbar is quite small, like 32 × 32 or 64 × 64 [13, 14]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "With the advantages of efficient in-memory computing ability, previous work has proposed several ReRAM-based Computing Systems, like PRIME [2] and ISAAC [3]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _baseline/comparison_: "With the advantages of efficient in-memory computing ability, previous work has proposed several ReRAM-based Computing Systems, like PRIME [2] and ISAAC [3]."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _contrasts/critiques_: "Besides, some work proposed to train a sparse NN that fits the hardware structures of ReRAM crossbar [10]."

## Cited by (in collection, 6)
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _contrasts/critiques_: "Although we could partition huge matrix into multiple small matrices[23], sparse mapping still needs 100x numbers of DACs&ADCs than dense mapping."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Reference 204 obtains a similar outcome, but starting with a sparse neural network, by re-arranging the matrix columns using k-means clustering, pruning elements that still remain outside of fixed-size blocks, and retraining the network."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _contrasts/critiques_: "Some designs prune DNNs [8, 26, 48, 75, 80] to reduce DNN weight count, so we call these designs Weight-Count-Limited."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _contrasts/critiques_: "Direct application of current ReRAM-based sparse methods [17, 28] to ReRAM-based SDDMM and SpMM operations will achieve inferior performance (for details to see § IV-C and § IV-D)."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _motivation_: "The second reason for full-stack modeling is that coexploring levels can find better systems [43–46]."
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2019_Lin_SparseReRAMMapping_ASP-DAC.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2019_Lin_SparseReRAMMapping_ASP-DAC.pdf)
- Full text: [../fulltext/2019_Lin_SparseReRAMMapping_ASP-DAC.txt](../fulltext/2019_Lin_SparseReRAMMapping_ASP-DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3287624.3287715
