---
id: W4307927141
key: 2022_Huang_HWAwareQuantMappingCIM_TODAES
title: "Hardware-aware Quantization/Mapping Strategies for Compute-in-Memory Accelerators"
short: "CIM Quant/Mapping DSE"
year: 2022
venue: "TODAES"
venue_full: "ACM Transactions on Design Automation of Electronic Systems"
authors: "Shanshi Huang, Hongwu Jiang, Shimeng Yu"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM", "FeFET"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["quantization", "weight-mapping", "bit-slicing", "adc-dac", "pruning-sparsity", "energy-efficiency", "benchmarking", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 10
citations_overall: 12
priority_score: 6.21
doi: "https://doi.org/10.1145/3569940"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2022_Huang_HWAwareQuantMappingCIM_TODAES.pdf"
fulltext: "../fulltext/2022_Huang_HWAwareQuantMappingCIM_TODAES.txt"
---

# CIM Quant/Mapping DSE

**Hardware-aware Quantization/Mapping Strategies for Compute-in-Memory Accelerators** — ACM Transactions on Design Automation of Electronic Systems (2022)

## TL;DR
A system-level design-space study of how quantization (fixed-point vs dynamic fixed-point), signed-number mapping (2's complement, differential pair, shifted unsigned) and ADC precision affect eNVM CIM accelerators, finding dynamic fixed-point plus an optimised mapping and ADC gives ~2x energy efficiency, 1.2-1.6x throughput and 5-25% less area than a naive baseline.

## Summary
Mixed-signal eNVM CIM accelerators require floating-point DNNs to be quantised and mapped onto crossbars, but prior chips choose these strategies ad hoc. The authors build a design flow and compare two quantisation algorithms (WAGE-style fixed-point and dynamic fixed-point, DF) with three number representations for mapping signed weights onto non-negative conductances: Case1 2's complement extended (sign column), Case2 differential pair (two arrays per digit), and Case3 shifted unsigned INT (dummy column to cancel Gmin offset). Inputs are 1-bit digits and weight digits 1-4 bit/cell with 8-bit weights and activations. Accuracy is checked versus cell on/off ratio, then hardware (area, TOPS/W, throughput) is evaluated with DNN+NeuroSim V1.3 at 22 nm (RRAM Ron/Roff 6k/900k Ohm; 128x128 arrays for VGG-8/CIFAR-10 and 64x64 for ResNet-18 on CIFAR-100 and ImageNet), first with full-precision SAR ADC and then with the lowest ADC precision meeting accuracy targets of 90%, 67% and 83% for CIFAR-10, CIFAR-100 and ImageNet subset. A layer-wise analysis shows deeper convolution layers are more efficient than FC and shallow layers.

## Contributions
- Complete NN-to-eNVM-CIM mapping flow covering quantisation, number representation and ADC
- Analysis of how input sparsity differs by quantisation method and drives CIM energy
- Joint comparison of three signed-weight mapping schemes across 1/2/4-bit cell precision and ADC precision
- Guidelines for architects: DF+Case1 for low cell precision, DF+Case3 or Case2 with reduced ADC for high precision
- Layer-by-layer energy and throughput analysis on VGG-8

## Key claims (stable IDs)
- **2022_Huang_HWAwareQuantMappingCIM_TODAES#C1** — Dynamic fixed-point quantisation gives better energy efficiency than WAGE fixed-point because its input bits contain more zeros — _support:_ Same area/throughput, higher TOPS/W (full-precision ADC) — _loc:_ Sec. 4.1, Fig. 7
- **2022_Huang_HWAwareQuantMappingCIM_TODAES#C2** — 2's complement mapping (Case1) with high-precision cells fails without Gmin cancellation, even at on/off ratio 100 for 4-bit cells — _support:_ Accuracy collapse; dummy column recovers it — _loc:_ Sec. 4.1, Fig. 6
- **2022_Huang_HWAwareQuantMappingCIM_TODAES#C3** — Case2 (differential pair) tolerates the most aggressive ADC precision reduction across cell precisions — _support:_ Lower partial-sum distribution mismatch; at least one array is zero — _loc:_ Sec. 4.2, Fig. 8
- **2022_Huang_HWAwareQuantMappingCIM_TODAES#C4** — Optimal design options give 29-45% energy efficiency improvement, 4-40% area reduction and 4-25% speedup with full-precision ADC — _support:_ DF+Case3 (high cell precision) or DF+Case1 (low) — _loc:_ Sec. 4.1, Fig. 7
- **2022_Huang_HWAwareQuantMappingCIM_TODAES#C5** — Overall ~2x energy efficiency and 1.2-1.6x throughput, with 5-25% less area vs naive strategy — _support:_ naive = fixed-point + differential pair + full-precision ADC — _loc:_ Abstract, Fig. 9

## Results
- Naive-to-optimised: ~2x TOPS/W, 1.2-1.6x throughput, 5-25% area reduction (Abstract, Fig. 9)
- Full-precision ADC: optimal options reach 29-45% higher energy efficiency, 4-40% area reduction, 4-25% speedup (Fig. 7)
- ADC reduced until accuracy stays >=90% (CIFAR-10 VGG-8), 67% (CIFAR-100 ResNet-18), 83% (ImageNet subset) (Fig. 9)
- Throughput shows no clear trend across options because latency is split between ADC-dependent array latency and NoC latency (Fig. 7 g-i)
- Deeper conv layers have higher TOPS/W and GOPS than FC and shallow layers (Fig. 10)

## Key numbers
- tech_node: 22nm
- array_size: 128x128 (VGG-8); 64x64 (ResNet-18)
- energy_eff: ~2x vs naive baseline
- throughput: 1.2-1.6x vs naive baseline
- accuracy: targets 90% CIFAR-10, 67% CIFAR-100, 83% ImageNet subset
- bits_weight: 8b weights, 1-4 bit/cell
- bits_adc: reduced from full-precision SAR ADC to lowest meeting accuracy target

## Datasets / benchmarks
CIFAR-10, CIFAR-100, ImageNet (subset)

## Limitations
- Simulation with DNN+NeuroSim; no silicon
- Only CNNs (VGG-8, ResNet-18); no transformers or language models, whose activation ranges and signed activations differ
- Device non-idealities (variation, drift, read noise) not the focus; only on/off ratio considered
- Single shared ADC reference for the whole network; no reconfigurable or calibrated ADC explored
- Dataflow mapping of 3D convolution to 2D MACs is fixed

## Remarks
A practical guide to the quantisation/number-representation choices that every crossbar mapping must make; the Gmin-cancellation and ADC-distribution insights apply directly to LM weight mapping, where heavy-tailed weights and activations make partial-sum distributions even less ADC-friendly. Evidence is solid for CNN CIM modelling (NeuroSim validated against chip data) but untested on LLM-scale workloads.

## Cites (in collection, 10)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "By integrating the computations into memory arrays, mixed-signal compute-in-memory architectures have shown impressive abilities in boosting the throughput and energy efficiency of deep learning algorithms [1]."
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017) — _background_: "Meanwhile, as emerging memories (such as resistive random access memory (RRAM) [2] and ferroelectric field-effect transistor (FeFET) [3]) offer high integration density and low operating energy costs, they are becoming promising candidates for CIM implementation."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "This differential-pair data representation is frequently used in CIM design such as [5, 24]."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _background_: "Other dataflow mapping methods could also be applied to improve the parallelism [20]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _background_: "Similarly, Zhenhua et al. [19] proposed the RRAM Computing Deviation Aware Quantization Scheme to search for the optimal precision for the weights and activations."
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020) — _background_: "Reference [29] uses the Cumulative distribution function (CDF) of the partial sum to decide the nonlinear references corresponding to linear quantized cumulative distribution."
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020) — _background_: "For example, RaQu [18] processes the layer-wise quantization and further finetunes the bit width of groups of weights."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _data/numbers_: "Besides, as illustrated in previous work [30], the ADC contributes a large portion of total energy consumption and latency in CIM design, becoming more severe with increasing ADC precision."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Thus, various CIM designs based on emerging non-volatile memory (eNVM) have been proposed for edge inference [4, 5, 6]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "For example, Wan et al. [25] use a differential pair in their weight encoding, but instead of dividing the positive and negative to separate arrays, the subtraction is directly done in the adjacents cells using inputs with opposite orientations."

## Cited by (in collection, 2)
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _contrasts/critiques_: "The in-situ weight update process was either performed in the offline training scheme [13–15] or performed one by one and coordinated by external closed-loop control circuits [16, 17]."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _uses-method-or-tool_: "The finite on/off ratio impact is not incorporated, as prior work has demonstrated that it can be effectively mitigated via the dummy column scheme [35]."

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2022_Huang_HWAwareQuantMappingCIM_TODAES.pdf](../../05_Mapping_Compilation_and_Dataflow/2022_Huang_HWAwareQuantMappingCIM_TODAES.pdf)
- Full text: [../fulltext/2022_Huang_HWAwareQuantMappingCIM_TODAES.txt](../fulltext/2022_Huang_HWAwareQuantMappingCIM_TODAES.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3569940
