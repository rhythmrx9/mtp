---
id: W4381233128
key: 2023_Sridharan_X-Former_TVLSI
title: "X-Former: In-Memory Acceleration of Transformers"
short: "X-Former"
year: 2023
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2023"
authors: "Shrihari Sridharan, Jacob R. Stevens, Kaushik Roy, Anand Raghunathan"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-analog"]
models: ["Transformer", "BERT"]
lm_models: ["BERT-base", "BERT-large"]
param_scale: "110M-340M"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "attention", "heterogeneous-analog-digital", "dataflow-pipelining", "endurance-retention", "bit-slicing", "energy-efficiency", "language-models"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 16
cites_in_collection: 7
citations_overall: 66
priority_score: 13.96
doi: "https://doi.org/10.1109/tvlsi.2023.3282046"
pdf: "../../04_Transformers_and_LLMs/2023_Sridharan_X-Former_TVLSI.pdf"
fulltext: "../fulltext/2023_Sridharan_X-Former_TVLSI.txt"
---

# X-Former

**X-Former: In-Memory Acceleration of Transformers** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems, 2023 (2023)

## TL;DR
X-Former is a hybrid ReRAM/8T-SRAM in-memory Transformer accelerator that keeps static weights in ReRAM crossbars and computes dynamic QK^T/AV matmuls in SRAM CIM tiles with a sequence-blocking dataflow, reporting up to 85x latency and 7.5x energy gains over a GTX 1060 GPU.

## Summary
Attention requires data-dependent matrix products (MVM_Dynamic) that would force frequent NVM writes, which are slow, energy hungry and endurance-limited (10^6-10^9 writes). X-Former partitions the encoder: a Projection Engine of ReRAM crossbar tiles (36 tiles, 8 cores/tile, 6 crossbars/core, 128x128 2-bit ReRAM, 1-bit DAC, 8-bit SAR ADCs shared per crossbar) holds all layers' static weights spatially (bit-sliced 8-bit weights, bit-streamed activations) plus read-only ReRAM tiles for the embedding table, while an Attention Engine of attention-head compute tiles (8T-SRAM CIM banks, shift-add, special function units for softmax) computes Q*K^T and attention*V with Query/Value stationary dataflow, overwritten for every layer. A sequence-blocking dataflow (SB=64) pipelines the two engines and makes intermediate activation size depend on SB x SB rather than SL x SL. Evaluation uses a PUMAsim-based simulator with SPICE-measured SRAM macros, CACTI memories and 32nm synthesized digital units on BERT-base and BERT-large (8-bit W/Q/K/V) over GLUE (SL 512) and SQuAD (SL 384). Accuracy under crossbar non-idealities is checked with NeuroSim on WNLI, and baselines are a GTX 1060 GPU, a PUMA-style NVM accelerator, an ideal-endurance NVM crossbar architecture and an iso-area SRAM IMC design.

## Language models evaluated
- Models: BERT-base, BERT-large
- Scale: 110M-340M

## Contributions
- Hybrid NVM+CMOS in-memory Transformer architecture separating MVM_Static (ReRAM Projection Engine) from MVM_Dynamic (SRAM Attention Engine)
- Intra-layer sequence-blocking dataflow that raises utilization and removes quadratic intermediate storage
- Simulation framework built on PUMAsim with SPICE/CACTI/RTL models
- Comparison against GPU, NVM accelerator, ideal-NVM and SRAM IMC baselines

## Key claims (stable IDs)
- **2023_Sridharan_X-Former_TVLSI#C1** — X-Former with sequence blocking greatly reduces latency vs GPU — _support:_ up to 85x (GLUE) and 81x (SQuAD) speedup vs GTX 1060; 51.46 ms -> 0.98 ms per inference and 0.0158 -> 6.72 TOPS/W — _loc:_ Sec. VII-B, Fig. 8, Table IV
- **2023_Sridharan_X-Former_TVLSI#C2** — Energy efficiency gain over GPU and NVM accelerator — _support:_ 4.85x-7.5x (GLUE), 3.52x-5.31x (SQuAD) vs GPU; up to 10.7x latency and 4.6x energy over a state-of-the-art NVM accelerator — _loc:_ Sec. VII-C, Fig. 11
- **2023_Sridharan_X-Former_TVLSI#C3** — Hybrid design beats ReRAM-only crossbars even with an idealized endurance-free NVM — _support:_ 8.1x speedup over all-NVM architecture with NVM_Ideal — _loc:_ Fig. 9
- **2023_Sridharan_X-Former_TVLSI#C4** — Analog non-idealities cost modest accuracy at low variation but more for deeper models — _support:_ <1% loss at variation 0-0.2; ~4.2% (BERT-base) and 9.87% (BERT-large) at higher variation on WNLI (software 56.34%) — _loc:_ Sec. VII-A, Fig. 7

## Results
- Without sequence blocking: ~10x average speedup over GPU; with SB=64 up to 85x/81x (Fig. 8)
- vs iso-area SRAM IMC: 1.82x/2.03x speedup and 52.1x/36.8x energy efficiency for BERT-base/large at SL 512
- Energy per encoder at SL=512: 15.2 uJ, 58% in Attention Engine, 28% in Q/K/V projection (Fig. 12)
- ADC is 36.8% of NVM engine MVM energy vs 12.1% in the SRAM attention engine
- Speedup declines at large sequence lengths (Fig. 8)

## Key numbers
- tech_node: 32nm (digital synthesis)
- array_size: 128x128 ReRAM crossbars; 8T-SRAM banks
- energy_eff: 6.72 TOPS/W (with sequence blocking) vs 0.0158 GPU
- throughput: 0.98 ms/inference vs 51.46 ms GPU
- accuracy: 4.2% (BERT-base) / 9.87% (BERT-large) WNLI loss at high variation
- bits_weight: 8b (2-bit ReRAM cells, bit-sliced)
- bits_adc: 8-bit SAR @ 1.28 GS/s

## Datasets / benchmarks
GLUE, SQuAD, WNLI

## Limitations
- Architecture-level simulation only; no silicon
- Accuracy study uses a single GLUE task (WNLI, near-chance 56.34% baseline) and NeuroSim variation sweeps
- Scaling requires more ReRAM tiles for larger models, no chip-to-chip evaluation
- Attention Engine sized for one layer, so encoder layers run sequentially
- Weak GPU baseline (GTX 1060) and encoder-only BERT; no decoder or KV-cache considerations

## Remarks
Influential partition of 'static weights in NVM, dynamic attention in SRAM', adopted by many later hybrid transformer accelerators, with a clean endurance argument against mapping QK^T on ReRAM. The evidence is architectural simulation with a thin accuracy analysis, so the noise-robustness side of running BERT on crossbars is underexplored. It addresses BERT-scale encoders (110M-340M), which sits at the small end of the LM range relevant to analog deployment; autoregressive decoding is not covered.

## Use in the original review
- F6 (High confidence): The central architectural gap between CNN-era analog IMC accelerators and transformer workloads is self-attention's dynamic matrix-matrix multiplication: both operands are input-dependent, so crossbars must be reprogrammed per self-attention layer. At sequence length 256 these dynamic MVMs consume 80% of total runtime, and the compute-write-compute dependency stalls MatMul until KT is written column by column.
- F9 (High confidence): Device non-idealities are the physical limit and span a hierarchy, not just the material: memory window, read noise, program noise and conductance drift act on different time scales while constraining manufacturability; errors originate at device, array, architecture and algorithm levels. NVM writes cost 1–2 orders of magnitude more latency and energy per bit than SRAM, with ~106–109 write endurance.

## Cites (in collection, 7)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Recently, various hardware accelerators have been proposed to improve the efficiency and performance of traditional deep learning networks [4, 12–16]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _baseline/comparison_: "We also compare our results with an in-memory NVM accelerator [14] where the MVM Dynamic operations are executed in the temporal 1-D SIMD lanes instead of the NVM tiles due to limited endurance."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _motivation_: "This is a challenge due to NVMs requiring atleast one to two orders of magnitude higher latency and energy/bit depending on the NVM device compared to SRAM for the same technology node [8]–[10]."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _background_: "Due to the analog nature of computations in X-Former, functional errors are introduced in the inference pass that impacts the overall application level accuracy [33], [34]."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _motivation_: "NVM devices also have very limited endurance, only about 10^6-10^9 conservative writes [8]–[10] which degrades the lifetime of these devices swiftly and limits their applicability to Transformers."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _contrasts/critiques_: "Both the works use NVM crossbars to accelerate both MVM Static and MVM Dynamic operations. While they propose techniques to reduce latency of reprogramming the NVM crossbars, these devices offer very low endurance which can degrade their lifetime quickly."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Recently, various hardware accelerators have been proposed to improve the efficiency and performance of traditional deep learning networks [4, 12–16]."

## Cited by (in collection, 16)
- [2024_Pan_PRIMATE_ASP-DAC](2024_Pan_PRIMATE_ASP-DAC.md) PRIMATE (2024) — _background_: "Previous works [19, 27] have shown a software-hardware co-designed PIM architecture can provide better throughput and power consumption than GPU and TPU for Transformers."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _background_: "Recent works [7–10] have proposed compact, energy-efficient and lowlatency implementations of transformers on IMC architectures using efficiency-driven hardware optimizations and architectural modifications."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _contrasts/critiques_: "Similar to ATT [16], X-Former [39] also employs dedicated CMOS-based processing units with SRAM-based crossbar arrays to handle intermediate results of Transformers."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _background_: "Recent IMC-centric transformer co-optimization works [10], [11], [18] have proposed IMC architecture implementations to efficiently compute the Matmul layers."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "Hence, standalone NVM-based PIM architectures are not suitable for transformer fine-tuning and inference [12]."
- [2025_Dong_TopkimaFormer_TCAS-I](2025_Dong_TopkimaFormer_TCAS-I.md) Topkima-Former (2025) — _contrasts/critiques_: "Subsequently, X-former proposes a hybrid IMC architecture built up with RRAM and SRAM together to efficiently execute different workloads of transformer [4]. However, it lacks a comprehensive co-design from circuit level, to architecture level and up to algorithm level."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "Compared to conventional architectures, CIM significantly mitigates persistent memory wall problem [49] and demonstrates strong competitiveness in data-intensive applications especially deep neural network (DNN) inference [38, 43, 52]."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _baseline/comparison_: "Other CIM works focused on content addressable memories for softmax, ReRAMSRAM hybrid architecture, and processing in off-chip memory to facilitate efficient data communication during transformer inference [26, 32, 33]."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _contrasts/critiques_: "KV cache has been implemented either by dynamic random-access memories (DRAMs)21,23, which have limited parallelism requiring many digital sequential adders, or by SRAMs19,24, which are limited by their volatility and relatively low density25."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _baseline/comparison_: "Previous studies have proposed using SRAM-based Analog CIM [7, 10, 13, 16] or Digital CIM [8, 9] to perform DMM operations."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _background_: "In this paper, we propose deploying finetuned LLMs on hybrid CIM, leveraging both the energy efficiency and computational density of RRAM and the noise-free computation of SRAM [64, 65]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _contrasts/critiques_: "For example, designs like iMCAT [19], ATT [21], ReBERT [22], iMTransformer [24], and X-Former [25] focus on smaller-scale, encoder-only models such as BERT variants."
- [2026_Zheng_InterfaceKVQ_ICCAD](2026_Zheng_InterfaceKVQ_ICCAD.md) InterfaceKVQ (2026) — _motivation_: "Prior work questions whether NVM suits data updated during decoding [11, 26], so we quantify the write cost."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)

## Files
- PDF: [../../04_Transformers_and_LLMs/2023_Sridharan_X-Former_TVLSI.pdf](../../04_Transformers_and_LLMs/2023_Sridharan_X-Former_TVLSI.pdf)
- Full text: [../fulltext/2023_Sridharan_X-Former_TVLSI.txt](../fulltext/2023_Sridharan_X-Former_TVLSI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tvlsi.2023.3282046
