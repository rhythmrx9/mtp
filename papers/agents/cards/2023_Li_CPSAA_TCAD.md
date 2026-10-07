---
id: W4390241252
key: 2023_Li_CPSAA_TCAD
title: "CPSAA: Accelerating Sparse Attention Using Crossbar-Based Processing-In-Memory Architecture"
short: "CPSAA"
year: 2023
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Huize Li, Hai Jin, Long Zheng, Xiaofei Liao, Yu Huang, Cong Liu, Jiahong Xu, Zhuohui Duan, Dan Chen, Chuangyi Gui"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer", "BERT", "GPT/LLM"]
lm_models: ["BERT-Base", "GPT-2 (12 decoders)", "BART"]
param_scale: "~110M-140M (BERT-base, GPT-2 small, BART-base)"
slm: true
evidence: simulation
topics: ["attention", "transformer-accelerator", "pruning-sparsity", "crossbar-architecture", "dataflow-pipelining", "energy-efficiency", "language-models", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 7
cites_in_collection: 3
citations_overall: 17
priority_score: 10.08
doi: "https://doi.org/10.1109/tcad.2023.3344524"
pdf: "../../04_Transformers_and_LLMs/2023_Li_CPSAA_TCAD.pdf"
fulltext: "../fulltext/2023_Li_CPSAA_TCAD.txt"
---

# CPSAA

**CPSAA: Accelerating Sparse Attention Using Crossbar-Based Processing-In-Memory Architecture** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023)

## TL;DR
CPSAA is a ReRAM-crossbar PIM sparse-attention accelerator that hides crossbar write latency, prunes in-memory, and runs SDDMM/SpMM by coupling ReRAM and ReCAM arrays, reporting 89.6x/32.2x/17.8x/3.39x/3.84x speedup and 755.6x/55.3x/21.3x/5.7x/4.9x energy savings over GPU/FPGA/SANGER/ReBERT/ReTransformer.

## Summary
Sparse attention cuts unnecessary token-pair computation, but unstructured sparsity and the separate pruning phase cause heavy off-chip random access (up to 60% of latency per Sec. II-D), and existing ReRAM attention accelerators (ReBERT, ReTransformer) neither handle sparsity nor hide the cost of writing runtime-generated matrices (K, V, X^T) into crossbars. CPSAA reformulates attention so that M = X*W_S (with W_S = W_Q*W_K^T precomputed) and V = X*W_V can be computed in parallel while X^T is being written, hiding write latency without losing VMM parallelism. A PIM-based pruning unit computes a low-precision (quantized) approximate score matrix on crossbars and binarizes it with a threshold to a mask, avoiding off-chip transfers, and runs in parallel with the attention calculation. Unstructured sparsity is exploited by storing the mask in two 512x512 ReCAM arrays that act as a scheduler generating control signals for ReRAM VMMs (SDDMM and SpMM). Static weights live in read-only arrays (ROA) and runtime matrices in write-enable arrays (WEA); weights are 32-bit fixed point (exponent extracted per array) processed by 32x32 crossbars with 2-bit DACs and a 1 GS/s 8-bit ADC per array group. A cycle-accurate Python simulator (64 tiles, each 11 ROA + 56 WEA, 32nm TaOx ReRAM, SPICE/CACTI for area-power) is compared on BERT-Base, GPT-2 and BART over GLUE and SQuAD v2.0.

## Language models evaluated
- Models: BERT-Base, GPT-2 (12 decoders), BART
- Scale: ~110M-140M (BERT-base, GPT-2 small, BART-base)

## Contributions
- Attention calculation mode that overlaps crossbar writes with VMM computation to hide ReRAM write overhead
- PIM-based sparsity pruning architecture (quantized score + binarization) that removes off-chip transfers and overlaps with attention
- ReRAM-based SDDMM and SpMM methods for unstructured sparsity by coupling ReRAM and ReCAM (scheduler) arrays
- Evaluation against GPU, FPGA, ASIC (SANGER) and ReRAM PIM (ReBERT, ReTransformer) baselines

## Key claims (stable IDs)
- **2023_Li_CPSAA_TCAD#C1** — CPSAA achieves 89.6x, 32.2x, 17.8x, 3.39x and 3.84x average performance over GPU, FPGA, SANGER, ReBERT, ReTransformer — _support:_ CPSAA avg 9142 GOPS vs GPU 102, FPGA 284, SANGER 513, ReBERT 2696, ReTransformer 2381 GOPS (BERT) — _loc:_ Sec. VI-A, Fig. 12
- **2023_Li_CPSAA_TCAD#C2** — Energy savings of 755.6x, 55.3x, 21.3x, 5.7x, 4.9x over the same baselines — _support:_ 476 GOPS/W vs 0.63 (GPU), 8.6 (FPGA), 22.4 (SANGER), 83.7 (ReBERT), 97.1 (ReTransformer) — _loc:_ Sec. VI-A, Fig. 13
- **2023_Li_CPSAA_TCAD#C3** — The new calculation mode alone (dense CPDAA) beats ReBERT/ReTransformer — _support:_ ReBERT 1.31x and ReTransformer 1.64x execution time vs CPDAA; 1.30x/1.21x energy — _loc:_ Sec. VI-B, Fig. 14-15
- **2023_Li_CPSAA_TCAD#C4** — Write endurance is not a limiting factor — _support:_ with 10^12 endurance and ~10^4 writes per long document, ~10^8 inferences — _loc:_ Sec. V Methodology

## Results
- Average throughput 9142 GOPS, 476 GOPS/W on BERT workload (GLUE+SQuAD v2.0)
- Speedups over GPU/FPGA/SANGER/ReBERT/ReTransformer: 89.6x/32.2x/17.8x/3.39x/3.84x; energy: 755.6x/55.3x/21.3x/5.7x/4.9x
- Speedups across BERT, GPT-2, BART vary by ~10%
- Config: 64 tiles, 32x32 crossbars, 533 MHz, 25 ns cycle (ISAAC-style), SET/RESET 1.52/2.11 ns SLC

## Key numbers
- tech_node: 32nm
- array_size: 32x32 ReRAM crossbars; 512x512 ReCAM
- energy_eff: 476 GOPS/W
- throughput: 9142 GOPS
- bits_weight: 32-bit fixed point (SLC cells)
- bits_adc: 8b 1.0 GS/s ADC; 2b DAC

## Datasets / benchmarks
GLUE (CoLA, SST-2, MRPC, STS-B, QQP, MNLI, WNLI, RTE), SQuAD v2.0

## Limitations
- Pure simulation (Python cycle-accurate simulator plus SPICE/CACTI-derived parameters); no fabrication
- No analog non-idealities (noise, drift, IR-drop, variation) or accuracy-under-noise evaluation; weights are 32-bit fixed point so ReRAM precision is idealized
- Single-level cell with 32-bit fixed point implies many bit-sliced crossbars, area not discussed in detail
- ADC/peripheral numbers inherited from ISAAC-style assumptions
- Fixed d_model=512, d_K=64 and 320-embedding batches; small models only

## Remarks
A well-argued architecture paper on handling runtime-written matrices (K, V) and dynamic unstructured sparsity in crossbars, the main obstacles for attention on NVM. Results are simulation-only with idealized 32-bit precision, so they should be read as architectural upper bounds, and nothing indicates how attention accuracy behaves with real analog noise. Complements noise-focused work in the collection (e.g., NORA, ClipFormer) by addressing latency/energy of dynamic attention rather than accuracy.

## Cites (in collection, 3)
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _contrasts/critiques_: "Direct application of current ReRAM-based sparse methods [17, 28] to ReRAM-based SDDMM and SpMM operations will achieve inferior performance (for details to see § IV-C and § IV-D)."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _baseline/comparison_: "These solutions use high parallel ReRAM arrays to significantly reduce the latency of DDMM operations [11, 36]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "As configured in ISAAC [27], the “cycle” in CPSAA means the time of ADC processing 32 column signals, i.e., 25ns."

## Cited by (in collection, 7)
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _background_: "CPSAA [26] further optimizes the computation model of ReTransformer and exploits ReRAM-based content addressable memory (ReCAM) to accelerate sparse MVMs."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _motivation_: "Though NVM cells could be reprogrammed, the programming of NVM devices is too expensive [17], [34]."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _contrasts/critiques_: "Though prior works have shown IMC/NMC-based systems for LLM acceleration, most only support model-specific dataflow with custom architectural design [5], [6], [7], falling short in terms of system and dataflow flexibility to diverse models."
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _background_: "Some studies [15– 18] explore eNVM-friendly data access through techniques like matrix decomposition or fine-grained dataflow designs to accelerate the VMM primitive in attention computation."
- [2025_Huang_VQTCiM_DAC](2025_Huang_VQTCiM_DAC.md) VQT-CiM (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Rhe_ETA_APCCAS](2025_Rhe_ETA_APCCAS.md) ETA (2025)

## Files
- PDF: [../../04_Transformers_and_LLMs/2023_Li_CPSAA_TCAD.pdf](../../04_Transformers_and_LLMs/2023_Li_CPSAA_TCAD.pdf)
- Full text: [../fulltext/2023_Li_CPSAA_TCAD.txt](../fulltext/2023_Li_CPSAA_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2023.3344524
