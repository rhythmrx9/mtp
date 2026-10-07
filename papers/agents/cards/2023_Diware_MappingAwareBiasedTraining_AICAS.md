---
id: W4383501742
key: 2023_Diware_MappingAwareBiasedTraining_AICAS
title: "Mapping-aware Biased Training for Accurate Memristor-based Neural Networks"
short: "Mapping-aware Biased Training"
year: 2023
venue: "AICAS"
venue_full: "2023 IEEE 5th International Conference on Artificial Intelligence Circuits and Systems (AICAS 2023)"
authors: "Sumit Diware, Anteneh Gebregiorgis, Rajiv Joshi, Said Hamdioui, Rajendra Bishnoi"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "device-variation", "weight-mapping", "bit-slicing", "quantization", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 10
citations_overall: 15
priority_score: 4.34
doi: "https://doi.org/10.1109/aicas57966.2023.10168661"
pdf: "../../07_Hardware_Aware_Training_and_Robustness/2023_Diware_MappingAwareBiasedTraining_AICAS.pdf"
fulltext: "../fulltext/2023_Diware_MappingAwareBiasedTraining_AICAS.txt"
---

# Mapping-aware Biased Training

**Mapping-aware Biased Training for Accurate Memristor-based Neural Networks** — 2023 IEEE 5th International Conference on Artificial Intelligence Circuits and Systems (AICAS 2023) (2023)

## TL;DR
Constrains the weights of the most hardware-important crossbar columns during training so their bit-slices land only in low-error RRAM conductance states, raising simulated hardware accuracy up to 2.4x (FMNIST/LeNet-5: 35.4% to 85.2%) with zero hardware overhead.

## Summary
Memristor conductance variation corrupts stored weights. The authors observe that the error current per device depends on the absolute conductance, so for a 2-bit memristor the state preference order is G00 (best), G01, G11, G10 (worst) based on Ierror, not variation percentage. They choose Config-3 (favorable = G00, G01, G11; unfavorable = G10) because it still allows positive and negative non-zero weights. Weights are 8-bit fixed point (6-bit fraction) in 2's complement shifted by 2^7, split into four 2-bit slices over four memristors as in ISAAC/PUMA; a favorability constraint on the weight values forces chosen slices (e.g. the MSB slice) onto favorable states. Importance of a crossbar column HIc is the sum over crossbar-sized chunks of gradient-based weight importance SIw = dQ/dw; the top m% columns per layer (found by design-space exploration) are constrained each epoch, and the best post-constraint test accuracy checkpoint is mapped to hardware. Evaluation uses a Python behavioral simulator of the IMA unit with PUMA/ISAAC power/area numbers and device variation data from measured RRAM (Prakash and Hwang), on LeNet-5 for MNIST, FMNIST and EMNIST-letters.

## Contributions
- Favorability analysis of conductance states based on error current rather than variation percentage
- Column-level importance metric HIc for hardware accuracy, aggregating gradient-based weight importance over crossbar columns
- Mapping-aware biased training that applies a favorability constraint only to important columns
- Evaluation showing up to 2.4x hardware accuracy and 2.4x correct operations per energy at no hardware cost

## Key claims (stable IDs)
- **2023_Diware_MappingAwareBiasedTraining_AICAS#C1** — Biased training improves hardware accuracy up to 2.4x over conventional training — _support:_ FMNIST: 35.4% to 85.2% hardware accuracy — _loc:_ Sec. IV-B, Fig. 9, Table I
- **2023_Diware_MappingAwareBiasedTraining_AICAS#C2** — No hardware overhead: same energy and area as conventional mapping — _support:_ 3738 pJ and 21765 um2 per IMA unit for both — _loc:_ Table I
- **2023_Diware_MappingAwareBiasedTraining_AICAS#C3** — Correct operations per unit energy rise from 96.9 to 233.4 GOP/J (FMNIST) — _support:_ Table I — _loc:_ Table I
- **2023_Diware_MappingAwareBiasedTraining_AICAS#C4** — Constraining too many weights hurts software accuracy and thus hardware accuracy; an intermediate percentage of columns is optimal — _support:_ design-space exploration of important-column percentage per dataset — _loc:_ Sec. IV-B.1, Fig. 8

## Results
- FMNIST (LeNet-5): hardware accuracy 35.4% (conventional) vs 85.2% (proposed)
- Up to 2.4x hardware accuracy across MNIST, FMNIST, EMNIST-L; larger gains for more complex datasets
- Slightly lower software accuracy than conventional training due to constraint
- Energy 3738 pJ, area 21765 um2 per IMA unit unchanged; 96.9 vs 233.4 GOP/J on FMNIST

## Key numbers
- energy_eff: 233.4 GOP/J correct operations (FMNIST) vs 96.9 conventional
- accuracy: 85.2% vs 35.4% FMNIST hardware accuracy (LeNet-5)
- bits_weight: 8b weights in four 2-bit slices

## Datasets / benchmarks
MNIST, Fashion-MNIST, EMNIST-letters

## Limitations
- Simulation only with behavioral Python framework; 4-page paper
- Only LeNet-5 on MNIST-family datasets; no CNNs of realistic size or language models
- No comparison with standard noise-injection hardware-aware training baselines
- Single device dataset for variation (2-bit RRAM); assumes error current scales with absolute conductance and that state ordering is known
- 8-bit weights split in 2-bit slices; ADC/DAC noise and IR drop not considered

## Remarks
A sensible mapping-aware twist on hardware-aware training that exploits column-wise MAC structure and bit-slice state-dependence. The evidence is weak because tiny models are used and noise-injection training (Joshi et al.) could close much of the gap, so the baseline appears weak. Conceptually relevant to state-aware quantization and bit-slice mapping for large models, but untested for transformers or LMs.

## Cites (in collection, 10)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _contrasts/critiques_: "Moreover, some works [17], [18] prevent large weights from mapping to high variation memristors. This requires extensive chip characterization and does not address errors due to the accumulation of variations in small weights."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _contrasts/critiques_: "First, on-chip training inherently adapts the weights to conductance variation as the network is trained on the CIM chip [13], [14]. However, it is not scalable due to individual training necessity for each chip, high energy consumption, and endurance issues."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _uses-method-or-tool_: "It is based on in-situ multiply-accumulate (IMA) unit in state-of-the-art CIM architectures [29], [33]. Power and area for various IMA components are also obtained from [29]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "Alternatively, noise estimated from a non-extensive chip characterization can be injected in off-chip training [19]-[24] to enhance the network's tolerance towards errors due to conductance variation. However, this approach fails to address the issue of reducing such errors, as memristors can still get mapped to high variation conductance states, rendering it ineffective."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "It uses emerging non-volatile memory technologies such as memristors, also called resistive random access memories (RRAMs), which are highly scalable and compatible with CMOS technology [11]."
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020) — _contrasts/critiques_: "Second, off-chip training using a hardware-calibrated software model of conductance variation [15], [16] is also not scalable, as each chip requires individual characterization and training."
- [2020_Song_ITTRNA_TCAD](2020_Song_ITTRNA_TCAD.md) ITT-RNA (2020) — _contrasts/critiques_: "Moreover, some works [17], [18] prevent large weights from mapping to high variation memristors. This requires extensive chip characterization and does not address errors due to the accumulation of variations in small weights."
- [2021_Pedretti_ConductanceVariationsIMC_IRPS](2021_Pedretti_ConductanceVariationsIMC_IRPS.md) Conductance Variations IMC (2021) — _data/numbers_: "(b) Measurements in [31]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The full-precision weights and inputs are split into smaller slices as i) bit-capacity of memristors is insufficient for weights and ii) full-precision inputs need digital-to-analog converters (DACs) and analog-to-digital converters (ADCs) which consume huge energy and area [29]."
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023) — _contrasts/critiques_: "Alternatively, noise estimated from a non-extensive chip characterization can be injected in off-chip training [19]-[24] to enhance the network's tolerance towards errors due to conductance variation. However, this approach fails to address the issue of reducing such errors, as memristors can still get mapped to high variation conductance states, rendering it ineffective."

## Files
- PDF: [../../07_Hardware_Aware_Training_and_Robustness/2023_Diware_MappingAwareBiasedTraining_AICAS.pdf](../../07_Hardware_Aware_Training_and_Robustness/2023_Diware_MappingAwareBiasedTraining_AICAS.pdf)
- Full text: [../fulltext/2023_Diware_MappingAwareBiasedTraining_AICAS.txt](../fulltext/2023_Diware_MappingAwareBiasedTraining_AICAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/aicas57966.2023.10168661
