---
id: W4322007931
key: 2023_Ma_SAFVariationTolerantMapping_JETC
title: "A Mapping Method Tolerating SAF and Variation for Memristor Crossbar Array Based Neural Network Inference on Edge Devices"
short: "SAF/Variation Remapping"
year: 2023
venue: "JETC"
venue_full: "ACM Journal on Emerging Technologies in Computing Systems, Vol. 19, No. 2, Article 15 (2023)"
authors: "Yu Ma, Linfeng Zheng, Pingqiang Zhou"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["Memristor(generic)"]
models: ["MLP", "Other"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "tiling-partitioning", "stuck-at-faults", "device-variation", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 5
priority_score: 3.54
doi: "https://doi.org/10.1145/3585518"
pdf: "../../06_Nonidealities_and_Reliability/2023_Ma_SAFVariationTolerantMapping_JETC.pdf"
fulltext: "../fulltext/2023_Ma_SAFVariationTolerantMapping_JETC.txt"
---

# SAF/Variation Remapping

**A Mapping Method Tolerating SAF and Variation for Memristor Crossbar Array Based Neural Network Inference on Edge Devices** — ACM Journal on Emerging Technologies in Computing Systems, Vol. 19, No. 2, Article 15 (2023) (2023)

## TL;DR
A retraining-free sort-based weight-to-crossbar remapping that groups similar-valued weights into the same crossbar, keeping a 3-layer MNIST MLP at 92% accuracy under 28% stuck-at faults and ~90% under lognormal variation sigma=0.4.

## Summary
For edge memristor-crossbar inference, SAFs and conductance variation cause weight deviation; prior fixes need retraining, SAF maps, or two devices per weight. The authors define a sum weight variation (SWV) metric and formulate the mapping of weights to MCAs as a 0-1 programming problem under one-memristor-per-weight and vector-vector multiplication. Because the 0-1 problem is costly, they observe that columns of a trained weight matrix have similar value distributions and simplify to a sorted remapping: weights are sorted by value per column and assigned in order to R/S x C/S crossbars of size S (padding with dummy rows/columns), so each crossbar holds a narrow weight range (Algorithm 1, Fig. 7), which lowers absolute error from any conductance deviation. The computing pipeline is modified to process columns serially with input re-arrangement. Evaluation uses Monte-Carlo effective-weight simulation (10k-1M ohm range, 81.6% stuck-on/18.4% stuck-off, lognormal variation, crossbar size 64 for MNIST and 32 for NeRF) on a 2- and 3-layer MNIST MLP and a NeRF model on the FERN dataset, comparing conventional (NO), local mapping (LC) and proposed (OP).

## Contributions
- SWV metric and 0-1 programming formulation of reliability-aware mapping for size-limited crossbars
- Observation that different columns of trained weight matrices have similar value distributions, enabling a simplified problem
- Sort-based remapping algorithm with modified computing pipeline, no retraining or fault map needed
- Evaluation on MNIST MLP and NeRF neural rendering, including overhead (speed, energy, storage) discussion

## Key claims (stable IDs)
- **2023_Ma_SAFVariationTolerantMapping_JETC#C1** — Proposed remapping keeps accuracy high under heavy SAF without retraining — _support:_ ~95% accuracy at 5% defect rate and 92% at 28% defect rate vs <80% at 5% for conventional mapping — _loc:_ Sec. 5.1.1, Fig. 10
- **2023_Ma_SAFVariationTolerantMapping_JETC#C2** — Recovery accuracy at 20% defects matches retraining-based method [15] at 95.9% vs 95%, and exceeds [27] at 30.1% — _support:_ Table 4 — _loc:_ Table 4
- **2023_Ma_SAFVariationTolerantMapping_JETC#C3** — Tolerates lognormal variation: 95% accuracy at sigma=0.2 and 90% at sigma=0.4 — _support:_ Conventional mapping falls below 85% at sigma=0.2; quantization method [29] only 50% to 80% — _loc:_ Sec. 5.1.2, Fig. 11
- **2023_Ma_SAFVariationTolerantMapping_JETC#C4** — Effectiveness grows with the ratio R/S of matrix rows to crossbar size — _support:_ ~90% loss reduction at R/S=32; no improvement at R/S=1 — _loc:_ Sec. 5.2, Fig. 12-13

## Results
- MNIST 3-layer MLP: 92% accuracy at 28% SAF rate; conventional mapping <80% at 5% and ~20% at 20%
- Local mapping reduces sum(max-min) by ~42% and 12.5% (layers 1, 2); remapping further ~5x and 3x
- Variation: 90% accuracy at sigma=0.4 vs 32% without method
- At 20% defects: 95.9% recovered accuracy vs 95% for retraining method [15] and 30.1% for [27]
- Speed estimate: 10^6 ns per layer for MCA size 100 at 100 ns cycles, ~10^3 FPS; extra storage <2MB for a 1024x1024 matrix
- NeRF/FERN rendering quality preserved at defect rate 0.001-0.01 where conventional mapping fails

## Key numbers
- array_size: 64x64 (MNIST), 32x32 (NeRF)
- throughput: ~10^3 FPS estimate
- accuracy: 92% MNIST at 28% SAF; ~90% at sigma=0.4

## Datasets / benchmarks
MNIST, FERN (NeRF)

## Limitations
- Effective-weight simulation rather than circuit-level crossbar simulation
- Small models only (2-3 layer MNIST MLP, NeRF); no CNN/transformer/LM
- One memristor per weight; ADC and per-crossbar scaling costs not evaluated
- Column-serial pipeline reduces crossbar parallelism and throughput
- Benefit vanishes when the matrix fits one crossbar (R/S=1); weak at high sigma for small layers

## Remarks
A cheap and neat mapping observation: narrowing the dynamic range each crossbar must represent reduces absolute weight error without fault maps or retraining. Evidence is weak for modern workloads because only tiny MLPs and effective weights are simulated. The idea relates to per-tile/per-column scaling in later AIMC compilers and to SAF permutation methods (Rescuing, matrix transformation) in the collection; for LMs with outlier-heavy weights, value sorting may interact poorly with matrix semantics and needs input re-arrangement hardware.

## Cites (in collection, 6)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Some researchers propose to first measure variation distribution and then map the weight according to the measured distribution [4, 8, 14]. This process needs a large amount of computation which is intolerable for edge devices."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _baseline/comparison_: "Although [15] can also reach 95% recovery accuracy, our proposed method doesn't need the retraining process which is a very costly process for platforms [27]."
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019) — _baseline/comparison_: "One is the retraining method [4, 15] and the other is the permutation of rows and columns of the weight matrix [23, 28]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "Large weight matrices are always separated into pieces and then mapped to several MCAs [3]."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _baseline/comparison_: "On MNIST dataset and with a 3-layer fully-connected network, the state-of-the-art method [29] can only increase the accuracy from 50% (without the method) to 80% (with the method)."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Tile and IMA (in-situ multiply-accumulate) are higher hierarchies of MCAs [18]."

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2023_Ma_SAFVariationTolerantMapping_JETC.pdf](../../06_Nonidealities_and_Reliability/2023_Ma_SAFVariationTolerantMapping_JETC.pdf)
- Full text: [../fulltext/2023_Ma_SAFVariationTolerantMapping_JETC.txt](../fulltext/2023_Ma_SAFVariationTolerantMapping_JETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3585518
