---
id: W2946522000
key: 2019_He_NoiseInjectionAdaption_DAC
title: "Noise Injection Adaption"
short: "NIA / PytorX"
year: 2019
venue: "DAC"
venue_full: "56th ACM/IEEE Design Automation Conference (DAC 2019); full title: \"Noise Injection Adaption: End-to-End ReRAM Crossbar Non-ideal Effect Adaption for Neural Network Mapping\""
authors: "Zhezhi He, Jie Lin, Rickard Ewetz, Jiann Shiun Yuan, Deliang Fan"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["noise-injection", "hardware-aware-training", "ir-drop-parasitics", "stuck-at-faults", "read-write-noise", "simulator", "calibration-compensation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 23
cites_in_collection: 4
citations_overall: 150
priority_score: 8.66
doi: "https://doi.org/10.1145/3316781.3317870"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2019_He_NoiseInjectionAdaption_DAC.pdf"
fulltext: "../fulltext/2019_He_NoiseInjectionAdaption_DAC.txt"
---

# NIA / PytorX

**Noise Injection Adaption** — 56th ACM/IEEE Design Automation Conference (DAC 2019); full title: "Noise Injection Adaption: End-to-End ReRAM Crossbar Non-ideal Effect Adaption for Neural Network Mapping" (2019)

## TL;DR
PytorX (PyTorch crossbar simulator) plus a one-time digital SAF error-correction and an IR-drop Noise Injection Adaption training method; SAF correction keeps ResNet-20/CIFAR-10 at 92.23% vs 92.39% SAF-free, while naive mapping onto 64x64 crossbars loses >65% accuracy from IR drop.

## Summary
The paper studies five ReRAM-crossbar non-idealities (stuck-at faults, IR drop, thermal noise, shot noise, random telegraph noise) when a crossbar acts as a DNN dot-product engine. It builds PytorX, a GPU-friendly PyTorch framework modelling differential (G+/G-) weight mapping, weight partition over multiple MxM arrays, DAC/ADC conversion and the non-idealities (IR drop via a simplified modified-nodal-analysis solver). For SAF, a digital error-correction step uses one-time profiling of SA0/SA1 cells and adds the computed output difference to the crossbar output, with no retraining. For IR drop, exact solver-in-the-loop training was infeasible (LeNet-5 used 64 GB RAM and days on 4 TitanX), so NIA profiles the current shift per crossbar, fits it as additive Gaussian-like noise on crossbar outputs and retrains once, independent of the specific chip. Thermal/shot/RTN noise are handled by lowering operating frequency (10 MHz vs 1 GHz). Evaluation uses LeNet-5/MNIST and ResNet-20/CIFAR-10 with 8-bit ADC/DAC and 7-bit ReRAM, crossbars 32/64/128.

## Contributions
- PytorX: end-to-end training/mapping/evaluation framework combining SAF, IR drop, thermal, shot and RTN noise
- Digital SAF error-correction algorithm needing one-time profiling and no retraining
- Noise Injection Adaption: statistical IR-drop noise injected into training for one-time chip-independent robustness
- Finding that operating-frequency tuning suppresses thermal/shot/RTN noise; SAF and IR drop dominate

## Key claims (stable IDs)
- **2019_He_NoiseInjectionAdaption_DAC#C1** — Directly mapping a trained network onto a 64x64 crossbar with IR drop loses >65% accuracy — _support:_ >65% degradation — _loc:_ Sec. 4.3 / Table 2
- **2019_He_NoiseInjectionAdaption_DAC#C2** — SAF error correction recovers near SAF-free accuracy on ResNet-20/CIFAR-10 — _support:_ 92.23 +/- 0.08% worst case vs 92.39% SAF-free — _loc:_ Sec. 4.2 / Fig. 2
- **2019_He_NoiseInjectionAdaption_DAC#C3** — 128x128 crossbars are impractical due to IR drop — _support:_ voltage-drop surfaces — _loc:_ Fig. 3
- **2019_He_NoiseInjectionAdaption_DAC#C4** — Lowering frequency to 10 MHz keeps conductance fluctuation within quantization boundary — _support:_ Monte Carlo 10000 trials — _loc:_ Fig. 5

## Results
- SAF-free ResNet-20 CIFAR-10 accuracy 92.39%; with error correction worst case 92.23% (Fig. 2)
- SAF defect rates of interest 1.75%/9.04% taken from fabrication data
- NIA greatly reduces IR-drop accuracy loss on MNIST for 32/64/128 crossbars (Table 2; numbers not recoverable in extracted text)
- At 1 GHz, thermal/shot noise buries the signal (negative conductance observed); at 10 MHz variation within +/-dG (Fig. 5)

## Key numbers
- array_size: 32x32, 64x64, 128x128
- accuracy: 92.23% CIFAR-10 ResNet-20 with SAF correction (92.39% SAF-free)
- bits_weight: 7b ReRAM
- bits_adc: 8b ADC / 8b DAC

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Only MNIST and CIFAR-10 small CNNs
- Purely simulated; no silicon
- NIA accuracy excludes thermal, shot and RTN noise
- IR-drop noise approximated statistically; Table 2 values garbled in extraction
- No language models

## Remarks
Early, influential simulation-based study showing that naive deployment fails and that noise-injection retraining plus cheap digital compensation can recover accuracy. Evidence is simulation only on tiny models, so conclusions about wire-resistance scale to transformers are extrapolation. Related to RxNN and other crossbar non-ideality simulators in the collection.

## Cites (in collection, 4)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Software approach: Other recent works [2, 3, 9] have adopted different methods that all require retraining the weights of target DNN to be mapped in a crossbar array w.r.t various non-ideal effects for the specific device."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _uses-method-or-tool_: "For simplicity, we adopt the naive network partition method similar as introduced in [16], which converts the weight tensor of each convolution/fully-connected layer into two"
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "ACM ISBN 978-1-4503-6725-7/19/06. . . $15.00 https://doi.org/10.1145/3316781.3317870 promising candidates as the basic computing unit for neural network accelerator design [5, 7]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _motivation_: "However, many non-ideal effects, such as wire resistance, Stuck-At-Fault (SAF), thermal noise, shot noise, random telegraph noise, etc. [9], are hampering the progress of real hardware implementation of large-scale deep neural network (DNN) on ReRAM crossbar-based accelerator."

## Cited by (in collection, 23)
- [2019_Angizi_AnalogVsDigitalPIM_ISVLSI](2019_Angizi_AnalogVsDigitalPIM_ISVLSI.md) Analog vs Digital PIM (2019) — _motivation_: "However, many non-ideal effects, such as IR-drop (i.e., wire resistance), Stuck-At-Fault (SAF), thermal noise, shot and random telegraph noise [16], are hampering the progress of real hardware implementation of large-scale DNNs on ReRAM crossbar-based accelerators."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _contrasts/critiques_: "Inference modeling. [15, 16, 17, 18] are modeling tools that consider the impact of non-idealities in crossbar-based inference."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _baseline/comparison_: "PytorX[12] and FTNNA[24] are designed for neural network applications with the consideration of non-ideal effects."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _uses-method-or-tool_: "To evaluate our proposed training algorithm, we build a comprehensive simulation framework based on PytorX [15], a simulator based on the PyTorch and implemented by Python."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _motivation_: "However, due to the immaturity of fabrication process combined with stochastic filament-based switching, ReRAM suffers from the resistance variations problem [10] [11], manifested as the deviation of actual resistance from its target value."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "In [106], the authors estimated the error contributed by SAF cells and recovered accuracy by additional CMOS circuits."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "A common approach is to add noise to weights and activations during forward propagation [28, 32, 34, 36, 44]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _contrasts/critiques_: "He et al. [27] investigated the integration of stochastic noise during the training process, but their method failed to reach the desired DNN inferencing accuracy."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _motivation_: "For example, the IR drop caused by wire resistance lead to a huge voltage drop at the target cell and limits the number of columns that can be executed at the same time [8, 11, 24]."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _uses-method-or-tool_: "Finally, we perform a hardware-aware training for the DNN by splitting the conv and FC layers into partial operations based on the IMC crossbar size (we use 64×64 [13])."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _background_: "We do not offer comparisons with software-oriented schemes such as those based on error correcting codes and architectures40–43, because they are orthogonal solutions that can be paired with any device redundancy-based fault tolerance scheme."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "NVM devices are susceptible to non-idealities arising from various factors including process variations, temperature fluctuations, conductance drift, and IR drop, among others [13] [14]."
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2026_Sharma_HatFi_VTS](2026_Sharma_HatFi_VTS.md) HATFI (2026)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2019_He_NoiseInjectionAdaption_DAC.pdf](../../07_Hardware_Aware_Training_and_Robustness/2019_He_NoiseInjectionAdaption_DAC.pdf)
- Full text: [../fulltext/2019_He_NoiseInjectionAdaption_DAC.txt](../fulltext/2019_He_NoiseInjectionAdaption_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3316781.3317870
