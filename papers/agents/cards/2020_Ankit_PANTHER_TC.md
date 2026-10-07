---
id: W2997247951
key: 2020_Ankit_PANTHER_TC
title: "PANTHER: A Programmable Architecture for Neural Network Training Harnessing Energy-Efficient ReRAM"
short: "PANTHER"
year: 2020
venue: "TC"
venue_full: "IEEE Transactions on Computers (2020)"
authors: "Aayush Ankit, Izzat El Hajj, Sai Rahul Chalamalasetti, Sapan Agarwal, Matthew J. Marinella, Martin Foltín, John Paul Strachan, Dejan S. Milojicic, Wen‐mei Hwu, Kaushik Roy"
category: "10 On-chip & Analog Training"
devices: ["ReRAM", "SRAM-digital"]
models: ["MLP", "CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["on-chip-training", "bit-slicing", "crossbar-architecture", "compiler-software-stack", "write-verify-programming", "energy-efficiency", "dataflow-pipelining", "mixed-precision"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 8
citations_overall: 88
priority_score: 6.3
doi: "https://doi.org/10.1109/tc.2020.2998456"
pdf: "../../10_On_Chip_and_Analog_Training/2020_Ankit_PANTHER_TC.pdf"
fulltext: "../fulltext/2020_Ankit_PANTHER_TC.txt"
---

# PANTHER

**PANTHER: A Programmable Architecture for Neural Network Training Harnessing Energy-Efficient ReRAM** — IEEE Transactions on Computers (2020) (2020)

## TL;DR
PANTHER is an ISA-programmable ReRAM training accelerator whose bit-sliced crossbars perform high-precision matrix-vector and outer-product-accumulate (OPA) operations in place, giving up to 8.02x/54.21x/103x lower energy and 7.16x/4.02x/16x faster execution than digital accelerators, ReRAM-based accelerators and GPUs.

## Summary
Training on ReRAM crossbars is hampered by serial reads and writes for weight-gradient and update, and in-crossbar outer-product demonstrations had low precision (2-5 bit) and covered SGD on fully-connected layers only. PANTHER proposes a bit-slicing technique for outer products, different from MVM bit-slicing: weights are split into slices across crossbars (up to 8 slices), each with limited cell bits (heterogeneous slice widths; searches suggest at least 4 bits for higher-order slices and at least 5 bits for the lower-order four), and a periodic Carry Resolution Step (CRS) rolls overflow into higher slices to avoid saturation. Three crossbar variants serve different training algorithms (SGD with exact, batch/minibatch and other weight-update flows), with MVM, transpose-MVM (MTVM) and OPA performed in the same crossbar. The architecture extends PUMA's tiled organisation, ISA, compiler (C++ graph front end) and simulator with an MCU supporting MVM, MTVM and OPA, so convolutional layers and many training algorithms are supported, including weight-gradient convolutions formulated as outer products (claimed first). Evaluation uses a 4-layer MLP on SVHN and VGG-16 on CIFAR-100 (ImageNet is infeasible on the simulator: ~1 month), compared with digital CMOS (32 nm), ReRAM baselines with serial reads/writes (Base_mvm, Base_opa/mvm approximating PipeLayer) and an RTX 2080-Ti. A PANTHER node is 117 mm2 and 105 W TDP at 1 GHz in 32 nm CMOS-ReRAM, versus 578 mm2 and 839 W for the digital baseline of the same on-chip memory.

## Contributions
- Bit-slicing technique for high-precision ReRAM outer-product accumulate with CRS carry handling
- Crossbar architecture with three variants for different training algorithms and layer types
- Formulation of convolutional weight-gradient computation as outer products
- ISA, compiler and simulator extensions of PUMA for training
- Design-space exploration of heterogeneous slice widths and CRS frequency versus accuracy and energy

## Key claims (stable IDs)
- **2020_Ankit_PANTHER_TC#C1** — Up to 8.02x, 54.21x, 103x energy reduction vs digital accelerators, ReRAM-based accelerators, GPUs — _support:_ abstract; FC layers show 54.21x vs ReRAM baselines — _loc:_ Abstract, Sec. 7.2-7.4
- **2020_Ankit_PANTHER_TC#C2** — Up to 7.16x, 4.02x, 16x execution-time reduction vs digital, ReRAM, GPU — _support:_ abstract — _loc:_ Abstract
- **2020_Ankit_PANTHER_TC#C3** — Heterogeneous slice widths give better accuracy-energy tradeoffs than uniform slicing — _support:_ sixteen slicing configurations; at least 4 bits for slices 4-7 and at least 5 bits for slices 0-3 preserve accuracy — _loc:_ Sec. 7.1, Fig. 10
- **2020_Ankit_PANTHER_TC#C4** — 3 bits per slice saturates low-order slice cells and 4 bits per slice needs frequent CRS — _support:_ percentage of saturated cells; CRS every 64 examples works at 4 bits — _loc:_ Sec. 7.1
- **2020_Ankit_PANTHER_TC#C5** — Existing ReRAM training accelerators (PipeLayer) compute weight-gradient convolutions with MVM, requiring crossbar writes of non-stationary data — _support:_ serial read/write dominates efficiency — _loc:_ Sec. 5.4.3

## Results
- Platform: PANTHER node 117 mm2, 105 W, 72.4 MB on-chip, 32 nm CMOS-ReRAM at 1 GHz; Base_digital 578 mm2, 839 W; RTX 2080-Ti 750 mm2, 250 W (Table 3)
- Energy for convolutional layers reduced 1.18-1.63x and 1.22-2.45x vs Base_mvm and Base_opa/mvm in the CNN
- Base_mvm suffers badly for small-batch MLPs because ReRAM write latency is not hidden
- Workloads: 4-layer MLP on SVHN, VGG-16 on CIFAR-100 (Top-5 accuracy)

## Key numbers
- tech_node: 32nm
- energy_eff: up to 8.02x (vs digital), 54.21x (vs ReRAM), 103x (vs GPU)
- throughput: up to 7.16x, 4.02x, 16x execution-time reduction
- bits_weight: slice widths 4-6 bits across 8 slices

## Datasets / benchmarks
SVHN, CIFAR-100

## Limitations
- Simulation (extended PUMA simulator + circuit models); no fabricated chip
- Workloads limited to MLP-L4/SVHN and VGG-16/CIFAR-100; ImageNet and larger models not run (simulator cost)
- Assumes ReRAM write precision and linearity sufficient for OPA pulse updates; endurance of frequent updates is a concern
- Floating-point training not supported without modification; fixed-point only
- Energy numbers underestimated for non-Pareto-optimal slicing choice (44466555)

## Remarks
A strong architectural answer to the 'write bottleneck' of crossbar training, and an important prerequisite for analog fine-tuning ideas relevant to adapting LMs on-device. The evidence is simulation on small models, and it does not address transformer-specific operators. Related in spirit to FloatPIM (digital alternative) and PipeLayer (serial writes) within the collection.

## Cites (in collection, 8)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "the iterative nature of DNN training and careful re-training helps recover the accuracy loss from non-idealities [43], faults [44], and variations [45]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _contrasts/critiques_: "Existing ReRAM-based training accelerators such as PipeLayer [8] do not compute the weight gradient convolutions using outer products, but rather, they compute them using MVM operations."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "the iterative nature of DNN training and careful re-training helps recover the accuracy loss from non-idealities [43], faults [44], and variations [45]."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _contrasts/critiques_: "The aforementioned technique has been demonstrated with low-precision inputs/outputs (2-4 bits) and weights (2-5 bits) on the SGD training algorithm for FC layers only [10, 11]."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _uses-method-or-tool_: "To strike a balance, we choose p = 4, since p > 4 requires a device precision that exceeds ReRAM technology limits [15]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _extends/builds-on_: "The PUMA [6] compiler provides a high-level programming interface in C++ that allows programmers to express"
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "We use the ReRam crossbar array and sample-and-hold circuit models in ISAAC [4]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 13)
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _uses-method-or-tool_: "We conservatively assume 32-bit precision for all data structures (viz.) weights, activations and errors in DNN training based on the scheme proposed in [30], since it provides classification accuracy close to floating-point training [31]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _extends/builds-on_: "To address such challenges, we describe a recently proposed technique to incorporate bit-slicing in the weight update operation [102] (see Section IV-E1)."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "To implement training, a Programmable Architecture for Neural Network Training Harnessing Energy-efficient ReRAM (PANTHER) was introduced and evaluated on PUMA [40]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "Another accelerator design, Panther [4], updates weights with outer product accumulate operations, where input voltages are fed to memristor crossbars' bitlines and wordlines simultaneously."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _motivation_: "This is a challenge due to NVMs requiring atleast one to two orders of magnitude higher latency and energy/bit depending on the NVM device compared to SRAM for the same technology node [8]–[10]."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "Processing-in-Memory (PIM) has emerged as a promising approach to accelerate the training/inference of machine learning (ML) workloads [9]."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "The dual-mode CIM array can operate as both a memory and compute unit when applying a slight enhancement on the input or output drivers [2, 10, 18, 24, 42, 48, 51, 53]."
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2020_Ankit_PANTHER_TC.pdf](../../10_On_Chip_and_Analog_Training/2020_Ankit_PANTHER_TC.pdf)
- Full text: [../fulltext/2020_Ankit_PANTHER_TC.txt](../fulltext/2020_Ankit_PANTHER_TC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tc.2020.2998456
