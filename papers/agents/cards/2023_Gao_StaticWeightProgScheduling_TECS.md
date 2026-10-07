---
id: W4385768723
key: 2023_Gao_StaticWeightProgScheduling_TECS
title: "Static Scheduling of Weight Programming for DNN Acceleration with Resource Constrained PIM"
short: "Static Weight-Programming Scheduling"
year: 2023
venue: "TECS"
venue_full: "ACM Transactions on Embedded Computing Systems"
authors: "Xin Qin Gao, Hongyue Wang, Yiyan Chen, Yuhao Zhang, Zhaoyan Shen, Lei Ju"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet", "Transformer", "BERT"]
lm_models: ["Transformer (base)", "BERT-base", "Chinese BERT-base", "ERNIE", "RoBERTa"]
param_scale: "~100M (BERT-base/RoBERTa class)"
slm: true
evidence: algorithm+simulation
topics: ["weight-mapping", "tiling-partitioning", "scheduling", "write-verify-programming", "endurance-retention", "ir-drop-parasitics", "compiler-software-stack", "language-models"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 13
citations_overall: 3
priority_score: 6.42
doi: "https://doi.org/10.1145/3615657"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Gao_StaticWeightProgScheduling_TECS.pdf"
fulltext: "../fulltext/2023_Gao_StaticWeightProgScheduling_TECS.txt"
---

# Static Weight-Programming Scheduling

**Static Scheduling of Weight Programming for DNN Acceleration with Resource Constrained PIM** — ACM Transactions on Embedded Computing Systems (2023)

## TL;DR
Static (offline) weight-to-operation-unit mapping framework for area-constrained ReRAM PIM that cuts runtime weight-reprogramming latency via similarity-, distance- and balance-aware placement, reducing end-to-end latency by 11.99% (ImageNet CNNs), 40.29% (CIFAR-10) and 37.62% (NLP models) on average, up to 52.91%.

## Summary
Most ReRAM PIM accelerators (PRIME, ISAAC) assume all DNN weights are mapped simultaneously and that only small operation units (OUs, e.g. 16x8 or 16x16 within a 512x512 crossbar) are activated for accuracy. With realistic area-constrained capacity (16 or 32 Mb) models of tens to hundreds of MB need multiple online programming stages. The authors build a programming latency model that captures bit-wise SET/RESET asymmetry (RESET much slower), segment-wise wordline programming (4- or 8-bit segments), and driver-distance dependence (up to 70x RESET latency gap across a 512x512 array, simulated by HSPICE). An offline search produces a weight-to-OU mapping table using similarity-based (reuse bit patterns already stored), distance-aware and balanced allocation, plus an OU scheduler table that records activation order so correct MVMs run online. Weights/inputs are INT8 mapped ISAAC-style (differential via 2's complement); evaluation uses modified MNSIM 2.0 (32nm, 500 MHz, 5-bit ADC, 8 PEs per tile) on AlexNet, GoogleNet, ResNet50/101, VGG16 (ImageNet and CIFAR-10) and five NLP models. A baseline distributes blocks evenly in sequential OU order. Compatible with SRE-ORC pruning (32.75% vs 31.57% improvement).

## Language models evaluated
- Models: Transformer (base), BERT-base, Chinese BERT-base, ERNIE, RoBERTa
- Scale: ~100M (BERT-base/RoBERTa class)

## Contributions
- Observation that full-model-on-chip mapping is impractical under area constraints, so online programming latency matters
- ReRAM crossbar programming latency model (SET/RESET asymmetry, parallel crossbar variation, driver distance)
- Similarity-based, distance-aware and balanced weight-to-OU mapping with OU scheduling tables
- Evaluation on CNN and NLP models, with pruning integration, endurance analysis and overhead analysis

## Key claims (stable IDs)
- **2023_Gao_StaticWeightProgScheduling_TECS#C1** — Average overall latency reductions are 11.99% (ImageNet), 40.29% (CIFAR-10) and 37.62% (NLP) versus the baseline; up to 52.91% versus state of the art. — _support:_ relative to even-distribution baseline — _loc:_ Sec. 6.2.1, Fig. 7-9; contributions
- **2023_Gao_StaticWeightProgScheduling_TECS#C2** — Programming overhead is a larger share for FC-dominated NLP models than for convolutional ImageNet models, whose computing latency is on average 69.09% of total. — _support:_ weight-to-MAC ratio VGG16 138.36 Mb/15.5 GMAC (ImageNet) vs 0.44 GMAC (CIFAR-10) — _loc:_ Sec. 6.2.1
- **2023_Gao_StaticWeightProgScheduling_TECS#C3** — Online reprogramming has limited endurance impact: AlexNet on 32 Mb with 15 programming stages at 30 fps would last ~70 years in the worst case (endurance >1e12). — _support:_ units needing SET/RESET fall from 31.05/23.62/36.70% to 22.11/17.41/28.12% (ImageNet/CIFAR/NLP) — _loc:_ Sec. 6.4, Fig. 17
- **2023_Gao_StaticWeightProgScheduling_TECS#C4** — Mapping/scheduling tables cost 0.22-1.28 MB and 0.24-1.32 MB of storage and negligible timing overhead. — _support:_ four configurations — _loc:_ Sec. 6.5

## Results
- Overall latency reduction 11.99% ImageNet, 40.29% CIFAR-10, 37.62% NLP; average ~31.57% across all models (32.75% with SRE-ORC pruning)
- Table 1: 8-bit weights of BERT-base 104.41 MB, RoBERTa 97.57 MB, Transformer 46.89 MB, VGG16 131.94 MB (ImageNet), requiring many programming stages on 16/32 Mb ReRAM
- RESET latency 10 ns to 2 us vs SET 10 ns (HSPICE parameters); up to 70x latency gap across a 512x512 crossbar
- Fewer cells programmed: units requiring SET/RESET reduced by 8.94%, 6.21%, 8.58% of chip units for ImageNet/CIFAR-10/NLP

## Key numbers
- tech_node: 32nm (simulated PE)
- array_size: 512x512 crossbar, 16x8 / 16x16 OU
- throughput: up to 52.91% overall latency reduction
- bits_weight: 8b (1 bit per cell)
- bits_adc: 5b

## Datasets / benchmarks
ImageNet, CIFAR-10, AlexNet, GoogleNet, ResNet50/101, VGG16, Transformer, BERT-base, RoBERTa, ERNIE

## Limitations
- Behavioral simulation (MNSIM 2.0 modified) with HSPICE-derived write latencies; no hardware
- No inference accuracy evaluation for NLP models: purely latency/programming cost, with no analog noise or ADC error
- Binary SLC cells, bit-slicing across 1-bit cells; MLC only argued to be compatible
- Gains depend on weight similarity/sparsity, lower for dense NLP weights
- NLP models are base-size encoders; no decoder LLMs or KV-cache

## Remarks
Addresses the commonly idealised full-model-fits-at-once assumption, which matters directly for larger models that exceed crossbar capacity and must be time-multiplexed with reprogramming. Because ReRAM writes are slow and wear-limited, a static pattern-aware schedule is a practical idea for scaling beyond toy sizes, and its inclusion of BERT/RoBERTa makes it one of the few mapping papers touching language models, though only for latency. Absence of accuracy data limits the weight of its NLP evidence.

## Cites (in collection, 13)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Processing-in-memory (PIM) -based accelerators can perform in-situ computation and eliminate the data movement between memory and processing elements [1, 4, 8, 11, 23]."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _uses-method-or-tool_: "We modify the MNSIM2.0 [33], a behavior-based PIM simulation platform, to evaluate the performance of the proposed ReRAM-based DNN accelerators."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _motivation_: "In practice, the accumulated current deviation of ReRAM cells would severely hurt model inference accuracy [2]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Processing-in-memory (PIM) -based accelerators can perform in-situ computation and eliminate the data movement between memory and processing elements [1, 4, 8, 11, 23]."
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020) — _contrasts/critiques_: "A few recent works [16-18] consider the constrained PIM resource, and propose some scheduling schemes to improve the inference throughput of batched images."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "Processing-in-memory (PIM) -based accelerators can perform in-situ computation and eliminate the data movement between memory and processing elements [1, 4, 8, 11, 23]."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "Figure 1 shows a typical ReRAM-based accelerator for DNN model [19, 21, 38]."
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022) — _background_: "Latest ReRAM technology advances in multi-level cell (MLC) design substantially improve the ReRAM density [10]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "ISAAC [21] further proposes a pipelined PIM architecture where individual crossbars are dedicated to each DNN layer."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "PRIME [3] provides a novel micro-architecture and circuit design for the ReRAM-based DNN PIM accelerator."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _data/numbers_: "Based on the latest technology, scaling of ReRAM PIM devices [14, 35, 37], we set the area-constrained ReRAM PIM capacity to 16 Mb and 32 Mb for a small AI edge devices [7]."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Gao_StaticWeightProgScheduling_TECS.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Gao_StaticWeightProgScheduling_TECS.pdf)
- Full text: [../fulltext/2023_Gao_StaticWeightProgScheduling_TECS.txt](../fulltext/2023_Gao_StaticWeightProgScheduling_TECS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3615657
