---
id: W4287736153
key: 2022_Garofalo_HeterogeneousIMCCluster_JETCAS
title: "A Heterogeneous In-Memory Computing Cluster for Flexible End-to-End Inference of Real-World Deep Neural Networks"
short: "Heterogeneous IMC Cluster"
year: 2022
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems, vol. 12, no. 2, 2022"
authors: "Angelo Garofalo, Gianmarco Ottavi, Francesco Conti, Geethan Karunaratne, Irem Boybat, Luca Benini, Davide Rossi"
category: "03 Crossbar Accelerator Architectures"
devices: ["PCM"]
models: ["CNN", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "heterogeneous-analog-digital", "tiling-partitioning", "dataflow-pipelining", "edge-ai", "cnn-accelerator", "energy-efficiency", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 14
citations_overall: 41
priority_score: 5.54
doi: "https://doi.org/10.1109/jetcas.2022.3170152"
pdf: "../../03_Crossbar_Accelerator_Architectures/2022_Garofalo_HeterogeneousIMCCluster_JETCAS.pdf"
fulltext: "../fulltext/2022_Garofalo_HeterogeneousIMCCluster_JETCAS.txt"
---

# Heterogeneous IMC Cluster

**A Heterogeneous In-Memory Computing Cluster for Flexible End-to-End Inference of Real-World Deep Neural Networks** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems, vol. 12, no. 2, 2022 (2022)

## TL;DR
Couples a 256x256 PCM in-memory accelerator (IMA) with 8 RISC-V cores and a digital depth-wise engine in a PULP cluster (22nm FDX, post-P&R), giving 11.5x speedup / 9.5x energy gain on a MobileNetV2 bottleneck vs the cores alone and 10.1 ms / 482 uJ end-to-end MobileNetV2 with 34 crossbars.

## Summary
Analog IMC arrays are efficient only on MVMs, so real networks (residuals, depth-wise convolutions, activations) hit Amdahl's law and IMA-to-system bandwidth bottlenecks. The authors integrate an analog IMA, based on the 256x256 14nm PCM HERMES core (4-bit signed weights as device pairs, 8-bit DAC input, 8-bit ADC output, 130 ns MVM latency, 1.008 TOPS peak), into a tightly coupled shared-memory PULP cluster (8 RISC-V XpulpV2 cores, 512 kB 32-bank TCDM) through Hardware Processing Engine interfaces, plus a digital depth-wise accelerator. The IMA, array timing/power, is extrapolated from 14nm silicon measurements scaled to GF 22nm FDX; the digital cluster is implemented through full place and route (2.5 mm2) with gate-level power. Point-wise (1x1) layers are mapped on the crossbar, depth-wise layers run on the digital accelerator, and residuals on the cores. For full MobileNetV2 they scale to multiple crossbars sharing one IMA interface with a Tile&Pack algorithm (Alg. 1: tile layers into 256x256 blocks, bin packing with BinBestFit/MaxRects) and weights pre-programmed because PCM reprogramming is 20-30x slower than an MVM. Results: 958 GOPS (>90% of peak) on MVMs, 2.6x/2.8x better performance/energy than the authors' previous cores+IMA design, 10x lower latency and 2.5x lower energy than a fully digital SoA, and two orders of magnitude over prior analog/digital heterogeneous SoCs.

## Contributions
- Post-P&R heterogeneous cluster (8 RISC-V cores + PCM IMA + digital depth-wise accelerator) in GF 22nm FDX, 2.5 mm2
- Optimized IMA-to-cluster interface reaching 958 GOPS on MVMs (>90% of peak), an order of magnitude over bus-attached IMAs
- Bottleneck-layer benchmark: 11.5x speed and 9.5x energy over 8 cores, 2.6x/2.8x over previous cores+IMA design
- Scale-up study with Tile&Pack mapping for end-to-end MobileNetV2: 34 IMAs, 10.1 ms, 482 uJ

## Key claims (stable IDs)
- **2022_Garofalo_HeterogeneousIMCCluster_JETCAS#C1** — The heterogeneous cluster runs a MobileNetV2 bottleneck 11.5x faster and 9.5x more energy-efficiently than the 8 cores alone — _support:_ 11.5x perf, 9.5x energy — _loc:_ Abstract, Sec. V-C, Fig. 9
- **2022_Garofalo_HeterogeneousIMCCluster_JETCAS#C2** — IMA interface sustains >90% of peak MVM throughput — _support:_ 958 GOPS vs 1.008 TOPS peak (256x256x2 OPs/130 ns) — _loc:_ Sec. V-B
- **2022_Garofalo_HeterogeneousIMCCluster_JETCAS#C3** — End-to-end MobileNetV2 inference takes 10.1 ms and 482 uJ, requiring 34 256x256 crossbars (~30 mm2 of PCM) — _support:_ 34 IMAs, 0.83 mm2 each — _loc:_ Sec. VI, Table I
- **2022_Garofalo_HeterogeneousIMCCluster_JETCAS#C4** — Mixing programmable cores with analog and digital accelerators beats IMA+MCU designs by two orders of magnitude on MobileNetV2 — _support:_ Fig. 13: 423x vs IMA+MCU — _loc:_ Sec. VII, Fig. 13

## Results
- Peak 958 GOPS on 8b-4b MVMs, 6.39 TOPS/W peak (Table I)
- MobileNetV2: 99 inf/s, 0.482 mJ/inf (Table I); 10x faster and 2.5x less energy than Vega-like digital SoA
- Cluster area 2.5 mm2; each 256x256 PCM IMA 0.83 mm2; ~1/3 area IMA, ~1/3 TCDM
- Programming IMA is 20-30x slower than one MVM, so layers larger than a crossbar are split over multiple IMAs rather than reprogrammed

## Key numbers
- tech_node: 22nm FDX (digital); 14nm PCM IMA scaled
- array_size: 256x256
- energy_eff: 6.39 TOPS/W peak (8b-4b)
- throughput: 958 GOPS peak MVM; 99 inf/s MobileNetV2
- bits_weight: 4b signed (PCM)
- bits_adc: 8b

## Datasets / benchmarks
MobileNetV2 (bottleneck layers and end-to-end)

## Limitations
- IMA modelled from 14nm silicon scaled to 22nm, not fabricated as a whole system
- No accuracy evaluation: analog noise, drift and quantization effects on MobileNetV2 accuracy are not simulated
- Activation access energy/time from on-chip memory not modelled in the scale-up
- 34 crossbars (~30 mm2) is a large area cost; only point-wise layers mapped to analog
- Only CNN workload; no transformers/LMs

## Remarks
A system-level paper that shifts the focus from peak TOPS/W to end-to-end utilization, showing that non-MVM operators and data movement dominate once MVMs are accelerated. Evidence is post-P&R digital plus extrapolated analog, so absolute numbers are indicative. The Tile&Pack mapping and the Amdahl argument carry over to transformers, where attention and nonlinear ops would be the equivalent heterogeneous bottleneck; there is no language-model content.

## Cites (in collection, 14)
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "This approach has been demonstrated to solve linear equations [26] and in DNN inference and even training tasks [23], showing limited error in the computation and much higher efficiency compared to traditional approaches [2]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "Considering ReRAM-based IMC, Chen et al. [12] demonstrate significant computing parallelism, performing 8k MAC operations simultaneously."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "Charge-based memory technologies (e.g. SRAM [10], DRAM, Flash) and non-volatile (NV) resistive memory technologies [11] (e.g. ReRAM [12] PCM [2] and MRAM [13]) both serve as computing substrates for analog in-memory computing."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _contrasts/critiques_: "The silicon prototype presented in [6] integrates a charge-domain compute-in-memory unit supporting 1to8-bit×1to8-bit matrix-vector multiplications, into a tiny RISC-V CPU enriched with a direct memory access controller (DMA) and a set of peripherals."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Note that typically 2 PCM devices are used to denote a signed weight [32]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Several demonstrations of AIMC-based architectures have appeared in the field of Deep Neural Network (DNN) inference acceleration, showing outstanding peak energy efficiency in the order of hundreds of TOPS/W [1, 2]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Other works show ReRAM-based IMC arrays as dense as 2Mb [24] or 4Mb [25], with peak energy efficiencies in the range of 120-200 TOPS/W within a power envelope of few milliwatts, suitable for tiny edge AI devices."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _data/numbers_: "The programming of the IMA is done in a diagonal [27] or row-wise [39] fashion, therefore takes considerably larger time (20× to 30× higher) than merely performing a parallel MVM."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _uses-method-or-tool_: "Khaddam-Aljameh et al. [27] recently presented a state-of-the-art 256×256 PCM-based IMC core targeting DNN inference, fabricated in 14nm, showing energy efficiency of 10.5 TOPS/W and performance density of 1.59 TOPS/mm2 on inference tasks of multi-layer perceptrons and ResNet9 models trained on MNIST and CIFAR-10 datasets, with comparable accuracies as software baseline."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 1)
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _extends/builds-on_: "Each cluster also includes a nvAIMC Accelerator (IMA) sharing the same multi-banked memory as the CORES for efficient communication, similarly to the architecture presented in Garofalo et al. [9]."

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2022_Garofalo_HeterogeneousIMCCluster_JETCAS.pdf](../../03_Crossbar_Accelerator_Architectures/2022_Garofalo_HeterogeneousIMCCluster_JETCAS.pdf)
- Full text: [../fulltext/2022_Garofalo_HeterogeneousIMCCluster_JETCAS.txt](../fulltext/2022_Garofalo_HeterogeneousIMCCluster_JETCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jetcas.2022.3170152
