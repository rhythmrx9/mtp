---
id: W2782791387
key: 2018_Hu_DotProductEngine_AdvMater
title: "Memristor‐Based Analog Computation and Neural Network Classification with a Dot Product Engine"
short: "HPE Dot Product Engine"
year: 2018
venue: "AdvMater"
venue_full: "Advanced Materials, vol. 30, 2018"
authors: "Miao Hu, Catherine E. Graves, Can Li, Yunning Li, Ning Ge, Eric Montgomery, Noraica Dávila, Hao Jiang, Richard Stanley Williams, J. Joshua Yang, Qiangfei Xia, John Paul Strachan"
category: "02 Fabricated Chips & Macros"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "analog-mvm", "write-verify-programming", "ir-drop-parasitics", "stuck-at-faults", "calibration-compensation", "adc-dac", "device-variation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 23
cites_in_collection: 2
citations_overall: 755
priority_score: 10.25
doi: "https://doi.org/10.1002/adma.201705914"
pdf: "../../02_Fabricated_Chips_and_Macros/2018_Hu_DotProductEngine_AdvMater.pdf"
fulltext: "../fulltext/2018_Hu_DotProductEngine_AdvMater.txt"
---

# HPE Dot Product Engine

**Memristor‐Based Analog Computation and Neural Network Classification with a Dot Product Engine** — Advanced Materials, vol. 30, 2018 (2018)

## TL;DR
Hardware demonstration of a 128x64 1T1M Ta/HfO2 memristor crossbar (Dot Product Engine) with closed-loop analog tuning to ~180 conductance levels, ~6-bit equivalent VMM accuracy and 89.9% accuracy on the full 10k MNIST test set with a single-layer softmax network (software 92.4%), projecting >100 TOPS/W (115 TOPS/W) if integrated and scaled.

## Summary
Earlier memristor crossbar neural-network claims relied on simulation or small (<1024 cells), binary-state arrays, and the 165,000-synapse PCM demonstration used a sequential interface rather than single-step VMM. This work builds a Dot Product Engine (DPE): Ta/HfO2/Pd memristors integrated by a BEOL process on 2 um CMOS access transistors in a 1T1M arrangement (transistor limits compliance during programming and is fully open in compute mode). A PCB-based system drives all rows simultaneously with 164 ns-4 us pulses, and senses all column currents via TIA, sample-and-hold and ADC, using probe-card access. Cells are programmed by a feedback (write-verify) algorithm varying pulse amplitude, gate voltage and width, reaching about 180 conductance levels (a greyscale logo) and an inset programming-error spread with most levels showing <10 uS spread but outliers and stuck-ON cells. VMM errors are dominated by wire resistance and sneak paths, matched by circuit simulation and reduced by a one-time linear per-column calibration (100 test patterns). Two applications reuse the same array: a DCT (signed values via two cells per value) and a single-layer softmax MNIST classifier trained offline in MATLAB, with images resized to 19x20 (380 inputs), reshaped to a 96x40 array and processed in four partial VMMs summed digitally (softmax normalisation not done in hardware). Weights are linearly mapped to 100-700 uS.

## Contributions
- First demonstration (to the authors' knowledge) of a large memristor crossbar (128x64) doing single-step analog VMM with full-array simultaneous drive and sensing
- High-precision closed-loop analog tuning across an entire array (~180 levels, ~6-bit VMM accuracy) in 1T1M Ta/HfO2 cells
- Per-column linear calibration that compensates wire-resistance/sneak-path errors with no runtime overhead
- Reprogrammability of one array for DCT and neural-network inference; 10k-image MNIST inference with 89.9% accuracy
- Power-efficiency forecast of 115 TOPS/W for an integrated scaled version

## Key claims (stable IDs)
- **2018_Hu_DotProductEngine_AdvMater#C1** — The DPE reaches an equivalent VMM precision of 6 bits — _support:_ abstract; 64 levels (6 bits) previously shown per 1T1M cell — _loc:_ Abstract, Fig. 3
- **2018_Hu_DotProductEngine_AdvMater#C2** — Single-layer MNIST inference on the full 10k test set achieves 89.9% accuracy, 2.5% below ideal software (92.4%) — _support:_ loss attributed to programming error, stuck-ON defects and wire resistance — _loc:_ Fig. 4c, Sec. 'Neural network inference'
- **2018_Hu_DotProductEngine_AdvMater#C3** — Parasitic-induced VMM errors are matched by circuit simulation and can be corrected with linear per-column scaling — _support:_ calibration from 100 test input patterns — _loc:_ Fig. 3b-d
- **2018_Hu_DotProductEngine_AdvMater#C4** — An integrated scaled DPE (<100 nm, 150 MHz, ADC <133 uW/column) would achieve ~115 TOPS/W vs ~7 TOPS/W for 4-bit digital in 40 nm — _support:_ 16,320 MACs in a 128x64 array — _loc:_ Discussion, Table S2

## Results
- VMM equivalent precision of 6 bits (Abstract)
- 89.9% MNIST accuracy on 10k test images vs 92.4% software (single-layer, 96x40 mapped array) (Fig. 4)
- ~180 distinct conductance levels programmed in the 128x64 array (Fig. 1c)
- Programming: 50 cycles used; most levels have spread <10 uS; error-histogram std 72.7 uS including outliers (Fig. 2)
- Forecast 115 TOPS/W vs 7 TOPS/W digital 4-bit (40 nm); measured system runs at 10 MHz
- Full-array read of >8000 devices takes <2 s via firmware (Experimental section)

## Key numbers
- tech_node: 2um CMOS transistors + BEOL Ta/HfO2 memristors
- array_size: 128x64 (96x40 used for MNIST)
- energy_eff: 115 TOPS/W (forecast)
- accuracy: 89.9% MNIST (single-layer softmax; software 92.4%)
- bits_weight: ~6-bit (~180 conductance levels)

## Datasets / benchmarks
MNIST

## Limitations
- Only a single-layer softmax classifier; no multilayer network or nonlinear activation in hardware, accuracy 2.5% below software
- Not a fully integrated chip: memristors on 2 um CMOS transistors, off-chip PCB drivers/ADCs and probe cards, 10 MHz operation
- Stuck-ON defects, programming outliers and wire-resistance errors; static (offline) weight programming only, no drift/retention or endurance study
- Efficiency number (115 TOPS/W) is a forecast, not measured
- Only one array evaluated, and images downscaled to fit 4096 cells

## Remarks
Important early measured-hardware milestone showing a reasonably large memristor array can be programmed accurately enough (~6 bits) for real inference, going beyond simulation-only work. The gap to software accuracy and single-layer scope illustrate why later work needed non-ideality-aware training, calibration and multi-layer chips (e.g. NeuRRAM-type designs). Its mapping (reshaping and partitioning large matrices over smaller arrays, partial sums added digitally) is the same pattern now used for LM weight tiling, but there is no language-model relevance beyond that.

## Cites (in collection, 2)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _contrasts/critiques_: "While such 1T1M integration can increase the area compared to purely passive crossbar arrays,[34] even 1T1M-based architectures can reduce silicon area compared to purely digital approaches.[11]"
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _contrasts/critiques_: "Large neural networks (165 000 synapses) were demonstrated with PCM arrays,[42] but this work was limited by a sequential interface and could not carry out VMM computations in a single step with access to all word-lines and bit-lines simultaneously, as would be required for an actual computational accelerator."

## Cited by (in collection, 23)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _contrasts/critiques_: "There are approaches to improve the robustness of ex situ training19,38, but most of them require that the parameters be tuned based on specific knowledge of the hardware (e.g., peripheral circuitry) and memristor array (e.g., device defects, wire resistance, etc.), while the in situ training adapts the weights and compensates them automatically."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _data/numbers_: "Practically realizable crossbars provide 2-6 bits of precision per device [52]."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "A 128 × 64 Ta/HfO2 1T1R array was built and used for efficient analogue signal and image processing and machine learning16–19."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Both charge-based storage devices, such as Flash memory4, and resistance-based (memristive) storage devices, such as metal-oxide resistive random-access memory (ReRAM)5,6 and phase-change memory (PCM)7-9 are being investigated for this."
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019) — _uses-method-or-tool_: "Row Decoder design is no larger than 128×64 [36] and is identical for all DNN layers."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _uses-method-or-tool_: "To strike a balance, we choose p = 4, since p > 4 requires a device precision that exceeds ReRAM technology limits [15]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "To this effect, researchers have explored Non Volatile Memory (NVM) [4, 5] based crossbar architectures to achieve higher on-chip storage density and efficient MVMs in the analog domain [6, 7]."
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020) — _uses-method-or-tool_: "Due to the increasing reading/writing errors caused by expanding the memristor crossbar size, we limited our design by using multiple 128×64 [25] crossbars for all DNN layers."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _background_: "To overcome the memory bottleneck, many researchers show interest in resistive crossbar arrays for the computing-in-memory feature [1, 8, 14, 21, 25, 41]."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _data/numbers_: "As a case study, HP's Dot Product Engine (128 x 128 crossbar) was evaluated in simulation using both analog routing-with buffers and repeaters-and digital routing, which interfaces with the crossbars via ADCs and DACs.65 The authors found that accuracy on the MNIST task degraded more strongly with analog routing"
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "nonvolatile memory (NVM) technologies [19, 20], such as phase-change memory (PCM) [21], resistive random access memory (RRAM) [22, 23], and spintronics [24], offer immense promise as an alternative to CMOS"
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _background_: "A major advantage of IMC is the capability to execute matrix-vector multiplication (MVM) in parallel on multiple rows and columns of a memory array, which allows for a strong acceleration of neural networks [3]-[7]."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _uses-method-or-tool_: "Multiplication of the intensity values of the input pixels by the kernel weights can be achieved using Ohm's law, and the accumulation can be achieved using Kirchhoff's law (20, 46)."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _data/numbers_: "In [169] a RRAM based cross-bar array with off-chip peripheral circuits was built with a Ta/HFO2/Pd stack as a switching element accessible through a select transistor... The demonstration vehicle was a one-layer (96 x 40) network for hand written digit classification (MNIST)... Classification error was 89.9% which was 2.5% shy of theoretical expectation for the same configuration."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Early works on performing neural network inference with AIMC showed promising accuracy results in mixed hardware/software implementations, where functionalities such as digital-to-analog and analog-to-digital conversions, activation functions, and other necessary digital operations were implemented with off-chip software or hardware (refs 8-12)."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "A cost-effective recurrent solution has been to use a smaller number of DACs and share them among different rows by adding a layer of analogue multiplexors between the DACs and the wordline inputs."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _background_: "Since memristor crossbars are programmable and non-volatile9,10, they can be utilized to build dedicated hardware accelerators for deep neural networks."
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2021_Nikam_PassiveRRAMLSTM_TED](2021_Nikam_PassiveRRAMLSTM_TED.md) Passive RRAM LSTM (2021)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2018_Hu_DotProductEngine_AdvMater.pdf](../../02_Fabricated_Chips_and_Macros/2018_Hu_DotProductEngine_AdvMater.pdf)
- Full text: [../fulltext/2018_Hu_DotProductEngine_AdvMater.txt](../fulltext/2018_Hu_DotProductEngine_AdvMater.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1002/adma.201705914
