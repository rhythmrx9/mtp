---
id: W4386859314
key: 2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED
title: "Partial-Sum Quantization for Near ADC-Less Compute-In-Memory Accelerators"
short: "ADC-Less CiM Partial-Sum Quant"
year: 2023
venue: "ISLPED"
venue_full: "ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED 2023)"
authors: "Utkarsh Saxena, Kaushik Roy"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["Memristor(generic)", "ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["adc-dac", "quantization", "energy-efficiency", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 15
priority_score: 3.34
doi: "https://doi.org/10.1109/islped58423.2023.10244291"
pdf: null
fulltext: null
---

# ADC-Less CiM Partial-Sum Quant

**Partial-Sum Quantization for Near ADC-Less Compute-In-Memory Accelerators** — ACM/IEEE International Symposium on Low Power Electronics and Design (ISLPED 2023) (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
By quantizing crossbar partial sums down to binary (1-bit, sense-amplifier-only, 'ADC-Less') or ternary (1.5-bit, two-comparator, 'near ADC-Less') precision and using a CiM-hardware-aware DNN quantization training method, this paper nearly eliminates ADC overhead, reporting up to 178x latency and 131x TOPS/mm2 improvement over an 8-bit-ADC baseline on ResNet-20/CIFAR-10 with minimal accuracy loss.

## Summary
ADCs are a dominant source of peripheral-circuit overhead in resistive-crossbar compute-in-memory (CiM) DNN accelerators, limiting the efficiency gains promised by analog MVM. This paper proposes eliminating or minimizing that overhead by quantizing the crossbar's partial sums (the per-column analog MVM output before conversion) to extremely low precision: binary (1-bit) partial sums require only a sense amplifier for analog-to-digital conversion, yielding a fully 'ADC-Less' design, while ternary (1.5-bit) partial sums require two comparators, yielding a 'near ADC-Less' design. Because this aggressive partial-sum quantization would otherwise cause large accuracy degradation, the authors develop a CiM-hardware-aware DNN quantization training methodology specifically to mitigate it. The approach is evaluated on CIFAR-10 (ResNet-20) with the fully ADC-Less design and on ImageNet (ResNet-18) with the near-ADC-Less design, reporting high accuracy with minimal degradation alongside large efficiency gains relative to a conventional 8-bit-ADC baseline.

## Contributions
- ADC-Less CiM design: binary (1-bit) partial-sum quantization requiring only a sense amplifier instead of a multi-bit ADC
- Near-ADC-Less CiM design: ternary (1.5-bit) partial-sum quantization requiring only two comparators
- A CiM-hardware-aware DNN quantization training methodology to recover accuracy lost to extreme partial-sum quantization
- Demonstrated large joint energy/latency/area-efficiency gains over an 8-bit-ADC baseline on both CIFAR-10 (ResNet-20) and ImageNet (ResNet-18) with minimal accuracy degradation

## Key claims (stable IDs)
- **2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED#C1** — The ADC-Less design achieves large efficiency gains over an 8-bit-ADC baseline on ResNet-20/CIFAR-10 with minimal accuracy loss — _support:_ 14x energy, 178x latency, and 131x TOPS/mm2 improvement over baseline (8-bit ADC) — _loc:_ Abstract
- **2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED#C2** — The near-ADC-Less design achieves large efficiency gains over an 8-bit-ADC baseline on ResNet-18/ImageNet with minimal accuracy loss — _support:_ 11x energy, 55x latency, and 36x TOPS/mm2 improvement over baseline (8-bit ADC) — _loc:_ Abstract

## Results
- ResNet-20/CIFAR-10, ADC-Less (binary partial sums): 14x energy, 178x latency, 131x TOPS/mm2 vs. 8-bit-ADC baseline
- ResNet-18/ImageNet, near-ADC-Less (ternary partial sums): 11x energy, 55x latency, 36x TOPS/mm2 vs. 8-bit-ADC baseline

## Limitations
- Analysis based on abstract only (full text not accessible); the exact CiM-hardware-aware quantization training method, accuracy numbers (not just 'minimal degradation'), and crossbar/array assumptions could not be verified
- Reducing partial-sum resolution to 1-1.5 bits per crossbar read likely requires many more reads/accumulation steps to reconstruct full precision, a tradeoff not quantifiable from the abstract alone

## Remarks
This is an ADC/peripheral-cost-reduction paper that pushes partial-sum quantization to its logical extreme (binary/ternary), directly extending prior partial-sum quantization work in this same in-set reference list (Kim et al., 'Extreme Partial-Sum Quantization', W4300228436, and the ADC-reduction line including Quarry, W4200001938). The very large reported latency/area gains (up to 178x) for only 1-2 bit ADC precision suggest the technique trades off read-cycle count for ADC simplicity; full-text access would be needed to confirm whether the TOPS/mm2 and latency figures already account for any additional read cycles needed to recover full-precision partial sums.

## Cites (in collection, 6)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/islped58423.2023.10244291
