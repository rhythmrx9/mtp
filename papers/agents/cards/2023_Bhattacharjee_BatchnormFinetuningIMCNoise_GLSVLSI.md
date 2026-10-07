---
id: W4378800995
key: 2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI
title: "Examining the Role and Limits of Batchnorm Optimization to Mitigate Diverse Hardware-noise in In-memory Computing"
short: "BN-Finetune-IMC"
year: 2023
venue: "GLSVLSI"
venue_full: "Proceedings of the Great Lakes Symposium on VLSI 2023 (GLSVLSI '23), ACM"
authors: "Abhiroop Bhattacharjee, Abhishek Moitra, Youngeun Kim, Yeshwanth Venkatesha, Priyadarshini Panda"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["FeFET", "PCM", "ReRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "calibration-compensation", "read-write-noise", "conductance-drift", "ir-drop-parasitics", "device-variation", "on-chip-training", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 12
citations_overall: 11
priority_score: 6.35
doi: "https://doi.org/10.1145/3583781.3590241"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.pdf"
fulltext: "../fulltext/2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.txt"
---

# BN-Finetune-IMC

**Examining the Role and Limits of Batchnorm Optimization to Mitigate Diverse Hardware-noise in In-memory Computing** — Proceedings of the Great Lakes Symposium on VLSI 2023 (GLSVLSI '23), ACM (2023)

## TL;DR
Fine-tuning only the digital batchnorm gamma/beta (5 epochs, conv weights frozen on crossbars) recovers accuracy lost to read noise, drift and parasitics while the non-linear weight distortion (PCA PC2) stays below ~1e-2, saving ~95%/52% training memory and ~8% training energy.

## Summary
The authors ask when cheap, nearly training-less correction of crossbar non-idealities is enough. Conv layers of pre-trained VGG16/CIFAR10 (88.62%) and ResNet-18/TinyImagenet (51.80%) are mapped on analog crossbars (8-bit weights from 4-bit cells, 64x64 and 128x128 RRAM, FeFET, PCM-i/ii devices of Table 1) with BN, pooling, activations and classifier in digital CMOS. Non-idealities are stochastic Gaussian read noise (sigma 0.05-0.35), temporal drift G(T) with exponent nu, and resistive parasitics (R_driver 1k, R_wire 5/10 ohm, R_sense 1k) via a crossbar-aware framework. They quantify the non-linear shift between ideal and non-ideal weights (W_ideal vs W_NI) with the second principal component PC2, then compare BN adaptation (recomputing statistics) with BN fine-tuning (gamma, beta, lr 0.01 dropped 5x every 2 epochs) as a function of PC2, device ON/OFF ratio, retention time and crossbar size, and estimate training memory/energy savings.

## Contributions
- Crossbar-noise-aware batchnorm adaptation/fine-tuning as a nearly training-less mitigation
- Holistic analysis of read noise, drift and parasitic resistance on conv weights across FeFET, PCM and RRAM
- PC2 (PCA-based) metric predicting when BN-only correction suffices (PC2 < ~1e-2)
- Quantified savings in on-hardware training memory and energy

## Key claims (stable IDs)
- **2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI#C1** — BN fine-tuning preserves accuracy on FeFET crossbars until PC2 < 1e-2 (sigma 0.15-0.2 for VGG16/CIFAR10; sigma 0.1, PC2=2.92e-3 for ResNet-18/TinyImagenet) — _support:_ Fig. 6 — _loc:_ Sec. 4.1 / Fig. 6
- **2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI#C2** — Simple BN adaptation fails beyond sigma 0.1 (PC2=2.71e-3); at sigma 0.15 (PC2=6.03e-3) accuracy is 77.89% — _support:_ VGG16/CIFAR10 — _loc:_ Sec. 4.1
- **2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI#C3** — Higher ON/OFF ratio lowers PC2 and raises accuracy: PCM-i (40) 82.0%, PCM-ii (80) 86.81%, RRAM (10) 84.07% after BN fine-tuning — _support:_ Fig. 7 — _loc:_ Sec. 4.1
- **2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI#C4** — With drift, BN fine-tuning cuts accuracy loss at T=1e10 s from 76.5%/26.1% to 5.0%/8.0% (VGG16/ResNet-18) — _support:_ Fig. 8 — _loc:_ Sec. 4.2
- **2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI#C5** — Parasitic non-idealities alone are fully mitigated by BN fine-tuning: 64x64 74.37->87.97%, 128x128 32.9->87.81% — _support:_ Fig. 10 — _loc:_ Sec. 4.3
- **2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI#C6** — ~95% and ~52% training-memory savings, ~8% training-energy savings — _support:_ VGG16/CIFAR10 and ResNet-18/TinyImagenet — _loc:_ Sec. 5 / Fig. 11

## Results
- FeFET VGG16/CIFAR10 at sigma 0.05: PC2 6.90e-4, 87.78% after BN adaptation
- Drift: BN-adaptation retention ~1e4-1e5 s on FeFET; BN fine-tuning keeps accuracy to 1e10 s with 5.0%/8.0% loss
- RRAM 64x64 parasitics: 74.37% -> 86.31% (BN adaptation) -> 87.97% (BN fine-tune); 128x128: 32.9% -> 83.03% -> 87.81%
- Parasitics + sigma 0.1 read noise on RRAM: 62.28% (27.86%) -> 83.22% (81.59%) after BN fine-tuning
- Training memory savings ~95% (VGG16) and ~52% (ResNet-18); training energy ~8%

## Key numbers
- array_size: 64x64, 128x128
- energy_eff: ~8% training-energy reduction
- accuracy: 87.97% VGG16/CIFAR10 (64x64 RRAM, parasitics, BN fine-tune); FeFET 87.78% at sigma 0.05
- bits_weight: 8b (4b cells)

## Datasets / benchmarks
CIFAR-10, TinyImageNet

## Limitations
- Only conv layers on crossbars; BN, classifier and activations digital and assumed ideal
- Small CNN benchmarks (CIFAR10, TinyImagenet); no transformers or LMs (LayerNorm analog not studied)
- Fails beyond PC2 ~1e-2; high noise still needs weight-level retraining
- Simulation only; noise models (Gaussian read noise, simple drift) are simplified
- Energy savings from reused data of a prior framework (~8%)

## Remarks
A clean boundary study giving a simple diagnostic (PC2) for when affine digital correction suffices; the idea transfers conceptually to LayerNorm/scale correction in transformers but is not demonstrated on LMs. Its low-cost recalibration view contrasts with heavy hardware-aware retraining such as AIHWKit-based HWA training. Evidence is simulation on small vision CNNs.

## Cites (in collection, 12)
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _data/numbers_: "We achieve ∼ 8% reduction in training-energy for both models, calculated based on the data in [14]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _uses-method-or-tool_: "In recent years, several noise models [2, 19, 26] and crossbar-realistic DNN accuracy evaluation frameworks (Neurosim [17], RxNN [10], GenieX [6], Memtorch [13]) have been proposed that are integrated with hardware-aware re-training or fine-tuning of GPU-trained DNN weights, to mitigate performance losses during inference"
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _extends/builds-on_: "Drift noiseaware BN adaptation can maintain the accuracy of crossbar-mapped DNNs till a retention time T beyond which the accuracy dramatically decreases [12]."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _motivation_: "However, this hardware-integrated re-training can lead to a huge increase in the overall training cost in terms of GPUhours [16, 17, 20]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "In recent years, several noise models [2, 19, 26] and crossbar-realistic DNN accuracy evaluation frameworks (Neurosim [17], RxNN [10], GenieX [6], Memtorch [13]) have been proposed that are integrated with hardware-aware re-training or fine-tuning of GPU-trained DNN weights, to mitigate performance losses during inference"
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "In-Memory Computing (IMC) systems, such as analog crossbar-arrays that alleviate the ‘memory-wall’ bottleneck of von-Neumann architectures are gaining popularity [21]."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _background_: "In recent years, several noise models [2, 19, 26] and crossbar-realistic DNN accuracy evaluation frameworks ... have been proposed that are integrated with hardware-aware re-training or fine-tuning of GPU-trained DNN weights"
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _motivation_: "However, this hardware-integrated re-training can lead to a huge increase in the overall training cost in terms of GPUhours [16, 17, 20]."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _background_: "For works that support on-chip training and inference using realistic IMC crossbar platforms for forward and backward propagation stages, fine-tuning (or re-programming) the weights (or memristive conductances) of a pre-trained DNN on hardware to mitigate accuracy losses due to noise and quantization effects becomes highly compute- & memory-intensive [11, 17, 18]."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021) — _uses-method-or-tool_: "Fig. 1 indicates the various resistive non-idealities, viz. 𝑅𝑑𝑟𝑖𝑣𝑒𝑟 , 𝑅𝑤𝑖𝑟𝑒_𝑟𝑜𝑤, 𝑅𝑤𝑖𝑟𝑒_𝑐𝑜𝑙 and 𝑅𝑠𝑒𝑛𝑠𝑒, prevalant in crossbars [3, 10]."
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023) — _background_: "Analog IMC platforms are susceptible to various non-idealities arising from the device-to-device variations and temporal conductance drift of the memristive devices as well as from the parasitic resistances of the metallic interconnects in the crossbar-arrays [2, 6, 10, 22]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _contrasts/critiques_: "This shows that resistive non-idealities, although can disrupt a DNN’s performance on crossbars, can be totally mitigated with the help of BN fine-tuning, without the need for parasitic noise-aware re-training of weights as proposed in [16, 19, 20]."

## Cited by (in collection, 4)
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _background_: "Previous works have demonstrated the effectiveness of using NVM devices with higher ON/OFF ratios to reduce read variations during inference of deep neural networks [14], [29]–[31]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _contrasts/critiques_: "Note that this in-memory training approach is radically different from hardware-aware training typically employed when using analog crossbar arrays for DNN inference only (e.g.,32,41,42)."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _motivation_: "However, this is challenging due to the accumulation of noise from the non-ideal behavior of memristors [45][46][47]."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _background_: "The IR-drop and transistor non-linearity noise follow a structured profile and can be mitigated using simple approaches such as batchnorm adaptation and weight retraining [28], [30]."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.pdf](../../07_Hardware_Aware_Training_and_Robustness/2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.pdf)
- Full text: [../fulltext/2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.txt](../fulltext/2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3583781.3590241
