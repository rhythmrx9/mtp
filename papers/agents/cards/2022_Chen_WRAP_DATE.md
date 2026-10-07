---
id: W4280592620
key: 2022_Chen_WRAP_DATE
title: "WRAP: Weight RemApping and Processing in RRAM-based Neural Network Accelerators Considering Thermal Effect"
short: "WRAP"
year: 2022
venue: "DATE"
venue_full: "Design, Automation and Test in Europe Conference (DATE 2022)"
authors: "Po-Yuan Chen, Fang-Yi Gu, Yühong Huang, Ing-Chao Lin"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["thermal", "weight-mapping", "cnn-accelerator", "crossbar-architecture"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 5
citations_overall: 15
priority_score: 4.74
doi: "https://doi.org/10.23919/date54114.2022.9774678"
pdf: null
fulltext: null
---

# WRAP

**WRAP: Weight RemApping and Processing in RRAM-based Neural Network Accelerators Considering Thermal Effect** — Design, Automation and Test in Europe Conference (DATE 2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
WRAP is a subarray-based, thermal-aware weight remapping and processing framework that maps DNN weights onto RRAM subarrays (rather than individual cells) to reduce computational complexity while compensating for temperature-dependent resistance variation, keeping accuracy loss under 2% (1% with compensation) at ambient temperatures up to ~360K.

## Summary
RRAM-based compute-in-memory accelerators lose accuracy both from intrinsic cell-to-cell resistance variation and from temperature-dependent resistance drift, which worsens at high operating temperatures. WRAP proposes a subarray-based weight remapping and processing framework: instead of analyzing and compensating weights/cells individually, it operates on RRAM subarrays, applying subarray-level algorithms to reduce the computational complexity of thermal-aware mapping while preserving accuracy. Evaluated across four DNN models, WRAP keeps inference accuracy loss below 2% relative to the ideal (noiseless) result, and below 1% when its thermal compensation is applied, even when the surrounding temperature is around 360 K.

## Contributions
- A subarray-based (rather than per-cell) framework for mapping and remapping DNN weights onto RRAM crossbars, reducing the computational cost of thermal-aware weight placement
- Subarray-level algorithms that account for thermal effects on RRAM resistance during weight mapping
- A compensation mechanism that further reduces temperature-induced accuracy loss
- Evaluation across four DNN models demonstrating accuracy robustness up to ~360 K ambient temperature

## Key claims (stable IDs)
- **2022_Chen_WRAP_DATE#C1** — WRAP keeps inference accuracy loss under 2% relative to the ideal result across four DNN models despite high ambient temperature. — _support:_ Accuracy loss <2% at ~360K surrounding temperature without compensation — _loc:_ Abstract (full text not available)
- **2022_Chen_WRAP_DATE#C2** — Applying WRAP's thermal compensation further reduces accuracy loss to under 1%. — _support:_ Accuracy loss <1% at ~360K with compensation applied — _loc:_ Abstract (full text not available)

## Results
- Inference accuracy loss <2% (without compensation) across four DNN models at ~360K ambient temperature
- Inference accuracy loss <1% (with thermal compensation applied) at ~360K ambient temperature

## Limitations
- Analysis is abstract-only here (full text not accessible from this machine) -- the specific DNN models/datasets evaluated, the subarray size/granularity used, and the overhead of the remapping algorithm are not verifiable without the full text
- As a DATE architecture paper, results are expected to be simulation-based rather than measured silicon, though this could not be confirmed from the abstract alone

## Remarks
Addresses a practically important and under-examined non-ideality -- temperature-dependent RRAM resistance variation -- with a subarray-granularity remapping approach that trades fine per-cell precision for tractable computational complexity, which is a sensible engineering compromise for thermal-aware mapping at scale. It builds directly on the same group's prior thermal-aware optimization framework (Shin et al., cited in-set) and is itself cited by later Transformer-on-CIM pipeline work (COMET-3D), suggesting the subarray-thermal-mapping idea carries forward into more complex accelerator designs; without the full text, the precise accuracy/overhead trade-off curve and generalization beyond the four tested models could not be assessed here.

## Cites (in collection, 5)
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 1)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2022_Chen_WRAP_DATE.pdf`)
- Full text: none
- DOI: https://doi.org/10.23919/date54114.2022.9774678
