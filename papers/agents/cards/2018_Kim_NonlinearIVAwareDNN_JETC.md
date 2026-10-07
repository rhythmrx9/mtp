---
id: W2605257365
key: 2018_Kim_NonlinearIVAwareDNN_JETC
title: "Deep Neural Network Optimized to Resistive Memory with Nonlinear Current-Voltage Characteristics"
short: "Nonlinear-IV NN"
year: 2018
venue: "JETC"
venue_full: "ACM Journal on Emerging Technologies in Computing Systems (JETC), 2018"
authors: "Hyungjun Kim, Taesu Kim, Jin-Seok Kim, Jae‐Joon Kim"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "weight-mapping", "analog-mvm", "device-variation", "quantization"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 4
citations_overall: 38
priority_score: 5.54
doi: "https://doi.org/10.1145/3145478"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2018_Kim_NonlinearIVAwareDNN_JETC.pdf"
fulltext: "../fulltext/2018_Kim_NonlinearIVAwareDNN_JETC.txt"
---

# Nonlinear-IV NN

**Deep Neural Network Optimized to Resistive Memory with Nonlinear Current-Voltage Characteristics** — ACM Journal on Emerging Technologies in Computing Systems (JETC), 2018 (2018)

## TL;DR
Replaces the perceptron's weighted-sum transfer function with the RRAM's own sinh I-V model (sum of w_i*sinh(B x_i)) and trains the network directly, so that a deep MNIST MLP on a k=7.5 nonlinear RRAM keeps 96.91% accuracy where naive linear mapping collapses to 9.05%.

## Summary
Sneak-path suppression pushes designers to nonlinear-I-V RRAM cells, but nonlinearity breaks the linear multiplication assumed by crossbar VMM, and prior fixes limit read voltage (hurting DAC resolution) or tune weights before mapping. The authors define half-bias nonlinearity k = I(Vmax)/I(Vmax/2) (k=2 is linear; surveyed devices span k=2.5 to 70) and show with a sinh model I(V)=e^{d/d0} sinh(BV) that errors peak for mid-range (~0.5 V) inputs, so deeper networks and natural-image inputs (CIFAR-10) with more mid-range activations suffer more. Their remedy is a device-aware network: the transfer function becomes f = sum_i w_i sinh(B x_i) with w = conductance, pairs of columns encode positive and negative sub-weights, ReLU is clipped to the read-voltage maximum (1 V) so layer outputs feed the next layer directly, and gradients through sinh/cosh are derived for SGD (Eqs. 14-21). Trained weights are linearly mapped into the device conductance range (e^-14 to e^-8) and inference is simulated in MATLAB with the device model. The method is also shown with a more complex exponential I-V model of a second RRAM. Evaluated on MLPs (784-500-250-10, 784-2500-2000-1500-1000-500-10, 2352-4000-1000-4000-10) for MNIST and CIFAR-10.

## Contributions
- Analysis linking I-V nonlinearity degree k, network depth and activation distribution to inference accuracy loss
- Device-model-based perceptron (transfer function from the I-V curve) and gradient derivation for training it
- Demonstration across k values and on a second, more complex RRAM I-V model

## Key claims (stable IDs)
- **2018_Kim_NonlinearIVAwareDNN_JETC#C1** — Naively mapped deep MLPs lose almost all accuracy at k=7.5 — _support:_ Deep MNIST 9.05% (naive) vs 97.43% ideal — _loc:_ Table 1
- **2018_Kim_NonlinearIVAwareDNN_JETC#C2** — The proposed network is nearly insensitive to k — _support:_ accuracy flat across k in Fig. 8 while naive mapping drops — _loc:_ Fig. 8
- **2018_Kim_NonlinearIVAwareDNN_JETC#C3** — Mid-range activations (near 0.5 V) cause the largest errors — _support:_ input data B (mean 0.5) gives large output error — _loc:_ Sec. 3, Fig. 5

## Results
- Shallow MNIST (k=7.5): ideal 94.8%, naive 87.90%, proposed 96.74%
- Deep MNIST: ideal 97.43%, naive 9.05%, proposed 96.91%
- Shallow CIFAR-10 MLP: ideal 54.97%, naive 41.94%, proposed 52.09%
- Works with a second complex exponential I-V model (Fig. 9b)

## Key numbers
- accuracy: 96.91% deep-MNIST MLP at k=7.5 (naive 9.05%)

## Datasets / benchmarks
MNIST, CIFAR-10

## Limitations
- Only MLPs on MNIST and a weak CIFAR-10 MLP (~55%); no CNNs or transformers
- MATLAB simulation of idealised device model; no variation, noise, drift or ADC modelling
- Needs a differentiable closed-form I-V model of each device and per-device retraining
- Assumes the device I-V is known and stable across conductance states

## Remarks
An early, clean example of hardware-aware training that bakes the exact device physics into the forward model rather than adding noise. The idea (differentiable device model as layer) generalises to other analog nonidealities but has not scaled to modern architectures; for transformers the sinh transfer would need to cope with attention dynamic range. Evidence is small-scale simulation.

## Cites (in collection, 4)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015) — _background_: "Since this approach can be several orders of magnitude more efficient than CMOS ASIC approaches in terms of both speed and power [3-6], many studies proposed neural network accelerators based on emerging NVM crossbar array [9-12]."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "Since this approach can be several orders of magnitude more efficient than CMOS ASIC approaches in terms of both speed and power [3-6], many studies proposed neural network accelerators based on emerging NVM crossbar array [9-12]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "To address the issue, many dedicated accelerators for vector-matrix multiplications have been proposed [3-6]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Since this approach can be several orders of magnitude more efficient than CMOS ASIC approaches in terms of both speed and power [3-6], many studies proposed neural network accelerators based on emerging NVM crossbar array [9-12]."

## Cited by (in collection, 2)
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _background_: "This exponential nonlinearity makes the VMM operation inaccurate, which deteriorates the training performance [119]."
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2018_Kim_NonlinearIVAwareDNN_JETC.pdf](../../07_Hardware_Aware_Training_and_Robustness/2018_Kim_NonlinearIVAwareDNN_JETC.pdf)
- Full text: [../fulltext/2018_Kim_NonlinearIVAwareDNN_JETC.txt](../fulltext/2018_Kim_NonlinearIVAwareDNN_JETC.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3145478
