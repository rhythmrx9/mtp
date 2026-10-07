---
id: W4416728625
key: 2025_Malekar_PimLlm_MWSCAS
title: "Accelerating 1-Bit Llms Via in-Memory Computing Architectures"
short: "PIM-LLM (1-bit LLMs)"
year: 2025
venue: "MWSCAS"
venue_full: "2025 IEEE 68th International Midwest Symposium on Circuits and Systems (MWSCAS)"
authors: "Jinendra Malekar, Ramtin Zand"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["GPT-2 (355M)", "GPT-2 (774M)", "GPT-2 (1.5B)", "OPT-1.3B", "OPT-2.7B", "OPT-6.7B", "LLaMA-7B (1-bit)"]
param_scale: "355M-7B"
slm: true
evidence: simulation
topics: ["language-models", "transformer-accelerator", "heterogeneous-analog-digital", "quantization", "dataflow-pipelining", "attention", "energy-efficiency", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/mwscas53549.2025.11244527"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Malekar_PimLlm_MWSCAS.pdf"
fulltext: "../fulltext/2025_Malekar_PimLlm_MWSCAS.txt"
---

# PIM-LLM (1-bit LLMs)

**Accelerating 1-Bit Llms Via in-Memory Computing Architectures** — 2025 IEEE 68th International Midwest Symposium on Circuits and Systems (MWSCAS) (2025)

## TL;DR
PIM-LLM partitions 1-bit LLMs between analog RRAM crossbars (1-bit-weight projection layers) and a digital 8-bit systolic array (attention MatMuls), reaching up to 79.2x tokens/s (OPT-6.7B, context 128) and up to 70.58% better tokens/J than a digital TPU baseline in simulation.

## Summary
In decoder-only 1-bit LLMs, projection-layer weights are binary/ternary (W1A8) while activation-to-activation attention MatMuls still need 8-bit precision, and over 99% of MatMuls in larger models are low-precision. PIM-LLM maps the projection weights (WQ, WK, WV, WX and FFN) stationary onto memristive crossbars (pairs of devices with differential amplifiers, weight kernels expanded into crossbar columns), with DACs, 8-bit ADCs and post-processing units for LayerNorm/GELU, organised in banks/tiles/PEs. Attention (QK^T and softmax(.)V with the KV cache) is run on a 32x32 8-bit systolic array with an output-stationary dataflow (chosen by SCALE-Sim cycle-accurate comparison) and a ConSmax-style softmax unit, avoiding RRAM write energy and endurance problems. The TPU is synthesised in Verilog at 45 nm (100 MHz, 8 MB SRAM) and the PIM part is modelled with MNSIM 2.0 using 256x256 RRAM crossbars and 45 nm 8-bit ADCs. Workloads are GPT-2 (355M-1.5B), OPT (1.3B-6.7B) and LLaMA-7B at context lengths 128 to 4096, compared to an LLM-specific TPU baseline and published TransPIM and HARDSEA numbers.

## Language models evaluated
- Models: GPT-2 (355M), GPT-2 (774M), GPT-2 (1.5B), OPT-1.3B, OPT-2.7B, OPT-6.7B, LLaMA-7B (1-bit)
- Scale: 355M-7B
- Note: Hybrid analog RRAM-crossbar PIM plus digital systolic array for 1-bit (BitNet-style binary/ternary) decoder-only LLMs; evaluated on GPT-2 350M up to OPT-6.7B. Projection-layer MatMuls run as analog MVM on 256x256 RRAM crossbars; attention MatMuls on digital systolic arrays.

## Contributions
- Hybrid analog-PIM plus digital-systolic architecture matched to the precision split of 1-bit LLMs
- Claimed first analog-PIM architecture targeting decoder-only LLMs at OPT/LLaMA scale (up to ~7B)
- Cycle-accurate dataflow study (OS vs WS vs IS) and latency breakdown showing attention systolic arrays dominate
- Comparison to TransPIM and HARDSEA, plus a 'words per battery life' metric

## Key claims (stable IDs)
- **2025_Malekar_PimLlm_MWSCAS#C1** — Up to ~80x tokens/s over a digital TPU-LLM baseline — _support:_ 11.6x (GPT 350M) and 79.2x (OPT 6.7B) at context 128; 1.5x and 5.71x at context 4096 — _loc:_ Sec. IV-A, Fig. 5
- **2025_Malekar_PimLlm_MWSCAS#C2** — Tokens/J gains grow with context length and model size, while small models at short context are less efficient than the TPU — _support:_ TPU has 33.7% lower energy for GPT-2 350M at l=256-1024; PIM-LLM +12.49% (OPT 6.7B, l=128), +17.95% / +22.79% (l=2048), +70.58% / +33.7% (l=4096) — _loc:_ Sec. IV-C, Fig. 7
- **2025_Malekar_PimLlm_MWSCAS#C3** — Attention systolic arrays dominate latency; crossbar+DAC+ADC under 1% — _support:_ systolic arrays 60% (OPT 6.7B) to 73.9% (GPT-2 350M) at l=128, over 97% at l=4096 — _loc:_ Sec. IV-B, Fig. 6
- **2025_Malekar_PimLlm_MWSCAS#C4** — At least 2x GOPS and 5x GOPS/W over prior PIM LLM accelerators — _support:_ vs HARDSEA 3.2 GOPS (GPT-2 Small, l=1024), vs TransPIM below 200 GOPS/W (GPT-2 Medium, l=4096); OPT-6.7B reaches 58.5 GOPS and 1134 GOPS/W at l=1024 — _loc:_ Sec. IV-E, Table III

## Results
- Speedup over TPU-LLM: 11.6x GPT-350M and 79.2x OPT-6.7B at l=128; 1.5x and 5.71x at l=4096
- Energy: up to 70.58% (GPT-2 350M, l=4096) and 33.7% (OPT-6.7B, l=4096) more tokens/J; TPU wins by 33.7% on GPT-2 350M at l=256-1024
- OPT-6.7B: 58.5 GOPS / 1134.14 GOPS/W (l=1024); 17.6 GOPS / 1262.72 GOPS/W (l=4096)
- Words per battery (5 Wh, 1.5 tokens/word): OPT-6.7B 1.6M vs 1.4M words (l=128); at l=4096 GPT-2 350M 35M vs 20M words, OPT-6.7B 1.6M vs 1.2M

## Key numbers
- tech_node: 45nm
- array_size: 256x256 RRAM crossbars; 32x32 systolic array
- energy_eff: 1134.14 GOPS/W (OPT-6.7B, l=1024)
- throughput: up to 79.2x tokens/s vs TPU-LLM; 58.5 GOPS (OPT-6.7B, l=1024)
- bits_weight: 1b (binary/ternary) projections; 8b attention
- bits_adc: 8b

## Datasets / benchmarks
GPT-2 / OPT / LLaMA workload shapes (no accuracy datasets)

## Limitations
- Simulation only (MNSIM 2.0 plus synthesised TPU); no silicon
- Accuracy of 1-bit LLMs under RRAM variation, noise, IR drop and ADC quantisation is not evaluated, so throughput gains are optimistic
- Attention/KV cache stays digital and grows to over 97% of latency at long context
- Comparison to prior work relies on published numbers for smaller GPT-2 models rather than same-workload runs
- Text analysed is the arXiv PIM-LLM version; the packet metadata (MWSCAS 2025 title) may describe a shortened variant

## Remarks
A reasonable architectural partitioning argument: use weight-stationary analog crossbars only where weights are static and extremely quantised, keep dynamic KV-cache MatMuls digital to avoid RRAM write cost. The 1-bit weight assumption eases analog precision demands, but no noise-robustness evidence is shown, so this is a throughput/energy model rather than proof of accurate analog LLM inference. It contrasts with the gain-cell analog-attention work, which attacks exactly the digital attention bottleneck this design leaves.

## Cites (in collection, 9)
- [2020_Guo_ATT_ICCD](2020_Guo_ATT_ICCD.md) ATT (2020) — _contrasts/critiques_: "For example, designs like iMCAT [19], ATT [21], ReBERT [22], iMTransformer [24], and X-Former [25] focus on smaller-scale, encoder-only models such as BERT variants."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _contrasts/critiques_: "For example, designs like iMCAT [19], ATT [21], ReBERT [22], iMTransformer [24], and X-Former [25] focus on smaller-scale, encoder-only models such as BERT variants."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _baseline/comparison_: "As listed in Table III, TransPIM [18] presents several variations of its architecture, all achieving a GOPS/W below 200 on the GPT2 Medium model with a 4096 context length."
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023) — _uses-method-or-tool_: "To simulate the PIM component and assess its latency and energy consumption, we used MNSIM 2.0 [39] with 256 × 256 RRAM crossbars and 45nm 8-bit ADCs [40]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _contrasts/critiques_: "For example, designs like iMCAT [19], ATT [21], ReBERT [22], iMTransformer [24], and X-Former [25] focus on smaller-scale, encoder-only models such as BERT variants."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _baseline/comparison_: "In this work, we compare our approach with HARDSEA [26] and TransPIM [18]."
- [2023_Lu_RIME_TVLSI](2023_Lu_RIME_TVLSI.md) RIME (2023) — _contrasts/critiques_: "Meanwhile, RIME [20] and ReTransformer [23] are PIM-based architectures designed to accelerate conventional encoder-decoder transformers [28]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "The crossbars carry out MVM operations in parallel, applying Kirchhoff’s and Ohm’s Laws for analog computation [14, 16]."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _contrasts/critiques_: "Meanwhile, RIME [20] and ReTransformer [23] are PIM-based architectures designed to accelerate conventional encoder-decoder transformers [28]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Malekar_PimLlm_MWSCAS.pdf](../../11_Small_Language_Models_on_AIMC/2025_Malekar_PimLlm_MWSCAS.pdf)
- Full text: [../fulltext/2025_Malekar_PimLlm_MWSCAS.txt](../fulltext/2025_Malekar_PimLlm_MWSCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/mwscas53549.2025.11244527
