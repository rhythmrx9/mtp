---
id: W3127794782
key: 2021_Huang_MixedPrecisionQuant_ASP-DAC
title: "Mixed Precision Quantization for ReRAM-based DNN Inference Accelerators"
short: "MPQ ReRAM"
year: 2021
venue: "ASP-DAC"
venue_full: "26th Asia and South Pacific Design Automation Conference (ASP-DAC 2021)"
authors: "Sitao Huang, Aayush Ankit, Plínio Silveira, Rodrigo Antunes, Sai Rahul Chalamalasetti, Izzat El Hajj, Dong Eun Kim, Glaucimar Aguiar, Pedro Bruel, Sergey Serebryakov, Cong Xu, Can Li et al."
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["mixed-precision", "quantization", "adc-dac", "bit-slicing", "peripheral-circuits", "energy-efficiency", "cnn-accelerator", "nas-codesign"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 10
citations_overall: 40
priority_score: 5.72
doi: "https://doi.org/10.1145/3394885.3431554"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Huang_MixedPrecisionQuant_ASP-DAC.pdf"
fulltext: "../fulltext/2021_Huang_MixedPrecisionQuant_ASP-DAC.txt"
---

# MPQ ReRAM

**Mixed Precision Quantization for ReRAM-based DNN Inference Accelerators** — 26th Asia and South Pacific Design Automation Conference (ASP-DAC 2021) (2021)

## TL;DR
Jointly quantizes weights, inputs and ADC partial sums per layer for ReRAM inference accelerators using a deep-RL search, cutting LeNet inference energy by up to 4.84x and latency by 3.89x at 1.18% accuracy loss on PUMAsim.

## Summary
Digital-oriented quantization flows target weights and activations only, but in ReRAM crossbars ADCs dominate energy and latency (ADC is the largest energy component of a 16-bit MVM; a 128x128 crossbar read with one 1 GHz ADC takes 128 ns versus 5-20 ns without ADC). The paper defines three knobs per layer: weight bit-width (changed by the number of 2-bit-per-cell crossbars, since more bits per cell worsen non-idealities per GENIEx), input bit-width (number of 1-bit input slices streamed) and partial-sum (ADC) resolution. Table 1 assumes conservatively that ADC power falls linearly with resolution. Because the design space is large and non-linear, the search is formulated as an RL problem (agent selects (input, weight, ADC) bit-widths per layer; reward combines accuracy cost = Loss_quant - Loss_original with energy/latency from the simulator). A functional simulator models the quantization scheme and PUMAsim (a cycle-level simulator for PUMA, extended to set ADC resolution) gives energy and latency. LeNet search ran 3,000 episodes (converging within 600) and VGG16 600 episodes.

## Contributions
- Quantization scheme jointly targeting weights, inputs and partial sums for ReRAM crossbars with a functional simulator
- Automated mixed-precision flow powered by deep reinforcement learning
- Evaluation of the joint impact of the three quantizations on energy and latency

## Key claims (stable IDs)
- **2021_Huang_MixedPrecisionQuant_ASP-DAC#C1** — Up to 4.84x energy and 3.89x latency savings with only 1.18% accuracy loss on LeNet — _support:_ LeNet: energy 850.99 uJ to 175.61 uJ (4.84x), latency 2.95 ms to 0.76 ms (3.89x), accuracy 97.27% to 96.09% — _loc:_ Table 3, Sec. 5
- **2021_Huang_MixedPrecisionQuant_ASP-DAC#C2** — Similar savings are found for VGG16 — _support:_ stated without full table — _loc:_ Sec. 5
- **2021_Huang_MixedPrecisionQuant_ASP-DAC#C3** — Partial-sum quantization is under-explored but ADC-dominated — _support:_ ADC dominates energy and area (Fig. 2) — _loc:_ Sec. 2, Fig. 2, Table 1

## Results
- Search converges within 600 episodes for LeNet (3,000 run)
- Schemes with higher accuracy but lower savings (e.g. Q_c) are also discovered, giving an accuracy-energy trade-off front
- Latency and energy are more sensitive to input and weight bit-width than ADC precision in some regions; design space non-linear (Fig. 4)

## Key numbers
- array_size: 128x128, 2 bits/cell
- energy_eff: 4.84x energy saving (LeNet)
- throughput: 3.89x latency reduction
- accuracy: 96.09% (-1.18%) LeNet
- bits_weight: mixed, 2 bits/cell
- bits_adc: mixed, baseline 8b

## Limitations
- Small models (LeNet, VGG16) and short paper; VGG16 results only summarized
- Linear ADC power-vs-resolution assumption
- Fixed 2 bits/cell and 1-bit input slices; non-idealities not simulated
- No transformers or language models
- Datasets are not named in the extracted text for the LeNet/VGG16 experiments

## Remarks
Early work that makes ADC resolution a per-layer search variable alongside weight and input precision; conceptually related to BWQ and extreme partial-sum quantization in the collection. Evidence is limited by tiny models and a modest accuracy evaluation.

## Cites (in collection, 10)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _data/numbers_: "Consequently, even with an ADC working at very high sampling frequency such as 1GHz, a crossbar read operation requires 128 ns, while typical crossbar reads without ADC require 5-20 ns [17]."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _uses-method-or-tool_: "To evaluate the impact of different quantization schemes on DNN inference energy consumption and latency, we use the PUMA [15] simulator, PUMAsim, which is a cycle-level architecture simulator for ReRAM-based accelerators."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _contrasts/critiques_: "Zhu et al. [29] provide a framework for quantizing CNNs on single-bit ReRAM crossbars."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "Hence, this work assumes a fixed two bits of weights are stored in each crossbar cell [13] and implements weight quantization by varying the number of crossbars used to store the weights."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _motivation_: "However, the impact of device-circuit non-idealities in the crossbar (both linear and non-linear) increases with increasing bits per crossbar cell leading to significant losses in network accuracy [16]."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."

## Cited by (in collection, 4)
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _baseline/comparison_: "SW-based optimization solution ReCom [13] and MPQ [14] proactively compress the models with algorithms."
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _background_: "Similarly, several frameworks optimize quantization policies to enhance the performance of CIM-based architectures [29–31]."
- [2023_Bai_CIMQ_TCAD](2023_Bai_CIMQ_TCAD.md) CIMQ (2023)
- [2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED](2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.md) ADC-Less CiM Partial-Sum Quant (2023)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Huang_MixedPrecisionQuant_ASP-DAC.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Huang_MixedPrecisionQuant_ASP-DAC.pdf)
- Full text: [../fulltext/2021_Huang_MixedPrecisionQuant_ASP-DAC.txt](../fulltext/2021_Huang_MixedPrecisionQuant_ASP-DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3394885.3431554
