---
id: W4313251083
key: 2022_Jain_AnalogAI2DMesh_TVLSI
title: "A Heterogeneous and Programmable Compute-In-Memory Accelerator Architecture for Analog-AI Using Dense 2-D Mesh"
short: "Analog-AI-2DMesh"
year: 2022
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2022)"
authors: "Shubham Jain, Hsinyu Tsai, Ching-Tzu Chen, R. Muralidhar, Irem Boybat, Martin M. Frank, Stanisław Woźniak, Miloš Stanisavljević, Praneet Adusumilli, Pritish Narayanan, Kohji Hosokawa, Masatoshi Ishii et al."
category: "03 Crossbar Accelerator Architectures"
devices: ["PCM"]
models: ["CNN", "LSTM/RNN", "Transformer", "BERT"]
lm_models: ["BERT"]
param_scale: ""
slm: true
evidence: simulation
topics: ["heterogeneous-analog-digital", "crossbar-architecture", "dataflow-pipelining", "transformer-accelerator", "recurrent-models", "weight-mapping"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 22
cites_in_collection: 13
citations_overall: 74
priority_score: 10.89
doi: "https://doi.org/10.1109/tvlsi.2022.3221390"
pdf: null
fulltext: null
---

# Analog-AI-2DMesh

**A Heterogeneous and Programmable Compute-In-Memory Accelerator Architecture for Analog-AI Using Dense 2-D Mesh** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IBM's heterogeneous, programmable compute-in-memory accelerator architecture combines spatially distributed analog CIM tiles for weight-stationary MAC with heterogeneous digital compute cores, connected by a dense circuit-switched 2-D mesh, and shows projected system-level performance 40x-140x more energy-efficient than an NVIDIA A100 across CNNs, LSTMs and transformers (including BERT).

## Summary
The paper presents a highly heterogeneous and programmable compute-in-memory (CIM) accelerator architecture for DNN inference that combines spatially distributed CIM memory array 'tiles' performing weight-stationary, energy-efficient MAC operations with heterogeneous special-function digital compute cores for auxiliary operations. Massively parallel activation vectors move between tiles and cores over short distances via a dense, efficient circuit-switched 2-D mesh (the 'analog fabric'), which is designed to support a wide range of DNN workloads including CNNs, LSTMs, and transformers end-to-end. The authors address both the mapping of DNNs onto this hardware and the pipelining of workloads across a range of batch sizes, and present system-level performance estimates using projected component parameters for a realistic 'analog AI' system built from dense crossbar arrays of low-power nonvolatile analog memory elements (PCM), including scaling the single analog-fabric design to larger networks by introducing inter-chip data transport across multiple analog AI chips. Performance estimates for several networks, including large LSTM and BERT, show highly competitive throughput while offering substantially higher energy efficiency than an NVIDIA A100 GPU.

## Language models evaluated
- Models: BERT
- Scale: —

## Contributions
- A heterogeneous, programmable CIM accelerator architecture combining analog CIM tiles (weight-stationary MAC) with heterogeneous digital special-function compute cores
- A dense, efficient circuit-switched 2-D mesh ('analog fabric') interconnecting tiles and cores for massively parallel activation data movement
- End-to-end support for a wide range of DNN workloads (CNNs, LSTM, transformers/BERT) on a single common hardware fabric design
- Mapping and pipelining strategies for DNN workloads across a range of batch sizes on the proposed architecture
- System-level performance projections using realistic component parameters for an analog-AI system based on dense nonvolatile-memory crossbars, including scale-out across multiple analog AI chips
- First system-level assessment (per the authors) showing analog-AI accelerators are competitive in throughput while offering large energy-efficiency gains over a modern GPU

## Key claims (stable IDs)
- **2022_Jain_AnalogAI2DMesh_TVLSI#C1** — The proposed analog-AI accelerator architecture offers highly competitive throughput for large and diverse DNN workloads, including transformers — _support:_ performance estimates reported for several networks including large LSTM and BERT, shown to be highly competitive in throughput — _loc:_ Abstract
- **2022_Jain_AnalogAI2DMesh_TVLSI#C2** — The analog-AI architecture offers dramatically higher energy efficiency than a state-of-the-art GPU — _support:_ 40x-140x higher energy efficiency than NVIDIA A100, depending on workload — _loc:_ Abstract
- **2022_Jain_AnalogAI2DMesh_TVLSI#C3** — A single common analog fabric design can scale to large networks via inter-chip data transport across multiple analog AI chips — _support:_ stated architectural capability demonstrated via system-level performance estimates — _loc:_ Abstract

## Results
- 40x-140x higher energy efficiency than NVIDIA A100 across evaluated networks (projected system-level estimates)
- Highly competitive throughput reported for CNNs, large LSTM networks, and BERT (transformer) workloads

## Limitations
- This entry is based on the abstract only (no full text or PDF was located); the exact simulation/estimation methodology, specific per-network throughput numbers, and batch-size sensitivity results are not confirmed here
- Performance figures are system-level projections using projected component parameters for a realistic analog-AI system, not measurements from a fabricated multi-tile chip
- Energy-efficiency comparison is against an NVIDIA A100 GPU baseline; comparisons to other PIM/CIM accelerator architectures are not stated in the abstract

## Remarks
This is IBM's influential heterogeneous analog-AI accelerator architecture paper (74 citations, with numerous later papers in this collection -- AnalogNAS, NORA, SAGE, CIMFlow, the ALBERT demonstration chip, and others -- explicitly building on or citing it), making it a key reference point for mapping transformer/LLM workloads onto PCM-based analog crossbar fabrics at system scale. Its central contribution for mapping research is the explicit co-design of a 2-D circuit-switched interconnect ('analog fabric') to support heterogeneous digital+analog cores and diverse workloads (CNN/LSTM/transformer) on one architecture, rather than a single-workload-specific crossbar design. Because only the abstract was available here, the specific mapping/pipelining algorithms and the precise throughput-vs-batch-size tradeoffs could not be verified and should be checked in the full text, which is recommended given the paper's centrality to this literature.

## Cites (in collection, 13)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022)

## Cited by (in collection, 22)
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _extends/builds-on_: "A highly heterogeneous and programmable accelerator architecture for analog AI has been introduced20 for which system-level performance assessments have predicted energy efficiencies 40–140 times higher than those of cutting-edge graphics processing units."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "In terms of AIMC workload execution latency and system mapping51, CNNs are already less well-suited for resistive crossbar arrays due to the uneven temporal reuse between layers and spatial underutilization of the large analog tiles by the small kernel matrices (see Table 1), although some optimization and mapping tricks52 are available."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _uses-method-or-tool_: "We conducted power performance simulations for AnalogNAS T500 and ResNet32 models using a 2D-mesh based heterogeneous analog IMC system with the simulation tool presented in [46]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _data/numbers_: "Such an architecture is projected to provide highly competitive throughput while offering 40x-140x higher energy efficiency than an NVIDIA A100 GPU14 ."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _data/numbers_: "Figure/table adaptation note: performance comparison chart adapted with permission, citing the 'Analog-AI Using Dense 2-D Mesh' architecture alongside DaDianNao and 3D-aCortex in the throughput/process-node comparison."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _data/numbers_: "For approximate numbers, we assume that a single update pulse would take approximately 5 ns, a single MVM about 40 ns39, and that the memory operations can be hidden behind the compute40."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _uses-method-or-tool_: "Hence, for transformer models, the self-attention is deployed on digital tiles or digital cores [9], [18], [20]."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _extends/builds-on_: "Combining insights from the 14nm hardware, we proposed a heterogeneous, programmable, and scalable system architecture with on-chip auxiliary operation support for CNN, LSTM, and Transformer [19]."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "Previous CIM-based accelerator proposals have recognised the importance of cross-layer inference [4, 15, 31]."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _background_: "In a more advanced design where digital compute units are distributed on-chip amongst the tiles, fine-grained pipelining within each layer can be expected to keep all resources continuously busy, leading to significant improvements in both energy-efficiency and throughput36."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _background_: "Due to the non-ideal effects of RRAM ACIM and the low-density of SRAM DCIM, a heterogeneous architecture has been adopted in prior research on CIM-based Transformer accelerators [5-16]."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _extends/builds-on_: "We recently introduced a highly programmable Analog-AI and Compute-In-Memory accelerator architecture [16], which utilizes a highly specialized set of Compute-cores and Tiles arranged within a common building block known as an Analog Fabric (AF) (Fig. 2), together with SRAM scratchpads, IO blocks, and a 2D Mesh on top of the building blocks."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _extends/builds-on_: "We recently introduced a highly programmable Analog-AI and Compute-In-Memory accelerator architecture [18], which utilizes a highly specialized set of Compute-cores and Tiles arranged within a common building block known as an Analog Fabric (AF) (Fig. 4), together with SRAM scratchpads, IO blocks, and a 2D Mesh on top of the building blocks."
- [2025_Malhotra_ReTern_TVLSI](2025_Malhotra_ReTern_TVLSI.md) ReTern (2025) — _extends/builds-on_: "Thus, works like [33] utilize digital compute cores for the self-attention layers, while using CiM-based memory arrays for the feedforward layers."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "The result is then send to either another AIMC core, a Digital Processing Unit (DPU), or a RISC-V in a heterogeneous multi-core architecture [41, 42]."
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023)
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025)
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024)
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: not available locally (save as `papers/03_Crossbar_Accelerator_Architectures/2022_Jain_AnalogAI2DMesh_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2022.3221390
