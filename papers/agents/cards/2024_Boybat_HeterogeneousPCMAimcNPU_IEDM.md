---
id: W4407720907
key: 2024_Boybat_HeterogeneousPCMAimcNPU_IEDM
title: "Heterogeneous Embedded Neural Processing Units Utilizing PCM-Based Analog In-Memory Computing"
short: "Heterogeneous PCM-AIMC NPU"
year: 2024
venue: "IEDM"
venue_full: "2024 IEEE International Electron Devices Meeting (IEDM)"
authors: "Irem Boybat, Thomas Boesch, Mario Allegra, M. Baldo, J.J. Bertolini-Agnoletto, Geoffrey W. Burr, Alessandro Buschini, Alessandro Cabrini, Emanuela Calvetti, Carmine Cappetta, Francesco Conti, Elena Ferro et al."
category: "03 Crossbar Accelerator Architectures"
devices: ["PCM"]
models: ["Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["heterogeneous-analog-digital", "edge-ai", "transformer-accelerator", "analog-mvm", "crossbar-architecture"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 4
citations_overall: 15
priority_score: 7.37
doi: "https://doi.org/10.1109/iedm50854.2024.10873479"
pdf: null
fulltext: null
---

# Heterogeneous PCM-AIMC NPU

**Heterogeneous Embedded Neural Processing Units Utilizing PCM-Based Analog In-Memory Computing** — 2024 IEEE International Electron Devices Meeting (IEDM) (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IBM and STMicroelectronics propose a heterogeneous embedded NPU architecture for edge AI that pairs PCM-based AIMC tiles (for matrix-vector multiplication) with digital accelerator nodes and a programmable software cluster, projecting transformer inference throughput competitive with high-end mobile SoCs built on more advanced nodes.

## Summary
The paper targets edge AI inference, where energy, area, and cost budgets are much tighter than in datacenter accelerators. It proposes a heterogeneous embedded Neural Processing Unit (NPU) that combines multiple digital and analog accelerator nodes to cover diverse operation types and precision requirements within one SoC. The key analog component is a set of Analog In-Memory Computing (AIMC) tiles based on Phase-Change Memory (PCM), used to execute matrix-vector multiplications with high energy efficiency and substantial non-volatile on-chip weight storage, avoiding the need to stream weights from off-chip DRAM. A digital data path and a programmable software cluster coordinate end-to-end inference across layers/operations that require different numeric precision (e.g., attention/softmax, normalization) that are not well suited to the analog tiles. The authors project that this heterogeneous PCM-AIMC/digital NPU can deliver throughput for transformer-based neural networks that is competitive with high-end mobile SoCs fabricated at more advanced technology nodes, despite relying on an older/cheaper process enabled by PCM's density and efficiency advantage.

## Contributions
- Proposes a heterogeneous embedded NPU architecture mixing digital accelerator nodes and PCM-based AIMC tiles within a single edge-AI SoC
- Uses PCM AIMC tiles specifically for matrix-vector multiplication to combine high energy efficiency with large non-volatile on-chip weight capacity
- Adds a digital data path and programmable software cluster to support end-to-end inference across multiple precision levels and non-MVM operations
- Targets transformer neural network workloads at the edge, projecting throughput competitive with higher-end mobile SoCs on more advanced technology nodes

## Key claims (stable IDs)
- **2024_Boybat_HeterogeneousPCMAimcNPU_IEDM#C1** — A heterogeneous PCM-AIMC + digital NPU can match the transformer inference throughput of high-end mobile SoCs built on more advanced process nodes — _support:_ The NPU is projected to deliver competitive throughput for transformer neural networks rivaling high-end mobile/edge SoCs fabricated at more advanced technology nodes (stated in the abstract; no full-text numeric figures available from this access) — _loc:_ Abstract

## Limitations
- Analysis based on abstract only; no full text was accessible (not found via arXiv or other legitimate open-access sources), so specific throughput/energy numbers, benchmark details, and comparison baselines could not be verified
- Claims described as 'projected'/architectural rather than confirmed as measured silicon results in the available abstract

## Remarks
This IEDM 2024 paper (IBM/STMicroelectronics-affiliated authorship consistent with the IBM PCM-AIMC line of work, e.g. HERMES chip) is a device-to-system architecture proposal pairing non-volatile PCM crossbars with digital compute for edge transformer inference; without full text, the specific throughput/efficiency numbers and the degree of silicon validation versus projection cannot be confirmed, so this entry should be revisited if the full paper becomes accessible.

## Cites (in collection, 4)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023)
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023)

## Cited by (in collection, 6)
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _background_: "A similar analog fabric was designed for edge Transformer applications [22], hosting 33 million PCM weights on a 30mm2 chip."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Consequently, NVM-based AIMC accelerators are predominantly investigated within the context of weight-stationary models that could meet the requirements of edge devices19 and large language model inference20."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "Analog In-Memory Computing (AIMC) has emerged as a promising computing paradigm to tackle these challenges, offering improved performance and energy-efficiency through computation directly within the memory array4,5."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _background_: "Similar to any other analog NVMs [19-21], PCM has its intrinsic nonidealities, such as read noise [12, 22, 23], device-to-device variations [24], conductance drift over time after programing [13, 25, 26], limited memory window [17, 27], which can adversely affect DNN inference accuracy."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _background_: "Furthermore, by performing affine-scale and digital aggregation operations at the edge of the Tile, the number of post-integration data-transport steps involving the 2D data-transport mesh can be significantly reduced [34]."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)

## Files
- PDF: not available locally (save as `papers/03_Crossbar_Accelerator_Architectures/2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iedm50854.2024.10873479
