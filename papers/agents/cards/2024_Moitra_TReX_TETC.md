---
id: W4403600569
key: 2024_Moitra_TReX_TETC
title: "TReX- Reusing Vision Transformer’s Attention for Efficient Xbar-Based Computing"
short: "TReX"
year: 2024
venue: "TETC"
venue_full: "IEEE Transactions on Emerging Topics in Computing (2024)"
authors: "Abhishek Moitra, Abhiroop Bhattacharjee, Youngeun Kim, Priyadarshini Panda"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["FeFET", "SRAM-analog"]
models: ["ViT", "BERT", "Transformer"]
lm_models: ["BERT-Base (CoLA fine-tune)"]
param_scale: "110M"
slm: true
evidence: algorithm+simulation
topics: ["transformer-accelerator", "attention", "nas-codesign", "energy-efficiency", "hardware-aware-training", "device-variation", "simulator", "heterogeneous-analog-digital"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 3
priority_score: 7.42
doi: "https://doi.org/10.1109/tetc.2024.3480524"
pdf: "../../04_Transformers_and_LLMs/2024_Moitra_TReX_TETC.pdf"
fulltext: "../fulltext/2024_Moitra_TReX_TETC.txt"
---

# TReX

**TReX- Reusing Vision Transformer’s Attention for Efficient Xbar-Based Computing** — IEEE Transactions on Emerging Topics in Computing (2024) (2024)

## TL;DR
TReX removes the attention block from selected ViT encoders and reuses the previous encoder's attention output through a small transformation block, chosen to meet a delay target on 64x64 FeFET/SRAM crossbars, giving 2.3x (DeiT-S) and 2.19x (LV-ViT-S) EDAP reduction at ~1% non-ideal accuracy drop on ImageNet-1k.

## Summary
The paper observes that on IMC-implemented ViTs the attention block dominates energy, delay and area, and that the K^T and V matrices of QK^T and S(QK^T)V must be written into crossbars (about 80% of overall delay). TReX replaces the attention of every 'reuse' encoder with the concatenated attention output of the previous encoder, passed through a transformation block (LayerNorm, d x d FC, GeLU) that adds data variability. A 4-step procedure picks N_reuse from a user delay target using the TReXSim simulator (Algorithm 1), enumerates strided/continuous/pyramid reuse patterns, partially trains each on 20% of the data, and fully trains the best pattern with IMC-variation-aware training (ADC quantisation plus read/write noise for FeFET; only ADC noise for SRAM). Mapping uses a tiled architecture with 64x64 crossbars, 8 crossbars per PE and 8 PEs per tile, 8-bit weights/inputs, 6-bit ADC and 1-bit input splitting, 32nm CMOS, 2-bit FeFETs with 10% read and 20% write variation. Static-weight layers go to FeFET and dynamic MatMuls can go to SRAM in a hybrid design. Evaluation is simulated on DeiT-S and LV-ViT-S (ImageNet-1k) and BERT-Base on CoLA, compared with token pruning, weight sharing and ReTransformer in TReXSim.

## Language models evaluated
- Models: BERT-Base (CoLA fine-tune)
- Scale: 110M

## Contributions
- TReX: attention-reuse optimisation framework for ViTs on crossbars with delay-targeted selection of encoders
- TReXSim: IMC-realistic benchmarking platform covering FeFET and SRAM crossbars including write energy/delay
- Analysis showing attention block dominates energy/delay/area and that crossbar writes for QK^T and S(QK^T)V are ~80% of delay
- Better accuracy-EDAP trade-off than token pruning and weight sharing; extension to BERT-Base on CoLA

## Key claims (stable IDs)
- **2024_Moitra_TReX_TETC#C1** — Attention reuse gives 2.3x EDAP reduction on DeiT-S at ~1% accuracy loss — _support:_ 2.3x (2.19x for LV-ViT-S) EDAP, 1.86x (1.79x) TOPS/mm2 — _loc:_ Abstract / Tables IV-V
- **2024_Moitra_TReX_TETC#C2** — Writes for the dynamic MatMuls account for ~80% of attention-block delay on crossbars — _support:_ ~80% of overall delay — _loc:_ Sec. I
- **2024_Moitra_TReX_TETC#C3** — Weight sharing WS=3 collapses accuracy while TReX keeps it — _support:_ WS=3 drops to ~60%; WS=2 78.3% at 2x EDAP; token pruning only 1.3x EDAP at 79.3% — _loc:_ Sec. VII, Fig. 13
- **2024_Moitra_TReX_TETC#C4** — On CoLA TReX improves non-ideal accuracy 2% at 1.6x lower EDAP — _support:_ TReX-B-7/6; 3% drop at 2x, 8% drop at 3.5x — _loc:_ Sec. VII-F, Fig. 18

## Results
- DeiT-S: EDAP 1115 -> 484 (2.3x lower) for TReX-D-6; TOPS/mm2 up to 4.21x at the most aggressive TReX-D-4 (EDAP 6.3x lower) (Table IV)
- LV-ViT-S: EDAP 2030 -> 924 (2.19x lower) at TReX-L-9, up to 5.57x lower at most aggressive target (Table V)
- TOPS/W improves only 1.03-1.11x; TOPS/mm2 up to 2.63x (DeiT-S) and 3.69x (LV-ViT-S, with 3-5% accuracy loss)
- BERT-Base/CoLA: 1.6x EDAP reduction with +2% non-ideal accuracy; 2x at -3%; 3.5x at -8%; overall 2.75x TOPS/mm2, 1.1x TOPS/W
- Token pruning limited to 1.3x EDAP at 79.3% accuracy; ReTransformer gives only 1.0001x TOPS/W gain on TReXSim

## Key numbers
- tech_node: 32nm CMOS
- array_size: 64x64
- energy_eff: 33.5-37.4 TOPS/W (LV-ViT-S baseline to TReX)
- accuracy: ~1% non-ideal accuracy drop at 2.3x EDAP (DeiT-S, ImageNet-1k)
- bits_weight: 8b (2 bits/cell FeFET)
- bits_adc: 6b

## Datasets / benchmarks
ImageNet-1k, CoLA

## Limitations
- Simulation only (TReXSim); no silicon
- Only read/write variation and ADC quantisation modelled; IR-drop and transistor non-linearity excluded
- Isotropic small ViTs; only one NLP model (BERT-Base, CoLA) with 10-epoch fine-tuning
- Accuracy loss grows quickly at high reuse ratios (3-8% on CoLA)
- Reuse pattern chosen by partial training on 20% data; heuristic pattern families only

## Remarks
A model-side co-design that cuts the part of the transformer that maps worst on weight-stationary NVM crossbars (dynamic attention MatMuls requiring writes). The NVM write cost insight is the most reusable result, and the FeFET/SRAM hybrid foreshadows heterogeneous mappings. The language-model evidence is thin (BERT-Base on CoLA only) so it is a ViT paper first. Evidence is simulation with noise-aware retraining from the Yale group, complementary to ClipFormer and X-Former.

## Cites (in collection, 9)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _motivation_: "This leads to significant accuracy losses for neural networks mapped onto crossbars, especially for larger crossbars with more non-idealities [27], [29], [30]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "While there exists other IMC-specific non-idealities such as IR-drop [26] and transistor nonlinearities [29], we use read/write variations (only for FeFET implementation) and ADC quantization noise (for both FeFET and SRAM implementations) to evaluate TReX."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _uses-method-or-tool_: "Additionally, to reduce the ADC precision, we follow input and weight splitting paradigms similar to prior works [7], [34]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "Following prior works, we assume that multiple tiles can map one layer but not vice-versa [7], [33]."
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022) — _background_: "Recently, many works have proposed efficient IMC implementations for transformers [10], [11]. The authors in [10] propose fully analog implementations for transformers by using memristive circuits for dot-product operations and analog circuits for implementing non-linear functions such as GeLU, ReLU and softmax."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "The IR-drop and transistor non-linearity noise follow a structured profile and can be mitigated using simple approaches such as batchnorm adaptation and weight retraining [28], [30]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Recent IMC-centric transformer co-optimization works [10], [11], [18] have proposed IMC architecture implementations to efficiently compute the Matmul layers."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _motivation_: "Extensive research has shown that device variations and ADC quantization contribute significantly towards accuracy degradation and cannot be easily mitigated [28], [39]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _data/numbers_: "The crossbar energy, delay and area values are obtained based on IMC implementations of SRAM and FeFET crossbars of size 64x64 [33], [40]."

## Files
- PDF: [../../04_Transformers_and_LLMs/2024_Moitra_TReX_TETC.pdf](../../04_Transformers_and_LLMs/2024_Moitra_TReX_TETC.pdf)
- Full text: [../fulltext/2024_Moitra_TReX_TETC.txt](../fulltext/2024_Moitra_TReX_TETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tetc.2024.3480524
