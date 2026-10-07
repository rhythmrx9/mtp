---
id: W4388210331
key: 2023_Li_CrossbarAllocationOpt_TODAES
title: "Mathematical Framework for Optimizing Crossbar Allocation for ReRAM-based CNN Accelerators"
short: "Crossbar Allocation Framework"
year: 2023
venue: "TODAES"
venue_full: "ACM Transactions on Design Automation of Electronic Systems (2023)"
authors: "Wanqian Li, Yinhe Han, Xiaoming Chen"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["weight-mapping", "tiling-partitioning", "dataflow-pipelining", "scheduling", "crossbar-architecture", "cnn-accelerator", "simulator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 9
citations_overall: 2
priority_score: 5.24
doi: "https://doi.org/10.1145/3631523"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Li_CrossbarAllocationOpt_TODAES.pdf"
fulltext: "../fulltext/2023_Li_CrossbarAllocationOpt_TODAES.txt"
---

# Crossbar Allocation Framework

**Mathematical Framework for Optimizing Crossbar Allocation for ReRAM-based CNN Accelerators** — ACM Transactions on Design Automation of Electronic Systems (2023) (2023)

## TL;DR
Mathematical framework plus dynamic-programming solver that picks per-layer crossbar duplication counts for ReRAM CNN accelerators under crossbar and bandwidth constraints, achieving 98% model accuracy against cycle-level simulation, near-optimal inference time, and 6.6x/13.2x lower inference time than ISAAC's heuristic (without/with bandwidth constraints).

## Summary
ReRAM CNN accelerators hold all layer weights stationary, so all layers can be pipelined and layers can be sped up by duplicating weights over more crossbars; prior work (PRIME, ISAAC, PipeLayer, mixed-size crossbar mapping) chooses duplication heuristically. The paper models CNN layers via a fused-layer parameter model (Ci, Co, Wo, Ho, Kc, stride, pooling), maps each layer to a crossbar set (Kc*Kc*Ci x Co weights split into MxN crossbars with partial-sum accumulation), and builds an abstract multi-level pipelined execution model whose inference time is a function of the per-layer duplication vector R. Bandwidth (on-chip buffer and inter-bus) enters as a constraint. A dynamic-programming solver finds R minimising inference time given total crossbars. Validation uses a cycle-level behavioral simulator checked against MNSIM (9.92% average difference without duplication) on AlexNet, VGG-A/E, ResNet-18 and MobileNet-v1, and an ISAAC-like architecture (128x128 crossbars, 72 per tile, 8-bit ADC, 1-bit DAC, 16-bit inputs/weights). Purely performance-level; no accuracy or noise analysis.

## Contributions
- Formulation of crossbar allocation as constrained optimization with bandwidth constraints
- Abstract, architecture-independent multi-level pipeline performance model (about 98% accuracy vs cycle-level simulation)
- Dynamic-programming solver giving near-optimal allocations without exhaustive search
- Analysis showing optimal duplication is ~proportional to Wo*Ho only without bandwidth limits

## Key claims (stable IDs)
- **2023_Li_CrossbarAllocationOpt_TODAES#C1** — The inference-time model is accurate to about 98% on average versus cycle-level simulation. — _support:_ model vs simulator on 5 CNNs — _loc:_ Sec. 4.1; Introduction contributions
- **2023_Li_CrossbarAllocationOpt_TODAES#C2** — Solutions are within 0.43% of optimum/quasi-optimum steps without bandwidth, and reach 94% of optimal performance with bandwidth constraints. — _support:_ vs exhaustive or 1e8 random searches with pruning — _loc:_ Sec. 4.2, Fig. 6
- **2023_Li_CrossbarAllocationOpt_TODAES#C3** — The method improves inference time over ISAAC's Sc^2-based duplication by 6.6x (no bandwidth) and 13.2x (with bandwidth). — _support:_ ISAAC-like config, 72 128x128 crossbars per tile, varying tiles — _loc:_ Sec. 4.4, Fig. 8
- **2023_Li_CrossbarAllocationOpt_TODAES#C4** — Under scarce crossbars ISAAC performance degrades faster than resources: 0.125x crossbars gives 0.07x performance on VGG-A. — _support:_ text in introduction — _loc:_ Sec. 1

## Results
- Optimal duplication R roughly proportional to Wo*Ho when bandwidth is not limiting; with bandwidth limits it balances computation and communication (Table 6, Fig. 9)
- Bandwidth stops being the bottleneck at >=2x the baseline 128 GB/s on-chip buffer and 12.8 GB/s inter-bus bandwidth (VGG-A, 2304 crossbars)
- Solver runtime from 11 s (AlexNet, 2048 crossbars) to ~4 h (MobileNet-v1, 4096 crossbars); exhaustive search estimated >1e10 years for the largest case
- Beats Wo*Ho-proportional (PipeLayer), Sc^2 (ISAAC) and identical duplication (PRIME-like) heuristics (Fig. 7)

## Key numbers
- array_size: 128x128 and 256x256 crossbars
- throughput: 6.6x / 13.2x lower inference time vs ISAAC allocation
- bits_weight: 16b (ISAAC-like)
- bits_adc: 8b

## Datasets / benchmarks
AlexNet, VGG-A, VGG-E, ResNet-18, MobileNet-v1

## Limitations
- CNNs only; no transformers or language models
- Performance model only: no accuracy, noise, ADC precision or energy modelling
- Ground truth is the authors' own behavior-level simulator (9.92% from MNSIM), not hardware
- Solver relies on approximate modelling of no-op count, causing small suboptimality
- Assumes weights fully stationary and all layers mapped simultaneously

## Remarks
Targets an under-addressed problem: most crossbar architectures treat per-layer duplication heuristically, while this gives a principled formulation with a tractable DP solver and explicit bandwidth cost, often the real bottleneck once compute is parallelised. It is performance-only, so conclusions about transformers (where dynamic attention matmuls cannot be duplicated this way) would require extension. Related heuristics in ISAAC, PRIME, PipeLayer and mixed-size mapping are the direct baselines.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _contrasts/critiques_: "PipeLayer [28] presents the results of crossbar duplication ratios but how to determine them is completely not mentioned."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _contrasts/critiques_: "Ref. [35] optimizes the resource allocation for different sized crossbars to boost the resource utilization. The solution is heuristically derived and not guaranteed to be optimal."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "ISAAC [25] allocates crossbars heuristically, according to the stride sizes of convolutional (Conv) layers."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "PRIME [7] duplicates the crossbars twice to hide data access latency with a ping-pong mode. The strategy is rough and cannot fully utilize the resources."

## Cited by (in collection, 1)
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "For accelerating DNNs on PIM, there is a crucial strategy called weight replication [5], [7], [24]."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Li_CrossbarAllocationOpt_TODAES.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Li_CrossbarAllocationOpt_TODAES.pdf)
- Full text: [../fulltext/2023_Li_CrossbarAllocationOpt_TODAES.txt](../fulltext/2023_Li_CrossbarAllocationOpt_TODAES.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3631523
