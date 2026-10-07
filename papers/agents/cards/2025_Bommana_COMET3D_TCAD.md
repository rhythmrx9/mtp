---
id: W4413394346
key: 2025_Bommana_COMET3D_TCAD
title: "COMET-3D: Compute-in-Memory-Based Transformer Accelerator With Optimized Pipeline and 3D Heterogeneous Integration"
short: "COMET-3D"
year: 2025
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Ashish Reddy Bommana, Farshad Firouzi, Krishnendu Chakrabarty"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["SRAM-analog", "ReRAM"]
models: ["Transformer", "BERT", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["3d-integration", "heterogeneous-analog-digital", "transformer-accelerator", "dataflow-pipelining", "attention", "chiplets"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 13
citations_overall: 7
priority_score: 5.63
doi: "https://doi.org/10.1109/tcad.2025.3601526"
pdf: null
fulltext: null
---

# COMET-3D

**COMET-3D: Compute-in-Memory-Based Transformer Accelerator With Optimized Pipeline and 3D Heterogeneous Integration** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
COMET-3D is a 3D heterogeneous compute-in-memory accelerator that pairs SRAM- and ReRAM-based CIM arrays with a logic die (digital MAC + softmax units) and a latency-optimized, operational-unit-aware pipeline for multi-head self-attention, achieving up to 34x EDP improvement on LLAMA versus similarly-resourced baselines.

## Summary
The paper argues that existing CIM-based Transformer accelerators rest on unrealistic assumptions (single-cycle activation of an entire crossbar), use pipelines not optimized for operational-unit (OU)-based execution, and incur high ADC cost. To address these, the authors propose a latency-optimized pipeline tailored to OU-based CIM execution, and COMET-3D, a 3D heterogeneous architecture stacking SRAM- and ReRAM-based CIM arrays with a logic die containing digital MAC units and softmax modules. The architecture and dataflow are designed to maximize hardware utilization for the multi-head self-attention (MHSA) layer specifically. Evaluated across BERT, GPT2, and LLaMA, COMET-3D outperforms baseline architectures with comparable compute resources, with the largest gains on the largest model (LLaMA).

## Contributions
- Identifies three limitations of prior CIM Transformer accelerators: unrealistic single-cycle whole-crossbar activation, OU-execution-unaware pipelines, and high ADC cost
- Proposes a latency-optimized pipeline specifically tailored for operational-unit (OU)-based CIM execution
- Introduces COMET-3D, a 3D heterogeneous architecture integrating SRAM- and ReRAM-based CIM arrays with a digital logic die (MAC units + softmax modules) via 3D integration
- Designs the dataflow to maximize hardware utilization specifically for multi-head self-attention (MHSA) acceleration
- Evaluates across BERT, GPT2 and LLaMA, demonstrating large energy-delay-product (EDP) gains over similarly-resourced baselines

## Key claims (stable IDs)
- **2025_Bommana_COMET3D_TCAD#C1** — COMET-3D achieves large EDP improvements over baseline CIM architectures with similar compute resources, with gains scaling with model size — _support:_ Up to 34x EDP improvement for LLAMA, 7.4x for GPT2, and 4.3x for BERT-Large — _loc:_ Abstract

## Results
- Up to 34x energy-delay-product (EDP) improvement for LLaMA vs. baseline architectures with similar compute resources
- 7.4x EDP improvement for GPT2
- 4.3x EDP improvement for BERT-Large

## Limitations
- Evaluation is simulation-based (architecture/CAD-level, consistent with the TCAD venue); no fabricated 3D chip is reported in the abstract
- 3D heterogeneous integration (SRAM + ReRAM CIM arrays + digital logic die) introduces assembly/thermal/yield considerations not addressed in the abstract
- Gains are reported relative to baselines with 'similar compute resources' as defined by the authors; the specific baseline architectures and their representativeness of the broader CIM-Transformer literature are not stated in the abstract

## Remarks
The explicit critique of the 'single-cycle whole-crossbar activation' assumption used in earlier CIM Transformer accelerator papers is a useful methodological point for mapping research -- it suggests that OU (operational-unit)-level timing realism materially changes design conclusions for self-attention acceleration. The EDP gains scaling with model size (34x for LLaMA vs. 4.3x for BERT-Large) is consistent with larger models amortizing the fixed overhead of 3D-integrated digital logic (softmax/MAC) more effectively, but this should be checked against the full text's baseline definitions before citing the headline multipliers.

## Cites (in collection, 13)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022)
- [2022_Chen_WRAP_DATE](2022_Chen_WRAP_DATE.md) WRAP (2022)
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025)
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025)
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2025_Bommana_COMET3D_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2025.3601526
