---
id: W7106169063
key: 2025_Guo_NIPA_ICCAD
title: "How Do Errors Impact NN Accuracy on Non-Ideal Analog PIM? Fast Evaluation via an Error-Injected Robustness Metric"
short: "NIPA"
year: 2025
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2025)"
authors: "Lidong Guo, Zhenhua Zhu, Qiushi Lin, Yuan Xie, Huazhong Yang, Wangyang Fu, Yu Wang"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Generic-NVM"]
models: ["CNN", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["security-robustness", "noise-injection", "analog-mvm", "simulator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 12
citations_overall: 0
priority_score: 3.5
doi: "https://doi.org/10.1109/iccad66269.2025.11240851"
pdf: null
fulltext: null
---

# NIPA

**How Do Errors Impact NN Accuracy on Non-Ideal Analog PIM? Fast Evaluation via an Error-Injected Robustness Metric** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes an error-injected robustness metric and a Non-Ideal PIM Accuracy (NIPA) model that unifies diverse analog-PIM error sources into a single weight-space representation, giving a non-slicing accuracy-evaluation method up to 105.8x faster than bit-and-crossbar slicing simulators like DNN+NeuroSim while matching accuracy within 0.29% average error and 0.91 correlation.

## Summary
The paper tackles the extreme simulation cost of evaluating DNN accuracy under non-ideal analog PIM hardware: standard simulators use a bit-and-crossbar slicing paradigm that evaluates each matrix-vector multiplication bit-by-bit and crossbar-by-crossbar, which becomes prohibitively slow for large models including LLMs. The authors propose an 'error-injected robustness metric' that unifies various software/hardware error sources (device variation, quantization, etc.) into the weight dimension, enabling joint error analysis. Building on this, they design a Non-Ideal PIM Accuracy (NIPA) evaluation model for fast relative accuracy evaluation that explicitly accounts for coupling between different error sources using the network's prior information (e.g., weight/activation statistics), and further propose a non-slicing absolute accuracy evaluation method that removes the need for the slow bit-and-crossbar slicing process entirely. Experiments on CNNs and LLMs show NIPA achieves correlations up to 0.91 with the absolute accuracy computed by DNN+NeuroSim, and the non-slicing method achieves up to 105.8x speedup over existing slicing-based evaluators with average evaluation error as low as 0.29%.

## Contributions
- Error-injected robustness metric that unifies heterogeneous analog-PIM error sources (software and hardware) into a single weight-dimension representation
- NIPA evaluation model for fast relative accuracy evaluation that models coupling effects between error sources using NN prior information
- Non-slicing absolute accuracy evaluation method that avoids the costly bit-by-bit, crossbar-by-crossbar slicing simulation
- Validation on both CNNs and LLMs, including comparison against the DNN+NeuroSim bit-and-crossbar slicing baseline

## Key claims (stable IDs)
- **2025_Guo_NIPA_ICCAD#C1** — NIPA's relative accuracy evaluation correlates strongly with ground-truth absolute accuracy from a standard slicing simulator — _support:_ Correlation up to 0.91 with absolute accuracy evaluated by DNN+NeuroSim — _loc:_ Abstract
- **2025_Guo_NIPA_ICCAD#C2** — The non-slicing absolute accuracy method is dramatically faster than bit-and-crossbar slicing evaluation while remaining accurate — _support:_ Up to 105.8x speedup with average evaluation error as low as 0.29% compared to existing slicing-based methods — _loc:_ Abstract

## Results
- Up to 105.8x speedup over bit-and-crossbar slicing-based accuracy evaluation methods
- Average evaluation error as low as 0.29% for the non-slicing absolute accuracy method
- Correlation up to 0.91 between NIPA relative-accuracy metric and DNN+NeuroSim absolute accuracy
- Validated on CNNs and LLMs (specific models/benchmarks not confirmable beyond the abstract since full text was not accessible)

## Limitations
- Full text not accessible to this reviewer (no open preprint found); exact models, error types, and experimental configurations beyond the abstract could not be verified
- Reported speedup/correlation figures are relative to a specific baseline (DNN+NeuroSim slicing simulation), so generality across other simulators/error models is unconfirmed from the abstract alone

## Remarks
Abstract-only assessment: ICCAD proceedings are not downloadable here and no arXiv preprint was found. This is squarely a simulation/benchmarking-framework contribution (category 08) that directly addresses a practical bottleneck for anyone trying to evaluate LLM-scale models on non-ideal analog PIM hardware — the combinatorial cost of bit-sliced, crossbar-by-crossbar Monte Carlo simulation. If the claimed 100x+ speedup with sub-1% error holds up, it would be a useful tool for thesis-level design-space exploration, but the fairness of the comparison and generality beyond DNN+NeuroSim-style baselines cannot be verified without the full paper.

## Cites (in collection, 12)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023)
- [2023_Sun_AIMCvsDIMC_ICCAD](2023_Sun_AIMCvsDIMC_ICCAD.md) AIMC-vs-DIMC (ZigZag-IMC) (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2025_Guo_NIPA_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccad66269.2025.11240851
