---
id: W4392367648
key: 2024_Aguirre_MemristorANNHWReview_NatCommun
title: "Hardware implementation of memristor-based artificial neural networks"
short: "Memristor ANN HW Review"
year: 2024
venue: "NatCommun"
venue_full: "Nature Communications"
authors: "Fernando Leonel Aguirre, Abu Sebastian, Manuel Le Gallo, Wenhao Song, Tong Wang, J. Joshua Yang, Wei Dong Lu, Meng‐Fan Chang, Daniele Ielmini, Yuchao Yang, Adnan Mehonić, Anthony Joseph Kenyon et al."
category: "01 Surveys & Foundations"
devices: ["Memristor(generic)", "ReRAM", "PCM", "Flash"]
models: ["MLP", "CNN", "SNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "crossbar-architecture", "adc-dac", "peripheral-circuits", "simulator", "benchmarking", "on-chip-training", "device-variation", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 33
citations_overall: 497
priority_score: 8.42
doi: "https://doi.org/10.1038/s41467-024-45670-9"
pdf: "../../01_Surveys_and_Foundations/2024_Aguirre_MemristorANNHWReview_NatCommun.pdf"
fulltext: "../fulltext/2024_Aguirre_MemristorANNHWReview_NatCommun.txt"
---

# Memristor ANN HW Review

**Hardware implementation of memristor-based artificial neural networks** — Nature Communications (2024)

## TL;DR
A Nature Communications review (Aguirre et al., 2024) walking through every block of a memristor-based ANN (devices, crossbars, DAC/ADC and peripherals, learning/programming, metrics, prototypes, simulators), with tables of published prototype chips, performance versus full-CMOS accelerators, and simulation frameworks.

## Summary
The review frames hybrid CMOS/memristor ANNs as an answer to the von Neumann data-movement bottleneck and gives a protocol-style description for newcomers. It describes memristive device types and the 1T1R/crossbar structure; the blocks of a complete system (input DACs or time-encoding, crossbar, TIAs/current sensing, ADCs, activation functions, buffers, control), with discussion of how fully on-chip integration differs from systems using off-chip electronics (Table 1 lists reported prototypes and which blocks are on-chip). It covers weight mapping (differential pairs, bias columns) and the key trade-off between ADC/DAC precision and energy/area (ADC can take 70-90% of crossbar-unit area and 80-88% of energy), then learning and programming schemes (supervised learning, write-verify, mixed-precision training, in-situ vs ex-situ) and evaluation metrics (Table 2: accuracy, precision, recall, etc., plus electrical metrics). Table 3 compares advanced hybrid RRAM/CMOS prototypes with commercial full-CMOS accelerators (throughput, density, efficiency); Table 4 surveys simulation frameworks across device, circuit, architecture and NN levels (MNSIM, NeuroSIM, PUMA, CIM-SIM, XB-SIM, IBM aihwkit, DL-RSIM, MemTorch, etc.); Table 5 compares accuracies of memristor ANNs across network types and learning algorithms. The review is concerned with MLP/CNN/SNN class networks; transformers and language models are not treated (only ChatGPT is mentioned in the introduction).

## Contributions
- Block-by-block description of memristor-based ANN hardware with design alternatives and trade-offs (e.g., DAC schemes, ADC sharing, time-encoding)
- Tabulated comparison of published hybrid CMOS/memristor prototypes and their on-chip vs off-chip blocks (Table 1) and against full-CMOS accelerators (Table 3)
- Catalogue of simulation frameworks at device, circuit, architecture and neural-network abstraction levels (Table 4, Fig. 15)
- Metric definitions and accuracy comparisons for pattern-classification memristive ANNs (Tables 2 and 5) plus supplementary code examples

## Key claims (stable IDs)
- **2024_Aguirre_MemristorANNHWReview_NatCommun#C1** — ADC/DAC overhead dominates hybrid memristor accelerators — _support:_ ADC can consume up to 70-90% of crossbar-unit area and up to 80-88% of energy — _loc:_ Peripheral circuits section (ADC)
- **2024_Aguirre_MemristorANNHWReview_NatCommun#C2** — Hybrid RRAM/CMOS prototypes reach throughput similar to full-CMOS accelerators but are often area-limited by ADCs — _support:_ Table 3 comparison — _loc:_ Table 3 and surrounding text
- **2024_Aguirre_MemristorANNHWReview_NatCommun#C3** — Truly full on-chip hybrid CMOS/memristor systems appeared only in the last two years — _support:_ Review conclusion; performance of systems relying on off-chip electronics must be analysed carefully — _loc:_ Concluding section
- **2024_Aguirre_MemristorANNHWReview_NatCommun#C4** — Device-hardware co-design and realistic electrical simulation are indispensable — _support:_ Conductance states and linearity set peripheral requirements — _loc:_ Concluding section

## Results
- No new experiments; main outputs are Tables 1-5 (prototype list, metrics, hybrid vs full-CMOS performance, simulator list, network accuracies)
- At least 8-bit ADC resolution reported necessary for >90% accuracy for ResNet50-1.5 on ImageNet (cited from Xiao et al.)
- Sharing/multiplexing DACs reduces area at cost of throughput; time-encoding allows one DAC per channel without losing input resolution

## Key numbers
- accuracy: >90% ImageNet with >=8-bit ADC (cited)
- bits_adc: >=8b for ResNet50-1.5

## Datasets / benchmarks
MNIST, ImageNet (as cited accuracy reference)

## Limitations
- A survey: no unified benchmark; reported numbers from heterogeneous prototypes are not normalised
- Focus on MLP, CNN and SNN pattern classification (largely MNIST-scale); no treatment of transformers, attention, LLMs or analog nonlinearity/softmax
- Table contents are partly garbled in text extraction (Tables 1, 3, 4 columns), so exact entries could not be verified here
- Published in 2024; later analog-AI and transformer accelerators are not covered

## Remarks
Useful entry-level reference for understanding block-level costs (ADC, DAC, TIA) and the vocabulary of memristive ANN hardware, and a good pointer list of prototypes and simulators that map onto categories 02, 03 and 08 of the collection. Its blind spot for transformers and LMs means it frames the problem at the MLP/CNN level, while later analog-AI work in the collection addresses attention, KV caches and LLMs. Treat its performance tables as secondary-source summaries.

## Cites (in collection, 33)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Multi-layer Perceptron (MLP), Convolutional Neural Networks (CNNs), Spiking Neural Networks (SNNs), among others (see Table 5)."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "Alternatives to overcome this limitation have been proposed, as for instance the simulator developed by Song et al. to evaluate their PipeLayer architecture, which considers highly parallel designs based on the notion of parallelism granularity and weight replication."
- [2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron](2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.md) Mixed-Precision IMC (2018) — _background_: "Mixed-precision training, which accumulates the weight update in software and only updates the memristor devices when the accumulated value surpasses the programming granularity, can greatly relax requirement for conductance update resolution and endurance and allow software-comparable accuracy to be achieved."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "A cost-effective recurrent solution has been to use a smaller number of DACs and share them among different rows by adding a layer of analogue multiplexors between the DACs and the wordline inputs."
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018) — _uses-method-or-tool_: ""Whitin this group, we found for instance the DL-RSIM simulator, proposed by Lin et al., which simulates the error rates of every sum-of-products computation in memristor-based accelerators externally, and injects the errors in targeted TensorFlow-based neural network models.""
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _uses-method-or-tool_: ""Moreover, ADC can consume up to 70-90% of the on-chip area of the crossbar-based computation unit, including memristive crossbar and peripheral circuits, and up to 80-88% of energy." ... "Then, moving forward with the path toward the most accurate memristive neural network simulators, the PUMAsim proposed by Ankit et al. uses Verilog HDL to model the tiles and cores at the Register Transfer Level, which allows them to be mapped into a 45 nm Silicon-on-Insulator CMOS process for area estimation.""
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "To avoid this loss of accuracy, hardware-aware training methods, in which device non-idealities are incorporated during training have been proposed in the literature."
- [2019_Yuan_ADMMMemristorPruning_ISLPED](2019_Yuan_ADMMMemristorPruning_ISLPED.md) ADMM Memristor Prune+Quant (2019) — _background_: "However, the negative side is that these are rather closed pieces of software, which has been partially solved by Ma et al. and Yuan et al., by using PyTorch instead of TensorFlow, focusing in this case on the weight pruning and quantization effects."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: ""To avoid this loss of accuracy, hardware-aware training methods, in which device non-idealities are incorporated during training have been proposed in the literature." (co-cited with Joshi et al. computational PCM paper)"
- [2020_Ma_TinyButAccurate_ASPDAC](2020_Ma_TinyButAccurate_ASPDAC.md) P-RM Memristor Framework (2020) — _background_: "However, the negative side is that these are rather closed pieces of software, which has been partially solved by Ma et al. and Yuan et al., by using PyTorch instead of TensorFlow, focusing in this case on the weight pruning and quantization effects."
- [2020_Fei_XBSIM_TST](2020_Fei_XBSIM_TST.md) XB-SIM* (2020) — _background_: "Other architectural-level simulators proposed in the literature and following a very similar approach include CIM-SIM and XB-SIM."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _data/numbers_: "ADCs with at least 8-bit resolution are necessary to achieve high (>90%) classification accuracy in a ResNET50-1.5 ANN used to classify the ImageNET database."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Finally, the most advanced prototypes exploit the time-encoding scheme, which simplifies the DAC design and allows one DAC per channel, without losing resolution of the input vector."
- [2022_Li_40nmMLCRRAMCIMMacro_JSSC](2022_Li_40nmMLCRRAMCIMMacro_JSSC.md) 40nm MLC-RRAM CIM Macro (2022) — _background_: "For this reason, these approaches have been demonstrated mostly for the weight update of isolated devices, with just a few examples of on-chip integrated approaches."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "The other method is sharing a single ADC across several columns or using a single ADC per crossbar tile."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _data/numbers_: "Figure/table adaptation note: performance comparison chart adapted with permission, citing the 'Analog-AI Using Dense 2-D Mesh' architecture alongside DaDianNao and 3D-aCortex in the throughput/process-node comparison."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _background_: "Nonetheless, for full on-chip integration of memristive neural network, the impact of ADC resolution on VMM accuracy needs to be carefully evaluated to identify the lowest ADC resolution (and thereby required Silicon area) while preserving the neural network accuracy."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "To avoid this loss of accuracy, hardware-aware training methods, in which device non-idealities are incorporated during training have been proposed in the literature."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "To overcome this challenge, Xia et al. presented MNSIM and Zhu et al. presented the successor MNSIM 2.0."
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019)
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)

## Cited by (in collection, 6)
- [2024_Chowdhury_MELISO_ICONS](2024_Chowdhury_MELISO_ICONS.md) MELISO (2024) — _background_: "Emerging non-volatile memory technologies, such as resistive random access memories (RRAMs) based crossbar arrays, provide a versatile solution to the challenges of data-intensive, large-scale computational tasks [6, 7]."
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _motivation_: "To maximize the hardware efficiency of CIM accelerators and maintain high performance for neural network workloads, it is essential to co-optimize both neural network model parameters and CIM hardware parameters [7]."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _contrasts/critiques_: "Whereas previous research studies and reviews4,17,18 have investigated the device innovations, crossbar architectures or hardware–algorithm co-optimization strategies, they rarely scrutinize the accuracy–overhead trade-off that is inherent to these solutions."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)
- [2025_Xiong_ASMA_ICCD](2025_Xiong_ASMA_ICCD.md) ASMA (2025)

## Files
- PDF: [../../01_Surveys_and_Foundations/2024_Aguirre_MemristorANNHWReview_NatCommun.pdf](../../01_Surveys_and_Foundations/2024_Aguirre_MemristorANNHWReview_NatCommun.pdf)
- Full text: [../fulltext/2024_Aguirre_MemristorANNHWReview_NatCommun.txt](../fulltext/2024_Aguirre_MemristorANNHWReview_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-024-45670-9
