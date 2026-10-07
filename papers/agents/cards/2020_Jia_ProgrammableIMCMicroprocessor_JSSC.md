---
id: W2899641901
key: 2020_Jia_ProgrammableIMCMicroprocessor_JSSC
title: "A Programmable Heterogeneous Microprocessor Based on Bit-Scalable In-Memory Computing"
short: "Princeton Programmable IMC Processor"
year: 2020
venue: "JSSC"
venue_full: "IEEE Journal of Solid-State Circuits, vol. 55, no. 9 (2020)"
authors: "Hongyang Jia, Hossein Valavi, Yinqi Tang, Jintao Zhang, Naveen Kumar Verma"
category: "02 Fabricated Chips & Macros"
devices: ["SRAM-analog", "Charge/Capacitor"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "heterogeneous-analog-digital", "adc-dac", "bit-slicing", "pruning-sparsity", "energy-efficiency", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 1
citations_overall: 227
priority_score: 9.18
doi: "https://doi.org/10.1109/jssc.2020.2987714"
pdf: "../../02_Fabricated_Chips_and_Macros/2020_Jia_ProgrammableIMCMicroprocessor_JSSC.pdf"
fulltext: "../fulltext/2020_Jia_ProgrammableIMCMicroprocessor_JSSC.txt"
---

# Princeton Programmable IMC Processor

**A Programmable Heterogeneous Microprocessor Based on Bit-Scalable In-Memory Computing** — IEEE Journal of Solid-State Circuits, vol. 55, no. 9 (2020) (2020)

## TL;DR
A 65 nm programmable microprocessor integrating a 590 kb charge-domain SRAM in-memory-computing unit with a near-memory digital datapath and a RISC-V CPU, measured at 152/297 1b-TOPS/W and CIFAR-10 accuracy of 89.3% (1b) and 92.4% (4b).

## Summary
Analog in-memory computing has limited robustness, scale and programmability. This work builds on charge-domain IMC (Valavi, VLSI 2018), where each 6T SRAM bit cell adds two PMOS transistors and a 1.2 fF MOM capacitor to do XNOR multiplication in the digital voltage domain and accumulate charge across a column, so that precision is set by capacitor geometry rather than transistor variation. The 590 kb compute-in-memory unit (CIMU) has 16 (4x4) banks and supports matrix dimension up to 256 x 2304 (input vector up to 3x3x256 for CNN filters), with banks activity-gated for configurable dimensionality. Multi-bit (1-8 b) matrix and input elements are handled with a bit-parallel/bit-serial scheme: matrix bits map to parallel columns, input bits are applied serially, each column feeds an 8-bit SAR ADC and a binarising analog batch-norm block (6-bit DAC reference), and a digital near-memory datapath performs barrel shifting, scaling, batch norm and activation. Tight CPU coupling (standard memory space, word-to-bit reshaping buffer, sparsity/AND-logic controller, DMA) provides programmability, and zero-valued inputs are masked for sparsity-proportional energy. Measurements on the chip show linear ADC/ABN transfer functions across 256 columns, bit-true multi-bit MVM with expected SQNR, and CIFAR-10 networks with 1b and 4b activations/weights. The supplied text appears to be the shorter conference version (65 nm microprocessor with configurable bit-scalable accelerator); the JSSC journal details are not reproduced.

## Contributions
- 590 kb charge-domain IMC accelerator integrated in a programmable RISC-V processor in 65 nm CMOS
- Bit-parallel/bit-serial scheme giving 1-8 b scalable precision with linear energy and throughput scaling
- Per-column 8-bit ADC and analog batch-norm interface to a configurable near-memory datapath
- Sparsity-proportional energy via input masking, plus SQNR and bandwidth design analysis
- Chip measurements and CIFAR-10 demonstrations at software-equivalent accuracy

## Key claims (stable IDs)
- **2020_Jia_ProgrammableIMCMicroprocessor_JSSC#C1** — Chip reaches 152/297 1b-TOPS/W and 4.7/1.9 1b-TOPS at VDD of 1.2/0.85 V — _support:_ measured — _loc:_ Abstract, Fig. 11
- **2020_Jia_ProgrammableIMCMicroprocessor_JSSC#C2** — CIFAR-10 accuracy matches ideal software: 92.4% (4b, ideal 92.7%) and 89.3% (1b, ideal 89.8%) — _support:_ measured on chip — _loc:_ Fig. 11
- **2020_Jia_ProgrammableIMCMicroprocessor_JSSC#C3** — Energy per classification is 5.31 uJ (1b) at 176 images/s and 105.2 uJ (4b) at 23 images/s — _support:_ measured — _loc:_ Sec. 4, Fig. 11
- **2020_Jia_ProgrammableIMCMicroprocessor_JSSC#C4** — 8-bit ADC emulates integer compute exactly when column levels <=255 and gives SQNR near integer compute for 2-6 b operands — _support:_ simulated SQNR vs BA, BX, N — _loc:_ Sec. 3, Fig. 7
- **2020_Jia_ProgrammableIMCMicroprocessor_JSSC#C5** — Mixed-signal BP/BS scales energy/throughput linearly with bits instead of exponentially — _support:_ design argument — _loc:_ Sec. 2

## Results
- 152/297 1b-TOPS/W and 4.7/1.9 1b-TOPS at 1.2/0.85 V (die 13.5 mm2 total)
- CIFAR-10 1b: 89.3% (ideal 89.8%), 5.31 uJ/image, 176 fps; 4b: 92.4% (ideal 92.7%), 105.2 uJ/image, 23 fps
- CIMA column energy 20.4 pJ (1.2 V) / 9.7 pJ (0.85 V); ADC 3.56/1.79 pJ per column
- 8-bit ADC adds 18% area and 15% energy to a CIMA column
- XNOR/AND compute and input broadcast are ~50% of CIMA energy, which sparsity masking reduces

## Key numbers
- tech_node: 65nm
- array_size: 590 kb CIMA, 256 x 2304 max
- energy_eff: 152/297 1b-TOPS/W (1.2/0.85 V)
- throughput: 4.7/1.9 1b-TOPS
- accuracy: 92.4% (4b) / 89.3% (1b) CIFAR-10
- bits_weight: 1-8b
- bits_adc: 8b

## Datasets / benchmarks
CIFAR-10

## Limitations
- SRAM charge-domain IMC, not NVM; relevance to analog NVM crossbars is architectural (heterogeneous IMC+NMC integration, bit-scalability)
- Small CIFAR-10 CNNs (9 layers); no transformers or language models
- 8-bit ADC cannot resolve N+1 levels for N up to 2304, so SQNR depends on N and sparsity
- Binary multiply per cell; multi-bit costs scale linearly with bit-serial cycles
- Weight loading is slow (up to ~18k cycles) and CIMU speed may require dedicated high-bandwidth interfaces

## Remarks
A landmark demonstration that analog IMC can be made precise and programmable by using capacitors instead of transistor currents, and by pairing the array with a digital near-memory datapath and CPU. Although SRAM-based, its heterogeneous analog+digital abstraction anticipates the DPU/AIMC-tile split used by NVM-based LLM accelerators in the collection. Evidence is measured silicon, but only on small CNNs, and the supplied document is the short conference text rather than the full JSSC paper.

## Cites (in collection, 1)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 13)
- [2021_Chen_CAP-RAM_JSSC](2021_Chen_CAP-RAM_JSSC.md) CAP-RAM (2021) — _baseline/comparison_: "Compared with recent IMC architectures, Jia et al. [26] show higher accuracy since it uses 8-bit ADCs and utilizes VGG-like network with 7.04 times more operations than ResNet-20."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _contrasts/critiques_: "This allows the execution of shift-and-add operations within the ADC at a minimal overhead, avoiding dedicated multi-bit adders [42]–[44]."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _contrasts/critiques_: "The silicon prototype presented in [6] integrates a charge-domain compute-in-memory unit supporting 1to8-bit×1to8-bit matrix-vector multiplications, into a tiny RISC-V CPU enriched with a direct memory access controller (DMA) and a set of peripherals."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "One way to address the limitations of standalone AIMCbased accelerators is to add local CPUs [8, 9, 10, 11]."
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _background_: "For this reason, few recent works [8–10] proposed the integration of nvAIMC cores into digital System-on-Chips (SoC), exploiting a mix of nvAIMC cores and more flexible specialized and programmable digital processors."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "This enables approximate MVM computation directly in-memory, by applying activation vectors (as voltages or pulse durations) to the crossbar array, and then reading out analog physical quantities (instantaneous current or accumulated charge)16–18."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _baseline/comparison_: "Macro A [16] reuses analog outputs across different columns by summing them on wires."
- [2024_Yoshioka_CRCIM_JSSC](2024_Yoshioka_CRCIM_JSSC.md) CR-CIM (2024) — _baseline/comparison_: "These metrics are 23 dB and 14 dB better than the previously reported charge-based CIMs [4,5], showing that CR-CIM and CB techniques lead to high compute accuracy."
- [2025_Zhang_ASiM_TVLSI](2025_Zhang_ASiM_TVLSI.md) ASiM (2025) — _extends/builds-on_: "Jia [24] used randomly generated weight and activation vectors, comparing the post-quantization output to the ideal full-precision output to measure the SQNR of a real device"
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "Recent studies employing capacitor-based unit cells have demonstrated that such architectures exhibit strong robustness against process and device-level variations23,47."
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022)
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2020_Jia_ProgrammableIMCMicroprocessor_JSSC.pdf](../../02_Fabricated_Chips_and_Macros/2020_Jia_ProgrammableIMCMicroprocessor_JSSC.pdf)
- Full text: [../fulltext/2020_Jia_ProgrammableIMCMicroprocessor_JSSC.txt](../fulltext/2020_Jia_ProgrammableIMCMicroprocessor_JSSC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jssc.2020.2987714
