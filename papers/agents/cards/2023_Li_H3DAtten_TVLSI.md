---
id: W4385656513
key: 2023_Li_H3DAtten_TVLSI
title: "H3DAtten: Heterogeneous 3-D Integrated Hybrid Analog and Digital Compute-in-Memory Accelerator for Vision Transformer Self-Attention"
short: "H3DAtten"
year: 2023
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems"
authors: "Wantong Li, Madison Manley, James Read, Ankit Kaul, Muhannad S. Bakir, Shimeng Yu"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-analog"]
models: ["ViT", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["3d-integration", "heterogeneous-analog-digital", "attention", "transformer-accelerator", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 8
cites_in_collection: 7
citations_overall: 30
priority_score: 8.4
doi: "https://doi.org/10.1109/tvlsi.2023.3299509"
pdf: null
fulltext: null
---

# H3DAtten

**H3DAtten: Heterogeneous 3-D Integrated Hybrid Analog and Digital Compute-in-Memory Accelerator for Vision Transformer Self-Attention** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
H3DAtten is a heterogeneous 3D-integrated accelerator for vision-transformer multi-head self-attention that stacks a 40nm RRAM analog-CIM tier with a 16nm SRAM digital-CIM tier, reporting 8.4x compute density over iso-capacity 2D baselines with no accuracy loss on ImageNet-1k.

## Summary
Vision transformers' multi-head self-attention (MHSA) is costly to run on conventional hardware due to the memory wall, and 2D compute-in-memory (CIM) designs must grow their footprint to hold increasingly large models. H3DAtten proposes heterogeneous 3D (H3D) integration that combines RRAM-based analog CIM (ACIM, 40nm) and SRAM-based digital CIM (DCIM, 16nm) tiers to target MHSA workloads specifically, exploiting the different strengths of analog (density/efficiency) and digital (precision) compute-in-memory within a single stacked package. The authors perform signaling and thermal analyses to characterize the effects of 3D stacking (e.g., inter-tier interconnect and heat) on the accelerator's behavior. A proposed 5-tier H3DAtten accelerator is compared against iso-capacity 2D CIM baselines, achieving 8.4x compute density without accuracy loss on ImageNet-1k.

## Contributions
- A heterogeneous 3D-integrated (H3D) CIM architecture combining RRAM analog-CIM (40nm) and SRAM digital-CIM (16nm) tiers in one package
- Targets vision transformer multi-head self-attention (MHSA) specifically, rather than only the linear/MVM-dominated feed-forward layers
- Comprehensive signaling and thermal analysis of the effects of 3D stacking on the accelerator
- A 5-tier H3DAtten design demonstrating 8.4x compute density over iso-capacity 2D baselines with no ImageNet-1k accuracy loss

## Key claims (stable IDs)
- **2023_Li_H3DAtten_TVLSI#C1** — 3D heterogeneous integration of analog and digital CIM tiers substantially increases compute density for ViT self-attention without hurting accuracy — _support:_ 8.4x compute density vs. iso-capacity 2D baseline designs, no accuracy loss on ImageNet-1k — _loc:_ Abstract

## Results
- 8.4x compute density vs. iso-capacity 2D CIM baseline designs (5-tier H3DAtten)
- No accuracy loss on ImageNet-1k

## Limitations
- Analysis based on abstract only (full text not accessible); the mix/partitioning of ACIM vs. DCIM tiers, exact self-attention mapping scheme, and thermal/signaling analysis details could not be verified
- 3D-stacking results (thermal, interconnect) are based on simulation/analysis rather than fabricated 3D silicon

## Remarks
H3DAtten is an architecture-level contribution notable for combining heterogeneous device classes (RRAM analog-CIM and SRAM digital-CIM) across 3D-stacked tiers specifically for the self-attention bottleneck in vision transformers, rather than treating CIM as homogeneous. It has a substantial in-set forward citation footprint (AESHA, COMET-3D, SAGE, Harmony, HyPIM, etc.), indicating it is an influential reference point for later hybrid CIM/ViT accelerator work; full-text access would be valuable to confirm the exact attention-mapping and 3D thermal/signaling methodology.

## Cites (in collection, 7)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC](2020_Wan_TransposableRRAMNeurosynapticCore_ISSCC.md) Transposable RRAM Neurosynaptic Core (2020)
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)

## Cited by (in collection, 8)
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _background_: "In addition to these approaches, some research [20–23] employs heterogeneous RRAM-SRAM CIM designs to balance low-precision prediction and exact computation workloads towards providing low-power and efficient solutions."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _background_: "Due to the non-ideal effects of RRAM ACIM and the low-density of SRAM DCIM, a heterogeneous architecture has been adopted in prior research on CIM-based Transformer accelerators [5-16]."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _baseline/comparison_: "H3DAtten [30] proposed the heterogeneous 3D-PIM architecture of ReRAM+SRAM and considered the hardware characteristics."
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)
- [2024_Li_MemristorCiMLLM_IoTJ](2024_Li_MemristorCiMLLM_IoTJ.md) MemristorCiMLLM (2024)

## Files
- PDF: not available locally (save as `papers/04_Transformers_and_LLMs/2023_Li_H3DAtten_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2023.3299509
