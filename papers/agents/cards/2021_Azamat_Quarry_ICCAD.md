---
id: W4200001938
key: 2021_Azamat_Quarry_ICCAD
title: "Quarry: Quantization-based ADC Reduction for ReRAM-based Deep Neural Network Accelerators"
short: "Quarry"
year: 2021
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021)"
authors: "Azat Azamat, Faaiz Asim, Jongeun Lee"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["quantization", "adc-dac", "energy-efficiency", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 9
citations_overall: 21
priority_score: 5.24
doi: "https://doi.org/10.1109/iccad51958.2021.9643502"
pdf: null
fulltext: null
---

# Quarry

**Quarry: Quantization-based ADC Reduction for ReRAM-based Deep Neural Network Accelerators** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021) (2021)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Quarry uses advanced quantization techniques (no hardware changes) to shrink the ADC resolution/size needed in ReRAM crossbar DNN accelerators, cutting ADC size 32x versus ISAAC at only 0.24 percentage-point accuracy loss on ImageNet.

## Summary
The paper addresses the well-known ADC overhead problem in ReRAM crossbar DNN accelerators, where peripheral analog-to-digital converters dominate area and/or slow down operation. Instead of changing the crossbar hardware, Quarry applies quantization techniques to reduce the required ADC precision/size, and is presented as general-purpose: it does not restrict the DNN type (binarized or multi-bit weights) or the ReRAM crossbar array size. Experimental results with ResNet on ImageNet show a large reduction in ADC size relative to the ISAAC baseline with only a very small accuracy loss. (Full text was not accessible from this machine; this entry is based on the abstract and OpenAlex metadata only, so method details beyond the abstract — e.g., the specific quantization scheme, whether it requires retraining, and comparisons beyond ISAAC — are not captured here.)

## Contributions
- A quantization-based method to reduce ADC resolution/overhead in ReRAM crossbar DNN accelerators without hardware modification
- A general approach claimed to be independent of DNN type (binarized vs. multi-bit) and crossbar array size
- Experimental demonstration on ResNet/ImageNet showing large ADC size reduction versus ISAAC at minimal accuracy cost

## Key claims (stable IDs)
- **2021_Azamat_Quarry_ICCAD#C1** — Quarry reduces ADC size substantially relative to the ISAAC baseline with negligible accuracy loss — _support:_ 32x reduction in ADC size compared with ISAAC at an accuracy loss of only 0.24 percentage points, measured with ResNet on ImageNet — _loc:_ Abstract
- **2021_Azamat_Quarry_ICCAD#C2** — The method requires no hardware changes and generalizes across DNN/ReRAM configurations — _support:_ Stated in abstract: 'does not require any hardware change' and 'no restriction in terms of DNN type (binarized or multi-bit) or ReRAM crossbar array size' — _loc:_ Abstract

## Results
- 32x reduction in ADC size vs. ISAAC at 0.24 percentage-point accuracy loss (ResNet, ImageNet)

## Limitations
- Analysis based on abstract and metadata only; full methodology, baselines beyond ISAAC, and robustness/noise considerations could not be verified
- No open-access copy found (OpenAlex reports closed access, no repository full text; IEEE Xplore not reachable from this environment)

## Remarks
This entry is abstract-only: a legitimate open copy could not be located (OpenAlex flags the work as closed access with no repository full text, and only IEEE Xplore hosts it). The claimed 32x ADC size reduction at 0.24-point accuracy loss is a strong, specific result in the same vein as other ADC-reduction work in this collection (e.g., TinyADC, Neural-PIM), suggesting a growing consensus that ADC overhead is the dominant cost center of ReRAM crossbar accelerators and that software-only quantization changes (no circuit redesign) can meaningfully attack it. This should be revisited with the full text if institutional IEEE Xplore access becomes available.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018)
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020)
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 3)
- [2023_Bai_CIMQ_TCAD](2023_Bai_CIMQ_TCAD.md) CIMQ (2023)
- [2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED](2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.md) ADC-Less CiM Partial-Sum Quant (2023)
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2021_Azamat_Quarry_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccad51958.2021.9643502
