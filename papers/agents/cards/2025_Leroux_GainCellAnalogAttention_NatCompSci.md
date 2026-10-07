---
id: W4414064893
key: 2025_Leroux_GainCellAnalogAttention_NatCompSci
title: "Analog in-memory computing attention mechanism for fast and energy-efficient large language models"
short: "Gain-Cell Analog Attention"
year: 2025
venue: "NatCompSci"
venue_full: "Nature Computational Science, vol. 5, pp. 813-824 (2025)"
authors: "Nathan Leroux, Paul-Philipp Manea, Chirag Sudarshan, Jan Finkbeiner, Sebastian Siegel, John Paul Strachan, Emre Neftci"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["Gain-cell", "Charge/Capacitor"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["GPT-2 (124M)", "GPT-2-XL (1.5B)"]
param_scale: "124M-1.5B"
slm: true
evidence: simulation
topics: ["attention", "kv-cache", "transformer-accelerator", "language-models", "adc-dac", "nonlinear-functions", "hardware-aware-training", "3d-integration"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 3
cites_in_collection: 8
citations_overall: 24
priority_score: 13.28
doi: "https://doi.org/10.1038/s43588-025-00854-1"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Leroux_GainCellAnalogAttention_NatCompSci.pdf"
fulltext: "../fulltext/2025_Leroux_GainCellAnalogAttention_NatCompSci.txt"
---

# Gain-Cell Analog Attention

**Analog in-memory computing attention mechanism for fast and energy-efficient large language models** — Nature Computational Science, vol. 5, pp. 813-824 (2025) (2025)

## TL;DR
Gain-cell (capacitor) analog IMC arrays store the KV cache and compute both attention dot products with ADC-free charge-to-pulse HardSigmoid blocks, and an adaptation algorithm maps pre-trained GPT-2 onto them, giving GPT-2-comparable benchmark accuracy and ~100x (H100) lower attention latency and ~70,000x lower attention energy.

## Summary
The paper targets the KV-cache loading bottleneck of autoregressive transformers on GPUs. It proposes sliding-window attention executed entirely in the analog domain on two 64x64 CMOS gain-cell arrays per sub-tile: keys and values are written column-wise as capacitor voltages (3-bit, via DACs), the query is applied as 4-bit PWM pulses, the first array computes Q.K^T, a charge-to-pulse circuit integrates the currents and implements a HardSigmoid replacing softmax, its PWM output drives the second array computing phi(S).V, and a signed charge-to-pulse block plus 16-level counter (5-bit output with sign) digitises the result. A head with window M=1024 and d=64 uses 16 sub-tiles whose outputs are summed digitally. Because the gain-cell multiplication is nonlinear (third-order polynomial), leaks (tau=5 ms), and the model differs from standard attention (HardSigmoid, sliding window, 4/3/5-bit quantisation), pre-trained weights cannot be mapped directly; the authors fine-tune a linear intermediate model on OpenWebText and then apply a layer-wise scaling adaptation algorithm before final fine-tuning. Evaluation is by SPICE-calibrated simulation on ARC-E/C, WinoGrande, HellaSwag, LAMBADA, PIQA and WikiText-2, with energy/latency/area from synthesised layout.

## Language models evaluated
- Models: GPT-2 (124M), GPT-2-XL (1.5B)
- Scale: 124M-1.5B
- Note: GPT-2 and GPT-2-XL (1.5B) adapted to a gain-cell analog in-memory attention design, evaluated by simulation/hardware modeling with energy/latency compared against digital GPUs; GPT-2 scale is SLM-range.

## Contributions
- Mixed analog-digital gain-cell attention architecture that stores K/V and computes both dot products in memory
- ADC-free end-to-end analog attention using charge-to-pulse circuits implementing HardSigmoid
- Fine-tuning plus nonlinearity-adaptation algorithm that maps pre-trained GPT-2 to non-ideal hardware without training from scratch
- Quantitative energy, latency, and area analysis with floorplan, including 3D-stacking estimates

## Key claims (stable IDs)
- **2025_Leroux_GainCellAnalogAttention_NatCompSci#C1** — Hardware attention model matches public GPT-2 benchmark accuracy without training from scratch — _support:_ Table 1 shows public GPT-2 avg acc 43.02 / ppl 36.26 vs scratch software 41.46 / 43.82; hardware models are comparable or better than scratch — _loc:_ Table 1, Downstream task benchmarks
- **2025_Leroux_GainCellAnalogAttention_NatCompSci#C2** — Adaptation algorithm repairs the nonlinear gain-cell mapping — _support:_ perplexity reduced from 1,757 to 21 during adaptation — _loc:_ Fig. 4c
- **2025_Leroux_GainCellAnalogAttention_NatCompSci#C3** — Linear intermediate model reaches GPT-2 quality in far fewer iterations than training from scratch — _support:_ <3,000 iterations vs >13,000 — _loc:_ Fig. 4d
- **2025_Leroux_GainCellAnalogAttention_NatCompSci#C4** — Attention latency 65 ns and 6.1 nJ per token per head — _support:_ 1,120 pJ + 700 pJ arrays, 4 nJ digital control/routing (113.7 mW), 330 pJ DACs — _loc:_ Energy consumption and latency, Fig. 5
- **2025_Leroux_GainCellAnalogAttention_NatCompSci#C5** — Large attention-only speed and energy gains over GPUs — _support:_ speed-up x7,000 Jetson Nano, x300 RTX 4090, x100 H100; energy reduction x40,000, x90,000, x70,000 — _loc:_ Fig. 5c,d

## Results
- 65 ns attention latency; 6.1 nJ per token per head (Fig. 5)
- Attention-only speed-up x100 vs H100, x300 vs RTX 4090, x7,000 vs Jetson Nano; energy reduction x70,000 / x90,000 / x40,000 respectively
- Head area 0.5 mm2 incl. digital control (6T gain cell ~1 um2); GPT-2 attention-head KV cache crossbars 15.7e-3 mm2 excl. control; 3D stacking 36.7e-3/N mm2 (N=12: 3.1e-3 mm2)
- GPT-2-XL (1.5B) hardware model falls slightly short of public checkpoint but matches from-scratch software XL (Table 1)
- CMOS gain-cell retention tau = 5 ms; OSFET gain cells quoted as orders of magnitude longer

## Key numbers
- array_size: 64x64 gain-cell arrays; 16 sub-tiles per head (M=1024, d=64)
- energy_eff: 6.1 nJ/token/head
- throughput: 65 ns attention latency
- accuracy: avg acc 43.02 (public GPT-2) vs hardware models comparable; Table 1
- bits_weight: 3b stored K/V
- bits_adc: ADC-free; 5b (16-level counter + sign) output, 4b PWM input

## Datasets / benchmarks
OpenWebText, ARC-Easy, ARC-Challenge, WinoGrande, HellaSwag, LAMBADA, PIQA, WikiText-2

## Limitations
- Simulation (SPICE-calibrated models, synthesized layout) only; no fabricated chip
- Savings compare an attention-only block with whole GPUs; headline numbers are inconsistent within the paper (abstract: 2 and 4 orders; intro: 2 and 5 orders; results: x100 and x70,000 vs H100)
- Model is co-designed (HardSigmoid instead of softmax, sliding window M=1024, 3-5 bit signals) and needs fine-tuning, not drop-in
- Only attention is analog; linear layers/FFN weights are not mapped to NVM crossbars
- Retention of CMOS gain cells is only 5 ms, requiring refresh/short windows; scaling beyond GPT-2-XL untested

## Remarks
A high-profile co-design addressing the dynamic KV cache that NVM crossbars handle badly (write energy and endurance). Charge-domain gain cells with ADC-free pulse chaining are plausible and the adaptation recipe is reusable for other nonlinear analog multipliers. It complements NVM-weight analog work (IBM PCM, ReRAM chips) which keeps attention digital, but the evidence is simulated and the GPU comparison is attention-only.

## Use in the original review
- F13 (Medium confidence): Charge-based analog gain cells targeting attention's KV-cache dot products project ~100× speedup and ~70,000× energy reduction versus an H100 (~6.1 nJ and ~65 ns per token per attention head). Circuit non-idealities — third-order polynomial nonlinearity, charge leakage, 4-bit queries / 3-bit stored K,V, HardSigmoid replacing softmax — make direct mapping of pre-trained weights impossible, so a hardware-aware adaptation step is mandatory; the authors mapped GPT-2 weights through a nonlinear gain-cell model rather than training from scratch.

## Cites (in collection, 8)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "IMC is particularly beneficial when using non-volatile memories to store stationary weights in linear layers22."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _contrasts/critiques_: "Non-volatile memories can be used for linear layers of transformers17, but are too slow, energy expensive and are not endurant enough for dynamical KV-cache writing18,22."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _contrasts/critiques_: "KV cache has been implemented either by dynamic random-access memories (DRAMs)21,23, which have limited parallelism requiring many digital sequential adders, or by SRAMs19,24, which are limited by their volatility and relatively low density25."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "To mitigate this issue, charge-based integration is an energy-efficient alternative35,36."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _contrasts/critiques_: "KV cache has been implemented either by dynamic random-access memories (DRAMs)21,23, which have limited parallelism requiring many digital sequential adders, or by SRAMs19,24, which are limited by their volatility and relatively low density25."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "To mitigate this issue, charge-based integration is an energy-efficient alternative35,36."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _contrasts/critiques_: "KV cache has been implemented either by dynamic random-access memories (DRAMs)21,23, which have limited parallelism requiring many digital sequential adders, or by SRAMs19,24, which are limited by their volatility and relatively low density25."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _background_: "In particular, to mitigate data-transfer overhead of weights loading, several approaches leverage either near-memory or in-memory computing (IMC)17–21."

## Cited by (in collection, 3)
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _background_: "Emerging alternatives such as gain-cell-based designs aim to improve density relative to SRAM while retaining the flexibility of reprogramming, but remain at an early stage of development and have not yet demonstrated large-scale AIMC systems [11]."
- [2026_Zheng_InterfaceKVQ_ICCAD](2026_Zheng_InterfaceKVQ_ICCAD.md) InterfaceKVQ (2026) — _contrasts/critiques_: "Leroux et al. [11] hold keys and values in volatile gain-cell arrays rewritten at every step over a fixed 1,024-token window, with 3-bit storage that requires retraining; X-Former [26] targets encoder-only models and has no decoding KV cache; HARDSEA [12] prescreens token relevance in analog ReRAM and computes the exact sparse attention in digital SRAMCiM, with 8-bit keys and values in volatile SRAM."
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Leroux_GainCellAnalogAttention_NatCompSci.pdf](../../11_Small_Language_Models_on_AIMC/2025_Leroux_GainCellAnalogAttention_NatCompSci.pdf)
- Full text: [../fulltext/2025_Leroux_GainCellAnalogAttention_NatCompSci.txt](../fulltext/2025_Leroux_GainCellAnalogAttention_NatCompSci.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s43588-025-00854-1
