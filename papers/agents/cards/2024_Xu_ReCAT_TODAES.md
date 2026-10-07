---
id: W4403546214
key: 2024_Xu_ReCAT_TODAES
title: "A Cascaded ReRAM-based Crossbar Architecture for Transformer Neural Network Acceleration"
short: "ReCAT"
year: 2024
venue: "TODAES"
venue_full: "ACM Transactions on Design Automation of Electronic Systems (2024)"
authors: "Jiahong Xu, Haikun Liu, Xiaoyang Peng, Zhuohui Duan, Xiaofei Liao, Hai Jin"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["Transformer", "BERT", "ViT"]
lm_models: ["BERT-base", "BART-base", "RoBERTa-base"]
param_scale: "~110M–140M"
slm: false
evidence: simulation
topics: ["transformer-accelerator", "attention", "crossbar-architecture", "adc-dac", "peripheral-circuits", "dataflow-pipelining", "analog-mvm", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 14
citations_overall: 6
priority_score: 5.59
doi: "https://doi.org/10.1145/3701034"
pdf: "../../04_Transformers_and_LLMs/2024_Xu_ReCAT_TODAES.pdf"
fulltext: "../fulltext/2024_Xu_ReCAT_TODAES.txt"
---

# ReCAT

**A Cascaded ReRAM-based Crossbar Architecture for Transformer Neural Network Acceleration** — ACM Transactions on Design Automation of Electronic Systems (2024) (2024)

## TL;DR
ReCAT cascades pairs of ReRAM crossbars with transimpedance amplifiers so attention intermediates (K^T, V) are written directly in the analog domain, plus ADC virtualization/sharing, giving 207.3x / 2.11x / 3.06x average speedup over GPU / ReBert / ReTransformer in simulation.

## Summary
Transformers need MatMuls on dynamically generated intermediates (Q, K, V), forcing slow ReRAM writes on the critical path, redundant ADC-then-DAC conversions, and idle ADCs while arrays are being programmed. ReCAT combines conventional crossbars (XB-A, ADC-attached) with cascaded pairs: an XB-T whose accumulated bitline currents are converted by a TIA (design from CASCADE) into write voltages for a buffer array XB-B, so intermediates are stored without AD/DA conversion and MVM overlaps with mapping. Wq is mapped to XB-A, Wk and Wv to XB-Ts; Q is digitised while K^T and V are written to XB-Bs. Signed operands are handled with offset-binary encoding in the first array and offset subtraction afterwards; 8-bit operands, 2-bit cells, 2-bit DACs with bit-slicing. An ADC virtualization scheme decouples ADCs from arrays and time-multiplexes them over a group of arrays so idle ADCs serve neighbours. Evaluation uses the MHSim instruction-driven simulator at 32 nm (TaOx/HfOx devices, NeuroSim device and circuit models, sigma=0.05 log-normal variation, 25 ns row/column write, 8-bit 1.25 GHz ADCs, 16 chips) on BERT-b, BART-b, RoBERTa-b (SQuAD v1), ViT-b-p16, DeiT-b, LeViT-384 (ImageNet-1k) against GPU (V100), a baseline, ReBert and ReTransformer. Attention nonlinearities (softmax, layer norm, activations) run in digital post-processing units.

## Language models evaluated
- Models: BERT-base, BART-base, RoBERTa-base
- Scale: ~110M–140M

## Contributions
- Cascaded crossbar pair with TIAs to write attention intermediates directly into ReRAM, hiding write latency and removing AD/DA conversions
- Offset-binary data mapping for signed operands in cascaded arrays
- ADC virtualization: time-division sharing of ADCs among a group of crossbars to raise ADC utilization
- Simulation-based comparison to GPU, ReBert, ReTransformer with ablations on cascading, ADC sharing and signed-mapping schemes

## Key claims (stable IDs)
- **2024_Xu_ReCAT_TODAES#C1** — ReCAT achieves 207.3x, 2.27x, 2.11x and 3.06x average speedup over GPU, Baseline, ReBert and ReTransformer — _support:_ average over six Transformer benchmarks — _loc:_ Sec. 4.3, Fig. 11
- **2024_Xu_ReCAT_TODAES#C2** — ReCAT cuts total energy by 27.72%, 24.51% and 31.47% vs Baseline, ReBert and ReTransformer — _support:_ energy normalized to ReCAT — _loc:_ Sec. 4.3, Fig. 12
- **2024_Xu_ReCAT_TODAES#C3** — Cascaded arrays alone give only 52% speedup over Baseline; combined with ADC sharing 2.27x — _support:_ ADC sharing alone also gives considerable gain; ADCs remain bottleneck — _loc:_ Sec. 4.4, Fig. 13
- **2024_Xu_ReCAT_TODAES#C4** — ReCAT loses only 1.15% accuracy vs the ReRAM Baseline (truncating low-order partial-sum bits), though all ReRAM designs lose ~10% on SQuAD models and 3.28-6.28% on image classification vs GPU — _support:_ sigma = 0.05 process variation, NeuroSim models — _loc:_ Sec. 4.3, Table 3
- **2024_Xu_ReCAT_TODAES#C5** — PRIME-style positive/negative array mapping underperforms the Baseline in ReCAT because it doubles array and MVM count — _support:_ offset-binary (ISAAC-style) mapping performs reasonably — _loc:_ Sec. 4.5, Fig. 14

## Results
- Average speedups 207.3x (GPU), 2.27x (Baseline), 2.11x (ReBert), 3.06x (ReTransformer) (Fig. 11)
- Energy: -27.72% vs Baseline, -24.51% vs ReBert, -31.47% vs ReTransformer (Fig. 12); but ~1.5x more write operations than mapping 8-bit digital operands, so lightweight models (LeViT-384) see little energy gain
- Accuracy: ~10% degradation on BERT-b/BART-b/RoBERTa-b (SQuAD) and 3.28-6.28% on ViT-b-p16/DeiT-b/LeViT-384 for all ReRAM designs; ReCAT only 1.15% worse than Baseline (Table 3)
- Per analog processing unit: 16 XB-A + 8 XB-T (64x64), 32 XB-B, 16 8-bit ADCs (30.4 mW), 2-bit DACs (Table 1)

## Key numbers
- tech_node: 32nm
- array_size: 64x64
- energy_eff: -24.51% to -31.47% energy vs ReBert/ReTransformer
- throughput: 207.3x vs GPU (V100)
- accuracy: 1.15% below ReRAM Baseline; ~10% below GPU on SQuAD models
- bits_weight: 8-bit operands, 2-bit cells
- bits_adc: 8-bit ADC, 2-bit DAC

## Datasets / benchmarks
SQuAD v1, ImageNet-1k

## Limitations
- Simulation only (MHSim, NeuroSim); no fabricated chip or measured TIA cascade
- Large accuracy drops (~10% on SQuAD) under the modelled ReRAM non-idealities, with no noise-aware training
- Small 64x64 arrays and 8-bit operands; encoder Transformers only, no autoregressive LLM / KV-cache
- Analog signal integrity across cascaded TIA stages (noise/offset accumulation) is only modelled via device variation sigma=0.05
- Extra partial sums raise ReRAM write energy; limited gain for small models

## Remarks
A clear architectural idea for the attention dynamic-matmul problem: keep intermediates analog and overlap writes with MVMs, avoiding the CMOS-offload of ATT/X-Former. Evidence is purely simulated and the accuracy table shows substantial degradation, so the practicality of analog-to-analog cascading with real device noise is unproven. Relevant to LM mapping because KV-cache-like dynamic operands remain the hard part for ReRAM (endurance and write energy are not analysed here).

## Cites (in collection, 14)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Two data mapping schemes proposed in ISAAC [35] and PRIME [6, 35] are commonly used in many ReRAM-based PIM architectures [1, 12, 37, 53]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _extends/builds-on_: "CASCADE [8] exploits TIAs to convert accumulated currents into write voltages, which then are applied to cascaded buffer arrays for multiply-and-add operations."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _uses-method-or-tool_: "We use the parameters of analog input buffers and analog adders according to TIMELY [27], and adopt the TIA design in CASCADE [8] to cascade crossbar arrays."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _baseline/comparison_: "For example, ReTransformer [50] tries to reduce the number of write operations and overlap the write latency with other ongoing analog MVMs."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "We note that this architecture only incurs a minor modification to the connection between multiplexers and ADCs, while crossbar arrays and other periphery circuits remain the same as previous works [1, 31, 35, 53]."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _baseline/comparison_: "We evaluate the inference performance and the energy efficiency for different Transformer models, and compare ReCAT with two state-of-the-art ReRAM-based PIM architectures designed for Transformer networks–ReTransformer [50] and ReBert [23]."
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022) — _contrasts/critiques_: "Yang et al. [48] use analog signal memory and analog multiply-add circuits to eliminate ReRAM write operations for intermediate results."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "Two data mapping schemes proposed in ISAAC [35] and PRIME [6, 35] are commonly used in many ReRAM-based PIM architectures [1, 12, 37, 53]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "A few proposals use double (i.e., positive/negative) crossbar arrays [6, 8] to process signed operands."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _contrasts/critiques_: "Similar to ATT [16], X-Former [39] also employs dedicated CMOS-based processing units with SRAM-based crossbar arrays to handle intermediate results of Transformers."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _background_: "CPSAA [26] further optimizes the computation model of ReTransformer and exploits ReRAM-based content addressable memory (ReCAM) to accelerate sparse MVMs."
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024) — _motivation_: "As the AD conversion is a performance bottleneck in ReRAM-based PIM architectures [13, 27, 35, 43], the ADC utilization has a significant impact on the performance and energy efficiency of ReRAMbased crossbar arrays [46]."
- [2020_Guo_ATT_ICCD](2020_Guo_ATT_ICCD.md) ATT (2020) — _contrasts/critiques_: "ATT [16] customizes matrix-matrix multiplication circuits for these matrix multiplications in the digital domain to avoid writing K and V to ReRAM."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)

## Files
- PDF: [../../04_Transformers_and_LLMs/2024_Xu_ReCAT_TODAES.pdf](../../04_Transformers_and_LLMs/2024_Xu_ReCAT_TODAES.pdf)
- Full text: [../fulltext/2024_Xu_ReCAT_TODAES.txt](../fulltext/2024_Xu_ReCAT_TODAES.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3701034
