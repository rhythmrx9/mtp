---
id: W4283733417
key: 2022_Mackin_WeightProgrammingOptimisation_NatCommun
title: "Optimised weight programming for analogue memory-based deep neural networks"
short: "DWE Weight Programming"
year: 2022
venue: "NatCommun"
venue_full: "Nature Communications, vol. 13, 3765 (2022)"
authors: "Charles Mackin, Malte J. Rasch, An Chen, Jonathan Timcheck, Robert L. Bruce, Ning Li, Pritish Narayanan, Stefano Ambrogio, Manuel Le Gallo, S. R. Nandakumar, Andrea Fasoli, Jose Luquin et al."
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["PCM"]
models: ["LSTM/RNN", "CNN", "ResNet", "Transformer", "BERT"]
lm_models: ["BERT-base", "2-layer LSTM (Penn Treebank)"]
param_scale: "~110M (BERT-base, ~86M encoder weights, 53M unique)"
slm: true
evidence: algorithm+simulation
topics: ["weight-mapping", "conductance-drift", "read-write-noise", "device-variation", "hardware-aware-training", "calibration-compensation", "bit-slicing", "language-models"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 10
cites_in_collection: 11
citations_overall: 54
priority_score: 9.34
doi: "https://doi.org/10.1038/s41467-022-31405-1"
pdf: "../../06_Nonidealities_and_Reliability/2022_Mackin_WeightProgrammingOptimisation_NatCommun.pdf"
fulltext: "../fulltext/2022_Mackin_WeightProgrammingOptimisation_NatCommun.txt"
---

# DWE Weight Programming

**Optimised weight programming for analogue memory-based deep neural networks** — Nature Communications, vol. 13, 3765 (2022) (2022)

## TL;DR
IBM's network-agnostic weight-programming optimiser (Differential Weight Evolution over six discretised weight points, a 4D+2 search space, scored by a time-averaged weight-error proxy) translates software weights into 4-conductance PCM weights that keep inference accuracy near iso-accuracy over time for LSTM, ResNet-32 and BERT-base, in simulation with measured PCM statistics.

## Summary
Hardware-aware training yields 'unitless' weights that must still be converted to target conductances; with multiple conductances per weight (G+, G-, g+, g- with MSP/LSP significance factor F) there are infinitely many encodings with different error behaviour, and PCM drift (G(t)=G0 (t/t0)^-nu, stochastic and conductance-dependent) makes the error time-varying. The paper solves for translation functions G+(W), G-(W), g+(W), g-(W) plus the scale factor beta_hw and F by reducing the ~4N+2 parameters (N weights) to 4D+2 using D=6 discretised positive weights (mirrored for negatives, linearly interpolated). The cost is a time-averaged weighted weight-error metric (including programming error, drift with per-column compensation factor alpha obtained from calibration vectors, and read noise), weighting errors by weight-density since gradients show zero correlation with weight value; BERT-base 212M parameters reduce to 26. DWE searches a hypercube de-normalised into valid conductance combinations. PCM statistics (mushroom-type doped GST, programming error, drift over 1000 s, read noise) were measured; networks were hardware-aware-trained with weight noise, 8-bit input and 10-bit output quantization, IR-drop and read noise. Evaluation: 25 independent simulated programming/inference runs over time on LSTM (Penn Treebank), ResNet-32 (CIFAR-10) and BERT-base (MNLI) against naive MSP/LSP strategies, for two device models.

## Language models evaluated
- Models: BERT-base, 2-layer LSTM (Penn Treebank)
- Scale: ~110M (BERT-base, ~86M encoder weights, 53M unique)

## Contributions
- Generalised, network-agnostic framework that automates weight programming strategy design for analogue memory
- Dimensionality reduction (discretised weights, symmetry) with a proxy time-averaged weight-error metric requiring no inference simulations
- Validation on LSTM, CNN and Transformer (BERT-base) across two PCM-like device models
- Method to compute best-achievable inference accuracy per device, enabling device comparison

## Key claims (stable IDs)
- **2022_Mackin_WeightProgrammingOptimisation_NatCommun#C1** — An optimised strategy reduces weight error by ~39% at t0 and ~17% at one month versus a naive MSP/LSP strategy in the illustrative example. — _support:_ identical device models, same weight range — _loc:_ Fig. 2b vs 2e
- **2022_Mackin_WeightProgrammingOptimisation_NatCommun#C2** — Optimised programming keeps inference accuracy as close to iso-accuracy as the device allows for LSTM, ResNet-32 and BERT-base, outperforming naive and other strategies. — _support:_ 25 independent simulations over time; accuracy curves — _loc:_ Fig. 4d-f, Fig. 5d-f
- **2022_Mackin_WeightProgrammingOptimisation_NatCommun#C3** — A device with larger dynamic range (gmax=30 uS) and lower average drift can still be worse once both are optimally programmed, which naive strategies would mask. — _support:_ Fig. 5 vs Fig. 4 comparison — _loc:_ Results
- **2022_Mackin_WeightProgrammingOptimisation_NatCommun#C4** — The optimal strategy programs weights in the LSP when possible and uses the MSP (F=2) only for large weights, because MSP errors are amplified by F. — _support:_ derived programming strategies — _loc:_ Results

## Results
- Parameter count reduction: BERT-base ~212 million -> 26 (4D+2 with D=6)
- Weight errors reduced ~39% at t0 and ~17% at one month in the example
- Accuracy results for LSTM (PTB), ResNet-32 (CIFAR-10), BERT-base (MNLI) shown only in figures; numeric values not recoverable from extracted text
- Hardware-aware training assumed 8-bit inputs, 10-bit ADC outputs, output noise ~1 LSB

## Key numbers
- accuracy: near iso-accuracy for LSTM/ResNet-32/BERT-base (values in figures)
- bits_weight: 4 conductances per weight (G+, G-, g+, g-), F=2
- bits_adc: 10b output / 8b input in training

## Datasets / benchmarks
Penn Treebank, CIFAR-10, MNLI

## Limitations
- Simulation only, with PCM characteristics from measured statistics but no end-to-end hardware validation
- Drift and multi-conductance splitting are not included in hardware-aware training itself
- Proxy metric assumes weight errors equally important weighted by density; gradient-insensitivity assumption
- BERT evaluated on MNLI only; no autoregressive language models
- Optimisation depends on accuracy of device model; numeric accuracy gains not stated in text

## Remarks
Treats the often-overlooked weight-to-conductance translation as a first-class optimisation problem, complementing hardware-aware training. Its inclusion of BERT-base shows the approach scales to transformer weight counts because dimensionality is reduced independent of network size. Simulation-only evidence tempers generalisation, but it is a frequently cited reference for IBM analog-AI toolkit work and for programming strategies (differential pairs, MSP/LSP) relevant to mapping language models.

## Cites (in collection, 11)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Analogue memory-based DNN accelerators are being widely developed in academia and industry using a variety of memories5, including resistive RAM (ReRAM)6,7, conductive-bridging RAM (CBRAM)8, NOR flash9-12, magnetic RAM (MRAM), and phase-change memory (PCM)13,14."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _motivation_: "This approach was recently shown capable of 280x speedup in per-area throughput while providing 100x enhancement in energy-efficiency over state-of-the-art GPUs4."
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019) — _background_: "Analogue memory-based DNN accelerators are being widely developed in academia and industry using a variety of memories5, including resistive RAM (ReRAM)6,7, conductive-bridging RAM (CBRAM)8, NOR flash9-12, magnetic RAM (MRAM), and phase-change memory (PCM)13,14."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "It has been shown that hardware-aware training in software is crucial for improving accuracy for analogue inference19,24,25,39."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019) — _background_: "To date, each type of analogue memory exhibits some form of non-ideal behaviour such as limited resistance contrast, significant non-linearity and stochasticity in conductance-vs-pulse characteristics, strong asymmetry during bidirectional programming, read noise, and conductance drift after programming to name a few15-19."
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _uses-method-or-tool_: "As mentioned earlier, this can be mitigated using a drift compensation technique32, where activations are amplified close to their original levels using drift compensation factor alpha, which may or may not be uniform along the column-wise dimension of the crossbar array."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Introducing such redundancy has been shown to offer accuracy benefits by effectively countering some of the variability present in analogue memory26,37,38."
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020) — _uses-method-or-tool_: "We have previously employed this weight programming time-scale as an effective compromise between conductance stability and programming speed for the programming of millions of weights40."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _background_: "Incorporating hardware non-idealities within DNN training (i.e., 'hardware-aware' algorithmic training) has been shown effective in making analogue memory-based DNNs more resilient to hardware imperfections22-25."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _uses-method-or-tool_: "The significance factor can be implemented in a number of ways, but is limited to discrete values in this case, which can be readily implemented by multiplying the pulse durations of the input activations applied to the MSP relative to the LSP30,31."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _background_: "By subjecting the DNN to memory and circuit non-idealities during training22-25, HWA training clearly makes the DNN more resilient to the various hardware non-idealities, and significantly enhances network accuracy relative to floating-point training across the board."

## Cited by (in collection, 10)
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "As discussed earlier, the weight transfer into an analog storage mode requires special considerations [182] [183]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _extends/builds-on_: "That said, our HWA training approach could readily be combined with more sophisticated online compensation methods, with on-chip or chip-in-the-loop training, or with more than one device pair used per weight, including optimization of how weights are assigned across these conductances62."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _motivation_: "These inherent characteristics limit their accuracy and reliability to use in practical deep learning workloads18–20 ."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _background_: "Furthermore, weight programming [3], [21], [22], as well as weight-related long-term non-ideality compensation techniques [14], [28], are well studied."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "If multiple devices are available to encode the weight magnitude, additional options for distributing the weight magnitude across these devices become available as well, allowing optimization for placement accuracy, long-term conductance stability and other considerations34,35."
- [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md) AIMC Device Specs (2026) — _uses-method-or-tool_: "To mitigate the impact of NVM non-idealities and obtain robust weight values for AIMC, we apply the hardware-aware (HWA) training procedure [5, 12]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2022_Mackin_WeightProgrammingOptimisation_NatCommun.pdf](../../06_Nonidealities_and_Reliability/2022_Mackin_WeightProgrammingOptimisation_NatCommun.pdf)
- Full text: [../fulltext/2022_Mackin_WeightProgrammingOptimisation_NatCommun.txt](../fulltext/2022_Mackin_WeightProgrammingOptimisation_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-022-31405-1
