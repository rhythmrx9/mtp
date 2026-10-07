---
id: W2740220207
key: 2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS
title: "Multiscale Co-Design Analysis of Energy, Latency, Area, and Accuracy of a ReRAM Analog Neural Training Accelerator"
short: "Multiscale Co-Design ReRAM Training"
year: 2018
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2018)"
authors: "Matthew J. Marinella, Sapan Agarwal, Alexander H. Hsia, Isaac Richter, Robin Bay Jacobs-Gedrim, John Niroula, Steven J. Plimpton, Engin İpek, Conrad D. James"
category: "10 On-chip & Analog Training"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["on-chip-training", "analog-mvm", "adc-dac", "peripheral-circuits", "energy-efficiency", "device-variation", "simulator", "bit-slicing"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 11
cites_in_collection: 3
citations_overall: 184
priority_score: 6.32
doi: "https://doi.org/10.1109/jetcas.2018.2796379"
pdf: "../../10_On_Chip_and_Analog_Training/2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.pdf"
fulltext: "../fulltext/2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.txt"
---

# Multiscale Co-Design ReRAM Training

**Multiscale Co-Design Analysis of Energy, Latency, Area, and Accuracy of a ReRAM Analog Neural Training Accelerator** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2018) (2018)

## TL;DR
Circuit-level (14/16 nm PDK) design and co-simulation of a 1024x1024 analog ReRAM crossbar block for VMM, MVM and outer-product update shows ~11 fJ/MAC and 270x energy / 540x latency advantage over a digital-ReRAM block (430x / 34x vs SRAM), but measured TaOx non-idealities limit MNIST backprop accuracy to ~77-85% vs ~98% numeric.

## Summary
The paper targets the three kernels of neural-network training (vector-matrix multiply, matrix-vector multiply, outer-product update) and designs an analog crossbar block in a commercial 14/16 nm FinFET PDK with 1024x1024 ReRAM cells, 8-bit inputs/outputs coded in time (ramp ADC with one ramp generator and 1024 comparators; voltage drivers with 4-bit update, 3 magnitude + 1 sign) and 256 parallel MAC digital registers for the digital baselines. Digital-ReRAM and SRAM versions of each kernel are designed for like-for-like comparison and broken down per component for energy, latency and area (Tables II-V). Weights are stored in analog conductance and updated in parallel; electromigration limits (about 33 uA for a 32 nm metal-1 line) bound per-device write current to ~32 nA, and to 10 nA to keep IR drop below 20 mV. Algorithm-level accuracy is evaluated with the open-source CrossSim simulator using experimentally measured TaOx ReRAM conductance-vs-pulse statistics (binned DeltaG distributions capturing nonlinearity, asymmetry and stochasticity) on a 784x300x34 MLP trained with backprop on MNIST. Mitigations such as periodic carry (multiple cells per weight) bring accuracy within 1% of numeric.

## Contributions
- Detailed analog ReRAM crossbar training block in 14/16 nm PDK for VMM, MVM and outer-product update
- Matched digital-ReRAM and SRAM designs with energy/latency/area comparison per kernel
- Device-to-algorithm co-simulation (CrossSim) with measured TaOx pulse data
- Quantification of which non-ideality dominates training accuracy loss and of periodic-carry mitigation

## Key claims (stable IDs)
- **2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS#C1** — The analog accelerator block takes ~11 fJ per MAC — _support:_ abstract: 11 fJ per MAC — _loc:_ Abstract / Sec. IV
- **2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS#C2** — Analog block has 270x energy and 540x latency advantage over digital ReRAM; 430x energy and 34x latency over SRAM — _support:_ abstract — _loc:_ Sec. IV / Table V
- **2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS#C3** — State-dependent nonlinear conductance change is the dominant accuracy degrader in training — _support:_ TaOx ReRAM tops out ~77% (up to ~85% with tuned pulses) vs ~98% numeric on MNIST — _loc:_ Sec. VI-A / Fig. 14
- **2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS#C4** — Periodic carry brings TaOx training within 1% of numerical accuracy — _support:_ Fig. 15 — _loc:_ Sec. VI-B

## Results
- Latency per kernel (VMM/MVM/OPU): analog 0.384/0.384/0.512 us, digital ReRAM 176/176/340 us, SRAM 4/32/8 us (Table V)
- Analog VMM energy total 12.8 nJ vs 2140 nJ digital ReRAM (Table IV, column mapping approximate due to extraction)
- Target of 20 fJ/MAC (50 TMAC/W) met by analog design at ~11 fJ/MAC
- 2- and 4-bit input/output variants gain a further order of magnitude in energy (Sec. IV discussion)
- MNIST 784x300x34 MLP: ~77% (up to ~85% tuned) with TaOx vs ~98% numeric; periodic carry within 1% (Figs. 14-15)

## Key numbers
- tech_node: 14/16 nm FinFET PDK
- array_size: 1024x1024
- energy_eff: 11 fJ/MAC (~50+ TMAC/W)
- throughput: VMM latency 0.384 us (analog)
- accuracy: ~77% (up to ~85%) MNIST with TaOx vs ~98% numeric
- bits_weight: ~8b analog weight
- bits_adc: 8b ramp ADC (2b/4b variants)

## Datasets / benchmarks
MNIST

## Limitations
- Block-level analysis only, no full accelerator architecture, NoC or system data movement
- MNIST MLP only; no CNN/transformer workloads
- Ramp ADC comparators burn static current; high-voltage drivers 8x larger than low-voltage transistors
- Large write-current/electromigration constraints force very high R_ON (~31 Mohm)
- Training accuracy unacceptable for single TaOx devices without mitigation

## Remarks
An influential (184 citations) early circuit-level quantification of analog training, valuable because it fixes the cost of peripherals (temporal coding, ramp ADC) and the physical write-current limits rather than assuming ideal circuits. It predates large-scale models, so it speaks to MLP-scale training only; its emphasis on nonlinear/asymmetric updates is the same issue later analog-training work (e.g. PANTHER, TTv2/Tiki-Taka) tackles. Useful for readers sizing energy of in-situ weight update in crossbars.

## Cites (in collection, 3)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _uses-method-or-tool_: "In order to model these effects on the training of the algorithm, statistical data is extracted from the repeated pulsing between GMIN and GMAX following the methodology first presented in Burr et al [27, 36]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "The ISAAC architecture is a full neural execution unit similar to DaDianNao but using ReRAM crossbars to store and process weights for CNN inference [9]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "PRIME is a new pipelined architecture and a method of efficiently processing neural network inference with analog weights. PRIME provides an energy advantage of three orders of magnitude [10]."

## Cited by (in collection, 11)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "While the external control electronics we use in this work is not optimized for fast speed and low power consumption yet, previous literature on circuit design45,51 and architecture21,53 suggest an on-chip integrated system would yield significant advantages in speed-energy efficiency."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _contrasts/critiques_: "The aforementioned technique has been demonstrated with low-precision inputs/outputs (2-4 bits) and weights (2-5 bits) on the SGD training algorithm for FC layers only [10, 11]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _data/numbers_: "Second, the high write voltage [103] and multiple programming cycles (program-verify approach [45]) result in much higher write cost (energy and latency) than SRAM."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _data/numbers_: "Consequently, even with an ADC working at very high sampling frequency such as 1GHz, a crossbar read operation requires 128 ns, while typical crossbar reads without ADC require 5-20 ns [17]."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "Several ReRAM-based in-situ mixed-signal DNN accelerators such as ISAAC [18], Newton [19], PipeLayer [20], PRIME [17], PUMA [21], MultiScale [22], XNORRRAM [37], RapidDNN [38], have been proposed in recent years."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "Within an array, individual analog MACs can also be conducted at a lower energy, higher density, and greater parallelism than digital MACs [45]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _uses-method-or-tool_: "To process inputs, we use 4b pulse-train DACs for their simple hardware [32] and superior linearity [55]."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _data/numbers_: "We achieve ∼ 8% reduction in training-energy for both models, calculated based on the data in [14]."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _contrasts/critiques_: "However, several NVM compute-in-memory studies have focused on the macro-level32,34,39,40,41, without accounting for data transport, control or chip infrastructure (such as clocking) costs. They are also usually at a much smaller scale ... than the work here."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.pdf](../../10_On_Chip_and_Analog_Training/2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.pdf)
- Full text: [../fulltext/2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.txt](../fulltext/2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jetcas.2018.2796379
