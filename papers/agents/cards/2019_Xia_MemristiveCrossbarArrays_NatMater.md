---
id: W2923010225
key: 2019_Xia_MemristiveCrossbarArrays_NatMater
title: "Memristive crossbar arrays for brain-inspired computing"
short: "Xia-Yang Memristive Crossbars"
year: 2019
venue: "NatMater"
venue_full: "Nature Materials, vol. 18, pp. 309-323 (2019)"
authors: "Qiangfei Xia, J. Joshua Yang"
category: "01 Surveys & Foundations"
devices: ["Memristor(generic)", "ReRAM", "PCM"]
models: ["MLP", "CNN", "LSTM/RNN", "SNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "analog-mvm", "crossbar-architecture", "device-variation", "write-verify-programming", "ir-drop-parasitics", "on-chip-training", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 11
cites_in_collection: 6
citations_overall: 1792
priority_score: 8.51
doi: "https://doi.org/10.1038/s41563-019-0291-x"
pdf: "../../01_Surveys_and_Foundations/2019_Xia_MemristiveCrossbarArrays_NatMater.pdf"
fulltext: "../fulltext/2019_Xia_MemristiveCrossbarArrays_NatMater.txt"
---

# Xia-Yang Memristive Crossbars

**Memristive crossbar arrays for brain-inspired computing** — Nature Materials, vol. 18, pp. 309-323 (2019) (2019)

## TL;DR
Nature Materials review of memristive crossbar arrays as accelerators for deep neural networks and as building blocks for spiking networks, arguing that experimental demos (largest ~128x64 1T1R, Table 1) lag far behind simulations because of device variability, nonlinear/asymmetric updates, wire resistance, sneak paths and peripheral-circuit overhead.

## Summary
The review frames memristors (ion-migration resistive switches) as synapse/neuron analogues and crossbars as hardware for vector-matrix multiplication via Ohm's and Kirchhoff's laws. Table 1 compares experimentally demonstrated analog crossbars (active 1T1R arrays up to 128x64 with Ta/HfO2, 128x8 HfAlyOx/TaOx; passive arrays up to 32x32 WOx), listing conductance range, synapse precision, update symmetry and the (mostly off-chip) peripheral circuitry. For DNNs it discusses device requirements (wide resistance range, low drift/fluctuation, high endurance), multilevel mechanisms (filament width, gap, composition modulation; PCM partial amorphization), variation-mitigation (write-verify, differential pairs, pulse optimisation), array programming/read schemes (1T1R versus selector 1S1R, PWM inputs), and offline (ex situ) versus online (in situ) training. A separate section covers SNNs with diffusive/threshold-switching memristor neurons, STDP synapses and comparison to CMOS neuromorphic systems (Neurogrid, SpiNNaker, TrueNorth, Loihi). The array-integration section treats sneak paths, wire resistance (to be compensated at algorithm level), 3D stacking, and on-chip integration of ADC/DAC with the arrays. The paper is qualitative and device-centric: no new experiments, no language models.

## Contributions
- Table 1 comparing figures of merit of the experimentally demonstrated analog memristor crossbars (size, conductance range, precision, update symmetry, peripherals)
- Identifies key device requirements for inference versus training (retention/low drift vs endurance/linear symmetric update)
- Reviews array programming/read schemes, selectors and wire/IR-drop effects for scaling to large arrays
- Covers memristor-based SNN building blocks (diffusive memristor neurons, STDP synapses)
- Argues for materials-to-algorithm co-design and integration of peripherals with the crossbar

## Key claims (stable IDs)
- **2019_Xia_MemristiveCrossbarArrays_NatMater#C1** — Experimental memristive networks remain limited to very small arrays solving simple problems, mainly due to device non-idealities and integration challenges. — _support:_ Largest demonstrated active array 128x64 (1T1R), passive 32x32 — _loc:_ Introduction; Table 1
- **2019_Xia_MemristiveCrossbarArrays_NatMater#C2** — Intrinsic memristor noise may be beneficial for neural computing rather than harmful. — _support:_ 'implying that memristors with their intrinsic noise might be more suitable for neural computing rather than memory' — _loc:_ Deep neural networks section (device requirements)
- **2019_Xia_MemristiveCrossbarArrays_NatMater#C3** — Wire-resistance effects must also be compensated at the algorithm level. — _support:_ citing refs 14,18 — _loc:_ Array integration and upscaling
- **2019_Xia_MemristiveCrossbarArrays_NatMater#C4** — No experimental large-scale SNN trained with STDP had been reported by 2019. — _support:_ 'no experimental demonstration of training a large-scale SNN using STDP has been reported so far' — _loc:_ SNN section

## Results
- Table 1: Ta/HfO2 1T1R 128x64 with 100-900 uS conductance range and 0.75% error, 2 um transistor node; HfAlyOx/TaOx 128x8 with 10-60 uS; passive arrays have nonlinear I-V and 5-35% error
- Peripherals in all surveyed demos are largely off-chip (MCU with DAC/ADC/TIA or semiconductor parameter analyser)
- Memristor claims: <2 nm size, <1 ns switching, retention >>10 years at 85 C (Ta/HfO2)
- CMOS SNNs ~20x/400x/2000x larger in neuron area/synaptic area/synaptic-op energy than biological systems (quoted from ref 63)

## Key numbers
- tech_node: 2 um / 1.2 um transistor nodes (surveyed 1T1R demos)
- array_size: 128x64 (largest 1T1R demo)

## Datasets / benchmarks
MNIST

## Limitations
- Qualitative review; no unified benchmark or energy/throughput numbers
- Published 2019: predates transformer/LLM work and large multi-core chips
- Strong device-materials focus; limited architecture/ADC discussion
- Text extraction of Table 1 is partially interleaved; some cell alignment uncertain

## Remarks
A standard materials-side reference for memristor crossbars from the UMass group; useful for device vocabulary (linearity, symmetry, drift, endurance) and the inference-versus-training device requirements. It gives no guidance for mapping language models, but its non-ideality list (variation, wire resistance, sneak paths, limited precision) is the problem set later tackled by hardware-aware training and chip work in the collection. For architecture-level and peripheral treatment see crossbar-architecture papers such as ISAAC.

## Cites (in collection, 6)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "A 10 × 6 portion in a 12 × 12 array of Al2O3/TiO2 memristors was used to recognize 3 × 3 pixel black/white images20."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "A 128 × 64 Ta/HfO2 1T1R array was built and used for efficient analogue signal and image processing and machine learning16–19."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _data/numbers_: "This has been experimentally confirmed recently17, implying that memristors with their intrinsic noise might be more suitable for neural computing rather than memory or storage applications."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 11)
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _background_: "These line resistance effects can be partially compensated for algorithmically [17] or partially mitigated by using multiple smaller crossbar arrays [18]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Studies on memristor-based neuromorphic computing have covered a broad range of topics, from device optimization to system implementation (refs 6, 17-23)."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "Analogue memory-based DNN accelerators are being widely developed in academia and industry using a variety of memories5, including resistive RAM (ReRAM)6,7, conductive-bridging RAM (CBRAM)8, NOR flash9-12, magnetic RAM (MRAM), and phase-change memory (PCM)13,14."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "Excellent recent reviews on these five types of memories, mentioned above, have been published earlier [94] [77] [95] [96] [97] [98] [99] [100] [101] [102] [103] [104]."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _background_: "By coordinating the applied read voltages and measurements of the output currents, the vector-matrix multiplications for information forwarding and error backpropagation can be done in one step [3, 4]."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _data/numbers_: "While 6T SRAM offers a read current ratio near 1,000, those of PCM and RRAM range from 10 to 100 (refs. 50,51), and that of spin-transfer torque MRAM often falls below 2 (ref. 52)."
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Nikam_PassiveRRAMLSTM_TED](2021_Nikam_PassiveRRAMLSTM_TED.md) Passive RRAM LSTM (2021)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)
- [2024_Li_MemristorCiMLLM_IoTJ](2024_Li_MemristorCiMLLM_IoTJ.md) MemristorCiMLLM (2024)

## Files
- PDF: [../../01_Surveys_and_Foundations/2019_Xia_MemristiveCrossbarArrays_NatMater.pdf](../../01_Surveys_and_Foundations/2019_Xia_MemristiveCrossbarArrays_NatMater.pdf)
- Full text: [../fulltext/2019_Xia_MemristiveCrossbarArrays_NatMater.txt](../fulltext/2019_Xia_MemristiveCrossbarArrays_NatMater.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41563-019-0291-x
