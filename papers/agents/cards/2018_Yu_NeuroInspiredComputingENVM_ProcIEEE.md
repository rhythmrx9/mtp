---
id: W2785141883
key: 2018_Yu_NeuroInspiredComputingENVM_ProcIEEE
title: "Neuro-Inspired Computing With Emerging Nonvolatile Memorys"
short: "Yu eNVM Neuro-Inspired Review"
year: 2018
venue: "ProcIEEE"
venue_full: "Proceedings of the IEEE, vol. 106, no. 2, pp. 260-285 (2018)"
authors: "Shimeng Yu"
category: "01 Surveys & Foundations"
devices: ["PCM", "ReRAM", "FeFET", "Flash", "Generic-NVM"]
models: ["MLP", "CNN", "SNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "crossbar-architecture", "analog-mvm", "device-variation", "on-chip-training", "simulator", "quantization", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 30
cites_in_collection: 5
citations_overall: 1168
priority_score: 9.61
doi: "https://doi.org/10.1109/jproc.2018.2790840"
pdf: "../../01_Surveys_and_Foundations/2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.pdf"
fulltext: "../fulltext/2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.txt"
---

# Yu eNVM Neuro-Inspired Review

**Neuro-Inspired Computing With Emerging Nonvolatile Memorys** — Proceedings of the IEEE, vol. 106, no. 2, pp. 260-285 (2018) (2018)

## TL;DR
Proc. IEEE review of emerging-NVM synaptic devices (PCM, RRAM, ferroelectric, floating-gate) and crossbar architectures for neuro-inspired computing, concluding via NeuroSim benchmarking that device nonlinearity (>1) and on/off ratio (<10) make online training poor while offline-trained inference is the near-term target.

## Summary
The paper reviews why von-Neumann/SRAM-based accelerators are limited by on-chip memory and motivates eNVM crossbars (4-12 F^2 cells) for parallel weighted-sum. It categorises hardware design options (digital vs analog, spiking vs non-spiking, online vs offline training; Table 1) and lists desirable synaptic-device metrics (Table 2: multilevel states, update nonlinearity/asymmetry, variation, endurance, energy). It surveys material systems with analog conductance tuning (PCM, RRAM, ferroelectric FET/tunnel junction, floating-gate/NOR flash). It then covers array architectures (1T1R, 2-terminal with selectors, pseudo-crossbar, 3-D), peripheral/neuron circuits, and prototypes such as IBM's 500x661 2-PCM-per-synapse MNIST array (164,885 synapses) and Yu's 16-Mb binary RRAM chip. The device-circuit-algorithm co-design section introduces ASU's NeuroSim C++ circuit macromodel used to benchmark a two-layer MLP on MNIST with device parameters extracted from literature (Table 3), and hybrid-precision training with binary weights (Table 4). The outlook argues that inference-only with offline training is the most promising near-term use and that large-scale monolithic eNVM+CMOS prototypes are needed.

## Contributions
- Taxonomy of neuromorphic hardware design options and a device-requirement checklist for synaptic devices
- Survey of PCM, RRAM, ferroelectric and floating-gate analog synapses with array-level prototypes
- NeuroSim-based device-to-system benchmarking of literature devices for online MNIST training (Table 3) and target specs
- Analysis of IR-drop, selector and precision constraints on array scaling, with binary/low-precision NN as interim solution

## Key claims (stable IDs)
- **2018_Yu_NeuroInspiredComputingENVM_ProcIEEE#C1** — Weight-update variation above ~2% overwhelms the deterministic backprop update and harms learning accuracy — _support:_ 'too large variation (>2%) overwhelms the deterministic update amount' — _loc:_ Sec. V-B
- **2018_Yu_NeuroInspiredComputingENVM_ProcIEEE#C2** — With 40 nm wire width, eNVM R_ON must exceed ~10 kOhm (training) and ~500 kOhm (inference) to avoid IR-drop accuracy loss — _support:_ 'should be higher than 10 and 500 kOhm' — _loc:_ Sec. V-B
- **2018_Yu_NeuroInspiredComputingENVM_ProcIEEE#C3** — Literature synaptic devices give poor online-learning accuracy at 65 nm due to update nonlinearity >1 and on/off <10; training latency of ~1e8 s needs 10-100 ns pulses — _support:_ NeuroSim benchmark, Table 3 — _loc:_ Table 3, Sec. V-B
- **2018_Yu_NeuroInspiredComputingENVM_ProcIEEE#C4** — Binarising weights/neurons costs little accuracy — _support:_ MNIST MLP 99.00% to 98.77%; CIFAR-10 CNN 89.98% to 88.47% — _loc:_ Table 4, Sec. VI
- **2018_Yu_NeuroInspiredComputingENVM_ProcIEEE#C5** — Inference with offline training is the most promising near-term eNVM application — _support:_ needs only on/off ~100, ~100 levels, ~1000 cycle endurance — _loc:_ Sec. VI

## Results
- Binary MLP (784-512-512-512-10) on MNIST: 98.77% vs 99.00% FP; six-conv+3FC CNN on CIFAR-10: 88.47% vs 89.98% FP (Table 4)
- IBM 2-PCM/synapse 3-layer MLP with 164,885 synapses trained on 5000 MNIST samples (cited prototype, Sec. IV-B1)
- Programming energy: RRAM ~100 fJ-10 pJ, PCM ~10-100 pJ per pulse (Sec. III)
- Cited SRAM density 100-200 F^2 vs eNVM 4-12 F^2 per bit (Sec. I)

## Key numbers
- tech_node: 65nm (NeuroSim benchmark)
- array_size: 500x661 (cited IBM PCM); 256x256 (medium-scale demos)
- accuracy: 98.77% MNIST (binary MLP); 88.47% CIFAR-10 (binary CNN)
- bits_weight: 1b inference / 6b update accumulation

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Review of 2018 state of the art; no transformers or language models
- Training-centric benchmarking via simulation (NeuroSim, MLP/MNIST); inference-mapping detail is limited
- Many numbers are from cited works, not measured by the author
- Text extraction of figures/tables is partial (Table 3 contents not readable)

## Remarks
Heavily cited device-to-system reference that set the standard list of synaptic-device specs (nonlinearity, asymmetry, levels, variation) later quantified by NeuroSim. Its conclusion that offline-trained inference is the practical path anticipates later AIMC LM work, but it says nothing about attention or LLMs. Superseded for inference mapping by later Yu reviews and Sebastian et al. 2020 in the collection.

## Cites (in collection, 5)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Memristors featuring low variability bilayer Al2O3/TiO2-x were recently reported in [37] and [104]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _data/numbers_: "The sensitivity analysis [102] showed that eNVM-based ANN can be expected to be highly resilient to random effects (e.g., variability, yield, and stochasticity), but highly sensitive to gradient effects that act to steer all synaptic weights."
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017) — _background_: "A recent experimental demonstration of analog FeFET synaptic devices used the gate last fabrication process flow of n-channel FeFETs [88], as shown in Fig. 6."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "Recently, architectural simulator platforms (e.g., PRIME [118], ISAAC [119], and Harmonica [120]) have been developed to support system-level design of neuromorphic accelerators, however they have limited considerations at the aforementioned nonideal device properties (i.e., they only considered the weight precision and/or variation)."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "Recently, architectural simulator platforms (e.g., PRIME [118], ISAAC [119], and Harmonica [120]) have been developed to support system-level design of neuromorphic accelerators, however they have limited considerations at the aforementioned nonideal device properties (i.e., they only considered the weight precision and/or variation)."

## Cited by (in collection, 30)
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018) — _background_: "With renewed interest in deep learning, it gained attention again as a possible solution to accelerate the required computations [26–28]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "This results in stringent requirements on the device granularity, asymmetry and linearity to obtain accurate training109,112, and high device endurance is critical."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _background_: "To overcome the memory bottleneck, many researchers show interest in resistive crossbar arrays for the computing-in-memory feature [1, 8, 14, 21, 25, 41]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "To that end, nonvolatile memory (NVM) technologies [19, 20], such as phase-change memory (PCM) [21], resistive random access memory (RRAM) [22, 23], and spintronics [24], offer immense promise as an alternative to CMOS due to their high storage density and the ability to perform massively parallel in situ MVM operations."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "resistive-random-access-memory-(ReRAM)-based PIM (R2 PIM) accelerators have gained extensive research interest due to ReRAM's high density (e.g. 25x-50x higher over SRAM [71, 79])."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _background_: "To solve the bottleneck of extensive data transfer in the conventional von Neumann architectures, compute-in-memory (CIM) has emerged as a promising paradigm for designing the machine learning hardware accelerator [1]."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "A major advantage of IMC is the capability to execute matrix-vector multiplication (MVM) in parallel on multiple rows and columns of a memory array, which allows for a strong acceleration of neural networks [3]-[7]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "Nonlinear and asymmetric update dynamics in some RRAM devices hinder large-scale deployment in neural networks [122]."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _background_: "For accurate VMM operation, synaptic devices are required, which can precisely adjust the conductance states via analog conductance modulation (5, 11, 12)."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "By integrating the computations into memory arrays, mixed-signal compute-in-memory architectures have shown impressive abilities in boosting the throughput and energy efficiency of deep learning algorithms [1]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _data/numbers_: "It has been shown that On-resistance in the range of 100-200 kΩ leads to minimal IR drop for moderate crossbar array sizes (such as 64 x 64 or 128 x 128) [36]."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _uses-method-or-tool_: "We chose the zero-centered normal distribution to model the noise caused by nonideal properties like variation, nonlinearity, and asymmetry, following [65]."
- [2023_Cao_RRAMPoolFormer_ISCAS](2023_Cao_RRAMPoolFormer_ISCAS.md) RRAM-PoolFormer (2023) — _uses-method-or-tool_: "The two-cell-one-weight method depicted is thus used [16]."
- [2026_Xiao_RoboPIM_TCAD](2026_Xiao_RoboPIM_TCAD.md) RoboPIM (2026) — _background_: "FPGAs and ASICs suffer from high data movement [28] during memoryintensive LLM inference, and static/dynamic random access memory (SRAM) PIMs [29, 30] are limited by low density and significant leakage/refresh power, which are prohibitive for energy-constrained robotics."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022)
- [2021_Nikam_PassiveRRAMLSTM_TED](2021_Nikam_PassiveRRAMLSTM_TED.md) Passive RRAM LSTM (2021)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2025_Li_CIMLLMDataflow_ISVLSI](2025_Li_CIMLLMDataflow_ISVLSI.md) CIM-LLM Dataflow (2025)

## Files
- PDF: [../../01_Surveys_and_Foundations/2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.pdf](../../01_Surveys_and_Foundations/2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.pdf)
- Full text: [../fulltext/2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.txt](../fulltext/2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jproc.2018.2790840
