---
id: W4285263226
key: 2022_Yang_AERO_JETCAS
title: "AERO: Design Space Exploration Framework for Resource-Constrained CNN Mapping on Tile-Based Accelerators"
short: "AERO"
year: 2022
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), 2022"
authors: "Simei Yang, Debjyoti Bhattacharjee, Vinay Kumar, S. Chatterjee, Sayandip De, Peter Debacker, Diederik Verkest, Arindam Mallik, Francky Catthoor"
category: "05 Mapping, Compilation & Dataflow"
devices: ["SRAM-analog", "Generic-NVM"]
models: ["MLP", "CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "tiling-partitioning", "dataflow-pipelining", "scheduling", "crossbar-architecture", "energy-efficiency", "heterogeneous-analog-digital", "simulator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 4
citations_overall: 11
priority_score: 7.08
doi: "https://doi.org/10.1109/jetcas.2022.3171826"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2022_Yang_AERO_JETCAS.pdf"
fulltext: "../fulltext/2022_Yang_AERO_JETCAS.txt"
---

# AERO

**AERO: Design Space Exploration Framework for Resource-Constrained CNN Mapping on Tile-Based Accelerators** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (JETCAS), 2022 (2022)

## TL;DR
AERO is a design-space-exploration framework for hierarchical (accelerator/cluster/tile-PE/AIMC) CNN mapping on hybrid digital-analog multi-layer-parallel accelerators under sufficient and limited resources; weight-stationary mapping is 1.57-3.2x more power efficient than weight-loading for CNNs and ~100x for an MLP.

## Summary
Hybrid tile-based accelerators integrate AIMC arrays with digital PEs for multi-layer pipelined CNN execution, but prior DSE assumed enough tiles to hold all weights and ignored weight loading and instruction memory. AERO provides a general mapping flow: virtual mapping (node fusion/splitting, loop-level choices) then physical mapping on a hierarchy of cluster, tile, PE and AIMC array, formulated with binary placement variables over clusters x tiles. A detailed PPA model (22nm GF22FDX, Genus-synthesized digital data) covers AIMC, DAC/ADC, digital function units, buffers, NoC, instruction memory and weight loading (WL). A TANIA-like template with 4 clusters and 1152x512 AIMC arrays (103.6 mm2; AIMC 46.6% area) is the baseline within a 200 mm2 budget. Case studies on MLP-3, LeNet-5 and ResNet-18/34/50/101 compare WL vs weight-stationary (WS) mode, sufficient vs limited resources, external weight bandwidth, AIMC array dimensions and cell technology (SRAM, IGZO, SOT-MRAM).

## Contributions
- Hierarchical tile/PE/AIMC mapping exploration with layer fusion/splitting for multi-layer parallel architectures
- Exploration under both sufficient and limited resource constraints incl. weight-loading overhead
- Detailed PPA model for hybrid digital/analog tile units, instruction memory and weight loading
- Case-study insights on weight reuse, memory bandwidth, array size and cell technology

## Key claims (stable IDs)
- **2022_Yang_AERO_JETCAS#C1** — WS mode is ~100x better in power efficiency and performance than WL (#reuse=1) for MLP-3 — _support:_ ~100x — _loc:_ Sec. V-C / Fig. 10
- **2022_Yang_AERO_JETCAS#C2** — For CNNs WS gives 1.570-3.207x better power efficiency and 1.186-3.362x better performance than WL — _support:_ Table VI — _loc:_ Table VI
- **2022_Yang_AERO_JETCAS#C3** — Weight reuse of 16 reaches up to 90% of WS efficiency for ResNet-18/50 — _support:_ up to 90% — _loc:_ Fig. 10
- **2022_Yang_AERO_JETCAS#C4** — Limited-resource WL (LR-WL) has 18% higher latency than SR-WL but 15% higher power efficiency and 73% lower area — _support:_ stated — _loc:_ Sec. VI / Fig. 12
- **2022_Yang_AERO_JETCAS#C5** — 1152 rows x 512 cols AIMC gives a good latency/energy/area trade-off — _support:_ 1152x512: 4234 cycles, 0.443 TOPS/W, 0.013 TOPS/mm2 (MLP-3 footnote) — _loc:_ Sec. V-F
- **2022_Yang_AERO_JETCAS#C6** — Weight access latency saturates at ~120 Bytes/cycle — _support:_ stated — _loc:_ Sec. VI / Fig. 13

## Results
- WS vs WL: 1.57-3.21x power efficiency, 1.19-3.36x performance on CNNs; ~100x for MLP-3
- LR-WL: +18% latency, +15% power efficiency, -73% area vs SR-WL
- SRAM lowest energy/latency in WL mode; IGZO best power/area efficiency in WS mode; SOT-MRAM WL ~3x slower, IGZO ~10x slower than SRAM
- Baseline TANIA 4 clusters 103.6 mm2, AIMC 46.6% of area; fD=1 GHz, fA=0.1 GHz

## Key numbers
- tech_node: 22nm GF22FDX
- array_size: 1152x512 (swept 512-1152 rows x 256-1024 cols)
- energy_eff: 0.443 TOPS/W (MLP-3 1152x512)

## Datasets / benchmarks
MLP-3, LeNet-5, ResNet-18, ResNet-34, ResNet-50, ResNet-101

## Limitations
- Pure simulation/analytic PPA; no silicon or accuracy modeling
- NoC contention not modeled
- Loop-transformation exploration over memory hierarchy not supported
- Only CNNs and an MLP; no attention/transformers or KV cache
- Cell technology parameters partly in-house data and mixed nodes (SOT-MRAM at 45nm)

## Remarks
Useful reminder that weight loading, not MAC cost, dominates when models exceed on-chip analog capacity -- the same issue large LMs face with AIMC (limited-resource mapping). The WL-vs-WS quantification (1.6-3.4x for CNNs, ~100x for FC-heavy MLPs) suggests FC/projection-heavy transformers would be extremely WL-sensitive. Limited to CNNs and ideal analog precision.

## Cites (in collection, 4)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "Unlike DSE frameworks for single-layer parallel architectures (i.e., considering loop mapping at memory hierarchies), the existing DSE frameworks/methodologies for multi-layer parallel architectures (e.g., in [5–7, 11]) and they focus more on mapping at AIMC-level and Tile/PE-level."
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021) — _background_: "In recent years, analog in memory compute (AIMC) arrays have attracted much attention in the accelerator design [3]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Second, multi-layer parallel architectures (e.g., ISAAC [5] and PUMA [7]) are capable of processing multiple CNN layers simultaneously, allowing multi-layer pipelines to maximize the throughput of a full CNN workload."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _background_: "This helps in reduction of intermediate result storage space as well as speeding up execution [6]."

## Cited by (in collection, 5)
- [2023_Sun_AIMCvsDIMC_ICCAD](2023_Sun_AIMCvsDIMC_ICCAD.md) AIMC-vs-DIMC (ZigZag-IMC) (2023) — _contrasts/critiques_: "Similarly, for mapping space explorations, most of the focus has been dedicated to AIMC designs, while lacking DIMC assessment [18, 19, 22, 23]."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _contrasts/critiques_: "Existing memory-centric dataflow exploration frameworks [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25] are predominantly tailored for conventional neural networks (NNs) and fall short in addressing the design challenges of LLMs."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _baseline/comparison_: "PUMA [16] employs compiler analysis passes to define which parts of the application have the most potential for speedup, while AERO [17] formulates this same problem as a cost function minimization."
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2022_Yang_AERO_JETCAS.pdf](../../05_Mapping_Compilation_and_Dataflow/2022_Yang_AERO_JETCAS.pdf)
- Full text: [../fulltext/2022_Yang_AERO_JETCAS.txt](../fulltext/2022_Yang_AERO_JETCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jetcas.2022.3171826
