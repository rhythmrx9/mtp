---
id: W2613989746
key: 2017_Song_PipeLayer_HPCA
title: "PipeLayer: A Pipelined ReRAM-Based Accelerator for Deep Learning"
short: "PipeLayer"
year: 2017
venue: "HPCA"
venue_full: "2017 IEEE International Symposium on High Performance Computer Architecture (HPCA)"
authors: "Linghao Song, Xuehai Qian, Hai Helen Li, Yiran Chen"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["MLP", "CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "dataflow-pipelining", "on-chip-training", "weight-mapping", "tiling-partitioning", "adc-dac", "bit-slicing", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 90
cites_in_collection: 2
citations_overall: 841
priority_score: 10.91
doi: "https://doi.org/10.1109/hpca.2017.55"
pdf: "../../03_Crossbar_Accelerator_Architectures/2017_Song_PipeLayer_HPCA.pdf"
fulltext: "../fulltext/2017_Song_PipeLayer_HPCA.txt"
---

# PipeLayer

**PipeLayer: A Pipelined ReRAM-Based Accelerator for Deep Learning** — 2017 IEEE International Symposium on High Performance Computer Architecture (HPCA) (2017)

## TL;DR
PipeLayer is a simulated ReRAM PIM accelerator that supports both CNN training and inference via intra-/inter-layer pipelining and weight replication (parallelism granularity), reporting 42.45x average speedup and 7.17x energy saving over a GTX 1080 GPU.

## Summary
PRIME and ISAAC accelerate only CNN inference; ISAAC's very deep pipeline stalls in training because batches (e.g., 64) must wait for weight updates. PipeLayer partitions ReRAM main memory into morphable subarrays (compute or store) and memory subarrays (intermediate data). A kernel is mapped to one bit line, so a 1152x256 matrix is split into 18 matrices of 128x128 arrays with outputs summed; a parallelism granularity G duplicates arrays to cut the 12,544 cycles needed for a conv layer. A layer-wise pipeline lets a new input enter every cycle within a batch and handles training dependencies (forward, error back-propagation, partial derivatives, weight update written back into ReRAM). Inputs use a weighted spike scheme (no DACs) and an Integration-and-Fire circuit with counters replaces ADCs. 16-bit resolution is built from four 4-bit cell groups with shift-and-add. A NVSim-based simulator (29.31/50.88 ns and 1.08 pJ/3.91 nJ read/write per spike) evaluates 4 MNIST networks plus AlexNet and VGG-A to E against GTX 1080 running Caffe.

## Contributions
- First ReRAM PIM accelerator supporting both training and testing of CNNs
- Pipeline for training that avoids ISAAC-style bubbles, plus parallelism-granularity weight replication
- Spike-based input and integrate-and-fire output eliminating DAC and ADC
- Resolution-compensation scheme using four 4-bit arrays for 16-bit weights and a layer-wise programming API

## Key claims (stable IDs)
- **2017_Song_PipeLayer_HPCA#C1** — Pipelined PipeLayer achieves geometric-mean 42.45x speedup over GTX 1080 (testing); 53.22x training, 33.85x overall (as reported) — _support:_ highest speedup 146.58x pipelined vs 20.81x non-pipelined — _loc:_ Sec. 6.3, Fig. 15
- **2017_Song_PipeLayer_HPCA#C2** — Average energy saving over GPU is 7.17x — _support:_ 6.52x training, 7.88x testing; maxima 27.03x (Mnist-C train), 70.03x (Mnist-A test) — _loc:_ Sec. 6.4, Fig. 16
- **2017_Song_PipeLayer_HPCA#C3** — Higher computational efficiency but lower power efficiency than ISAAC/DaDianNao — _support:_ 1485 GOPS/s/mm2 vs 479.0 (ISAAC) and 63.46 (DaDianNao); 142.9 GOPS/s/W vs 380.7 and 286.4 — _loc:_ Sec. 6.6
- **2017_Song_PipeLayer_HPCA#C4** — CNN accuracy is more sensitive to cell resolution than MLPs — _support:_ MLPs fine at 4b; M-C and C-4 drop sharply from 3b, C-4 normalised accuracy ~0.2 at 4b — _loc:_ Fig. 13

## Results
- 42.45x speedup (pipelined) over GTX 1080 on average; up to 146.58x
- 7.17x average energy saving; 6.52x training and 7.88x testing
- Area 82.63 mm2; 1485 GOPS/s/mm2 vs ISAAC 479.0 and DaDianNao 63.46; 142.9 GOPS/s/W vs ISAAC 380.7
- Default 16-bit precision with 4-bit ReRAM cells

## Key numbers
- array_size: 128x128
- energy_eff: 142.9 GOPS/s/W; 7.17x energy saving vs GPU
- throughput: 1485 GOPS/s/mm2; 42.45x speedup vs GTX 1080
- bits_weight: 16b (four 4b cells)
- bits_adc: ADC-free (integrate-and-fire + counter)

## Datasets / benchmarks
MNIST, ImageNet (AlexNet, VGG-A to E)

## Limitations
- Architecture-level simulation (NVSim-based), no silicon; device non-idealities, noise and write endurance during training are not modelled
- Only CNNs/MLPs (MNIST, ImageNet-scale VGG/AlexNet); no accuracy results for full-scale training under analog noise
- Resolution study shows 4-bit cells poorly support CNNs without multiple arrays
- Lower power efficiency than ISAAC because intermediate data are written to ReRAM instead of eDRAM; frequent ReRAM writes raise endurance concerns
- Abstract headline 42.45x matches the paper's testing geometric mean in Sec. 6.3 while overall is 33.85x

## Remarks
Foundational early architecture paper for in-ReRAM training and a standard comparison point after PRIME and ISAAC. Its mapping (kernel-per-bitline, 128x128 tiles, replication granularity G) is a recurring template in later mapping work. Evidence is simulation-only and ignores device noise and write endurance, so it says little about modern transformer/LM mapping, but the training-pipeline hazards it identifies are relevant to on-chip adaptation.

## Cites (in collection, 2)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "The data input scheme used in [2] is similar as our spike-based input, both eliminating DACs, but our Integration and Fire component eliminates ADCs while [2] keeps."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Recent works [1] demonstrated that ReRAM-based PIM oﬀer great acceleration of CNNs with low energy cost."

## Cited by (in collection, 90)
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "This capability has lead to significant interest in implementing the dot product in the analog domain, thereby improving the speed and energy efficiency of prediction with neural networks [1-3, 9-11]."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _contrasts/critiques_: "However, the conventional mapping method used in [3] [15] cannot make full use of the computation ability of large crossbars."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _background_: "Besides conventional technologies, plenty of researches leverage modified SRAM [8]/ Flash [9] or various emerging non-volatile memory devices with in-memory computing capability to design this many-crossbar architecture, such as the most widely used RRAM (resistive RAM) [4–6, 19–24], PCRAM (phase-change RAM) [7, 25], and MRAM [26]."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _background_: "Therefore, designing ReRAM based NN accelerators attracts lots of researchers’ attentions [2–4]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "These accelerators have been demonstrated on several types of workloads including BSBs [53], MLPs [22, 39, 73, 88], SNNs [9, 66], BMs [12], and CNNs [22, 23, 95, 100, 109]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _uses-method-or-tool_: "For simplicity, we adopt the naive network partition method similar as introduced in [16], which converts the weight tensor of each convolution/fully-connected layer into two"
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _uses-method-or-tool_: "When the length of the unrolled weight is larger than the crossbar size, the column vector of inputs and weights are split for mapping onto different crossbars [16]."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _baseline/comparison_: "PipeLayer [1] modified the ISAAC [2] pipeline architecture and use spike-based input to eliminate ADC and DAC blocks."
- [2019_Angizi_AnalogVsDigitalPIM_ISVLSI](2019_Angizi_AnalogVsDigitalPIM_ISVLSI.md) Analog vs Digital PIM (2019) — _background_: "PipeLayer [15] achieves the speedup and energy saving of 42.45× and 7.17×, respectively, compared with a GPU platform on average."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _baseline/comparison_: "2.2 In-RRAM Computation ISAAC [38], PRIME [12] and PipeLayer [41] are three recently published architectures for implementing DNN and RNN through in-RRAM computation."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _contrasts/critiques_: "Existing ReRAM-based training accelerators such as PipeLayer [8] do not compute the weight gradient convolutions using outer products, but rather, they compute them using MVM operations."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _background_: "Various efforts that propose crossbar-based training architectures [11-13] also develop performance and energy models to evaluate them."
- [2020_Zhang_RepresentableMatrices_ASPDAC](2020_Zhang_RepresentableMatrices_ASPDAC.md) Representable Matrices (2020) — _background_: "Moreover, the use of MCAs allow matrices to be stored inplace, which reduces data fetching and communication costs that fundamentally bounds the performance of any computing system that processes large amounts of data [8, 2, 9]."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "The PipeLayer accelerator takes the above approach of using a second ReRAM array as a buffer to store intermediate weight updates in a batch.174"
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _baseline/comparison_: "Compared with representative R2 PIM accelerators (see Table IV), TIMELY can improve energy efficiency by over 10x (over PRIME [14]) and the computational density by over 6.4x (over PipeLayer [62])."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _baseline/comparison_: "Pipelayer [27] enables neural network training with ReRAM, and further optimizes the computation latency by using pipelined stages and balancing computation resources."
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020) — _uses-method-or-tool_: "In the ReRAM-based DNN accelerator, weights of DNNs are allocated into ReRAM arrays as stated in [11]."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _background_: "Recent works present several NN accelerators based on ReRAM crossbars, such as PRIME [4], ISAAC [5], and PipeLayer [6]."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _background_: "Various works propose ReRAM-based accelerators for DNN inference [11–15] and training [31–35]."
- [2021_Chen_CAP-RAM_JSSC](2021_Chen_CAP-RAM_JSSC.md) CAP-RAM (2021) — _background_: "It is worth mentioning that fully parallelism of all MAC operations is possible with inter-layer pipelining [27, 28], and the imbalanced speed/throughput of each pipeline stage can be solved by mapping techniques, such as replication."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _contrasts/critiques_: "A similar approach is used in other works [10], [35]-[37] where the in-memory accelerator exposes an API."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "Several ReRAM-based in-situ mixed-signal DNN accelerators such as ISAAC [18], Newton [19], PipeLayer [20], PRIME [17], PUMA [21], MultiScale [22], XNORRRAM [37], RapidDNN [38], have been proposed in recent years."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "Unlike PRIME and ISAAC, PipeLayer supports both the training and inference of neural networks [36]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _uses-method-or-tool_: "Therefore, multiple inputs can be processed simultaneously, increasing parallelism and improving throughput [5]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "Another example, Pipelayer [35] computes partial derivatives with memristor crossbars and updates weights by reading them out, merging them with partial derivatives, and writing updated weights back."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _baseline/comparison_: "Strategy A (Fig. 3(a)) conducts accumulation after quantizing BL analog partial sums. Prior work, e.g., ISAAC [1], PRIME [16], and PipeLayer [17], adopts this strategy."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _background_: "A certain number of ReRAM crossbar-based DNN accelerator designs are built in prior works, such as ISAAC [9], PRIME [4], PipeLayer [10], and CASCADE [6]."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _background_: "RRAM-based IMC architectures provide a promising alternative to conventional von-Neumann architectures [2–4, 8, 19– 21]."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _baseline/comparison_: "PipeLayer [48] in the baseline design for training."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _background_: "Existing studies have proposed various memristor-based PIM architecture and realize 2-3 orders of magnitude energy efficiency improvement compared with GPU and CMOS-based ASIC solutions [3] [4] [6] [5] [23]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _background_: "This density allows ReRAM-based systems to store and run on-chip pipelines that compute DNN layers sequentially [54, 56] without costly accesses to off-chip memory [59]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Recently, various hardware accelerators have been proposed to improve the efficiency and performance of traditional deep learning networks [4, 12–16]."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "Processing-in-memory (PIM) -based accelerators can perform in-situ computation and eliminate the data movement between memory and processing elements [1, 4, 8, 11, 23]."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _contrasts/critiques_: "PipeLayer [28] presents the results of crossbar duplication ratios but how to determine them is completely not mentioned."
- [2023_Pelke_MultiCoreCNNMapping_VLSI-SoC](2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.md) Multi-core RRAM CNN Mapping (2023) — _background_: "RRAM-based CIM architectures Several RRAM-based CIM architectures have been presented [6-8, 18]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Alternatives to overcome this limitation have been proposed, as for instance the simulator developed by Song et al. to evaluate their PipeLayer architecture, which considers highly parallel designs based on the notion of parallelism granularity and weight replication."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _extends/builds-on_: "To accommodate different CIM designs for executing MVM on crossbars [4, 39, 42, 51], we introduce the concept of VXB (Virtual Crossbar) as the computational unit rather than physical crossbars to facilitate the computing scheduling in the compiler."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "To store large DNNs, this may require a multi-chip pipeline [2, 67] or dense storage technologies [1]."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _motivation_: "Thus it is of great interest to enable online training or online learning, which refers to the scheme that conducts all three essential operations of a deep neural network in memristive crossbar arrays [18]."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _uses-method-or-tool_: "We follow the evaluation methodology employed in three highly cited works: PRIME [22], ISAAC [9], and PipeLayer [23]."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _background_: "Two data mapping schemes proposed in ISAAC [35] and PRIME [6, 35] are commonly used in many ReRAM-based PIM architectures [1, 12, 37, 53]."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "For accelerating DNNs on PIM, there is a crucial strategy called weight replication [5], [7], [24]."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _uses-method-or-tool_: "In our performance evaluation, we assume that the pre-trained model parameters are mapped to ReRAM crossbars prior to inferencing or fine-tuning consistent with prior work [38]."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "The Computing-In-Memory (CIM) architecture is highly regarded for enabling in-situ computation [3, 5, 8, 9, 15, 38, 41]."
- [2025_Park_COMPASS_DATE](2025_Park_COMPASS_DATE.md) COMPASS (2025) — _background_: "Recognizing these challenges, attention to Processing-In-Memory (PIM) architectures has been rapidly increasing as an alternative to traditional architecture [1–4]."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _background_: "The initial works on analog CIM based accelerators focused on convolutional and fully connected networks [30, 51-53]."
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025) — _contrasts/critiques_: "They are similarly disregarded in [18] and [19], where all FC and CONV layers are executed using AIMC tiles, without attempting to control induced accuracy degradation."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _background_: "ReRAM, a new non-volatile memory technology, comes into the field of PIM design because of its high storage density and high efficiency [46]."
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019)
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)
- [2020_Ji_FPSAReducedArchitecture_TC](2020_Ji_FPSAReducedArchitecture_TC.md) FPSA Reduced Architecture (2020)
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020)
- [2021_Li_RaQu_TCAD](2021_Li_RaQu_TCAD.md) RaQu (2021)
- [2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I](2021_Yu_RRAMforCIMInferenceToTraining_TCAS-I.md) RRAM for CIM: Inference to Training (2021)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2021_Huang_NvcimAccuracyOpt_TCAS-I](2021_Huang_NvcimAccuracyOpt_TCAS-I.md) nvCIM Accuracy Opt (2021)
- [2021_Azamat_Quarry_ICCAD](2021_Azamat_Quarry_ICCAD.md) Quarry (2021)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2022_Lee_OfflineTrainingIRDropMitigation_TCAD](2022_Lee_OfflineTrainingIRDropMitigation_TCAD.md) Offline Training IR-Drop Mitigation (2022)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022)
- [2022_Qu_CoordinatedPruningMapping_TCAD](2022_Qu_CoordinatedPruningMapping_TCAD.md) Coordinated Pruning-Mapping (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2023_Cui_ARES_ICCAD](2023_Cui_ARES_ICCAD.md) ARES (2023)
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024)
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2025_Li_CIMLLMDataflow_ISVLSI](2025_Li_CIMLLMDataflow_ISVLSI.md) CIM-LLM Dataflow (2025)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2025_Rhe_ETA_APCCAS](2025_Rhe_ETA_APCCAS.md) ETA (2025)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2017_Song_PipeLayer_HPCA.pdf](../../03_Crossbar_Accelerator_Architectures/2017_Song_PipeLayer_HPCA.pdf)
- Full text: [../fulltext/2017_Song_PipeLayer_HPCA.txt](../fulltext/2017_Song_PipeLayer_HPCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/hpca.2017.55
