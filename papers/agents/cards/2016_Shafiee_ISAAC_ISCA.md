---
id: W4243519499
key: 2016_Shafiee_ISAAC_ISCA
title: "ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars"
short: "ISAAC"
year: 2016
venue: "ISCA"
venue_full: "ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA 2016)"
authors: "Ali Reza Shafiee, Anirban Nag, Naveen Muralimanohar, Rajeev Balasubramonian, John Paul Strachan, Miao Hu, Richard Stanley Williams, Vivek Srikumar"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM", "Memristor(generic)"]
models: ["CNN", "MLP", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "dataflow-pipelining", "bit-slicing", "adc-dac", "peripheral-circuits", "weight-mapping", "energy-efficiency", "cnn-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 154
cites_in_collection: 3
citations_overall: 741
priority_score: 11.57
doi: "https://doi.org/10.1109/isca.2016.12"
pdf: "../../03_Crossbar_Accelerator_Architectures/2016_Shafiee_ISAAC_ISCA.pdf"
fulltext: "../fulltext/2016_Shafiee_ISAAC_ISCA.txt"
---

# ISAAC

**ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars** — ACM/IEEE 43rd Annual International Symposium on Computer Architecture (ISCA 2016) (2016)

## TL;DR
ISAAC is the first full-fledged memristor-crossbar CNN accelerator, combining an inter-layer pipeline, bit-serial inputs, 2-bit cells and a weight-flipping encoding that saves one ADC bit, reaching 14.8x throughput, 5.5x lower energy and 7.5x computational density versus DaDianNao.

## Summary
Crossbars were known as analog dot-product engines but no complete CNN accelerator had been designed around them. ISAAC dedicates crossbars to each layer in a weight-stationary pipeline with eDRAM buffers between stages, and replicates early layers to balance throughput. Each in-situ multiply-accumulate unit (IMA) holds 128x128 crossbars with 2 bits per cell (16-bit weights bit-sliced across 8 cells), 1-bit DACs that feed 16-bit inputs bit-serially over 16 cycles of 100 ns, sample-and-hold circuits and a shared 1.28 GSps 8-bit ADC, with shift-and-add units merging partial sums. A data encoding stores columns in original or flipped form so that the ADC needs one fewer bit, and the saving is applied back digitally. Design-space exploration over crossbars per IMA, ADCs per IMA and IMAs per tile yields ISAAC-CE (8 128x128 arrays, 8 ADCs per IMA, 12 IMAs per tile) and ISAAC-PE variants. Evaluation is by simulation (CACTI 6.5 at 32 nm, ADC/DAC models) on a suite of CNNs (VGG variants, MSRA variants, DeepFace) and a large DNN layer versus DaDianNao.

## Contributions
- Pipelined layer-per-crossbar architecture with eDRAM inter-stage buffering
- Bit-serial input and bit-sliced weight scheme plus a data encoding that reduces ADC resolution by one bit
- Design-space exploration of memristor storage/compute, ADCs and eDRAM per tile
- Comparison with DaDianNao across CNN and DNN workloads

## Key claims (stable IDs)
- **2016_Shafiee_ISAAC_ISCA#C1** — 14.8x higher throughput, 5.5x lower energy, 7.5x higher computational density than DaDianNao — _support:_ ISAAC-CE on 16-chip configurations — _loc:_ Abstract, Sec. VIII
- **2016_Shafiee_ISAAC_ISCA#C2** — Weight-flipping encoding improves computational and power efficiency by 50% and 80% — _support:_ saves one ADC bit — _loc:_ Sec. V
- **2016_Shafiee_ISAAC_ISCA#C3** — Peak CE of a 128x128 2-bit array is 1707 GOP/s/mm2; with ADCs, tile overhead and eDRAM it falls to 479 — _support:_ vs DaDianNao 63.5 GOP/s/mm2 — _loc:_ Sec. VIII-B

## Results
- ISAAC chip consumes 65.8 W vs DaDianNao 20.1 W at the same size but PE is 119% better
- Chip area 85.4 mm2 (Table I)
- ISAAC-CE consumes 95% more power than DaDianNao on average
- Conservative choice of 1-bit DAC, 2 bits per cell, 128x128 arrays justified by noise tolerance of CNNs

## Key numbers
- tech_node: 32nm
- array_size: 128x128, 2 bits/cell
- energy_eff: 5.5x lower energy than DaDianNao
- throughput: 14.8x vs DaDianNao
- bits_weight: 16b (8 x 2-bit cells)
- bits_adc: 8b at 1.28 GSps

## Datasets / benchmarks
ILSVRC (VGG-1..4, MSRA-1..3 CNN configurations), DeepFace

## Limitations
- Simulation and analytical models only; no fabricated chip
- Noise and parasitics not simulated in depth (justified by citing Hu et al.)
- CNN/DNN only; no attention or dynamic matrices
- ADC energy dominates and scaling depends on ADC technology trends

## Remarks
The reference template for ReRAM crossbar accelerators (weight-stationary tiles, bit-serial inputs, bit-sliced weights, shared ADCs); most later works in the collection use it as a baseline. Its assumptions (full crossbar activation, static weights) are what later OU-based and transformer-oriented designs revisit, since attention requires writing dynamic operands.

## Cites (in collection, 3)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Prior work has already observed that crossbar arrays using resistive memory are effective at performing many dot-product operations in parallel [33, 43, 53, 71, 78]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Other emerging memory technologies (e.g., PCM) have also been used as synaptic weight elements [6], [68]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "Chi et al. [10] propose PRIME, a morphable PIM structure for ReRAM based main memory with carefully designed peripheral circuits that allow arrays to be used as memory, scratchpads, and dot product engines for CNN workloads."

## Cited by (in collection, 154)
- [2018_Kim_NonlinearIVAwareDNN_JETC](2018_Kim_NonlinearIVAwareDNN_JETC.md) Nonlinear-IV NN (2018) — _background_: "To address the issue, many dedicated accelerators for vector-matrix multiplications have been proposed [3-6]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "The data input scheme used in [2] is similar as our spike-based input, both eliminating DACs, but our Integration and Fire component eliminates ADCs while [2] keeps."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _uses-method-or-tool_: "Two related designs [6], [7] are simulated using MNSIM to validate its scalability."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _background_: "The ISAAC architecture is a full neural execution unit similar to DaDianNao but using ReRAM crossbars to store and process weights for CNN inference [9]."
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "Research on these devices has already led to the development of massively parallel, memory-centric hardware accelerators with applications ranging from image processing to healthcare19-22."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _contrasts/critiques_: "Recently, architectural simulator platforms (e.g., PRIME [118], ISAAC [119], and Harmonica [120]) have been developed to support system-level design of neuromorphic accelerators, however they have limited considerations at the aforementioned nonideal device properties (i.e., they only considered the weight precision and/or variation)."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _uses-method-or-tool_: "We evaluate a memristive accelerator similar to ISAAC [9], wherein each layer of the neural network is placed in one or more tiles."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _uses-method-or-tool_: "First, original feature maps from the input or pooling layer are transformed to fixed-point representation using the same method introduced by Shafiee et al. [9], and these feature maps are decomposed based on the WLD resolution."
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018) — _baseline/comparison_: "The current RRAM architectures use small crossbars, e.g., 128 x 128 crossbars in ISAAC [13]."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _background_: "Our implementation using off-the-shelf SRAM array and extra PEs to mimic the crossbar behavior is just for cost saving, and in fact, the proposed SemiMap can be easily extended to other crossbar architectures, such as the emerging devices with in-memory computing [5–9, 21–26]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "Resistive crossbar based specialized hardware systems have been proposed for accelerating DNN inference [7–11] and training [12, 13]."
- [2019_Lin_SparseReRAMMapping_ASP-DAC](2019_Lin_SparseReRAMMapping_ASP-DAC.md) Learning-Sparsity-ReRAM (2019) — _background_: "With the advantages of efficient in-memory computing ability, previous work has proposed several ReRAM-based Computing Systems, like PRIME [2] and ISAAC [3]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _baseline/comparison_: "PUMA has 20.7% lower power efficiency and 29.2% lower area efficiency than ISAAC due to the overhead of programmability."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _baseline/comparison_: "the equivalent energy efficiency of the computing units (i.e., RRAM Banks) is 3.44TOps/W, nearly 8.6x and 1.6x compared with existing RRAM-based accelerators, ISAAC [15] and PRIME [3], respectively."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "In order to reduce the data transfers to a minimum in inference accelerators, a promising avenue is to employ in-memory computing using non-volatile memory devices3."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _motivation_: "However, the mixed-signal ADC/DAC blocks take the majority of the chip area and power, e.g., 98% of the total area and 89% of the total power, and do not scale as fast as the CMOS technology does [2]."
- [2019_Angizi_AnalogVsDigitalPIM_ISVLSI](2019_Angizi_AnalogVsDigitalPIM_ISVLSI.md) Analog vs Digital PIM (2019) — _background_: "For example, ISAAC [14] architecture improves throughput and energy by 14.8× and 5.5×, respectively, relative to a well-known ASIC architecture."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _uses-method-or-tool_: "We use the ReRam crossbar array and sample-and-hold circuit models in ISAAC [4]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "Crossbar-based accelerators commonly use bit-slicing to perform high precision MVM operations [6, 7]."
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020) — _background_: "From Figure 3, non-uniform quantization can reduce 1 bit ADC resolution compared with uniform quantization without accuracy loss, and ADC overheads grow exponentially with resolution [11]."
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020) — _background_: "Due to its outstanding performance on computing matrix-vector multiplications (MVM), memristor crossbars are widely used as dot-product accelerator in recent neuromorphic computing designs [19]."
- [2020_Zhang_RepresentableMatrices_ASPDAC](2020_Zhang_RepresentableMatrices_ASPDAC.md) Representable Matrices (2020) — _background_: "Moreover, the use of MCAs allow matrices to be stored in-place, which reduces data fetching and communication costs that fundamentally bounds the performance of any computing system that processes large amounts of data [8, 2, 9]."
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020) — _background_: "Nonvolatile memory (NVM)-based processing-in-memory (PIM) architectures, such as the crossbar, have demonstrated the potential to speed up the multiply-and-accumulate (MAC) operations in DNNs, achieving high energy efficiency with low latency [8, 9, 11]."
- [2020_Zhang_ParasiticResistanceMitigationCNN_JETC](2020_Zhang_ParasiticResistanceMitigationCNN_JETC.md) Parasitic-Mitigation-CNN (2020) — _uses-method-or-tool_: "In Table 2, crossbar, ADC/DAC parameters are adopted from ISAAC[29]."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _data/numbers_: "A significant bottleneck for many of the analog architectures is the ADC, which consumes 49% of the total chip power in ISAAC and 41% in the memristive Boltzmann machine."
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _baseline/comparison_: "For instance, ISAAC [29] and PUMA [30] adopted an 8-bit SAR ADC for higher precision computations, while XNOR-RRAM implemented a 3-bit flash ADC for binary input/weight computation [57]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _motivation_: "Fig. 4. (a) The number of input/Psum accesses, (b) energy breakdown of PRIME [14], and (c) energy breakdown of ISAAC [58]."
- [2021_Zhang_RobustTrainableQuantizer_ASPDAC](2021_Zhang_RobustTrainableQuantizer_ASPDAC.md) Robust Trainable Quantizer (2021) — _background_: "With these merits, the ReRAM-based neural network accelerator has been widely studied and is proved to be a promising alternative to Von-Neumann architecture [2] [3] for this type of application."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _background_: "PRIME [4] and ISAAC [24] designs utilize ReRAM to accelerate the inference of CNNs."
- [2020_Shin_TOPAR_ICCAD](2020_Shin_TOPAR_ICCAD.md) TOPAR (2020) — _uses-method-or-tool_: "The resolution of ADC and DAC is set as 8bit and 1bit by following the result from [2]."
- [2020_Guo_ATT_ICCD](2020_Guo_ATT_ICCD.md) ATT (2020) — _background_: "Processing-in-Memory (PIM) platforms are more and more popular in accelerating neural network applications due to fewer data movements compared to FPGA and ASIC implementations [1–3]."
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _uses-method-or-tool_: "The hardware simulator is cycle-accurate. It can calculate the energy consumption and area of the architecture based on the data from ISAAC [5] as listed in Table II."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _uses-method-or-tool_: "Hence, this work assumes a fixed two bits of weights are stored in each crossbar cell [13] and implements weight quantization by varying the number of crossbars used to store the weights."
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _background_: "Previous work, such as PRIME [21] and ISAAC [22], leverages in-situ computation to avoid the tremendous cost of data movement and efficiently compute multiply-accumulate operations, the most intensive computation in DNNs."
- [2021_Chen_CAP-RAM_JSSC](2021_Chen_CAP-RAM_JSSC.md) CAP-RAM (2021) — _background_: "It is worth mentioning that fully parallelism of all MAC operations is possible with inter-layer pipelining [27, 28], and the imbalanced speed/throughput of each pipeline stage can be solved by mapping techniques, such as replication."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _motivation_: "As a consequence, efficient exploitation of CIM acceleration still relies on the programmer and her understanding of the hardware, thus severely limiting programmability [6], [9], [10]."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _baseline/comparison_: "In contrast, ISAAC [18] adds an offset to weights so that all values become positive."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "It outperformed the fully digital DaDianNao with improvements of 14.8x, 5.5x, and 7.5x in throughput, energy, and computational density, respectively [34]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _baseline/comparison_: "In bit slicing, the bit representation of each matrix element is divided into multiple slices, and the results of bit sliced MVMs are combined via shift-and-add (S&A) reduction [9, 21, 56]."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _uses-method-or-tool_: "We conduct experiments with two memristor-based architectures, ISAAC [33] and FPSA [24], to evaluate the different invocation granularity of the compilation framework."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _baseline/comparison_: "For example, ISAAC [1] and CASCADE [2] adopt a 1-bit DAC to stream a 16-bit input with 16 cycles."
- [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) Area-Efficient Multi-Task BERT (2021) — _uses-method-or-tool_: "The simulator is based on ISAAC [20] configuration with 32nm process node, and it utilizes positive and negative arrays to store weight parameters."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _baseline/comparison_: "Fig. 11 shows the speed up over the baseline accelerator (i.e., ISAAC), we compare the cycles of inference on various networks."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _contrasts/critiques_: "This allows the execution of shift-and-add operations within the ADC at a minimal overhead, avoiding dedicated multi-bit adders [42]–[44]."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _background_: "Consequently, MCAs have been aggressively harnessed for energy-efficient DNN acceleration [2, 4, 22]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Recently, a full-ﬂedged NN accelerator design based on ReRAM crossbars have been proposed, named ISAAC [39]."
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _background_: "Second, multi-layer parallel architectures (e.g., ISAAC [5] and PUMA [7]) are capable of processing multiple CNN layers simultaneously, allowing multi-layer pipelines to maximize the throughput of a full CNN workload."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Network-on-chip and program scheduling need to be carefully designed to achieve good end-to-end application-level energy efficiency [ISAAC, PUMA]."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _background_: "Prior works with RRAM-based crossbar architectures have shown up to 1,000× improvement in energy efﬁciency as compared to CPUs/GPUs [2–4]."
- [2022_Kim_ExtremePartialSumQuant_JETC](2022_Kim_ExtremePartialSumQuant_JETC.md) Extreme Partial-Sum Quantization (2022) — _background_: "Therefore, to support bit-scalable computation with low-resolution DAC, most of CIM accelerators process input values in bit-serial manner [8, 15, 20]."
- [2022_Huang_HWAwareQuantMappingCIM_TODAES](2022_Huang_HWAwareQuantMappingCIM_TODAES.md) CIM Quant/Mapping DSE (2022) — _background_: "Thus, various CIM designs based on emerging non-volatile memory (eNVM) have been proposed for edge inference [4, 5, 6]."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _background_: "One approach to exploit in-memory computing for DNNs is to design stand-alone accelerators where multiple AIMC tiles and associated digital logic blocks are interconnected by a suitable communication fabric [6, 7]."
- [2023_Ma_SAFVariationTolerantMapping_JETC](2023_Ma_SAFVariationTolerantMapping_JETC.md) SAF/Variation Remapping (2023) — _background_: "Tile and IMA (in-situ multiply-accumulate) are higher hierarchies of MCAs [18]."
- [2023_Kim_INCA_HPCA](2023_Kim_INCA_HPCA.md) INCA (2023) — _background_: "Specifically, PIM hardware with resistive random-access memory (RRAM, ReRAM, a.k.a. memristor) has been explored to build accelerators for deep learning models in numerous works [6], [10], [20], [42], [48]."
- [2023_Sun_Gibbon_TCAD](2023_Sun_Gibbon_TCAD.md) Gibbon (2023) — _background_: "Existing studies have proposed various memristor-based PIM architecture and realize 2-3 orders of magnitude energy efficiency improvement compared with GPU and CMOS-based ASIC solutions [3] [4] [6] [5] [23]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _baseline/comparison_: "Architectures often partition, or slice, the bits in DNN inputs and weights into multiple lower-resolution slices and compute with different slices in multiple steps [54]."
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _contrasts/critiques_: "For example, Dazzi et al. [11] targeted a relatively small ResNet-like network targeting the CIFAR10 dataset, while Shafiee et al. [12] and Ankit et al. [13] target VGG-like networks featuring no residual layers, nicely fitting mapping on pipelined data-flow architectures."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Recently, various hardware accelerators have been proposed to improve the efficiency and performance of traditional deep learning networks [4, 12–16]."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _uses-method-or-tool_: "The full-precision weights and inputs are split into smaller slices as i) bit-capacity of memristors is insufficient for weights and ii) full-precision inputs need digital-to-analog converters (DACs) and analog-to-digital converters (ADCs) which consume huge energy and area [29]."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "ISAAC [21] further proposes a pipelined PIM architecture where individual crossbars are dedicated to each DNN layer."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Analog in-memory computing (AIMC) with spatially instantiated synaptic weights holds high promise to overcome this challenge, by performing matrix-vector multiplications (MVMs) directly within the network weights stored on a chip to execute an inference workload (refs 2-7)."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _uses-method-or-tool_: "Our proposed abstract architecture is compatible with the Crossbar/IMA/Tile/Chip structure widely adopted in previous work [5]."
- [2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC](2023_Zheng_ReconfigurableSparseAttentionNVPIM_DAC.md) Reconfigurable Sparse-Attention NVPIM (2023) — _uses-method-or-tool_: "For the NVPIM bank, we use the memory array model from [9]."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _contrasts/critiques_: "ISAAC [25] allocates crossbars heuristically, according to the stride sizes of convolutional (Conv) layers."
- [2023_Pelke_MultiCoreCNNMapping_VLSI-SoC](2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.md) Multi-core RRAM CNN Mapping (2023) — _background_: "Previous works presented accelerator architectures that use RRAM crossbars as matrix-vector multiplication (MVM) units [5-8]."
- [2023_Jang_VECOM_ICCAD](2023_Jang_VECOM_ICCAD.md) VECOM (2023) — _uses-method-or-tool_: "The simulations focus on a ReRAM-based DNN accelerator with a hardware configuration based on ISAAC architecture [1]."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _uses-method-or-tool_: "As configured in ISAAC [27], the “cycle” in CPSAA means the time of ADC processing 32 column signals, i.e., 25ns."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "The other method is sharing a single ADC across several columns or using a single ADC per crossbar tile."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _contrasts/critiques_: "Some works manually deployed the model on CIMs [39] with customized mapping and scheduling policies that are hard to generalize to other CIMs."
- [2024_Wu_BWQ_TCAD](2024_Wu_BWQ_TCAD.md) BWQ (2024) — _baseline/comparison_: "HW-based optimization solutions only improve the accelerators’ performance from an HW perspective, featuring intra-layer pipeline (ISAAC [5]) or leveraging the natural sparsity of the neural networks with index reordering (SRE [3])."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _uses-method-or-tool_: "The Library Plug-In models a library of components used in various CiM works [2, 6, 18, 29, 37, 38, 40, 44, 51, 57]."
- [2024_Wang_LLMOnMemristorCrossbar_TPAMI](2024_Wang_LLMOnMemristorCrossbar_TPAMI.md) LLM-on-Memristor-Crossbar (2024) — _motivation_: "For instance, the GPT-3 model has over 175 billion parameters, and it would require 2777 ISAAC chips [9] to store all of its parameters."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _baseline/comparison_: "Two data mapping schemes proposed in ISAAC [35] and PRIME [6, 35] are commonly used in many ReRAM-based PIM architectures [1, 12, 37, 53]."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _motivation_: "Due to the different micro-architectures of various accelerators, it is uneconomical and unrealistic to manually design the deployment schemes for each DNN model on each accelerator as in previous works [5–10]."
- [2024_Chowdhury_MELISO_ICONS](2024_Chowdhury_MELISO_ICONS.md) MELISO (2024) — _background_: "Emerging non-volatile memory technologies, such as resistive random access memories (RRAMs) based crossbar arrays, provide a versatile solution to the challenges of data-intensive, large-scale computational tasks [6, 7]."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _extends/builds-on_: "We facilitate dequantization by integrating additional shift-and-add (S&A) units into the previously proposed ReRAM tile architecture [20]."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _background_: "Compared to conventional architectures, CIM significantly mitigates persistent memory wall problem [49] and demonstrates strong competitiveness in data-intensive applications especially deep neural network (DNN) inference [38, 43, 52]."
- [2025_Park_COMPASS_DATE](2025_Park_COMPASS_DATE.md) COMPASS (2025) — _background_: "Recognizing these challenges, attention to Processing-In-Memory (PIM) architectures has been rapidly increasing as an alternative to traditional architecture [1–4]."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2025_Song_HyFlexPIM_ISCA](2025_Song_HyFlexPIM_ISCA.md) HyFlexPIM (2025) — _background_: "The pioneering works, ISAAC [50] and [20] demonstrate a pipelined RRAM crossbar and hybrid RRAM capable of efficiently executing CNNs."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _background_: "In the past, compute-in-memory (CIM) has shown great promise in accelerating convolutional and fully-connected layers by leveraging their weight stationary nature, as their feature maps are known before runtime [29-31]."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "ISAAC [31] presents multi-core CIM architectures and demonstrates the importance of cross-layer inference, which the authors refer to as pipelining."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _contrasts/critiques_: "The first is an adhoc strategy that integrates specialized CMOS-based units tailored to specific workloads, as exemplified by ISAAC [9]."
- [2026_Hu_HyPIM_TECS](2026_Hu_HyPIM_TECS.md) HyPIM (2026) — _uses-method-or-tool_: "The simulation parameters for the ReRAM, including tile configuration, area, and power, are derived from prior research [43]."
- [2026_Zhao_NLDPE_TCAD](2026_Zhao_NLDPE_TCAD.md) NL-DPE (2026) — _motivation_: "Unfortunately, ADCs are both energy- and area-inefficient, consuming more than 30% of the chip area and accounting for over 50% of the total power consumption [4, 5]."
- [2026_Zheng_InterfaceKVQ_ICCAD](2026_Zheng_InterfaceKVQ_ICCAD.md) InterfaceKVQ (2026) — _background_: "Accelerators built on NVM, often referred to as nonvolatile CiM (NVCiM) [19, 22, 34], have demonstrated large density and energy advantages for matrix-heavy inference [17, 20, 24]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _data/numbers_: "For example, a moderate array size containing 128 rows with 2-bit memory devices and 1-bit per stream already requires a 8bit ADC [41]."
- [2026_Xiao_RoboPIM_TCAD](2026_Xiao_RoboPIM_TCAD.md) RoboPIM (2026) — _uses-method-or-tool_: "The resolution of ADCs and DACs is 8 and 2 bit, respectively, and their area and power specifications are based on [37]."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2020_Jia_ProgrammableIMCMicroprocessor_JSSC](2020_Jia_ProgrammableIMCMicroprocessor_JSSC.md) Princeton Programmable IMC Processor (2020)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2019_Cai_LBCNN_TCAD](2019_Cai_LBCNN_TCAD.md) LB-CNN (2019)
- [2019_Zhang_MTFramework_TCAD](2019_Zhang_MTFramework_TCAD.md) MT Framework (2019)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)
- [2020_Ji_FPSAReducedArchitecture_TC](2020_Ji_FPSAReducedArchitecture_TC.md) FPSA Reduced Architecture (2020)
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Jiang_MINT_ISCAS](2020_Jiang_MINT_ISCAS.md) MINT (2020)
- [2020_Qu_RaQu_DAC](2020_Qu_RaQu_DAC.md) RaQu (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Li_RaQu_TCAD](2021_Li_RaQu_TCAD.md) RaQu (2021)
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
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
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED](2023_PerezBoschQuesada_MultilevelRRAMVMMAssessment_TED.md) Multilevel-RRAM-VMM-Assessment (2023)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2023_Bai_CIMQ_TCAD](2023_Bai_CIMQ_TCAD.md) CIMQ (2023)
- [2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED](2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.md) ADC-Less CiM Partial-Sum Quant (2023)
- [2023_Cui_ARES_ICCAD](2023_Cui_ARES_ICCAD.md) ARES (2023)
- [2024_Bai_eFlashIMCSoC_TCAD](2024_Bai_eFlashIMCSoC_TCAD.md) eFlash IMC SoC Toolchain (2024)
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024)
- [2024_Cai_MemristorLSHAttention_ISCAS](2024_Cai_MemristorLSHAttention_ISCAS.md) Memristor LSH Attention (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)
- [2024_Lv_NonIdealPIMFineTuning_TCAD](2024_Lv_NonIdealPIMFineTuning_TCAD.md) Non-Ideal PIM Fine-Tuning (2024)
- [2025_Bommana_COMET3D_TCAD](2025_Bommana_COMET3D_TCAD.md) COMET-3D (2025)
- [2025_Li_CIMLLMDataflow_ISVLSI](2025_Li_CIMLLMDataflow_ISVLSI.md) CIM-LLM Dataflow (2025)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Jeon_OptiRange_ICCAD](2025_Jeon_OptiRange_ICCAD.md) OptiRange (2025)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2025_Sun_DuoPIM_TCAD](2025_Sun_DuoPIM_TCAD.md) DuoPIM (2025)
- [2025_Rhe_ETA_APCCAS](2025_Rhe_ETA_APCCAS.md) ETA (2025)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2016_Shafiee_ISAAC_ISCA.pdf](../../03_Crossbar_Accelerator_Architectures/2016_Shafiee_ISAAC_ISCA.pdf)
- Full text: [../fulltext/2016_Shafiee_ISAAC_ISCA.txt](../fulltext/2016_Shafiee_ISAAC_ISCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isca.2016.12
