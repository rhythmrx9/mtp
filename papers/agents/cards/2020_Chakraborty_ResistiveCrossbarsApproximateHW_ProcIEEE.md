---
id: W3042468132
key: 2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE
title: "Resistive Crossbars as Approximate Hardware Building Blocks for Machine Learning: Opportunities and Challenges"
short: "Resistive Crossbars as Approximate HW"
year: 2020
venue: "ProcIEEE"
venue_full: "Proceedings of the IEEE, vol. 108, no. 12, pp. 2276-2310 (2020)"
authors: "Indranil Chakraborty, Mustafa Ali, Aayush Ankit, Shubham Jain, Sourjya Roy, Shrihari Sridharan, Amogh Agrawal, Anand Raghunathan, Kaushik Roy"
category: "01 Surveys & Foundations"
devices: ["ReRAM", "PCM", "MRAM", "FeFET", "SRAM-analog", "Generic-NVM"]
models: ["MLP", "CNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "crossbar-architecture", "analog-mvm", "ir-drop-parasitics", "device-variation", "adc-dac", "write-verify-programming", "simulator", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 20
citations_overall: 140
priority_score: 7.03
doi: "https://doi.org/10.1109/jproc.2020.3003007"
pdf: "../../01_Surveys_and_Foundations/2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.pdf"
fulltext: "../fulltext/2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.txt"
---

# Resistive Crossbars as Approximate HW

**Resistive Crossbars as Approximate Hardware Building Blocks for Machine Learning: Opportunities and Challenges** — Proceedings of the IEEE, vol. 108, no. 12, pp. 2276-2310 (2020) (2020)

## TL;DR
Proceedings of the IEEE tutorial/review that frames NVM resistive crossbars as inherently approximate MVM engines, covering devices, peripherals, non-idealities, spatial inference/training accelerators (PUMA, PANTHER) and functional/performance modeling and compensation tools.

## Summary
The paper reviews resistive crossbars (PCM, RRAM, spintronic, FeFET) as building blocks for ML accelerators, arguing that crossbar computation is approximate on two axes: functional errors from device/circuit non-idealities and deliberate approximation in peripherals (mainly ADC precision). Sec. II covers device technologies (Table 1), peripherals (DAC/ADC, ADCs reported at up to ~80% of MVM-unit energy and ~70% of area), write operations (parallel write, bit-slicing) and silicon demonstrations (Table 2), plus a comparison to SRAM-based CMOS MVM macros. Sec. III classifies non-idealities into linear (wire, driver and sink resistance), nonlinear (device I-V, access device) and stochastic (process variation, write noise, temperature, endurance/retention) and gives crossbar models (including the fast crossbar model). Sec. IV describes spatial architectures (core/multicore/node hierarchy, bit-serial MVM units with shared 8-bit SAR ADCs per 128 columns) for inference (PUMA) and training (PANTHER with bit-sliced parallel writes), with energy comparisons to CPU/GPU/TPU. Sec. V covers DNN-to-crossbar mapping, functional simulators (RxNN/CxDNN, TxSim, GENIEx, NeuroSim) and compensation by retraining, mapping, and hardware. Models discussed are MLPs, CNNs and LSTMs; no transformers or language models are treated.

## Contributions
- Unified device-to-architecture-to-software view of resistive crossbar ML systems (Fig. 1)
- Taxonomy of read/write non-idealities (linear, nonlinear, random) and their effect on MVM output current
- Review of inference and training spatial architectures and their energy benefits vs CPU/GPU/TPU
- Survey of functional/performance modeling frameworks and compensation techniques (retraining, mapping, hardware)

## Key claims (stable IDs)
- **2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE#C1** — ADCs dominate energy and area of crossbar MVM units — _support:_ ADC up to ~80% of MVM-unit energy and ~70% of area; 8-10-bit ADCs typical — _loc:_ Sec. I, Sec. IV-G, Fig. 30
- **2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE#C2** — Non-idealities cause large accuracy loss on complex datasets for 64x64 crossbars with 6-bit precision — _support:_ accuracy degradation of 19.8%-57.8% for large networks on e.g. ImageNet, minimal for LeNet/ConvNet on MNIST — _loc:_ Sec. V-B, Fig. 32(a)
- **2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE#C3** — Retraining recovers accuracy lost to crossbar non-idealities — _support:_ 8%-27% accuracy improvement for AlexNet, VGG-16, GoogleNet with as few as 150 retraining iterations — _loc:_ Sec. V-C, Fig. 35(a)
- **2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE#C4** — ReRAM-based inference accelerator (PUMA) saves energy over CPU/GPU, most for LSTMs — _support:_ CNN up to 13x, MLP up to 80.1x, LSTM up to 2446x energy reduction vs Pascal GPU; peak area and power efficiency >9.7x and 1.8x vs TPU — _loc:_ Sec. IV-C, Fig. 26

## Results
- Inference energy reduction of a ReRAM accelerator (PUMA) vs GPU (Pascal): up to 13x CNN, 80.1x MLP, 2446x LSTM at batch size 1 (Fig. 26)
- Peak area/power efficiency over Google TPU: >9.7x and >1.8x (Sec. IV-C)
- Bit-sliced parallel-write training accelerator (PANTHER) shows large energy reduction vs Turing 2080Ti GPU for CNN and MLP across batch sizes (Fig. 29)
- Cell density: ~4F2 (12F2 for 1T-1R) vs 124F2 for 6T SRAM (Sec. VI)

## Key numbers
- array_size: 64x64 (non-ideality study); 128 columns per shared ADC (PUMA)
- accuracy: 19.8%-57.8% degradation for large DNNs at 64x64, 6-bit
- bits_weight: 6b (functional study)
- bits_adc: 8-bit SAR (PUMA)

## Datasets / benchmarks
MNIST, CIFAR-10, CIFAR-100, ImageNet

## Limitations
- Survey of 2020: no transformers, attention or language models
- Results are reprinted from cited works, not new experiments
- Mostly simulation-based accuracy/energy evidence; silicon demos are small
- Text extraction includes IEEE watermarks but body is intact

## Remarks
Strong 2020 bridge between device reviews and architecture papers, with a clear treatment of how ADC cost and non-idealities bound crossbar benefits. It predates transformer and LLM mapping, so dynamic matmul (attention), nonlinear functions and KV caches are absent; its LSTM/MLP energy-savings argument (low weight reuse favors crossbars) is the conceptual precursor of later claims for LLM decode. Useful background for RxNN, TxSim, GENIEx, PUMA and PANTHER in the collection.

## Cites (in collection, 20)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "For example, a defect map or variation distribution [153, 155, 157] of devices in the crossbar can aid the training process by mapping the sensitive cells to defect-free or low variation cells."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "For example, a defect map or variation distribution [153, 155, 157] of devices in the crossbar can aid the training process by mapping the sensitive cells to defect-free or low variation cells."
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _data/numbers_: "Second, the high write voltage [103] and multiple programming cycles (program-verify approach [45]) result in much higher write cost (energy and latency) than SRAM."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "nonvolatile memory (NVM) technologies [19, 20], such as phase-change memory (PCM) [21], resistive random access memory (RRAM) [22, 23], and spintronics [24], offer immense promise as an alternative to CMOS"
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "To that end, nonvolatile memory (NVM) technologies [19, 20], such as phase-change memory (PCM) [21], resistive random access memory (RRAM) [22, 23], and spintronics [24], offer immense promise as an alternative to CMOS due to their high storage density and the ability to perform massively parallel in situ MVM operations."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "In fact, researchers have been successful in experimentally demonstrating large-scale PCM crossbars for ML applications [21, 43]."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "This led to a growing interest in exploring NVM technology as the substrate for the next generation of ML hardware [19, 25, 26]."
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018) — _background_: "Previous works have focused on structured sparsity [165-167]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "One such simulator, CxDNN [130], is a functional simulator that maps low-precision DNNs to resistive crossbars."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _data/numbers_: "Fig. 26 shows the inference energy of a ReRam-based accelerator [30] compared with a CPU (Intel Skylake) and a GPU (NVIDIA Pascal)."
- [2020_Ankit_PANTHER_TC](2020_Ankit_PANTHER_TC.md) PANTHER (2020) — _extends/builds-on_: "To address such challenges, we describe a recently proposed technique to incorporate bit-slicing in the weight update operation [102] (see Section IV-E1)."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _data/numbers_: "Fig. 34. (a) Test accuracy versus epoch plots for various models, such as LeNet-5 and AlexNet, showing a more detrimental effect of device and circuit nonidealities for the deeper network (AlexNet). (b) Sensitivity of test accuracy to crossbar design parameters, such as crossbar size and RON/ROFF ratio (reprinted from [151])."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "Fig. 32(a) shows the degradation in accuracy for various benchmark DNNs."
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017) — _background_: "Previous works have focused on structured sparsity [165-167]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _baseline/comparison_: "For instance, ISAAC [29] and PUMA [30] adopted an 8-bit SAR ADC for higher precision computations, while XNOR-RRAM implemented a 3-bit flash ADC for binary input/weight computation [57]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 6)
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _data/numbers_: "As is illustrated in Figure 5, ADC consumes about 60% of the total energy, and over 80% of the chip area in CIM hardware [27]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _motivation_: "NVM devices also have very limited endurance, only about 10^6-10^9 conservative writes [8]–[10] which degrades the lifetime of these devices swiftly and limits their applicability to Transformers."
- [2023_Sun_PIMCOMP_DAC](2023_Sun_PIMCOMP_DAC.md) PIMCOMP (2023) — _background_: "The 2D crossbar structure formed by NVM devices has attracted growing interest due to its high memory density and parallel in-situ computing properties [4]."
- [2025_Kim_HASTILY_TCASAI](2025_Kim_HASTILY_TCASAI.md) HASTILY (2025) — _motivation_: "While emerging memories offer a high-density memory solution, they typically suffer from issues such as resistance drift, write endurance and/or low on-off distinguishability [50]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: [../../01_Surveys_and_Foundations/2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.pdf](../../01_Surveys_and_Foundations/2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.pdf)
- Full text: [../fulltext/2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.txt](../fulltext/2020_Chakraborty_ResistiveCrossbarsApproximateHW_ProcIEEE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jproc.2020.3003007
