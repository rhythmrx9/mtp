---
id: W4405718102
key: 2024_Lv_NonIdealPIMFineTuning_TCAD
title: "Improving DNN Accuracy on MLC PIM via Non-Ideal PIM Device Fine-Tuning"
short: "Non-Ideal PIM Fine-Tuning"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)"
authors: "Hao Lv, Lei Zhang, Ying Wang"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "device-variation", "calibration-compensation", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 38
priority_score: 5.11
doi: "https://doi.org/10.1109/tcad.2024.3521195"
pdf: null
fulltext: null
---

# Non-Ideal PIM Fine-Tuning

**Improving DNN Accuracy on MLC PIM via Non-Ideal PIM Device Fine-Tuning** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024) (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
The paper recasts model-accuracy recovery on multilevel RRAM (one-to-one weight-cell mapping, no precise programming) as a non-ideal PIM device optimization problem and proposes a knowledge-distillation-guided fine-tuning scheme that uses the on-chip model's own input/output to recover nearly all accuracy lost to device variation, beating variation-aware training by over 3%.

## Summary
Multilevel RRAM cells are attractive for one-to-one weight-cell mapping (better memory utilization than multi-cell encoding of a weight), but RRAM variation (device variation, read disturbance, limited on/off ratio) causes the mapped weight to deviate from its intended value, degrading model accuracy, and this problem is exacerbated as DNN model sizes grow. Rather than requiring precise weight programming (the conventional multi-cell-per-weight workaround), the authors frame post-deployment accuracy recovery on multilevel RRAM as a non-ideal PIM device optimization problem, and systematically study how different fine-tuning strategies behave when recovering accuracy under this non-ideal setting. Based on this analysis, they propose a fine-tuning scheme that leverages knowledge distillation together with the input/output behavior of the deployed (non-ideal) model itself to guide the fine-tuning process, restoring accuracy without needing precise weight programming or an accurate per-cell noise profile. Experiments show the scheme achieves nearly complete recovery of model performance on multilevel RRAM, improving accuracy by over 3% compared to variation-aware training baselines.

## Contributions
- Reframing of RRAM-variation-induced accuracy loss under one-to-one weight-cell mapping as a 'non-ideal PIM device optimization' problem rather than a programming-precision problem
- A systematic analysis of how various fine-tuning strategies perform at recovering accuracy under this non-ideal device setting
- A knowledge-distillation-based fine-tuning scheme that uses the deployed model's own input/output information (rather than requiring precise device-noise profiling) to guide recovery
- Demonstrated near-complete accuracy recovery and >3% improvement over variation-aware training approaches

## Key claims (stable IDs)
- **2024_Lv_NonIdealPIMFineTuning_TCAD#C1** — The proposed fine-tuning scheme achieves nearly complete recovery of model accuracy under multilevel RRAM non-ideality — _support:_ 'achieving nearly complete recovery of model performance' (abstract) — _loc:_ Abstract
- **2024_Lv_NonIdealPIMFineTuning_TCAD#C2** — The method outperforms variation-aware training baselines — _support:_ 'over a 3% improvement in model accuracy compared to variation-aware training approaches' (abstract) — _loc:_ Abstract

## Results
- >3% accuracy improvement over variation-aware training baselines
- Near-complete recovery of model performance under non-ideal multilevel RRAM device settings (exact accuracy figures not available from abstract alone)

## Limitations
- Abstract-only analysis in this record: full text unavailable, so the exact fine-tuning/distillation algorithm, models/datasets used, and comparison baselines beyond 'variation-aware training' could not be verified
- Approach appears to require post-deployment fine-tuning access to the chip's own input/output behavior, which may have practical constraints (data availability, latency/energy cost of fine-tuning on edge) not assessable from the abstract

## Remarks
This addresses a practically important variant of the hardware-aware training problem: most non-ideality-robustness work (e.g. this paper's own in-set references on accelerator-friendly training, program/verify schemes) either assumes training-time noise injection or write-verify at programming time, whereas this paper targets post-deployment recovery without precise programming, framed via knowledge distillation against the model's own non-ideal behavior. Because only the abstract was available, it is not possible to assess how this compares quantitatively to write-verify (program/verify) approaches or how much fine-tuning data/compute it requires, which would matter for its practicality on resource-constrained PIM edge devices.

## Cites (in collection, 9)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2024_Lv_NonIdealPIMFineTuning_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2024.3521195
