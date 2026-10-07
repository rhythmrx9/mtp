---
id: W3191560475
key: 2021_Yuan_FORMS_ISCA
title: "FORMS: Fine-grained Polarized ReRAM-based In-situ Computation for Mixed-signal DNN Accelerator"
short: "FORMS"
year: 2021
venue: "ISCA"
venue_full: "ACM/IEEE 48th International Symposium on Computer Architecture (ISCA 2021)"
authors: "Geng Yuan, Payman Behnam, Zhengang Li, Ali Reza Shafiee, Sheng Lin, Xiaolong Ma, Hang Liu, Xuehai Qian, Mahdi Nazm Bojnordi, Yanzhi Wang, Caiwen Ding"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["crossbar-architecture", "pruning-sparsity", "quantization", "adc-dac", "hardware-aware-training", "device-variation", "energy-efficiency", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 14
citations_overall: 73
priority_score: 8.24
doi: "https://doi.org/10.1109/isca52012.2021.00029"
pdf: "../../03_Crossbar_Accelerator_Architectures/2021_Yuan_FORMS_ISCA.pdf"
fulltext: "../fulltext/2021_Yuan_FORMS_ISCA.txt"
---

# FORMS

**FORMS: Fine-grained Polarized ReRAM-based In-situ Computation for Mixed-signal DNN Accelerator** — ACM/IEEE 48th International Symposium on Computer Architecture (ISCA 2021) (2021)

## TL;DR
FORMS trains CNNs with ADMM so that weights in each small crossbar sub-array column share one sign (polarization), removing the dual-crossbar/offset cost, and adds input zero-skipping, giving 1.50x GOPs/s/mm2 and 1.93x GOPs/W over an optimised ISAAC.

## Summary
ReRAM crossbars need all cells of a column to have one sign, so prior designs use two crossbars per signed weight (PRIME) or an offset (ISAAC), costing area or peripheral circuitry. FORMS instead enforces the property in the model: after structured pruning, weights are cut into fixed-size fragments (e.g. 4-16 rows) that map to one sub-array column, and an ADMM-regularised training step forces every fragment to be uniformly positive or negative, with only magnitudes stored in 2-bit cells and a sign bit per fragment kept separately. Sub-arrays of a logical 128x128 crossbar are operated at fine granularity, so small 4-bit ADCs replace ISAAC's shared 8-bit ADC and fewer rows are summed per read, which reduces noise susceptibility. Small fragments also make input bit-stream zero-skipping effective: if all inputs of a fragment are zero in higher bit positions, those cycles are skipped by on-the-fly shift control. The architecture (tiles, MCUs with zero-skip DACs, sample-and-hold ADCs, eDRAM, shift-and-add, sign indicators) is evaluated with 16-bit inputs, 8-bit weights, 2-bit cells; models LeNet-5, ResNet-18/50, VGG16 on MNIST, CIFAR-10/100 and ImageNet, with area/power from synthesis/CACTI-style models compared against ISAAC, DaDianNao, PUMA, TPU, WAX and SIMBA. A variation study uses log-normal device variation (sigma 0.1, 50 runs).

## Contributions
- Fragment polarization: ADMM-enforced same-sign weights within fine-grained crossbar sub-array columns, avoiding dual crossbars or offsets
- Fine-grained sub-array computation with small (4-bit) ADCs that is less susceptible to non-idealities
- Input zero-skipping logic that exploits small fragment size to cut cycles
- Joint pruning + polarization + quantization framework giving large crossbar reduction

## Key claims (stable IDs)
- **2021_Yuan_FORMS_ISCA#C1** — FORMS improves area and power efficiency over optimised ISAAC at similar cost — _support:_ 1.50x GOPs/s/mm2 and 1.93x GOPs/W; 1.12x-2.4x FPS — _loc:_ Abstract / Table (architecture comparison) / Sec. V
- **2021_Yuan_FORMS_ISCA#C2** — The optimisation framework alone can speed up original ISAAC 10.7x to 377.9x — _support:_ Speedup over ISAAC-32 across networks — _loc:_ Fig. 13 / Conclusion
- **2021_Yuan_FORMS_ISCA#C3** — Polarization and zero-skipping do not reduce robustness to variation; pruning does — _support:_ ResNet18 ImageNet degradation 2.87% original vs 2.86% polarization-only vs 4.21% full optimisation (sigma 0.1) — _loc:_ Sec. V-E / Table VI
- **2021_Yuan_FORMS_ISCA#C4** — Large crossbar reduction on MNIST — _support:_ LeNet-5: 185.44x (23.18x pruning, 4x quantization, 2x polarization) — _loc:_ Sec. V-A / Table I

## Results
- 1.50x GOPs/s/mm2 and 1.93x GOPs/W vs optimised ISAAC at almost same power/area (abstract)
- 1.12x-2.4x FPS speedup over optimised ISAAC; up to 377.9x over original ISAAC (Fig. 13)
- LeNet-5 MNIST 185.44x crossbar reduction at 99.17% accuracy (Table I)
- Device variation (log-normal, 0.1 std, 50 runs) ResNet-18: CIFAR-10 0.35% to 1.80%, CIFAR-100 0.72% to 1.89%, ImageNet 2.87% to 4.21% accuracy degradation, original vs full optimisation (Table VI)

## Key numbers
- array_size: 128x128 crossbar, fragments (sub-array columns) of 4-16 rows
- energy_eff: 1.93x GOPs/W vs optimised ISAAC
- throughput: 1.50x GOPs/s/mm2 vs optimised ISAAC
- accuracy: 99.17% MNIST LeNet-5; ResNet-18 variation degradation 1.80% CIFAR-10
- bits_weight: 8b (2b cells)
- bits_adc: 4b (vs 8b in ISAAC)

## Datasets / benchmarks
MNIST, CIFAR-10, CIFAR-100, ImageNet

## Limitations
- Evaluated by simulation/analytical models, no silicon
- Only CNNs/MLP; no transformers or LMs
- Large ISAAC speedups depend on comparing against unoptimised ISAAC; fair baseline is optimised ISAAC
- Pruning reduces variation robustness (extra ~1.3% degradation); only ReRAM variation modelled, no IR drop or drift
- Requires retraining with ADMM and a sign indicator per fragment

## Remarks
A clean algorithm/architecture co-design that attacks signed-weight representation, a design axis common to all analog MVM (cf. 2T2R differential pairs in Liu ISSCC'20). The idea of constraining weight structure per sub-array column is transferable, but retraining cost and the CNN-only evaluation limit direct relevance to language models, where outlier weights may make polarization harder. Complements TinyADC and structured-pruning ADMM works from the same group in the collection.

## Cites (in collection, 14)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Several ReRAM-based in-situ mixed-signal DNN accelerators such as ISAAC [18], Newton [19], PipeLayer [20], PRIME [17], PUMA [21], MultiScale [22], XNORRRAM [37], RapidDNN [38], have been proposed in recent years."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "A promising emerging technology is the recently discovered resistive random access memory (ReRAM) [14, 15] devices that are able to perform the inherently parallel insitu matrix-vector multiplication in the analog domain."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _background_: "Several ReRAM-based in-situ mixed-signal DNN accelerators such as ISAAC [18], Newton [19], PipeLayer [20], PRIME [17], PUMA [21], MultiScale [22], XNORRRAM [37], RapidDNN [38], have been proposed in recent years."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _contrasts/critiques_: "The general way is to use two ReRAM crossbars to hold the positive and negative magnitudes weights separately, doubling the ReRAM portion of hardware cost [17, 25-28]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Several ReRAM-based in-situ mixed-signal DNN accelerators such as ISAAC [18], Newton [19], PipeLayer [20], PRIME [17], PUMA [21], MultiScale [22], XNORRRAM [37], RapidDNN [38], have been proposed in recent years."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _motivation_: "The recent study [40, 42] reports the ADC/DAC blocks may become the major contributor to the total chip area and power."
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019) — _contrasts/critiques_: "The previous ReRAM-based accelerator designs [47, 48] apply structured pruning and aim to make the pruning ratio as high as possible while maintaining an acceptable accuracy loss."
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020) — _contrasts/critiques_: "The previous ReRAM-based accelerator designs [47, 48] apply structured pruning and aim to make the pruning ratio as high as possible while maintaining an acceptable accuracy loss."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _background_: "variation [18, 61]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "Besides, the recent work TIMELY [23] is proposed to enhance the analog data C."
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _background_: "While keeping the number of crossbars the same, the latter approach introduces additional hardware costs for the peripheral circuits by adding extra offset circuits and may also decrease the network robustness to hardware failures [29]."
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021) — _contrasts/critiques_: "TinyADC [40] proposes a pruning solution that fixes the number of non-zero weights in each column of the ReRAM crossbar while their positions can vary."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "In contrast, ISAAC [18] adds an offset to weights so that all values become positive."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "The general way is to use two ReRAM crossbars to hold the positive and negative magnitudes weights separately, doubling the ReRAM portion of hardware cost [17, 25-28]."

## Cited by (in collection, 13)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _baseline/comparison_: "Comparison of data representation in selected prior work on analog in situ inference accelerators (Table 1), listing FORMS alongside ISAAC, PUMA, PRIME and others by bit-slicing, sign handling, array size and ADC/DAC bits."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _motivation_: "It is well-known that ADCs exponentially undermine performance and energy efficiency [67], [71]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _baseline/comparison_: "FORMS [80], a Weight-Count-Limited architecture, achieves a 2.0x MACs/DNN"
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "Figure 1 shows a typical ReRAM-based accelerator for DNN model [19, 21, 38]."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _background_: "We sort out the designs of recent CIM accelerators from three dimensions: memory device, architecture hierarchy, and programming interface, and summarize them in Figure 1 [4, 6, 13, 18, 19, 21, 23, 28, 29, 33, 34, 39, 43, 46–51]."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _uses-method-or-tool_: "CiMLoop supports encoding and slicing functions from CiM implementations, including offset [2], differential [38], XNOR [16], and magnitudeonly [44]."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _background_: "We note that this architecture only incurs a minor modification to the connection between multiplexers and ADCs, while crossbar arrays and other periphery circuits remain the same as previous works [1, 31, 35, 53]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2021_Yuan_FORMS_ISCA.pdf](../../03_Crossbar_Accelerator_Architectures/2021_Yuan_FORMS_ISCA.pdf)
- Full text: [../fulltext/2021_Yuan_FORMS_ISCA.txt](../fulltext/2021_Yuan_FORMS_ISCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isca52012.2021.00029
