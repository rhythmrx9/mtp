---
id: W2978384356
key: 2019_Zhang_MTFramework_TCAD
title: "Handling Stuck-at-Fault Defects Using Matrix Transformation for Robust Inference of DNNs"
short: "MT Framework"
year: 2019
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 39, no. 10, pp. 2448-2460 (2020; online 2019)"
authors: "Baogang Zhang, Necati Uysal, Deliang Fan, Rickard Ewetz"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["Memristor(generic)"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["stuck-at-faults", "weight-mapping", "calibration-compensation", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 6
citations_overall: 52
priority_score: 5.51
doi: "https://doi.org/10.1109/tcad.2019.2944582"
pdf: null
fulltext: null
---

# MT Framework

**Handling Stuck-at-Fault Defects Using Matrix Transformation for Robust Inference of DNNs** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 39, no. 10, pp. 2448-2460 (2020; online 2019) (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
The MT framework tolerates stuck-at faults in memristor crossbars by transforming weight matrices (row flipping, permutation, value-range reduction) to minimise a fault-impact cost, recovering 99% of the accuracy loss on MNIST and CIFAR-10 without hardware-aware training, at 8.19x power and 9.23x area overhead.

## Summary
Stuck-at faults in memristor crossbar arrays severely degrade DNN inference accuracy, and earlier fixes rely on extra hardware or hardware-aware (fault-aware) retraining. This TCAD extension of the authors' ASP-DAC'19 paper defines a cost metric capturing the negative impact of stuck-at faults and minimises it by applying matrix transformations T, so that W is mapped as T(W). Row flipping converts stuck-off faults into stuck-on faults (and vice versa), permutation maps small weights onto stuck-off cells and large weights onto stuck-on cells, and value-range transformation shrinks the extreme weight magnitudes so each fault introduces a smaller error. Experiments on MNIST and CIFAR-10 recover 99% of the accuracy loss without hardware-aware training, at the cost of 8.19x power and 9.23x area overhead, which can be reduced by up to 50% when combined with hardware-aware training.

## Contributions
- Cost metric quantifying the impact of stuck-at faults on a mapped weight matrix
- Row-flipping transformation swapping stuck-on/stuck-off semantics
- Permutation transformation matching weight magnitudes to fault types
- Value-range transformation reducing per-fault error magnitude
- Combination with hardware-aware training to reduce overhead

## Key claims (stable IDs)
- **2019_Zhang_MTFramework_TCAD#C1** — Matrix transformations alone, without retraining, recover nearly all SAF-induced accuracy loss. — _support:_ 'capable of recovering 99% of the accuracy loss on both the MNIST and CIFAR-10 datasets without utilizing hardware aware training' — _loc:_ Abstract
- **2019_Zhang_MTFramework_TCAD#C2** — The recovery comes at significant hardware cost. — _support:_ '8.19x and 9.23x overhead in power and area, respectively' — _loc:_ Abstract
- **2019_Zhang_MTFramework_TCAD#C3** — Hardware-aware training can reduce the overhead. — _support:_ 'the overhead can be reduced with up to 50% by leveraging hardware aware training' — _loc:_ Abstract

## Results
- 99% of SAF-induced accuracy loss recovered on MNIST and CIFAR-10 without hardware-aware training (abstract)
- 8.19x power and 9.23x area overhead; up to 50% overhead reduction with hardware-aware training (abstract)

## Limitations
- Abstract-only analysis; fault rates, network architectures and baselines not verified
- Large power/area overhead (8-9x) relative to the unprotected design
- Requires per-chip fault map
- Stuck-at faults only; does not address variation, drift or IR drop
- Small datasets (MNIST, CIFAR-10)

## Remarks
Represents the retraining-free, mapping-centric school of SAF tolerance (contrast with Liu et al. DAC'17 retraining/remapping, which it cites), and is cited by later fault-tolerant mapping work for ReRAM and attention models. The 8-9x overhead reported in the abstract is a serious practical caveat and suggests the transformations require substantial redundant hardware, so its value is more conceptual (fault-aware weight-to-cell assignment) than as a deployable scheme.

## Cites (in collection, 6)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 3)
- [2020_Guo_ATT_ICCD](2020_Guo_ATT_ICCD.md) ATT (2020) — _contrasts/critiques_: "Meanwhile, Zhang et al. [13], [41] also use similar methods to handle this issue."
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _contrasts/critiques_: "Although these methods are effective in mitigating the accuracy drop caused by the stuck-at-fault defects, even [7] can restore 99% of the accuracy drop, but for mass-produced IoT products, applying optimization for each individual product (IoT device) will bring a huge time cost, and is not realistic."
- [2023_Ma_SAFVariationTolerantMapping_JETC](2023_Ma_SAFVariationTolerantMapping_JETC.md) SAF/Variation Remapping (2023) — _baseline/comparison_: "One is the retraining method [4, 15] and the other is the permutation of rows and columns of the weight matrix [23, 28]."

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2019_Zhang_MTFramework_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2019.2944582
