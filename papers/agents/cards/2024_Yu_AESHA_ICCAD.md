---
id: W4409285593
key: 2024_Yu_AESHA_ICCAD
title: "AESHA: Accelerating Eigen-decomposition-based Sparse Transformer with Hybrid RRAM-SRAM Architecture"
short: "AESHA"
year: 2024
venue: "ICCAD"
venue_full: "Proceedings of the 43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024)"
authors: "Xuliang Yu, Tianwei Ni, Xinsong Sheng, Yun Pan, Lei He, Liang Zhao"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM", "SRAM-digital"]
models: ["Transformer", "BERT", "ViT"]
lm_models: ["BERT-Base", "BERT-Large", "BigBird", "Sanger"]
param_scale: "110M-340M"
slm: true
evidence: simulation
topics: ["transformer-accelerator", "attention", "heterogeneous-analog-digital", "pruning-sparsity", "dataflow-pipelining", "endurance-retention", "language-models", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 8
citations_overall: 5
priority_score: 8.45
doi: "https://doi.org/10.1145/3676536.3676660"
pdf: "../../04_Transformers_and_LLMs/2024_Yu_AESHA_ICCAD.pdf"
fulltext: "../fulltext/2024_Yu_AESHA_ICCAD.txt"
---

# AESHA

**AESHA: Accelerating Eigen-decomposition-based Sparse Transformer with Hybrid RRAM-SRAM Architecture** — Proceedings of the 43rd IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2024) (2024)

## TL;DR
AESHA rewrites attention via eigen-decomposition of W_Q W_K^T so static RRAM crossbars do sparse feature transformation and an SRAM systolic array reconstructs attention, eliminating runtime RRAM writes and giving 2.5-2.69x (BERT) and 3.07-7.84x (ViT) weight compression and 3.72x better energy efficiency than ReBERT.

## Summary
Prior RRAM-CIM transformer accelerators (ReBERT, ReTransformer, CPSAA) accelerate VMM for Q/K/V but store large dynamic intermediates in RRAM, ignoring endurance limits. AESHA uses the symmetric/skew-symmetric structure of W_Q W_K^T to eigen-decompose it, turning attention into an orthogonal feature transformation (static weights, mapped to analog weight-stationary RRAM-CIM) plus outer-product-based attention reconstruction (dynamic, done in digital output-stationary SRAM-CIM with a fine-grained systolic array). An adaptive energy-distribution threshold-based structured pruning keeps principal eigen-features per head, reducing static weight and activation footprint, and a fused softmax engine with mask-guided recomputation (4th-order Taylor exponential) handles the nonlinearity. Evaluation: BERT-Base/Large, BigBird and Sanger on 8 GLUE tasks (sequence length 128) and ViT-Base/Large on CIFAR-10/100 and ImageNet-1K, fine-tuned in PyTorch with pruning threshold tau_unit=0.1; hardware is modelled in NeuroSim at 32 nm (RRAM 4-bit cells; SRAM-CIM), the sense-amplifier-based unit verified in Virtuoso, digital logic synthesised at 28 nm, with CPU/GPU baselines measured by PyRAPL and nvidia-smi. Four pipeline variants (AESHA-WS, OS, PW, PO) are compared.

## Language models evaluated
- Models: BERT-Base, BERT-Large, BigBird, Sanger
- Scale: 110M-340M

## Contributions
- Eigen-decomposition attention pipeline that converts dynamic attention into static orthogonal feature transformation plus outer-product reconstruction
- Adaptive energy-distribution threshold structured pruning of feature spaces at head granularity
- Heterogeneous CIM design: analog WS RRAM for transformation, digital OS SRAM-CIM systolic array for reconstruction
- No runtime RRAM write accesses, avoiding endurance limits
- Ablations on pruning threshold and systolic-array granularity

## Key claims (stable IDs)
- **2024_Yu_AESHA_ICCAD#C1** — Static RRAM footprint reduced 2.59x, 2.69x, 2.62x, 2.58x, 3.08x, 7.84x for BERT-Base, BERT-Large, BigBird, Sanger, ViT-Base, ViT-Large — _support:_ vs vanilla computation stack — _loc:_ Abstract, Fig. 7
- **2024_Yu_AESHA_ICCAD#C2** — Single attention layer speedups of 3170.0x, 95.6x, 4.1x, 19.0x, 19.2x over CPU, GPU, ReBERT, ReTransformer, CPSAA — _support:_ AESHA-PO — _loc:_ Sec. 5, Fig. 9
- **2024_Yu_AESHA_ICCAD#C3** — Attention-layer energy reduction of 336.0Kx, 12.6Kx, 7.3x, 23.1x, 25.8x over CPU, GPU, ReBERT, ReTransformer, CPSAA — _support:_ AESHA-PO — _loc:_ Sec. 5, Fig. 9
- **2024_Yu_AESHA_ICCAD#C4** — End-to-end 31.24% higher throughput and 3.72x better energy efficiency than ReBERT — _support:_ AESHA-PO; also 21.53x/22.72x/1.97x vs ReTransformer/CPSAA/AESHA-PW — _loc:_ Table 3, Conclusion
- **2024_Yu_AESHA_ICCAD#C5** — BERT-Base is sensitive to aggressive pruning while BERT-Large and ViTs are more robust — _support:_ At threshold 0.6, BERT-Base drops 0.8%-30.2%, BERT-Large 0.53%-7.25%, ViTs 1.14%-9.55% — _loc:_ Sec. 5.2, Fig. 7(a)

## Results
- Weight compression 2.5-2.69x on BERTs and 3.07-7.84x on ViTs with minimal accuracy degradation (Conclusion)
- AESHA-PO attention-layer speedup 4.1x over ReBERT, 19.0x over ReTransformer, 19.2x over CPSAA
- AESHA-PO energy reduction on attention 7.3x vs ReBERT, 23.1x vs ReTransformer, 25.8x vs CPSAA; 8.74-9.36% more than AESHA-PW on BERT-Base and 22.18-23.45% on BERT-Large
- Fine-grained 32x32 systolic granularity: ViT 3.49x energy-efficiency and 3.70x throughput improvement (Sec. 5.3)
- Table 3 throughput (GOPS): ReBERT ~128-135 (ViT-B/L, BERT-B/L), ReTransformer 44-122; energy efficiency ReBERT 0.90-0.96 TOPS/W, ReTransformer 0.17-0.24 TOPS/W

## Key numbers
- tech_node: 32nm (NeuroSim RRAM/SRAM CIM); 28nm digital synthesis
- array_size: 32x32 systolic granularity (best)
- energy_eff: 3.72x vs ReBERT; ~0.96 TOPS/W ReBERT baseline
- throughput: 31.24% higher than ReBERT (end-to-end)
- accuracy: minimal degradation at tau_unit=0.1
- bits_weight: 4-bit RRAM cells

## Datasets / benchmarks
GLUE (MNLI, QNLI, QQP, SST-2, STS-B, RTE, CoLA, MRPC), CIFAR-10, CIFAR-100, ImageNet-1K

## Limitations
- Simulation only; RRAM analog non-idealities (noise, drift, ADC error) are not applied to accuracy evaluation
- Encoder-only models of at most 340M parameters (BERT-Large); no decoder-only LLMs, no KV cache
- Pruning requires fine-tuning and degrades BERT-Base noticeably at low thresholds
- Insufficient on-chip systolic cells for long sequences (noted for challenging datasets)
- SRAM systolic array adds area and holds dynamic data, so overall footprint and SRAM capacity matter for long contexts

## Remarks
A thoughtful algorithm-architecture co-design for the attention endurance problem: keep only static weights in RRAM and move dynamic data to SRAM, using linear algebra (eigen-decomposition of W_Q W_K^T) rather than hardware tricks. The weakness is the lack of analog-noise accuracy evaluation. It targets encoder models (BERT, ViT); its static/dynamic split mirrors the IMC/NMC split used in LLM-scale systems like JADE in the collection.

## Cites (in collection, 8)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "We simulate the RRAM-CIM and SRAM-CIM macros using the peripheral setups under 32nm node technology in NeuroSim [37]."
- [2020_Guo_ATT_ICCD](2020_Guo_ATT_ICCD.md) ATT (2020) — _background_: "Some studies [15– 18] explore eNVM-friendly data access through techniques like matrix decomposition or fine-grained dataflow designs to accelerate the VMM primitive in attention computation."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _contrasts/critiques_: "Some approaches [24, 25] reduce on-chip memory occupancy of partial feature vectors by confining attention windows or blocks. However, this comes at the sacrifice of the model’s accuracy."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _uses-method-or-tool_: "The read and write pulse times of the RRAM cells are taken from [38], whereas the on/off resistances of RRAM cells with the 4-bit cell precision [39] are extracted from [26]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _background_: "Some studies [15– 18] explore eNVM-friendly data access through techniques like matrix decomposition or fine-grained dataflow designs to accelerate the VMM primitive in attention computation."
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023) — _background_: "In addition to these approaches, some research [20–23] employs heterogeneous RRAM-SRAM CIM designs to balance low-precision prediction and exact computation workloads towards providing low-power and efficient solutions."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _contrasts/critiques_: "Alternative methods such as SPRINT [20] and HARDSEA [21] leverage dynamic sparse attention features to reduce ineffective computations."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _background_: "Some studies [15– 18] explore eNVM-friendly data access through techniques like matrix decomposition or fine-grained dataflow designs to accelerate the VMM primitive in attention computation."

## Cited by (in collection, 1)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../04_Transformers_and_LLMs/2024_Yu_AESHA_ICCAD.pdf](../../04_Transformers_and_LLMs/2024_Yu_AESHA_ICCAD.pdf)
- Full text: [../fulltext/2024_Yu_AESHA_ICCAD.txt](../fulltext/2024_Yu_AESHA_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3676536.3676660
