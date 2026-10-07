---
id: W2765081478
key: 2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron
title: "Mixed-precision in-memory computing"
short: "Mixed-Precision IMC"
year: 2018
venue: "NatElectron"
venue_full: "Nature Electronics, vol. 1, pp. 246-253 (2018)"
authors: "Manuel Le Gallo, Abu Sebastian, Roland Mathis, Matteo Manica, Heiner Giefers, Tomáš Tůma, Costas Bekas, Alessandro Curioni, Evangelos S. Eleftheriou"
category: "02 Fabricated Chips & Macros"
devices: ["PCM"]
models: ["Other"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["chip-demo", "analog-mvm", "mixed-precision", "write-verify-programming", "conductance-drift", "calibration-compensation", "adc-dac", "heterogeneous-analog-digital"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 10
cites_in_collection: 2
citations_overall: 481
priority_score: 8.5
doi: "https://doi.org/10.1038/s41928-018-0054-8"
pdf: "../../02_Fabricated_Chips_and_Macros/2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.pdf"
fulltext: "../fulltext/2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.txt"
---

# Mixed-Precision IMC

**Mixed-precision in-memory computing** — Nature Electronics, vol. 1, pp. 246-253 (2018) (2018)

## TL;DR
Mixed-precision in-memory computing: an imprecise PCM crossbar performs the bulk matrix-vector products inside a Krylov inner solver while a digital processor does high-precision iterative refinement, solving a 5,000-equation system with 998,752 PCM devices to near machine precision (~1.3e-15 error) with dynamic energy gains of 6.8x (up to 24x with lower noise) in measurement-based estimates.

## Summary
Analog memristive arrays suffer from variability and noise, limiting numerical precision for scientific computing and analytics. The paper combines a von Neumann processor with a computational memory unit: the processor computes the residual r = b - Ax in high precision and the PCM crossbar solves A z = r inexactly using an inner Conjugate Gradient or GMRES solver whose matrix-vector products are done in memory, with outer iterative refinement guaranteeing convergence. Experiments use a prototype chip of one million PCM devices (512 word lines x 2048 bit lines, 90nm CMOS, PCM in series with access transistor, 8-bit on-chip ADC, 1 us read, serial device access), programmed via iterative program-and-verify (margin 1.74 uS, max 20 iterations, 400 ns pulses). Matrix entries map to conductances of 0-50 uS and vector elements to read voltages 0.1-0.3 V; a polynomial 'pseudo-Ohm's law' models the PCM I-V; K devices are averaged per element (error scales as K^-0.5), and a periodic calibration compensates drift. Tasks: model covariance matrices (N=500 with K=4, N=5,000 using a banded matrix with 12 entries per side and K=8) and a 40x40 gene covariance inversion from TCGA RNA data to build cancer and normal tissue interactomes.

## Contributions
- Concept of mixed-precision in-memory computing (low-precision analog inner loop, high-precision digital outer refinement)
- Experimental demonstration solving a 5,000-equation dense system on 998,752 PCM devices
- Techniques: multi-device averaging, banded matrix approximation, drift calibration, iterative program-and-verify
- Energy comparison against POWER8 CPU and P100 GPU using measured runtime/power

## Key claims (stable IDs)
- **2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron#C1** — Mixed-precision IMC reaches accuracy limited only by the digital unit's machine precision, not the PCM precision (~1.3e-15 for N=500, tol=1e-15). — _support:_ experimental convergence curves — _loc:_ Fig. 3; Results
- **2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron#C2** — The N=500 system converges in 23 iterative refinements (K=4, CG inner solver, tol 1e-5); N=5,000 with banded matrix and K=8 also needs 23 high-precision MVMs versus 50 for a fully digital solver. — _support:_ text — _loc:_ Results, Fig. 3
- **2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron#C3** — Maximum measured dynamic energy gains are 6.8x versus CPU/GPU, up to 24x assuming two orders of magnitude less noise in the memory unit. — _support:_ memory-unit time and energy assumed negligible (upper bound) — _loc:_ Energy comparison paragraph
- **2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron#C4** — Computed 40-gene interactome from RNA data using in-memory solves is identical to the exact one. — _support:_ 40 systems solved with GMRES, m=5 — _loc:_ Fig. 4

## Results
- 998,752 PCM devices used for the 5,000x5,000 (banded) system
- Averaging K devices reduces MVM error as K^-0.5; analog multiplication works over ~2 decades of current
- Dynamic energy gains 6.8x (current PCM precision) to 24x (100x lower noise) vs CPU/GPU for the model matrix
- Speed target: 10 crossbars of 1000x1000 at <=1 us cycle for near-optimal performance (Supplementary Note VII.B)

## Key numbers
- tech_node: 90nm CMOS
- array_size: 512 x 2048 PCM crossbar (1M devices)
- energy_eff: 6.8x-24x dynamic energy gain vs CPU/GPU (estimate)
- accuracy: ~1.3e-15 error (N=500)
- bits_weight: analog conductance 0-50 uS, K devices averaged
- bits_adc: 8b

## Datasets / benchmarks
Synthetic covariance matrices, TCGA RNA data (autophagy genes)

## Limitations
- Problems are small, well-conditioned diagonally dominant covariance matrices
- Hardware allows only serial device access, so the MVM is emulated device by device with off-chip accumulation, not a true parallel crossbar MVM
- Energy results are optimistic upper bounds assuming the memory unit is free
- Requires storing the matrix in both PCM and digital memory
- No neural networks or language models

## Remarks
Key conceptual paper for IBM's PCM line: it frames analog arrays as approximate engines acceptable whenever an outer digital loop corrects errors, the same logic later used in mixed-precision training and hybrid analog-digital accelerators. Evidence is real PCM data but not a true parallel crossbar MVM, and the energy numbers are bounds. For DNN mapping, its practical lessons are drift calibration through global conductance scaling and multi-device averaging; later work such as the IBM IMC review and PCM inference (Joshi et al.) builds on it.

## Cites (in collection, 2)
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _background_: "Possible avenues are improving the memristive device characteristics with respect to variability and conductance noise33, mapping a single column of the matrix to multiple physical columns of an array encoding different bits, and using error-correction techniques within the computational memory unit41."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "Research on these devices has already led to the development of massively parallel, memory-centric hardware accelerators with applications ranging from image processing to healthcare19-22."

## Cited by (in collection, 10)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Both charge-based storage devices, such as Flash memory4, and resistance-based (memristive) storage devices, such as metal-oxide resistive random-access memory (ReRAM)5,6 and phase-change memory (PCM)7-9 are being investigated for this."
- [2020_Joksas_CommitteeMachines_NatCommun](2020_Joksas_CommitteeMachines_NatCommun.md) Committee Machines (2020) — _contrasts/critiques_: "To mitigate the effects of these device non-idealities, it is often necessary to modify device structure [9], to use more advanced programming schemes [14] or to use additional circuitry [15] or high-precision processing units [16] in conjunction with memristive elements."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _extends/builds-on_: "The adaptation of this concept for in-memory computing and experimental demonstration of solving a system of 5,000 linear equations using 998,752 PCM devices with arbitrarily high accuracy was presented in ref. 64."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _background_: "This approach has been demonstrated to solve linear equations [26] and in DNN inference and even training tasks [23], showing limited error in the computation and much higher efficiency compared to traditional approaches [2]."
- [2022_Klein_ALPINE_TC](2022_Klein_ALPINE_TC.md) ALPINE (2022) — _data/numbers_: "The scalar multiplication of an analog input with PCMbased weights is shown to be comparable to an implementation with 4-bit fixed-point inputs and weights [32], and even to an implementation with 8-bit fixed-point inputs and weights with suitable innovations in device design [33]."
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024) — _background_: "Mixed-precision training, which accumulates the weight update in software and only updates the memristor devices when the accumulated value surpasses the programming granularity, can greatly relax requirement for conductance update resolution and endurance and allow software-comparable accuracy to be achieved."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "Memristor-CIM (9–37) provides large memory capacity, high storage density, and high energy efficiency."
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _background_: "Analog In-Memory Computing (AIMC) has emerged as a promising computing paradigm to tackle these challenges, offering improved performance and energy-efficiency through computation directly within the memory array4,5."
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.pdf](../../02_Fabricated_Chips_and_Macros/2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.pdf)
- Full text: [../fulltext/2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.txt](../fulltext/2018_LeGallo_MixedPrecisionInMemoryComputing_NatElectron.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41928-018-0054-8
