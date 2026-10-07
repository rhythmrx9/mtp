---
id: W3016762888
key: 2020_Charan_KDRSA_JXCDC
title: "Accurate Inference With Inaccurate RRAM Devices: A Joint Algorithm-Design Solution"
short: "KD+RSA"
year: 2020
venue: "JXCDC"
venue_full: "IEEE Journal on Exploratory Solid-State Computational Devices and Circuits (JXCDC), vol. 6, no. 1, 2020"
authors: "Gouranga Charan, Abinash Mohanty, Xiaocong Du, Gokul Krishnan V, Rajiv Joshi, Yu Kevin Cao"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM", "SRAM-digital"]
models: ["CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "noise-injection", "device-variation", "stuck-at-faults", "write-verify-programming", "quantization", "heterogeneous-analog-digital", "calibration-compensation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 4
citations_overall: 48
priority_score: 5.99
doi: "https://doi.org/10.1109/jxcdc.2020.2987605"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2020_Charan_KDRSA_JXCDC.pdf"
fulltext: "../fulltext/2020_Charan_KDRSA_JXCDC.txt"
---

# KD+RSA

**Accurate Inference With Inaccurate RRAM Devices: A Joint Algorithm-Design Solution** — IEEE Journal on Exploratory Solid-State Computational Devices and Circuits (JXCDC), vol. 6, no. 1, 2020 (2020)

## TL;DR
Combines knowledge-distillation variation-aware training with random sparse adaptation (a small SRAM array retrained after mapping) to recover RRAM inference accuracy to 91.86% (VGG-16, CIFAR-10) with <=5% parameters in SRAM and 10-150x faster than read-verify-write.

## Summary
Programming a pretrained DNN onto RRAM introduces accuracy loss from write variation, 4-bit quantization and stuck-at faults, and cell-by-cell read-verify-write (R-V-W) compensation is slow. The authors propose a two-stage joint algorithm-design fix. Pre-mapping, an FP32 teacher guides a student trained with injected RRAM non-idealities (4-bit weights, SAFs with 1.75% SA1 and 9.04% SA0, multiplicative lognormal-style Gaussian noise sigma=0.1), using KD with temperature 2. Post-mapping, random sparse adaptation (RSA) selects a random fraction of weights, keeps them in a small hard-wired on-chip SRAM array whose output is summed with the RRAM array output, freezes the RRAM cells, and retrains only the SRAM weights online. Experiments are TensorFlow simulations of LeNet-5/MNIST and VGG-16/CIFAR-10, with timing assumptions of 6.5 us-4.5 ms RRAM write vs ~1 ns SRAM write, and area estimated with NeuroSim (16 PEs per tile). KD cuts the required SRAM fraction from 7% to 3% (MNIST) and 10% to 5% (CIFAR-10); at 15% SRAM parameters the total chip area grows by 26%.

## Contributions
- KD-based variation-aware training that transfers an FP32 teacher into a student trained under RRAM non-idealities
- Random sparse adaptation: post-mapping online retraining of a small SRAM array in parallel with the frozen RRAM array
- Joint algorithm-design flow with area analysis via NeuroSim
- Faster accuracy recovery than R-V-W (reported 10-150x)

## Key claims (stable IDs)
- **2020_Charan_KDRSA_JXCDC#C1** — KD-based VAT outperforms standalone variation-aware training under RRAM non-idealities — _support:_ MNIST 97.43% vs 95.15%; CIFAR-10 87.13% vs 82.6% (teacher-FP 99.33% / 93.35%) — _loc:_ Sec. V-A, Fig. 6
- **2020_Charan_KDRSA_JXCDC#C2** — RSA recovers baseline accuracy without RRAM rewrites, ~10x faster than R-V-W — _support:_ RSA alone needs 10% of VGG-16 parameters (1.53M of 15.3M) in SRAM — _loc:_ Sec. V-B, Fig. 7
- **2020_Charan_KDRSA_JXCDC#C3** — KD+RSA halves the SRAM parameter need — _support:_ 3% vs 7% (MNIST), 5% vs 10% (CIFAR-10); 765k vs 1.53M parameters for VGG-16 — _loc:_ Fig. 8
- **2020_Charan_KDRSA_JXCDC#C4** — State-of-the-art accuracy with 10-150x speedup over R-V-W — _support:_ 91.86% CIFAR-10 (VGG-16), 99.13% MNIST in body text (abstract states 99.41%) — _loc:_ Sec. V-B, Fig. 9, Table 4
- **2020_Charan_KDRSA_JXCDC#C5** — On-chip SRAM adaptation has area cost — _support:_ 15% SRAM parameters -> 26% total area increase — _loc:_ Sec. V, Fig. 10, Table 5

## Results
- VGG-16/CIFAR-10: KD+RSA 91.86% with <=5% parameters in SRAM vs 82.6% standalone VAT and 93.35% FP32 baseline
- R-V-W on VGG-16 needs 100% of top-ranked parameters and still leaves 4.87% accuracy loss (Table 3)
- RSA alone gives 10x faster accuracy recovery than R-V-W (Fig. 7); KD+RSA 10-150x (Fig. 9)
- SRAM array energy for RSA at 5%/10% parameters: 0.397/0.8 mJ
- 15% SRAM parameters -> +26% area (Fig. 10)

## Key numbers
- throughput: 10-150x faster accuracy recovery than R-V-W
- accuracy: 91.86% CIFAR-10 (VGG-16); 99.13% MNIST (LeNet-5)
- bits_weight: 4b

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Simulation only; RRAM device model is an assumed statistical model, not measured
- Small CNNs (LeNet-5, VGG-16); no transformers or LMs
- Needs extra SRAM area/power that scales with model size, a bottleneck for large models
- RSA needs on-chip backprop capability and training data at deployment
- Abstract MNIST figure (99.41%) differs from body text (99.13%)

## Remarks
A pragmatic hybrid analog-digital approach: keep most weights in RRAM and correct residual error with a small digital/SRAM side-path, conceptually close to LoRA-style or sparse residual correction. Evidence is simulation on small CNNs with an assumed noise model. For LMs on analog crossbars the SRAM overhead (5-10% of parameters) would be large in absolute terms, but the idea of a small trainable digital correction is relevant to adapter-based approaches in the collection.

## Cites (in collection, 4)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "In VAT [20, 21, 23], RRAM array is read to characterize device variations, and these statistical variations are then embedded to train the neural network."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _contrasts/critiques_: "Recently, Lin et al. [18] proposed a simulation framework to compute and model the error rates of the memristor computation in the DNN model to partially recover the inference accuracy."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "To evaluate the hardware efficiency of the proposed method, we use NeuroSim [27], an architectural analysis tool for evaluating the area cost of the main model and the additional on-chip memory."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Nonvolatile memory (NVM)-based processing-in-memory (PIM) architectures, such as the crossbar, have demonstrated the potential to speed up the multiply-and-accumulate (MAC) operations in DNNs, achieving high energy efficiency with low latency [8, 9, 11]."

## Cited by (in collection, 3)
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "In a knowledge distillation (KD)-based retraining, the teacher network transfers 'knowledge' to a student network [102]."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _contrasts/critiques_: "Second, off-chip training using a hardware-calibrated software model of conductance variation [15], [16] is also not scalable, as each chip requires individual characterization and training."
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2020_Charan_KDRSA_JXCDC.pdf](../../07_Hardware_Aware_Training_and_Robustness/2020_Charan_KDRSA_JXCDC.pdf)
- Full text: [../fulltext/2020_Charan_KDRSA_JXCDC.txt](../fulltext/2020_Charan_KDRSA_JXCDC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jxcdc.2020.2987605
