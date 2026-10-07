---
id: W3020429010
key: 2020_Song_ITTRNA_TCAD
title: "ITT-RNA: Imperfection Tolerable Training for RRAM-Crossbar-Based Deep Neural-Network Accelerator"
short: "ITT-RNA"
year: 2020
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2020"
authors: "Zhuoran Song, Yanan Sun, Lerong Chen, Tianjian Li, Naifeng Jing, Xiaoyao Liang, Li Jiang"
category: "07 Hardware-aware Training & Noise Robustness"
devices: ["ReRAM"]
models: ["MLP", "CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["hardware-aware-training", "device-variation", "weight-mapping", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 4
cites_in_collection: 5
citations_overall: 32
priority_score: 6.16
doi: "https://doi.org/10.1109/tcad.2020.2989373"
pdf: null
fulltext: null
---

# ITT-RNA

**ITT-RNA: Imperfection Tolerable Training for RRAM-Crossbar-Based Deep Neural-Network Accelerator** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (TCAD), 2020 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ITT-RNA combines an accelerator-friendly off-device training method (exploiting NN self-healing to avoid mapping large weights onto imperfect memristors) with a software-hardware co-design on-device fine-tuning step to keep CNN/MLP accuracy loss under 1.1% despite RRAM-crossbar defects and up to 20% stuck-at-fault rates.

## Summary
The paper targets accuracy loss in RRAM-crossbar DNN accelerators caused by fabrication imperfections -- device defects and process variations, including stuck-at-faults (SAFs) -- which both reduce manufacturing yield and degrade inference accuracy. The authors first propose an 'accelerator-friendly' off-device (pure software) training method that leverages the neural network's inherent self-healing capability to steer large-magnitude weights away from imperfect memristor cells, with a dynamic adjustment mechanism to handle error accumulation/magnification across layers in deeper MLPs. Since this software-only approach is insufficient for CNNs, they add a software-hardware co-design step that permits a small number of on-device retraining iterations directly on the RRAM crossbar to recover accuracy while limiting the number of (endurance-damaging) write operations, as an alternative to fully hardware-based on-device training. Based on the abstract, the reported results show the combined method keeps accuracy loss under 1.1% for resistance variations on both MLPs and CNNs, and under 1% even at a 20% stuck-at-fault rate.

## Contributions
- An accelerator-friendly, off-device (pure software) training method that uses the neural network's self-healing property to avoid mapping large-magnitude weights onto defective/imperfect memristor cells
- A dynamic adjustment mechanism extending this training approach to deeper MLPs where imperfect-memristor-induced errors accumulate and magnify across layers
- A software-hardware co-design methodology enabling CNNs to preserve accuracy with only a few on-device training (retraining) iterations on the RRAM crossbar, reducing the write-endurance cost versus fully hardware-based on-device training

## Key claims (stable IDs)
- **2020_Song_ITTRNA_TCAD#C1** — The proposed off-device, self-healing-based training method mitigates accuracy loss from RRAM resistance variation and defects for MLPs and CNNs — _support:_ Reported accuracy loss <=1.1% for resistance variations in both MLP and CNN (abstract) — _loc:_ Abstract
- **2020_Song_ITTRNA_TCAD#C2** — The software-hardware co-design method remains robust even at high stuck-at-fault rates — _support:_ Reported accuracy loss <=1% even at SAF rate = 20% (abstract) — _loc:_ Abstract
- **2020_Song_ITTRNA_TCAD#C3** — A pure off-device/software training solution is insufficient for CNNs, motivating the need for limited on-device retraining — _support:_ Stated directly: 'it is unable to provide enough accuracy for convolutional neural networks (CNNs)' (abstract) — _loc:_ Abstract

## Results
- <=1.1% accuracy loss under resistance variation for both MLP and CNN (per abstract)
- <=1% accuracy loss even with 20% stuck-at-fault rate (per abstract)

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Xplore is not downloadable here), so method details (datasets, network sizes, exact SAF/variation models, number of on-device iterations) could not be verified beyond what the abstract states
- The on-device co-design step still requires some RRAM write operations for retraining, which the paper itself identifies as an endurance concern it only partially mitigates

## Remarks
Based on the abstract, this is a hardware-aware training / fault-tolerance contribution combining offline self-healing-guided weight placement with limited on-device fine-tuning, addressing both device variation and stuck-at-faults -- a combination that is more complete than the typical variation-only (VAT) or SAF-only compensation. Because the full text could not be obtained from this environment, the specific network sizes, variation models, and the quantitative comparison against prior work could not be independently verified; this assessment should be read as abstract-derived and treated with appropriate caution for a thesis-level literature review.

## Cites (in collection, 5)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 4)
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021) — _contrasts/critiques_: "The previous work [18] proposed a software and hardware co-design method to get higher accuracy in CNN, even under large device variations. The off-device training was employed to get a relatively high accuracy while the on-device training was used to further suppress the accuracy loss."
- [2023_Diware_MappingAwareBiasedTraining_AICAS](2023_Diware_MappingAwareBiasedTraining_AICAS.md) Mapping-aware Biased Training (2023) — _contrasts/critiques_: "Moreover, some works [17], [18] prevent large weights from mapping to high variation memristors. This requires extensive chip characterization and does not address errors due to the accumulation of variations in small weights."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021)
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)

## Files
- PDF: not available locally (save as `papers/07_Hardware_Aware_Training_and_Robustness/2020_Song_ITTRNA_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2020.2989373
