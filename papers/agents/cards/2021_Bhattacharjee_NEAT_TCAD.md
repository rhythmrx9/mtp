---
id: W3198405160
key: 2021_Bhattacharjee_NEAT_TCAD
title: "NEAT: Nonlinearity Aware Training for Accurate, Energy-Efficient, and Robust Implementation of Neural Networks on 1T-1R Crossbars"
short: "NEAT"
year: 2021
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Abhiroop Bhattacharjee, Lakshya Bhatnagar, Youngeun Kim, Priyadarshini Panda"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM", "Memristor(generic)"]
models: ["CNN", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "weight-mapping", "device-variation", "energy-efficiency", "peripheral-circuits", "cnn-accelerator", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 5
citations_overall: 31
priority_score: 6.36
doi: "https://doi.org/10.1109/tcad.2021.3109857"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2021_Bhattacharjee_NEAT_TCAD.pdf"
fulltext: "../fulltext/2021_Bhattacharjee_NEAT_TCAD.txt"
---

# NEAT

**NEAT: Nonlinearity Aware Training for Accurate, Energy-Efficient, and Robust Implementation of Neural Networks on 1T-1R Crossbars** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2021)

## TL;DR
NEAT clips and iteratively retrains DNN weights so they stay in the linear conductance regime of a 1T-1R crossbar cell (set by transistor gate voltage Vg), giving ~20% energy gain with <1% accuracy loss for ResNet18 on CIFAR-10/100.

## Summary
1T-1R crossbars add an access transistor to suppress sneak paths, but the transistor makes the effective cell conductance G_eff = 1/(R_M+R_t) depend on the input voltage (data-dependent non-linearity), which degrades DNN accuracy; the effect worsens at low gate voltage Vg and high conductance. The authors characterise G_eff(G_M, Vin, Vg) with SPICE (PTM 45nm transistor, R_ON=30kOhm, R_OFF=300kOhm, Vsupply up to 0.5 V) and define a tolerance metric (2.5%) that yields a conductance cut-off G_M,cutoff per Vg. DNN weights are linearly mapped to conductance and clipped to [-Wcut, Wcut], then the network is retrained for N=30 clip-and-retrain iterations (Adam, lr 1e-5) so most weights lie in the linear regime. Two Vg policies are proposed: homogeneous (same Vg for all layers) and heterogeneous (per-layer Vg chosen from the layer's weight range via Algorithm 1, no data needed). Evaluation is PyTorch simulation of VGG11 and ResNet18 on CIFAR-10/100 with energy estimated following prior work (RESPARC). The device-agnostic approach assumes the NVM can be programmed to any target conductance and treats interconnect parasitics and device variation as orthogonal. This text is the arXiv v1 preprint (Dec 2020), not the published TCAD version, so later additions (adversarial robustness, parasitics) are not verified here.

## Contributions
- SPICE analysis of 1T-1R power and transistor-induced non-linearity as function of Vg, Vin and G_M, with a tolerance-metric-based conductance cut-off
- Non-linearity Aware Training: weight clipping to Wcut plus iterative retraining (Algorithm 2)
- Homogeneous and heterogeneous (layer-wise) gate-voltage control as an energy/accuracy knob (Algorithm 1)
- ~20% energy gain with ~1% accuracy loss on ResNet18 (CIFAR-10/100)

## Key claims (stable IDs)
- **2021_Bhattacharjee_NEAT_TCAD#C1** — Lower Vg reduces 1T-1R synapse power but narrows the linear conductance range — _support:_ G_M,cutoff ~1.25e-5 S at Vg=0.8 V and ~3.34e-5 S at Vg=1.0 V (tm<2.5%); no cutoff at Vg=1.3 V — _loc:_ Sec. II-D, Figs. 2-5
- **2021_Bhattacharjee_NEAT_TCAD#C2** — Iterative training recovers accuracy at low Vg — _support:_ >50% accuracy improvement for ResNet18 at Vg=0.75 V; ~96% of first-conv weights in linear regime after 30 iterations — _loc:_ Sec. IV-A, Figs. 8-9
- **2021_Bhattacharjee_NEAT_TCAD#C3** — Heterogeneous Vg at the searched optimum loses <0.3% accuracy even without retraining — _support:_ e.g. VGG11 CIFAR-10 88.05% (no retrain) vs 88.74% (retrain) — _loc:_ Sec. IV-B, Table I
- **2021_Bhattacharjee_NEAT_TCAD#C4** — Homogeneous Vg reduction gives ~23% energy gain on ResNet18/CIFAR-10 at ~1.5% accuracy loss — _support:_ Vg=0.8 V vs Vg=1.0 V baseline — _loc:_ Sec. IV-C, Fig. 11

## Results
- Homogeneous: ~23% energy gain at Vg=0.8 V for ResNet18/CIFAR-10 with ~1.5% accuracy drop vs Vg=1.0 V baseline (Fig. 11)
- Heterogeneous: >10% energy gain across all model/dataset pairs (Fig. 11)
- Optimal Vg-0.05 config without retraining collapses (ResNet18 CIFAR-10 55.67%, CIFAR-100 27.62%); iterative training lifts these by only 2-5 points (59.23%, 29.22%) (Table I)
- VGG11 CIFAR-100 at optimal Vg: 68.42% -> 68.88% with retraining; ResNet18 CIFAR-100: 72.99% -> 73.60% (Table I)
- Input layers need high Vg, intermediate layers tolerate low Vg (Fig. 10)

## Key numbers
- tech_node: 45nm (PTM transistor model)
- array_size: 8x8 (Monte Carlo power analysis)
- energy_eff: ~20-23% energy gain vs Vg=1.0 V baseline
- accuracy: 90.58% CIFAR-10 / 73.60% CIFAR-100 (ResNet18, optimal Vg, retrained)

## Datasets / benchmarks
CIFAR-10, CIFAR-100

## Limitations
- Simulation only (SPICE + PyTorch); no measured silicon
- Non-linearity characterised at the single-cell level; array-level leakage/sensing limits only discussed qualitatively
- Device-agnostic: assumes ideal programming of conductance; variations and IR-drop not evaluated here
- Only small CNNs (VGG11, ResNet18) on CIFAR; no transformers or language models
- Energy model follows prior work and is not a full system estimate; iterative training has low gain when Vg is aggressively reduced

## Remarks
A clean, device-physics-grounded example of treating a specific data-dependent non-ideality (access-transistor non-linearity) with weight-range regularisation plus a circuit knob (Vg). Evidence is simulation on small CNNs, and this is the preprint rather than the TCAD version. For analog mapping of LMs the lesson is that conductance-range clipping is a cheap lever, but activation-dependent non-linearity matters more for transformers with wide activation ranges, which is untested. It is complementary to GENIEx-style emulation work and to variation-aware training in the collection.

## Cites (in collection, 5)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "Most of the previous works [3, 7–10] have proposed strategies and frameworks to model and mitigate data-independent non-idealities (primarily resistive non-idealities and NVM device variations) pertaining to 1R crossbar arrays to improve on the accuracy of the mapped DNNs."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _background_: "Select-lines (SL) are used to turn on transistors for selected rows. for performing the Matrix-Vector-Multiplication (MVM) operations of DNNs in the analog domain [2, 3]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _contrasts/critiques_: "Recent work GenieX [6] provides a neural network based framework to model both data-dependent and data-independent nonidealities for a crossbar array of 1T-1R synapses."
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020)

## Cited by (in collection, 3)
- [2022_Lin_DNAT_JETCAS](2022_Lin_DNAT_JETCAS.md) D-NAT (2022) — _baseline/comparison_: "In [20], an iterative training algorithm was proposed to regularize model parameters to fit into a linear operating range of 1T1R cells in a layer-by-layer manner to compensate for the accuracy degradation."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _uses-method-or-tool_: "Fig. 1 indicates the various resistive non-idealities, viz. 𝑅𝑑𝑟𝑖𝑣𝑒𝑟 , 𝑅𝑤𝑖𝑟𝑒_𝑟𝑜𝑤, 𝑅𝑤𝑖𝑟𝑒_𝑐𝑜𝑙 and 𝑅𝑠𝑒𝑛𝑠𝑒, prevalant in crossbars [3, 10]."
- [2024_Bhattacharjee_ClipFormer_TCAD](2024_Bhattacharjee_ClipFormer_TCAD.md) ClipFormer (2024) — _uses-method-or-tool_: "In step- 2 , we partition these matrices into multiple NVM crossbars of size 64×64 [13, 22]."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2021_Bhattacharjee_NEAT_TCAD.pdf](../../07_Hardware_Aware_Training_and_Robustness/2021_Bhattacharjee_NEAT_TCAD.pdf)
- Full text: [../fulltext/2021_Bhattacharjee_NEAT_TCAD.txt](../fulltext/2021_Bhattacharjee_NEAT_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2021.3109857
