---
id: W2949989598
key: 2019_Imani_FloatPIM_DAC
title: "FloatPIM"
short: "FloatPIM"
year: 2019
venue: "DAC"
venue_full: "ACM/IEEE Design Automation Conference (DAC 2019)"
authors: "Mohsen Imani, Saransh Gupta, Yeseong Kim, Tajana Rosing"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM", "Memristor(generic)"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "on-chip-training", "dataflow-pipelining", "endurance-retention", "cnn-accelerator", "energy-efficiency", "bit-slicing"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 9
cites_in_collection: 4
citations_overall: 190
priority_score: 7.59
doi: "https://doi.org/10.1145/3307650.3322237"
pdf: "../../03_Crossbar_Accelerator_Architectures/2019_Imani_FloatPIM_DAC.pdf"
fulltext: "../fulltext/2019_Imani_FloatPIM_DAC.txt"
---

# FloatPIM

**FloatPIM** — ACM/IEEE Design Automation Conference (DAC 2019) (2019)

## TL;DR
FloatPIM is a fully digital ReRAM PIM architecture that performs floating-point (bfloat16/fp32) CNN training and inference with in-memory NOR operations, achieving on average 303.2x speedup and 48.6x energy gain over a GTX 1080 for training and 4.3x/15.8x over PipeLayer.

## Summary
Prior ReRAM PIM accelerators (ISAAC, PRIME, PipeLayer) exploit analog crossbar currents, need expensive ADC/DAC blocks and multi-bit cells, and are limited to fixed-point precision, which hurts CNN training accuracy. FloatPIM instead stores data digitally in single-bit bipolar memristors and implements all arithmetic, including floating-point add and multiply, as sequences of bitwise NOR operations inside the memory (a digital in-memory logic style), so no analog-domain conversion occurs and no multi-bit devices are required. Weights and activations live in 1 Mb memory blocks (1K-bit rows) with 256 blocks per tile and 32 tiles total. Computation alternates between a compute mode, in which all blocks run row-parallel, and a data-transfer mode, in which neighbouring blocks exchange data through a pipelined row-parallel switch network. Evaluation uses a TensorFlow-based cycle-accurate emulator with HSPICE circuit simulation at 28 nm (VTEAM memristor model, Ron 10 kOhm, Roff 10 MOhm, 1 ns switching) cross-checked with NVSim, on AlexNet, VGGNet, GoogleNet and SqueezeNet with ImageNet. FloatPIM adds endurance management by rotating the columns used for intermediate processing state.

## Contributions
- First PIM-based CNN training architecture working on floating-point and fixed-point data without explicit analog conversion (per the authors)
- Fully digital NOR-based computation on single-bit bipolar ReRAM, removing ADC/DAC and multi-bit device needs
- Compute/data-transfer phases with row-parallel pipelined block-to-block transfer to cut internal data movement
- Endurance management by rotating processing columns, ~11x lifetime gain
- Evaluation on four ImageNet CNNs versus GPU, ISAAC and PipeLayer

## Key claims (stable IDs)
- **2019_Imani_FloatPIM_DAC#C1** — Floating-point precision yields up to 5.1% higher accuracy than fixed-point PIM — _support:_ bfloat vs fixed-point error rates on AlexNet, GoogleNet, VGGNet, SqueezeNet — _loc:_ Sec. 7.2, Table 4
- **2019_Imani_FloatPIM_DAC#C2** — Training is on average 303.2x faster and 48.6x more energy efficient than GTX 1080; 4.3x and 15.8x versus PipeLayer — _support:_ averages over four networks — _loc:_ Sec. 7.4, Abstract
- **2019_Imani_FloatPIM_DAC#C3** — Testing is 324.8x faster and 297.9x more energy efficient than GPU and 6.3x/21.6x vs ISAAC — _support:_ average over four networks — _loc:_ Sec. 7.3, Abstract
- **2019_Imani_FloatPIM_DAC#C4** — Crossbar memory dominates area — _support:_ 32 tiles = 30.64 mm2, 95.1% crossbar; tile 0.96 mm2 and 7.64 mW; total 62.60 W — _loc:_ Sec. 7.7, Table 2
- **2019_Imani_FloatPIM_DAC#C5** — Rotating processing columns extends memory lifetime by ~11x — _support:_ 1024 columns per block, 93 reserved for bfloat16 processing — _loc:_ Sec. 7.8

## Results
- Training: 303.2x speedup, 48.6x energy efficiency vs GTX 1080 GPU; 4.3x and 15.8x vs PipeLayer (Sec. 7.4)
- Testing: 324.8x and 297.9x vs GPU; 6.3x and 21.6x vs ISAAC (Sec. 7.3)
- bfloat16 versus 32-bit float: 2.9x speedup and 2.5x energy savings (Sec. 7.2)
- Area 30.64 mm2 for 32 tiles, power 62.60 W; 95.1% of area is crossbar memory (Sec. 7.7, Table 2)
- Hardware assumes 8-bit ADC/1-bit DAC/128x128 arrays with 2 bit/cell for ISAAC comparison

## Key numbers
- tech_node: 28nm
- array_size: 1Mb blocks (1K-bit rows); 256 blocks/tile; 32 tiles
- energy_eff: 48.6x vs GTX 1080 (training); 15.8x vs PipeLayer
- throughput: 303.2x vs GTX 1080 (training)
- accuracy: up to 5.1% lower error than fixed-point PIM
- bits_weight: bfloat16 / fp32 (also fixed-point)
- bits_adc: none (digital)

## Datasets / benchmarks
ImageNet

## Limitations
- Simulation (HSPICE + TensorFlow emulator), no fabricated chip
- Bit-serial NOR logic makes floating-point operations very long sequences; throughput relies on massive parallelism and large area/power (62.6 W)
- ReRAM endurance for training remains a concern even with 11x rotation gain
- Digital in-memory logic requires high write counts; benefit depends on assumed 1 ns switching device
- Only CNNs, no transformers or language models; not analog MVM, so non-idealities of analog crossbars are not studied
- The packet lists DAC as venue, but the paper header shows ISCA 2019

## Remarks
An influential counterpoint to the ISAAC/PRIME analog crossbar line: it avoids analog noise and ADC cost entirely by using digital in-memory logic, at the price of bit-serial latency and heavy endurance stress. Evidence is circuit-level simulation. Relevant for the analog mapping thesis as a design-space alternative (precision-preserving training in memory), but its approach does not transfer to the dense analog MVM efficiency that analog LM inference chips target.

## Cites (in collection, 4)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "PipeLayer [1] modified the ISAAC [2] pipeline architecture and use spike-based input to eliminate ADC and DAC blocks."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _motivation_: "However, the mixed-signal ADC/DAC blocks take the majority of the chip area and power, e.g., 98% of the total area and 89% of the total power, and do not scale as fast as the CMOS technology does [2]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "ISAAC [2] and PRIME [11] exploit analog characteristics of non-volatile memory to support matrix multiplication in memory."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _contrasts/critiques_: "For example, work in [25–27] extend the application of analog crossbar memory to accelerate training, but they still have expensive converter units and multi-bit devices."

## Cited by (in collection, 9)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _motivation_: "The recent study [40, 42] reports the ADC/DAC blocks may become the major contributor to the total chip area and power."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _contrasts/critiques_: "FloatPIM [17] supports reduction by organizing reduction data in a bit-serial way to avoid extra data movement. But this scheme sacrifices parallelism in Transformer which usually has long vectors for reduction."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _baseline/comparison_: "Because of the different disposition of elements, previous crossbar designs should separately hold transposed weight matrices in addition to the original weight [20, 48]."
- [2024_Pan_PRIMATE_ASP-DAC](2024_Pan_PRIMATE_ASP-DAC.md) PRIMATE (2024) — _contrasts/critiques_: "This work focuses on DRAM-based (HBM) PIM technologies which can support larger capacity than SRAM [23] with high bandwidth, lower latency, and higher numerical stability than nonvolatile memory designs [6], [24]."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "Digital PIM, which has been extensively studied [22, 31, 72], achieves data movement reduction with reliable computation through simple bit-wise operations (e.g., NOR, INV, and others) but suffers from limited parallelism compared to analog PIM."
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021)
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2019_Imani_FloatPIM_DAC.pdf](../../03_Crossbar_Accelerator_Architectures/2019_Imani_FloatPIM_DAC.pdf)
- Full text: [../fulltext/2019_Imani_FloatPIM_DAC.txt](../fulltext/2019_Imani_FloatPIM_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3307650.3322237
