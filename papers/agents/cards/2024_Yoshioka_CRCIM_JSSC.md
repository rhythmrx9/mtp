---
id: W4402811198
key: 2024_Yoshioka_CRCIM_JSSC
title: "A 818–4094 TOPS/W Capacitor-Reconfigured Analog CIM for Unified Acceleration of CNNs and Transformers"
short: "CR-CIM"
year: 2024
venue: "JSSC"
venue_full: "IEEE Journal of Solid-State Circuits (2024)"
authors: "Kentaro Yoshioka"
category: "02 Fabricated Chips & Macros"
devices: ["SRAM-analog", "Charge/Capacitor"]
models: ["ViT", "CNN", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "analog-mvm", "adc-dac", "peripheral-circuits", "transformer-accelerator", "energy-efficiency", "heterogeneous-analog-digital"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 1
citations_overall: 27
priority_score: 7.54
doi: "https://doi.org/10.1109/jssc.2024.3457898"
pdf: "../../02_Fabricated_Chips_and_Macros/2024_Yoshioka_CRCIM_JSSC.pdf"
fulltext: "../fulltext/2024_Yoshioka_CRCIM_JSSC.txt"
---

# CR-CIM

**A 818–4094 TOPS/W Capacitor-Reconfigured Analog CIM for Unified Acceleration of CNNs and Transformers** — IEEE Journal of Solid-State Circuits (2024) (2024)

## TL;DR
A 65nm charge-domain SRAM CIM macro reuses its compute capacitor array as the 10-bit C-DAC of a SAR ADC, reaching 45 dB SQNR / 31 dB CSNR, 818 TOPS/W (1b-normalised) and 95.8% CIFAR-10 ViT accuracy; the journal version extends to a CNN/Transformer dual mode up to 4094 TOPS/W.

## Summary
Transformers need higher compute SNR than CNNs, and prior analog CIMs (current-, time- or charge-based) have not demonstrated Transformer inference. The macro uses a 10T cell (6T SRAM plus capacitor, 2.3 um2 in 65nm, about 2x a 6T cell) with a custom 1.5 fF fringe capacitor. The capacitor array does charge-domain MAC and is then reconfigured as a binary C-DAC (DDAC[9:0] connected to 512, 256, ... cells) for a 10-bit SAR conversion, keeping signal charge stationary so there is no charge-redistribution attenuation (2x signal swing, equivalent to 2x ADC noise improvement, 4x comparator energy efficiency). A shared DDAC/reset path removes in-cell reset switches. A software-analog co-design (SAC) scheme enables a CSNR-boost (6x majority voting on the last 3 SA comparisons, +5.5 dB, 1.9x power and 2.5x time) only for MLP layers because attention layers need ~10 dB less CSNR, improving Transformer inference efficiency up to 2.1x. The prototype is a 1088x78 array in 65nm. A ViT is run with 4-bit inputs/weights (attention without CSNR boost) and reaches 95.8% CIFAR-10 top-1 vs 96.8% ideal. Weights are held in SRAM so no NVM is involved; accumulation happens in capacitors and digital shift-and-add combines bits.

## Contributions
- Capacitor-reconfiguring CIM: compute capacitors double as the ADC C-DAC (about 2x area saving, no attenuation)
- DDAC/reset sharing 10T cell
- Software-analog co-design: layer-adaptive majority voting for CSNR boost (up to 2.1x Transformer efficiency)
- First analog CIM demonstrating ViT inference; highest reported compute accuracy among analog CIMs

## Key claims (stable IDs)
- **2024_Yoshioka_CRCIM_JSSC#C1** — Highest compute accuracy among analog CIMs — _support:_ SQNR 45.3 dB, CSNR 31.3 dB; 23 dB and 14 dB better than prior charge-based CIMs — _loc:_ Measurement results, Fig. 5-6
- **2024_Yoshioka_CRCIM_JSSC#C2** — Attention layers tolerate ~10 dB lower CSNR than MLP layers — _support:_ CB applied only on MLP — _loc:_ Fig. 4
- **2024_Yoshioka_CRCIM_JSSC#C3** — ViT CIFAR-10 accuracy near ideal — _support:_ 95.8% vs 96.8% ideal — _loc:_ Fig. 6

## Results
- 818 TOPS/W (normalised to 1b x 1b) in the Transformer-oriented configuration; abstract of journal version: 818-4094 TOPS/W across modes
- CSNR-FoM 1.5x and SQNR-FoM 2.3x better than prior analog CIMs
- Column INL within 2 LSB at 10-bit; readout noise 0.58 LSB rms with CB, 2x higher without
- CSNR boost: 25.8 dB -> 31.3 dB with 10 -> 26 comparisons per conversion (1.9x quantizer power)
- 95.8% CIFAR-10 top-1 with ViT-small vs 96.8% ideal

## Key numbers
- tech_node: 65nm
- array_size: 1088x78
- energy_eff: 818 TOPS/W (1b-normalised); up to 4094 TOPS/W in CNN mode (journal abstract)
- accuracy: 95.8% CIFAR-10 (ViT, 4b/4b) vs 96.8% ideal
- bits_weight: 4b-8b (8b input/8b weight bit-serial)
- bits_adc: 10b (8b in CNN mode)

## Datasets / benchmarks
CIFAR-10

## Limitations
- Supplied text is the short conference-style paper (VLSI-style 2-pager with figure text), not the full JSSC article; CNN-mode details (8-bit ADC, 4094 TOPS/W) come only from the packet abstract
- Small ViT on CIFAR-10 only; no language model
- Chip area/cell is about 2x a 6T SRAM cell
- Peak TOPS/W normalised to 1-bit x 1-bit, which inflates headline numbers
- Text extraction contains garbled figure fragments

## Remarks
Important for the argument that analog CIM can reach the SNR needed for transformers by fixing the ADC/quantisation side rather than the memory device. It is SRAM based, so the weight-drift and variation issues of NVM do not appear, but the CSNR-vs-layer insight (attention tolerates less precision than MLP) transfers to NVM crossbar design. Measured silicon but only a ViT demonstration.

## Cites (in collection, 1)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020) — _baseline/comparison_: "These metrics are 23 dB and 14 dB better than the previously reported charge-based CIMs [4,5], showing that CR-CIM and CB techniques lead to high compute accuracy."

## Cited by (in collection, 2)
- [2025_Zhang_ASiM_TVLSI](2025_Zhang_ASiM_TVLSI.md) ASiM (2025) — _extends/builds-on_: "Yoshioka [25] extended this approach by introducing analog Gaussian noise into each binary MAC cycle to estimate the actual CSNR of ACiM chips."
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2024_Yoshioka_CRCIM_JSSC.pdf](../../02_Fabricated_Chips_and_Macros/2024_Yoshioka_CRCIM_JSSC.pdf)
- Full text: [../fulltext/2024_Yoshioka_CRCIM_JSSC.txt](../fulltext/2024_Yoshioka_CRCIM_JSSC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jssc.2024.3457898
