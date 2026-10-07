---
id: W3005619596
key: 2019_Peng_DNNNeuroSim_IEDM
title: "DNN+NeuroSim: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators with Versatile Device Technologies"
short: "DNN+NeuroSim V1.0"
year: 2019
venue: "IEDM"
venue_full: "IEEE International Electron Devices Meeting (IEDM 2019)"
authors: "Xiaochen Peng, Shanshi Huang, Yandong Luo, Xiaoyu Sun, Shimeng Yu"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["SRAM-digital", "ReRAM", "PCM", "FeFET", "ECRAM", "MRAM"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "benchmarking", "adc-dac", "conductance-drift", "tiling-partitioning", "energy-efficiency", "peripheral-circuits", "quantization"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 40
cites_in_collection: 0
citations_overall: 361
priority_score: 9.12
doi: "https://doi.org/10.1109/iedm19573.2019.8993491"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2019_Peng_DNNNeuroSim_IEDM.pdf"
fulltext: "../fulltext/2019_Peng_DNNNeuroSim_IEDM.txt"
---

# DNN+NeuroSim V1.0

**DNN+NeuroSim: An End-to-End Benchmarking Framework for Compute-in-Memory Accelerators with Versatile Device Technologies** — IEEE International Electron Devices Meeting (IEDM 2019) (2019)

## TL;DR
Introduces DNN+NeuroSim, an open-source Python/PyTorch-TensorFlow wrapper around the NeuroSim macro model that benchmarks CIM accelerators (SRAM, RRAM, PCM, FeFET, ECRAM) for accuracy, area, energy and throughput, finding high on-state resistance (>100 kOhm) the key to efficiency.

## Summary
Earlier MLP+NeuroSim (IEDM 2017) handled only a 2-layer MLP on MNIST at array level. DNN+NeuroSim adds chip-level peripherals (buffers, H-tree interconnect, pooling/accumulation/activation units) and supports VGG/ResNet on CIFAR/ImageNet. The Python wrapper trains with low-precision WAGE-style quantisation, with weight precision limited by device levels and partial-sum quantisation limited by ADC precision, and applies a retention/drift model at inference. NeuroSim automatically floorplans the network layer by layer onto a chip/tile/PE/synaptic-array hierarchy, uses weight duplication to raise memory utilisation, and takes real traces of weights and activations to compute area, latency, dynamic energy, leakage, TOPS/W and throughput; circuit modules are SPICE-calibrated with PTM models. Evaluation uses VGG-8/CIFAR-10 at 8-bit weights/activations: drift scenarios, ADC precision (3-5 bit) versus array size (64x64 to 256x256) and cell precision (1/2/4 b), then cross-device benchmarking (SRAM at 7 nm and 32 nm, NVMs at 32 nm). A FeFET ResNet-18/ImageNet case compares real-trace, pseudo-trace and average-activity simulation modes.

## Contributions
- End-to-end hierarchical CIM inference benchmarking framework from device to algorithm level
- Python wrapper interfacing NeuroSim with PyTorch and TensorFlow, with automatic algorithm-to-hardware mapping
- Analysis of conductance drift and ADC quantisation effects on accuracy
- Cross-technology benchmark (SRAM, RRAM, PCM, FeFET, ECRAM) showing the benefit of high on-state resistance
- Open-source release (DNN_NeuroSim_V1.0)

## Key claims (stable IDs)
- **2019_Peng_DNNNeuroSim_IEDM#C1** — With 1-bit cells, a 4-bit ADC suffices for ~89% VGG-8/CIFAR-10 accuracy at 64x64 and 128x128 arrays; multi-bit cells need 5-bit ADC — _support:_ Fig. 4 — _loc:_ Sec. III-B
- **2019_Peng_DNNNeuroSim_IEDM#C2** — Larger arrays shrink chip area but reduce throughput and energy efficiency; 128x128 with 5-bit ADC is a balanced design — _support:_ Fig. 5 radar plot — _loc:_ Sec. III-B
- **2019_Peng_DNNNeuroSim_IEDM#C3** — Large Ron (>100 kOhm) analog synapses at 32 nm can beat parallel-readout SRAM at 7 nm in TOPS/W — _support:_ Table 1 — _loc:_ Sec. III-C
- **2019_Peng_DNNNeuroSim_IEDM#C4** — Real-trace simulation is most accurate; pseudo-trace and average-activity modes underestimate performance — _support:_ Fig. 7, FeFET ResNet-18 ImageNet — _loc:_ Sec. IV
- **2019_Peng_DNNNeuroSim_IEDM#C5** — Random conductance drift preserves accuracy best over 10 years (2% equivalent drift) — _support:_ Fig. 3 — _loc:_ Sec. III-A

## Results
- VGG-8/CIFAR-10 at 8b weights/activations is the benchmark workload (Table 1, Figs. 3-6)
- Conventional RRAM or PCM with a few kOhm to tens of kOhm Ron is not competitive because transistors must be upsized, increasing area and latency
- Drift toward maximum or minimum conductance degrades accuracy faster than drift toward intermediate states (Fig. 3)
- Higher ADC precision hurts area and energy efficiency while higher cell precision helps by saving peripherals (Fig. 6)

## Key numbers
- tech_node: 7nm and 32nm (SRAM); 32nm (NVM)
- array_size: 64x64 to 256x256 (128x128 chosen)
- accuracy: ~89% VGG-8 CIFAR-10 (1-bit cell, 4-bit ADC, 64x64/128x128)
- bits_weight: 8b (algorithm), 1/2/4 b per cell
- bits_adc: 3-5b

## Datasets / benchmarks
CIFAR-10, ImageNet

## Limitations
- Inference only, offline training; on-chip training version only announced as under development
- Drift scenarios are assumed because analog retention data is scarce
- Device parameters taken from literature and NVM nodes assumed at 32 nm
- No transformers or language models; no read noise or IR-drop modelling beyond SPICE-calibrated circuit estimates
- Short conference paper with limited numerical detail in text (results largely in figures and Table 1)

## Remarks
The foundational benchmarking tool behind many later CIM papers (cited for area/energy evaluation in e.g. KD+RSA). Its value is the hierarchical hardware model and ADC/array-size trade-off analysis rather than accuracy modelling of noise. For LM-on-analog studies, V1.0 lacks attention and non-MVM operators, so later versions or other simulators are needed.

## Cited by (in collection, 40)
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020) — _uses-method-or-tool_: "To evaluate the hardware efficiency of the proposed method, we use NeuroSim [27], an architectural analysis tool for evaluating the area cost of the main model and the additional on-chip memory."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _uses-method-or-tool_: "We simulate the ReRAM circuit parameters using NeuroSim [22] based on the ReRAM and peripheral configurations [23] shown in Table 1(b)."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _extends/builds-on_: "As what has been proposed in prior framework V1.0 [7], the NeuroSim core is wrapped by python library, to support flexible network topologies, the default model is VGG-8 for CIFAR-10 based on low precision training method WAGE [9]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _uses-method-or-tool_: "We use NeruoSim [51] along with the 32 nm technology node parameters to evaluate the hardware area, execution time, and energy consumption."
- [2022_Kim_FeTFTSynapticCIM_SciAdv](2022_Kim_FeTFTSynapticCIM_SciAdv.md) FeTFT Synaptic CIM (2022) — _data/numbers_: "For an efficient CIM array, Gmax needs to be lower than 10 μS (12, 56)."
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022) — _uses-method-or-tool_: "We use NeuroSim [12], a benchmark framework of CIM accelerators, to measure the area and energy efficiency of CIM accelerators."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _uses-method-or-tool_: "For the evaluation, a customized simulator was implemented based on our circuit simulation results and NeuroSim+ [38], [39]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _baseline/comparison_: "Some aspects of our AIMC crossbar model have been investigated individually in earlier studies, such as the effect of ADC/DAC quantization, IR-drop, and general read noise55–57, as well as data-dependent long-term noise38."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _baseline/comparison_: "The toolkits are compared against five key dimensions: ML library, supported network types, on-chip inference capabilities, on-chip training, and on-chip inference."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _baseline/comparison_: "Modeling Work Architecture Flexibility Circuit Flexibility Energy Accuracy Model Speed NeuroSim [3–6] MNSim [7, 8] Timeloop [9–14] This Work"
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _uses-method-or-tool_: "We simulate the RRAM-CIM and SRAM-CIM macros using the peripheral setups under 32nm node technology in NeuroSim [37]."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _motivation_: "First, input and output activations on CIM devices have to be quantized into lower precision compared with digital cores due to the energy and area constraints of high-resolution Analog/Digital converters [2], [26]."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "Accelergy is basically a wrapper, providing a single interface to established energy estimation tools, including CACTI [23] and NeuroSim [30]."
- [2025_Zhang_ASiM_TVLSI](2025_Zhang_ASiM_TVLSI.md) ASiM (2025) — _contrasts/critiques_: "NeuroSim [14, 31] quantizes ADC outputs based on the Min-Max range of MAC results, which leads to overly optimistic estimations of ADC rounding effects and the corresponding impact of analog noise."
- [2025_Fu_CrossTypeMappedDataflow_ISLPED](2025_Fu_CrossTypeMappedDataflow_ISLPED.md) Cross-Type Mapped Dataflow (2025) — _uses-method-or-tool_: "Digital CIM data is from [21] and scaled to 22nm via [25] while analog CIM data is extracted from NeuroSim v1.3 [26]."
- [2026_Wu_HaLoRA_TODAES](2026_Wu_HaLoRA_TODAES.md) HaLoRA (2026) — _uses-method-or-tool_: "Additionally, following the block-wise linear mapping characteristics of weights on physical RRAM crossbars [50], we partitioned the corresponding weights into 64×64 blocks to align with conventional memory tile dimensions."
- [2025_Malhotra_ReTern_TVLSI](2025_Malhotra_ReTern_TVLSI.md) ReTern (2025) — _uses-method-or-tool_: "To estimate the energy, latency, and area of the TCiM array peripherals including the row decoder, flash ADC, and subtractor as well as the additional multiplexers (MUXes) and register required for ReTern, we use NeuroSim [42]."
- [2024_Qin_RoCR_ICCAD](2024_Qin_RoCR_ICCAD.md) RoCR (2024) — _data/numbers_: "Given the same amount of documents, CiM can finish computation within 50ms [15], which is negligible compared to the computation latency on normal edge devices."
- [2026_Zheng_InterfaceKVQ_ICCAD](2026_Zheng_InterfaceKVQ_ICCAD.md) InterfaceKVQ (2026) — _uses-method-or-tool_: "Hardware energy and area are computed with a NeuroSim-based model [17] at 22nm; per-component constants appear in Section 4.3, with only the DAC constants as negligible literature placeholders."
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022)
- [2022_GarciaRedondo_SACA_DCIS](2022_GarciaRedondo_SACA_DCIS.md) SACA (2022)
- [2022_Jiang_ENNA_TCAS-I](2022_Jiang_ENNA_TCAS-I.md) ENNA (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Ye_WH2T1RRRAMCIM_JSSC](2023_Ye_WH2T1RRRAMCIM_JSSC.md) WH-2T1R RRAM CIM Macro (2023)
- [2023_Bai_CIMQ_TCAD](2023_Bai_CIMQ_TCAD.md) CIMQ (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED](2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.md) ADC-Less CiM Partial-Sum Quant (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Huang_VQTCiM_DAC](2025_Huang_VQTCiM_DAC.md) VQT-CiM (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)
- [2025_Sun_DuoPIM_TCAD](2025_Sun_DuoPIM_TCAD.md) DuoPIM (2025)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2019_Peng_DNNNeuroSim_IEDM.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2019_Peng_DNNNeuroSim_IEDM.pdf)
- Full text: [../fulltext/2019_Peng_DNNNeuroSim_IEDM.txt](../fulltext/2019_Peng_DNNNeuroSim_IEDM.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iedm19573.2019.8993491
