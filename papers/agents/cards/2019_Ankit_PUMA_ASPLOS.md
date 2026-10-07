---
id: W2913104037
key: 2019_Ankit_PUMA_ASPLOS
title: "PUMA"
short: "PUMA"
year: 2019
venue: "ASPLOS"
venue_full: "24th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS '19), ACM"
authors: "Aayush Ankit, Izzat El Hajj, Sai Rahul Chalamalasetti, Geoffrey Ndu, Martin Foltín, Richard Stanley Williams, Paolo Faraboschi, Wen‐mei Hwu, John Paul Strachan, Kaushik Roy, Dejan S. Milojicic"
category: "03 Crossbar Accelerator Architectures"
devices: ["Memristor(generic)", "ReRAM"]
models: ["MLP", "CNN", "VGG", "LSTM/RNN", "Other"]
lm_models: ["BigLSTM (856M)", "LSTM-2048 (554M)", "NMT LSTM L3 (91M) and L5 (125M)"]
param_scale: "91M-856M (LSTM language/translation models)"
slm: false
evidence: simulation
topics: ["crossbar-architecture", "compiler-software-stack", "dataflow-pipelining", "heterogeneous-analog-digital", "tiling-partitioning", "recurrent-models", "energy-efficiency", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 54
cites_in_collection: 8
citations_overall: 422
priority_score: 10.05
doi: "https://doi.org/10.1145/3297858.3304049"
pdf: "../../03_Crossbar_Accelerator_Architectures/2019_Ankit_PUMA_ASPLOS.pdf"
fulltext: "../fulltext/2019_Ankit_PUMA_ASPLOS.txt"
---

# PUMA

**PUMA** — 24th International Conference on Architectural Support for Programming Languages and Operating Systems (ASPLOS '19), ACM (2019)

## TL;DR
PUMA is a programmable spatial memristor-crossbar inference accelerator with an ISA and compiler that reaches 577 GOPS/s/mm2 and 837 GOPS/s/W, up to 2,446x energy and 66x latency improvement over a Pascal GPU on LSTM benchmarks, at ~21-29% efficiency cost versus ISAAC.

## Summary
Special-purpose crossbar accelerators (ISAAC, PRIME) encode one or two network types as state machines and cannot run LSTMs (vector linear and transcendental ops), flexible data movement or diverse workloads. PUMA is a spatial architecture of nodes of tiles of cores: each core has multiple 128x128 matrix-vector multiplication units (MVMUs; 2-bit cells, 16-bit fixed point via bit slicing and shift-and-add) plus a vector functional unit (VFU, 4 lanes sweet spot), scalar unit, transcendental ROM-Embedded-RAM lookup, register file and a 3-stage instruction pipeline; tiles share eDRAM memory with synchronization attributes and communicate over an on-chip network. A specialized ISA with MVM, ALU/VFU, load/store and send/receive instructions keeps decode cost low. The compiler takes a high-level C++ model (graph of operations), partitions matrices across crossbars/cores/tiles, linearises the graph, schedules instructions and does register allocation to run on thousands of spatial cores, so weights are programmed once and only activations move. A detailed simulator models functionality, timing and power (32nm CMOS-memristive, 1 GHz, 90.6 mm2 and 62.5 W per node, ~69 MB weight capacity). Benchmarks (Table 5) cover MLPs (5M-21M), deep and wide LSTMs/NMT (91M, 125M, 554M, 856M), VGG16/19 CNNs; baselines are Haswell CPU, Kepler/Maxwell/Pascal GPUs, Google TPU and ISAAC.

## Language models evaluated
- Models: BigLSTM (856M), LSTM-2048 (554M), NMT LSTM L3 (91M) and L5 (125M)
- Scale: 91M-856M (LSTM language/translation models)

## Contributions
- Programmable, general-purpose memristor-crossbar ML inference architecture exposed by a specialized ISA
- Complete compiler from high-level code to PUMA ISA with graph partitioning, scheduling and register allocation
- Detailed open-sourced architecture simulator with functional, timing and power models
- Evaluation across MLP, LSTM and CNN workloads versus CPUs, GPUs, TPU and ISAAC, including design-space sweeps and a noise study

## Key claims (stable IDs)
- **2019_Ankit_PUMA_ASPLOS#C1** — PUMA reaches 577 GOPS/s/mm2 and 837 GOPS/s/W at 1 GHz — _support:_ Peak AE 0.58 TOPS/s/mm2, PE 0.84 TOPS/s/W; 90.6 mm2, 62.5 W — _loc:_ Abstract / Table 6
- **2019_Ankit_PUMA_ASPLOS#C2** — Large energy and latency gains over Pascal GPU, largest for LSTMs — _support:_ Energy: CNN 11.7-13.0x, MLP 30.2-80.1x, deep LSTM 2,302-2,446x, wide LSTM 758-1,336x; latency: CNN 2.73-2.99x, deep LSTM 41.6-66.0x, wide LSTM 4.70-5.24x; MLP slower 0.24-0.40x — _loc:_ Sec. 7.1-7.2 / Fig. 11
- **2019_Ankit_PUMA_ASPLOS#C3** — Programmability costs about a quarter of ISAAC's efficiency — _support:_ 20.7% lower power efficiency and 29.2% lower area efficiency than ISAAC — _loc:_ Sec. 7.4.2 / Table 6
- **2019_Ankit_PUMA_ASPLOS#C4** — Analog MVMU is far more efficient than digital MVMU — _support:_ Digital needs 8.97x area, 4.17x energy per MVMU; whole chip 4.93x area and 6.76x energy — _loc:_ Sec. 7.4.3

## Results
- 8.3x higher peak area efficiency and 1.65x higher peak power efficiency than TPU; 64.4x/193x/9.7x area efficiency for MLP/LSTM/CNN at best TPU batch
- Memristive 128x128 MVMU: 16,384 MACs in 2,304 ns at 43.97 nJ
- PUMA with 2-bit cells tolerates high write-noise levels, higher bits per cell lose noise margin (Fig. 13)
- Benefits shrink with large batch (16-128) as GPU weight reuse improves, but energy advantage persists (Fig. 11c,d)

## Key numbers
- tech_node: 32nm CMOS + memristor
- array_size: 128x128 MVMUs
- energy_eff: 837 GOPS/s/W (0.84 TOPS/s/W)
- throughput: 52.31 TOPS peak (node, 16-bit)
- bits_weight: 16b fixed point (2-bit cells)

## Datasets / benchmarks
MLPL4, MLPL5, NMTL3, NMTL5, BigLSTM, LSTM-2048, VGG16, VGG19

## Limitations
- Simulator-based; no fabricated PUMA chip
- Noise study limited to write noise on bits per device; no IR drop, drift or ADC non-linearity
- Workloads are CNN/MLP/LSTM; no transformers or attention (dynamic matrices would need crossbar writes)
- MLPs can be slower than GPUs (no inter-layer parallelism); GPU/CPU baselines run via Torch7
- Programmability overhead reduces efficiency versus ISAAC

## Remarks
Foundational architecture (420+ citations) showing how to make crossbars programmable with a compiler; its main lessons (weights stationary, pipelined spatial cores, VFU/lookup for nonlinearities) carry over to transformer accelerators, but attention and KV-cache dynamic operands are not addressed. Its LSTM language-model results (BigLSTM 856M) are the earliest large 'language model on memristor crossbar' evidence in the collection, though under idealised noise. Mapping/synchronization approach is critiqued by Pelke et al. (centralized attribute buffer).

## Cites (in collection, 8)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "To overcome this limitation, memristor crossbars can store a matrix with high storage density and perform MVM operations with very low energy and latency [5, 13, 52, 87, 98, 116]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "To overcome this limitation, memristor crossbars can store a matrix with high storage density and perform MVM operations with very low energy and latency [5, 13, 52, 87, 98, 116]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "These accelerators have been demonstrated on several types of workloads including BSBs [53], MLPs [22, 39, 73, 88], SNNs [9, 66], BMs [12], and CNNs [22, 23, 95, 100, 109]."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _data/numbers_: "Practically realizable crossbars provide 2-6 bits of precision per device [52]."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "Further, recent research have explored coding schemes for reliable memristor computation at high precision [38, 92]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "PUMA has 20.7% lower power efficiency and 29.2% lower area efficiency than ISAAC due to the overhead of programmability."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Several architectures have been proposed, both digital [20, 21, 36, 61, 72, 89] and mixed digital-analog using memristor crossbars [22, 23, 73, 95, 100]."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018) — _background_: "Many machine learning accelerators have been proposed that leverage memristor crossbars [9, 10, 12, 22, 23, 53, 58, 66, 73, 88, 95, 100]."

## Cited by (in collection, 54)
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _extends/builds-on_: "The PUMA [6] compiler provides a high-level programming interface in C++ that allows programmers to express"
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "Crossbar-based accelerators commonly use bit-slicing to perform high precision MVM operations [6, 7]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "There is significant on-going research on defining such hierarchical organizations of in-memory computing cores to tackle a range of applications58,167,168."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020) — _background_: "The PUMA architecture uses smaller functional units to execute the equivalent wide instruction over several cycles: this compromise offsets the parallelism of SIMD but still reduces the overhead of instruction fetch and decode.148"
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020) — _data/numbers_: "Fig. 26 shows the inference energy of a ReRam-based accelerator [30] compared with a CPU (Intel Skylake) and a GPU (NVIDIA Pascal)."
- [2021_Huang_MixedPrecisionQuant_ASP-DAC](2021_Huang_MixedPrecisionQuant_ASP-DAC.md) MPQ ReRAM (2021) — _uses-method-or-tool_: "To evaluate the impact of different quantization schemes on DNN inference energy consumption and latency, we use the PUMA [15] simulator, PUMAsim, which is a cycle-level architecture simulator for ReRAM-based accelerators."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _contrasts/critiques_: "Building on their effort, Ankit et al. [24] developed a runtime compiler implemented as a C++ library, which requires the users to rewrite the application with the proposed API."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "Several ReRAM-based in-situ mixed-signal DNN accelerators such as ISAAC [18], Newton [19], PipeLayer [20], PRIME [17], PUMA [21], MultiScale [22], XNORRRAM [37], RapidDNN [38], have been proposed in recent years."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "PUMA is a spatial processor and provides more flexibility and scalability to accelerate a wide range of workloads and different types of data [41]."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021) — _background_: "Select-lines (SL) are used to turn on transistors for selected rows. for performing the Matrix-Vector-Multiplication (MVM) operations of DNNs in the analog domain [2, 3]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _contrasts/critiques_: "Recent work has optimized the performance and energy of bit-sliced accelerators [6, 14, 42, 49], but rarely evaluates the effect of system-level design decisions on inference accuracy."
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _contrasts/critiques_: "For example, PUMA [5] has a lower area and energy efficiency than ISAAC [33], due to the overhead to achieve better programmability."
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _contrasts/critiques_: "Unlike DSE frameworks for single-layer parallel architectures (i.e., considering loop mapping at memory hierarchies), the existing DSE frameworks/methodologies for multi-layer parallel architectures (e.g., in [5–7, 11]) and they focus more on mapping at AIMC-level and Tile/PE-level."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Multi-core architecture design with network-on-chip that realizes efficient and versatile data transfers and inter-array pipelining is likely to be the next major challenge for RRAM-CIM [ISAAC, PUMA]."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _contrasts/critiques_: "[9] describes an ISA and compiler dedicated to programming and utilizing a multi-tile AIMC accelerator, and an associated architectural simulator (named PUMASim) to evaluate the energy and performance of compiled applications."
- [2022_Amin_ParasiticsPartitioning_ISCAS](2022_Amin_ParasiticsPartitioning_ISCAS.md) Parasitics-Partitioning (2022) — _motivation_: "One of the major factors limiting their wide use in practical ML applications is the large and energy-hungry signal conversion units required to change the computation domain from analog-to-digital (and vice versa) to compute the nonlinear vector operations, e.g. activation functions in DNNs [9]."
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023) — _contrasts/critiques_: "Shafiee et al. [12] and Ankit et al. [13] target VGG-like networks featuring no residual layers, nicely fitting mapping on pipelined data-flow architectures."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _baseline/comparison_: "We also compare our results with an in-memory NVM accelerator [14] where the MVM Dynamic operations are executed in the temporal 1-D SIMD lanes instead of the NVM tiles due to limited endurance."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _uses-method-or-tool_: "It is based on in-situ multiply-accumulate (IMA) unit in state-of-the-art CIM architectures [29], [33]. Power and area for various IMA components are also obtained from [29]."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "Processing-in-memory (PIM) -based accelerators can perform in-situ computation and eliminate the data movement between memory and processing elements [1, 4, 8, 11, 23]."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _baseline/comparison_: "In the field of PIM, PUMA [10] is the first memristor-based ML inference accelerator that supports ISA with a compiler that can convert high-level languages into ISA code. Nonetheless, heuristic weight replicating and core mapping methods adopted by its compiler are difficult to guarantee high performance."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2023_Pelke_MultiCoreCNNMapping_VLSI-SoC](2023_Pelke_MultiCoreCNNMapping_VLSI-SoC.md) Multi-core RRAM CNN Mapping (2023) — _extends/builds-on_: "We improve on this idea by proposing a decentralized synchronization scheme that requires significantly less memory."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _uses-method-or-tool_: ""Moreover, ADC can consume up to 70-90% of the on-chip area of the crossbar-based computation unit, including memristive crossbar and peripheral circuits, and up to 80-88% of energy." ... "Then, moving forward with the path toward the most accurate memristive neural network simulators, the PUMAsim proposed by Ankit et al. uses Verilog HDL to model the tiles and cores at the Register Transfer Level, which allows them to be mapped into a 45 nm Silicon-on-Insulator CMOS process for area estimation.""
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _contrasts/critiques_: "Ambrosi et al. [2] propose a compilation tool that schedules matrix-vector computation (MVM) on a ReRAM-based architecture, but its performance degrades when the CIM architecture and computing granularity change."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _contrasts/critiques_: "PUMA [74] provides a detailed model of a particular DNN system but does not explore the design space."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _baseline/comparison_: "For the comparison of compilation methods, we select SongC [18], PUMA [22], and Polyhedral [16] as baselines, whose characteristics are elaborated in Section II."
- [2025_Zhao_CMSwitch_ASPLOS](2025_Zhao_CMSwitch_ASPLOS.md) CMSwitch (2025) — _baseline/comparison_: "PUMA [3] (focusing on operator duplication and pipeline scheduling), OCC [39] (optimizing operator mapping via tiling and loop unrolling), and CIM-MLC [33] (employing multi-grained pipelining and operator duplication for diverse architecture)."
- [2025_Park_COMPASS_DATE](2025_Park_COMPASS_DATE.md) COMPASS (2025) — _contrasts/critiques_: "PIM-aware compilers like PUMA [13] and PIMCOMP [3] have their primary focus on mapping all the weights on chip, but it is not possible to map large networks on chip when PIM memory footprint is constrained to tens of MBs at most."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _uses-method-or-tool_: "To maximize the throughput, CIM based spatial accelerators constitute of a hierarchical architecture as proposed in a previous work, PUMA [52]."
- [2025_CuberoCascante_CIMFlow_TECS](2025_CuberoCascante_CIMFlow_TECS.md) CIMFlow (2025) — _background_: "PUMA [4] proposes an architecture based on a hierarchical interconnect, where shared memory buffers are present in each tile."
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _contrasts/critiques_: "The second approach, adopted by architectures such as PUMA [13], introduces programmable digital Vector Functional Units (VFUs) to support a wide range of operations. However, this programmability comes at the cost of performance, particularly for DMMuls in Transformer models."
- [2026_Wang_JADE_JETCAS](2026_Wang_JADE_JETCAS.md) JADE (2026) — _contrasts/critiques_: "Existing memory-centric dataflow exploration frameworks [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25] are predominantly tailored for conventional neural networks (NNs) and fall short in addressing the design challenges of LLMs."
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)
- [2021_Li_RaQu_TCAD](2021_Li_RaQu_TCAD.md) RaQu (2021)
- [2021_Yuan_TinyADC_DATE](2021_Yuan_TinyADC_DATE.md) TinyADC (2021)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED](2023_Saxena_ADCLessCiMPartialSumQuant_ISLPED.md) ADC-Less CiM Partial-Sum Quant (2023)
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)
- [2023_Cui_ARES_ICCAD](2023_Cui_ARES_ICCAD.md) ARES (2023)
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024)
- [2024_Ahsan_SPICEenvmACIMFramework_ICCAD](2024_Ahsan_SPICEenvmACIMFramework_ICCAD.md) SPICE eNVM ACIM Framework (2024)
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Mai_CIMWise_ICCAD](2025_Mai_CIMWise_ICCAD.md) CIMWise (2025)
- [2025_Li_HARMONY_TCAD](2025_Li_HARMONY_TCAD.md) HARMONY (2025)
- [2025_Xiong_ASMA_ICCD](2025_Xiong_ASMA_ICCD.md) ASMA (2025)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2019_Ankit_PUMA_ASPLOS.pdf](../../03_Crossbar_Accelerator_Architectures/2019_Ankit_PUMA_ASPLOS.pdf)
- Full text: [../fulltext/2019_Ankit_PUMA_ASPLOS.txt](../fulltext/2019_Ankit_PUMA_ASPLOS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3297858.3304049
