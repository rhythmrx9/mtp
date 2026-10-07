---
id: W3036663566
key: 2020_Lu_CIMAreaConstraintBenchmark_TVLSI
title: "Benchmark of the Compute-in-Memory-Based DNN Accelerator With Area Constraint"
short: "CIM Area-Constraint Benchmark"
year: 2020
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2020"
authors: "Anni Lu, Xiaochen Peng, Yandong Luo, Shimeng Yu"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-analog", "FeFET"]
models: ["ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["benchmarking", "energy-efficiency", "macro", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 8
citations_overall: 22
priority_score: 4.88
doi: "https://doi.org/10.1109/tvlsi.2020.3001526"
pdf: null
fulltext: null
---

# CIM Area-Constraint Benchmark

**Benchmark of the Compute-in-Memory-Based DNN Accelerator With Area Constraint** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2020 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
This benchmarking study designs and evaluates compute-in-memory DNN accelerators under realistic chip-area constraints (rather than assuming all weights fit on-chip), comparing two weight-reload dataflows and SRAM vs. FeFET device technologies for ResNet-18/ImageNet inference.

## Summary
Most prior compute-in-memory (CIM) DNN accelerator work assumes a full-custom design where all weights are stored on-chip, an assumption that breaks down for lightweight, area-constrained edge devices. This paper designs and benchmarks CIM-based DNN accelerators under different chip area constraints, where only part of the weight set can reside on-chip at a time. It investigates a scheduling strategy and dataflow for DNN inference under this constraint, comparing two weight-reload schemes: (1) reloading partial weights while reusing on-chip input/output feature maps, and (2) loading a batch of inputs and reusing the on-chip partial weights across that batch. A system-level performance benchmark is then run for ResNet-18 inference on ImageNet, comparing design tradeoffs across area constraints, dataflow choice, and device technology (SRAM vs. ferroelectric FET, FeFET).

## Contributions
- A scheduling/dataflow framework for CIM DNN accelerators operating under chip area constraints where not all weights fit on-chip simultaneously
- Two weight-reload schemes evaluated: reload-partial-weights-reuse-activations vs. reload-batch-of-inputs-reuse-partial-weights
- A system-level benchmark of ResNet-18/ImageNet inference performance across different area constraints, dataflows, and device technologies (SRAM vs. FeFET)

## Key claims (stable IDs)
- **2020_Lu_CIMAreaConstraintBenchmark_TVLSI#C1** — CIM accelerator performance under area constraints depends significantly on the choice of weight-reload dataflow — _support:_ Two distinct reload schemes are compared and lead to different design tradeoffs (abstract) — _loc:_ Abstract
- **2020_Lu_CIMAreaConstraintBenchmark_TVLSI#C2** — Device technology choice (SRAM vs. FeFET) materially affects area-constrained CIM accelerator design tradeoffs — _support:_ Abstract explicitly frames device technology (SRAM vs. FeFET) as a benchmarked design axis — _loc:_ Abstract

## Results
- System-level performance benchmarking was performed specifically for ResNet-18 inference on ImageNet under varying area constraints, dataflows, and device technologies (per abstract); specific throughput/energy numbers are not stated in the abstract and could not be verified without full text

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Xplore is not downloadable here); quantitative results, exact area-constraint values, and specific performance/energy numbers could not be extracted or verified
- Evaluation appears limited to a single network (ResNet-18) and dataset (ImageNet) based on the abstract

## Remarks
Based on the abstract, this paper fills a practically important gap in the CIM accelerator literature by relaxing the common (and often unrealistic for edge devices) assumption that all weights fit on-chip, and by directly comparing SRAM and FeFET as the on-chip analog storage technology under area constraints. Without full-text access the specific quantitative tradeoffs (e.g., throughput/energy vs. area curves) cannot be reported here; a thesis reader interested in realistic edge-deployment constraints for compute-in-memory accelerators should treat this as a relevant benchmarking reference to follow up on directly.

## Cites (in collection, 8)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 2)
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _contrasts/critiques_: "A few recent works [16-18] consider the constrained PIM resource, and propose some scheduling schemes to improve the inference throughput of batched images."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2020_Lu_CIMAreaConstraintBenchmark_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2020.3001526
