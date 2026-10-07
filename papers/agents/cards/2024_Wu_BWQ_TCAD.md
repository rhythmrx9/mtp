---
id: W4399310783
key: 2024_Wu_BWQ_TCAD
title: "Block-Wise Mixed-Precision Quantization: Enabling High Efficiency for Practical ReRAM-Based DNN Accelerators"
short: "BWQ"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)"
authors: "Xueying Wu, Edward Hanson, Nansu Wang, Qilin Zheng, Xiaoxuan Yang, Huanrui Yang, Shiyu Li, Feng Cheng, Partha Pratim Pande, Janardhan Rao Doppa, Krishnendu Chakrabarty, Hai Helen Li"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG", "MobileNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["mixed-precision", "quantization", "adc-dac", "weight-mapping", "crossbar-architecture", "energy-efficiency", "cnn-accelerator", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 15
priority_score: 3.84
doi: "https://doi.org/10.1109/tcad.2024.3409193"
pdf: "../../09_ADCs_Peripherals_Quantization_Sparsity/2024_Wu_BWQ_TCAD.pdf"
fulltext: "../fulltext/2024_Wu_BWQ_TCAD.txt"
---

# BWQ

**Block-Wise Mixed-Precision Quantization: Enabling High Efficiency for Practical ReRAM-Based DNN Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024) (2024)

## TL;DR
BWQ combines block-wise mixed-precision quantization (BWQ-A) with a precision-aware OU-based ReRAM accelerator (BWQ-H), giving 6.08x average speedup and 17.47x energy saving over ISAAC.

## Summary
Practical ReRAM accelerators can only activate a small Operation Unit (OU, 9 WLs x 8 BLs here) per cycle for accuracy, and ADCs dominate latency and energy (50-70% of power per cited work), which wastes the parallelism assumed by ISAAC-style designs but creates room for fine-grained mixed precision. BWQ-A quantizes weights at the granularity of weight blocks (OU-sized) with quantization-aware training and periodic re-quantization (650 epochs for CIFAR), also compressing activations. BWQ-H uses 128x128 1-bit-per-cell crossbars, 1-bit DACs, 4-bit ADCs, and a precision-aware mapping that places same-significance bit positions of different weights into one OU to raise utilization, plus a memory controller (synthesized in TSMC 28nm) that tracks per-block bit-width. Evaluation: algorithm on CIFAR-10/100 and ImageNet (ResNet-18/20/34, VGG16/19-BN, MobileNetV2, DenseNet-121), hardware with a modified MNSIM against ISAAC, SRE, SME and BSQ. Results show higher compression than BSQ at similar accuracy (15.74x lower average bit-width on VGG19-BN) and the highest speedup/energy efficiency.

## Contributions
- Block-level mixed-precision quantization algorithm BWQ-A for weights and activations
- BWQ-H OU-based ReRAM architecture with precision-aware weight mapping and mixed-precision memory controller
- Scalability analysis of OU sizes from 9x8 up to 128x128

## Key claims (stable IDs)
- **2024_Wu_BWQ_TCAD#C1** — BWQ-H gives 6.08x speedup and 17.47x energy saving over ISAAC on average — _support:_ averages over models/datasets — _loc:_ Sec. VI-B, Fig. 9
- **2024_Wu_BWQ_TCAD#C2** — BWQ-H outperforms SRE, SME, BSQ — _support:_ 4.44x/11.98x over SRE, 3.66x/7.65x over SME, 1.45x/2.66x over BSQ (speedup/energy) — _loc:_ Sec. VI-B
- **2024_Wu_BWQ_TCAD#C3** — Finer granularity lowers average bit-width vs BSQ — _support:_ 15.74x lower avg bit-width on VGG19-BN CIFAR-10 — _loc:_ Fig. 7-8

## Results
- ADC energy dominates in OU-based operation; compression reduces ADC cycles
- Chip total power 25.25W incl. 23.22W for one component class (Table I), 1.2 GHz, 28nm controller
- SRE achieves only ~3.3x compression with 9x8 OUs (~10x with 2x2 OUs)
- Runtime minimum near 64x64 OU in the OU-size study

## Key numbers
- tech_node: 28nm (controller)
- array_size: 128x128 crossbar, 9x8 OU
- energy_eff: 17.47x vs ISAAC
- throughput: 6.08x speedup vs ISAAC
- bits_weight: mixed, 1 bit/cell
- bits_adc: 4b

## Datasets / benchmarks
CIFAR-10, CIFAR-100, ImageNet

## Limitations
- Simulation (modified MNSIM), no silicon
- No analog noise injected in accuracy; non-idealities only motivate OU size
- CNNs only; no transformers/LMs
- Baselines re-implemented by authors

## Remarks
A well-grounded architecture paper because it adopts the realistic OU-limited regime instead of whole-crossbar MVM. The block-wise precision granularity aligned with OU is reusable for mixed-precision mapping of any model, including LMs, but no such evidence here. Related to MPQ (mixed-precision for ReRAM inference) in the collection.

## Cites (in collection, 8)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _data/numbers_: "Several studies have demonstrated that, in practice, an OU can accommodate a block with only nine WLs and eight BLs [3, 11]."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _background_: "For a practical ReRAM-based DNN accelerator, the VMM on the crossbar arrays should operate at a much finer granularity, termed as an Operation Unit (OU), rather than at the subarray granularity. [3, 9, 10]."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _motivation_: "It is demonstrated by several recent studies that for a practical ReRAM-based DNN accelerator to attain an acceptable level of inference accuracy, only nine WLs and eight BLs can be turned on concurrently [3, 11, 12]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "HW-based optimization solutions only improve the accelerators’ performance from an HW perspective, featuring intra-layer pipeline (ISAAC [5]) or leveraging the natural sparsity of the neural networks with index reordering (SRE [3])."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "They assume that it is possible to activate all the rows and columns of a 128 × 128 or 256 × 256 array simultaneously within a single clock cycle without impacting computational accuracy[4, 5]."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _baseline/comparison_: "SW-based optimization solution ReCom [13] and MPQ [14] proactively compress the models with algorithms."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _contrasts/critiques_: "For example, CMP [15] conducts layerwise mixed-precision quantization, and its model compression performance is limited."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)

## Files
- PDF: [../../09_ADCs_Peripherals_Quantization_Sparsity/2024_Wu_BWQ_TCAD.pdf](../../09_ADCs_Peripherals_Quantization_Sparsity/2024_Wu_BWQ_TCAD.pdf)
- Full text: [../fulltext/2024_Wu_BWQ_TCAD.txt](../fulltext/2024_Wu_BWQ_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2024.3409193
