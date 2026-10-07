---
id: W3041897167
key: 2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev
title: "Analog architectures for neural network acceleration based on non-volatile memory"
short: "Xiao Analog NVM Review"
year: 2020
venue: "ApplPhysRev"
venue_full: "Applied Physics Reviews, vol. 7, 031301 (2020)"
authors: "T. Patrick Xiao, Christopher H. Bennett, Ben Feinberg, Sapan Agarwal, Matthew J. Marinella"
category: "01 Surveys & Foundations"
devices: ["ReRAM", "PCM", "FeFET", "ECRAM", "Flash", "Charge/Capacitor", "Generic-NVM"]
models: ["MLP", "CNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "crossbar-architecture", "analog-mvm", "adc-dac", "bit-slicing", "peripheral-circuits", "on-chip-training", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 19
citations_overall: 195
priority_score: 7.13
doi: "https://doi.org/10.1063/1.5143815"
pdf: "../../01_Surveys_and_Foundations/2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.pdf"
fulltext: "../fulltext/2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.txt"
---

# Xiao Analog NVM Review

**Analog architectures for neural network acceleration based on non-volatile memory** — Applied Physics Reviews, vol. 7, 031301 (2020) (2020)

## TL;DR
Sandia review that organizes analog NVM crossbar DNN accelerators by design-hierarchy level (devices, peripherals, inference and training architectures, non-ideality mitigation) and shows ADC/peripheral overhead (e.g. 49% of ISAAC chip power) is the central bottleneck.

## Summary
The review addresses why analog in-memory accelerators have not yet delivered their promised gains over digital hardware, attributing it to peripheral-circuit overhead and non-ideal memory devices. Rather than organizing by device, it is organized around accelerator building blocks: computational primitives of DNN inference/training (Sec. II), digital baselines (III), candidate devices and access devices/array-size limits (IV, Table I), peripherals (V: analog vs digital routing, input encoding by voltage level, temporal encoding or input bit slicing, ramp vs SAR ADCs, neuron functions), inference architectures (VI), training architectures (VII), and non-ideality mitigation (VIII). Weights map to crossbar conductances, with signed weights handled by differential pairs, biased/flipped encoding, or offset columns, and high precision obtained by synaptic (weight) bit slicing across columns/crossbars plus input bit slicing, reassembled with shift-and-add. Tiled hierarchies (ISAAC, Newton, PUMA, PRIME, memristive Boltzmann machine) are compared in Table III against digital accelerators on TOPS/mm2 and TOPS/W, with CNN layer pipelining and weight replication discussed. Training sections cover backpropagation support, parallel outer-product updates, batch size >1, and compensation for device asymmetry. Scope is deep supervised learning (MLP, CNN, LSTM); transformers/LMs are not covered.

## Contributions
- Organizes the analog NVM accelerator literature around the design hierarchy (device, array, peripheral, tile, chip) instead of by device technology
- Quantifies and compares ADC architectures (ramp vs SAR) and techniques to reduce ADC overhead (bit slicing, flipped/biased weight encoding, adaptive-resolution SAR, divide-and-conquer)
- Compares inference accelerators (ISAAC, Newton, PUMA, PRIME, Boltzmann machine) against digital designs in Table III
- Surveys inference-vs-training architecture requirements and non-ideality mitigations (IR drop, sparsity, drift, stuck-at faults, device-aware training)

## Key claims (stable IDs)
- **2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev#C1** — The ADC is a dominant energy/area/latency bottleneck of analog accelerators — _support:_ ADC consumes 49% of total chip power in ISAAC and 41% in the memristive Boltzmann machine; Newton cuts ADC cost by up to 60% vs ISAAC — _loc:_ Sec. VI G (Table III discussion)
- **2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev#C2** — Projected analog accelerators only approximately reach parity with the best measured digital accelerators when adjusted for arithmetic precision — _support:_ 'approximately reaches parity with the measured performance, compute density, and energy efficiency of the best digital accelerators' — _loc:_ Sec. VI G / Table III
- **2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev#C3** — Bit slicing relaxes device requirements and reduces required ADC resolution at the cost of repeated operations — _support:_ 'Bit slicing allows less ideal memory devices to be used, reduces the required ADC resolution, and offers greater protection against noise' — _loc:_ Sec. VI A
- **2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev#C4** — Digital routing with ADCs/DACs is more accurate than analog routing between crossbars — _support:_ DPE simulation on MNIST: analog routing degraded more than digital routing with 4-bit ADC/DAC — _loc:_ Sec. V A

## Results
- Table III compares ISAAC, Newton, PUMA, PRIME, memristive Boltzmann machine with digital accelerators (TPU, UNPU etc.) on TOPS, TOPS/mm2, TOPS/W at stated precisions
- Newton reduces ADC cost by as much as 60% over ISAAC via adaptive ADC resolution and divide-and-conquer
- Digital-domain-heavy designs (ISAAC) use 2-bit device slices (8 x 2-bit for 16-bit weights)

## Key numbers
- array_size: 128x128 (DPE case study)
- bits_weight: 16b weights as 8x2-bit slices (ISAAC)
- bits_adc: 8-bit SAR (ISAAC)

## Datasets / benchmarks
MNIST, CIFAR-10, MLPerf inference (cited)

## Limitations
- Review only; numbers are taken from the original papers and are mostly simulated/projected rather than measured
- Scope limited to deep supervised learning (MLP/CNN/LSTM); no transformer, attention or language-model coverage
- Published 2020, so predates the multi-core PCM/ReRAM chips and LLM-era work

## Remarks
A circuit- and architecture-centered review that is the best entry point in the collection for ADC overhead, bit slicing and weight-encoding trade-offs. Its treatment of peripherals transfers directly to mapping transformers onto crossbars, although attention, KV-cache and dynamic matrices are absent. It complements the device-centric reviews and the hardware-measured chip papers later in the collection.

## Cites (in collection, 19)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "Reference 209 proposes a scheme to assign the rows of the weight matrix to the crossbar rows in a way that minimizes the expected deviations on the column outputs due to cycle-to-cycle variability. Then, during a re-training phase, weights that remain particularly prone to errors are frozen and reduced to zero."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "The PipeLayer accelerator takes the above approach of using a second ReRAM array as a buffer to store intermediate weight updates in a batch.174"
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _data/numbers_: "As a case study, HP's Dot Product Engine (128 x 128 crossbar) was evaluated in simulation using both analog routing-with buffers and repeaters-and digital routing, which interfaces with the crossbars via ADCs and DACs.65 The authors found that accuracy on the MNIST task degraded more strongly with analog routing"
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "Noise and cycle-to-cycle variability in the readout currents of the individual memory elements can cause random errors in a VMM computation, while endurance failures, manufacturing defects, and programming errors can lead to persistent errors.164"
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _background_: "Reference 204 obtains a similar outcome, but starting with a sparse neural network, by re-arranging the matrix columns using k-means clustering, pruning elements that still remain outside of fixed-size blocks, and retraining the network."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "The PUMA architecture uses smaller functional units to execute the equivalent wide instruction over several cycles: this compromise offsets the parallelism of SIMD but still reduces the overhead of instruction fetch and decode.148"
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _data/numbers_: "A significant bottleneck for many of the analog architectures is the ADC, which consumes 49% of the total chip power in ISAAC and 41% in the memristive Boltzmann machine."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Here, we review the two types of ADCs most commonly used by crossbar accelerators: the ramp ADC, as used in Ref. 62 and PRIME,136 and the SAR ADC, as used in ISAAC,68 PUMA,148 and the memristive Boltzmann machine.12"
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019)

## Cited by (in collection, 6)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _background_: "Pruning is more difficult to exploit in analog accelerators, due to the rigid structure of a memory crossbar [62]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "Therefore, many large-scale simulations encompassing device and circuit nonidealities have been performed to quantify their impact on DNN accuracy for training and inference21–28 ."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "In the digital bit-slicing weight-storage approach, weights are typically mapped using a two’s complement format36."
- [2022_Wen_RRAMReadDisturb_DFT](2022_Wen_RRAMReadDisturb_DFT.md) RRAM Read Disturb (2022)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)

## Files
- PDF: [../../01_Surveys_and_Foundations/2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.pdf](../../01_Surveys_and_Foundations/2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.pdf)
- Full text: [../fulltext/2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.txt](../fulltext/2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1063/1.5143815
