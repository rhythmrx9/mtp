---
id: W4411926812
key: 2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng
title: "Deep learning software stacks for analogue in-memory computing-based accelerators"
short: "AIMC Software Stacks"
year: 2025
venue: "NatRevElectrEng"
venue_full: "Nature Reviews Electrical Engineering"
authors: "Corey Lammie, Hadjer Benmeziane, William Simon, Elena Ferro, Athanasios Vasilopoulos, Julian Büchel, Manuel Le Gallo, Irem Boybat, Abu Sebastian"
category: "01 Surveys & Foundations"
devices: ["PCM", "Generic-NVM", "ReRAM", "Flash", "SRAM-analog"]
models: ["CNN", "Transformer", "GPT/LLM"]
lm_models: []
param_scale: ""
slm: false
evidence: survey
topics: ["survey", "compiler-software-stack", "heterogeneous-analog-digital", "tiling-partitioning", "scheduling", "dataflow-pipelining", "hardware-aware-training", "calibration-compensation", "chip-in-the-loop"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 1
cites_in_collection: 20
citations_overall: 7
priority_score: 8.03
doi: "https://doi.org/10.1038/s44287-025-00187-1"
pdf: "../../01_Surveys_and_Foundations/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.pdf"
fulltext: "../fulltext/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.txt"
---

# AIMC Software Stacks

**Deep learning software stacks for analogue in-memory computing-based accelerators** — Nature Reviews Electrical Engineering (2025)

## TL;DR
Perspective explaining why standard DL compiler stacks do not transfer to heterogeneous AIMC+DPU accelerators (weight stationarity, inter-layer pipelining, stochastic noise) and outlining five research directions for AIMC-specific software stacks.

## Summary
The paper gives an overview of DL software stacks (front end, IRs/dialects, graph optimisation, compiler, back end, feedback-directed optimisation) and of existing tools (PyTorch/TensorFlow/ONNX, TVM, LLVM, XLA, Glow, TensorRT, OpenVINO, MLIR). It then lists four attributes of AIMC accelerators that complicate stack design: co-located heterogeneous processing units (DPUs for activations, attention and noise-sensitive MVMs), analogue noise (deterministic and stochastic), fixed weight stationarity with required pipelined execution across layers, and the analogue-to-digital conversion path and inter/intra-tile weight mapping. Box 1 describes the standard pre-deployment flow: hardware-aware retraining with Gaussian weight noise and quantised I/O, post-placement calibration (input range, conductance range), and chip-in-the-loop retraining. A conceptual AIMC stack (Fig. 3) is proposed, with the parts needing extension highlighted, plus feedback-directed optimisation using proxy metrics such as the analogue MAC ratio. Table 1 compares existing IMC compilation tools (e.g. PUMA, DNN+NeuroSim, OCC, CIM-MLC, PIMCOMP) on openness and framework interfaces. The authors argue that most tools are closed source, benchmarking is non-standardised, and conclude with five themes: framework integration, IR standardisation, joint placement/routing/scheduling, accuracy-preserving HWA training/calibration, and model serving including LLM KV-cache management. No new experiments are reported.

## Contributions
- Concise tutorial on DL software stack components (IRs, dialects, passes, FDO) aimed at AIMC hardware designers
- Identification of four AIMC attributes (heterogeneity, noise, weight stationarity, ADC/DAC path and tile mapping) that break assumptions of conventional compilers
- Conceptual AIMC software stack with feedback loops and analogue MAC ratio as a proxy metric
- Comparison table of IMC compilation tools and five research opportunities

## Key claims (stable IDs)
- **2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng#C1** — Existing DL compilers are not directly applicable to AIMC accelerators because they assume weight reloading and intra-layer parallelism — _support:_ AIMC needs layer-pipelined, weight-stationary execution since NVM programming is slow and endurance-limited — _loc:_ Key attributes of AIMC-based accelerators, Fixed weight stationarity
- **2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng#C2** — Noise-sensitive operations should be offloaded to DPUs, making placement an accuracy-critical decision — _support:_ AIMC tiles used for less sensitive static MVMs; dynamic MVMs, accumulation, activations and normalisation on DPUs — _loc:_ Key attributes, Noise
- **2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng#C3** — Chip-in-the-loop retraining is hard to scale to LLMs and is hardware-instance specific — _support:_ Prone to overfitting, limited by device endurance, needs extra circuitry/memory — _loc:_ Research opportunities, accuracy section
- **2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng#C4** — Most AIMC compilation tools are closed source and compared non-uniformly — _support:_ Table 1 observations; comparisons use normalised tokens/s or TOPS/W — _loc:_ Table 1 discussion

## Results
- Qualitative only: motivating figures include GPUs at >5 TOPS/W (about 8.35 TOPS/W for H100 NVL at 400 W) and edge TPU at 2 TOPS/W versus IMC prototypes at sustained >10 TOPS/W and heterogeneous AIMC projected >50 TOPS/W (Introduction)
- No experimental results; Table 1 compares tool features, not performance

## Key numbers
- energy_eff: >10 TOPS/W sustained (IMC prototypes); >50 TOPS/W projected (heterogeneous AIMC)

## Limitations
- Perspective with no new experiments or benchmarks
- Focus on weight-stationary NVM AIMC; digital and SRAM-based IMC only briefly covered
- LLM-specific issues (KV cache, dynamic MVMs in attention) mentioned briefly
- Text extraction garbled the reference numbering, so some citation contexts could not be located

## Remarks
The clearest statement in the collection of why mapping and compilation for analog hardware is its own research problem, written by the IBM group behind the PCM AIMC chips and AIHWKIT. It frames the heterogeneous AIMC+DPU design point that transformer/LLM work (attention, KV cache on DPUs) relies on. It is a foundations text for category 05 papers (PIMCOMP, CIM-MLC, LionHeart) and category 07 HWA-training papers, rather than evidence of its own.

## Use in the original review
- F11 (Medium confidence): Heterogeneous architecture is the consensus design point: AIMC tiles combined with digital processing units, because analog tiles alone cannot execute an end-to-end deep neural network.
- R2 (Refuted 0–3): “Conventional deep-learning compiler stacks (TVM, Glow, nGraph) cannot be reused for AIMC, making software a first-order bottleneck.”

## Cites (in collection, 20)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "There are a broad range of DPU types, from general-purpose core-based units that accelerate a wide range of operations to more specialized units, for certain specific operations, that are optimized for lower latency9,13,29."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2021_Siemieniuk_OCC_TCAD](2021_Siemieniuk_OCC_TCAD.md) OCC (2021) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "although the effect of these on accuracy can be mitigated using different techniques (such as hardware-aware (HWA) training31, post-placement calibration methods and chip-in-the-loop retraining; Box 1), AIMC tiles remain unsuitable for particularly sensitive operations."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2024_Lammie_AIMCPostTrainingOpt_ISCAS](2024_Lammie_AIMCPostTrainingOpt_ISCAS.md) AIMC Post-Training Optimization (2024) — _background_: "Post-placement calibration methods42 help mitigate accuracy loss caused by mismatches between the assumed hardware during HWA model adaptations and the actual hardware used for deployment."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _baseline/comparison_: "Table 1 provides an overview and comparison of different compilation tools that can be used to automatically deploy general-purpose kernels and DL workloads to IMC-based accelerators."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023)
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024)
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024)
- [2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun](2025_Lammie_InherentAdversarialRobustnessAIMC_NatCommun.md) AIMC-Adversarial-Robustness (2025)
- [2025_Lammie_LionHeart_TETC](2025_Lammie_LionHeart_TETC.md) LionHeart (2025)
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023)

## Cited by (in collection, 1)
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "However, distinct properties of AIMC, namely device noise and circuit non-idealities, introduce additional complexity to NN training and deployment6."

## Files
- PDF: [../../01_Surveys_and_Foundations/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.pdf](../../01_Surveys_and_Foundations/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.pdf)
- Full text: [../fulltext/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.txt](../fulltext/2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s44287-025-00187-1
