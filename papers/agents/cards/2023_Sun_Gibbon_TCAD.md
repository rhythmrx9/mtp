---
id: W4361857408
key: 2023_Sun_Gibbon_TCAD
title: "Gibbon: An Efficient Co-Exploration Framework of NN Model and Processing-In-Memory Architecture"
short: "Gibbon"
year: 2023
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023)"
authors: "Hanbo Sun, Zhenhua Zhu, Chenyu Wang, Xuefei Ning, Guohao Dai, Huazhong Yang, Yu Wang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM", "Memristor(generic)"]
models: ["CNN", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["nas-codesign", "simulator", "crossbar-architecture", "adc-dac", "quantization", "mixed-precision", "energy-efficiency", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 9
citations_overall: 12
priority_score: 6.21
doi: "https://doi.org/10.1109/tcad.2023.3262201"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2023_Sun_Gibbon_TCAD.pdf"
fulltext: "../fulltext/2023_Sun_Gibbon_TCAD.txt"
---

# Gibbon

**Gibbon: An Efficient Co-Exploration Framework of NN Model and Processing-In-Memory Architecture** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023) (2023)

## TL;DR
Gibbon co-searches NN topology/quantisation and memristor-PIM hardware (crossbar size, ADC/DAC bits, cell precision) with an evolutionary search with adaptive parameter priority (ESAPP) and an RNN predictor, finding better designs in ~6 GPU hours (9.8-48.2x faster), with up to 15.3% higher accuracy and 5.96x lower EDP than prior PIM-NAS.

## Summary
Joint NN/PIM search spaces are enormous (3.3e54 for the NN alone, 4.3e84 combined) and prior PIM-oriented NAS (NACIM, UAE, NAS4RRAM) uses typical odd-kernel search spaces with poor crossbar utilisation (NACIM 53.1%) and slow simulators (MNSIM/NeuroSim, about ten minutes per candidate; 3,000 candidates >21 days). Gibbon provides (i) a PIM-oriented search space with group convolutions, even-sized kernels and a PIM-friendly topology, plus per-layer weight/activation bit-widths and hardware parameters (crossbar size, DAC/ADC resolution, memristor precision 1- or 2-bit); (ii) ESAPP, which prioritises hyperparameters and searches in small sub-spaces first, evolving the population; (iii) a multi-level joint simulator in which an RNN-based predictor with a design-candidate embedder predicts PIM-based NN accuracy loss, area, power and latency from a one-shot supernet and MNSIM 2.0 training data (Kendall's Tau used to assess ranking). The hardware infrastructure is the Multi-Precision single-bit RRAM PIM architecture; accuracy includes ADC quantisation and device noise through MNSIM 2.0. Evaluation on CIFAR-10 and CIFAR-100 compares with NACIM, UAE, NAS4RRAM and CARS under accuracy-, area- and EDP-optimised targets.

## Contributions
- PIM-oriented NN search space (even kernels, group convs) improving crossbar utilisation
- ESAPP evolutionary search with adaptive parameter priority
- Multi-level joint simulator with RNN predictor to cut evaluation time
- Six design insights (even kernels, ADC bits, crossbar size) from the search results

## Key claims (stable IDs)
- **2023_Sun_Gibbon_TCAD#C1** — Gibbon finds better NN+PIM designs 9.8-48.2x faster than prior PIM NAS — _support:_ ~6 GPU hours vs 59 (NACIM) and 154 (UAE) GPU hours — _loc:_ Abstract, Sec. I, Sec. VII
- **2023_Sun_Gibbon_TCAD#C2** — Up to 15.3% accuracy improvement and 5.96x EDP reduction vs existing work — _support:_ Table III (CIFAR-10) — _loc:_ Abstract, Sec. IX
- **2023_Sun_Gibbon_TCAD#C3** — 2x2 kernels cut EDP ~84% and area ~35% vs 3x3 — _support:_ Insight 1 — _loc:_ Sec. VIII
- **2023_Sun_Gibbon_TCAD#C4** — 8-bit ADCs are within 0.2% of 10-bit, 6-bit loses accuracy — _support:_ CIFAR-10/100 PIM-based accuracy — _loc:_ Insight 4
- **2023_Sun_Gibbon_TCAD#C5** — 64x64 crossbars give lowest accuracy loss; 256x256 saves ~68% energy vs 128x128 — _support:_ predictor analysis — _loc:_ Insight 6, Fig. 17

## Results
- Search space 4.3e84 candidates; PIM utilisation of NACIM design only 53.1%
- ESAPP + predictor give ~12x co-exploration speedup over vanilla CARS-style search
- Search completes in ~6 GPU hours (RTX 2080 Ti) versus ~59 h (NACIM) and ~154 h (UAE)
- Design insight: deeper layers prefer high weight bit-width, shallow layers lower

## Key numbers
- array_size: 64x64 to 256x256 searched
- energy_eff: 5.96x lower EDP vs prior PIM-NAS
- throughput: 9.8-48.2x faster search
- accuracy: up to +15.3% PIM-based NN accuracy vs existing work
- bits_weight: 1b/2b cells; per-layer weight bits searched
- bits_adc: 6b/8b/10b compared

## Datasets / benchmarks
CIFAR-10, CIFAR-100

## Limitations
- CNN image classification on CIFAR-10/100 only; no transformers or LMs
- Hardware numbers come from MNSIM 2.0 simulation and a trained predictor, not measurement
- 1-bit/2-bit memristor cells and a single base architecture assumed
- Noise model limited to ADC/device defaults of MNSIM 2.0

## Remarks
A representative hardware-NAS paper for crossbar accelerators; its concrete findings (even kernels, ADC resolution sweet spot, 64 vs 256 crossbars) are small-CNN specific. For LM mapping the transferable piece is the predictor-based evaluation and priority-based search, which would need a transformer search space (attention matmuls, embeddings).

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Existing studies have proposed various memristor-based PIM architecture and realize 2-3 orders of magnitude energy efficiency improvement compared with GPU and CMOS-based ASIC solutions [3] [4] [6] [5] [23]."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "Furthermore, they utilize PIM simulators, e.g., MNSIM [16] and NeuroSim [17], to evaluate the PIM-based NN accuracy and other hardware performance."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "Existing studies have proposed various memristor-based PIM architecture and realize 2-3 orders of magnitude energy efficiency improvement compared with GPU and CMOS-based ASIC solutions [3] [4] [6] [5] [23]."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _background_: "On the one hand, the numbers of rows and columns of the crossbars (the basic computing units in PIM) are always the power of two, e.g., 64, 128, and 256 [36]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _contrasts/critiques_: "However, NACIM utilizes a time-consuming PIM simulator (i.e., NeuroSim [17]) as the performance evaluator, resulting in a tremendous search time cost (~59 GPU hours)."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Existing studies have proposed various memristor-based PIM architecture and realize 2-3 orders of magnitude energy efficiency improvement compared with GPU and CMOS-based ASIC solutions [3] [4] [6] [5] [23]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Therefore, PIM-based NN accelerators can improve the energy efficiency of NN computing by two to three orders of magnitude over GPU and CMOS ASIC solutions [3-7]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _uses-method-or-tool_: "We adopt the PIM architecture proposed in MultiPrecision [6] as our infrastructure, for it can achieve higher equivalent energy efficiency with nearly no accuracy loss."
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)

## Cited by (in collection, 2)
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _motivation_: "However, separately optimizing hardware parameters for high-accuracy models may result in suboptimal designs, as software-optimized models often lead to underutilized CIM-based hardware in deployment [25]."
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2023_Sun_Gibbon_TCAD.pdf](../../05_Mapping_Compilation_and_Dataflow/2023_Sun_Gibbon_TCAD.pdf)
- Full text: [../fulltext/2023_Sun_Gibbon_TCAD.txt](../fulltext/2023_Sun_Gibbon_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2023.3262201
