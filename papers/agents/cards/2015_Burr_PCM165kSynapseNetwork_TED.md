---
id: W1937359183
key: 2015_Burr_PCM165kSynapseNetwork_TED
title: "Experimental Demonstration and Tolerancing of a Large-Scale Neural Network (165 000 Synapses) Using Phase-Change Memory as the Synaptic Weight Element"
short: "PCM 165k-Synapse Network"
year: 2015
venue: "TED"
venue_full: "IEEE Transactions on Electron Devices, 2015"
authors: "Geoffrey W. Burr, Robert M. Shelby, Severin Sidler, Carmelo di Nolfo, Junwoo Jang, Irem Boybat, Rohit S. Shenoy, Pritish Narayanan, Kumar R. Virwani, Emanuele U. Giacometti, Bulent N. Kurdi, Hyunsang Hwang"
category: "10 On-chip & Analog Training"
devices: ["PCM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["on-chip-training", "analog-mvm", "device-variation", "chip-demo"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 37
cites_in_collection: 0
citations_overall: 941
priority_score: 8.31
doi: "https://doi.org/10.1109/ted.2015.2439635"
pdf: null
fulltext: null
---

# PCM 165k-Synapse Network

**Experimental Demonstration and Tolerancing of a Large-Scale Neural Network (165 000 Synapses) Using Phase-Change Memory as the Synaptic Weight Element** — IEEE Transactions on Electron Devices, 2015 (2015)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
IBM demonstrates a three-layer perceptron with 164,885 synapses, each a pair of phase-change memory devices, trained in situ with a backpropagation variant suited to NVM+selector crossbars, reaching 82.2% train / 82.9% test accuracy on a 5000-example MNIST subset, and uses a matched simulator to tolerance how much PCM variability, yield, stochasticity, nonlinearity and asymmetry can be tolerated before accuracy collapses.

## Summary
The paper addresses whether phase-change memory (PCM), as a non-volatile analog synaptic weight element, can support training of a reasonably large neural network despite its non-ideal conductance-update behavior (noise, nonlinearity, asymmetry between potentiation and depression, device-to-device variability, and imperfect yield). Each synaptic weight is represented differentially by two PCM devices, and a large-scale three-layer perceptron (164,885 synapses) is built/operated and trained with a backpropagation-derived weight-update rule adapted for crossbar arrays with an access device (selector) at each cell, on a 5,000-example subset of MNIST. The experimental system achieves 82.2% training accuracy and 82.9% generalization (test) accuracy. To go beyond what the hardware demonstrator alone could probe, the authors build a neural-network simulator calibrated to match the experimental PCM array and use it to perform extensive tolerancing studies, sweeping NVM variability, device yield, and the stochasticity/linearity/asymmetry of the conductance response. The central finding is that a bidirectional NVM device with a symmetric, linear, high-dynamic-range conductance response can in principle match the accuracy of a conventional software-trained network on this task, identifying which device non-idealities are and are not tolerable for on-chip/analog training.

## Contributions
- Large-scale (164,885-synapse) experimental demonstration of an on-chip-trainable neural network using PCM devices as the synaptic weight element, with two PCM devices per differential synapse
- Adapts the backpropagation weight-update rule to a form compatible with NVM+selector crossbar arrays for in-situ training
- Achieves 82.2% training / 82.9% generalization accuracy on a 5,000-example MNIST subset with real PCM hardware
- Builds and calibrates a neural-network simulator matched to the experimental PCM demonstrator to extend analysis beyond the hardware's own scale/conditions
- Performs extensive tolerancing of PCM-array non-idealities (variability, yield, stochasticity, conductance-response linearity and asymmetry) to identify the device requirements for analog on-chip training to match software baseline accuracy

## Key claims (stable IDs)
- **2015_Burr_PCM165kSynapseNetwork_TED#C1** — A PCM-based crossbar network can be trained in situ to reach close to the accuracy of a software-trained equivalent network on a reduced MNIST task — _support:_ 82.2% training accuracy and 82.9% generalization accuracy reported for the experimental 164,885-synapse PCM network (abstract) — _loc:_ Abstract
- **2015_Burr_PCM165kSynapseNetwork_TED#C2** — A bidirectional NVM device with symmetric, linear, high-dynamic-range conductance response is sufficient to match conventional software-based classification accuracy on this problem — _support:_ Simulator-based tolerancing results (as stated in the abstract) show such a device profile achieves accuracy parity with software — _loc:_ Abstract / tolerancing simulation results

## Results
- 164,885-synapse three-layer perceptron implemented with PCM devices (two PCM per synapse)
- 82.2% training accuracy and 82.9% generalization (test) accuracy on a 5,000-example MNIST subset
- Simulator-based tolerancing shows accuracy is sensitive to NVM variability, yield, and the stochasticity/linearity/asymmetry of the conductance response, with symmetric+linear+high-dynamic-range response needed to match software accuracy

## Limitations
- Analysis based on the paper's abstract only; full methodological details, exact figures/tables for the tolerancing sweeps, and specific numeric tolerance thresholds could not be independently verified in this pass
- Evaluated on a reduced 5,000-example subset of MNIST rather than the full dataset, and with a relatively small 3-layer perceptron by later standards
- Reported accuracies (~82%) are notably below the near-99% achievable by software MLPs on MNIST, reflecting the impact of real PCM device non-idealities
- Tolerancing conclusions are drawn from a simulator calibrated to, but not identical to, the physical hardware, so its generality beyond the specific PCM device model used is not established here

## Remarks
This is one of the earliest and most-cited large-scale hardware demonstrations of on-chip/analog training with PCM, establishing both a scaling milestone (164,885 synapses on real NVM) and a widely used tolerancing methodology (sweeping variability, yield, nonlinearity, and asymmetry against a calibrated simulator) that strongly influenced later PCM/ReRAM hardware-aware training work, including subsequent IBM papers on equivalent-accuracy analog training and PCM device models for deep learning. Because this entry is abstract-only (no verified open-access full text could be retrieved within the allotted attempts -- IBM Research, EPFL Infoscience, and Semantic Scholar mirrors were checked but the Infoscience OA copy was blocked by a bot-verification wall), the specific tolerancing numbers, figures and architecture details beyond what the abstract states should be confirmed against the original IEEE TED paper before being cited with precision.

## Cited by (in collection, 37)
- [2018_Kim_NonlinearIVAwareDNN_JETC](2018_Kim_NonlinearIVAwareDNN_JETC.md) Nonlinear-IV NN (2018) — _background_: "Since this approach can be several orders of magnitude more efficient than CMOS ASIC approaches in terms of both speed and power [3-6], many studies proposed neural network accelerators based on emerging NVM crossbar array [9-12]."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _uses-method-or-tool_: "In order to model these effects on the training of the algorithm, statistical data is extracted from the repeated pulsing between GMIN and GMAX following the methodology first presented in Burr et al [27, 36]."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _contrasts/critiques_: "Large neural networks (165 000 synapses) were demonstrated with PCM arrays,[42] but this work was limited by a sequential interface and could not carry out VMM computations in a single step with access to all word-lines and bit-lines simultaneously, as would be required for an actual computational accelerator."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _data/numbers_: "The sensitivity analysis [102] showed that eNVM-based ANN can be expected to be highly resilient to random effects (e.g., variability, yield, and stochasticity), but highly sensitive to gradient effects that act to steer all synaptic weights."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "Crosspoint MVM can be adopted for a broad range of problems, including image compression, sparse coding, and implementation of artificial neural networks (ANNs), where Gij has the meaning of a synaptic weight, Vj is a pre-synaptic spike amplitude, and Ii is the input signal to the ith neuron (refs 69, 70)."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _motivation_: "However, experimental demonstrations to date have been limited to discrete devices24,25 or small arrays and simplified problems26-31."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _background_: "RRAM [1, 9-14], PCRAM [15-17], MRAM [18], etc.) are being widely used in neural network (NN) accelerators."
- [2018_Deng_SemiMap_TCAD](2018_Deng_SemiMap_TCAD.md) SemiMap (2018) — _background_: "Besides conventional technologies, plenty of researches leverage modified SRAM [8]/ Flash [9] or various emerging non-volatile memory devices with in-memory computing capability to design this many-crossbar architecture, such as the most widely used RRAM (resistive RAM) [4–6, 19–24], PCRAM (phase-change RAM) [7, 25], and MRAM [26]."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "To overcome this limitation, memristor crossbars can store a matrix with high storage density and perform MVM operations with very low energy and latency [5, 13, 52, 87, 98, 116]."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _background_: "Fortunately, this type of behaviour is more relevant for in-situ training where it is necessary to ensure linear adjustment of ANN's weights [27]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Several experimental demonstrations (refs 4, 24-28) related to practical applications of in-memory computing have been reported as well."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "One approach is to perform a parallel weight update by sending deterministic or stochastic overlapping pulses from the rows and columns simultaneously to implement an approximate outer product and program the devices at the same time (Fig. 6b)107–111."
- [2021_Milo_RRAMProgramVerify_TED](2021_Milo_RRAMProgramVerify_TED.md) RRAM Program/Verify Schemes (2021) — _uses-method-or-tool_: "Namely by encoding the weight as the difference of two 1T1R conductances G+ and G- [3]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _contrasts/critiques_: "Prior to this, most of the demonstrations have been based on either simulation studies based on the measured characteristics of individual devices or on experiments based on PCM memory chips that were re-purposed for IMC operations [28]–[30]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Other emerging memory technologies (e.g., PCM) have also been used as synaptic weight elements [6], [68]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "Analogue memory-based DNN accelerators are being widely developed in academia and industry using a variety of memories5, including resistive RAM (ReRAM)6,7, conductive-bridging RAM (CBRAM)8, NOR flash9-12, magnetic RAM (MRAM), and phase-change memory (PCM)13,14."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "One approach is to perform a parallel weight update by sending deterministic or stochastic overlapping pulses from the rows and columns simultaneously to implement an approximate outer product and program the devices at the same time (Fig. 2(b))16,17,40 ."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Multi-layer Perceptron (MLP), Convolutional Neural Networks (CNNs), Spiking Neural Networks (SNNs), among others (see Table 5)."
- [2024_Wang_LearningInMemoryReview_NeuromorphComputEng](2024_Wang_LearningInMemoryReview_NeuromorphComputEng.md) Learning-in-Memory Review (2024) — _motivation_: "The non-uniform conductance change under identical write pulses would be a major problem of the online training [50, 54]."
- [2025_Yousuf_LayerEnsembleAveraging_NatCommun](2025_Yousuf_LayerEnsembleAveraging_NatCommun.md) Layer Ensemble Averaging (2025) — _background_: "Diverse technologies including resistive randomaccess memory (ReRAM) and phase change memory are being considered as promising crossbar candidates to implement the multiply and accumulate operations representing the standard synaptic weights model used in most neural networks11–19."
- [2018_Haensch_AnalogComputingDeepLearning_ProcIEEE](2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.md) Analog Computing for DL (Haensch) (2018) — _background_: "Despite this, PCM materials have been successfully used for deep learning [29, 39]."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _background_: "The simple and elegant in-RRAM dot product has been projected to achieve impressive performance and efficiency [5, 11, 21, 26, 29, 35]."
- [2018_Cheng_TIME_TCAD](2018_Cheng_TIME_TCAD.md) TIME (2018)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019)
- [2020_Lu_CIMAreaConstraintBenchmark_TVLSI](2020_Lu_CIMAreaConstraintBenchmark_TVLSI.md) CIM Area-Constraint Benchmark (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE](2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.md) Resistive Crossbars as Approximate HW (2020)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_Gao_BRoCoM_TCAD](2022_Gao_BRoCoM_TCAD.md) BRoCoM (2022)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2025_Haidar_CSPCMVisionSystem_ISCAS](2025_Haidar_CSPCMVisionSystem_ISCAS.md) CS-PCM Vision System (2025)
- [2025_Haidar_DriftAwarePCMRegularization_AICAS](2025_Haidar_DriftAwarePCMRegularization_AICAS.md) Drift-Aware PCM Regularization (2025)

## Files
- PDF: not available locally (save as `papers/10_On_Chip_and_Analog_Training/2015_Burr_PCM165kSynapseNetwork_TED.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/ted.2015.2439635
