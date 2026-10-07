---
id: W4408145534
key: 2025_Lammie_LionHeart_TETC
title: "LionHeart: A Layer-Based Mapping Framework for Heterogeneous Systems With Analog In-Memory Computing Tiles"
short: "LionHeart"
year: 2025
venue: "TETC"
venue_full: "IEEE Transactions on Emerging Topics in Computing"
authors: "Corey Lammie, Yuxuan Wang, Flavio Ponzina, Joshua Alexander Harrison Klein, Hadjer Benmeziane, Marina Zapater, Irem Boybat, Abu Sebastian, Giovanni Ansaloni, David Atienza"
category: "05 Mapping, Compilation & Dataflow"
devices: ["PCM", "Generic-NVM"]
models: ["CNN", "ResNet", "VGG", "MobileNet", "Transformer", "BERT"]
lm_models: ["MobileBERT (24.8M weights, SQuAD)"]
param_scale: "~25M"
slm: true
evidence: algorithm+simulation
topics: ["weight-mapping", "heterogeneous-analog-digital", "hardware-aware-training", "conductance-drift", "scheduling", "energy-efficiency", "edge-ai", "language-models"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 8
citations_overall: 10
priority_score: 8.66
doi: "https://doi.org/10.1109/tetc.2025.3546128"
pdf: "../../05_Mapping_Compilation_and_Dataflow/2025_Lammie_LionHeart_TETC.pdf"
fulltext: "../fulltext/2025_Lammie_LionHeart_TETC.txt"
---

# LionHeart

**LionHeart: A Layer-Based Mapping Framework for Heterogeneous Systems With Analog In-Memory Computing Tiles** — IEEE Transactions on Emerging Topics in Computing (2025)

## TL;DR
LionHeart greedily decides, layer by layer under a user-set accuracy-drop threshold (with hardware-aware retraining and PCM drift), which DNN/MobileBERT layers run on AIMC tiles versus digital cores, giving up to ~6x (e.g. 425% on AlexNet at 5% drop, 285% VGG16) simulated speedup/energy gains over an int8 digital baseline.

## Summary
AIMC crossbars accelerate MVMs but introduce noise, ADC/DAC limits and temporal PCM drift, so fully analog mapping degrades accuracy. LionHeart explores hybrid digital/analog mappings: layers are sorted by MAC count (largest first, giving linear rather than exponential search), each layer is tentatively converted to an analog AIHWKIT layer (PCM-like noise model, 256x256 tiles, ADC/DAC with dynamic scaling and clipping), hardware-aware retrained with multiplicative Gaussian weight noise, and kept analog only if the cumulative accuracy drop stays within the global threshold at a user-defined evaluation time t_eval (so drift is accounted for). Evaluated on ResNet8, ResNet20, MobileNetV2, VGG16, AlexNet on CIFAR-10/100 and on MobileBERT (169 mappable layers, SQuAD F1 90.2 baseline). Performance and energy come from a gem5-X cycle-accurate ARMv8 simulator with tightly coupled AIMC tiles (ALPINE), int8 digital baseline using NEON SIMD. Compared against DIANA (Ueyoshi) and Harmonica mappings, plus an exhaustive HWA-trained Pareto front for ResNet8.

## Language models evaluated
- Models: MobileBERT (24.8M weights, SQuAD)
- Scale: ~25M

## Contributions
- Accuracy-driven heuristic for hybrid digital/analog layer mapping with linear exploration complexity
- Hardware-agnostic framework built on AIHWKIT with hardware-aware retraining per candidate mapping
- Temporal-drift-aware mapping at user-chosen evaluation time
- System-level gem5-X evaluation of speedup/energy and comparison with DIANA and Harmonica; exhaustive Pareto upper bound on ResNet8

## Key claims (stable IDs)
- **2025_Lammie_LionHeart_TETC#C1** — A sizable share of MACs can run on AIMC even at tight accuracy thresholds — _support:_ almost 60% of ResNet-8 computation analog at 5% threshold, whereas all-analog loses ~20% accuracy — _loc:_ Sec. VI-D / Fig. 5
- **2025_Lammie_LionHeart_TETC#C2** — Achievable speedup depends on DNN structure — _support:_ MobileNetV2 only +24% even fully analog; VGG16 660% and AlexNet 550% full-analog — _loc:_ Sec. VI-E / Fig. 6
- **2025_Lammie_LionHeart_TETC#C3** — At 5% accuracy drop LionHeart captures most potential speedup — _support:_ 425% AlexNet, 285% VGG16 — _loc:_ Sec. VI-E / Fig. 6
- **2025_Lammie_LionHeart_TETC#C4** — First and intermediate layers are most sensitive to analog noise; first attention layers of MobileBERT are amenable but bottleneck layers are not — _support:_ Table III conversion percentages — _loc:_ Sec. VI-D / Table III

## Results
- Run-time and energy gains exceeding 6x vs fully digital baseline at user accuracy threshold (abstract)
- AlexNet 425% and VGG16 285% speedup at 5% drop; full-analog upper bounds 550% / 660% (Fig. 6)
- MobileNetV2 full-analog upper bound only 24% speedup due to depthwise-conv low data reuse
- System energy gains closely follow speedup because AIMC tiles are minor contributors to system power
- Effective Op/s are 57% (AIMC system) and 35% (baseline) of peak

## Key numbers
- array_size: 256x256
- throughput: up to 425% speedup (AlexNet, 5% drop)
- accuracy: MobileBERT baseline F1 90.2 (SQuAD)

## Datasets / benchmarks
CIFAR-10, CIFAR-100, SQuAD

## Limitations
- Simulation only (AIHWKIT noise model + gem5-X), no silicon; PCM only modelled
- Heuristic with stochastic outcomes and a global drop threshold that can be consumed by early layers
- Single CPU core with tightly coupled tiles; no multi-tile NoC or full SoC
- One transformer (MobileBERT, ~25M) on SQuAD; no decoder LLM and no KV-cache/attention-matrix modelling
- Retraining time overhead of per-layer HWA training not quantified

## Remarks
A practical, open-source (IBM) mapping tool that makes the accuracy-versus-speedup trade-off explicit and is one of the few mapping works to include a transformer language model and PCM drift. MobileBERT results hint that not all layers are equally analog-friendly, an insight relevant to heterogeneous mapping of SLMs. Evidence is simulation-based and small-scale relative to modern SLMs, but it is cited by later AIMC software-stack and LoRA-adapter work in the collection.

## Cites (in collection, 8)
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _uses-method-or-tool_: "Architectures can utilize IMC at different levels of the memory hierarchy, for example, when interfacing main memory [10], as part of smart caches [11], or as functional units that augment processor pipelines and register files [4]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "We employ the open-source AIHWKIT toolkit [5] to expose these behaviours using systemlevel explorations in LionHeart, allowing both the realistic characterization of analog non-idealities and analog HWA retraining."
- [2023_Benmeziane_AnalogNAS_EDGE](2023_Benmeziane_AnalogNAS_EDGE.md) AnalogNAS (2023) — _background_: "The rationale behind this approach is that larger layers have more redundancy and, hence, more leeway to compensate for the perturbations induced by analog computing [5, 6]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _data/numbers_: "For instance, a 256×256 Phase Change Memory (PCM) crossbar is shown to perform a total of 65,536 MAC operations in 130ns in Le Gallo et al. [12]."
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _baseline/comparison_: "PUMA [16] employs compiler analysis passes to define which parts of the application have the most potential for speedup, while AERO [17] formulates this same problem as a cost function minimization."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _contrasts/critiques_: "They are similarly disregarded in [18] and [19], where all FC and CONV layers are executed using AIMC tiles, without attempting to control induced accuracy degradation."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _extends/builds-on_: "While not investigated in this paper, it is possible to extend the methodology of LionHeart to co-apply different techniques to further improve accuracy, e.g., tunable ADC resolutions in RAELLA [25]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _data/numbers_: "This is in agreement with prior work [30]."

## Cited by (in collection, 2)
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "This challenge represents a typical resource allocation problem34."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)

## Files
- PDF: [../../05_Mapping_Compilation_and_Dataflow/2025_Lammie_LionHeart_TETC.pdf](../../05_Mapping_Compilation_and_Dataflow/2025_Lammie_LionHeart_TETC.pdf)
- Full text: [../fulltext/2025_Lammie_LionHeart_TETC.txt](../fulltext/2025_Lammie_LionHeart_TETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tetc.2025.3546128
