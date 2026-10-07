---
id: W4311978413
key: 2022_Klein_ALPINE_TC
title: "ALPINE: Analog In-Memory Acceleration with Tight Processor Integration for Deep Learning"
short: "ALPINE"
year: 2022
venue: "TC"
venue_full: "IEEE Transactions on Computers"
authors: "Joshua Alexander Harrison Klein, Irem Boybat, Yasir Mahmood Qureshi, Martino Dazzi, Alexandre Levisse, Giovanni Ansaloni, Marina Zapater, Abu Sebastian, David Atienza"
category: "03 Crossbar Accelerator Architectures"
devices: ["PCM"]
models: ["MLP", "LSTM/RNN", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "heterogeneous-analog-digital", "simulator", "weight-mapping", "tiling-partitioning", "compiler-software-stack", "energy-efficiency", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 11
citations_overall: 17
priority_score: 5.81
doi: "https://doi.org/10.1109/tc.2022.3230285"
pdf: "../../03_Crossbar_Accelerator_Architectures/2022_Klein_ALPINE_TC.pdf"
fulltext: "../fulltext/2022_Klein_ALPINE_TC.txt"
---

# ALPINE

**ALPINE: Analog In-Memory Acceleration with Tight Processor Integration for Deep Learning** — IEEE Transactions on Computers (2022)

## TL;DR
ALPINE integrates PCM-based AIMC tiles into ARMv8 multi-core CPUs via custom ISA instructions and a gem5-X simulator plus AIMClib, showing up to 20.5x performance and 20.8x energy gains over a NEON-SIMD CPU on MLP, LSTM and CNN inference.

## Summary
Stand-alone AIMC accelerators lack flexibility (network types, dataflow, activation functions, number formats), and loosely coupled CPU-AIMC designs are bottlenecked by CPU-tile interaction because tiles run in about 100 ns. ALPINE builds a gem5-X full-system model (Linux + ARMv8 MinorCPU, 8 cores) where AIMC crossbar tiles are tightly coupled via custom instructions for queue/process/dequeue, with a software library AIMClib. Weights are mapped to PCM tiles (M rows x N columns; MLP layers split over 1-4 tiles; LSTM gates sliced so element-wise ops read consecutive columns; CNN kernels flattened into columns with fine-grained pipelining), while activations (ReLU, sigmoid, softmax, pooling) run on CPU in int8 with fp32 accumulation. The AIMC tile is modeled from 14 nm PCM chip measurements (256x256, 100 ns latency, 12.8 TOp/s/W, 4 GB/s IO) scaled to 28 nm (5.3x high-power, 2x low-power); cores and caches use a 28 nm Cortex-A53-based power model and DRAM energy 120 pJ/access. Three studies (MLP, LSTM, CNN-F/M/S) compare against a digital multithreaded NEON baseline in single- and multi-core cases. Results: MLP up to 12.8x/12.5x speedup/energy, LSTM up to 9.4x/9.3x, CNN up to 20.5x/20.8x; the work also quantifies MVM share of runtime (Amdahl-style application-wide benefit).

## Contributions
- gem5-X-based full-system simulation framework (ALPINE) with AIMC tile models.
- Custom ARMv8 ISA extension for tightly coupled AIMC tiles.
- AIMClib software library for programming AIMC inference.
- Mapping and multi-core exploration of MLP, LSTM and CNN with up to 20.5x/20.8x gains.
- Quantification of MVM as hotspot and application-wide acceleration limits.

## Key claims (stable IDs)
- **2022_Klein_ALPINE_TC#C1** — Tightly coupled AIMC yields up to 20.5x performance and 20.8x energy gain over SIMD CPU for CNNs. — _support:_ abstract and contributions — _loc:_ Sec. IX, Abstract
- **2022_Klein_ALPINE_TC#C2** — MLP up to 12.8x/12.5x speedup/energy; LSTM up to 9.4x/9.3x. — _support:_ contribution list — _loc:_ Sec. I, VII, VIII
- **2022_Klein_ALPINE_TC#C3** — AIMC tile latency increased 10x has minimal impact on MLP results. — _support:_ sensitivity study — _loc:_ Sec. VII

## Results
- MLP: up to 12.8x speedup and 12.5x energy improvement vs NEON digital baseline.
- LSTM: up to 9.4x / 9.3x with working set 7x larger.
- CNN (F/M/S, 8 cores): up to 20.5x / 20.8x.
- Loosely coupled two-AIMC configuration reports 4.1x speedup but 3.1x slowdown versus tightly coupled system in one case (Sec. VII).

## Key numbers
- tech_node: 28nm CPU/cache model; 14nm PCM AIMC tile scaled
- array_size: 256x256 AIMC tile
- energy_eff: 12.8 TOp/s/W (256x256 tile MVM)
- throughput: 20.5x speedup (CNN)
- bits_weight: int8
- bits_adc: 8-bit digital output

## Limitations
- Simulation only; AIMC tile is a performance/energy model from 14 nm data, no analog noise or accuracy modeled in system results.
- Technology scaling of mixed-signal tile to 28 nm is an acknowledged conservative approximation.
- In-order cores only; small networks (MLP, LSTM, CNN); no Transformers or LMs evaluated.

## Remarks
A system-integration study that shows how much CPU-AIMC interplay and non-MVM work (activations, softmax) limit end-to-end gains, which matters for LM mapping where attention and nonlinearities stay digital. It does not evaluate accuracy under analog noise. Complements tile-based accelerators like ISAAC/PUMA in the collection.

## Cites (in collection, 11)
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _data/numbers_: "The scalar multiplication of an analog input with PCMbased weights is shown to be comparable to an implementation with 4-bit fixed-point inputs and weights [32], and even to an implementation with 8-bit fixed-point inputs and weights with suitable innovations in device design [33]."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _background_: "One way to address the limitations of standalone AIMCbased accelerators is to add local CPUs [8, 9, 10, 11]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "[9] describes an ISA and compiler dedicated to programming and utilizing a multi-tile AIMC accelerator, and an associated architectural simulator (named PUMASim) to evaluate the energy and performance of compiled applications."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "PCM-based implementations hence offer high performance densities (TOp/s/mm2 ), where a pair of PCM devices can represent signed multi-bit weights [16]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "With analog in-memory computing (AIMC) certain computations directly take place where the data is located, exploiting device physics and circuit laws [5]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _motivation_: "The CPU-AIMC interplay nonetheless often is the run-time bottleneck in these systems, as AIMC tiles at competitive technology nodes typically operate on the order of hundreds of nanoseconds [12, 13]."
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020) — _background_: "Despite the reduced precision weights, AIMC implementations were shown to address the inference of MLPs [30, 31], CNNs [16, 30, 31], RNNs [19, 30, 31], and transformers [20] with high accuracies."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _background_: "Prior work includes iso-accuracy studies for convolutional neural networks (CNNS) [16, 17, 18], recurrent neural networks (RNNs) [19, 17] and transformers [20]."
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022) — _contrasts/critiques_: "Zheng et al. also use the ONNX framework as the front end for their event-driven cross-level simulation of processing-in-memory accelerators, while also incorporating elements for simulating memory access and interconnects [24]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "One approach to exploit in-memory computing for DNNs is to design stand-alone accelerators where multiple AIMC tiles and associated digital logic blocks are interconnected by a suitable communication fabric [6, 7]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "PCM devices have the potential to scale to nanoscale dimensions and can be integrated in the back-end of a CMOS chip [13]."

## Cited by (in collection, 2)
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _uses-method-or-tool_: "Architectures can utilize IMC at different levels of the memory hierarchy, for example, when interfacing main memory [10], as part of smart caches [11], or as functional units that augment processor pipelines and register files [4]."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2022_Klein_ALPINE_TC.pdf](../../03_Crossbar_Accelerator_Architectures/2022_Klein_ALPINE_TC.pdf)
- Full text: [../fulltext/2022_Klein_ALPINE_TC.txt](../fulltext/2022_Klein_ALPINE_TC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tc.2022.3230285
