---
id: W4366389026
key: 2023_Andrulis_RAELLA_ISCA
title: "RAELLA: Reforming the Arithmetic for Efficient, Low-Resolution, and Low-Loss Analog PIM: No Retraining Required!"
short: "RAELLA"
year: 2023
venue: "ISCA"
venue_full: "ACM/IEEE 50th Annual International Symposium on Computer Architecture (ISCA 2023)"
authors: "Tanner Andrulis, Joel Emer, Vivienne Sze"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "MobileNet", "Transformer", "BERT"]
lm_models: ["BERT-Large (feed-forward layers only)"]
param_scale: "340M"
slm: true
evidence: algorithm+simulation
topics: ["adc-dac", "bit-slicing", "quantization", "peripheral-circuits", "energy-efficiency", "read-write-noise", "calibration-compensation", "crossbar-architecture"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 8
cites_in_collection: 15
citations_overall: 45
priority_score: 8.52
doi: "https://doi.org/10.1145/3579371.3589062"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2023_Andrulis_RAELLA_ISCA.pdf"
fulltext: "../fulltext/2023_Andrulis_RAELLA_ISCA.txt"
---

# RAELLA

**RAELLA: Reforming the Arithmetic for Efficient, Low-Resolution, and Low-Loss Analog PIM: No Retraining Required!** — ACM/IEEE 50th Annual International Symposium on Computer Architecture (ISCA 2023) (2023)

## TL;DR
RAELLA cuts ReRAM-PIM ADC cost without retraining by shaping column-sum distributions (Center+Offset signed weights on 2T2R, per-layer adaptive weight slicing, speculative/recovery input slicing), giving 2.9-4.9x (geomean 3.9x) energy efficiency and 0.7-3.3x throughput over an 8b ISAAC baseline in simulation.

## Summary
ADCs dominate energy in ReRAM PIM; prior fixes either prune weights (Weight-Count-Limited: FORMS, SRE, PIM-Prune) or use low-resolution ADCs that lose fidelity (Sum-Fidelity-Limited: PRIME, TIMELY, CASCADE), and both retrain the DNN. RAELLA instead reshapes analog value distributions so a 7b ADC suffices at high fidelity. (1) Center+Offset encoding shifts each weight by a per-filter center so positive and negative weight slices balance, giving near-zero signed column sums computed in-crossbar by 2T2R cells, with the center contribution done digitally. (2) Adaptive Weight Slicing picks per-layer slicings (usually 4b-2b-2b ReRAM cells) under an error budget (0.09). (3) Dynamic Input Slicing runs 4b speculation input slices then 1b recovery slices only on columns where speculation saturated. Crossbars are 512x512 with 4b DACs (pulse trains), ReRAM 1k/20k ohm on/off; models in Accelergy/Timeloop at 32nm with modified NeuroSim, 743 tiles in 600 mm2. Workloads: six ImageNet CNNs and BERT-Large (SQuAD, feed-forward layers only, signed inputs processed in separate cycles). Noise is modelled as Gaussian on column sums with sigma = E*sqrt(N+ + N-), up to 12%.

## Language models evaluated
- Models: BERT-Large (feed-forward layers only)
- Scale: 340M

## Contributions
- Center+Offset signed weight encoding that keeps analog column sums small and zero-centered
- Adaptive per-layer weight slicing using an error budget
- Dynamic input slicing with speculation and recovery to reduce ADC converts
- Retraining-free architecture matched against ISAAC, FORMS and TIMELY, with accuracy and noise ablations

## Key claims (stable IDs)
- **2023_Andrulis_RAELLA_ISCA#C1** — RAELLA improves energy efficiency 2.9-4.9x (geomean 3.9x) and throughput up to 3.3x over ISAAC without retraining, with ADC converts reduced 5-15x. — _support:_ RAELLA 7b ADC vs ISAAC 8b; 512x512 vs 128x128 crossbars — _loc:_ Sec. 6.2, Fig. 12
- **2023_Andrulis_RAELLA_ISCA#C2** — Without speculation RAELLA retains 2.8x geomean efficiency and 2.7x throughput. — _support:_ recovery slices only — _loc:_ Sec. 6.2
- **2023_Andrulis_RAELLA_ISCA#C3** — Center+Offset is essential for accuracy and noise tolerance; Zero+Offset (plain differential) causes high ADC saturation and large accuracy loss. — _support:_ Table 4 and Fig. 15 (ISAAC suffers high loss at noise > 4%) — _loc:_ Sec. 6.3, 7.2
- **2023_Andrulis_RAELLA_ISCA#C4** — Matches FORMS throughput and exceeds FORMS/TIMELY efficiency while running off-the-shelf models. — _support:_ ResNet18/50 geomean comparison — _loc:_ Fig. 13

## Results
- Energy efficiency 2.9-4.9x (geomean 3.9x) and throughput 0.7-3.3x (geomean 2.0x) vs 8b ISAAC across seven DNNs
- Converts/MAC from 0.25 (ISAAC) to 0.063 with Center+Offset; adaptive slicing cuts ADC energy ~25%; speculation cuts ADC energy by 60%
- BERT-Large (SQuAD F1) and ImageNet CNNs show little to no accuracy loss; exact Table 4 values not recoverable from extracted text
- Gaussian column-sum noise up to 12% error (sigma ~4 for 512 2b x 2b MACs): RAELLA stays accurate while ISAAC degrades beyond 4%

## Key numbers
- tech_node: 32nm (65nm for TIMELY comparison)
- array_size: 512x512 (2T2R)
- energy_eff: 2.9-4.9x vs ISAAC (geomean 3.9x)
- throughput: 0.7-3.3x vs ISAAC
- accuracy: little to no accuracy loss without retraining
- bits_weight: 8b (4b-2b-2b slices)
- bits_adc: 7b

## Datasets / benchmarks
ImageNet, SQuAD, GoogLeNet, InceptionV3, ResNet18, ResNet50, ShuffleNetV2, MobileNetV2, BERT-Large

## Limitations
- Simulation (Accelergy/Timeloop, modified NeuroSim) with authors' re-implementations of ISAAC/FORMS
- BERT-Large evaluated only on feed-forward layers; attention not mapped
- Throughput gains lower for signed-input transformer layers and for compact CNNs with small filters
- Noise model is simple Gaussian on column sums; no drift, IR drop or device measurements
- Larger crossbar area from 2T2R and 512x512 arrays

## Remarks
A strong ADC-reduction contribution that decouples accuracy preservation from retraining, a practical advantage when training data is private. Its relevance to LM mapping: it is one of few ADC/bit-slicing papers testing BERT-Large, showing signed non-ReLU activations erode benefits. Evidence is simulator-derived, so absolute numbers should be read cautiously, but the noise ablation gives a useful template for column-sum noise analyses of transformers.

## Cites (in collection, 15)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "This density allows ReRAM-based systems to store and run on-chip pipelines that compute DNN layers sequentially [54, 56] without costly accesses to off-chip memory [59]."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _uses-method-or-tool_: "To process inputs, we use 4b pulse-train DACs for their simple hardware [32] and superior linearity [55]."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _uses-method-or-tool_: "If there is space, weights are replicated in-crossbar to compute multiple convolution steps using a partial Toeplitz expansion [11, 24]."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _contrasts/critiques_: "Some designs prune DNNs [8, 26, 48, 75, 80] to reduce DNN weight count, so we call these designs Weight-Count-Limited."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _contrasts/critiques_: "Alternatively, other designs use efficient lower-resolution ADCs to process high-resolution analog values from crossbars [5, 7, 24]."
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020) — _extends/builds-on_: "RAELLA uses 2T2R devices, shown in Fig. 6, to realize analog subtraction in-crossbar. 2T2R, with two ReRAMs (2R) per weight accessed via two access transistors (2T), have been explored as a method to represent signed weights [3, 27, 28, 67, 74]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _contrasts/critiques_: "Alternatively, other designs use efficient lower-resolution ADCs to process high-resolution analog values from crossbars [5, 7, 24]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _uses-method-or-tool_: "DAC, input driver, and crossbar area/energy are generated using a modified NeuroSim [2, 44]."
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021) — _contrasts/critiques_: "TinyADC [79] retrains while pruning DNN weight bits, achieving impressive reductions in column sum resolution."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _baseline/comparison_: "FORMS [80], a Weight-Count-Limited architecture, achieves a 2.0x MACs/DNN"
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _uses-method-or-tool_: "ISAAC's encoding strategy relies on an analog circuit that sums crossbar inputs [54]. This component has been shown to degrade accuracy under noise [73], so we replace it with a digital equivalent."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021) — _contrasts/critiques_: "BRAHMS [57] tailors ADC quantization steps for each layer to maximize DNN accuracy under fidelity loss."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "Architectures often partition, or slice, the bits in DNN inputs and weights into multiple lower-resolution slices and compute with different slices in multiple steps [54]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "Alternatively, other designs use efficient lower-resolution ADCs to process high-resolution analog values from crossbars [5, 7, 24]. We call these designs Sum-Fidelity-Limited as the resolution difference reduces output fidelity and introduces error."
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022) — _background_: "Other works explore accelerating Transformer attention [39, 58, 77]."

## Cited by (in collection, 8)
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _uses-method-or-tool_: "For more information, see the Titanium Law [38], which breaks down the factors that contribute to ADC energy and shows how ADC energy can be reduced."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "In particular, both digital and analog PIM approaches have shown significant efficiency improvements - digital PIM reduces data movement costs while maintaining the accuracy for high bit-precision operations [16, 24, 32, 58, 60, 68, 79], and analog PIM demonstrates dramatic efficiency improvement, achieving more than two orders of magnitude benefit [5, 9, 17, 24] through low-voltage swing operations."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "RAELLA [2] is a more recent architecture proposal that also leverages a hierarchical interconnect."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _extends/builds-on_: "While not investigated in this paper, it is possible to extend the methodology of LionHeart to co-apply different techniques to further improve accuracy, e.g., tunable ADC resolutions in RAELLA [25]."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _baseline/comparison_: "To understand the inefficiency of RRAM-based IMC accelerators for evolving AI models, we analyze the energy consumption breakdown of ISAAC [4] and RAELLA [6]."
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2023_Andrulis_RAELLA_ISCA.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2023_Andrulis_RAELLA_ISCA.pdf)
- Full text: [../fulltext/2023_Andrulis_RAELLA_ISCA.txt](../fulltext/2023_Andrulis_RAELLA_ISCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3579371.3589062
