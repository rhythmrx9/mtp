---
id: W3184191382
key: 2021_Yuan_TinyADC_DATE
title: "TinyADC: Peripheral Circuit-aware Weight Pruning Framework for Mixed-signal DNN Accelerators"
short: "TinyADC"
year: 2021
venue: "DATE"
venue_full: "Design, Automation & Test in Europe Conference (DATE 2021)"
authors: "Geng Yuan, Payman Behnam, Yuxuan Cai, Ali Reza Shafiee, Jingyan Fu, Zhiheng Liao, Zhengang Li, Xiaolong Ma, Jieren Deng, Jinhui Wang, Mahdi Nazm Bojnordi, Yanzhi Wang et al."
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "adc-dac", "peripheral-circuits", "energy-efficiency", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 6
citations_overall: 30
priority_score: 5.35
doi: "https://doi.org/10.23919/date51398.2021.9474235"
pdf: null
fulltext: null
---

# TinyADC

**TinyADC: Peripheral Circuit-aware Weight Pruning Framework for Mixed-signal DNN Accelerators** — Design, Automation & Test in Europe Conference (DATE 2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
TinyADC is a weight-pruning framework for ReRAM-based mixed-signal DNN accelerators that is explicitly aware of peripheral ADC circuit cost, reducing required ADC resolution (and thus area/power) without introducing computational inaccuracy, achieving 3.5x power and 2.9x area reduction vs state-of-the-art pruning on ImageNet.

## Summary
Prior ReRAM-crossbar weight-pruning work for mixed-signal DNN accelerators largely ignores peripheral circuitry, even though ADCs dominate the area and power budget of such accelerators. TinyADC proposes a pruning framework that is peripheral-circuit-aware: by constraining how weights are pruned/mapped onto crossbar columns, it reduces the number of ADC resolution bits actually required, cutting ADC area and power without degrading computational accuracy (i.e., without approximating the MVM result). The approach targets the ADC overhead directly rather than treating crossbar/weight-storage reduction as the only optimization goal, situating it as a direct refinement of prior ReRAM pruning frameworks (e.g., TinyButAcc, the ADMM-based structured pruning line of work by the same group). Evaluated against a state-of-the-art pruning baseline on ImageNet, TinyADC achieves 3.5x power and 2.9x area reduction for the ADC/peripheral subsystem, and improves overall architecture throughput by 29% (GOPs/s*mm^2) and 40% (GOPs/W).

## Contributions
- Identifies that existing ReRAM DNN pruning frameworks largely overlook ADC/peripheral circuit cost despite ADCs dominating accelerator area/power
- Proposes a peripheral-circuit-aware weight pruning framework (TinyADC) that reduces required ADC resolution bits as a first-class optimization target
- Achieves ADC resolution/area/power reduction without introducing computational inaccuracy (i.e., no approximation of the dot-product result)
- Demonstrates improved throughput-per-area and throughput-per-power over a state-of-the-art accelerator baseline

## Key claims (stable IDs)
- **2021_Yuan_TinyADC_DATE#C1** — TinyADC reduces peripheral circuit (power/area) cost relative to state-of-the-art pruning on ImageNet — _support:_ 3.5x power reduction and 2.9x area reduction compared to state-of-the-art pruning work on ImageNet — _loc:_ Abstract
- **2021_Yuan_TinyADC_DATE#C2** — TinyADC improves accelerator throughput efficiency — _support:_ 29% improvement in GOPs/(s*mm^2) and 40% improvement in GOPs/W over state-of-the-art architecture design — _loc:_ Abstract

## Results
- 3.5x ADC power reduction vs state-of-the-art pruning baseline on ImageNet
- 2.9x ADC area reduction vs state-of-the-art pruning baseline on ImageNet
- 29% throughput-per-area (GOPs/s*mm^2) improvement over state-of-the-art architecture
- 40% throughput-per-power (GOPs/W) improvement over state-of-the-art architecture

## Limitations
- Full text not available to this analysis (abstract-only basis); specific network architectures, pruning ratios, ADC resolution numbers, and experimental methodology could not be independently verified
- Based on the abstract, evaluation appears limited to ImageNet-scale CNN classification and simulation/estimation rather than fabricated silicon

## Remarks
TinyADC is a direct, closely-related follow-up/companion to the same group's ADMM-based structured pruning work (e.g., 'Tiny but Accurate') and to TinyADC's successor FORMS, which explicitly cites it as addressing ADC overhead via pruning. Because full text could not be located (not on arXiv, and other open-access aggregators were rate-limited or blocked), this entry is abstract-only and the quantitative claims are taken at face value from the DATE 2021 abstract; a thesis treatment should try to obtain the DATE proceedings version via a library for figure/table-level detail on the pruning method and ADC resolution reduction technique.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019)
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019)
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 3)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _contrasts/critiques_: "TinyADC [40] proposes a pruning solution that fixes the number of non-zero weights in each column of the ReRAM crossbar while their positions can vary."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _contrasts/critiques_: "TinyADC [79] retrains while pruning DNN weight bits, achieving impressive reductions in column sum resolution."
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2021_Yuan_TinyADC_DATE.pdf`)
- Full text: none
- DOI: https://doi.org/10.23919/date51398.2021.9474235
