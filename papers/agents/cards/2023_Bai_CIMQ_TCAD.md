---
id: W4385255585
key: 2023_Bai_CIMQ_TCAD
title: "CIMQ: A Hardware-Efficient Quantization Framework for Computing-In-Memory-Based Neural Network Accelerators"
short: "CIMQ"
year: 2023
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Jinyu Bai, Sifan Sun, Weisheng Zhao, Wang Kang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["quantization", "adc-dac", "hardware-aware-training", "mixed-precision", "energy-efficiency"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 5
citations_overall: 21
priority_score: 3.44
doi: "https://doi.org/10.1109/tcad.2023.3298705"
pdf: null
fulltext: null
---

# CIMQ

**CIMQ: A Hardware-Efficient Quantization Framework for Computing-In-Memory-Based Neural Network Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
CIMQ is a hardware-aware quantization framework for CIM accelerators that jointly quantizes activations (bit-sparsity aware), weights (array-wise granularity), and partial sums (reparametrized clipping to cut ADC resolution), plus a random-dropping PTQ enhancement, reporting up to 222% hardware-efficiency gain with 58.97% accuracy improvement over conventional quantization.

## Summary
Compute-in-memory accelerators need low-precision data because of limited memory-device and data-interface resolution, but conventional NN quantization methods ignore CIM hardware characteristics (e.g., crossbar array structure, ADC cost), hurting both performance and efficiency when ported to CIM. CIMQ addresses the three CIM computing elements holistically: (1) bit-level-sparsity-induced activation quantization to cut dynamic computation energy, (2) an array-wise weight quantization granularity designed around the crossbar's computation paradigm (rather than per-tensor/per-channel granularity used in digital accelerators), and (3) partial-sum quantization via a reparametrized clipping function that reduces the needed ADC resolution. A fourth technique, a random quantization dropping strategy, is added to a post-training quantization (PTQ) pipeline to recover accuracy without retraining. The framework is evaluated on multiple networks and datasets (CIFAR-10, CIFAR-100, ImageNet), reporting up to 222% hardware-efficiency improvement together with a 58.97% accuracy improvement over conventional (non-CIM-aware) quantization methods in typical cases.

## Contributions
- Bit-level sparsity-induced activation quantization to reduce dynamic computation energy in CIM accelerators
- A CIM-specific array-wise weight quantization granularity motivated by the crossbar computation paradigm, as opposed to standard per-tensor/per-channel granularity
- Partial-sum quantization via a reparametrized clipping function that directly targets reducing required ADC resolution
- A random quantization dropping strategy enhancing post-training quantization (PTQ) accuracy for CIM-targeted QNNs
- A holistic framework spanning all three CIM computing elements (inputs/activations, weights, outputs/partial sums), evaluated across CIFAR-10, CIFAR-100, and ImageNet

## Key claims (stable IDs)
- **2023_Bai_CIMQ_TCAD#C1** — CIMQ improves hardware efficiency and accuracy versus conventional quantization methods when applied to CIM accelerators — _support:_ up to 222% hardware efficiency improvement with 58.97% accuracy improvement in typical cases — _loc:_ Abstract

## Results
- Up to 222% hardware-efficiency improvement vs. conventional quantization (typical case)
- 58.97% accuracy improvement vs. conventional quantization (typical case)
- Evaluated on CIFAR-10, CIFAR-100, and ImageNet across various NNs

## Limitations
- Analysis based on abstract only (full text not accessible); exact networks, bit-widths, baseline quantization method, and per-dataset breakdowns could not be verified
- "Typical case" framing for the headline 222%/58.97% numbers suggests they are not uniform across all tested configurations; range/variance is unclear without full text

## Remarks
CIMQ is a quantization/mapping-layer contribution rather than a new device or crossbar architecture; its key idea — treating ADC resolution reduction as a quantization-aware design target via partial-sum clipping, and using array-wise (not per-channel) granularity to match crossbar structure — is directly relevant to ADC/peripheral cost reduction, a major bottleneck this literature map tracks. The large reported gains (222% efficiency, 58.97% accuracy) are plausible for a holistic PTQ scheme but could not be cross-checked against baselines without the full text.

## Cites (in collection, 5)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2023_Bai_CIMQ_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2023.3298705
