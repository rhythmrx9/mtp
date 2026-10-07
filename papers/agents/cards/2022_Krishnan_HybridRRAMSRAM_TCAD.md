---
id: W4293243554
key: 2022_Krishnan_HybridRRAMSRAM_TCAD
title: "Hybrid RRAM/SRAM in-Memory Computing for Robust DNN Acceleration"
short: "Hybrid RRAM/SRAM IMC"
year: 2022
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022); also presented at CASES 2022 as part of the ESWEEK-TCAD special issue"
authors: "Gokul Krishnan V, Zhenyu Wang, Injune Yeo, Li Yang, Jian Meng, Maximilian Liehr, Rajiv Joshi, Nathaniel C. Cady, Deliang Fan, Jae-sun Seo, Yu Kevin Cao"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM", "SRAM-digital"]
models: ["CNN", "ResNet", "VGG", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["heterogeneous-analog-digital", "device-variation", "calibration-compensation", "hardware-aware-training", "quantization", "pruning-sparsity", "macro", "chip-demo"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 9
citations_overall: 31
priority_score: 6.46
doi: "https://doi.org/10.1109/tcad.2022.3197516"
pdf: "../../06_Nonidealities_and_Reliability/2022_Krishnan_HybridRRAMSRAM_TCAD.pdf"
fulltext: "../fulltext/2022_Krishnan_HybridRRAMSRAM_TCAD.txt"
---

# Hybrid RRAM/SRAM IMC

**Hybrid RRAM/SRAM in-Memory Computing for Robust DNN Acceleration** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022); also presented at CASES 2022 as part of the ESWEEK-TCAD special issue (2022)

## TL;DR
A parallel digital SRAM+MAC macro with a programmable shifter compensates RRAM multilevel-cell variation, improving post-mapping accuracy by up to 21.9%/12.65%/6.52% (ResNet-20, VGG-16 on CIFAR-10; ResNet-18 on ImageNet) at <=20% area and <=2.6% power overhead, with a 65nm test chip.

## Summary
Multilevel RRAM cells suffer large device variation (lognormal) that causes severe post-mapping accuracy loss. The proposed hybrid architecture splits each weight into a coarse part stored in a 64x64 1T1R RRAM IMC macro (3-bit flash ADC, 8-to-1 column mux, up to 3-bit/8-level cells from a measured SUNY 65nm 1T1R device) and a sparse residual stored in a small digital SRAM macro with MAC units; the SRAM output compensates the non-ideal RRAM output, and a programmable shifter scales the compensation (different compensation scales). The training framework performs quantization, group-wise structured pruning of the SRAM weights, RRAM-variation-aware training (variation injected per epoch from measured device data, bitwise per Table I), and ensemble learning across compensation scales. A 65nm test chip (RRAM macro + SRAM macro + scan chain; shifter off-chip; 100 MHz) provides post-layout area/power. Evaluated on ResNet-20/VGG-16 (CIFAR-10), ResNet-18 and MobileNet-v2 (ImageNet) versus variation-aware training (VAT) and other techniques.

## Contributions
- Hybrid RRAM/SRAM IMC architecture with programmable shifter for variation compensation
- Training framework: quantization, structured pruning, RRAM IMC-aware training and ensemble learning over compensation scales
- Experimental evaluation showing MLC RRAM becomes usable despite high variation
- 65nm SUNY test chip validating the architecture and overhead analysis

## Key claims (stable IDs)
- **2022_Krishnan_HybridRRAMSRAM_TCAD#C1** — Up to 21.9%, 12.65% and 6.52% post-mapping accuracy improvement over state of the art for ResNet-20/CIFAR-10, VGG-16/CIFAR-10 and ResNet-18/ImageNet — _support:_ abstract numbers — _loc:_ Abstract / Sec. V
- **2022_Krishnan_HybridRRAMSRAM_TCAD#C2** — Versus VAT at same RRAM precision: +3.3% ResNet-20, +1.7% VGG-16, +5.4% ResNet-18, +25% MobileNet-v2 — _support:_ Table III — _loc:_ Sec. V-D / Table III
- **2022_Krishnan_HybridRRAMSRAM_TCAD#C3** — Hybrid VGG-16 reaches 92.97% vs 93.04% FP-32; ResNet-20 90.92% vs 91.34% — _support:_ best configuration — _loc:_ Sec. V-C
- **2022_Krishnan_HybridRRAMSRAM_TCAD#C4** — SRAM macro pruning ratio >87% for all networks except MobileNet-v2 — _support:_ VGG-16 95-98.9% pruning — _loc:_ Sec. V-D
- **2022_Krishnan_HybridRRAMSRAM_TCAD#C5** — Overheads: memory up to 24%, area up to 20%, power up to 2.6%, training time up to 25% — _support:_ post-layout from 65nm test chip — _loc:_ Sec. V-F / Fig. 11

## Results
- FP-32 baselines: ResNet-20 91.32%, VGG-16 93.04%, ResNet-18 69.57%, MobileNet-v2 71.87%
- VGG-16 3b RRAM + 2b SRAM, 2-bit shift: 92.76% at 95% SRAM pruning; 3b SRAM 0-bit shift: 92.75% at 98.9% pruning
- Device supports up to 8 levels (3-bit) in 65nm 1T1R; HRS has higher variation than LRS
- Test chip: 64x64 1T1R RRAM macro, 3-bit flash ADC, 100 MHz

## Key numbers
- tech_node: 65nm SUNY
- array_size: 64x64
- accuracy: VGG-16 CIFAR-10 92.97% vs 93.04% FP-32
- bits_weight: up to 3b RRAM + 3b SRAM
- bits_adc: 3b flash ADC

## Datasets / benchmarks
CIFAR-10, ImageNet

## Limitations
- Shifter implemented off-chip on the test chip; full system not integrated
- Evaluated on CNNs only; no transformers or LMs
- Extra SRAM macro, pruning and ensemble training overhead (up to 25% training time)
- Variation modelled as lognormal per device; drift and IR drop not the focus
- Small crossbar (64x64); accuracy of MobileNet-v2 still needs high compensation

## Remarks
A silicon-validated hybrid analog/digital compensation scheme that is conceptually relevant to LMs: outlier or sensitive weights can be kept in a small digital residual while the bulk runs on noisy analog arrays. Evidence is partly measured (device data and test-chip area/power) and partly simulated (accuracy). Related to the collection's variation-aware training, GENIEx and unary-coding mapping work.

## Cites (in collection, 9)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _baseline/comparison_: "[7, 24] utilize VAT based on known device variation (σ) characterized from RRAM devices, while [5] combines VAT with dynamic precision"
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "RRAM-based IMC architectures provide a promising alternative to conventional von-Neumann architectures [2–4, 8, 19– 21]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _uses-method-or-tool_: "Finally, we perform a hardware-aware training for the DNN by splitting the conv and FC layers into partial operations based on the IMC crossbar size (we use 64×64 [13])."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _motivation_: "However, RRAM device suffers from several non-idealities such as limited resistance levels, device-to-device write variations, stuck-at-faults, and limited Roff /Ron ratio, posing a signiﬁcant challenge to designing reliable RRAM-based IMC architectures [5–12]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _motivation_: "However, RRAM device suffers from several non-idealities such as limited resistance levels, device-to-device write variations, stuck-at-faults, and limited Roff /Ron ratio, posing a signiﬁcant challenge to designing reliable RRAM-based IMC architectures [5–12]."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _background_: "To mitigate the post-mapping accuracy loss in DNNs, variation-aware training (VAT) and special encoding schemes are employed [5–9, 13]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _motivation_: "However, RRAM device suffers from several non-idealities such as limited resistance levels, device-to-device write variations, stuck-at-faults, and limited Roff /Ron ratio, posing a signiﬁcant challenge to designing reliable RRAM-based IMC architectures [5–12]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Prior works with RRAM-based crossbar architectures have shown up to 1,000× improvement in energy efﬁciency as compared to CPUs/GPUs [2–4]."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019)

## Cited by (in collection, 3)
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "Existing work related to CIM has investigated the implementation of small-scale neural networks [1, 7, 8]."
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2022_Krishnan_HybridRRAMSRAM_TCAD.pdf](../../06_Nonidealities_and_Reliability/2022_Krishnan_HybridRRAMSRAM_TCAD.pdf)
- Full text: [../fulltext/2022_Krishnan_HybridRRAMSRAM_TCAD.txt](../fulltext/2022_Krishnan_HybridRRAMSRAM_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2022.3197516
