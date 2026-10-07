---
id: W3011221635
key: 2020_Chakraborty_GENIEx_DAC
title: "GENIEx: A Generalized Approach to Emulating Non-Ideality in Memristive Xbars using Neural Networks"
short: "GENIEx"
year: 2020
venue: "DAC"
venue_full: "ACM/IEEE Design Automation Conference (DAC 2020)"
authors: "Indranil Chakraborty, Mustafa Ali, Dong Eun Kim, Aayush Ankit, Kaushik Roy"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Memristor(generic)"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["simulator", "ir-drop-parasitics", "bit-slicing", "tiling-partitioning", "analog-mvm", "device-variation", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 16
cites_in_collection: 5
citations_overall: 109
priority_score: 7.61
doi: "https://doi.org/10.1109/dac18072.2020.9218688"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2020_Chakraborty_GENIEx_DAC.pdf"
fulltext: "../fulltext/2020_Chakraborty_GENIEx_DAC.txt"
---

# GENIEx

**GENIEx: A Generalized Approach to Emulating Non-Ideality in Memristive Xbars using Neural Networks** — ACM/IEEE Design Automation Conference (DAC 2020) (2020)

## TL;DR
GENIEx trains a neural network on HSPICE crossbar data to emulate data-dependent (nonlinear) memristive crossbar non-idealities, with 7x and 12.8x lower RMSE than an analytical model, and shows analytical models overestimate DNN accuracy loss by about 12% on CIFAR-100 and about 4-6.5% on ImageNet.

## Summary
Analytical crossbar models capture only linear, data-independent effects (parasitic wire resistance), but access-transistor and device I-V nonlinearity make the output current depend on voltage and conductance patterns. GENIEx runs HSPICE for 16/32/64-size crossbars with ON resistance 50k/100k/300kOhm and varied ON/OFF ratio, using voltage vectors drawn from CIFAR-100/ImageNet activations and conductances from pretrained ResNet weights. A small neural network takes concatenated normalized (V, G) and predicts the non-ideality ratio f_R = I_ideal/I_non-ideal. This is embedded in a PyTorch functional simulator that implements conv2d/linear as crossbar MVMs with tiling, 16-bit fixed-point weights/activations and bit-slicing (weight Slices across devices) plus bit-streaming (input Streams through DACs), ISAAC/PUMA-style. Accuracy is evaluated on ResNet-20 (CIFAR-100) and larger ImageNet networks, sweeping crossbar size, ON resistance, ON/OFF ratio, precision, and Slice/Stream widths.

## Contributions
- Analysis of linear and nonlinear crossbar non-ideality sources via SPICE
- NN-based crossbar emulator capturing data-dependent behavior
- Functional simulator with tiling and bit-slicing for large-scale DNNs
- Design-space study of crossbar size, ON resistance, ON/OFF ratio, bit precision, Slice/Stream widths

## Key claims (stable IDs)
- **2020_Chakraborty_GENIEx_DAC#C1** — GENIEx RMSE vs HSPICE is 0.25 (V=0.25V) and 0.7 (V=0.5V), 7x and 12.8x better than analytical — _support:_ analytical RMSE 8.99 at V=0.5 for 64x64 — _loc:_ Fig. 5
- **2020_Chakraborty_GENIEx_DAC#C2** — Analytical model overestimates accuracy degradation by 12.34% (V=0.25V) and 11.6% (V=0.5V) on CIFAR-100 ResNet-20 — _support:_ Fig. 7(d) — _loc:_ Sec. 7.1
- **2020_Chakraborty_GENIEx_DAC#C3** — Non-idealities hurt more at lower precision — _support:_ degradation 12.5% to 29.6% (CIFAR-100) and 4.54% to 17.67% (ImageNet) from 16-bit to 8-bit — _loc:_ Fig. 8, Sec. 7.2

## Results
- 64x64 crossbar loses 12% accuracy vs ideal FxP; 16x16 loses <=1% (Fig. 7a)
- ON resistance 300kOhm gives 7.6% less degradation than 100kOhm (Fig. 7b)
- ON/OFF ratio 2 gives up to 46% degradation vs 8.6% at ratio 10 (Fig. 7c)
- 2-bit or 1-bit Slices/Streams reach near ideal FxP; 4-bit gives 12.48% degradation (Fig. 9)

## Key numbers
- array_size: 16x16, 32x32, 64x64
- accuracy: 12% degradation on 64x64 crossbar (ResNet-20, CIFAR-100)
- bits_weight: 16b FxP with 1-4b slices

## Datasets / benchmarks
CIFAR-100, ImageNet

## Limitations
- Emulator is trained per crossbar configuration/device model; device model is generic
- No temporal drift, stuck-at faults or read noise modelled in the main study
- HSPICE ground truth only, no measured silicon
- CNN workloads only

## Remarks
Influential evidence that linear analytical models mis-predict accuracy loss, mostly pessimistically, which matters when judging mapping decisions. For LM/transformer mapping the lesson is that bit-slice/stream widths and crossbar size interact strongly with non-ideality; no language-model data here.

## Cites (in collection, 5)
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "An alternative way of capturing effects such as stuck-at-faults [14] or device variations [15] is to map the distribution of the variations or defects."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "To this effect, researchers have explored Non Volatile Memory (NVM) [4, 5] based crossbar architectures to achieve higher on-chip storage density and efficient MVMs in the analog domain [6, 7]."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "To this effect, researchers have explored Non Volatile Memory (NVM) [4, 5] based crossbar architectures to achieve higher on-chip storage density and efficient MVMs in the analog domain [6, 7]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Crossbar-based accelerators commonly use bit-slicing to perform high precision MVM operations [6, 7]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Crossbar-based accelerators commonly use bit-slicing to perform high precision MVM operations [6, 7]."

## Cited by (in collection, 16)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _background_: "Fig. 32(a) shows the degradation in accuracy for various benchmark DNNs."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021) — _contrasts/critiques_: "Recent work GenieX [6] provides a neural network based framework to model both data-dependent and data-independent nonidealities for a crossbar array of 1T-1R synapses."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "The first category includes device defects (e.g., stuck-at-high or stuckat-low resistance [12]) and device reliability issues (e.g., retention failure [13] and resistance drift [14]) that are mostly deterministic in nature and have been addressed in prior work [15–20]."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _motivation_: "However, RRAM device suffers from several non-idealities such as limited resistance levels, device-to-device write variations, stuck-at-faults, and limited Roff /Ron ratio, posing a signiﬁcant challenge to designing reliable RRAM-based IMC architectures [5–12]."
- [2023_Ma_SAFVariationTolerantMapping_JETC](2023_Ma_SAFVariationTolerantMapping_JETC.md) SAF/Variation Remapping (2023) — _background_: "Large weight matrices are always separated into pieces and then mapped to several MCAs [3]."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "In recent years, several noise models [2, 19, 26] and crossbar-realistic DNN accuracy evaluation frameworks (Neurosim [17], RxNN [10], GenieX [6], Memtorch [13]) have been proposed that are integrated with hardware-aware re-training or fine-tuning of GPU-trained DNN weights, to mitigate performance losses during inference"
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _background_: "Previous works have demonstrated the effectiveness of using NVM devices with higher ON/OFF ratios to reduce read variations during inference of deep neural networks [14], [29]–[31]."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _motivation_: "However, this is challenging due to the accumulation of noise from the non-ideal behavior of memristors [45][46][47]."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _background_: "While there exists other IMC-specific non-idealities such as IR-drop [26] and transistor nonlinearities [29], we use read/write variations (only for FeFET implementation) and ADC quantization noise (for both FeFET and SRAM implementations) to evaluate TReX."
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025) — _contrasts/critiques_: "While automated ML-based in-the-loop modeling40 approaches can be utilized, they require a significant amount of data, which is instance-specific."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _motivation_: "However, the impact of device-circuit non-idealities in the crossbar (both linear and non-linear) increases with increasing bits per crossbar cell leading to significant losses in network accuracy [16]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "It has been demonstrated that the IR drop leads to significant error due to the reduction of the output currents in the array, especially for larger array sizes [43]."
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2020_Chakraborty_GENIEx_DAC.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2020_Chakraborty_GENIEx_DAC.pdf)
- Full text: [../fulltext/2020_Chakraborty_GENIEx_DAC.txt](../fulltext/2020_Chakraborty_GENIEx_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/dac18072.2020.9218688
