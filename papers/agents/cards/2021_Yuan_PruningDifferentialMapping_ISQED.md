---
id: W3162727751
key: 2021_Yuan_PruningDifferentialMapping_ISQED
title: "Improving DNN Fault Tolerance using Weight Pruning and Differential Crossbar Mapping for ReRAM-based Edge AI"
short: "Pruning + Differential Mapping"
year: 2021
venue: "ISQED"
venue_full: "22nd International Symposium on Quality Electronic Design (ISQED 2021)"
authors: "Geng Yuan, Zhiheng Liao, Xiaolong Ma, Yuxuan Cai, Zhenglun Kong, Xuan Shen, Jingyan Fu, Zhengang Li, Chengming Zhang, Hongwu Peng, Ning Liu, Ao Ren et al."
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["ResNet", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["stuck-at-faults", "pruning-sparsity", "weight-mapping", "analog-mvm", "crossbar-architecture", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 8
citations_overall: 36
priority_score: 5.0
doi: "https://doi.org/10.1109/isqed51717.2021.9424332"
pdf: "../../06_Nonidealities_and_Reliability/2021_Yuan_PruningDifferentialMapping_ISQED.pdf"
fulltext: "../fulltext/2021_Yuan_PruningDifferentialMapping_ISQED.txt"
---

# Pruning + Differential Mapping

**Improving DNN Fault Tolerance using Weight Pruning and Differential Crossbar Mapping for ReRAM-based Edge AI** — 22nd International Symposium on Quality Electronic Design (ISQED 2021) (2021)

## TL;DR
Combines ADMM unstructured weight pruning (hierarchical progressive search for best ratio) with a differential two-cell weight mapping so stuck-off and stuck-on faults more often coincide with intended cell values, tolerating almost 10x higher stuck-at-fault rates than standard two-column mapping with no extra hardware or per-chip optimisation.

## Summary
Stuck-at faults in ReRAM crossbars cause mismatch between trained and mapped weights; existing fixes (row/column permutation, fault-aware retraining, redundant columns) need per-chip optimisation, which is impractical for mass-produced IoT devices. The authors observe that pruned (zero) weights can land on stuck-off cells, so unstructured pruning statistically improves stuck-off tolerance; accuracy drop under stuck-off faults is minimal around prune ratio 0.6 for ResNet18/CIFAR10 and rises again beyond that (Fig. 3), so a hierarchical progressive pruning algorithm (Alg. 1) searches for the best ratio. Because stuck-on faults are 5.2x more frequent than stuck-off (defect model of Chen et al. 2015), they propose a differential mapping where w is stored as two cells with wa = 1 (w>=0) or 1-|w| (w<0) and wb = 1-w (w>0) or 1 (w<=0), and the weight is wa-wb. Zero weights thus map to both cells at high conductance, converting pruning-induced zeros into 'ones' that overlap stuck-on faults. The same Ga/Gb column pair and subtractor as the conventional two-column scheme is used, so no extra hardware cost. Evaluation is purely software fault injection in PyTorch (averaged over 100 runs) on ResNet18 for CIFAR10 and ImageNet and YOLOv4 on MS COCO, with stuck-off:stuck-on ratio 1:5.2.

## Contributions
- Use of unstructured pruning as a fault-tolerance technique (not just compression) for ReRAM DNNs, applicable universally without per-device optimisation
- Empirical relation between prune ratio and stuck-off tolerance, with a hierarchical progressive pruning algorithm to find the best ratio
- Differential mapping converting pruning-driven stuck-off tolerance into stuck-on tolerance at no additional hardware cost
- Validation on image classification (CIFAR10, ImageNet) and object detection (YOLOv4/COCO)

## Key claims (stable IDs)
- **2021_Yuan_PruningDifferentialMapping_ISQED#C1** — Method tolerates almost an order of magnitude higher failure rate than traditional two-column mapping — _support:_ Abstract and Sec. V-B: preserves high accuracy at 0.01 failure rate where traditional mapping collapses by 0.005 — _loc:_ Abstract; Fig. 6; Sec. V-B
- **2021_Yuan_PruningDifferentialMapping_ISQED#C2** — Pruning minimises stuck-off accuracy drop at an intermediate ratio — _support:_ minimum accuracy drop at prune ratio 0.6 for ResNet18/CIFAR10 — _loc:_ Sec. IV, Fig. 3
- **2021_Yuan_PruningDifferentialMapping_ISQED#C3** — Offset mapping is less fault tolerant than two-column mapping — _support:_ Fig. 2 ResNet18/CIFAR10 shows offset much worse — _loc:_ Sec. III, Fig. 2
- **2021_Yuan_PruningDifferentialMapping_ISQED#C4** — No extra hardware versus two-column mapping — _support:_ same Ga/Gb columns and subtractor — _loc:_ Sec. IV-D, Fig. 5

## Results
- CIFAR10 ResNet18 (94.1% fault-free): at failure rate 0.001 average accuracy drop 0.2% versus 1.2% for traditional two-column mapping (Sec. V-B)
- Traditional mapping drops severely at failure rate 0.005; proposed method keeps high accuracy at 0.01 (Fig. 6)
- ImageNet ResNet18 and YOLOv4/COCO (mAP) show improved tolerance across failure rates up to ~0.004 (Figs. 6, 7); exact values only in plots
- Stuck-on faults modelled 5.2x more frequent than stuck-off

## Key numbers
- accuracy: 94.1% CIFAR10 ResNet18 fault-free; 0.2% drop at 0.001 failure rate vs 1.2% for two-column

## Datasets / benchmarks
CIFAR-10, ImageNet, MS COCO

## Limitations
- Only software fault injection with a simple binary stuck-at model; no measured devices, no IR drop, variation, or ADC modelling
- Assumes mapping weights onto high-conductance for zeros, which raises array power/current (not quantified)
- Unstructured sparsity gives no area/latency savings in crossbars; benefit is purely fault tolerance
- Weights treated as continuous analog conductances (bit-slicing / multilevel cell effects not discussed); only CNN workloads, no transformers
- Many numerical results only appear as plots in extracted text

## Remarks
A simple, zero-hardware-cost idea whose evidence is limited to idealised stuck-at injection. The insight that sparsity interacts with fault location and that the dominant fault polarity should guide the mapping carries over to other crossbar mappings. It is relevant to the non-ideality category but says nothing about language models or attention, whose dense weight/activation distributions might not tolerate this pruning ratio.

## Cites (in collection, 8)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _baseline/comparison_: "Several methods are proposed to address the stuck-at-fault defects, such as permuting the order of the crossbar rows and columns [4], retraining the network by considering the defect locations [5], [6]."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _contrasts/critiques_: "In [5], redundant columns of ReRAM crossbars are utilized as a substitution for the defect ReRAM columns. But this method not only introduces nontrivial area overhead, but also increases design complexity of peripheral circuit."
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019) — _background_: "DNN Weight pruning [8], [28]-[31], as one of the DNN model compression techniques, has also been investigated to reduce the weight storage and improve performance for ReRAM-based acceleration designs [32], [33]."
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019) — _contrasts/critiques_: "Although these methods are effective in mitigating the accuracy drop caused by the stuck-at-fault defects, even [7] can restore 99% of the accuracy drop, but for mass-produced IoT products, applying optimization for each individual product (IoT device) will bring a huge time cost, and is not realistic."
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020) — _background_: "DNN Weight pruning [8], [28]-[31], as one of the DNN model compression techniques, has also been investigated to reduce the weight storage and improve performance for ReRAM-based acceleration designs [32], [33]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "Recent work, TIMELY [23] saves the energy cost of data movements and D/A and A/D domain conversion by enhancing analog data locality to keep computations in analog domain."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Previous work, such as PRIME [21] and ISAAC [22], leverages in-situ computation to avoid the tremendous cost of data movement and efficiently compute multiply-accumulate operations, the most intensive computation in DNNs."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Previous work, such as PRIME [21] and ISAAC [22], leverages in-situ computation to avoid the tremendous cost of data movement and efficiently compute multiply-accumulate operations, the most intensive computation in DNNs."

## Cited by (in collection, 1)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "While keeping the number of crossbars the same, the latter approach introduces additional hardware costs for the peripheral circuits by adding extra offset circuits and may also decrease the network robustness to hardware failures [29]."

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2021_Yuan_PruningDifferentialMapping_ISQED.pdf](../../06_Nonidealities_and_Reliability/2021_Yuan_PruningDifferentialMapping_ISQED.pdf)
- Full text: [../fulltext/2021_Yuan_PruningDifferentialMapping_ISQED.txt](../fulltext/2021_Yuan_PruningDifferentialMapping_ISQED.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isqed51717.2021.9424332
