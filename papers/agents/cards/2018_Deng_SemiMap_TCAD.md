---
id: W2902501132
key: 2018_Deng_SemiMap_TCAD
title: "SemiMap: A Semi-Folded Convolution Mapping for Speed-Overhead Balance on Crossbars"
short: "SemiMap"
year: 2018
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Lei Deng, Ling Liang, Guanrui Wang, Liang Juan Chang, Xing Hu, Xin Ma, Liu Liu, Jing Pei, Guoqi Li, Yuan Xie"
category: "05 Mapping, Compilation & Dataflow"
devices: ["SRAM-digital", "Generic-NVM"]
models: ["CNN", "VGG", "ResNet", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "tiling-partitioning", "dataflow-pipelining", "scheduling", "crossbar-architecture", "chip-demo", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 6
citations_overall: 25
priority_score: 6.58
doi: "https://doi.org/10.1109/tcad.2018.2883959"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2018_Deng_SemiMap_TCAD.pdf"
fulltext: "../fulltext/2018_Deng_SemiMap_TCAD.txt"
---

# SemiMap

**SemiMap: A Semi-Folded Convolution Mapping for Speed-Overhead Balance on Crossbars** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2018)

## TL;DR
SemiMap folds convolution mapping along the feature-map row dimension and unfolds along the column dimension on a many-crossbar architecture, giving 10x-36x lower crossbar overhead than fully-unfolded mapping and 23x-462x fewer phases than fully-folded mapping, validated with a 28 nm fabricated chip (156 SRAM-based virtual crossbars) plus chip-calibrated simulation.

## Summary
Crossbars suit FC layers but mapping Conv layers forces a choice between fully-unfolded mapping (huge crossbar count, e.g. >30,000 for CIFAR-10 CNNs, hundreds of thousands for ImageNet models) and fully-folded mapping (reusing one crossbar sliding window by sliding window, e.g. >5x10^4 cycles for a 224-size FM with 3x3 kernel). SemiMap observes that one output row needs only a few input rows and a shared kernel, so it reuses physical crossbars and weight memory along the FM row dimension (folding) while duplicating weights and neurons along the column dimension (unfolding) to keep parallelism. An FM-slicing scheme splits large images; a row-by-row streaming pipeline handles intra-image dataflow and a periodical pipeline handles inter-frame dataflow, where throughput depends on image height rather than model size. The supporting many-crossbar architecture ('FunC' functional crossbars with VMM, vector-add and buffer modes, multi-phase-per-step timing, P2P and adjacent-multicast routing, routing-aware neuron reservation) was fabricated in UMC 28 nm using off-the-shelf SRAM arrays with extra multipliers/accumulators to emulate a crossbar (8-bit weights/activations, 256x256). A Matlab mapping compiler and C++ cycle-accurate simulator, calibrated with measured power (1.95-6.29 mW per FunC, 16.8 us minimum phase latency at 300 MHz), evaluate LeNet-variant (MNIST), VGG8 (CIFAR-10), AlexNet, VGG16, ResNet18 (ImageNet).

## Contributions
- Semi-folded convolution mapping: fold along FM rows, unfold along FM columns, balancing speed and crossbar overhead
- FM slicing for large images plus row-by-row streaming and inter-frame periodical pipelines
- Many-crossbar architecture features (multi-phase-per-step schedule, AMC routing, neuron reservation) and a fabricated 28 nm chip
- Chip-measurement-based mapping compiler and cycle-accurate simulator evaluated on CNNs of different scales

## Key claims (stable IDs)
- **2018_Deng_SemiMap_TCAD#C1** — SemiMap reduces crossbar resource overhead 10x-36x versus fully-unfolded mapping — _support:_ >35x resource saving in abstract; up to 36x in conclusion — _loc:_ Sec. IV-D, Fig. 16
- **2018_Deng_SemiMap_TCAD#C2** — SemiMap needs 23x-462x fewer phases than fully-folded mapping (serial layers) — _support:_ throughput set by input image height, not model size — _loc:_ Sec. IV-D, Fig. 17
- **2018_Deng_SemiMap_TCAD#C3** — Throughput up to 2.8x vs GPU and on average 14.7x and 2x vs Eyeriss and DNA — _support:_ 1.5x-2.8x vs GPU on small images, 1.1x-1.4x on ImageNet (except AlexNet); 1.3x average vs the high-bandwidth accelerator in Table IV — _loc:_ Sec. IV-D, Fig. 18, Table IV
- **2018_Deng_SemiMap_TCAD#C4** — Neuron reservation keeps routing within capability (1.14x redundancy on VGG16) at slight extra crossbar cost — _support:_ without it packets exceed peak routing capability in many layers — _loc:_ Sec. IV-C, Fig. 15

## Results
- Resource saving 10x-36x vs fully-unfolded (Fig. 16)
- Phase reduction 23x-462x vs fully-folded (Fig. 17)
- Throughput 1.5x-2.8x vs GPU on small-image datasets; 1.1x-1.4x on ImageNet; 14.7x vs Eyeriss and 2x vs DNA on average (Fig. 18, Table IV)
- Chip: UMC 28 nm HLP, 156 FunCs, 300 MHz, 16.8 us minimum phase latency, 1.95-6.29 mW per FunC
- Inter-layer routing shows 86x redundancy for most layers (Fig. 14)

## Key numbers
- tech_node: 28nm (UMC HLP)
- array_size: 256x256 (SRAM virtual crossbar), 12x13 FunCs per chip
- energy_eff: 1.95-6.29 mW per FunC
- throughput: up to 2.8x vs GPU; 14.7x vs Eyeriss
- bits_weight: 8b

## Datasets / benchmarks
MNIST, CIFAR-10, ImageNet

## Limitations
- Hardware validation is a digital SRAM-emulated 'virtual crossbar' - no analog NVM behaviour, ADC/DAC or device noise is evaluated
- Large-network results come from a cycle-accurate simulator, inter-chip communication cost is ignored
- Temporal underutilisation: each FunC is busy only part of the periodical duration, hurting power efficiency in later layers; spatial crossbar utilisation by Conv kernels remains low
- CNN-only; throughput comparisons to Eyeriss/DNA/GPU are indirect
- 8-bit weights/activations only

## Remarks
Useful reference for convolution-to-crossbar mapping strategies between the fully-unfolded (ISAAC-style) and fully-folded (PRIME-style) extremes; the key idea (throughput governed by image height, resource governed by folding) is independent of memory technology. Because the chip is digital, it says nothing about analog non-idealities, and the approach is specific to convolutions with data reuse, so it does not directly transfer to transformer/LM matmuls. Strong on methodology (chip-calibrated simulator), weaker on cross-platform fairness.

## Cites (in collection, 6)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Besides conventional technologies, plenty of researches leverage modified SRAM [8]/ Flash [9] or various emerging non-volatile memory devices with in-memory computing capability to design this many-crossbar architecture, such as the most widely used RRAM (resistive RAM) [4–6, 19–24], PCRAM (phase-change RAM) [7, 25], and MRAM [26]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Besides conventional technologies, plenty of researches leverage modified SRAM [8]/ Flash [9] or various emerging non-volatile memory devices with in-memory computing capability to design this many-crossbar architecture, such as the most widely used RRAM (resistive RAM) [4–6, 19–24], PCRAM (phase-change RAM) [7, 25], and MRAM [26]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Besides conventional technologies, plenty of researches leverage modified SRAM [8]/ Flash [9] or various emerging non-volatile memory devices with in-memory computing capability to design this many-crossbar architecture, such as the most widely used RRAM (resistive RAM) [4–6, 19–24], PCRAM (phase-change RAM) [7, 25], and MRAM [26]."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _motivation_: "One promising direction is to study the crossbar-aware sparsification like that in [43]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Our implementation using off-the-shelf SRAM array and extra PEs to mimic the crossbar behavior is just for cost saving, and in fact, the proposed SemiMap can be easily extended to other crossbar architectures, such as the emerging devices with in-memory computing [5–9, 21–26]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _baseline/comparison_: "Specifically, it fully reuses the crossbar cycle by cycle for completing the Conv operations across many sliding windows [6]."

## Cited by (in collection, 4)
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _uses-method-or-tool_: "For one-to-one comparison, we adopt the same semi-folded mapping compiler for the neural network chip in [29]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "Such reshaping strategies have been well investigated [13, 33, 35] and should be implemented in the compilation framework."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _uses-method-or-tool_: "If there is space, weights are replicated in-crossbar to compute multiple convolution steps using a partial Toeplitz expansion [11, 24]."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2018_Deng_SemiMap_TCAD.pdf](../../05_Mapping_Compilation_and_Dataflow/2018_Deng_SemiMap_TCAD.pdf)
- Full text: [../fulltext/2018_Deng_SemiMap_TCAD.txt](../fulltext/2018_Deng_SemiMap_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2018.2883959
