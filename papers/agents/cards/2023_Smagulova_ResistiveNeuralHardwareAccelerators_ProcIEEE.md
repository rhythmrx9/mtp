---
id: W3197197128
key: 2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE
title: "Resistive Neural Hardware Accelerators"
short: "Resistive Neural Hardware Accelerators"
year: 2023
venue: "ProcIEEE"
venue_full: "Proceedings of the IEEE, vol. 111, 2023 (arXiv:2109.03934 preprint, 2021)"
authors: "Kamilya Smagulova, Mohammed E. Fouda, Fadi Kurdahi, Khaled N. Salama, Ahmed M. Eltawil"
category: "01 Surveys & Foundations"
devices: ["ReRAM"]
models: ["CNN", "MLP", "LSTM/RNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "crossbar-architecture", "dataflow-pipelining", "adc-dac", "peripheral-circuits", "chip-demo", "device-variation", "simulator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 20
citations_overall: 31
priority_score: 5.45
doi: "https://doi.org/10.1109/jproc.2023.3268092"
pdf: "../../01_Surveys_and_Foundations/2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.pdf"
fulltext: "../fulltext/2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.txt"
---

# Resistive Neural Hardware Accelerators

**Resistive Neural Hardware Accelerators** — Proceedings of the IEEE, vol. 111, 2023 (arXiv:2109.03934 preprint, 2021) (2023)

## TL;DR
Survey of many-core ReRAM crossbar DNN accelerators (ISAAC, PRIME, AEPE, PipeLayer, AtomLayer, Newton, CASCADE, PUMA/PANTHER) and fabricated ReRAM CIM macros, concluding that ADC/DAC, buffers and interconnect dominate cost and that fair metrics, standard benchmarks and device-aware CAD tools are missing.

## Summary
The survey (Proc. IEEE 2023; arXiv 2109.03934) reviews ReRAM-crossbar (RCA) based DNN accelerators as a response to the von Neumann bottleneck. Section 2 describes each architecture's tile/IMA organisation, how layers are assigned to crossbars, the pipeline and the peripherals (e.g. ISAAC: tiles with 12 IMAs, each with eight 128x128 RCAs, shared ADCs, per-array DAC and S&H, eDRAM buffers, c-mesh NoC). Section 3 compares them on area/power breakdown, utilisation and algorithm-to-hardware mapping efficiency across workloads (VGG, ResNet, AlexNet, MNIST nets) at 32 nm or 65 nm technology assumptions. Section 4 tabulates fabricated ReRAM CIM macros (65 nm 1 Mb ISSCC'18, 55 nm 1 Mb ISSCC'19, 22 nm 2 Mb ISSCC'20, 130 nm analog macro, 40 nm 4T2R) by cell, ADC precision and TOPS/W. Section 5 covers non-idealities (IR drop, defects/SAF, I-V nonlinearity, update asymmetry) and mitigation groups (retraining, matrix permutation, post-processing correction) and simulation frameworks. No language models or transformers are discussed; the scope is CNN/MLP/RNN-era accelerators. It is an architecture-centric snapshot with no new experiments.

## Contributions
- Unified description of seven many-core ReRAM accelerators (ISAAC, PRIME, AEPE, PipeLayer, AtomLayer, Newton, CASCADE) plus PUMA/PANTHER, with pipelining and mapping explanations
- Comparison tables of technology, workloads, area/power distribution, utilisation and efficiency
- Summary table of fabricated ReRAM-CIM macros (capacity, subarray, cell, ADC precision, TOPS/W, accuracy)
- Taxonomy of ReRAM non-idealities and mitigation methods, and a list of open gaps (metrics, benchmarks, CAD tools)

## Key claims (stable IDs)
- **2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE#C1** — ISAAC outperforms digital DaDianNao in throughput, energy and computational density — _support:_ 14.8x, 5.5x and 7.5x improvements — _loc:_ Sec. 2.1
- **2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE#C2** — CASCADE's analog buffer arrays cut partial-sum accumulation energy versus digital accumulation — _support:_ up to 7.59x energy reduction — _loc:_ Sec. 2.7
- **2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE#C3** — Newton improves on ISAAC through smaller eDRAM buffers, adaptive ADCs and Karatsuba/Strassen tricks — _support:_ 51% power efficiency and 2.2x computational efficiency improvement — _loc:_ Sec. 2.6
- **2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE#C4** — Reported accelerator metrics are not comparable because they are given at maximum utilisation and for only 1-2 workloads; no industry-standard benchmark exists for ReRAM accelerators — _support:_ Conclusion text — _loc:_ Sec. 6

## Results
- ISAAC: 14.8x throughput, 5.5x energy, 7.5x computational density vs DaDianNao (Sec. 2.1)
- PipeLayer: 142.9 GOPS/W despite high RCA write energy (Sec. 2.4)
- Newton: +51% power efficiency, 2.2x computation efficiency over ISAAC (Sec. 2.6)
- CASCADE: up to 7.59x less energy than digital partial-sum accumulation (Sec. 2.7)
- Macro table: 65 nm 1 Mb 25.42 TOPS/W (1-bit in, ternary weight, 3-bit out); 55 nm 1 Mb 21.9 TOPS/W, CIFAR-10 88.52% (Sec. 4 table)
- AtomLayer: average 42.45x speedup and 7.17x energy saving vs GPU platforms (Sec. 3)

## Key numbers
- tech_node: 32 nm / 65 nm (accelerator models); 130 nm-22 nm (macros)
- array_size: 128x128 (ISAAC)
- energy_eff: 25.42 TOPS/W (65 nm macro)
- accuracy: 88.52% CIFAR-10 (55 nm macro)
- bits_adc: 3b (macros)

## Datasets / benchmarks
MNIST, CIFAR-10, VGG-19, ResNet-152, AlexNet, DCGAN

## Limitations
- Literature review only; numbers are taken from the original papers under differing technology assumptions
- Covers CNN/MLP/RNN accelerators only; no transformers or language models
- Focus on ReRAM, other NVMs (PCM, FeFET, MRAM) barely treated
- Text extraction of the large comparison tables is flattened, so per-cell values are hard to verify

## Remarks
A useful, architecture-centric tour of the ISAAC lineage with a clear message that peripherals and data movement, not the crossbars, set efficiency. It predates the transformer/LLM wave, so it gives background for mapping rather than guidance on language models. In the collection it is the natural companion to ISAAC, PRIME, PipeLayer, CASCADE and PUMA/PANTHER and to the ReRAM macro papers it tabulates.

## Cites (in collection, 20)
- [2018_Kim_NonlinearIVAwareDNN_JETC](2018_Kim_NonlinearIVAwareDNN_JETC.md) Nonlinear-IV NN (2018) — _background_: "This exponential nonlinearity makes the VMM operation inaccurate, which deteriorates the training performance [119]."
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "Matrix permutation [100, 103, 107, 108] can be based on row permutation [100, 107] and neuron permutation [100, 107]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Unlike PRIME and ISAAC, PipeLayer supports both the training and inference of neural networks [36]."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "The first one is retraining [100–103]."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "Nonlinear and asymmetric update dynamics in some RRAM devices hinder large-scale deployment in neural networks [122]."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _background_: "A 65 nm ReRAm macro was designed to accelerate a binary convolution neural network (CNN) [39]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "PUMA is a spatial processor and provides more flexibility and scalability to accelerate a wide range of workloads and different types of data [41]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _background_: "In [106], the authors estimated the error contributed by SAF cells and recovered accuracy by additional CMOS circuits."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _data/numbers_: "The CASCADE architecture implemented an analog partial sum accumulation and achieved a peak performance of 101 GOPS/mm2 [38]."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "To implement training, a Programmable Architecture for Neural Network Training Harnessing Energy-efficient ReRAM (PANTHER) was introduced and evaluated on PUMA [40]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "In a fabricated 22 nm 2 Mb ReRAM-CIM macro [65], the precision of input data was increased from binary to 4-bit."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _background_: "A Fully Integrated Analog ReRAM-based 130 nm macro used a 2T2R cell, which decreased the effect of the IR drop by decreasing the accumulative SL current [66]."
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020) — _background_: "In a knowledge distillation (KD)-based retraining, the teacher network transfers 'knowledge' to a student network [102]."
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020) — _background_: "They also provide a simplified estimation of power, area, and latency [141, 142]."
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020) — _background_: "However, even the small value of the wire resistance has a significant effect on the weights stored in RCA [112–114]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "It outperformed the fully digital DaDianNao with improvements of 14.8x, 5.5x, and 7.5x in throughput, energy, and computational density, respectively [34]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Around the same time, the architecture of PRIME was introduced [35]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "A Reconfigurable 4T2R ReRAM Computing In-Memory Macro on a 40 nm process [67] utilized a 4T2R cell, which allowed for row-wise memory access."
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021)

## Cited by (in collection, 1)
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _background_: "Compute-In-Memory (CIM) neural network accelerators have emerged as promising architectures for achieving energyefficient AI processing [2–6]."

## Files
- PDF: [../../01_Surveys_and_Foundations/2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.pdf](../../01_Surveys_and_Foundations/2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.pdf)
- Full text: [../fulltext/2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.txt](../fulltext/2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jproc.2023.3268092
