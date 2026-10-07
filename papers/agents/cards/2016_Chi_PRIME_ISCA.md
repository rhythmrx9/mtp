---
id: W4254672563
key: 2016_Chi_PRIME_ISCA
title: "PRIME: A Novel Processing-in-Memory Architecture for Neural Network Computation in ReRAM-Based Main Memory"
short: "PRIME"
year: 2016
venue: "ISCA"
venue_full: "ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA 2016)"
authors: "Ping Chi, Shuangchen Li, Cong Xu, Tao Zhang, Jishen Zhao, Yongpan Liu, Yu Wang, Yuan Xie"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["MLP", "CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "analog-mvm", "weight-mapping", "tiling-partitioning", "bit-slicing", "adc-dac", "peripheral-circuits", "compiler-software-stack"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 113
cites_in_collection: 2
citations_overall: 570
priority_score: 11.09
doi: "https://doi.org/10.1109/isca.2016.13"
pdf: "../../03_Crossbar_Accelerator_Architectures/2016_Chi_PRIME_ISCA.pdf"
fulltext: "../fulltext/2016_Chi_PRIME_ISCA.txt"
---

# PRIME

**PRIME: A Novel Processing-in-Memory Architecture for Neural Network Computation in ReRAM-Based Main Memory** — ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA 2016) (2016)

## TL;DR
PRIME turns part of a ReRAM main memory (full-function subarrays) into morphable NN accelerators, reporting ~2360x speedup and ~895x energy saving over a CPU+NPU co-processor baseline (abstract) with 5.76% area overhead.

## Summary
Memory-wall costs motivate processing-in-memory; ReRAM crossbars compute matrix-vector products natively and are candidates for main memory. PRIME divides each ReRAM bank into Mem subarrays, full-function (FF) subarrays that switch between memory and NN-compute mode, and Buffer subarrays (the memory subarrays adjacent to the FF ones) that hide data movement (Sec. III, Fig. 4). The FF subarray reuses write drivers as DACs (multi-level voltage sources) and sense amplifiers as ADCs (a Po-bit, Po<=8, reconfigurable SA), adds subtraction (positive/negative weight matrices in a crossbar pair), sigmoid and max-pool support. Because cells are 4-bit MLC and inputs 3-bit, a composing scheme builds 6-bit inputs from two 3-bit signals and 8-bit weights from two 4-bit cells, with 6-bit outputs, and the partial results are summed (Sec. III-D). A software/hardware interface (Map Topology, Program Weight, Config Datapath, Run, Post Proc) maps small NNs by replication, medium NNs by splitting across mats (e.g. 512x512 over four 256x256 mats), and large NNs across banks/chips (Sec. IV, Fig. 7). Trace-based simulation with modified NVSim/CACTI compares against CPU-only, a parallel NPU co-processor and a 3D-stacked PIM NPU on MlBench (CNN-1/2, MLP-S/M/L on MNIST and VGG-D on ImageNet), assuming training is done offline.

## Contributions
- Morphable ReRAM main-memory architecture where FF subarrays serve as NN accelerator or normal memory.
- Circuit and microarchitecture designs that reuse peripherals (SA as ADC, write driver as DAC) to keep area overhead low.
- Input and synapse composing scheme to reach 6-bit input / 8-bit weight precision from 3-bit inputs and 4-bit cells.
- Software/hardware interface and compile-time mapping with replication and inter-bank communication for large NNs.

## Key claims (stable IDs)
- **2016_Chi_PRIME_ISCA#C1** — PRIME greatly improves performance and energy for NN inference over a CPU+NPU baseline. — _support:_ ~2360x speedup, ~895x energy saving (abstract) — _loc:_ Abstract, Sec. V, Figs. 8, 10
- **2016_Chi_PRIME_ISCA#C2** — Placing the NPU in memory helps, but ReRAM-based in-situ compute helps more. — _support:_ pNPU-pim gives 9.1x speedup on average over pNPU-co; PRIME is about 4.1x faster than pNPU-pim-x64 — _loc:_ Sec. V, Fig. 8
- **2016_Chi_PRIME_ISCA#C3** — The morphable design costs little area. — _support:_ 5.76% overhead with 2 FF + 1 Buffer subarray per bank; computation support adds ~60% area to an FF mat (driver 23%, subtraction+sigmoid 29%) — _loc:_ Sec. V area, Fig. 12
- **2016_Chi_PRIME_ISCA#C4** — Low-precision ReRAM is adequate for NN inference. — _support:_ LeNet-5/MNIST: 3-bit dynamic fixed-point inputs and weights suffice for 99% accuracy — _loc:_ Sec. III-D, Fig. 6

## Results
- PRIME speedup is smaller on VGG-D because mapping across 8 chips needs costly inter-bank/chip communication.
- pNPU-pim-x64 saves 93.9% memory energy on average vs pNPU-co; PRIME reduces computation, buffer and memory energy further (Fig. 11).
- FF subarray utilisation 39.8% before and 75.9% after replication on MlBench (excluding VGG-D); 53.9% / 73.6% for VGG-D.
- Largest NN mappable on the whole PRIME system ~2.7x10^8 synapses vs TrueNorth 1.4x10^7.

## Key numbers
- tech_node: 65nm CMOS (NPU models); ReRAM Pt/TiO2-x/Pt Ron/Roff 1k/20k ohm, 2V SET/RESET
- array_size: 256x256 per mat, 4-bit MLC
- energy_eff: ~895x energy saving vs CPU+NPU (abstract)
- throughput: ~2360x speedup (abstract)
- accuracy: 99% on MNIST LeNet-5 with 3-bit inputs/weights
- bits_weight: 8b (two 4-bit cells)
- bits_adc: 6b (reconfigurable SA, Po<=8)

## Datasets / benchmarks
MNIST, ImageNet (VGG-D), MlBench

## Limitations
- Simulation only with a trace-based in-house simulator; no fabricated ReRAM chip.
- Programming (configuration) latency and energy are excluded from results, assuming NNs run tens of thousands of times.
- Ideal analog behaviour: no device variation, IR drop or noise modelling beyond a 6-bit output precision assumption; training is offline.
- Weak CPU/NPU baselines make headline numbers an upper bound; LRN needs the CPU.
- Only MLP/CNN workloads; no transformers or language models.

## Remarks
PRIME and ISAAC (same ISCA 2016) started the ReRAM-crossbar accelerator field; PRIME's distinctive idea is morphable memory/compute subarrays within main memory. Its composing scheme (low-precision cells and input slices combined digitally) is an early form of the bit-slicing now standard in crossbar mapping and ADC-resolution discussions. For mapping modern models it is a conceptual baseline only: no non-idealities, and the large-NN reprogramming problem it identifies is the same weight-capacity issue faced by transformers today.

## Cites (in collection, 2)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Most prior work exploits ReRAM either as DRAM/ﬂash replacement [20], [28], [40] or as synapses for NN computation [10], [11], [12], [13], [38]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Recently, a full-ﬂedged NN accelerator design based on ReRAM crossbars have been proposed, named ISAAC [39]."

## Cited by (in collection, 113)
- [2018_Kim_NonlinearIVAwareDNN_JETC](2018_Kim_NonlinearIVAwareDNN_JETC.md) Nonlinear-IV NN (2018) — _background_: "Since this approach can be several orders of magnitude more efficient than CMOS ASIC approaches in terms of both speed and power [3-6], many studies proposed neural network accelerators based on emerging NVM crossbar array [9-12]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Recent works [1] demonstrated that ReRAM-based PIM oﬀer great acceleration of CNNs with low energy cost."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "This characteristic avoids the high-writing-cost problem [6] and the endurance limitation [16] of memristor devices."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _background_: "PRIME is a new pipelined architecture and a method of efficiently processing neural network inference with analog weights. PRIME provides an energy advantage of three orders of magnitude [10]."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _contrasts/critiques_: "Recently, architectural simulator platforms (e.g., PRIME [118], ISAAC [119], and Harmonica [120]) have been developed to support system-level design of neuromorphic accelerators, however they have limited considerations at the aforementioned nonideal device properties (i.e., they only considered the weight precision and/or variation)."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _extends/builds-on_: "To achieve a smaller energy-hardware cost, this work proposes a hardware-driven binary-input ternary-weighted (BITW) network using our pseudo-binary nvCIM macros and a two-macro (nvCIM-P and nvCIM-N) DNN structure [5]: the nvCIM–P macro stores positive weights while the nvCIM-N stores negative weights."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "Without loss of generality, we focus on four of these recent proposals in the rest of this paper: 1) the Memristive Boltzmann Machine (MBM) [1], 2) ISAAC [9], 3) PRIME [10], and 4) PipeLayer [11]."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _background_: "It can achieve extremely throughput compared to the fully-folded mapping that reuses all the neurons and weights [1] cycle by cycle, however, this scheme consumes significantly huge crossbar resources."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _contrasts/critiques_: "The non-ideal circuit and device properties that cause the current sensing errors are usually ignored in prior system-level work [3, 9]."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _contrasts/critiques_: "However, the conventional mapping method used in [3] [15] cannot make full use of the computation ability of large crossbars."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _baseline/comparison_: "Specifically, it fully reuses the crossbar cycle by cycle for completing the Conv operations across many sliding windows [6]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "Resistive crossbar based specialized hardware systems have been proposed for accelerating DNN inference [7–11] and training [12, 13]."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _baseline/comparison_: "With the advantages of efficient in-memory computing ability, previous work has proposed several ReRAM-based Computing Systems, like PRIME [2] and ISAAC [3]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Several architectures have been proposed, both digital [20, 21, 36, 61, 72, 89] and mixed digital-analog using memristor crossbars [22, 23, 73, 95, 100]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _background_: "ACM ISBN 978-1-4503-6725-7/19/06. . . $15.00 https://doi.org/10.1145/3316781.3317870 promising candidates as the basic computing unit for neural network accelerator design [5, 7]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _contrasts/critiques_: "In addition, some RRAM-based accelerators utilize the multi-bit RRAM devices which have more than two stable resistance states, to achieve higher storage and computation density, such as PRIME [3] and PipeLayer [16] with 4-bit RRAM."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _background_: "ISAAC [2] and PRIME [11] exploit analog characteristics of non-volatile memory to support matrix multiplication in memory."
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019) — _background_: "To ensure a relatively high accuracy, usually two (or more) memristors are bundled to represent weights with high resolution (more bits) [39]."
- [2019_Angizi_AnalogVsDigitalPIM_ISVLSI](2019_Angizi_AnalogVsDigitalPIM_ISVLSI.md) Analog vs Digital PIM (2019) — _background_: "More importantly, its currentmode weighted summation operation intrinsically matches the dominant Multiplication-and-Accumulation (MAC) in the artificial neural network, making it one of the most promising candidates as the basic computing unit for neural network accelerator design [6]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _baseline/comparison_: "PRIME [12] uses sense amplifiers (SAs) instead of conventional ADCs to reduce area."
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020) — _background_: "Because PIM architectures have the ability to complete the CNN computing in memory by converting convolution operations into analog-domain Matrix-VectorMultiplications (MVMs), data movements are greatly reduced and energy efficiency can be enhanced by over 100× compared with CMOS-based architectures [1]."
- [2020_Zhang_RepresentableMatrices_ASPDAC](2020_Zhang_RepresentableMatrices_ASPDAC.md) Representable Matrices (2020) — _background_: "Moreover, the use of MCAs allow matrices to be stored in-place, which reduces data fetching and communication costs that fundamentally bounds the performance of any computing system that processes large amounts of data [8, 2, 9]."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "Here, we review the two types of ADCs most commonly used by crossbar accelerators: the ramp ADC, as used in Ref. 62 and PRIME,136 and the SAR ADC, as used in ISAAC,68 PUMA,148 and the memristive Boltzmann machine.12"
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _baseline/comparison_: "However, the energy efficiency of R2 PIM accelerators (such as PRIME [14], ISAAC [58], and PipeLayer [62]) is still limited due to two bottlenecks (see Fig. 1 (b)): (1) although the weights are kept stationary in memory, the energy cost of data movements due to inputs and Psums is still large (as high as 83% in PRIME [14])"
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _background_: "With these merits, the ReRAM-based neural network accelerator has been widely studied and is proved to be a promising alternative to Von-Neumann architecture [2] [3] for this type of application."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _background_: "PRIME [4] and ISAAC [24] designs utilize ReRAM to accelerate the inference of CNNs."
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020) — _background_: "Among various platforms of PIM, ReRAM is widely regarded as a proper platform for PIM with its intrinsic characteristic of matrix-vector multiplication [2, 11, 18]."
- [2020_Guo_ATT_ICCD](2020_Guo_ATT_ICCD.md) ATT (2020) — _background_: "Processing-in-Memory (PIM) platforms are more and more popular in accelerating neural network applications due to fewer data movements compared to FPGA and ASIC implementations [1–3]."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _background_: "Recent works present several NN accelerators based on ReRAM crossbars, such as PRIME [4], ISAAC [5], and PipeLayer [6]."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _background_: "Previous work, such as PRIME [21] and ISAAC [22], leverages in-situ computation to avoid the tremendous cost of data movement and efficiently compute multiply-accumulate operations, the most intensive computation in DNNs."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _contrasts/critiques_: "A similar approach is used in other works [10], [35]-[37] where the in-memory accelerator exposes an API."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _contrasts/critiques_: "The general way is to use two ReRAM crossbars to hold the positive and negative magnitudes weights separately, doubling the ReRAM portion of hardware cost [17, 25-28]."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "Around the same time, the architecture of PRIME was introduced [35]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "A commonly adopted programming paradigm [12, 35] provides application programming interface (API) functions to improve the programmability of such architectures."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _contrasts/critiques_: "For example, PRIME [16] and PipeLayer [17] adopt 1-bit SAs and IF neurons to successively perform 2n conversions to produce an n-bit output."
- [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) Area-Efficient Multi-Task BERT (2021) — _background_: "The ReRAM-based accelerators [3], [20], [27] are proposed to solve the data communication issue by adopting in-memory computation."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _background_: "A certain number of ReRAM crossbar-based DNN accelerator designs are built in prior works, such as ISAAC [9], PRIME [4], PipeLayer [10], and CASCADE [6]."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _background_: "Consequently, MCAs have been aggressively harnessed for energy-efficient DNN acceleration [2, 4, 22]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _contrasts/critiques_: "Chi et al. [10] propose PRIME, a morphable PIM structure for ReRAM based main memory with carefully designed peripheral circuits that allow arrays to be used as memory, scratchpads, and dot product engines for CNN workloads."
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022) — _background_: "The overhead of ADCs also increase as their resolution increases so that ADCs significantly degrade area and energy efficiency of CIM accelerators [2, 15, 20]."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _contrasts/critiques_: "Prior PIM-based designs [9], [10], [42], [48] have been built upon the WS dataflow, especially by unrolling the weight values."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _background_: "Therefore, PIM-based NN accelerators can improve the energy efficiency of NN computing by two to three orders of magnitude over GPU and CMOS ASIC solutions [3-7]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _contrasts/critiques_: "Alternatively, other designs use efficient lower-resolution ADCs to process high-resolution analog values from crossbars [5, 7, 24]. We call these designs Sum-Fidelity-Limited as the resolution difference reduces output fidelity and introduces error."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "PRIME [3] provides a novel micro-architecture and circuit design for the ReRAM-based DNN PIM accelerator."
- [2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC](2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.md) Reconfigurable Sparse-Attention NVPIM (2023) — _background_: "We select ReRAM as our target device because of its high density and energy efficiency, as shown in previous designs for other neural networks [8, 9]."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _contrasts/critiques_: "PRIME [7] duplicates the crossbars twice to hide data access latency with a ping-pong mode. The strategy is rough and cannot fully utilize the resources."
- [2023_Pelke_MultiCoreCNNMapping_VLSI-SoC](2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.md) Multi-core RRAM CNN Mapping (2023) — _background_: "RRAM-based CIM architectures Several RRAM-based CIM architectures have been presented [6-8, 18]."
- [2023_Jang_VECOM_ICCAD](2023_Jang_VECOM_ICCAD.md) VECOM (2023) — _background_: "Processing-In Memory (PIM) architecture, utilizing Resistive Random Access Memory (ReRAM), offers a promising solution to address the limitations of conventional von Neumann architecture [1-3]."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _background_: "Thus, SRAM-based CIM supports flexible data read and write updates on CIM memory [6], while ReRAM-based CIM usually assumes that weights are frozen in the crossbar, avoiding the penalty of frequent writes [13, 39]."
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _contrasts/critiques_: "They assume that it is possible to activate all the rows and columns of a 128 × 128 or 256 × 256 array simultaneously within a single clock cycle without impacting computational accuracy[4, 5]."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "CiM can reduce energy costs by computing directly within the memory arrays [29], which we define as two-dimensional grids of interconnected memory cells (e.g., SRAM bitcells or RRAM devices)."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _contrasts/critiques_: "While the PRIME [22] and PipeLayer [23] approaches eliminate the need for ADCs, their input or output circuits still contain numerous capacitors, which consume a significant amount of chip area."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _background_: "A few proposals use double (i.e., positive/negative) crossbar arrays [6, 8] to process signed operands."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "Similarly, a signed weight may need two crossbar arrays to store the positive and negative parts separately [6]."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "Prior researches [1, 3, 5, 8, 9, 15, 23, 25-27, 32, 37, 38, 41, 47] have proposed various CIM accelerators, providing robust support for high-performance computing and naturally aligning with large-scale parallel computing applications such as DNN inference."
- [2024_Yu_AESHA_ICCAD](2024_Yu_AESHA_ICCAD.md) AESHA (2024) — _uses-method-or-tool_: "The read and write pulse times of the RRAM cells are taken from [38], whereas the on/off resistances of RRAM cells with the 4-bit cell precision [39] are extracted from [26]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "PRIME [11] introduces a reconfigurable RRAM PIM architecture, where the same PIM hardware can be configured as both regular memory and computing elements."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _background_: "The initial works on analog CIM based accelerators focused on convolutional and fully connected networks [30, 51-53]."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _background_: "Some PIM architectures such as ISAAC [43], W2W-PIM [31], PRIME [6], and RENO [35] use ReRAM crossbar memory arrays to perform analog data computations."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019)
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)
- [2020_Ji_FPSAReducedArchitecture_TC](2020_Ji_FPSAReducedArchitecture_TC.md) FPSA Reduced Architecture (2020)
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2020_Jiang_MINT_ISCAS](2020_Jiang_MINT_ISCAS.md) MINT (2020)
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020)
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020)
- [2021_Li_RaQu_TCAD](2021_Li_RaQu_TCAD.md) RaQu (2021)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2022_Chen_WRAP_DATE](2022_Chen_WRAP_DATE.md) WRAP (2022)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022)
- [2022_Wen_RRAMReadDisturb_DFT](2022_Wen_RRAMReadDisturb_DFT.md) RRAM Read Disturb (2022)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022)
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2023_Cui_ARES_ICCAD](2023_Cui_ARES_ICCAD.md) ARES (2023)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2025_Li_CIMLLMDataflow_ISVLSI](2025_Li_CIMLLMDataflow_ISVLSI.md) CIM-LLM Dataflow (2025)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)
- [2025_Xiong_ASMA_ICCD](2025_Xiong_ASMA_ICCD.md) ASMA (2025)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2016_Chi_PRIME_ISCA.pdf](../../03_Crossbar_Accelerator_Architectures/2016_Chi_PRIME_ISCA.pdf)
- Full text: [../fulltext/2016_Chi_PRIME_ISCA.txt](../fulltext/2016_Chi_PRIME_ISCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isca.2016.13
