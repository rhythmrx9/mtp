---
id: W3211168157
key: 2021_Cao_NeuralPIM_TC
title: "Neural-PIM: Efficient Processing-In-Memory with Neural Approximation of Peripherals"
short: "Neural-PIM"
year: 2021
venue: "TC"
venue_full: "IEEE Transactions on Computers"
authors: "Weidong Cao, Yilong Zhao, Adith Boloor, Yinhe Han, Xuan Zhang, Li Jiang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG", "MobileNet", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["adc-dac", "peripheral-circuits", "crossbar-architecture", "dataflow-pipelining", "bit-slicing", "energy-efficiency", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 5
citations_overall: 22
priority_score: 4.88
doi: "https://doi.org/10.1109/tc.2021.3122905"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Cao_NeuralPIM_TC.pdf"
fulltext: "../fulltext/2021_Cao_NeuralPIM_TC.txt"
---

# Neural-PIM

**Neural-PIM: Efficient Processing-In-Memory with Neural Approximation of Peripherals** — IEEE Transactions on Computers (2021)

## TL;DR
Neural-PIM replaces ADCs and digital shift-and-add in RRAM PIM with small RRAM-crossbar neural approximators and an analog-accumulation dataflow, giving 5.36x (1.73x) energy efficiency and 3.43x (1.59x) throughput over ISAAC (CASCADE) in simulation.

## Summary
RRAM PIM accelerators spend most energy and area on high-resolution ADCs (58% of system energy in ISAAC). The paper first characterises the dataflows of ISAAC/PRIME/PipeLayer (quantize then digitally accumulate) and CASCADE (buffer analog partial sums in RRAM cells), then proposes a dataflow that does shift-and-add in the analog domain across input cycles before a single quantization. Two peripherals are built from small RRAM-crossbar neural networks plus CMOS inverters: NNS+A (analog shift-and-add/accumulation) and NNADC (quantizer), trained offline in TensorFlow with 3-bit weights and sigma=0.025 variation noise. Weights are 8-bit, stored as 1-bit RRAM cells with W_P and W_N in adjacent columns of the same 128x128 array (16 columns per 8-bit weight vector), inputs are streamed bit-serially, with eDRAM buffers and SRAM IRs/ORs. Evaluation uses circuit simulation (Cadence Spectre, 130 nm scaled to 32 nm) and a full-system simulator of a 280-tile chip with equal-area baselines on 8 CNNs plus NeuralTalk (RNN) trained on ImageNet at 8-bit. Results: average energy efficiency 5.36x vs ISAAC and 1.73x vs CASCADE, throughput 3.43x and 1.59x, accuracy preserved with about 50 dB SINAD. No silicon.

## Contributions
- Characterisation framework comparing analog dataflows of existing RRAM PIM accelerators.
- New analog-accumulation dataflow that reduces A/D conversions.
- NeuralPeriph: RRAM-crossbar neural approximators for shift-and-add (NNS+A) and ADC (NNADC).
- Neural-PIM accelerator architecture with system-level evaluation versus ISAAC and CASCADE.

## Key claims (stable IDs)
- **2021_Cao_NeuralPIM_TC#C1** — Neural-PIM improves energy efficiency 5.36x over ISAAC and 1.73x over CASCADE. — _support:_ averages over 8 CNNs + 1 RNN — _loc:_ Sec. 7.2, Fig. 12(a)
- **2021_Cao_NeuralPIM_TC#C2** — Throughput improves 3.43x vs ISAAC and 1.59x vs CASCADE. — _support:_ same benchmarks, equal area — _loc:_ Sec. 7.2, Fig. 12(b)
- **2021_Cao_NeuralPIM_TC#C3** — Analog S+A consumes 33x less energy than ISAAC ADCs. — _support:_ energy breakdown — _loc:_ Sec. 7.2, Fig. 13
- **2021_Cao_NeuralPIM_TC#C4** — Dataflow gives highest SINAD (about 50 dB), adequate for accuracy. — _support:_ SINAD comparison vs ISAAC and CASCADE — _loc:_ Sec. 5.3, Fig. 10-11

## Results
- 5.36x / 1.73x energy efficiency vs ISAAC / CASCADE (Fig. 12a).
- 3.43x / 1.59x throughput vs ISAAC / CASCADE (Fig. 12b).
- Array density (PE-level) 0.68% ISAAC, 0.76% CASCADE, 0.71% Neural-PIM (Table 3), i.e. comparable area.
- CASCADE has lowest SINAD due to 6-bit RRAM buffering.

## Key numbers
- tech_node: 32nm (scaled from 130nm CMOS circuit sim)
- array_size: 128x128
- energy_eff: 5.36x vs ISAAC, 1.73x vs CASCADE
- throughput: 3.43x vs ISAAC, 1.59x vs CASCADE
- accuracy: no loss; about 50 dB SINAD
- bits_weight: 8b (1-bit cells)
- bits_adc: NNADC (vs 8b ADC in ISAAC)

## Datasets / benchmarks
ImageNet, AlexNet, ResNet-50/101, VGG-16/19, Inception, GoogleNet, MobileNet, NeuralTalk

## Limitations
- Simulation only; NeuralPeriph validated by circuit simulation at 130 nm and scaled to 32 nm.
- Noise modeled as Gaussian on activations, not full device non-idealities.
- Only CNNs and one RNN; no Transformers or language models.
- Baselines are re-implementations of ISAAC/CASCADE scaled to 8-bit.

## Remarks
A peripheral-centric answer to the ADC bottleneck that is relevant for any AIMC mapping since ADC cost dominates. Evidence is architectural simulation with scaled component models, so absolute gains are indicative. Its analog accumulation idea is orthogonal to the model, but nothing is shown for attention-style workloads.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "Strategy A (Fig. 3(a)) conducts accumulation after quantizing BL analog partial sums. Prior work, e.g., ISAAC [1], PRIME [16], and PipeLayer [17], adopts this strategy."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _baseline/comparison_: "Strategy B (Fig. 3(b)) buffers analog partial sums from all input cycles before the quantization, capturing the scheme adopted by CASCADE [2]."
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019) — _uses-method-or-tool_: "We adopt a similar NoC implementation proposed in a prior work [31]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "For example, ISAAC [1] and CASCADE [2] adopt a 1-bit DAC to stream a 16-bit input with 16 cycles."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "For example, PRIME [16] and PipeLayer [17] adopt 1-bit SAs and IF neurons to successively perform 2n conversions to produce an n-bit output."

## Cited by (in collection, 2)
- [2023_Pelke_MultiCoreCNNMapping_VLSI-SoC](2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.md) Multi-core RRAM CNN Mapping (2023) — _background_: "Multiple RRAM devices can be arranged in crossbar structures to enable in-memory computing [16]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "In particular, both digital and analog PIM approaches have shown significant efficiency improvements - digital PIM reduces data movement costs while maintaining the accuracy for high bit-precision operations [16, 24, 32, 58, 60, 68, 79], and analog PIM demonstrates dramatic efficiency improvement, achieving more than two orders of magnitude benefit [5, 9, 17, 24] through low-voltage swing operations."

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Cao_NeuralPIM_TC.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2021_Cao_NeuralPIM_TC.pdf)
- Full text: [../fulltext/2021_Cao_NeuralPIM_TC.txt](../fulltext/2021_Cao_NeuralPIM_TC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tc.2021.3122905
