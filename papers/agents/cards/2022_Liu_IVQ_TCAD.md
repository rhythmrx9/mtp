---
id: W4214834240
key: 2022_Liu_IVQ_TCAD
title: "IVQ: In-Memory Acceleration of DNN Inference Exploiting Varied Quantization"
short: "IVQ"
year: 2022
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 41, no. 12, pp. 5313-5326 (2022)"
authors: "Fangxin Liu, Wenbo Zhao, Zongwu Wang, Yilong Zhao, Tao Yang, Yiran Chen, Li Jiang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["mixed-precision", "bit-slicing", "quantization", "crossbar-architecture", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 18
priority_score: 3.4
doi: "https://doi.org/10.1109/tcad.2022.3156017"
pdf: null
fulltext: null
---

# IVQ

**IVQ: In-Memory Acceleration of DNN Inference Exploiting Varied Quantization** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, vol. 41, no. 12, pp. 5313-5326 (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IVQ reorganizes crossbar-based processing-in-memory to natively support mixed/varied weight-quantization schemes by bit-aligning weights of the same magnitude along a bitline, using a spatial mapping to exempt resulting idle ('hollow') cells and a temporal scheduling scheme to pack bits of different magnitudes onto shared bitlines, achieving up to 91.7x speedup and 541x energy savings over compared baselines.

## Summary
Crossbar-based PIM accelerators are efficient but the weight-stationary crossbar binds each weight's bits to a fixed add-operation position on the bitline, so nonuniform/diverse per-layer or per-channel quantization schemes normally must be 'rolled back' to a uniform format before mapping -- discarding the benefits of mixed quantization. IVQ instead aligns bits of equal magnitude along the same bitline, turning the quantization-diversity problem into a consistency problem; naive application of this leaves many idle ('hollow') cells, so the authors propose a spatial mapping that exempts hollow crossbars from the inter-crossbar data path, plus a temporal scheduling scheme that decouples the intra-crossbar data path from the physical bitline so bits of different magnitudes can still share a bitline over time. A temporal pipeline avoids the stalls this scheduling would otherwise introduce, and a dataflow with corresponding control logic realizes the new intra/inter-crossbar data paths. Evaluated against two PIM baselines (ISAAC, CASCADE), two customized quantization accelerators (ASIC- and FPGA-based), and an NVIDIA RTX 2080 GPU, IVQ reports 19.7x/10.7x/4.7-63.4x/91.7x speedup and 17.7x/5.1x/5.7-68.1x/541x energy savings respectively.

## Contributions
- Identification of a PIM-specific opportunity to exploit varied/mixed quantization schemes rather than rolling them back to a uniform format before crossbar mapping
- A bit-alignment reframing of the quantization-diversity problem as a bitline-consistency problem
- A spatial mapping scheme that exempts 'hollow' (idle-cell) crossbars created by naive bit-alignment from the inter-crossbar data path
- A temporal scheduling scheme decoupling the intra-crossbar data path from the physical bitline, letting differently-scaled bits share bitlines over time, with a pipelined dataflow to avoid stalls
- A full IVQ architecture/dataflow and comparative evaluation against PIM, ASIC/FPGA, and GPU baselines

## Key claims (stable IDs)
- **2022_Liu_IVQ_TCAD#C1** — IVQ achieves substantial speedup over PIM baselines, customized quantization accelerators, and GPUs by natively supporting varied quantization on crossbar PIM. — _support:_ 19.7x, 10.7x, 4.7-63.4x, and 91.7x speedup over ISAAC, CASCADE, ASIC/FPGA quantization accelerators, and an RTX 2080 GPU respectively — _loc:_ Abstract (full text not available)
- **2022_Liu_IVQ_TCAD#C2** — IVQ achieves substantial energy savings over the same set of baselines. — _support:_ 17.7x, 5.1x, 5.7-68.1x, and 541x energy savings over the same four baseline categories respectively — _loc:_ Abstract (full text not available)

## Results
- 19.7x speedup / 17.7x energy savings vs. ISAAC
- 10.7x speedup / 5.1x energy savings vs. CASCADE
- 4.7x-63.4x speedup / 5.7x-68.1x energy savings vs. customized ASIC/FPGA quantization accelerators
- 91.7x speedup / 541x energy savings vs. NVIDIA RTX 2080 GPU

## Limitations
- Analysis is abstract-only (full text not accessible from this machine; only IEEE Xplore hosts a PDF) -- the specific benchmarks, quantization schemes, and crossbar configuration underlying the reported multipliers are not verifiable here
- As with most ReRAM PIM architecture papers of this kind, results are expected to be simulation-based rather than measured silicon, though this could not be confirmed from the abstract alone
- The very large top-end multipliers (e.g., 541x energy savings vs. GPU) likely reflect a favorable workload/precision regime for mixed quantization; abstract does not specify which network(s)/datasets produce the top-end numbers versus the lower end of the ranges

## Remarks
A natural companion to the same group's Bit-Transformer (bit-level sparsity) and D-NAT-adjacent quantization-aware training work: IVQ tackles the orthogonal problem of making crossbar PIM hardware itself flexible enough to exploit non-uniform quantization schemes without forcing algorithms back to a uniform format. The idea of decoupling the logical (per-magnitude) bit layout from the physical bitline via spatial+temporal scheduling is architecturally interesting and specific to the weight-stationary nature of crossbar PIM; because only the abstract was available, the practical overhead of the added control logic and pipeline, and how the reported speedups vary across real DNN benchmarks, could not be assessed here.

## Cites (in collection, 10)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021)
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2022_Liu_IVQ_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2022.3156017
