---
id: W4407065774
key: 2025_Yousuf_LayerEnsembleAveraging_NatCommun
title: "Layer ensemble averaging for fault tolerance in memristive neural networks"
short: "Layer Ensemble Averaging"
year: 2025
venue: "NatCommun"
venue_full: "Nature Communications"
authors: "Osama Yousuf, Brian D. Hoskins, K Ramu, Mitchell Fream, William A. Borders, Advait Madhavan, Matthew W. Daniels, Andrew Dienstfrey, Jabez J. McClelland, Martin Lueker-Boden, Gina C. Adam"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM", "Memristor(generic)"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["stuck-at-faults", "device-variation", "weight-mapping", "tiling-partitioning", "read-write-noise", "write-verify-programming", "analog-mvm", "chip-demo"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 19
priority_score: 4.41
doi: "https://doi.org/10.1038/s41467-025-56319-6"
pdf: "../../06_Nonidealities_and_Reliability/2025_Yousuf_LayerEnsembleAveraging_NatCommun.pdf"
fulltext: "../fulltext/2025_Yousuf_LayerEnsembleAveraging_NatCommun.txt"
---

# Layer Ensemble Averaging

**Layer ensemble averaging for fault tolerance in memristive neural networks** — Nature Communications (2025)

## TL;DR
Layer ensemble averaging maps the same pre-trained ternary network onto redundant crossbar blocks and averages (outlier-suppressed) currents per layer, raising MNIST accuracy under 20% stuck-at faults from 40% to 89.6% in simulation and a Yin-Yang continual-learning task on a 20,000-device ReRAM chip from 55% to 71%.

## Summary
Memristive crossbars suffer from stuck-at faults, variability and limited tunability, and many fault-tolerance schemes assume stuck devices lie within the operable conductance range and that devices have high-precision tuning. The authors observe that on their ReRAM chip stuck devices are far outside the operable range (stuck-high ~500 uS, stuck-low ~10 uS vs operable G_OFF=133 uS, G_ON=233 uS) and that tuning to those values damages devices. They propose layer ensemble averaging (LEA): a ternary weight matrix is encoded into G_pos and G_neg blocks, each mapped alpha times onto contiguous crossbar blocks selected by a summed-conductance-variation (SCV) metric (greedy or random search); at inference, for each output, the beta least-defective of alpha row currents are averaged and the rest discarded, so correction occurs in the analog domain at every layer without retraining. Evaluation is (i) a PyTorch simulation with 12-bit input/output quantization, uniform read noise of +/-10 uS and Gaussian write noise sigma=16.66 uS, comparing against MAO and Committee Machines on a 784x150x10 MNIST MLP at equal device count (2*alpha*m*n), and (ii) hardware experiments on a custom 'Daffodil' mixed-signal platform (20,000-device 1T1R ReRAM chip, FPGA, DAC/ADC PCB) running a 3-layer perceptron on the multi-task Yin-Yang dataset with alpha in [1,4] and beta in [1,alpha]. Results show LEA outperforms MAO and CM, and in hardware approaches the 72% software baseline at (alpha,beta)=(4,4).

## Contributions
- LEA: hardware-oriented, retraining-free, device-agnostic fault tolerance using layer-level redundant mapping and current averaging
- Fault model matched to measured chip behaviour (stuck states outside operable range) exposing why MAO-style compensation fails
- SCV-based greedy/random block mapping plus simple and reduced-mapping-error encoding algorithms
- Validation against MAO and CM in simulation and end-to-end on a 20,000-device ReRAM prototype

## Key claims (stable IDs)
- **2025_Yousuf_LayerEnsembleAveraging_NatCommun#C1** — LEA tolerates 20% stuck-at faults on MNIST with near-baseline accuracy — _support:_ 89.6 +/- 1.0% at alpha=6 vs ~40% without correction; within 5% of baseline — _loc:_ Abstract, Fig. 4
- **2025_Yousuf_LayerEnsembleAveraging_NatCommun#C2** — LEA improves hardware continual-learning accuracy to near software baseline — _support:_ 55% -> 71% (software baseline 72%) at (alpha,beta)=(4,4); alpha=beta=1 is below a linear solver (<63.8%) — _loc:_ Fig. 5b
- **2025_Yousuf_LayerEnsembleAveraging_NatCommun#C3** — Greedy mapping gives tighter and higher accuracy than random mapping — _support:_ median 71% vs 69% — _loc:_ Results, hardware demonstration
- **2025_Yousuf_LayerEnsembleAveraging_NatCommun#C4** — MAO can degrade with added redundancy when stuck conductances are out of operable range — _support:_ at 10% defects accuracy drops from alpha=1 to alpha=3 — _loc:_ Results, simulation validation

## Results
- MNIST 784x150x10 MLP, 20% stuck-at faults, alpha=6: 89.6+/-1.0% (LEA) vs lower for CM and MAO at equal 2*alpha*m*n devices (Fig. 4)
- Hardware Yin-Yang 3-layer MLP: 71% vs 72% software baseline (Fig. 5)
- Device characterization: 4 conductance states 133/167/200/233 uS (2-bit), ~96% tuning success on a kernel with 27 stuck devices (Fig. 3)
- Even at 50% stuck devices LEA beats MAO and CM in mapping error (Fig. 4)

## Key numbers
- array_size: 20,000-device ReRAM chip
- accuracy: 89.6% MNIST at 20% stuck faults (alpha=6); 71% Yin-Yang hardware
- bits_weight: ternary weights, 1-bit conductance levels (2-bit tunable devices)
- bits_adc: 12-bit quantized I/O in simulation

## Datasets / benchmarks
MNIST, Yin-Yang

## Limitations
- Only small MLPs (ternary weights, 1-bit conductance levels) evaluated; no CNN/transformer/LM
- Redundancy cost: alpha-fold devices and area; overhead analysis is qualitative
- Hardware demo small (Yin-Yang, 4x12 first layer) and slow platform with limited ADC/DAC precision
- Excludes comparison with retraining-based and ECC-based schemes by design

## Remarks
A credible device-experiment-backed fault-tolerance paper: fault model derived from measured chip statistics is its main strength. For analog LM deployment it is only indirectly relevant, since billion-parameter weight matrices make alpha-fold redundancy costly, but the per-layer analog averaging idea and defect-aware block mapping could complement noise-aware training. Complements training-based robustness work in the collection and Committee Machines, which it compares against.

## Cites (in collection, 7)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Diverse technologies including resistive randomaccess memory (ReRAM) and phase change memory are being considered as promising crossbar candidates to implement the multiply and accumulate operations representing the standard synaptic weights model used in most neural networks11–19."
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Compared to other schemes in literature45,48, we map weight matrices as contiguous blocks instead of varying rows or lines on the crossbar."
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _background_: "Since memristor crossbars are programmable and non-volatile9,10, they can be utilized to build dedicated hardware accelerators for deep neural networks."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _background_: "We do not offer comparisons with software-oriented schemes such as those based on error correcting codes and architectures40–43, because they are orthogonal solutions that can be paired with any device redundancy-based fault tolerance scheme."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _baseline/comparison_: "Contrary to existing related literature26,30 where neural network outputs are obtained by polling outputs of an ensemble of neural networks, not necessarily mapping the same solution, here ensemble outputs are polled at the level of each layer by mapping the same solution multiple times."
- [2020_Xue_22nm2MbReRAMCIM_ISSCC](2020_Xue_22nm2MbReRAMCIM_ISSCC.md) 22nm 2Mb ReRAM CIM Macro (2020) — _motivation_: "A purely experimental approach is unfeasible since commercial tape-outs have long timelines and signiﬁcant design and fabrication costs4,20,21."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Diverse technologies including resistive randomaccess memory (ReRAM) and phase change memory are being considered as promising crossbar candidates to implement the multiply and accumulate operations representing the standard synaptic weights model used in most neural networks11–19."

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2025_Yousuf_LayerEnsembleAveraging_NatCommun.pdf](../../06_Nonidealities_and_Reliability/2025_Yousuf_LayerEnsembleAveraging_NatCommun.pdf)
- Full text: [../fulltext/2025_Yousuf_LayerEnsembleAveraging_NatCommun.txt](../fulltext/2025_Yousuf_LayerEnsembleAveraging_NatCommun.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41467-025-56319-6
