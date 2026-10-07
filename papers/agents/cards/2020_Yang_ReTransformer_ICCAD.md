---
id: W3111375540
key: 2020_Yang_ReTransformer_ICCAD
title: "ReTransformer"
short: "ReTransformer"
year: 2020
venue: "ICCAD"
venue_full: "39th IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2020)"
authors: "Xiaoxuan Yang, Bonan Yan, Hai Li, Yiran Chen"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer", "BERT"]
lm_models: ["Transformer base (65M, encoder-decoder, WMT16 En-De)"]
param_scale: "~65M (base Transformer); BERT 108M cited only for quantisation-variation sensitivity"
slm: false
evidence: algorithm+simulation
topics: ["transformer-accelerator", "attention", "dataflow-pipelining", "nonlinear-functions", "weight-mapping", "heterogeneous-analog-digital", "endurance-retention", "device-variation"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 16
cites_in_collection: 5
citations_overall: 80
priority_score: 11.52
doi: "https://doi.org/10.1145/3400302.3415640"
pdf: "../../04_Transformers_and_LLMs/2020_Yang_ReTransformer_ICCAD.pdf"
fulltext: "../fulltext/2020_Yang_ReTransformer_ICCAD.txt"
---

# ReTransformer

**ReTransformer** — 39th IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2020) (2020)

## TL;DR
ReRAM-PIM Transformer accelerator that decomposes Q*K^T into (Q*W_K^T)*X^T so intermediate K is never written to crossbars, adds an in-memory-logic hybrid softmax and a sub-matrix pipeline, simulated at 23.21x GPU and 3.25x PipeLayer computing efficiency.

## Summary
Transformer self-attention needs matrix-matrix products whose both operands are runtime intermediates, so standard ReRAM PIM must write K^T into a crossbar before every Q*K^T, causing a compute-write-compute (CWC) stall, high write energy and endurance wear (programming ~7.2 ns/column, Sec. 3). ReTransformer rewrites Out = Q*K^T = (Q*W_K^T)*X^T, so crossbars hold only static W_Q, W_K^T and X^T (one copy of X with a dual-access crossbar also serves S*X), and no intermediate is programmed (Sec. 4.2, Fig. 6). Scaling by 1/sqrt(d_k) is a 3-bit shift for d_k=64, and softmax is implemented as a hybrid: max-subtraction, ReRAM in-memory logic (NOR/XOR/INV, compare 13 cycles, select 8 cycles) for compare/select, and lookup tables for exp and log, avoiding division (Sec. 4.3, Fig. 7). A sub-matrix pipeline flattens Q and R into vectors and feeds d_k-length segments cycle by cycle to keep subarrays busy instead of layer-granularity pipelining (Sec. 4.4, Fig. 8). Evaluation uses NeuroSim-based circuit parameters, 2-bit cells, 8-bit weights/activations (quantisation-aware training; BLEU 31.17 to 30.45 for Model A) for two Transformer models (A base, B larger) on WMT 2016 En-De, compared with a GPU and PipeLayer (Sec. 5). The optimised MatMul cuts latency 1.32x (Model A) and 1.16x (Model B); the hybrid softmax uses 0.6913 mW vs 1.0233 mW CMOS; overall 467.68 GOPs/s/W.

## Language models evaluated
- Models: Transformer base (65M, encoder-decoder, WMT16 En-De)
- Scale: ~65M (base Transformer); BERT 108M cited only for quantisation-variation sensitivity

## Contributions
- ReRAM-based PIM architecture for Transformer inference with processing, buffer and memory subarrays.
- Matrix-decomposition MatMul that removes the compute-write-compute dependency and avoids rewriting intermediates in ReRAM.
- ReRAM in-memory-logic hybrid softmax with lookup-table exp/log, lowering power vs a CMOS softmax.
- Sub-matrix (fine-grained) pipeline for multi-head self-attention.

## Key claims (stable IDs)
- **2020_Yang_ReTransformer_ICCAD#C1** — Eliminating K^T writes via matrix decomposition reduces MatMul latency. — _support:_ 1.32x (Model A) and 1.16x (Model B) latency reduction — _loc:_ Sec. 5, Fig. 9
- **2020_Yang_ReTransformer_ICCAD#C2** — ReTransformer improves computing efficiency over GPU and PipeLayer. — _support:_ 23.21x vs GPU, 3.25x vs PipeLayer; power reduced 1086x and 2.82x; 467.68 GOPs/s/W — _loc:_ Abstract, Fig. 11
- **2020_Yang_ReTransformer_ICCAD#C3** — Hybrid ReRAM softmax lowers power relative to CMOS. — _support:_ 0.6913 mW vs 1.0233 mW; compare/select logic 0.3889 mW vs 0.533 mW — _loc:_ Fig. 10
- **2020_Yang_ReTransformer_ICCAD#C4** — 8-bit quantisation costs little translation quality. — _support:_ BLEU 31.17 to 30.45 for Model A — _loc:_ Sec. 5 discussion
- **2020_Yang_ReTransformer_ICCAD#C5** — Transformer accuracy is sensitive to ReRAM weight variation. — _support:_ 2.5/5/7.5/10% weight mismatch gives 0.50/5.09/21.27/38.54% accuracy drop for quantised BERT on QNLI (baseline 90.79%) — _loc:_ Sec. 5 discussion

## Results
- Latency of MatMul reduced 1.32x/1.16x for Models A/B by removing K^T writes (Fig. 9).
- Finer sub-matrix pipeline outperforms layer-granularity pipeline in throughput (Table 3; numeric values not recoverable from extracted text).
- Model A has 145 softmax layers, so softmax power matters far more than in CNNs.
- Compare logic takes 13 cycles and select logic 8 cycles in ReRAM in-memory logic.

## Key numbers
- energy_eff: 467.68 GOPs/s/W
- throughput: 23.21x computing efficiency vs GPU; 3.25x vs PipeLayer
- accuracy: BLEU 31.17 (FP) to 30.45 (8-bit), Model A
- bits_weight: 8b (2-bit cells)

## Datasets / benchmarks
WMT 2016 En-De translation (newstest2016), QNLI (variation sensitivity, via Q8BERT)

## Limitations
- Simulation only (NeuroSim-based circuit parameters, in-house latency model); no fabricated hardware.
- Ideal analog behaviour assumed; reliability is discussed only as compatibility with existing methods, with the BERT variation sensitivity quoted from a separate experiment.
- Small encoder-decoder Transformer on WMT16, not decoder-only LMs; KV-cache growth for autoregressive decoding is not analysed.
- In-memory logic endurance is acknowledged as an open issue; GPU/PipeLayer baselines use different technologies and settings.
- Extracted text lacks numeric content of Tables 1-3, so model dimensions and Table 3 throughput values are not reported here.

## Remarks
One of the first (2020) ReRAM-PIM designs specifically addressing attention's dynamic matrix-matrix products; its key observation, that Q*K^T needs intermediates written to NVM, is the core obstacle for analog crossbars with attention and is the origin of later work on avoiding or tolerating K/V writes (e.g. X-Former and other designs that cite it in this collection). The decomposition trades extra stored matrices and multiplications for fewer writes, which grows with sequence length, so it is not obviously viable for LLM-size contexts. The BERT variation numbers are a sobering data point for analog noise tolerance of transformers.

## Use in the original review
- F6 (High confidence): The central architectural gap between CNN-era analog IMC accelerators and transformer workloads is self-attention's dynamic matrix-matrix multiplication: both operands are input-dependent, so crossbars must be reprogrammed per self-attention layer. At sequence length 256 these dynamic MVMs consume 80% of total runtime, and the compute-write-compute dependency stalls MatMul until KT is written column by column.
- F7 (Medium confidence): The write bottleneck is being attacked algorithmically rather than only with better devices, via reformulations that keep the static weight matrix in the crossbar; dedicated ReRAM PIM transformer accelerators report large gains (ReTransformer: 23.21× efficiency and 1086× power versus GPU).

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "Pipelayer [27] enables neural network training with ReRAM, and further optimizes the computation latency by using pipelined stages and balancing computation resources."
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018) — _background_: "A ReRAM-based PIM design for RNN [20] extends to RNN acceleration with multiplier arrays and special function units to handle element-wise multiplication and nonlinear functions."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "We simulate the ReRAM circuit parameters using NeuroSim [22] based on the ReRAM and peripheral configurations [23] shown in Table 1(b)."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "PRIME [4] and ISAAC [24] designs utilize ReRAM to accelerate the inference of CNNs."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "PRIME [4] and ISAAC [24] designs utilize ReRAM to accelerate the inference of CNNs."

## Cited by (in collection, 16)
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) Area-Efficient Multi-Task BERT (2021) — _background_: "By exploiting in-memory computation, the ReRAM-based accelerator enables energy-efficient execution of a single BERT model [29]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _contrasts/critiques_: "Both the works use NVM crossbars to accelerate both MVM Static and MVM Dynamic operations. While they propose techniques to reduce latency of reprogramming the NVM crossbars, these devices offer very low endurance which can degrade their lifetime quickly."
- [2023_Cao_RRAMPoolFormer_ISCAS](2023_Cao_RRAMPoolFormer_ISCAS.md) RRAM-PoolFormer (2023) — _contrasts/critiques_: "For example, the self-attention operation is decomposed to reduce the frequency of intermediate results reloading and transfers the Softmax function to logical inference with lookup table [24]. However, these reported solutions still require considerable computation resources."
- [2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC](2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.md) Reconfigurable Sparse-Attention NVPIM (2023) — _baseline/comparison_: "For the baseline NVPIM accelerators, we quantitatively compare our design with ReTransformer [3], as implemented with our cycle-accurate simulator. ReTransformer is designed for dense attention computation, so we apply the method proposed in SRE [6] to support the sparse attention."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _baseline/comparison_: "For example, ReTransformer [50] tries to reduce the number of write operations and overlap the write latency with other ongoing analog MVMs."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "ReTransformer proposes a ReRAM-based PIM architecture to accelerate transformer inference [21]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _contrasts/critiques_: "However, it has shown limited improvement due to less parallelism in General matrix-vector multiplications (GEMV) operations than analog PIMs [72], falling short of fully leveraging the substantial potential for energy and delay efficiency offered by lowswing analog operations."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _contrasts/critiques_: "Non-volatile memories can be used for linear layers of transformers17, but are too slow, energy expensive and are not endurant enough for dynamical KV-cache writing18,22."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _contrasts/critiques_: "The third approach, as demonstrated in ReTransformer [6], directly computes DMMuls and Softmax within RRAM crossbars by programming the inputs into the array. While promising, it suffers from the inherent drawbacks of RRAM’s slow writes and limited endurance [19]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _contrasts/critiques_: "Meanwhile, RIME [20] and ReTransformer [23] are PIM-based architectures designed to accelerate conventional encoder-decoder transformers [28]."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023)
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2025_Li_CIMLLMDataflow_ISVLSI](2025_Li_CIMLLMDataflow_ISVLSI.md) CIM-LLM Dataflow (2025)
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024)

## Files
- PDF: [../../04_Transformers_and_LLMs/2020_Yang_ReTransformer_ICCAD.pdf](../../04_Transformers_and_LLMs/2020_Yang_ReTransformer_ICCAD.pdf)
- Full text: [../fulltext/2020_Yang_ReTransformer_ICCAD.txt](../fulltext/2020_Yang_ReTransformer_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3400302.3415640
