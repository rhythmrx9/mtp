---
id: W4414198682
key: 2025_Xu_UniCAIM_DAC
title: "UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference"
short: "UniCAIM"
year: 2025
venue: "DAC"
venue_full: "ACM/IEEE Design Automation Conference (DAC), 2025"
authors: "Weikai Xu, Wenxuan Zeng, Qianqian Huang, Meng Li, Ru Huang"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["FeFET"]
models: ["GPT/LLM", "Transformer"]
lm_models: ["LongChat-v1.5-7B-32k", "Llama-2-7B (motivation, Fig. 1)"]
param_scale: "7B"
slm: true
evidence: algorithm+simulation
topics: ["kv-cache", "attention", "transformer-accelerator", "language-models", "pruning-sparsity", "adc-dac", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 4
citations_overall: 3
priority_score: 8.42
doi: "https://doi.org/10.1109/dac63849.2025.11133273"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Xu_UniCAIM_DAC.pdf"
fulltext: "../fulltext/2025_Xu_UniCAIM_DAC.txt"
---

# UniCAIM

**UniCAIM: A Unified CAM/CIM Architecture with Static-Dynamic KV Cache Pruning for Efficient Long-Context LLM Inference** — ACM/IEEE Design Automation Conference (DAC), 2025 (2025)

## TL;DR
FeFET-based unified CAM/CIM array performing O(1) dynamic top-k KV-cache selection, charge-domain static eviction and current-domain exact attention, cutting area-energy-delay product 8.2-831x vs Sprint/TranCIM/CIMFormer (HSPICE) with LongChat-7B accuracy near dense attention.

## Summary
Long-context LLM inference is limited by KV-cache size and attention latency (Fig. 1, Llama-2-7B), and existing CIM accelerators support either fixed-pattern static pruning (TranCIM) or dynamic pruning needing costly top-k hardware (CIMFormer, Sprint). The paper proposes a hybrid pruning algorithm: one-shot static eviction at prefill by accumulated attention score (H=512 heavy tokens kept), then at each decode step dynamic top-k selection by q.K^T similarity plus eviction of the lowest-accumulated-score token to keep a fixed KV cache (M=64 reserved entries). Hardware is a FeFET array storing the key cache (signed multi-bit, up to 3-bit cells using multilevel Vth) with three modes: CAM mode for approximate similarity and O(1) top-k via a single search-line charge/discharge without ADCs, charge-domain CIM mode to accumulate scores for static eviction, and current-domain CIM mode for exact attention on selected tokens using 64 parallel 10-bit SAR ADCs. Circuit evaluation uses HSPICE with 45 nm BSIM MOSFETs and a Preisach FeFET model, cache of 576 tokens, d=128. Application accuracy is evaluated on LongChat-v1.5-7B-32k with LongBench HotpotQA (1.5k prompt) and NarrativeQA (2.5k prompt) against SnapKV and StreamingLLM.

## Language models evaluated
- Models: LongChat-v1.5-7B-32k, Llama-2-7B (motivation, Fig. 1)
- Scale: 7B
- Note: FeFET unified CAM/CIM macro for KV-cache pruning and attention in long-context LLMs; accuracy evaluated on LongChat-v1.5-7B-32k (7B). Weights not in CIM; only the KV cache attention is in-memory (CAM approximate similarity, charge-domain accumulation, current-domain exact attention). Circuit-level simulation.

## Contributions
- Hardware-friendly hybrid static-dynamic KV cache pruning framework (prefill one-shot eviction, decode top-k plus eviction at fixed cache size)
- UniCAIM unified CAM/CIM architecture with CAM, charge-domain CIM and current-domain CIM modes
- FeFET CAM/CIM cell exploiting multilevel Vth for signed multi-bit KV storage and in-place attention
- Circuit- and application-level evaluation showing 8.2-831x AEDP reduction with accuracy comparable to dense attention

## Key claims (stable IDs)
- **2025_Xu_UniCAIM_DAC#C1** — UniCAIM reduces AEDP by 8.2-831x vs state-of-the-art CIM LLM accelerators — _support:_ 1-bit cell: 8.2x/13.9x/124x (50% pruning) and 11.5x/19x/277x (80%) vs Sprint/TranCIM/CIMFormer; 3-bit cell: 24.8x/41.7x/372x and 34.6x/56.9x/831x — _loc:_ Sec. IV-A.4, Table II
- **2025_Xu_UniCAIM_DAC#C2** — CAM-based top-k selection is O(1) and ADC-free for pruning — _support:_ Latency speedup 4.2x to 16.7x and energy improvement 5.3x to 27x as sequence length increases — _loc:_ Sec. IV-A.2-3, Fig. 11-12
- **2025_Xu_UniCAIM_DAC#C3** — Static-dynamic pruning keeps accuracy close to full-cache attention and beats SnapKV and StreamingLLM — _support:_ LongChat-v1.5-7B-32k F1 on HotpotQA and NarrativeQA at low KV cache ratios — _loc:_ Sec. IV-B, Fig. 13
- **2025_Xu_UniCAIM_DAC#C4** — Area efficiency improves up to ~15x and dynamic pruning circuit adds little area — _support:_ improvement drops only from 15x to 14.7x — _loc:_ Sec. IV-A.1, Fig. 10

## Results
- AEDP reduction 8.2x-831x vs Sprint, TranCIM, CIMFormer at equal pruning ratios (50% and 80%)
- Energy-efficiency gain grows from 5.3x to 27x and speedup from 4.2x to 16.7x with sequence length
- Area efficiency gain ~15x (14.7x with CAM pruning circuit)
- Accuracy on LongBench HotpotQA/NarrativeQA comparable with full KV cache and above SnapKV/StreamingLLM (Fig. 13; numeric values only in figure)

## Key numbers
- tech_node: 45nm BSIM (HSPICE)
- array_size: 576 tokens x 128 dims
- energy_eff: 5.3x-27x improvement
- throughput: 4.2x-16.7x speedup
- accuracy: comparable to dense attention on LongChat-7B (LongBench)
- bits_weight: 1-3b FeFET cell
- bits_adc: 10-bit SAR (64 parallel)

## Datasets / benchmarks
LongBench HotpotQA, LongBench NarrativeQA

## Limitations
- Circuit-level HSPICE simulation only; no fabricated chip
- Accuracy evaluation is algorithmic (pruning policy) and does not inject FeFET variation, noise or ADC quantization effects
- Only attention/KV cache is mapped to FeFET; weight GEMMs (projections, FFN) not addressed
- Large AEDP gains partly depend on baseline choice and equalized pruning ratios
- Cache of only 576 tokens, d=128 per head studied in circuit evaluation

## Remarks
A cogent KV-cache-in-NVM design relevant to long-context SLM deployment, where the dynamic key/value matrices are the hard part for crossbars because writes are frequent; FeFET's low write energy is exploited. It differs from weight-stationary analog work in the collection by targeting attention with CAM search. Robustness under device noise is untested, so evidence for analog viability is limited.

## Cites (in collection, 4)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "In recent years, various emerging NVMs, such as resistive random-access memory (RRAM), magnetic tunnel junction (MTJ) and FeFET, have triggered lots of attention for CIM, due to the high storage density and efficient GEMV operation via analog computing within the memory array [26-28]."
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023) — _background_: "In recent years, various emerging NVMs, such as resistive random-access memory (RRAM), magnetic tunnel junction (MTJ) and FeFET, have triggered lots of attention for CIM, due to the high storage density and efficient GEMV operation via analog computing within the memory array [26-28]."
- [2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC](2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.md) Reconfigurable Sparse-Attention NVPIM (2023) — _contrasts/critiques_: "Besides, there are emerging non-volatile memories (NVMs)-based CIM designs for dynamic pruning by utilizing approximate attention scores [17, 18], but suffering the trade-off between energy efficiency and accuracy."
- [2023_Lu_RIME_TVLSI](2023_Lu_RIME_TVLSI.md) RIME (2023) — _background_: "Meanwhile, from the hardware perspective, the computing-in-memory (CIM) architecture which can perform the general matrix-vector multiplication (GEMV) operations within the memory array, has been proven to compute attention efficiently by reducing the data movement [9-12]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Xu_UniCAIM_DAC.pdf](../../11_Small_Language_Models_on_AIMC/2025_Xu_UniCAIM_DAC.pdf)
- Full text: [../fulltext/2025_Xu_UniCAIM_DAC.txt](../fulltext/2025_Xu_UniCAIM_DAC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/dac63849.2025.11133273
