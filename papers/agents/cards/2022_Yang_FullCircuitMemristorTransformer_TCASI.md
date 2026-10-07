---
id: W4205363571
key: 2022_Yang_FullCircuitMemristorTransformer_TCASI
title: "Full-Circuit Implementation of Transformer Network Based on Memristor"
short: "Full-Circuit Memristor Transformer"
year: 2022
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 69, no. 4, pp. 1395-1407 (2022)"
authors: "Chao Yang, Xiaoping Wang, Zhigang Zeng"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["Memristor(generic)"]
models: ["Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "nonlinear-functions", "analog-mvm", "peripheral-circuits", "crossbar-architecture"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 4
citations_overall: 66
priority_score: 7.87
doi: "https://doi.org/10.1109/tcsi.2021.3136355"
pdf: null
fulltext: null
---

# Full-Circuit Memristor Transformer

**Full-Circuit Implementation of Transformer Network Based on Memristor** — IEEE Transactions on Circuits and Systems I: Regular Papers, vol. 69, no. 4, pp. 1395-1407 (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
An all-analog, full-circuit memristor implementation of the Transformer network -- crossbar VMM plus dedicated analog circuit modules for softmax, layer normalization, ReLU, multiply-add and residual connections -- that computes end-to-end without any ADC, DAC or digital memory, verified in PSPICE on a character image-recognition task.

## Summary
The paper proposes what it presents as the first full-circuit (entirely analog) implementation of a Transformer network using memristors, rather than offloading only the matrix multiplications to crossbars while handling nonlinear Transformer operations (softmax, layer norm, residual, activations) digitally. The design comprises: (1) a memristor crossbar module storing weights and performing vector-matrix multiplication; (2) an analog signal memory module that stores intermediate analog signals in near-memory fashion (avoiding repeated analog-to-digital round trips); (3) dedicated analog function-circuit modules realizing softmax, layer normalization, ReLU, multiply-add and residual-connection transformations; and (4) a timing-signal generation module to sequence circuit operation. Because all signal paths stay analog, the design needs no ADC, DAC, or digital memory anywhere in the pipeline. The authors verify functional correctness in PSPICE using a character image-recognition task and analyze signal retention of the analog memory, overall circuit performance, and the impact of memristor non-idealities, reporting advantages in area overhead, energy efficiency, and noise tolerance relative to (unspecified in the abstract) comparison points.

## Contributions
- A memristor-crossbar module for Transformer weight storage and vector-matrix multiplication
- An analog signal memory module that retains intermediate activations in near-memory analog form, avoiding repeated ADC/DAC conversion between Transformer sub-layers
- Dedicated analog function-circuit modules implementing softmax, layer normalization, ReLU, multiply-add, and residual connections directly in the analog domain
- A timing-signal generation module to schedule the full set of circuit operations
- An end-to-end, ADC/DAC/digital-memory-free analog Transformer circuit verified functionally in PSPICE

## Key claims (stable IDs)
- **2022_Yang_FullCircuitMemristorTransformer_TCASI#C1** — A Transformer network can be implemented end-to-end in the analog domain using memristors without any ADC, DAC, or digital memory. — _support:_ Full circuit design (crossbar + analog memory + analog function circuits + timing control) verified functionally in PSPICE on a character image-recognition task — _loc:_ Abstract (full text not available)
- **2022_Yang_FullCircuitMemristorTransformer_TCASI#C2** — The proposed all-analog Transformer circuit has advantages in area overhead, energy efficiency, and noise tolerance. — _support:_ Stated as a conclusion from PSPICE-based circuit performance and memristor-non-ideality analysis — _loc:_ Abstract (full text not available)

## Results
- Functional correctness of the full analog Transformer circuit verified via PSPICE simulation on a character image-recognition task (per abstract; no specific accuracy/throughput/energy numbers given in the abstract)

## Limitations
- Analysis is abstract-only here (full text not accessible from this machine; only IEEE Xplore hosts it and no legitimate open copy was found) -- quantitative results, baseline comparisons, and the scale of the demonstrated Transformer are not independently verifiable
- As described, evaluation is circuit-level SPICE simulation on a small character-recognition task, not a fabricated chip or a large-scale NLP/vision Transformer benchmark

## Remarks
Notable for pushing analog Transformer implementation beyond just the matmul/attention-score crossbar step to also realize softmax, layer-norm and residual connections in the analog domain, eliminating per-sublayer ADC/DAC conversions that dominate many other analog-Transformer proposals. Being a circuit-simulation (PSPICE) study rather than silicon, and evaluated on what the abstract describes as a small character-image task, its claims about area/energy/noise advantages should be read as circuit-level, simulation-based estimates; later citing works (e.g., TReX, cascaded ReRAM Transformer accelerators) suggest it is referenced primarily for its all-analog nonlinear-function circuit modules rather than as a scaled system.

## Cites (in collection, 4)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 4)
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _contrasts/critiques_: "Yang et al. [48] use analog signal memory and analog multiply-add circuits to eliminate ReRAM write operations for intermediate results."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _background_: "Recently, many works have proposed efficient IMC implementations for transformers [10], [11]. The authors in [10] propose fully analog implementations for transformers by using memristive circuits for dot-product operations and analog circuits for implementing non-linear functions such as GeLU, ReLU and softmax."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _motivation_: "For attention blocks, dynamic matrix-matrix multiplication (MatMul) necessitates extensive write-verify operations in RRAM [47, 48]."
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2022_Yang_FullCircuitMemristorTransformer_TCASI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcsi.2021.3136355
