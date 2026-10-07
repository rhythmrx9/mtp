---
id: W3006908002
key: 2021_Roy_TxSim_TVLSI
title: "TxSim: Modeling Training of Deep Neural Networks on Resistive Crossbar Systems"
short: "TxSim"
year: 2021
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2021)"
authors: "Sourjya Roy, Shrihari Sridharan, Shubham Jain, Anand Raghunathan"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM"]
models: ["MLP", "CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "on-chip-training", "ir-drop-parasitics", "device-variation", "adc-dac", "read-write-noise", "benchmarking"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 9
cites_in_collection: 6
citations_overall: 54
priority_score: 7.21
doi: "https://doi.org/10.1109/tvlsi.2021.3063543"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2021_Roy_TxSim_TVLSI.pdf"
fulltext: "../fulltext/2021_Roy_TxSim_TVLSI.txt"
---

# TxSim

**TxSim: Modeling Training of Deep Neural Networks on Resistive Crossbar Systems** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2021) (2021)

## TL;DR
TxSim is a PyTorch/BLAS-based functional simulator that models crossbar non-idealities in forward, backward and weight-update phases of DNN training, 6x-108x faster than prior tools, and shows 3%-36.4% accuracy degradation for large DNNs.

## Summary
Existing crossbar tools either only handle inference (RxNN, GENIEx-style) or are too slow for training (CrossSim, NeuroSim). TxSim models each layer as DAC model, crossbar array model and ADC model. A non-ideal conductance matrix generator maps weights to devices (on-off ratio, precision), tiles into crossbar instances, splits positive/negative onto separate crossbars, applies process variation, and applies the Fast Crossbar Model (FCM) to include wire, source and sink resistances and sneak paths; the matrix multiply then uses BLAS. The update model includes asymmetric write non-linearity (factor v) and Gaussian stochastic write noise (factor gamma). Because FCM per minibatch is slow, two speedups are proposed: an Approximate Analytical Model (AAM, only short current paths; valid when Rmin is much larger than wire resistance) and Interpolated-FCM (run FCM every L iterations and reuse the distortion profile). Experiments use 64x64 Ag/Si ReRAM crossbars (Rmin 100kOhm, Rmax 1MOhm), 2-bit devices, 1-bit DACs, 32-bit digital precision, on LeNet-5, AlexNet, ResNet-20/56/18, VGG-16 across MNIST, CIFAR and Tiny-ImageNet.

## Contributions
- TxSim: scalable, customisable training-aware crossbar non-ideality modelling (forward, backward, update)
- AAM and Interpolated-FCM speedup techniques with small fidelity loss
- Sensitivity analysis over crossbar size, on-off ratio, update non-linearity and write noise
- 6x-108x faster than prior training simulators

## Key claims (stable IDs)
- **2021_Roy_TxSim_TVLSI#C1** — TxSim is 108x faster than CrossSim on MLP/MNIST training — _support:_ CrossSim needs ~1 week for a 3-layer net — _loc:_ Sec. II, VI-A
- **2021_Roy_TxSim_TVLSI#C2** — Non-idealities degrade crossbar-trained DNN accuracy by 3%-36.4% — _support:_ Cross-NI vs Cross-Ideal — _loc:_ Sec. VI-B, Fig. 8-9
- **2021_Roy_TxSim_TVLSI#C3** — Update non-linearity factor should stay within 0.1 and write noise factor within 5 — _support:_ gamma=10 gives ~10% drop; v=1 fails to converge — _loc:_ Sec. VI-C, Fig. 10
- **2021_Roy_TxSim_TVLSI#C4** — There is a sweet spot in Rmax/Rmin — _support:_ best ratio ~8 (vary Rmin) or ~5 — _loc:_ Fig. 12

## Results
- Simulation 14x slower than native GPU (GTX 1080 Ti) fixed-point training at batch 128, 64x64 crossbars (Fig. 7)
- 3%-36.4% accuracy degradation across benchmarks incl. ResNet-56/CIFAR-100 and ResNet-18/Tiny-ImageNet
- Larger crossbars slightly lower accuracy; wire parasitics minor for ReRAM/PCM but prominent for low-resistance devices such as spintronics

## Key numbers
- array_size: 64x64
- throughput: 6x-108x faster than prior simulators
- accuracy: 3%-36.4% training accuracy degradation
- bits_weight: 32b digital (2b devices)

## Datasets / benchmarks
MNIST, CIFAR-10, CIFAR-100, Tiny-ImageNet

## Limitations
- Single device model (Ag/Si ReRAM); no drift, retention or endurance
- Conductance variation/IR drop evaluated with specific 64x64 setting
- No transformers or language models
- AAM invalid for low Rmin/Rmax ranges
- Not validated against silicon

## Remarks
A solid 2021 reference simulator for training on analog crossbars with detailed parasitic modelling. Useful for the collection's non-ideality and training-in-the-loop themes, but it targets CNNs/MLPs and 32-bit digital data paths, so it says nothing directly about LM mapping. Evidence is simulation only.

## Cites (in collection, 6)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Various efforts that propose crossbar-based training architectures [11-13] also develop performance and energy models to evaluate them."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "MNSIM [21] is a tool for early design space exploration of such architectures."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _contrasts/critiques_: "Prior efforts on functional modeling of crossbar-based DNN hardware can be broadly classified into efforts that model inference [14-16] and efforts that model training [12, 14]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _contrasts/critiques_: "Inference modeling. [15, 16, 17, 18] are modeling tools that consider the impact of non-idealities in crossbar-based inference."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _uses-method-or-tool_: "We conservatively assume 32-bit precision for all data structures (viz.) weights, activations and errors in DNN training based on the scheme proposed in [30], since it provides classification accuracy close to floating-point training [31]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)

## Cited by (in collection, 9)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _data/numbers_: "Fig. 34. (a) Test accuracy versus epoch plots for various models, such as LeNet-5 and AlexNet, showing a more detrimental effect of device and circuit nonidealities for the deeper network (AlexNet). (b) Sensitivity of test accuracy to crossbar design parameters, such as crossbar size and RON/ROFF ratio (reprinted from [151])."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _motivation_: "However, this hardware-integrated re-training can lead to a huge increase in the overall training cost in terms of GPUhours [16, 17, 20]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Due to the analog nature of computations in X-Former, functional errors are introduced in the inference pass that impacts the overall application level accuracy [33], [34]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _contrasts/critiques_: "We chose to intentionally ignore static crossbar effects that would change the conductance value systematically55,60, since read–write-verify conductance programming can readily adapt to such effects."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _uses-method-or-tool_: "The noisy conductance G′ under write noise [12, 25] is given as G′ = G + ñW , where the write noise ñW is modelled as:"
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_Cao_NonIdealitiesAwareCoDesign_JETCAS](2022_Cao_NonIdealitiesAwareCoDesign_JETCAS.md) Non-Idealities Aware Co-Design (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2021_Roy_TxSim_TVLSI.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2021_Roy_TxSim_TVLSI.pdf)
- Full text: [../fulltext/2021_Roy_TxSim_TVLSI.txt](../fulltext/2021_Roy_TxSim_TVLSI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tvlsi.2021.3063543
