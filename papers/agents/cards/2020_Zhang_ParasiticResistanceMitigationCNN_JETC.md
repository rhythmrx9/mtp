---
id: W3030670306
key: 2020_Zhang_ParasiticResistanceMitigationCNN_JETC
title: "Mitigate Parasitic Resistance in Resistive Crossbar-based Convolutional Neural Networks"
short: "Parasitic-Mitigation-CNN"
year: 2020
venue: "JETC"
venue_full: "ACM Journal on Emerging Technologies in Computing Systems (JETC), Special Issue on Nanoelectronic Device, Circuit, Architecture Design, 2020"
authors: "Fan Zhang, Miao Hu"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["Memristor(generic)", "ReRAM"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["ir-drop-parasitics", "weight-mapping", "calibration-compensation", "adc-dac", "cnn-accelerator", "tiling-partitioning", "quantization"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 6
citations_overall: 27
priority_score: 4.94
doi: "https://doi.org/10.1145/3371277"
pdf: "../../06_Nonidealities_and_Reliability/2020_Zhang_ParasiticResistanceMitigationCNN_JETC.pdf"
fulltext: "../fulltext/2020_Zhang_ParasiticResistanceMitigationCNN_JETC.txt"
---

# Parasitic-Mitigation-CNN

**Mitigate Parasitic Resistance in Resistive Crossbar-based Convolutional Neural Networks** — ACM Journal on Emerging Technologies in Computing Systems (JETC), Special Issue on Nanoelectronic Device, Circuit, Architecture Design, 2020 (2020)

## TL;DR
Dense kernel-to-crossbar mapping plus a conductance conversion and calibration algorithm that compensates wire/IO parasitic resistance in full-circuit simulation of CNNs; LeNet-style MNIST keeps 98.8% (software 99.1%) at 8-bit ADC/DAC, and ResNet-20/32/56 on CIFAR-10 hold near-software accuracy at 8-bit (6-bit partly).

## Summary
Parasitic wire and interface resistance makes large crossbars deviate from ideal VMM. The authors model a 1T1M-style crossbar with parasitic resistances using nodal analysis, validated against experiment up to 128x64 (a dot-product-engine measurement). For mapping, negative weights are handled by shifting the matrix by a constant A_shift (removed by subtracting A_shift x sum(X) using a digital or analog accumulator column) instead of using differential pairs; convolution is mapped densely by flattening each 4-D kernel into a crossbar column (versus Toeplitz sparse mapping needing up to about 100x more DACs/ADCs). A mitigation algorithm adapts the earlier conversion algorithm: conductances G are fine-tuned to G' using a conversion signal whose amplitude (not sparsity) matters (all 0.1 best for 144x16; smaller for larger arrays), followed by a first-order polynomial calibration fitted on ten random inputs per crossbar, embedded in ADC/DAC settings. Crossbar parameters are Ron=15 kOhm, Roff=300 kOhm, 1 Ohm wire per segment, input range 0-0.4 V. End-to-end circuit simulation of a 4-layer CNN on MNIST (4000 test images) and ResNet-20/32/56 on CIFAR-10 (150-image subset, about 5 min per image) with ADC/DAC quantization of 4, 6, 8 bits and none; error propagation is analysed per layer and the impact of Gaussian programming error (sigma up to 1 uS) is studied. Largest crossbar is 800x500 (MNIST) and 576x64 (ResNets).

## Contributions
- Dense mapping of 4-D convolution kernels to 2-D crossbars with near-zero hardware overhead.
- Parasitic-aware crossbar simulator verified against experiment up to 128x64.
- Mitigation (conversion + calibration) algorithm accounting for data and kernel sparsity, without retraining.
- End-to-end circuit simulation of CNN/ResNet-20/32/56 showing error propagation and quantization requirements.

## Key claims (stable IDs)
- **2020_Zhang_ParasiticResistanceMitigationCNN_JETC#C1** — Method gives about 50% better overall accuracy than the original conversion algorithm. — _support:_ relative error comparison on 27x16 to 576x64 crossbars — _loc:_ Sec. 4.2, Fig. 14-18
- **2020_Zhang_ParasiticResistanceMitigationCNN_JETC#C2** — For 576x64 crossbar, mean relative error 0.25% (about 8.6 bits) and worst 1.2% (about 6.4 bits). — _support:_ Conclusion — _loc:_ Sec. 5
- **2020_Zhang_ParasiticResistanceMitigationCNN_JETC#C3** — 8-bit ADC/DAC keeps MNIST accuracy at 98.8% vs 99.1% software. — _support:_ 4000 validation images — _loc:_ Sec. 4.3, Table 6
- **2020_Zhang_ParasiticResistanceMitigationCNN_JETC#C4** — 8-bit or even 6-bit ADC/DAC prevents error accumulation in CNNs up to about 50 layers; 4-bit causes major accuracy drop. — _support:_ ResNet error propagation — _loc:_ Fig. 19-20, Table 6
- **2020_Zhang_ParasiticResistanceMitigationCNN_JETC#C5** — Programming error sigma < 0.4 uS keeps ResNet-20 above 80% accuracy. — _support:_ Gaussian sigma sweep with calibration — _loc:_ Fig. 21

## Results
- Output error vs conversion signal amplitude: all-1 gives about +/-20% error, all-0.1 about +/-0.2% (144x16 crossbar, Fig. 11).
- Sparse mapping needs about 100x more DACs/ADCs than dense mapping (e.g. 3x3x64x64 kernel: 4096 DACs vs 576, Table 3).
- MNIST 98.8% at 8-bit vs 99.1% software; ResNet 8-bit slightly better than software on 150-image subset; 4-bit degrades strongly (Table 6, exact values garbled in extraction).

## Key numbers
- array_size: up to 800x500 (MNIST CNN), 576x64 (ResNet)
- accuracy: 98.8% MNIST at 8-bit (99.1% software)
- bits_adc: 6-8b ADC/DAC

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- CIFAR-10 evaluated on only 150 images due to simulation time.
- Only CNNs; no attention or language models.
- Only parasitic resistance and Gaussian programming error; drift, read noise and stuck-at faults are not studied; capacitance ignored (DC only).
- Per-crossbar conductance conversion requires solving the nodal model, assumed known and static.

## Remarks
Useful reference for how IR drop interacts with ADC/DAC resolution and sparsity in deep networks, with a rigorous circuit-level simulation rather than behavioral models. Its compensation scheme depends on a known parasitic model and per-array tuning, so scaling to Transformer-size matrices is untested. Related collection work on crossbar simulators (PytorX, MNSIM) is simpler but faster.

## Cites (in collection, 6)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "To overcome the memory bottleneck, many researchers show interest in resistive crossbar arrays for the computing-in-memory feature [1, 8, 14, 21, 25, 41]."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "To overcome the memory bottleneck, many researchers show interest in resistive crossbar arrays for the computing-in-memory feature [1, 8, 14, 21, 25, 41]."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _contrasts/critiques_: "Although we could partition huge matrix into multiple small matrices[23], sparse mapping still needs 100x numbers of DACs&ADCs than dense mapping."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _baseline/comparison_: "PytorX[12] and FTNNA[24] are designed for neural network applications with the consideration of non-ideal effects."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "In Table 2, crossbar, ADC/DAC parameters are adopted from ISAAC[29]."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _baseline/comparison_: "MNSIM[38] and NeuroSim[5] are two famous ReRAM crossbar simulators."

## Cited by (in collection, 2)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "It is well known that parasitic resistance degrades MVM accuracy and some compensation methods have been proposed [30,32,33,71]."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "In recent years, several noise models [2, 19, 26] and crossbar-realistic DNN accuracy evaluation frameworks ... have been proposed that are integrated with hardware-aware re-training or fine-tuning of GPU-trained DNN weights"

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2020_Zhang_ParasiticResistanceMitigationCNN_JETC.pdf](../../06_Nonidealities_and_Reliability/2020_Zhang_ParasiticResistanceMitigationCNN_JETC.pdf)
- Full text: [../fulltext/2020_Zhang_ParasiticResistanceMitigationCNN_JETC.txt](../fulltext/2020_Zhang_ParasiticResistanceMitigationCNN_JETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3371277
