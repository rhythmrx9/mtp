---
id: W4379116135
key: 2023_Bruschi_AIMCResNet18Manycore_DATE
title: "End-to-End DNN Inference on a Massively Parallel Analog In Memory Computing Architecture"
short: "AIMC-ResNet18-Manycore"
year: 2023
venue: "DATE"
venue_full: "Design, Automation & Test in Europe Conference (DATE 2023)"
authors: "Nazareno Bruschi, Giuseppe Tagliavini, Angelo Garofalo, Francesco Conti, Irem Boybat, Luca Benini, Davide Rossi"
category: "05 Mapping, Compilation & Dataflow"
devices: ["PCM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["dataflow-pipelining", "tiling-partitioning", "weight-mapping", "heterogeneous-analog-digital", "crossbar-architecture", "scheduling", "energy-efficiency", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 5
priority_score: 4.54
doi: "https://doi.org/10.23919/date56975.2023.10137208"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Bruschi_AIMCResNet18Manycore_DATE.pdf"
fulltext: "../fulltext/2023_Bruschi_AIMCResNet18Manycore_DATE.txt"
---

# AIMC-ResNet18-Manycore

**End-to-End DNN Inference on a Massively Parallel Analog In Memory Computing Architecture** — Design, Automation & Test in Europe Conference (DATE 2023) (2023)

## TL;DR
A 512-cluster RISC-V (PULP) + PCM AIMC many-core is simulated running end-to-end ResNet-18 (batch 16, 256x256 images) at up to 20.2 TOPS, 6.5 TOPS/W and 42 GOPS/mm2 on a 480 mm2 design, using static multi-cluster mapping, data replication and optimized residual buffering.

## Summary
The paper targets the gap between prototype AIMC cores (limited array size ~256x256 usable, slow writes demanding static weight mapping) and end-to-end inference of non-trivial CNNs with residual connections. The architecture is a hierarchical many-core: each cluster has 16 RISC-V cores, 1 MB multi-banked L1 and an nvAIMC accelerator (IMA) with a 256x256 PCM crossbar, DACs/ADCs and streamers; clusters are grouped into quadrants with L2/L3 interconnect and an HBM. An MVM is assumed 130 ns (HERMES core). The DNN is statically mapped across clusters: layers larger than the IMA (256 rows/cols) are split across clusters with digital reduction, layers are pipelined as a systolic dataflow, bottleneck layers are replicated, and residual tensors are buffered on-chip (2 MB) rather than in HBM. An extended open-source system-level simulator calibrated against cycle-accurate RTL/FPGA (>90% accuracy) gives performance. Results are decomposed into global-mapping, local-mapping and pipeline-imbalance inefficiencies.

## Contributions
- End-to-end ResNet-18 inference (with residual layers) on a 512-cluster heterogeneous AIMC+RISC-V architecture
- Mapping strategy: pipelined multi-cluster splitting, data replication and optimized residual management
- Performance and inefficiency analysis (global, local, pipeline imbalance) with guidelines for next-generation AIMC many-cores
- Open-source hardware/software

## Key claims (stable IDs)
- **2023_Bruschi_AIMCResNet18Manycore_DATE#C1** — Architecture delivers 20.2 TOPS (3303 images/s), 42 GOPS/mm2 and 6.5 TOPS/W on ResNet-18 (batch 16, 256x256) — _support:_ 9.2 ms and 15 mJ per inference as reported in results; 4.8 ms quoted in intro — _loc:_ Sec. VI / Conclusion
- **2023_Bruschi_AIMCResNet18Manycore_DATE#C2** — Data replication and parallelization improve performance 1.6x at the cost of 61 more clusters; optimized residual mapping adds another 1.9x for 2 more clusters — _support:_ Fig. 5B-D — _loc:_ Sec. VI / Fig. 5
- **2023_Bruschi_AIMCResNet18Manycore_DATE#C3** — Only 322 of 512 clusters are used for mapping parameters — _support:_ global-mapping inefficiency — _loc:_ Sec. VI
- **2023_Bruschi_AIMCResNet18Manycore_DATE#C4** — Peak area efficiency 600 GOPS/mm2 on layer 12 (10 clusters, replication 2); deep strided layers drop to 50 GOPS/mm2 — _support:_ Fig. 7 — _loc:_ Sec. VI

## Results
- 20.2 TOPS, 6.5 TOPS/W, 42 GOPS/mm2 on a 480 mm2 architecture
- Naive mapping vs data-replicated: 1.6x; vs optimized residual mapping: additional 1.9x
- Residuals need 1.6 MB to store simultaneously; 1 MB L1 per cluster, 2 MB used for optimized residual buffering
- Pipeline unbalance: first layers have high IFM reuse, deep layers (group 5, layers 20, 21, 23, 24 on 40 clusters each) have analog latency <0.2 ms

## Key numbers
- array_size: 256x256 IMA, 512 clusters
- energy_eff: 6.5 TOPS/W
- throughput: 20.2 TOPS; 3303 images/s
- bits_weight: 8b equivalent

## Datasets / benchmarks
ResNet-18 (256x256 images)

## Limitations
- Simulation (calibrated to RTL/FPGA), no silicon of the full system
- Analog accuracy/noise not modeled; assumes ideal 256x256 PCM IMA with 130 ns MVM
- Large area (480 mm2) with 160 of 512 clusters unused for weights
- Only a ResNet-18 CNN; transformers, attention and LM weights not addressed
- Inconsistent latency figures between abstract-level text (4.8 ms) and results (9.2 ms)

## Remarks
Concrete evidence that full-network mapping onto many small nvAIMC arrays is dominated by data movement, pipeline balance and residual buffering rather than MVM time. Static weight mapping is a hard constraint for PCM, which for LMs means the whole model must fit on chip -- the same constraint appears in later LM-on-AIMC studies. Complements IBM's measured chips (HERMES, speech chip) with a system-level view.

## Cites (in collection, 8)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _background_: "For this reason, few recent works [8–10] proposed the integration of nvAIMC cores into digital System-on-Chips (SoC), exploiting a mix of nvAIMC cores and more flexible specialized and programmable digital processors."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "Shafiee et al. [12] and Ankit et al. [13] target VGG-like networks featuring no residual layers, nicely fitting mapping on pipelined data-flow architectures."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "In recent years, Analog InMemory Computing (AIMC) has been a widely studied computing paradigm since it promises outstanding performance and energy efficiency on MVM operations [1]."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _motivation_: "Moreover, a further challenge is the fabricable size of nvIMC devices, which de-facto is limited to 1024×1024 with up to 8-bit equivalent memory cells [4]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _data/numbers_: "In this work, we assume an MVM to be executed in 130 ns as reported in Khaddam et al. [7]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "For example, Dazzi et al. [11] targeted a relatively small ResNet-like network targeting the CIFAR10 dataset, while Shafiee et al. [12] and Ankit et al. [13] target VGG-like networks featuring no residual layers, nicely fitting mapping on pipelined data-flow architectures."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _extends/builds-on_: "Each cluster also includes a nvAIMC Accelerator (IMA) sharing the same multi-banked memory as the CORES for efficient communication, similarly to the architecture presented in Garofalo et al. [9]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Bruschi_AIMCResNet18Manycore_DATE.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Bruschi_AIMCResNet18Manycore_DATE.pdf)
- Full text: [../fulltext/2023_Bruschi_AIMCResNet18Manycore_DATE.txt](../fulltext/2023_Bruschi_AIMCResNet18Manycore_DATE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.23919/date56975.2023.10137208
