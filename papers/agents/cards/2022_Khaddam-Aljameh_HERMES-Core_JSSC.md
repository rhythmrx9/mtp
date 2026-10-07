---
id: W4210530509
key: 2022_Khaddam-Aljameh_HERMES-Core_JSSC
title: "HERMES-Core—A 1.59-TOPS/mm 2 PCM on 14-nm CMOS In-Memory Compute Core Using 300-ps/LSB Linearized CCO-Based ADCs"
short: "HERMES-Core"
year: 2022
venue: "JSSC"
venue_full: "IEEE Journal of Solid-State Circuits, vol. 57, no. 4, pp. 1027-1038 (2022)"
authors: "Riduan Khaddam-Aljameh, Miloš Stanisavljević, Jordi Fornt, Geethan Karunaratne, Matthias Brändli, Feng Liu, Abhairaj Singh, Silvia M. Müller, Urs Egger, Anastasios Petropoulos, Theodore A. Antonakopoulos, Kevin W. Brew et al."
category: "02 Fabricated Chips & Macros"
devices: ["PCM"]
models: ["MLP", "CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "adc-dac", "peripheral-circuits", "hardware-aware-training", "weight-mapping", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 20
cites_in_collection: 10
citations_overall: 140
priority_score: 10.06
doi: "https://doi.org/10.1109/jssc.2022.3140414"
pdf: "../../02_Fabricated_Chips_and_Macros/2022_Khaddam-Aljameh_HERMES-Core_JSSC.pdf"
fulltext: "../fulltext/2022_Khaddam-Aljameh_HERMES-Core_JSSC.txt"
---

# HERMES-Core

**HERMES-Core—A 1.59-TOPS/mm 2 PCM on 14-nm CMOS In-Memory Compute Core Using 300-ps/LSB Linearized CCO-Based ADCs** — IEEE Journal of Solid-State Circuits, vol. 57, no. 4, pp. 1027-1038 (2022) (2022)

## TL;DR
A 256x256 8T4R PCM in-memory compute core in 14-nm CMOS with 256 linearized CCO-based ADCs at 4-um pitch and an LDPU measures 1.008 TOPS, 1.59 TOPS/mm2 and 10.5 TOPS/W at 1 GHz, and runs MNIST MLP (98.3%) and CIFAR-10 ResNet-9 (85.6%) on two cores.

## Summary
Peripheral circuits (ADCs) dominate energy, latency and area of analog IMC, and prior PCM IMC systems lacked a complete chip. HERMES core integrates back-end-of-line mushroom PCM into 14-nm CMOS as a 256x256 array of 8T4R unit cells: each signed weight uses a positive device pair (G1+,G2+) and a negative pair (G1-,G2-), and inputs of both signs are applied as read pulses on VBLs at V_cm +/- V_read so all four sign quadrants are computed in one MVM step. Each of 256 column-wise ADCs is a current-controlled oscillator (CCO) with a frequency-linearization technique (peak ~3.3 GHz, 300 ps/LSB, >420 charge levels, >8 bit) feeding a ripple counter with variable increment size to perform shift-and-add inside the ADC; a digital calibration removes offset and gain mismatch between ADCs. A local digital processing unit applies per-column affine scaling and ReLU. Inputs can be applied as 8-bit PWM (128 ns integration) or bit-serial. Networks are trained in software with weight-noise injection and clipping (hardware-aware training), weights iteratively programmed to PCM, and inferred on two cores with an FPGA handling control and inter-layer transfer; ResNet-9 pooling is done in software.

## Contributions
- Fabricated 256x256 PCM IMC core on 14-nm CMOS with 8T4R unit cell supporting signed weights, signed MVM in one step and O(N) parallel programming
- Frequency-linearized CCO ADC with 300 ps/LSB resolution at 4-um pitch, built-in shift-and-add and bit-serial input support
- Digital ADC calibration procedure and statistical characterization of MVM accuracy (multi-bit PWM versus bit-serial)
- Measured inference on MNIST MLP and CIFAR-10 ResNet-9 using two cores, and comparison with prior IMC designs

## Key claims (stable IDs)
- **2022_Khaddam-Aljameh_HERMES-Core_JSSC#C1** — The core reaches 1.008 TOPS peak and 10.5 TOPS/W at 1 GHz, 0.8 V — _support:_ 1.59 TOPS/mm2 throughput density — _loc:_ Sec. V-C, Table I
- **2022_Khaddam-Aljameh_HERMES-Core_JSSC#C2** — Measured 8-bit MVM error is Gaussian with sigma = 1.94% for multi-bit PWM — _support:_ error PDF in Fig. 7(d) — _loc:_ Sec. IV-A, Fig. 7
- **2022_Khaddam-Aljameh_HERMES-Core_JSSC#C3** — Two-core system achieves 98.3% on MNIST and 85.6% on CIFAR-10 (ResNet-9, 100,726 params) — _support:_ software 98.6% and 88.4% — _loc:_ Sec. V-B
- **2022_Khaddam-Aljameh_HERMES-Core_JSSC#C4** — ADC gain residual spread after calibration is 7.09% (sigma 2.48 MHz/uA) and static gain variations lie within +/-21% — _support:_ calibration measurement — _loc:_ Sec. III, Fig. 5

## Results
- Throughput 1.008 TOPS at 10.5 TOPS/W, 1.59 TOPS/mm2 (14 nm, 1 GHz, 0.8 V)
- MNIST 2-layer MLP (240 hidden) 98.3% on-chip vs 98.6% software (-0.3%)
- CIFAR-10 ResNet-9 85.6% on-chip vs 88.4% software (-2.8%)
- Relative weight programming error sigma 4.8% (MLP) and 5.3% (ResNet-9); iterative programming convergence 100% / 99.9%
- Throughput density above non-volatile ReRAM designs [24],[45] and slightly above SRAM+capacitor designs [44]; only a 4-bit 8T SRAM design is denser

## Key numbers
- tech_node: 14nm CMOS
- array_size: 256x256 (8T4R cells, 4 PCM per cell)
- energy_eff: 10.5 TOPS/W; 1.59 TOPS/mm2
- throughput: 1.008 TOPS at 1 GHz
- accuracy: 98.3% MNIST (MLP); 85.6% CIFAR-10 (ResNet-9)
- bits_weight: multi-level PCM, 4 devices per weight
- bits_adc: >8b CCO-based (300 ps/LSB)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Single core with FPGA control; only two cores and tiny networks (MLP, 100k-parameter ResNet-9)
- PCM inserted high in the BEOL so the cell footprint underuses 14-nm density
- Accuracy gap of 2.8% on CIFAR-10 attributed to programming error and ADC nonlinearity; no drift mitigation or long-term retention reported
- Pooling executed in software; energy efficiency measured on the MNIST experiment, not on the largest network
- Weight programming error limited by on-chip ADC read resolution

## Remarks
A foundational measured-silicon PCM core whose ADC design and per-column digital affine post-processing became the template for IBM's 64-core chip and for the crossbar model in AIHWKit-based HWA training. Evidence is strong for circuit-level claims (calibrated MVM error sigma 1.94%), but workloads are toy-scale, so no inference about transformers or language models can be drawn directly. Useful for understanding the ADC/accuracy bottleneck behind analog LM deployments.

## Cites (in collection, 10)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _contrasts/critiques_: "Prior to this, most of the demonstrations have been based on either simulation studies based on the measured characteristics of individual devices or on experiments based on PCM memory chips that were re-purposed for IMC operations [28]–[30]."
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _contrasts/critiques_: "This allows the execution of shift-and-add operations within the ADC at a minimal overhead, avoiding dedicated multi-bit adders [42]–[44]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "Prior to mapping the networks onto analog IMC cores, it is essential to perform a hardware-aware custom training in software as described in [30]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _contrasts/critiques_: "In addition, voltage-based A/D converters (ADCs) are mostly used [31] that require a voltage to current conversion, usually employing a large capacitor for integration [23], [32]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "In-memory computing (IMC) is an emerging non-von Neumann paradigm where computation is performed in the memory array itself [1], [2]."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _contrasts/critiques_: "In addition, voltage-based A/D converters (ADCs) are mostly used [31] that require a voltage to current conversion, usually employing a large capacitor for integration [23], [32]."
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020) — _background_: "The analog nature of the device, however, allows the encoding of more levels, the only limit being ADC precision and allowable programming time [35], [36]."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "Although experimental results on ReRAM-based IMC systems have already been demonstrated [23]–[25], complete IMC systems based on PCM crossbar arrays had been lacking till recently [26], [27]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "This allows the execution of shift-and-add operations within the ADC at a minimal overhead, avoiding dedicated multi-bit adders [42]–[44]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "Although experimental results on ReRAM-based IMC systems have already been demonstrated [23]–[25], complete IMC systems based on PCM crossbar arrays had been lacking till recently [26], [27]."

## Cited by (in collection, 20)
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _data/numbers_: "In this work, we assume an MVM to be executed in 130 ns as reported in Khaddam et al. [7]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _extends/builds-on_: "Furthermore, the internal current mirror, which drives the attached current-controlled oscillator (CCO) unit, contains trimming registers that allow matching the gain between the different ADCs per core and compensating nonlinearity in their transfer function (ref 18)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "Analog in-memory computing (analog-AI)3–7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "AIMC accelerators that are based on resistive memory device technologies such as Phase Change Memory (PCM)5–8 , Resistive Random Access Memory (ReRAM)9–12 , and Magnetic Random Access Memory (MRAM)13 , have shown great promise in accelerating and reducing the power consumption of deep learning systems."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Finally, the most advanced prototypes exploit the time-encoding scheme, which simplifies the DAC design and allows one DAC per channel, without losing resolution of the input vector."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _contrasts/critiques_: "However, most previous works [11]–[13], [28] require hardware-aware training, which is non-trivial, if not prohibitive for LLMs with large number of parameters."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _data/numbers_: "Programming memristive devices typically requires high voltages (~2 V for PCM, 3–4 V for RRAM) and 100–500-μA currents, necessitating thick oxide drivers and large select transistors43, which further limits array size."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _background_: "By exploiting such weight stationarity over short timespans with Volatile Memories (VMs) – SRAM or e-DRAM [6, 8] – or over longer timespans with slower, finite-endurance NonVolatile Memories (NVMs) – Flash [9], Resistive-RAM [10], or phase-change memory (PCM) [11, 12] – such CIM approaches can offer high throughput, low latency, and high energy-efficiency [6, 7, 8]."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _background_: "Conversion is performed in parallel using dedicated Current-Controlled Oscillator (CCO)-based Analog-to-Digital Converters (ADCs) [13]."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _uses-method-or-tool_: "Khaddam-Aljameh et al. [27] recently presented a state-of-the-art 256×256 PCM-based IMC core targeting DNN inference, fabricated in 14nm, showing energy efficiency of 10.5 TOPS/W and performance density of 1.59 TOPS/mm2 on inference tasks of multi-layer perceptrons and ResNet9 models trained on MNIST and CIFAR-10 datasets, with comparable accuracies as software baseline."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "PCM devices have the potential to scale to nanoscale dimensions and can be integrated in the back-end of a CMOS chip [13]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "Potential for scalability was shown in [175] in which a convolutional network with 9 layers was demonstrated using the CIFAR10 dataset."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _uses-method-or-tool_: "Note that such ADC conversion using a scale and bias per column is already available in prototypes44 but has not previously been incorporated into studies on HWA training."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _uses-method-or-tool_: "Each core comprises a crossbar array of 256x256 PCM-based unit-cells along with a local digital processing unit [45]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Using resistive crossbar arrays to compute an MVM in-memory has been suggested early on46, and multiple prototype chips where MVMs of DNNs during inference are accelerated have been recently described6-9,11,47."
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)
- [2022_Jiang_ENNA_TCAS-I](2022_Jiang_ENNA_TCAS-I.md) ENNA (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2022_Khaddam-Aljameh_HERMES-Core_JSSC.pdf](../../02_Fabricated_Chips_and_Macros/2022_Khaddam-Aljameh_HERMES-Core_JSSC.pdf)
- Full text: [../fulltext/2022_Khaddam-Aljameh_HERMES-Core_JSSC.txt](../fulltext/2022_Khaddam-Aljameh_HERMES-Core_JSSC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jssc.2022.3140414
