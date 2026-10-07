---
id: W2899868573
key: 2018_Zhu_MISCA_ICCAD
title: "Mixed size crossbar based RRAM CNN accelerator with overlapped mapping method"
short: "MISCA"
year: 2018
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2018)"
authors: "Zhenhua Zhu, Jilan Lin, Ming Cheng, Lixue Xia, Hanbo Sun, Xiaoming Chen, Yu Wang, Huazhong Yang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["weight-mapping", "tiling-partitioning", "crossbar-architecture", "cnn-accelerator", "adc-dac", "peripheral-circuits", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 11
cites_in_collection: 4
citations_overall: 55
priority_score: 7.95
doi: "https://doi.org/10.1145/3240765.3240825"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2018_Zhu_MISCA_ICCAD.pdf"
fulltext: "../fulltext/2018_Zhu_MISCA_ICCAD.txt"
---

# MISCA

**Mixed size crossbar based RRAM CNN accelerator with overlapped mapping method** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2018) (2018)

## TL;DR
MISCA combines mixed-size RRAM crossbars with an Overlapped Mapping Method (OMM) that maps a kernel to several staggered columns to reuse idle cells, raising crossbar utilization from 56.75% to 91.26% and giving 2.7x speedup / 1.2x energy efficiency over fixed-size crossbars, and 26.4x speedup / 1.65x energy efficiency over PRIME on VGG-D (simulation).

## Summary
Large crossbars cut ADC/DAC interface cost (interfaces are >85% of energy in RRAM computing systems), but conventional mapping (one kernel unfolded into one crossbar column) wastes cells: ResNet-18 and AlexNet reach only 57% utilization on 512x512 crossbars (Table 1) because 60-90% of CNN layers have fewer than 512 output channels and kernel length is not a multiple of the crossbar row count (e.g. a 576-long ResNet-34 kernel wastes 87.5% of a second crossbar). OMM merges input vectors of consecutive sliding-window positions into a long vector and maps staggered, overlapped copies of each kernel to different columns, computing several outputs per cycle while reusing input data (reducing DAC activations, e.g. 25% in a toy example). Limits of OMM on fixed-size crossbars (utilization, unbalanced mapping, buffer bandwidth) motivate MISCA, with mixed-size crossbars, an area-constrained crossbar allocation/mapping algorithm for Conv layers (first to use mixed sizes for 1x1 convolutions) and FC layers. Evaluated with MNSIM at 100 MHz on AlexNet, VGG-D, ResNet-18/34/50 (ImageNet) against fixed-size crossbars, an NVIDIA Titan X GPU and PRIME.

## Contributions
- OMM: maps one kernel to multiple overlapped columns to reuse inputs and exploit idle cells in large crossbars
- MISCA mixed-size crossbar accelerator that overcomes fixed-size limitations
- Area-constrained mixed-size mapping and allocation strategy for whole CNNs, including 1x1 convolutions
- Simulation evaluation vs fixed-size crossbars, GPU and PRIME

## Key claims (stable IDs)
- **2018_Zhu_MISCA_ICCAD#C1** — Conventional mapping uses only ~57% of 512x512 crossbar cells for ResNet-18 and AlexNet. — _support:_ Utilization 99/79/57% (AlexNet) and 99/88/57% (ResNet-18) for 128/256/512 crossbars — _loc:_ Table 1, Sec. 1
- **2018_Zhu_MISCA_ICCAD#C2** — MISCA with OMM raises average utilization from 56.75% to 91.26%. — _support:_ Table 4 — _loc:_ Sec. 1 contributions; Sec. 6.4
- **2018_Zhu_MISCA_ICCAD#C3** — MISCA gives 2.7x speedup and 1.2x energy efficiency on average over fixed-size crossbars, 1.7-2.7x whole-system and 3.1-6.7x on Conv layers. — _support:_ limited by buffer bandwidth — _loc:_ Sec. 6.2-6.3
- **2018_Zhu_MISCA_ICCAD#C4** — Versus PRIME on VGG-D, 26.4x speedup and 1.65x energy efficiency; versus Titan X, 4.7-30.94x speedup and 490.4x average energy efficiency. — _support:_ buffer/peripheral designs differ from PRIME — _loc:_ Sec. 6.2, 6.6, Table 3

## Results
- Energy of conv layers falls with crossbar size: AlexNet 1.33/0.82/0.59 mJ and ResNet-18 2.47/1.78/1.52 mJ at 128/256/512
- Speedup vs GPU 4.7-30.94x; VGG weakest because of slow RRAM writes when mapping FC layers
- Average utilization 56.75% -> 91.26%
- 26.4x speedup / 1.65x energy vs PRIME (VGG-D)

## Key numbers
- array_size: mixed; 128/256/512 crossbars evaluated
- energy_eff: 1.2x vs fixed-size; 1.65x vs PRIME; 490.4x vs GPU
- throughput: 2.7x vs fixed-size; 26.4x vs PRIME

## Datasets / benchmarks
ImageNet, AlexNet, VGG-D, ResNet-18, ResNet-34, ResNet-50

## Limitations
- Simulation only (MNSIM); no silicon and no accuracy or noise analysis
- CNNs only; no transformers or dynamic matmuls
- GPU/PRIME comparisons use differing buffers and peripherals, so absolute multipliers are favourable
- Whole-system speedup limited by buffer bandwidth; VGG limited by FC-layer RRAM writes
- Needs multiple crossbar sizes at fabrication, adding design complexity

## Remarks
Attacks the same wasted-cell inefficiency as other mapping works (SemiMap, crossbar-aware pruning) from the crossbar-sizing and overlapped-kernel side, and is a baseline for later allocation frameworks. Large simulation-only multipliers (490x vs GPU) should be read against the chosen baseline configuration. Overlapped kernel mapping is specific to sliding-window convolutions, so it does not carry over directly to transformer MVMs.

## Cites (in collection, 4)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _contrasts/critiques_: "However, the conventional mapping method used in [3] [15] cannot make full use of the computation ability of large crossbars."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _uses-method-or-tool_: "The work frequency of MISCA is set to 100MHz, and the whole system is simulated by MNSIM[17]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "The current RRAM architectures use small crossbars, e.g., 128 x 128 crossbars in ISAAC [13]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "However, the conventional mapping method used in [3] [15] cannot make full use of the computation ability of large crossbars."

## Cited by (in collection, 11)
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _extends/builds-on_: "Besides, since the crossbar size determines the number of crossbars we need for storing the weights, it will also affect the hardware area and energy overhead [24]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "In addition, integrating multiple crossbars with different sizes instead of monolithic design has also been investigated [47]."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "Other dataflow mapping methods could also be applied to improve the parallelism [20]."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _contrasts/critiques_: "Fine-grained WS accelerators demand extra processing but do not resolve light models' utilization [67], [71]."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _background_: "On the one hand, the numbers of rows and columns of the crossbars (the basic computing units in PIM) are always the power of two, e.g., 64, 128, and 256 [36]."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _background_: "Nonetheless, related optimizations such as mixed size crossbars [13] and low-bit ADCs [14] are compatible with this abstract architecture."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _contrasts/critiques_: "Ref. [35] optimizes the resource allocation for different sized crossbars to boost the resource utilization. The solution is heuristically derived and not guaranteed to be optimal."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "By configuring different array sizes for different cores, a mixed-size deployment can be realized [29]."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2018_Zhu_MISCA_ICCAD.pdf](../../05_Mapping_Compilation_and_Dataflow/2018_Zhu_MISCA_ICCAD.pdf)
- Full text: [../fulltext/2018_Zhu_MISCA_ICCAD.txt](../fulltext/2018_Zhu_MISCA_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3240765.3240825
