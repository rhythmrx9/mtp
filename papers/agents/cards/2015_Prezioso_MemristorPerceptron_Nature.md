---
id: W1542981317
key: 2015_Prezioso_MemristorPerceptron_Nature
title: "Training and operation of an integrated neuromorphic network based on metal-oxide memristors"
short: "Prezioso Memristor Perceptron"
year: 2015
venue: "Nature"
venue_full: "Nature, vol. 521 (2015)"
authors: "M. Prezioso, Farshad Merrikh‐Bayat, Brian D. Hoskins, Gina C. Adam, Konstantin K. Likharev, Dmitri B. Strukov"
category: "02 Fabricated Chips & Macros"
devices: ["Memristor(generic)", "ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "analog-mvm", "on-chip-training", "device-variation", "weight-mapping", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 34
cites_in_collection: 0
citations_overall: 3032
priority_score: 11.16
doi: "https://doi.org/10.1038/nature14441"
pdf: "../../02_Fabricated_Chips_and_Macros/2015_Prezioso_MemristorPerceptron_Nature.pdf"
fulltext: "../fulltext/2015_Prezioso_MemristorPerceptron_Nature.txt"
---

# Prezioso Memristor Perceptron

**Training and operation of an integrated neuromorphic network based on metal-oxide memristors** — Nature, vol. 521 (2015) (2015)

## TL;DR
First experimental demonstration of a transistor-free 12x12 Al2O3/TiO2-x memristor crossbar trained in situ (Manhattan update rule) as a 10x3 single-layer perceptron that classifies 3x3-pixel images into 3 classes perfectly after ~15 epochs on average.

## Summary
Metal-oxide memristors with nonlinear I-V curves permit transistor-free dense crossbars, but device-to-device variability (notably forming voltage) had forced earlier demonstrations to use per-device transistors or off-chip wiring. The authors reduce variability with optimized Al2O3(4 nm)/TiO2-x(30 nm) stacks (low-temperature sputtering for 3D integration) and thicker electrodes (wire resistance ~600-800 ohm), forming each device individually inside an integrated 12x12 crossbar (200x200 nm2 devices). A single-layer perceptron with 10 inputs (9 pixels + bias) and 3 outputs is mapped with two memristors per synapse (30 weights, 60 devices): inputs are +/-0.1 V, external electronics hold virtual ground on columns and subtract adjacent half-column currents so Ohm's law gives the differential weighted sum; conductances were 10-100 uS (currents of a few uA). Activation functions and error calculation are done off-chip. Training in situ uses the Manhattan Update rule (batch coarse-grain delta rule) implemented by fixed-amplitude +/-1.3 V set/reset pulses per half-column; the 30-pattern set (3 stylized letters with 1-pixel noise) is used for both training and testing.

## Contributions
- First integrated, transistor-free metal-oxide memristor crossbar neural network operated and trained
- Low-variability Al2O3/TiO2-x device stack with strong I-V nonlinearity and >4 orders ON/OFF in isolated devices
- In-situ training with Manhattan Update using fixed-amplitude pulses, without an external model
- Differential two-memristor synapse with external virtual-ground sensing for signed weights

## Key claims (stable IDs)
- **2015_Prezioso_MemristorPerceptron_Nature#C1** — A 12x12 transistor-free memristor crossbar can be trained in situ to classify 3x3 binary images into 3 classes with perfect accuracy. — _support:_ perfect classification reached on average after ~15 epochs when initialised near 35 uS — _loc:_ Fig. 4; main text
- **2015_Prezioso_MemristorPerceptron_Nature#C2** — Optimized devices show ON/OFF >4 orders of magnitude (at 0.1 V), >10x I-V nonlinearity, endurance >=5000 cycles, retention >=10 years (estimated), forming <2 V and switching ~1.5 V. — _support:_ Figs. S1, S3-S4 — _loc:_ Memristor Fabrication, Forming and Characterization
- **2015_Prezioso_MemristorPerceptron_Nature#C3** — Best performance requires initialising conductances mid-range (~35 uS) because switching dynamics make step size state-dependent. — _support:_ dG +60/-5 uS at G=20 uS vs +24/-55 uS at G=65 uS — _loc:_ Fig. 1c, S7b

## Results
- 10x3 perceptron, 30 weights on 60 memristors; effective conductances 10-100 uS, column currents of a few uA
- Perfect classification of 30 patterns after ~15 training epochs on average
- In-crossbar ON/OFF ratio <100 versus isolated devices (leakage through other crosspoints, lower switching voltages)
- Set pulse 1.3 V / reset pulse -1.3 V fixed-amplitude updates

## Key numbers
- tech_node: 200x200 nm2 devices; 248 nm DUV lithography
- array_size: 12x12 (10x3 weights used, 60 memristors)
- accuracy: 100% (30-pattern train=test set)
- bits_weight: analog conductance 10-100 uS (differential pairs)

## Datasets / benchmarks
3x3-pixel binary letter patterns (30 patterns)

## Limitations
- Tiny, trivial task; the same 30 patterns used for training and testing
- Activation function, subtraction, error computation and pulse control done by external electronics
- Single layer only; no multilayer or deep network
- Device-state-dependent update steps deviate from ideal Manhattan rule; requires careful initialization
- Individual forming of each device is not scalable

## Remarks
Foundational proof of concept rather than a system paper: first hardware evidence that transistor-free metal-oxide crossbars can do analog vector-matrix multiplication and learn in place. Heavily cited by later ReRAM accelerator, in-situ training and fault-tolerance works as the earliest demonstration. It is of historical rather than practical relevance for mapping modern models, since scale and peripherals are minimal.

## Cited by (in collection, 34)
- [2018_Kim_NonlinearIVAwareDNN_JETC](2018_Kim_NonlinearIVAwareDNN_JETC.md) Nonlinear-IV NN (2018) — _background_: "Since this approach can be several orders of magnitude more efficient than CMOS ASIC approaches in terms of both speed and power [3-6], many studies proposed neural network accelerators based on emerging NVM crossbar array [9-12]."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "Emerging technologies such as spin devices and memristor also create new opportunities to develop neuromorphic systems with high scalability and efficiency [8, 9, 10, 11, 12]."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _motivation_: "In the future, we will further support the simulation for other structures like dynamic synaptic properties [22], on-chip Training method [51], and inner-layer pipeline structure [7]."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _contrasts/critiques_: "While such 1T1M integration can increase the area compared to purely passive crossbar arrays,[34] even 1T1M-based architectures can reduce silicon area compared to purely digital approaches.[11]"
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "Memristors featuring low variability bilayer Al2O3/TiO2-x were recently reported in [37] and [104]."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "Crosspoint MVM can be adopted for a broad range of problems, including image compression, sparse coding, and implementation of artificial neural networks (ANNs), where Gij has the meaning of a synaptic weight, Vj is a pre-synaptic spike amplitude, and Ii is the input signal to the ith neuron (refs 69, 70)."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _motivation_: "However, experimental demonstrations to date have been limited to discrete devices24,25 or small arrays and simplified problems26-31."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _background_: "Besides conventional technologies, plenty of researches leverage modified SRAM [8]/ Flash [9] or various emerging non-volatile memory devices with in-memory computing capability to design this many-crossbar architecture, such as the most widely used RRAM (resistive RAM) [4–6, 19–24], PCRAM (phase-change RAM) [7, 25], and MRAM [26]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "To overcome this limitation, memristor crossbars can store a matrix with high storage density and perform MVM operations with very low energy and latency [5, 13, 52, 87, 98, 116]."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "A 10 × 6 portion in a 12 × 12 array of Al2O3/TiO2 memristors was used to recognize 3 × 3 pixel black/white images20."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _background_: "Although here we focus on ex-situ training, such systems have been successfully utilised for in-situ training too [10, 11]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Several experimental demonstrations (refs 4, 24-28) related to practical applications of in-memory computing have been reported as well."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Another approach is a mixed analogue/digital weight update whereby ∆Wij is computed digitally and applied to the arrays row-by-row or column-by-column (Fig. 6c). ∆Wij can be applied either at every individual training example (online training) or batch of training examples113–115."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _background_: "Thus, MCA is an analog computation unit and performs highly area and energy efficient inner-product operations [19]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Prior work has already observed that crossbar arrays using resistive memory are effective at performing many dot-product operations in parallel [33, 43, 53, 71, 78]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Most prior work exploits ReRAM either as DRAM/ﬂash replacement [20], [28], [40] or as synapses for NN computation [10], [11], [12], [13], [38]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Compute-in-memory (CIM) based on resistive random-access memory (RRAM) promises to meet such demand... thus eliminating power-hungry data movement between separate compute and memory [refs 2-5]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "Compared to MRAM, RRAM and PCM offer the advantages of compact cell size, large ON/OFF ratio and multi-bit capability [78] [171] [178] [179]."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "Manhattan update rule In the Manhattan learning rule, the amount of weight changes is disregarded, leaving only the direction of weight changes [33, 48, 49]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "Out of these efforts, RRAM is one of the most widely explored devices for PIM acceleration due to its non-volatile memory (NVM) nature, high storage density, fast read operation, low energy consumption, and excellent analog programmability for the multi-level cell (MLC) [23, 42, 46, 58, 60, 74, 78, 80]."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _background_: "Substantial progress has been made in developing analogue CIM chips for AI, evolving from initial proof-of-concept arrays5 to board-level integrated systems6–9 and recently achieving full system-on-chip integration10,11."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2015_Prezioso_MemristorPerceptron_Nature.pdf](../../02_Fabricated_Chips_and_Macros/2015_Prezioso_MemristorPerceptron_Nature.pdf)
- Full text: [../fulltext/2015_Prezioso_MemristorPerceptron_Nature.txt](../fulltext/2015_Prezioso_MemristorPerceptron_Nature.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/nature14441
