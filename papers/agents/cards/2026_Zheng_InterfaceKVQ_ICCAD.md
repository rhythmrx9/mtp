---
id: W7212031114
key: 2026_Zheng_InterfaceKVQ_ICCAD
title: "Interface-Aware KV Cache Quantization for Dense On-Chip NVM in Long-Context LLM Decoding"
short: "InterfaceKVQ"
year: 2026
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2026), accepted; arXiv 2609.05764"
authors: "Jiahao Zheng, Yifan Qin, Xiaobo Sharon Hu, Yiyu Shi"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["GPT/LLM", "Transformer"]
lm_models: ["Llama-3.2-3B", "Llama-3.1-8B", "Qwen2.5-14B"]
param_scale: "3B-14B"
slm: true
evidence: algorithm+simulation
topics: ["kv-cache", "quantization", "language-models", "attention", "3d-integration", "read-write-noise", "energy-efficiency", "heterogeneous-analog-digital"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 6
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.48550/arxiv.2609.05764"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Zheng_InterfaceKVQ_ICCAD.pdf"
fulltext: "../fulltext/2026_Zheng_InterfaceKVQ_ICCAD.txt"
---

# InterfaceKVQ

**Interface-Aware KV Cache Quantization for Dense On-Chip NVM in Long-Context LLM Decoding** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2026), accepted; arXiv 2609.05764 (2026)

## TL;DR
A randomized-Hadamard-rotation plus shared-codebook 4-bit KV quantizer matched to fixed-range NVM read converters gives 3.1-3.6x lower modeled KV read energy and 8x less metadata than KIVI/KVQuant on the same NVM, but is less accurate than both in software.

## Summary
Long-context LLM decoding is bound by KV-cache bandwidth; the paper asks what KV quantization suits a KV cache held in dense on-chip NVM (RRAM) behind fixed-range converters. KIVI's per-group scale/zero-point metadata adds ~25% storage and KVQuant's sparse fp outliers cannot live in a dense array. The proposed scheme applies a fixed randomized Hadamard rotation (mapped on one static, write-once analog crossbar with differential column pairs) and per-vector normalization so every coordinate has the same range; one 16-level codebook for keys (data-free analytic) and one for values (single offline calibration over 64 sequences) is shared across all tokens, and codebook thresholds are programmed as the read converter's reference levels. Dequantization is a 16-entry LUT plus one norm multiply; attention stays in digital logic. Evaluation: Llama-3.2-3B, Llama-3.1-8B, Qwen2.5-14B on a QuaRot W8A8 backbone with 2% weight noise, ARC-c, WikiText PPL, RULER, LongBench, SAMSum, with storage noise on KV cells and device noise on the rotation crossbar; energy/area from a NeuroSim-based 22nm analytic model.

## Language models evaluated
- Models: Llama-3.2-3B, Llama-3.1-8B, Qwen2.5-14B
- Scale: 3B-14B
- Note: 4-bit KV cache for Llama-3.2-3B, Llama-3.1-8B, Qwen2.5-14B stored in dense on-chip NVM (RRAM-class); one small static analog crossbar does a fixed random rotation; attention stays digital. NVM is mainly storage with noisy reads; analog compute is only the rotation.

## Contributions
- Identifies mismatch between GPU-oriented KV quantizers (KIVI, KVQuant) and dense NVM KV storage and quantifies it (up to 25% capacity, 3.1-3.6x read energy)
- Interface-matched scheme: shared fixed codebooks whose thresholds are converter reference levels, one norm scalar per vector as only metadata
- Static write-once analog rotation crossbar as only analog compute; attention in digital
- Evaluation on 3B-14B models under simulated storage and crossbar noise with candid accuracy-gap reporting

## Key claims (stable IDs)
- **2026_Zheng_InterfaceKVQ_ICCAD#C1** — Proposed format cuts KV metadata ~8x vs KIVI and modeled KV read energy 3.1-3.6x vs KIVI/KVQuant on the same NVM — _support:_ Metadata 3.1% vs 25% (KIVI) vs 7.1% (KVQuant); read energy 1.00x vs 3.64x vs 3.11x — _loc:_ Sec. 4.3 / Table 3
- **2026_Zheng_InterfaceKVQ_ICCAD#C2** — Accuracy is below KIVI and KVQuant at equal bit-width — _support:_ RULER multi-value 98.1 (8B) vs 100 KIVI; 94.9 vs 98.5 (14B); 80.4 vs 89.0 (3B) — _loc:_ Sec. 4.2 / Table 2
- **2026_Zheng_InterfaceKVQ_ICCAD#C3** — Static rotation crossbar adds no measurable accuracy cost under 2% conductance noise, 6-bit DAC, 2% accumulation noise — _support:_ ARC 3B 43.3->43.1, 8B 52.4->53.1, 14B 69.1->68.5 — _loc:_ Sec. 4.5 / Fig. 4
- **2026_Zheng_InterfaceKVQ_ICCAD#C4** — KV retrieval stays flat up to 3% storage noise and drops sharply at 5% — _support:_ Fig. 3 noise sweep — _loc:_ Sec. 4.4 / Fig. 3
- **2026_Zheng_InterfaceKVQ_ICCAD#C5** — Removing KVQuant's outliers to fit a dense array collapses retrieval — _support:_ RULER-MV 96.5->81.2 (14B), 86.5->58.0 (3B) — _loc:_ Sec. 4.3

## Results
- 4-bit KV is 3.88x smaller than fp16: 28.9 KB/token vs 112 KB; 242 MB vs 939 MB at 8k on 3B (Table 4)
- On-chip KV area at 8k: 62 mm2 vs 140 mm2 fp16; read energy/step 0.041 mJ vs 0.16 mJ
- KV area at 8k: 62/71/107 mm2 (3B/8B/14B); at 32k 250/285/428 mm2, exceeding a single die
- Read energy: ~4x from quantization and ~320x from on-chip vs off-chip (7 pJ/bit); CiM-specific rotation <1% of read energy
- Single cell write ~3.3 pJ; one write per KV cell per session, far below 1e6-1e9 RRAM endurance
- Fully data-free codebook collapses at larger sizes (PPL 21 on 8B, 53 on 14B); hybrid codebook fixes it
- Real tasks track backbone: only 8B LongBench drops >2 points (-4.2 F1); SAMSum within 1.6 ROUGE-L

## Key numbers
- tech_node: 22nm (NeuroSim model)
- array_size: d=128 rotation crossbar
- energy_eff: KV read energy 0.041 mJ/step (3B, 8k) ; 3.1-3.6x lower than KIVI/KVQuant
- accuracy: RULER-MV 98.1 (8B), 94.9 (14B), 80.4 (3B)
- bits_weight: 4b KV; W8A8 backbone
- bits_adc: 4b-equivalent sense-amp comparator readout; 6b input DAC

## Datasets / benchmarks
ARC-Challenge, WikiText, RULER, needle-in-a-haystack, LongBench, SAMSum

## Limitations
- Accuracy below KIVI/KVQuant even at matched storage budget
- Energy/area from an analytic NeuroSim-based 22nm model, not full-system or silicon
- Norm scalars must reside in noise-free digital SRAM (26 mm2 at 8k on 3B)
- 32k context exceeds single-die area; needs multi-die/3D
- Analog compute is only the fixed rotation; attention is digital, so little 'analog MVM' for LMs
- Noise axes (storage vs crossbar) never combined

## Remarks
A candid co-design paper: it does not claim accuracy gains and honestly attributes most energy savings to compression and on-chip residence rather than CiM. Relevant to the collection as the NVM-resident KV cache counterpart to gain-cell attention (Leroux) and HARDSEA/X-Former. Evidence is simulation with analytic cost; the 3-14B scale makes it directly SLM-relevant.

## Cites (in collection, 6)
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _contrasts/critiques_: "Leroux et al. [11] hold keys and values in volatile gain-cell arrays rewritten at every step over a fixed 1,024-token window, with 3-bit storage that requires retraining; X-Former [26] targets encoder-only models and has no decoding KV cache; HARDSEA [12] prescreens token relevance in analog ReRAM and computes the exact sparse attention in digital SRAMCiM, with 8-bit keys and values in volatile SRAM."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _contrasts/critiques_: "HARDSEA [12] prescreens token relevance in analog ReRAM and computes the exact sparse attention in digital SRAMCiM, with 8-bit keys and values in volatile SRAM."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "Hardware energy and area are computed with a NeuroSim-based model [17] at 22nm; per-component constants appear in Section 4.3, with only the DAC constants as negligible literature placeholders."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Accelerators built on NVM, often referred to as nonvolatile CiM (NVCiM) [19, 22, 34], have demonstrated large density and energy advantages for matrix-heavy inference [17, 20, 24]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _motivation_: "Prior work questions whether NVM suits data updated during decoding [11, 26], so we quantify the write cost."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "A compute-in-memory (CiM) accelerator performs the multiplyaccumulate inside the memory array: weights are cell conductances in a crossbar, inputs drive the rows as voltages, and each column’s accumulated current yields one dot product in the analog domain [29]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Zheng_InterfaceKVQ_ICCAD.pdf](../../11_Small_Language_Models_on_AIMC/2026_Zheng_InterfaceKVQ_ICCAD.pdf)
- Full text: [../fulltext/2026_Zheng_InterfaceKVQ_ICCAD.txt](../fulltext/2026_Zheng_InterfaceKVQ_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.48550/arxiv.2609.05764
