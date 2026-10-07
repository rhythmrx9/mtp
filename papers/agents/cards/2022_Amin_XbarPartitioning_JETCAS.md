---
id: W4312141825
key: 2022_Amin_XbarPartitioning_JETCAS
title: "Xbar-Partitioning: A Practical Way for Parasitics and Noise Tolerance in Analog IMC Circuits"
short: "Xbar-Partitioning"
year: 2022
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2022)"
authors: "Md Hasibul Amin, Mohammed Elbtity, Ramtin Zand"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["Memristor(generic)", "PCM", "ReRAM", "MRAM"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["tiling-partitioning", "ir-drop-parasitics", "read-write-noise", "crossbar-architecture"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 8
citations_overall: 16
priority_score: 4.76
doi: "https://doi.org/10.1109/jetcas.2022.3222966"
pdf: null
fulltext: null
---

# Xbar-Partitioning

**Xbar-Partitioning: A Practical Way for Parasitics and Noise Tolerance in Analog IMC Circuits** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Proposes horizontal/vertical partitioning of fully-analog in-memory-computing crossbars to limit interconnect-parasitic and noise degradation, finding PCM with 1T-1R cells and fine partitioning gives the best accuracy/noise tradeoff.

## Summary
Fully-analog IMC circuits perform both matrix-vector multiplication and nonlinear vector operations in the analog domain to avoid energy-hungry ADC/DAC signal converters, but this makes them far more sensitive to interconnect parasitics and noise than conventional mixed-signal IMC. The paper proposes 'Xbar-partitioning', which splits large crossbar arrays into smaller horizontal and vertical partitions with dedicated routing/accumulation circuitry (demultiplexers and switches) so that partial products from sub-arrays are recombined, shortening interconnects and reducing parasitic resistance/capacitance per partition. Using SPICE simulation of a 400x120x84x10 DNN (apparently an MNIST-scale MLP) mapped onto crossbars built from several 2-terminal and 3-terminal resistive device technologies, six bitcell layouts, and four partitioning schemes, they report that PCM devices with a 1T-1R bitcell and a specific per-layer partition configuration (13/4/3 horizontal and 4/3/1 vertical partitions for the three layers) achieve the best accuracy (98.08%). They further provide an SNR-based analysis showing that smaller bitcells, finer partitioning, and devices with higher Roff/Ron ratio improve noise tolerance.

## Contributions
- Xbar-partitioning: a circuit-level method (horizontal + vertical) to split large fully-analog IMC crossbars into smaller sub-arrays with DEMUX/switch routing to recombine partial MAC products
- SPICE-level evaluation across five device technologies (2- and 3-terminal) and six bitcell layouts on a small DNN workload
- Identification of a best configuration (PCM, 1T-1R, fine-grained per-layer partitioning) reaching 98.08% accuracy
- SNR-based noise-tolerance analysis linking partition count, bitcell size, and Roff/Ron ratio to robustness

## Key claims (stable IDs)
- **2022_Amin_XbarPartitioning_JETCAS#C1** — Fine-grained partitioning recovers accuracy lost to interconnect parasitics in fully-analog IMC crossbars — _support:_ best configuration (PCM, 1T-1R, 13/4/3 horizontal and 4/3/1 vertical partitions) reaches 98.08% accuracy — _loc:_ Abstract
- **2022_Amin_XbarPartitioning_JETCAS#C2** — Noise tolerance improves with smaller bitcells, more partitions, and higher Roff/Ron device ratio — _support:_ SNR analysis across partitioning schemes and device technologies — _loc:_ Abstract / SNR analysis section

## Results
- Best configuration (PCM devices, 1T-1R bitcell, 13/4/3 horizontal and 4/3/1 vertical partitions across the three layers of a 400x120x84x10 DNN) achieves 98.08% accuracy

## Limitations
- Abstract-only analysis: full text not available, so method details (routing overhead, area/energy cost of partitioning circuitry, exact SNR numbers) could not be verified from the paper itself
- Evaluated on a single small MLP-scale model (400x120x84x10), not larger CNNs or modern DNNs
- Partitioning necessarily adds peripheral circuitry (DEMUX, switches) whose area/energy overhead is not quantified in the abstract

## Remarks
This is a companion/extension of the authors' own fully-analog IMAC line of work (IMAC co-processor, interconnect-parasitics ISCAS paper); a related 2-page preprint by the same authors (arXiv:2211.00590, 'Reliability-Aware Deployment of DNNs on In-Memory Analog Computing Architectures') covers the same partitioning idea with different device numbers, so it was not used here as a stand-in for this paper to avoid misattributing figures. The core idea — trade partitioning granularity against routing/accumulation overhead to balance parasitic/noise tolerance versus area/power — is a useful practical knob for mapping models onto fully-analog crossbars, but the evidence is simulation-only on a toy-scale model.

## Cites (in collection, 8)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Amin_ParasiticsPartitioning_ISCAS](2022_Amin_ParasiticsPartitioning_ISCAS.md) Parasitics-Partitioning (2022)

## Cited by (in collection, 1)
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2022_Amin_XbarPartitioning_JETCAS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/jetcas.2022.3222966
