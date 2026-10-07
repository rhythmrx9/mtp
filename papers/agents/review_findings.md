# Findings of the original review (F = verified, R = refuted, N = unadjudicated)

## F1 — High confidence 2 claims merged · 3–0 unanimous
Transformers now run on real analog PCM silicon at near-iso-accuracy: ALBERT-base on a single 14 nm PCM chip across 28.3M devices, averaging only 1.8% below the floating-point reference on 7 GLUE tasks, with several tasks at full iso-accuracy.

_Note:_ Nature Communications 2025 · corroborated on PubMed 41027896, PMC12485056
Papers: [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](cards/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md)

## F2 — High confidence 3–0 on HERMES and NeuRRAM · 2–1 on the 14 nm chip
Analog CIM has moved past simulation to fabricated, measured multi-core silicon in both PCM and RRAM: IBM's 14 nm chip, IBM's 64-core HERMES chip, and NeuRRAM. HERMES's 400 GOPS/mm² in 4-phase mode is more than 15× higher than previous multi-core resistive-memory AIMC chips.

_Note:_ The single dissent concerned the scope of “software-equivalent”, not the hardware specifications.
Papers: [2023_LeGallo_IBMHERMESChip_NatElectron](cards/2023_LeGallo_IBMHERMESChip_NatElectron.md), [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](cards/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md), [2022_Wan_NeuRRAM_Nature](cards/2022_Wan_NeuRRAM_Nature.md)

## F3 — High confidence 3–0 on NeuRRAM · 2–1 on HERMES and RNN-T
Measured on-chip accuracy is close to software but not free, and the penalty grows with model scale — from full software-equivalence on keyword spotting, to <1 pp on ResNet-9, to 1.8 pp on ALBERT/GLUE, to a missed equivalence threshold on a 45M-weight RNN-T.

_Note:_ Dissents addressed interpretive framing, not the numbers. Caveat: NeuRRAM's “comparable to software” baseline is itself 4-bit quantized.
Papers: [2023_LeGallo_IBMHERMESChip_NatElectron](cards/2023_LeGallo_IBMHERMESChip_NatElectron.md), [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](cards/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md), [2022_Wan_NeuRRAM_Nature](cards/2022_Wan_NeuRRAM_Nature.md), [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](cards/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md)

## F4 — High confidence 3–0 on the LLM result and the 4.4% ALBERT figure
Hardware-aware training — injecting realistic device noise during training or fine-tuning — is the field's dominant and empirically validated mitigation, and it now scales to pre-trained LLMs. On under 1% of pre-training tokens, Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct retained accuracy comparable to 4-bit-weight / 8-bit-activation quantized baselines under hardware-realistic analog noise — a gap off-the-shelf LLMs cannot close on their own.

_Note:_ Analog Foundation Models, NeurIPS 2025 (IBM Zurich / ETH) · ALBERT paper quantifies HWA's own contribution at 4.4% average recovery
Papers: [2023_LeGallo_IBMHERMESChip_NatElectron](cards/2023_LeGallo_IBMHERMESChip_NatElectron.md), [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](cards/2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md), [2025_Buchel_AnalogFoundationModels_NeurIPS](cards/2025_Buchel_AnalogFoundationModels_NeurIPS.md)

## F5 — Medium confidence 2 claims merged · 3–0 unanimous
Full-model analog retraining is not necessary. Analog hardware-aware LoRA freezes the analog-programmed weights as fixed meta-weights and trains only small external digital low-rank adapters, matching full HWA retraining within 1% F1/EM on SQuAD v1.1 and beating it after 10 years of simulated PCM drift (F1 85.36 vs 85.14; EM 76.92 vs 76.40). Adapter-swapping also mitigates the reprogramming problem: one analog base model serves many tasks, avoiding the error accumulation of repeated programming, with adapters refreshed off-chip and drift handled by global drift compensation.

_Note:_ Graded medium: single research group, one model (MobileBERT), one task, and drift modeled rather than measured over 10 years.
Papers: [2026_Li_AHWA-LoRA_NeuromorphComputEng](cards/2026_Li_AHWA-LoRA_NeuromorphComputEng.md)

## F6 — High confidence 4 claims merged · 3–0 unanimous
The central architectural gap between CNN-era analog IMC accelerators and transformer workloads is self-attention's dynamic matrix-matrix multiplication: both operands are input-dependent, so crossbars must be reprogrammed per self-attention layer. At sequence length 256 these dynamic MVMs consume 80% of total runtime, and the compute-write-compute dependency stalls MatMul until KT is written column by column.

_Note:_ X-Former (IEEE TVLSI) · ReTransformer (ICCAD 2020) · arXiv 2601.14260 — three independent groups; repeated by ClipFormer, CPSAA, RED-PIM, RAELLA, TransPIM
Papers: [2023_Sridharan_X-Former_TVLSI](cards/2023_Sridharan_X-Former_TVLSI.md), [2020_Yang_ReTransformer_ICCAD](cards/2020_Yang_ReTransformer_ICCAD.md)

## F7 — Medium confidence 2 claims merged · 3–0 unanimous
The write bottleneck is being attacked algorithmically rather than only with better devices, via reformulations that keep the static weight matrix in the crossbar; dedicated ReRAM PIM transformer accelerators report large gains (ReTransformer: 23.21× efficiency and 1086× power versus GPU).

_Note:_ Graded medium: self-reported simulator and architecture-level speedups against differing baselines, not measured silicon. The 1086× power figure compares an accelerator model against a general-purpose GPU.
Papers: [2020_Yang_ReTransformer_ICCAD](cards/2020_Yang_ReTransformer_ICCAD.md)

## F8 — High confidence 3 claims merged · 3–0 unanimous
ADC/DAC conversion is a first-order cost and it creates a scaling trap: up to 58% of energy and 81% of area, energy exponential in precision; AIMC only beats DIMC once that overhead is amortized over a large array, but larger arrays force higher-resolution ADCs that degrade throughput and computational density.

_Note:_ arXiv 2406.08413 · KU Leuven quantitative IMC benchmarking (ICCAD 2023)
Papers: [2023_Sun_AIMCvsDIMC_ICCAD](cards/2023_Sun_AIMCvsDIMC_ICCAD.md)

## F9 — High confidence 3–0 unanimous
Device non-idealities are the physical limit and span a hierarchy, not just the material: memory window, read noise, program noise and conductance drift act on different time scales while constraining manufacturability; errors originate at device, array, architecture and algorithm levels. NVM writes cost 1–2 orders of magnitude more latency and energy per bit than SRAM, with ~106–109 write endurance.

_Note:_ Wiley Adv. Intelligent Systems 2026 · Nature Materials 2026 · X-Former
Papers: [2026_Jiang_HighAccuracyMemristorCIM_NatMater](cards/2026_Jiang_HighAccuracyMemristorCIM_NatMater.md), [2023_Sridharan_X-Former_TVLSI](cards/2023_Sridharan_X-Former_TVLSI.md), [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](cards/2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md)

## F10 — High confidence 2–1 on BERT variation · 3–0 on read-disturb
Non-idealities translate into quantified, model-scale-dependent accuracy loss. Simulated device variation costs under 1% in low-variation regimes (0–0.2) but up to 4.2% for BERT-base and 9.87% for BERT-large, because errors accumulate across layers. Separately, measured RRAM read-disturb resistance shifts from a 40 nm foundry test chip (1300 mV bitline, 10 cycles of 50k stresses) dropped VGG-8 CIFAR-10 accuracy from 87% to 66%.

_Note:_ The dissent objected to inferring “scales with depth” from a single task. Caveat: the depth-scaling numbers come from one simulator (NeuroSim) on one task (WNLI, 56.34% baseline). An IRPS 2020 study reports a harsher 87.35% → 11.58% after 144 hours of read disturb.
Papers: source not in collection

## F11 — Medium confidence 3–0 unanimous
Heterogeneous architecture is the consensus design point: AIMC tiles combined with digital processing units, because analog tiles alone cannot execute an end-to-end deep neural network.

_Note:_ Graded medium because “dominant” is a review-level characterization resting largely on one review plus the same lab's own chips — and a companion claim from that same review was refuted 0–3 (see §09).
Papers: [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](cards/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md)

## F12 — Medium confidence 2–1 on degradation · 3–0 on non-uniformity
LLM KV-cache state is a newly identified analog-noise vulnerability and it is highly non-uniform across token positions. Under measured CIM-chip noise, average perplexity across nine models rose from a clean 11.06 to 33.91 unprotected (Llama3.2-1B collapsing 15.42 → 100.78; Qwen3-8B 10.64 → 21.54), but attention-sink and recent-window tokens carry disproportionate sensitivity while middle-bulk tokens are near noise-tolerant — so protecting roughly 5% of tokens in high-precision digital storage recovers most of the loss (33.91 → ~11.95).

_Note:_ Graded medium: a single un-peer-reviewed 2026 preprint, no independent replication, and the noise model is injected into digital simulation rather than run on the chip.
Papers: source not in collection

## F13 — Medium confidence 2 claims merged · 3–0 unanimous
Charge-based analog gain cells targeting attention's KV-cache dot products project ~100× speedup and ~70,000× energy reduction versus an H100 (~6.1 nJ and ~65 ns per token per attention head). Circuit non-idealities — third-order polynomial nonlinearity, charge leakage, 4-bit queries / 3-bit stored K,V, HardSigmoid replacing softmax — make direct mapping of pre-trained weights impossible, so a hardware-aware adaptation step is mandatory; the authors mapped GPT-2 weights through a nonlinear gain-cell model rather than training from scratch.

_Note:_ Graded medium: SPICE simulation of the attention mechanism alone, no fabricated chip, explicitly excluding linear projections and end-to-end energy. The paper itself notes that substantial overall energy reductions require optimizing all components.
Papers: [2025_Leroux_GainCellAnalogAttention_NatCompSci](cards/2025_Leroux_GainCellAnalogAttention_NatCompSci.md)

## F14 — Medium confidence 3–0 unanimous
The field's framing of its own open problem has shifted: since floating-point-level inference accuracy has been demonstrated via hardware-aware training, the question is no longer whether analog can match digital accuracy but what device specifications are required at what fabrication cost — motivating systematic methodologies for mapping the multidimensional device-specification space, with PCM as the representative platform.

_Note:_ Graded medium: a research-agenda framing statement from a single recent paper, and it understates the residual gap seen at larger model scale (see F3, F10).
Papers: [2026_Wu_DeviceSpecMethodology_AdvIntellSyst](cards/2026_Wu_DeviceSpecMethodology_AdvIntellSyst.md), [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](cards/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md)

## F15 — High confidence 4 claims merged · 3–0 unanimous
The shared motivation across this literature is the memory wall: data movement between separate processing and memory units is the dominant time and energy cost in von Neumann systems, aggravated by data-centric AI workloads. In-memory computing computes in place inside the array by exploiting device physics; two-terminal resistive switching devices are the favoured substrate.

_Note:_ Nature Electronics 2018 · Nature Nanotechnology 2020
Papers: [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](cards/2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md), [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](cards/2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md)

## R1 — Refuted 0–3 Nature Materials 2026
“Accuracy, not energy efficiency, is the binding constraint on memristor-based analogue CIM — high efficiency and high accuracy cannot be achieved simultaneously.”

_Note:_ Consequence: do not present analog accuracy as fundamentally unachievable. The review this came from catalogues mitigation strategies; the claim overstated its own source.
Papers: [2026_Jiang_HighAccuracyMemristorCIM_NatMater](cards/2026_Jiang_HighAccuracyMemristorCIM_NatMater.md)

## R2 — Refuted 0–3 Nature Rev. Electrical Engineering 2025
“Conventional deep-learning compiler stacks (TVM, Glow, nGraph) cannot be reused for AIMC, making software a first-order bottleneck.”

_Note:_ Consequence: the software-stack story in this review is thin and should not be asserted. This is a genuine coverage gap, not a settled negative.
Papers: [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](cards/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md)

## R3 — Refuted 0–3 Nature Communications 2023
“Direct mapping of FP-trained DNN weights onto realistic PCM crossbars causes accuracy losses of roughly 1.3% to 23.9% across 11 benchmark networks.”


Papers: [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](cards/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md)

## R4 — Refuted 1–2 Nature Communications 2023
“Hardware-aware training makes analog-deployable not just small CNNs but large-scale, diverse architectures including BERT, RoBERTa, ALBERT, RNN/LSTM and CNN families.”

_Note:_ Consequence: the HWA-training evidence in F4 rests on the ALBERT chip paper, Analog Foundation Models and HERMES instead — not on this breadth claim.
Papers: [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](cards/2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md)

## R5 — Refuted 1–2 arXiv 2502.05948
“Per-ADC reference-tuning granularity is required because coarse per-module tuning fails on larger networks — ResNeXt50-32x4d on ImageNet failed entirely under per-module tuning.”


Papers: source not in collection

## N1 — Not adjudicated 
The December 2025 IBM Research perspective (Nature Electronics) frames the AIMC tile as the building block, buildable from volatile charge-based or non-volatile memristive memory; no single memory technology has been settled on, and signed multi-bit weight encoding and output conversion remain open design axes.

_Note:_ Reported in §10 of the review as a lead; never sampled into verification.
Papers: [2025_Singh_AIMCTileDesign_NatElectron](cards/2025_Singh_AIMCTileDesign_NatElectron.md)
