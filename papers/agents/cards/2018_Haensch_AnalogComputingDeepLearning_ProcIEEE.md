---
id: W2896122000
key: 2018_Haensch_AnalogComputingDeepLearning_ProcIEEE
title: "The Next Generation of Deep Learning Hardware: Analog Computing"
short: "Analog Computing for DL (Haensch)"
year: 2018
venue: "ProcIEEE"
venue_full: "Proceedings of the IEEE, vol. 107, no. 1, pp. 108-122 (2019; online 2018)"
authors: "Wilfried E. Haensch, Tayfun Gokmen, Ruchir Puri"
category: "01 Surveys & Foundations"
devices: ["PCM", "ReRAM", "ECRAM", "FeFET", "Generic-NVM"]
models: ["MLP", "CNN", "LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: analytical
topics: ["survey", "analog-mvm", "on-chip-training", "device-variation", "adc-dac", "energy-efficiency", "crossbar-architecture", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 6
cites_in_collection: 4
citations_overall: 236
priority_score: 7.19
doi: "https://doi.org/10.1109/jproc.2018.2871057"
pdf: "../../01_Surveys_and_Foundations/2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.pdf"
fulltext: "../fulltext/2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.txt"
---

# Analog Computing for DL (Haensch)

**The Next Generation of Deep Learning Hardware: Analog Computing** — Proceedings of the IEEE, vol. 107, no. 1, pp. 108-122 (2019; online 2018) (2018)

## TL;DR
IBM Proc. IEEE perspective that NVM crossbars can execute deep-learning matrix operations in constant time, deriving from RPU simulations that training needs symmetric weight updates within 2%, ~1000 states (~10b), a 5b DAC/9b ADC and 6% integrator noise tolerance, whereas inference relaxes these constraints.

## Summary
The paper contrasts GPU-based DL training (mini-batch, distributed scaling, Eq. 1) with analog in-memory compute where an n x m NVM array performs n x m MACs in parallel by Kirchhoff's law, with forward, backward and update cycles using time-encoded pulses. Signed weights are realised differentially (G = G+ - G- or G_local - G_global). The authors built a simulation tool (Gokmen and Vlasov) capturing DAC/ADC accuracy, integrator SNR and device switching with device-to-device and cycle-to-cycle variation, and ran a 784-256-128-10 FCN on MNIST (235,000 weights) to derive material requirements (Fig. 7). A single-tile performance estimate (Fig. 8) assumes 80 ns integration, one 200 MS/s ADC at 23 pJ/sample per 16 rows/columns and R_dev = 24 MOhm. Section V reviews PCM, RRAM, ECRAM-like and ferroelectric materials against these needs, noting no material is a clear winner for training, while inference-only relaxes symmetry and state-count constraints (weights within 5% error suffice). The conclusion expects analog to augment rather than replace digital ecosystems.

## Contributions
- Quantitative device and interface requirements for analog DL training derived from RPU-style simulations
- Argument that NVM materials optimised for memory (binary, high SNR) are mismatched with DL needs (gradual symmetric updates)
- Single-tile performance model and NoC-level estimate (thousands of TOPS/W/s potential)
- Survey of PCM, RRAM, ferroelectric and other candidate materials against the requirements

## Key claims (stable IDs)
- **2018_Haensch_AnalogComputingDeepLearning_ProcIEEE#C1** — Training on analog arrays needs potentiation/depression symmetric within 2% and about 1000 conductance steps (~10b) when all variations are combined — _support:_ 'must be symmetric within 2%'; '1000 steps (~10 b)' — _loc:_ Sec. IV, Fig. 7
- **2018_Haensch_AnalogComputingDeepLearning_ProcIEEE#C2** — A 5-bit DAC and 9-bit ADC suffice and 6% noise at the integrator output is tolerable (0.3% penalty vs floating point) — _support:_ 'A 5-b DAC and a 9-b ADC are required, and a noise level of 6% can be tolerated' — _loc:_ Sec. IV, Fig. 7
- **2018_Haensch_AnalogComputingDeepLearning_ProcIEEE#C3** — Inference-only relaxes material constraints: replicating FP weights within 5% error reproduces classification error — _support:_ 'replication of the floating-point weights within a 5% error is sufficient' — _loc:_ Sec. V
- **2018_Haensch_AnalogComputingDeepLearning_ProcIEEE#C4** — Analog tiles could deliver thousands of TOPS/W/s on chip — _support:_ 80 ns integration, ADC 200 MS/s at 23 pJ/sample, R_dev=24 MOhm, 90 GB/s on-chip data rate for the largest tile — _loc:_ Sec. IV, Fig. 8

## Results
- FCN 784-256-128-10 (235k weights) on MNIST trained within 0.3% penalty of floating point under combined device sensitivities (Fig. 7)
- Single-tile performance estimate for input vectors of 500, 1000, 4000 (Fig. 8); largest tile needs 90 GB/s data rate

## Key numbers
- array_size: input vector 500/1000/4000 (tile model)
- energy_eff: thousands of TOPS/W/s (on-chip potential)
- accuracy: within 0.3% of FP on MNIST FCN
- bits_weight: ~10b states for training
- bits_adc: 9b ADC, 5b DAC

## Datasets / benchmarks
MNIST

## Limitations
- Analytical/simulation perspective; no measured hardware
- Sensitivity analysis done on a small MNIST FCN; authors state it is unclear whether it holds for massively scaled networks
- Training-centric requirements are stricter than inference needs
- Convolution mapping is only qualitatively addressed; no transformers/LMs

## Remarks
IBM's framing of RPU-style analog training and the symmetric-update requirement that motivated later ECRAM and Tiki-Taka work. For inference-mapping of LMs its requirements are overly stringent; later IBM papers show inference is feasible on PCM through hardware-aware training. Useful for ADC/DAC resolution rules of thumb.

## Cites (in collection, 4)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "With renewed interest in deep learning, it gained attention again as a possible solution to accelerate the required computations [26–28]."
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017) — _background_: "If we assume a time between weight updates of the order of 200 ns, and a retention time in the order of seconds, the updated weight will decay according to w ←w 1− . τret (12) This has the same form as the weight decay produced by L2 regularization [59] which is a method to avoid overfitting."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Despite this, PCM materials have been successfully used for deep learning [29, 39]."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)

## Cited by (in collection, 6)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _background_: "One promising future technology is the use of memristive crossbar arrays for accelerating the ubiquitous matrix-vector multiply and rank-update operations in ANNs by employing in-memory computation of matrices stored as analog quantities in tunable resistive elements [1,7,8,13]."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "The mechanism and operation of all analog MAC has also been described in detail elsewhere [59] [52] [57]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Analog in-memory computing AIMC is a promising future hardware technology for accelerating deep-learning workloads. Great energy efficiency is achieved by representing weight matrices in resistive elements of crossbar arrays and using basic physical laws of electrostatics (Kirchhoff's and Ohm's laws) to compute ubiquitous matrix-vector multiplications (MVMs) directly in memory in essentially constant time O(1)1-5."
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)

## Files
- PDF: [../../01_Surveys_and_Foundations/2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.pdf](../../01_Surveys_and_Foundations/2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.pdf)
- Full text: [../fulltext/2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.txt](../fulltext/2018_Haensch_AnalogComputingDeepLearning_ProcIEEE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jproc.2018.2871057
