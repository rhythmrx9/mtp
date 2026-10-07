---
id: W4404294109
key: 2024_Sun_PIMCOMP_TCAD
title: "PIMCOMP: An End-to-End DNN Compiler for Processing-In-Memory Accelerators"
short: "PIMCOMP (TCAD)"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)"
authors: "Xiaotian Sun, Xinyu Wang, Wanqian Li, Yinhe Han, Xiaoming Chen"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM", "Generic-NVM"]
models: ["CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["compiler-software-stack", "weight-mapping", "tiling-partitioning", "dataflow-pipelining", "scheduling", "crossbar-architecture", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 13
citations_overall: 6
priority_score: 6.89
doi: "https://doi.org/10.1109/tcad.2024.3496847"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2024_Sun_PIMCOMP_TCAD.pdf"
fulltext: "../fulltext/2024_Sun_PIMCOMP_TCAD.txt"
---

# PIMCOMP (TCAD)

**PIMCOMP: An End-to-End DNN Compiler for Processing-In-Memory Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024) (2024)

## TL;DR
PIMCOMP is an end-to-end DNN compiler for crossbar PIM accelerators using an abstract hardware template with pseudo-instructions, genetic-algorithm weight-layout/replication optimisation and two pipeline schedulers (high-throughput and low-latency), giving up to 274.4x throughput (HT, vs SongC) and 21.8x/9.8x/5.4x lower latency (LL, vs SongC/PUMA/Polyhedral).

## Summary
Manual deployment of DNNs onto thousand-crossbar PIM accelerators is impractical across diverse micro-architectures, so the paper extends the authors' earlier PIMCOMP conference framework into a full compiler (frontend, optimizer, backend, profiler). Hardware is abstracted as a configurable template (chip/core/crossbar array, vector functional unit, local/global memory, NoC) plus a set of pseudo-instructions and user-specified execution patterns. Layer partitioning treats an 'array group' as the basic programming unit and uses a flexible unfolding format (e.g. (IK^2,O,1) vs (I,O,K^2)) to reshape convolutions onto crossbars; high-precision and signed weights use multiple arrays. Layout-computation mapping uses a genetic algorithm to jointly choose weight replication and layout, then adaptively assigns computation tasks (weight-layout guided computation-storage-mapping). Dataflow scheduling provides a High-Throughput mode (sample-granularity pipelining, batch 128) and a Low-Latency mode (inter-layer pipelining at convolution-operator/pixel granularity, batch 1, with heuristic centralized communication). The evaluation is by simulation (profiler plus CACTI/Orion, scaled to 32 nm) on vgg8, resnet18 (MNIST), resnet34 and googlenet (ImageNet), 16-bit fixed weights, on three architectures (Arch-A ISAAC-like 128x128 2b, Arch-B PUMA-like, Arch-C 512x1024), comparing against SongC, PUMA and Polyhedral re-implemented in the same framework.

## Contributions
- End-to-end DNN compiler (frontend, optimizer, backend, profiler) with two pipelines for HT and LL scenarios
- Configurable PIM accelerator abstraction with hardware template, pseudo-instructions and execution patterns
- Three-stage optimisation: array-group layer partitioning with flexible unfolding, GA-based weight-layout guided computation-storage mapping, dataflow scheduling for both pipelines
- Evaluation on three PIM architectures against three baseline compilation methods implemented faithfully in one framework

## Key claims (stable IDs)
- **2024_Sun_PIMCOMP_TCAD#C1** — In HT mode PIMCOMP reaches up to 274.4x throughput over SongC and on average 3.3x over Polyhedral — _support:_ PIMCOMP 149.5x vs Polyhedral 44.7x average over SongC; 38.8% higher average resource utilization than Polyhedral — _loc:_ Sec. VIII-B1, Fig. 10
- **2024_Sun_PIMCOMP_TCAD#C2** — In LL mode PIMCOMP lowers inference latency 21.8x, 9.8x and 5.4x vs SongC, PUMA and Polyhedral — _support:_ batch size 1; energy savings 5.6x, 2.0x, 2.3x — _loc:_ Sec. VIII-B2, Figs. 12-13
- **2024_Sun_PIMCOMP_TCAD#C3** — Energy saving in HT mode comes mainly from reduced leakage; average 9.0x and 7.7x vs SongC on Arch-A and Arch-B but only 3.9x on Arch-C — _support:_ Arch-C has fewer cores (lower leakage) and larger arrays (higher dynamic power) — _loc:_ Sec. VIII-B1, Fig. 11
- **2024_Sun_PIMCOMP_TCAD#C4** — Compilation time is dominated by the GA mapping stage, taking about 400-2200 s per model — _support:_ e.g. googlenet HT 2178.6 s total, mapping 2170.4 s — _loc:_ Table VI

## Results
- HT throughput: up to 274.4x vs SongC; 3.3x average vs Polyhedral (Fig. 10)
- LL latency: 21.8x / 9.8x / 5.4x vs SongC / PUMA / Polyhedral at batch 1 (Fig. 12)
- LL energy: 5.6x / 2.0x / 2.3x lower vs SongC / PUMA / Polyhedral (Fig. 13)
- Flexible unfolding format and layer grouping reduce global memory access and first-batch latency (Figs. 14-15, up to ~6.4x in the plotted ablations)
- Compilation time ~415-2179 s per network, mostly GA mapping (Table VI)

## Key numbers
- tech_node: 32nm (power scaled)
- array_size: 128x128 (Arch-A/B), 512x1024 (Arch-C)
- energy_eff: 5.6x LL energy savings vs SongC
- throughput: up to 274.4x vs SongC (HT)
- bits_weight: 16-bit fixed (2-bit cells)

## Datasets / benchmarks
MNIST (vgg8, resnet18), ImageNet (resnet34, googlenet)

## Limitations
- Simulation only (behavioral profiler, CACTI/Orion power scaled to 32 nm); no silicon or real compiler-to-chip flow
- Workloads are CNNs (vgg8, resnet18/34, googlenet); no Transformer/LLM support or analysis of dynamic matrices (attention)
- Assumes enough crossbars to hold the entire model so weight rewriting is avoided (chip count of Arch-C expanded to 16)
- Ignores analog non-idealities and accuracy; 16-bit fixed-point weights
- Baselines are re-implemented, not the original tools

## Remarks
A solid compiler contribution on the mapping/dataflow side of crossbar PIM; implementing three prior approaches inside the same framework makes comparisons fairer than quoting reported numbers. It is orthogonal to device/circuit work and CNN-only, so applying it to transformer or LM workloads (large static weights plus dynamic attention) is untested. The weight-replication/layout interplay it formalises is a useful reference for tiling large LM matrices onto many crossbars.

## Cites (in collection, 13)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "For accelerating DNNs on PIM, there is a crucial strategy called weight replication [5], [7], [24]."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _background_: "By configuring different array sizes for different cores, a mixed-size deployment can be realized [29]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _baseline/comparison_: "For the comparison of compilation methods, we select SongC [18], PUMA [22], and Polyhedral [16] as baselines, whose characteristics are elaborated in Section II."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _motivation_: "Therefore, a compiler that can adapt to various PIM architectures and automatically complete DNN model deployment is indispensable to improve the usability of PIM accelerators, which also helps build a PIM ecosystem [11]."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _contrasts/critiques_: "TC-CIM [19], TDO-CIM [20], CINM [23], OCC [21], Polyhedral [16], Co-Design [17], and PUMA [22] do not consider the interaction between weight replication and weight layout, and simply map computational tasks to PIM arrays."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _baseline/comparison_: "TC-CIM [19], TDO-CIM [20], CINM [23], OCC [21], Polyhedral [16], Co-Design [17], and PUMA [22] do not consider the interaction between weight replication and weight layout, and simply map computational tasks to PIM arrays."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _motivation_: "Due to the different micro-architectures of various accelerators, it is uneconomical and unrealistic to manually design the deployment schemes for each DNN model on each accelerator as in previous works [5–10]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Similarly, a signed weight may need two crossbar arrays to store the positive and negative parts separately [6]."
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023) — _background_: "Due to the limited precision of crossbar array cells, high-precision weights usually need multiple crossbar arrays to store collaboratively [27]."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _extends/builds-on_: "A previous version of this work was published in [12], which provides an optimization scheme for resource allocation, task mapping, and pipeline dataflow through four stages: layer partitioning, weight replication, core mapping, and dataflow scheduling."
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023) — _background_: "Furthermore, a reconfigurable architecture is introduced in [32] to support different unfolding strategies."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _background_: "For accelerating DNNs on PIM, there is a crucial strategy called weight replication [5], [7], [24]."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _background_: "To reuse input data and reduce loading overhead, (I, O, K 2 ) is adopted in [30], requiring further accumulation of results from K 2 parallel weight matrices to obtain the complete result."

## Cited by (in collection, 3)
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2024_Sun_PIMCOMP_TCAD.pdf](../../05_Mapping_Compilation_and_Dataflow/2024_Sun_PIMCOMP_TCAD.pdf)
- Full text: [../fulltext/2024_Sun_PIMCOMP_TCAD.txt](../fulltext/2024_Sun_PIMCOMP_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2024.3496847
