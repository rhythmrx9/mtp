---
id: W3201198776
key: 2021_Yang_CFMESMO_ICCAD
title: "Multi-Objective Optimization of ReRAM Crossbars for Robust DNN Inferencing under Stochastic Noise"
short: "CF-MESMO / ReSNA"
year: 2021
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021)"
authors: "Xiaoxuan Yang, Syrine Belakaria, Biresh Kumar Joardar, Huanrui Yang, Janardhan Rao Doppa, Partha Pratim Pande, Krishnendu Chakrabarty, Hai Helen Li"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "noise-injection", "read-write-noise", "nas-codesign", "adc-dac", "device-variation", "energy-efficiency", "tiling-partitioning"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 13
citations_overall: 50
priority_score: 6.79
doi: "https://doi.org/10.1109/iccad51958.2021.9643444"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2021_Yang_CFMESMO_ICCAD.pdf"
fulltext: "../fulltext/2021_Yang_CFMESMO_ICCAD.txt"
---

# CF-MESMO / ReSNA

**Multi-Objective Optimization of ReRAM Crossbars for Robust DNN Inferencing under Stochastic Noise** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021) (2021)

## TL;DR
ReSNA trains DNNs against thermal, shot, RTN and programming noise of ReRAM crossbars (+2.57% accuracy on ResNet20/CIFAR-10 on average) and CF-MESMO, a continuous-fidelity Bayesian multi-objective optimiser, finds ReRAM design Pareto fronts with 90.91% less computation cost than NSGA-II.

## Summary
The paper targets stochastic ReRAM noise (thermal, shot, random telegraph, programming), which prior defect-/variation-aware methods ignore and which becomes severe at high operating frequency, high temperature and high cell resolution (noise margin drops 64x going from 2 to 8 bits). Deployment is modelled as software training, deterministic mapping of quantised weights to ceil(Bit_quan/Res_cell) cells (Conv kernels duplicated across crossbars, FC not), stochastic noise injection on conductances, and crossbar computation with ADC (Fig. 1, Table I), simulated with PytorX. ReSNA starts from a pre-trained model, injects freshly sampled device noise each iteration while keeping a noise-free weight copy, applies lower noise to FC layers than Conv layers (since duplication averages out Conv noise), and optionally majority-votes over 3 copies of the last FC layer. CF-MESMO uses continuous-fidelity Gaussian processes where fidelity is the number of ReSNA training epochs, and picks the (design, fidelity) pair maximising information gain per unit cost about the Pareto front over accuracy, area, latency and energy (NeuroSim at 32 nm). The design space is ~1.485x10^7 configurations over cell resolution, crossbar size, frequency and temperature. Experiments cover ResNet20/32/44, VGG11/13 on CIFAR-10 and ResNet18 on CIFAR-100.

## Contributions
- Study showing stochastic noise (not only programming variation or defects) degrades ReRAM DNN inference, especially for high-resolution cells and large crossbars.
- ReSNA: stochastic-noise-aware training with layer-wise noise levels and optional majority voting on the classification layer.
- CF-MESMO: information-theoretic continuous-fidelity multi-objective Bayesian optimisation for the ReRAM design space.
- Pareto analysis of cell resolution, crossbar size, frequency and temperature versus accuracy, area, latency and energy.

## Key claims (stable IDs)
- **2021_Yang_CFMESMO_ICCAD#C1** — Training without noise leaves ResNet20 at 69.61% when stochastic noise is present (8-bit cells, 500 MHz, 350 K, 128x128). — _support:_ Conv_ideal + FC_ideal training row — _loc:_ Table II, Sec. V
- **2021_Yang_CFMESMO_ICCAD#C2** — ReSNA improves accuracy over the noise-unaware baseline. — _support:_ +1.62% average without voting, +2.57% with voting on ResNet20; +5.47% at 1000 MHz and 400 K; ResNet18/CIFAR-100: 70.80% vs 69.37% (500 MHz, 350 K) and 68.23% vs 64.45% (1000 MHz) — _loc:_ Sec. VII-B, Fig. 4
- **2021_Yang_CFMESMO_ICCAD#C3** — CF-MESMO reaches equal Pareto quality at far lower cost than NSGA-II and random search. — _support:_ 90.91% and 91.21% cost reduction vs NSGA-II and random search; 78.18% reduction vs single-fidelity MESMO — _loc:_ Sec. VII-C, Fig. 6
- **2021_Yang_CFMESMO_ICCAD#C4** — FC layers are more sensitive to stochastic noise than Conv layers because kernel duplication averages noise. — _support:_ noise accumulation n^2*delta_c for FC vs n^2*delta_c/k for Conv with k copies — _loc:_ Sec. V

## Results
- Naive Gaussian (RGN) and programming-noise-only (PROG) training do not recover accuracy under the real stochastic noise model (Fig. 3, ResNet20/VGG13).
- Raising cell resolution from 2 to 8 bits cuts crossbar count by 75% but shrinks noise margin 64x.
- For ResNet20 CF-MESMO finds 11 Pareto designs in 100 iterations; low temperature (300-350 K) and 32x32/64x64 crossbars recommended (Fig. 7).
- Brute-force evaluation of 100 configurations would take ~30 GPU days; one ReSNA run is over 7 hours for 100 epochs of ResNet20.

## Key numbers
- tech_node: 32nm (NeuroSim)
- array_size: 32x32 to 128x128 crossbars
- accuracy: +2.57% avg ResNet20/CIFAR-10 (8-bit cells); 69.61% noise-unaware ResNet20 at 500 MHz/350 K
- bits_weight: 8b quantised, 2-8b cells

## Datasets / benchmarks
CIFAR-10, CIFAR-100

## Limitations
- Simulation only (PytorX plus NeuroSim at 32 nm); noise models from literature, no measured chip.
- Small image-classification CNNs (ResNet20/32/44, VGG11/13, ResNet18); no transformers or language models.
- Fidelity assumption that low-epoch accuracy is a lower bound of high-epoch accuracy is not guaranteed in general.
- Absolute accuracies stay below noise-free numbers (e.g. ~70% on ResNet18/CIFAR-100 versus 74.57% unquantised).

## Remarks
A software/algorithmic co-design paper rather than a device paper: the useful reusable pieces are the separation of stochastic noise from deterministic defects, the FC-versus-Conv sensitivity argument from kernel duplication, and the multi-fidelity design-space search. The evidence is purely simulated on small CNNs, so its relevance to mapping transformers or LMs is indirect (the noise-aware training recipe could transfer, but FC-heavy LMs would be in the sensitive regime the authors identify). Builds directly on PytorX/NIA in this collection.

## Cites (in collection, 13)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "The first category includes device defects (e.g., stuck-at-high or stuckat-low resistance [12]) and device reliability issues (e.g., retention failure [13] and resistance drift [14]) that are mostly deterministic in nature and have been addressed in prior work [15–20]."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _uses-method-or-tool_: "Therefore, multiple inputs can be processed simultaneously, increasing parallelism and improving throughput [5]."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "The first category includes device defects (e.g., stuck-at-high or stuckat-low resistance [12]) and device reliability issues (e.g., retention failure [13] and resistance drift [14]) that are mostly deterministic in nature and have been addressed in prior work [15–20]."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _uses-method-or-tool_: "We convert the change in current to the equivalent conductance change and model these two noise sources using Gaussian distributions [22]"
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _contrasts/critiques_: "He et al. [27] investigated the integration of stochastic noise during the training process, but their method failed to reach the desired DNN inferencing accuracy."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "Long et al. [25] injected Gaussian noise during training to mimic programming noise, and Joshi et al. [26] incorporated device programming variation extracted from experiments during training."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _uses-method-or-tool_: "The ReRAM crossbar and peripheral configurations are adopted from [52]."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "We use NeruoSim [51] along with the 32 nm technology node parameters to evaluate the hardware area, execution time, and energy consumption."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "The first category includes device defects (e.g., stuck-at-high or stuckat-low resistance [12]) and device reliability issues (e.g., retention failure [13] and resistance drift [14]) that are mostly deterministic in nature and have been addressed in prior work [15–20]."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."

## Cited by (in collection, 4)
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _motivation_: "However, RRAM device suffers from several non-idealities such as limited resistance levels, device-to-device write variations, stuck-at-faults, and limited Roff /Ron ratio, posing a signiﬁcant challenge to designing reliable RRAM-based IMC architectures [5–12]."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _uses-method-or-tool_: "For this purpose, we follow existing work and utilize a noise injection approach to improve the robustness of the finetuned model to ReRAM non-idealities [54] [55]."
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _contrasts/critiques_: "In contrast, CIM-based design space exploration focuses on identifying the optimal CIM hardware parameters for deploying a fixed neural network model [18, 19, 23]."
- [2025_Li_CIMLLMDataflow_ISVLSI](2025_Li_CIMLLMDataflow_ISVLSI.md) CIM-LLM Dataflow (2025)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2021_Yang_CFMESMO_ICCAD.pdf](../../07_Hardware_Aware_Training_and_Robustness/2021_Yang_CFMESMO_ICCAD.pdf)
- Full text: [../fulltext/2021_Yang_CFMESMO_ICCAD.txt](../fulltext/2021_Yang_CFMESMO_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccad51958.2021.9643444
