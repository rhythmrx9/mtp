---
id: W4416963215
key: 2025_Fu_CrossTypeMappedDataflow_ISLPED
title: "Optimizing Heterogeneous Compute-in-Memory with Hybrid Dataflow and In-Network Reduction for Vision Transformer"
short: "Cross-Type Mapped Dataflow"
year: 2025
venue: "ISLPED"
venue_full: "2025 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED 2025)"
authors: "Zexin Fu, Yihang Zuo, Yuzhe Ma, Jiayi Huang"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-digital"]
models: ["ViT", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["transformer-accelerator", "heterogeneous-analog-digital", "dataflow-pipelining", "scheduling", "tiling-partitioning", "crossbar-architecture", "adc-dac", "device-variation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 10
citations_overall: 1
priority_score: 6.11
doi: "https://doi.org/10.1109/islped65674.2025.11261801"
pdf: "../../04_Transformers_and_LLMs/2025_Fu_CrossTypeMappedDataflow_ISLPED.pdf"
fulltext: "../fulltext/2025_Fu_CrossTypeMappedDataflow_ISLPED.txt"
---

# Cross-Type Mapped Dataflow

**Optimizing Heterogeneous Compute-in-Memory with Hybrid Dataflow and In-Network Reduction for Vision Transformer** — 2025 IEEE/ACM International Symposium on Low Power Electronics and Design (ISLPED 2025) (2025)

## TL;DR
Flat-NoC heterogeneous RRAM analog-CIM plus SRAM digital-CIM ViT accelerator whose Hybrid Dataflow reuses idle cross-type CIMs for static VMMs and whose In-Network Reduction folds partial-sum accumulation into NoC routers, giving 4.63x speedup and 2.47-2.59x energy efficiency over an X-Former-like design in simulation.

## Summary
Static weight VMMs (QKV/projection/FFN) suit RRAM analog CIM (ACIM) while dynamic attention matmuls (QK^T, softmax x V) need runtime weight writes that are costly and inaccurate on RRAM, so prior designs map them to SRAM CIM. Such isolated mapping leaves one CIM type idle, and partial sums arising from crossbar row partitioning are reduced on global units adding routing redundancy. The proposed architecture is a flat mesh NoC mixing ACIM PEs (NeuroSim-style crossbars with dummy off-state columns for finite on/off ratio), SRAM DCIM PEs (AutoDCIM-based, 3:1 ACIM:DCIM ratio), INT8 SIMD PEs (I-ViT approximations for softmax/LayerNorm/GELU) and memory units. Hybrid Dataflow duplicates static weights into idle DCIMs for cross-type VMM collaboration; In-Network Reduction uses deadlock-aware software-scheduled routing and active routers to accumulate partial sums in transit. Evaluated with a cycle-level simulator (DCIM data scaled to 22nm, NeuroSim v1.3 analog, BookSim/DSENT NoC, CACTI DRAM) on DeiT-Tiny/Small/Base layers, and with modified NeuroSim v2.1 for ADC and device non-ideality accuracy.

## Contributions
- Flat heterogeneous analog-digital CIM NoC architecture enabling cross-type collaboration
- Hybrid Dataflow reusing idle CIM types for static VMMs
- In-Network Reduction with deadlock-aware routing for heterogeneous layouts, extending INA
- Evaluation against homogeneous DCIM, isolated mapping, X-Former-like and INA baselines

## Key claims (stable IDs)
- **2025_Fu_CrossTypeMappedDataflow_ISLPED#C1** — Heterogeneous CIM alone gives 3.57x speedup and 2.78x energy efficiency over homogeneous DCIM; with Hybrid Dataflow + INR, 4.63x / 2.59x over an X-Former-like design. — _support:_ abstract averages across ViT workloads (conclusion: 4.63x and 2.47x in Sec. VI) — _loc:_ Abstract; Sec. VI-B
- **2025_Fu_CrossTypeMappedDataflow_ISLPED#C2** — INR achieves 1.63x speedup and 1.47x energy efficiency over INA, and 4.28x / 3.17x on DeiT-Small at 1x1 granularity. — _support:_ INA routing failures 2/21 (DeiT-Small), 12/51 (DeiT-Base) fall back to SIMD — _loc:_ Sec. VI-B
- **2025_Fu_CrossTypeMappedDataflow_ISLPED#C3** — Homogeneous RRAM ACIM collapses on ViTs (0.12% DeiT-Tiny, 1.38% DeiT-Small) because of weight-update non-idealities, while heterogeneous CIM keeps 71.88% / 79.74%. — _support:_ drift coefficient 0.001, 10 s timespan — _loc:_ Sec. VI-C, Fig. 7
- **2025_Fu_CrossTypeMappedDataflow_ISLPED#C4** — ADC resolution of 8 bits or more causes <1% accuracy loss; 6 bits or fewer is ineffective. — _support:_ Fig. 7 bars — _loc:_ Sec. VI-C

## Results
- Hybrid Dataflow + INR: 4.91x speedup, 2.64x energy efficiency over isolated-mapping heterogeneous CIM (Sec. VI-B)
- INR alone: 3.37x speedup and 2.63x energy efficiency over IsolatedMap on average
- Accuracy at ADC >= 8b loss <1%; heterogeneous CIM 71.88% (DeiT-Tiny), 79.74% (DeiT-Small) vs homogeneous RRAM ACIM 0.12% / 1.38% under drift/variation/update non-idealities

## Key numbers
- tech_node: 22nm (scaled DCIM)
- energy_eff: 2.47-2.59x vs X-Former-like
- throughput: 4.63x speedup vs X-Former-like
- accuracy: 71.88% DeiT-Tiny, 79.74% DeiT-Small (heterogeneous, drift 0.001)
- bits_weight: INT8 (SIMD)
- bits_adc: >=8b

## Datasets / benchmarks
DeiT-Tiny, DeiT-Small, DeiT-Base

## Limitations
- Simulation only with small workloads (DeiT-Tiny/Small/Base layers, short sequences); no silicon
- Finite on/off ratio not simulated (assumed solved by dummy columns)
- Periodic weight calibration still needed when drift coefficient >=0.003
- Vision transformers only; no language-model workloads or KV-cache/decoder behaviour
- X-Former-like baseline is a re-implementation

## Remarks
An architecture/NoC paper where most gain comes from scheduling and network side (PE utilisation, removing reduction hops) rather than analog compute. Its main lesson for crossbar mapping is that partial-sum reduction from limited crossbar rows can dominate NoC traffic and be absorbed into routers. The accuracy study gives a simple simulated argument for the now-standard split (static weights on NVM, dynamic attention on SRAM). Evidence is limited, so conclusions for LLMs are indirect.

## Cites (in collection, 10)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "Digital CIM data is from [21] and scaled to 22nm via [25] while analog CIM data is extracted from NeuroSim v1.3 [26]."
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _background_: "Device engineering [36] and circuit-device co-design [37] can further alleviate effects, which is out of the scope of this work."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "We modify NeuroSim v2.1 [30] to evaluate the non-ideal effects."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _uses-method-or-tool_: "The finite on/off ratio impact is not incorporated, as prior work has demonstrated that it can be effectively mitigated via the dummy column scheme [35]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _background_: "Due to the non-ideal effects of RRAM ACIM and the low-density of SRAM DCIM, a heterogeneous architecture has been adopted in prior research on CIM-based Transformer accelerators [5-16]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _baseline/comparison_: "Previous studies have proposed using SRAM-based Analog CIM [7, 10, 13, 16] or Digital CIM [8, 9] to perform DMM operations."
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023) — _background_: "Due to the non-ideal effects of RRAM ACIM and the low-density of SRAM DCIM, a heterogeneous architecture has been adopted in prior research on CIM-based Transformer accelerators [5-16]."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _baseline/comparison_: "Prior research on heterogeneous-CIM-based Transformer accelerators aims to reduce computation amounts of DMM through algorithm co-design [8, 14, 15]."
- [2024_Cai_MemristorLSHAttention_ISCAS](2024_Cai_MemristorLSHAttention_ISCAS.md) Memristor LSH Attention (2024) — _baseline/comparison_: "Prior research on heterogeneous-CIM-based Transformer accelerators aims to reduce computation amounts of DMM through algorithm co-design [8, 14, 15]."
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024) — _baseline/comparison_: "Some studies have developed specific modules to leverage the varying sparsity, precision, and weight writing needs of operators [10, 12]."

## Cited by (in collection, 1)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../04_Transformers_and_LLMs/2025_Fu_CrossTypeMappedDataflow_ISLPED.pdf](../../04_Transformers_and_LLMs/2025_Fu_CrossTypeMappedDataflow_ISLPED.pdf)
- Full text: [../fulltext/2025_Fu_CrossTypeMappedDataflow_ISLPED.txt](../fulltext/2025_Fu_CrossTypeMappedDataflow_ISLPED.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/islped65674.2025.11261801
