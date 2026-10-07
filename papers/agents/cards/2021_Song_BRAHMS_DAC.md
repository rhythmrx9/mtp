---
id: W3212662098
key: 2021_Song_BRAHMS_DAC
title: "BRAHMS: Beyond Conventional RRAM-based Neural Network Accelerators Using Hybrid Analog Memory System"
short: "BRAHMS"
year: 2021
venue: "DAC"
venue_full: "ACM/IEEE 58th Design Automation Conference (DAC 2021)"
authors: "Tao Song, Xiaoming Chen, Xiaoyu Zhang, Yinhe Han"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "adc-dac", "peripheral-circuits", "dataflow-pipelining", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 7
cites_in_collection: 8
citations_overall: 15
priority_score: 7.05
doi: "https://doi.org/10.1109/dac18074.2021.9586247"
pdf: null
fulltext: null
---

# BRAHMS

**BRAHMS: Beyond Conventional RRAM-based Neural Network Accelerators Using Hybrid Analog Memory System** — ACM/IEEE 58th Design Automation Conference (DAC 2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
BRAHMS eliminates redundant analog-to-digital conversions in RRAM-based CNN accelerators by fusing post-MAC operations (shift-add, pooling, activation, etc.) into analog resistive content-addressable memory (ARCAM) arrays, reporting several-fold throughput and >10x energy-efficiency gains over an ISAAC-like baseline.

## Summary
The paper targets the ADC/DAC overhead in conventional RRAM-based CNN accelerators, observing that many AD conversions performed after a crossbar MAC are redundant because the result is immediately fed into further arithmetic (e.g., shift-and-add across bit-sliced partial sums, or pooling/activation). It proposes BRAHMS, which reorders operations following a convolutional or fully-connected layer and groups them into 'fused operators' (FOPs) that are executed as a whole inside analog resistive content-addressable memory (ARCAM) arrays rather than through digital logic and ADCs. The resulting architecture is a mixed-signal pipeline that keeps signals in the analog domain within an FOP and only converts to digital between FOPs, reducing conversion counts while reusing RRAM crossbars for both matrix-vector multiplication and the fused post-processing operators. Compared with an ISAAC-like baseline architecture, simulation results show BRAHMS improves performance by several times and average energy efficiency by over 10x.

## Contributions
- Identifies redundant analog-to-digital conversions as a major inefficiency in conventional RRAM-based CNN accelerators
- Proposes 'fused operators' (FOPs) that reorder and merge post-MAC operations (e.g., shift-add, pooling) to avoid unnecessary AD/DA conversions
- Introduces analog resistive content-addressable memory (ARCAM) arrays as the hardware substrate implementing FOPs without digital logic or ADCs
- Designs a mixed-signal pipeline (BRAHMS) that keeps data analog within an FOP and digital only between FOPs
- Reports simulation-based performance and energy comparisons against an ISAAC-like RRAM CNN accelerator baseline

## Key claims (stable IDs)
- **2021_Song_BRAHMS_DAC#C1** — Conventional RRAM-based CNN accelerators perform redundant analog-to-digital conversions that waste energy — _support:_ Abstract: conventional mixed-signal accelerators use DACs/ADCs that cause performance and energy efficiency degradation; BRAHMS eliminates 'redundant AD conversions' — _loc:_ Abstract
- **2021_Song_BRAHMS_DAC#C2** — Fusing post-MAC operations into ARCAM arrays removes the need for digital logic and ADCs within a fused operator — _support:_ Abstract: FOPs 'are implemented as a whole by ARCAM arrays so that digital logic and ADCs are eliminated' — _loc:_ Abstract
- **2021_Song_BRAHMS_DAC#C3** — BRAHMS substantially outperforms an ISAAC-like RRAM CNN accelerator — _support:_ Abstract: 'compared with an ISAAC-like architecture, BRAHMS improves the performance by several times and the energy efficiency by 10+ times on average' — _loc:_ Abstract

## Results
- Several-times performance (throughput) improvement over an ISAAC-like RRAM-based CNN accelerator baseline (abstract-level figure, no further breakdown available)
- Average energy efficiency improvement of >10x over the ISAAC-like baseline (abstract-level figure)

## Limitations
- Only the abstract was available for this analysis (paper is paywalled, no open-access copy found); quantitative claims beyond the abstract (architectural details, benchmarks used, array sizes) could not be verified
- Evaluation is simulation-based; no silicon measurements are reported in the abstract
- Scope is limited to CNNs (convolutional/fully-connected layers); applicability to other workloads (RNN/Transformer) is not indicated

## Remarks
Abstract-only analysis: BRAHMS belongs to the line of work (alongside CASCADE, Neural-PIM, TinyADC) attacking ADC/DAC overhead in RRAM crossbar accelerators, here via a content-addressable-memory-based analog fusion of post-MAC operators rather than ADC-resolution reduction or peripheral-circuit-aware pruning. Because no full text was accessible, the strength of evidence and the precise mechanism of ARCAM fused operators cannot be independently verified beyond what the abstract states; the reported '10+x' energy efficiency gain should be treated as a headline claim pending verification against the full paper.

## Cites (in collection, 8)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018)
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 7)
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _contrasts/critiques_: "BRAHMS [57] tailors ADC quantization steps for each layer to maximize DNN accuracy under fidelity loss."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _contrasts/critiques_: "There are previous works (e.g., [5]–[9]) proposing NVM crossbar-based PIM DNN accelerators. However, they mainly focus on the design of specific architectures and lack consideration of the execution details of DNNs."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _uses-method-or-tool_: "The Library Plug-In models a library of components used in various CiM works [2, 6, 18, 29, 37, 38, 40, 44, 51, 57]."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _contrasts/critiques_: "Recently proposed IMC designs [7, 8] strive to eliminate ADCs but work only if the AI model contains ReLU-like non-linear functions, and thus lack the flexibility to adapt to evolving AI models."
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)

## Files
- PDF: not available locally (save as `papers/03_Crossbar_Accelerator_Architectures/2021_Song_BRAHMS_DAC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/dac18074.2021.9586247
