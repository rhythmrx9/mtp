---
id: W4394891385
key: 2024_Xu_ReHarvest_TACO
title: "ReHarvest: An ADC Resource-Harvesting Crossbar Architecture for ReRAM-Based DNN Accelerators"
short: "ReHarvest"
year: 2024
venue: "TACO"
venue_full: "ACM Transactions on Architecture and Code Optimization"
authors: "Jiahong Xu, Haikun Liu, Zhuohui Duan, Xiaofei Liao, Hai Jin, Xiaokang Yang, Huize Li, Cong Liu, Fubing Mao, Yu Zhang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["adc-dac", "crossbar-architecture", "peripheral-circuits", "tiling-partitioning", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 6
citations_overall: 12
priority_score: 4.68
doi: "https://doi.org/10.1145/3659208"
pdf: null
fulltext: null
---

# ReHarvest

**ReHarvest: An ADC Resource-Harvesting Crossbar Architecture for ReRAM-Based DNN Accelerators** — ACM Transactions on Architecture and Code Optimization (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ReHarvest decouples ADCs from fixed crossbar arrays via a many-to-many crossbar-ADC resource pool plus multi-tile matrix mapping, improving ADC utilization by 3.2x and achieving 3.5x speedup with 3.1x less ReRAM resource usage versus the state-of-the-art PIM architecture FORMS.

## Summary
The paper targets the ADC bottleneck in ReRAM-based PIM accelerators: ADCs are high-latency, area-inefficient, and are conventionally tightly coupled one-to-one (or few-to-one) with each crossbar array, leaving the scarce ADC resource underutilized when a given crossbar's MVM does not need continuous AD conversion. ReHarvest proposes an ADC-crossbar decoupled architecture with a many-to-many mapping structure that pools all ADCs within a tile so that any crossbar array in that tile can 'harvest' additional ADCs to parallelize its AD conversion, rather than being limited to its statically assigned converters. To extend this sharing benefit across tiles, the authors add a multi-tile matrix mapping (MTMM) scheme that increases data parallelism across tiles, supported by a bus-based interconnection network that multicasts input vectors to multiple tiles to avoid data redundancy and network congestion during the resulting fine-grained data dispatch. Evaluated against the state-of-the-art PIM architecture FORMS, ReHarvest substantially improves ADC resource utilization and throughput while also reducing the amount of ReRAM crossbar hardware needed.

## Contributions
- Identifies ADC-crossbar static coupling as a key source of underutilized ADC resources in ReRAM PIM accelerators
- Proposes a many-to-many crossbar-to-ADC mapping that pools all ADCs in a tile as a shared resource for any crossbar needing AD conversion
- Proposes a multi-tile matrix mapping (MTMM) scheme to extend ADC sharing/parallelism benefits across multiple tiles
- Designs a bus-based interconnection network for fine-grained, multicast-based input-vector dispatch across tiles to avoid data redundancy and network congestion under MTMM
- Demonstrates simultaneous gains in ADC utilization, throughput, and reduced ReRAM array resource consumption versus FORMS

## Key claims (stable IDs)
- **2024_Xu_ReHarvest_TACO#C1** — ReHarvest improves ADC utilization by 3.2x on average compared to FORMS. — _support:_ reported average utilization improvement — _loc:_ Abstract / experimental results
- **2024_Xu_ReHarvest_TACO#C2** — ReHarvest achieves 3.5x performance speedup on average compared to FORMS. — _support:_ reported average speedup — _loc:_ Abstract / experimental results
- **2024_Xu_ReHarvest_TACO#C3** — ReHarvest reduces ReRAM resource consumption by 3.1x on average compared to FORMS. — _support:_ reported average resource reduction — _loc:_ Abstract / experimental results
- **2024_Xu_ReHarvest_TACO#C4** — Statically coupling a fixed number of ADCs to each crossbar array leaves ADC resources underutilized because MVM demand across crossbars is uneven. — _support:_ motivation/architectural rationale for the many-to-many design — _loc:_ Introduction/motivation (abstract)

## Results
- 3.2x average ADC utilization improvement vs. FORMS
- 3.5x average performance speedup vs. FORMS
- 3.1x average reduction in ReRAM crossbar resource consumption vs. FORMS

## Limitations
- Full text not available for this analysis; the quantitative claims above are taken from the abstract only and not independently verified against tables/figures
- Evaluation baseline is limited (as reviewed) to a single state-of-the-art comparison point (FORMS); comparison against other ADC-sharing or ADC-reduction approaches (e.g., Quarry, TinyADC) is not confirmed from the abstract
- The approach adds interconnection/bus complexity (multicast network across tiles) whose own area/energy overhead relative to the ADC savings is not quantified in the abstract

## Remarks
ReHarvest addresses the same ADC-bottleneck problem noted across much of the ReRAM-crossbar accelerator literature in this collection (e.g., Quarry, TinyADC cited as prior ADC-reduction work for this same research group's related papers), but attacks it from a resource-sharing/architecture angle (decoupling ADC-to-crossbar binding) rather than reducing ADC precision or count directly. This is a useful architectural counterpoint for a mapping/peripheral-circuits thesis chapter: rather than reducing analog-to-digital conversion precision, it reorganizes dataflow and interconnect to make better use of existing ADC resources. Because only the abstract was reviewed, the FORMS baseline comparison and the added interconnect overhead should be checked in the full TACO 2024 paper before relying on the specific 3.1x-3.5x figures.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 1)
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _motivation_: "As the AD conversion is a performance bottleneck in ReRAM-based PIM architectures [13, 27, 35, 43], the ADC utilization has a significant impact on the performance and energy efficiency of ReRAMbased crossbar arrays [46]."

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2024_Xu_ReHarvest_TACO.pdf`)
- Full text: none
- DOI: https://doi.org/10.1145/3659208
