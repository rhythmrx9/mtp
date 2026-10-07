---
id: W4408563999
key: 2025_Dong_TopkimaFormer_TCAS-I
title: "Topkima-Former: Low-Energy, Low-Latency Inference for Transformers Using Top- k In-Memory ADC"
short: "Topkima-Former"
year: 2025
venue: "TCAS-I"
venue_full: "IEEE Transactions on Circuits and Systems I: Regular Papers"
authors: "Shuai Dong, Junyi Yang, Xiaoqi Peng, Hongyang Shang, Ye Ke, Xiaofeng Yang, H. Liu, Arindam Basu"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-analog"]
models: ["Transformer", "BERT", "ViT"]
lm_models: ["BERT-base", "DistilBERT"]
param_scale: "66M-110M"
slm: true
evidence: algorithm+simulation
topics: ["transformer-accelerator", "attention", "nonlinear-functions", "adc-dac", "heterogeneous-analog-digital", "quantization", "peripheral-circuits", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 3
citations_overall: 7
priority_score: 7.63
doi: "https://doi.org/10.1109/tcsi.2025.3549060"
pdf: "../../04_Transformers_and_LLMs/2025_Dong_TopkimaFormer_TCAS-I.pdf"
fulltext: "../fulltext/2025_Dong_TopkimaFormer_TCAS-I.txt"
---

# Topkima-Former

**Topkima-Former: Low-Energy, Low-Latency Inference for Transformers Using Top- k In-Memory ADC** — IEEE Transactions on Circuits and Systems I: Regular Papers (2025)

## TL;DR
Topkima merges top-k selection into a ramp in-memory ADC on the SRAM Q.K^T macro so only k=5 scores reach softmax, giving a ~15x faster softmax macro and 1.8x-84x speedup over prior IMC transformer accelerators with 0.4%-1.2% accuracy loss.

## Summary
Softmax can take up to 40% of transformer inference time and existing approximations (base-2, Taylor, I-BERT) still process all inputs, while digital top-k needs O(SL) sorting (at least 75% of latency by the authors' estimate). Topkima uses an in-memory ADC (IMA) on a dual 10T SRAM array that stores K^T, with Q applied by pulse-width-modulated wordlines; replacing the increasing ramp by a decreasing ramp makes the largest MAC voltages cross first, so the first k conversions are the top-k and the ramp stops early (saving ADC energy/latency), with no sorting. Because crossbar rows are partly used for ADC replica/calibration cells, K^T is split across sub-crossbars with sub-top-k values (e.g. k1=3 and k2=2 on 256x256 arrays, 4-bit K^T; ternary K^T with three 128x128 arrays) that are merged into a global top-5 before a digital softmax. Algorithmically, top-k forward / complete backward propagation (TFCBP) trains with only top-k in the forward pass and all activations in backward, and QAT (5-bit Q/activations, 4-bit K^T, 8-bit PTQ projection weights) keeps accuracy. Architecturally, projection weights W_Q,K,V sit on RRAM IMC, attention products on SRAM IMC, a scale-free trick folds 1/sqrt(d_k) into W_Q and a fine pipeline schedules dataflow. Evaluation combines SPICE (65 nm) for the Q.K^T macro, NeuroSim for the rest of one BERT-base attention module on SQuAD, and software accuracy runs of ViT (CIFAR-10/100) and DistilBERT/BERT-base (SQuAD v1.1).

## Language models evaluated
- Models: BERT-base, DistilBERT
- Scale: 66M-110M

## Contributions
- Topkima: top-k selection fused with ramp in-memory ADC giving sorting-free, early-stopping softmax input generation
- TFCBP training and sub-top-k aggregation to handle crossbar size limits
- Scale-free attention (1/sqrt(d_k) absorbed into W_Q) and fine-grained pipeline
- System comparison against ELSA, ReTransformer, X-Former and HARDSEA

## Key claims (stable IDs)
- **2025_Dong_TopkimaFormer_TCAS-I#C1** — Topkima softmax macro is ~15x faster than conventional softmax and ~8x faster than digital top-k — _support:_ Energy 30x and 3x lower respectively — _loc:_ Sec. IV-B / Fig. 4(a)
- **2025_Dong_TopkimaFormer_TCAS-I#C2** — k=5 gives <1.2% accuracy drop across ViT, DistilBERT, BERT-base — _support:_ 0.4% to 1.2% drop (ViT CIFAR-10 top-1 only 0.4% loss) — _loc:_ Sec. IV-A / Fig. 3
- **2025_Dong_TopkimaFormer_TCAS-I#C3** — Full system is 1.8x-84x faster and 1.3x-35x more energy efficient than prior IMC accelerators — _support:_ 6.70 TOPS and 16.84 TOPS/W at 200 MHz (abstract states 1.2x-36x EE) — _loc:_ Table 1 / Sec. IV-B
- **2025_Dong_TopkimaFormer_TCAS-I#C4** — Scale-free design speeds attention — _support:_ 2.4x vs left-shift scaling, 1.5x vs Tron free-scale — _loc:_ Fig. 4(d)

## Results
- Topkima-SM latency ~15x lower than conventional and ~8x lower than digital-top-k softmax; energy 30x and 3x lower (Fig. 4a)
- Circuit non-ideality injection (IMA error distribution over 256 conversions) lowers SQuAD accuracy from 86.7% to 85.1% (Fig. 4b)
- 256x256 crossbars sufficient for accuracy close to global top-k; 128x128 gives ternary K^T and 3 sub-top-k so larger degradation (Fig. 4c)
- Table 1: 6.70 TOPS and 16.84 TOPS/W at 200 MHz with 5-bit ADC and 256x256 arrays; baseline rows (X-Former, HARDSEA, ELSA, ReTransformer) partially garbled in extraction

## Key numbers
- tech_node: 65nm SPICE for macro; NeuroSim 32nm system
- array_size: 256x256 SRAM sub-arrays (K^T: (64x3)x256 + (64x3)x128 per head)
- energy_eff: 16.84 TOPS/W
- throughput: 6.70 TOPS at 200 MHz
- accuracy: 0.4%-1.2% drop at k=5; SQuAD 86.7% to 85.1% with circuit error
- bits_weight: 8b projection (RRAM), 4b K^T, 5b Q/A/V
- bits_adc: 5b in-memory ramp ADC

## Datasets / benchmarks
SQuAD v1.1, CIFAR-10, CIFAR-100

## Limitations
- Hardware numbers are SPICE plus NeuroSim estimates; only one BERT-base attention module costed and extrapolated
- No fabricated chip; noise is modelled by injecting measured-from-simulation IMA error only into SRAM-mapped products
- Encoder models (BERT-base, DistilBERT) and ViT only, no generative LLMs or KV-cache
- Table 1 extraction is garbled so some baseline figures are unreliable; no dedicated pipelining in the compared system
- Top-k restricted to attention softmax; RRAM projection layers modelled without device noise

## Remarks
Neat circuit/algorithm co-design that attacks the softmax bottleneck rather than MVM energy and ties it to existing in-memory ADC hardware; strong claims (84x) are against a mixed set of baselines and normalisation is unclear. The sub-top-k limitation by crossbar size is a useful, honest design constraint. Relevant to LM mapping because softmax and long sequences dominate latency once MVMs are in memory; complements HARDSEA/X-Former hybrid RRAM-SRAM designs in the collection.

## Cites (in collection, 3)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "The overall system simulation, conducted using the NeuroSim framework [5], comprises chip, tile, processing element (PE) and array hierarchies."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _contrasts/critiques_: "Subsequently, X-former proposes a hybrid IMC architecture built up with RRAM and SRAM together to efficiently execute different workloads of transformer [4]. However, it lacks a comprehensive co-design from circuit level, to architecture level and up to algorithm level."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _baseline/comparison_: "Compared to ELSA [22], ReTransformer [1], X-Former [4] and HARDSEA [23], Topkima-Former can achieve 1.8x-84x higher speed, and 1.3x-35x energy reduction, respectively."

## Files
- PDF: [../../04_Transformers_and_LLMs/2025_Dong_TopkimaFormer_TCAS-I.pdf](../../04_Transformers_and_LLMs/2025_Dong_TopkimaFormer_TCAS-I.pdf)
- Full text: [../fulltext/2025_Dong_TopkimaFormer_TCAS-I.txt](../fulltext/2025_Dong_TopkimaFormer_TCAS-I.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcsi.2025.3549060
