---
id: W4236788275
key: 2017_Ankit_TraNNsformer_ICCAD
title: "TraNNsformer: Neural network transformation for memristive crossbar based neuromorphic system design"
short: "TraNNsformer"
year: 2017
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2017)"
authors: "Aayush Ankit, Abhronil Sengupta, Kaushik Roy"
category: "05 Mapping, Compilation & Dataflow"
devices: ["Memristor(generic)"]
models: ["MLP", "SNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "tiling-partitioning", "weight-mapping", "crossbar-architecture", "energy-efficiency", "nas-codesign"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 3
citations_overall: 32
priority_score: 7.09
doi: "https://doi.org/10.1109/iccad.2017.8203823"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2017_Ankit_TraNNsformer_ICCAD.pdf"
fulltext: "../fulltext/2017_Ankit_TraNNsformer_ICCAD.txt"
---

# TraNNsformer

**TraNNsformer: Neural network transformation for memristive crossbar based neuromorphic system design** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2017) (2017)

## TL;DR
TraNNsformer interleaves magnitude pruning with size-constrained spectral clustering during training so surviving FC weights form dense crossbar-sized blocks, cutting memristive-crossbar area by 28-55% and energy by 49-67% versus the original MLP-SNNs at iso-accuracy.

## Summary
Unstructured pruning creates irregular connectivity that leaves most memristive crossbar (MCA) cross-points unused and makes peripherals (buffers, communication, control) dominate energy, so sparsity does not translate into hardware savings. TraNNsformer adds clustering to training: a Size Constrained Iterative Clustering (SCIC) step, adapted from spectral clustering on the layer's binary connectivity matrix, groups input and output neurons into clusters whose size is limited to the target MCA dimension. Training iterates cluster pruning, retraining to recover accuracy, and reinforcement of clusters, leaving a small residue of unclustered synapses. Mapping assigns each dense cluster to a crossbar (utilisation factor = used cross-points), and unclustered synapses to residual crossbars; the framework is technology-aware and accepts any permissible MCA size. Benchmarks are MLP-based SNNs on MNIST (4 layers, 2.39M synapses), SVHN (5 layers, 4.12M) and CIFAR-10 (6 layers, 5.56M), implemented in MATLAB with a DeepLearn toolbox, comparing Original, Pruning, Offline clustering and TraNNsformer at iso-accuracy using normalised area and energy.

## Contributions
- Integrated training framework that learns pruned and crossbar-clustered connectivity
- Size Constrained Iterative Clustering (SCIC) that bounds cluster size to the MCA dimension
- Technology-aware mapping for any permitted MCA size
- Area/energy analysis on MCA-based and CMOS-based (45 nm arithmetic energy) architectures

## Key claims (stable IDs)
- **2017_Ankit_TraNNsformer_ICCAD#C1** — TraNNsformer reduces MCA area 28-55% (39% average) versus the original DNN at iso-accuracy — _support:_ normalised area across MNIST/SVHN/CIFAR-10 — _loc:_ Sec. V-B, Fig. 7
- **2017_Ankit_TraNNsformer_ICCAD#C2** — Energy per classification drops 49-67% (56% average) versus original, and 15-29% (20% average) versus pruned networks — _support:_ normalised energy — _loc:_ Sec. V-B, Fig. 8
- **2017_Ankit_TraNNsformer_ICCAD#C3** — Pruning alone yields low crossbar utilisation — _support:_ 70% average sparsity maps to MCAs with ~0.3 utilisation factor — _loc:_ Sec. V-A, Fig. 5
- **2017_Ankit_TraNNsformer_ICCAD#C4** — Training-time clustering outperforms offline clustering — _support:_ fewer unclustered synapses and higher cluster quality across layers (SVHN) — _loc:_ Fig. 5, Fig. 6

## Results
- Area: 28-55% lower than original, 28-49% lower than pruned (Fig. 7)
- Energy: 49-67% lower than original, 15-29% lower than pruned (Fig. 8)
- Benchmarks: MNIST 2,392,800 synapses; SVHN 4,120,800; CIFAR-10 5,560,800 (Fig. 4)
- Also reduces energy on CMOS general-purpose architectures (Fig. 9)

## Key numbers
- tech_node: 45nm (CMOS arithmetic energy)
- array_size: any permissible MCA size (not fixed)
- energy_eff: 49-67% energy reduction
- accuracy: iso-accuracy with original

## Datasets / benchmarks
MNIST, SVHN, CIFAR-10

## Limitations
- Simulation-only with normalised area/energy numbers; no device non-idealities, ADC/DAC detail or measured hardware
- MLP-based SNN workloads only; convolution, attention and recurrent mapping are not evaluated
- Residual unclustered synapses still need extra crossbars; MATLAB toolbox-scale networks
- Absolute accuracy figures and crossbar sizes used are not clearly tabulated in the extracted text

## Remarks
One of the earliest clear statements that sparsity pays off on crossbars only if structured at crossbar granularity, an idea later reused in crossbar-aware pruning and block-sparse mapping. The evidence is limited (MLP-SNNs, normalised results), so magnitudes should not be extrapolated to CNNs or transformers where attention and large projection matrices dominate. Its tile-clustering principle is still relevant when mapping sparse or pruned LMs onto analog tiles.

## Cites (in collection, 3)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Thus, MCA is an analog computation unit and performs highly area and energy efficient inner-product operations [19]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Consequently, MCAs have been aggressively harnessed for energy-efficient DNN acceleration [2, 4, 22]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Consequently, MCAs have been aggressively harnessed for energy-efficient DNN acceleration [2, 4, 22]."

## Cited by (in collection, 6)
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _contrasts/critiques_: "With this guidance, previous work attempted to obtain crossbar-oriented pruning using iterative clustering method [39], but the fully-connected (FC) layer was the focus."
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019) — _background_: "Ankit et al. [22] implemented weight pruning techniques to NC systems using memristor crossbar arrays, which reduces the area (energy) consumption compared to the original network."
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020) — _contrasts/critiques_: "[16] implemented weight pruning techniques on a neuromorphic computing system using irregular pruning caused unbalanced workload, greater circuits overheads and extra memory requirement on indices."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "Previous works have focused on structured sparsity [165-167]."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _contrasts/critiques_: "Besides, some work proposed to train a sparse NN that fits the hardware structures of ReRAM crossbar [10]."
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2017_Ankit_TraNNsformer_ICCAD.pdf](../../05_Mapping_Compilation_and_Dataflow/2017_Ankit_TraNNsformer_ICCAD.pdf)
- Full text: [../fulltext/2017_Ankit_TraNNsformer_ICCAD.txt](../fulltext/2017_Ankit_TraNNsformer_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccad.2017.8203823
