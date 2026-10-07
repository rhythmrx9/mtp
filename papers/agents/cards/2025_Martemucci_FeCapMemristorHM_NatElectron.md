---
id: W4414428210
key: 2025_Martemucci_FeCapMemristorHM_NatElectron
title: "A ferroelectric–memristor memory for both training and inference"
short: "FeCAP-Memristor Hybrid Memory"
year: 2025
venue: "NatElectron"
venue_full: "Nature Electronics, Volume 8 (October 2025), pp. 921-933"
authors: "Michele Martemucci, François Rummens, Yannick Malot, Tifenn Hirtzlin, Olivier Guille, Simon Martin, Catherine Carabasse, Adrien F. Vincent, Sylvain Saïghi, L. Grenouillet, Damien Querlioz, Elisa Vianello"
category: "10 On-chip & Analog Training"
devices: ["ReRAM", "FeRAM"]
models: ["MLP", "CNN", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["on-chip-training", "endurance-retention", "analog-mvm", "write-verify-programming", "edge-ai", "energy-efficiency", "macro", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 27
priority_score: 3.51
doi: "https://doi.org/10.1038/s41928-025-01454-7"
pdf: "../../10_On_Chip_and_Analog_Training/2025_Martemucci_FeCapMemristorHM_NatElectron.pdf"
fulltext: "../fulltext/2025_Martemucci_FeCapMemristorHM_NatElectron.txt"
---

# FeCAP-Memristor Hybrid Memory

**A ferroelectric–memristor memory for both training and inference** — Nature Electronics, Volume 8 (October 2025), pp. 921-933 (2025)

## TL;DR
A single BEOL HfO2:Si/Ti stack in 130-nm CMOS serves as both ferroelectric capacitor (FeCAP, 10-bit hidden weights) and memristor (analogue weights), with a measured 18,432-device hybrid array transferring 3 MSBs + sign to differential memristor conductance (15 levels) without a DAC; calibrated simulations give 96.7% MNIST at 38 nJ programming energy (38x lower than k=1).

## Summary
Edge learning needs high write endurance and low programming energy (training) but also non-destructive reads (inference); memristors have the latter, FeCAPs the former. The authors integrate a 10-nm Si-doped HfO2 film with a Ti scavenging layer into the BEOL of 130-nm CMOS; each device is a FeCAP after wake-up or a memristor after one forming step. They fabricate 16,384-FeCAP (1T-1C) and 16,384-memristor (1T-1R) arrays for device characterization, then a hybrid array of 128 vertical transfer lines each with 128 FeCAPs and 16 memristors (16,384 FeCAPs + 2,048 memristors) with on-chip CMOS drivers, registers, sense amps and timing. Each weight has a 10-bit sign-magnitude hidden value in FeCAPs (updated per sample, stochastic Bernoulli mask) and an analogue weight in two memristors (G+ - G-) used for forward/backward MVMs and inference. Every k inputs, the sign and 3 MSBs are read from FeCAPs in parallel onto a transfer line whose capacitance-weighted voltage (capacitors sized 4x/2x/1x) sets the access-transistor gate and thus the memristor compliance current, giving DAC-free digital-to-analogue transfer. Measured transfer calibrates system-level simulations of MLPs on MNIST, Fashion-MNIST, ECG and of MobileNet-V2 transfer learning (last FC layer trained on-chip) on CIFAR-10 and ImageNet-derived datasets.

## Contributions
- Unified metal-ferroelectric-metal stack operating as FeCAP or memristor in the same BEOL process without extra masks
- Fabricated 18,432-device hybrid FeCAP/memristor array with CMOS periphery
- DAC-free digital-to-analogue weight transfer via capacitor-area-weighted transfer line setting memristor compliance current (15 differential levels measured)
- On-chip training scheme with hidden weights in FeCAPs and analogue weights in memristors, validated by calibrated simulation on MNIST/Fashion-MNIST/ECG and MobileNet-V2 transfer learning

## Key claims (stable IDs)
- **2025_Martemucci_FeCapMemristorHM_NatElectron#C1** — FeCAP mode has far higher endurance and lower energy than memristor mode in the same stack — _support:_ FeCAP switching energy <200 fJ/bit, window positive over 10^7 cycles; memristor endurance ~10^5 cycles — _loc:_ Fig. 2c-d, 2h
- **2025_Martemucci_FeCapMemristorHM_NatElectron#C2** — Sign + 3 MSBs of the hidden weight transfer to 15 distinct differential conductance levels without a DAC — _support:_ integers -7..7 measured across 33 circuits, 6 transfers each; memristors support up to 8 analogue levels — _loc:_ Fig. 4
- **2025_Martemucci_FeCapMemristorHM_NatElectron#C3** — Updating the analogue weights only every k=100 inputs cuts programming energy 38x with no accuracy loss — _support:_ 96.7% MNIST, ~38 nJ total; operations 17x below memristor and 75x below FeCAP endurance limits — _loc:_ Fig. 5c-e
- **2025_Martemucci_FeCapMemristorHM_NatElectron#C4** — The hybrid approach performs within ~1-2 points of floating-point training — _support:_ HM with hidden-weight quantization ~1 point lower, induced transfer errors ~1 point more; MNIST online FP 98.1 vs 96.7 etc. — _loc:_ Fig. 5f

## Results
- Memory window: median 360 mV, worst-case 120 mV over 16,384 FeCAPs (after 1,000 wake-up cycles)
- FeCAP switching energy <200 fJ/bit; endurance >10^7 cycles vs ~10^5 for memristor SET/RESET
- Memristor programmed at 8 conductance levels (up to ~67 uA compliance; Fig. 2f-g)
- MNIST 96.7% (online, k=100) vs 98.1% FP-trained reference; ~1 point loss from hidden-weight quantization and ~1 more from transfer variability (Fig. 5f)
- MobileNet-V2 transfer learning with 4-bit quantized feature extractor and 4-bit HM-trained classifier, evaluated on CIFAR-10 and 4 ImageNet-derived datasets (Fig. 6c)

## Key numbers
- tech_node: 130nm
- array_size: 128 transfer lines x (128 FeCAPs + 16 memristors); 16,384 FeCAPs + 2,048 memristors
- energy_eff: FeCAP <200 fJ/bit switching; 38 nJ total training energy at k=100
- accuracy: 96.7% MNIST (online, k=100, simulation calibrated on measurements)
- bits_weight: 10b hidden (FeCAP), 4b analogue (3 MSB + sign, memristor)

## Datasets / benchmarks
MNIST, Fashion-MNIST, ECG detection, CIFAR-10, CIFAR-100, ImageNet, Oxford-IIIT Pet, Oxford Flowers 102, Caltech Birds, Stanford Cars

## Limitations
- Training results are hardware-calibrated simulations; on-chip end-to-end training loop was not run on the fabricated chip
- Only small networks (3-layer MLP) and last-layer FC training for MobileNet-V2; scaling to deep networks or transformers needs more FeCAP precision and area
- Only 8 analogue memristor levels (4 bits with sign); FeCAP MSBs need differently sized capacitors (area cost)
- Memristor endurance ~10^5 cycles limits transfer frequency; 130-nm node, no ADC/full MVM macro characterized
- Programming energies for the training simulations are assumed (1 pJ memristor, 100 fJ FeCAP) from literature

## Remarks
A device/circuit co-integration result that tackles the endurance versus read-stability tension in analog training by splitting hidden and analogue weights across two modes of one stack; the measured transfer data is real, but the learning results rely on simulation and tiny models. For the collection's language-model focus it is peripheral: it suggests how adapter-like or last-layer on-device fine-tuning could be supported, but the authors themselves flag transformers as future work. It complements software-only HWA training (e.g., Rasch et al.) by addressing the weight-update side at the device level.

## Cites (in collection, 9)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _contrasts/critiques_: "For example, a fully analogue solution based on a synaptic unit cell combining non-volatile phase change memory (PCM) with conventional CMOS-based capacitors (the PCM array was fabricated and the CMOS capacitors were simulated) has been explored16."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Among the memory types suitable for integration into advanced commercial processes, filamentary memristors have been extensively studied for analogue in-memory neural network inference7,8,23."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Among the memory types suitable for integration into advanced commercial processes, filamentary memristors have been extensively studied for analogue in-memory neural network inference7,8,23."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "However, the limited write endurance and high programming energy make them poorly suited for on-chip training, necessitating off-chip training and pre-programming for specific tasks11."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _contrasts/critiques_: "One approach to the challenge of training at the edge is to combine memristors with accurate digital static random-access memory, which can be made using standard transistors15."

## Files
- PDF: [../../10_On_Chip_and_Analog_Training/2025_Martemucci_FeCapMemristorHM_NatElectron.pdf](../../10_On_Chip_and_Analog_Training/2025_Martemucci_FeCapMemristorHM_NatElectron.pdf)
- Full text: [../fulltext/2025_Martemucci_FeCapMemristorHM_NatElectron.txt](../fulltext/2025_Martemucci_FeCapMemristorHM_NatElectron.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41928-025-01454-7
