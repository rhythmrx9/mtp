---
id: W3188508394
key: 2021_Siemieniuk_OCC_TCAD
title: "OCC: An Automated End-to-End Machine Learning Optimizing Compiler for Computing-In-Memory"
short: "OCC"
year: 2021
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 41, no. 6, pp. 1674-1686 (published online Aug. 2021, issue June 2022)"
authors: "Adam Siemieniuk, Lorenzo Chelini, Asif Ali Khan, Jerónimo Castrillón, Andi Drebes, Henk Corporaal, Tobias Grosser, Martin Kong"
category: "05 Mapping, Compilation & Dataflow"
devices: ["PCM"]
models: ["MLP", "CNN", "LSTM/RNN", "Speech"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["compiler-software-stack", "tiling-partitioning", "weight-mapping", "scheduling", "endurance-retention", "bit-slicing", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 5
cites_in_collection: 6
citations_overall: 31
priority_score: 7.38
doi: "https://doi.org/10.1109/tcad.2021.3101464"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2021_Siemieniuk_OCC_TCAD.pdf"
fulltext: "../fulltext/2021_Siemieniuk_OCC_TCAD.txt"
---

# OCC

**OCC: An Automated End-to-End Machine Learning Optimizing Compiler for Computing-In-Memory** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 41, no. 6, pp. 1674-1686 (published online Aug. 2021, issue June 2022) (2021)

## TL;DR
OCC is an MLIR-based multilevel-rewriting compiler that automatically detects GEMM-like motifs (contractions via TTGT, convolutions via Im2Col) in Tensor Comprehension code and offloads tiled GEMMs to a PCM crossbar co-processor, giving up to 17x average speedup and 5.0x energy reduction over an ARM core in gem5 and ~2 years longer crossbar lifetime from write-minimising loop interchange.

## Summary
Memristor crossbar accelerators are programmed manually through APIs, hindering adoption; the paper builds a fully automatic end-to-end compiler. The frontend (Teckyl) accepts Tensor Comprehensions, entered at the MLIR Linalg dialect. Hardware-agnostic passes rewrite contractions with transpose-transpose-GEMM-transpose (TTGT) and convolutions with Im2Col so that matrix multiplication is the only primitive. Hardware-specific passes in a new CIM dialect (cim.write, cim.matmul, cim.barrier, copyTile, accumulate, storeTile) tile GEMMs to the crossbar size, interchange loops so a written weight tile is reused (cutting crossbar writes by tiledRows), and unroll the reduction loop to run tiles in parallel. CIM operations lower one-to-one to a runtime library driving a memory-mapped co-processor with DMA. The target is a gem5 full-system SoC with an in-order ARM core (2 GHz) and a 4-tile PCM accelerator (64x64 per tile, 8-bit via bit slicing across columns, ADC/sample-and-hold peripherals, PCM write 2.5x costlier than read). Workloads are 8-bit ML and tensor kernels (mm, 2mm, 3mm, conv1d/2d/3d, mlp3, lstm, WaveNet, contractions); energy uses McPAT plus a separate CIM model, and accuracy effects of ADC quantisation or device noise are explicitly not addressed.

## Contributions
- First end-to-end CIM compilation flow based on multilevel IR rewriting (MLIR) with transparent offloading, no user rewriting of code
- Hardware-agnostic rewrites (TTGT, Im2Col) mapping contractions and convolutions to GEMM, plus a CIM dialect and runtime library
- Hardware-specific tiling, loop interchange (fewer crossbar writes) and unrolling (multi-tile parallelism) passes
- gem5-based evaluation of performance, energy, endurance, and comparison against TDO-CIM and TC-CIM in kernel detection

## Key claims (stable IDs)
- **2021_Siemieniuk_OCC_TCAD#C1** — OCC identifies all expected CIM callsites where prior compilers miss some — _support:_ OCC matches the Oracle; TDO-CIM and TC-CIM miss all contractions and one matrix-vector product in mlp3 and WaveNet — _loc:_ Sec. V-F, Fig. 12
- **2021_Siemieniuk_OCC_TCAD#C2** — Offloading gives large speedup over the ARM host — _support:_ tile 6.6x, tile+parallel 15.5x, tile+interchange+parallel 17x average; up to 512x for large mm — _loc:_ Sec. V-B/C, Figs. 7, 8
- **2021_Siemieniuk_OCC_TCAD#C3** — Energy reduction of 1.9x-5.0x on average — _support:_ 4.5x and 5.0x for tile+parallel and tile+parallel+interchange — _loc:_ Sec. V-D, Fig. 8
- **2021_Siemieniuk_OCC_TCAD#C4** — Loop interchange extends lifetime — _support:_ 7.4x fewer crossbar writes; lifetime increased by almost two years (cell endurance 3.2e7) — _loc:_ Sec. V-C/E, Fig. 11

## Results
- Small matrices run 32% slower than ARM because crossbar programming dominates; large matrices reach 512x speedup (Fig. 7)
- Average speedup 6.6x (tile), 15.5x (tile+parallel), 17x (tile+parallel+interchange); loop interchange cuts writes 7.4x
- Average energy reduction 1.9x-5.0x, but waveNet, conv2d, lstm and mv use 60%, 30%, 10%, 40% more energy in the full-optimisation configuration
- Convolution utilises ~2% of crossbar and WaveNet ~6.5%; only 50% of WaveNet and 99.5% of mlp3 computation offloaded
- Im2Col overhead limits conv2d acceleration to 34% of kernel computations

## Key numbers
- tech_node: PCM models from 90nm CMOS devices
- array_size: 4 tiles of 64x64
- energy_eff: 1.9x-5.0x lower energy vs ARM
- throughput: up to 17x average speedup vs ARM; 512x on large mm
- bits_weight: 8b (bit-sliced)

## Datasets / benchmarks
mm/2mm/3mm/tmm kernels, conv1d/2d/3d, mlp3, lstm, WaveNet, tensor contractions (abcd-aebf-dfce, kronecker3)

## Limitations
- Simulated co-processor (gem5) with 4 small 64x64 PCM tiles; no silicon
- ADC quantisation loss, device noise, drift and variation are not modelled or addressed in accuracy terms
- Baseline is a single in-order ARM core, so speedups are inflated relative to GPUs/accelerators
- Unsupported kernels: batched matmul, grouped convolution, I x I self-products, gather; non-GEMM ops stay on the CPU
- No transformer/attention or language-model workloads; bit-slicing 8-bit only

## Remarks
A foundational compiler paper in the collection: shows how MLIR progressive lowering can detect and offload GEMM motifs and how loop interchange trades writes for reuse, which matters for write-expensive PCM/ReRAM. The weak baseline and ideal analog assumptions limit absolute claims. Direct relevance to language models is indirect: transformers' linear layers reduce to the same GEMM primitive, but attention (dynamic operands requiring crossbar writes) is exactly the case where its write-reduction logic would be stressed. Cited by later CIM compilers such as CIM-MLC and PIMCOMP.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _contrasts/critiques_: "A similar approach is used in other works [10], [35]-[37] where the in-memory accelerator exposes an API."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "Building on their effort, Ankit et al. [24] developed a runtime compiler implemented as a C++ library, which requires the users to rewrite the application with the proposed API."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Memristor crossbars, in particular, have attracted significant interest due to their ability to efficiently perform matrix-matrix and matrix-vector multiplications-the dominant computational kernels in deep neural networks [6]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _motivation_: "As a consequence, efficient exploitation of CIM acceleration still relies on the programmer and her understanding of the hardware, thus severely limiting programmability [6], [9], [10]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "A similar approach is used in other works [10], [35]-[37] where the in-memory accelerator exposes an API."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _uses-method-or-tool_: "To accomplish 8-bit precision, we rely on the bit-slicing technique, which allows increasing accuracy by combining modules of smaller bit width [7]."

## Cited by (in collection, 5)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _contrasts/critiques_: "Relatively, OCC [40] is a comprehensive compilation that encompasses abundant device types as well as numerous programming interfaces."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _contrasts/critiques_: "TC-CIM [19], TDO-CIM [20], CINM [23], OCC [21], Polyhedral [16], Co-Design [17], and PUMA [22] do not consider the interaction between weight replication and weight layout, and simply map computational tasks to PIM arrays."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _baseline/comparison_: "To enhance efficiency and fully realize the potential of the CIM accelerators, researchers have explored various compilation optimization techniques, aimed at various CIM architectures such as resistant RAM and SRAM-based solutions [14, 16, 21, 33, 39, 44]."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2021_Siemieniuk_OCC_TCAD.pdf](../../05_Mapping_Compilation_and_Dataflow/2021_Siemieniuk_OCC_TCAD.pdf)
- Full text: [../fulltext/2021_Siemieniuk_OCC_TCAD.txt](../fulltext/2021_Siemieniuk_OCC_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2021.3101464
