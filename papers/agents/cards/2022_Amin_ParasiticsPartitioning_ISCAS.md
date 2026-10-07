---
id: W4313170690
key: 2022_Amin_ParasiticsPartitioning_ISCAS
title: "Interconnect Parasitics and Partitioning in Fully-Analog In-Memory Computing Architectures"
short: "Parasitics-Partitioning"
year: 2022
venue: "ISCAS"
venue_full: "IEEE International Symposium on Circuits and Systems (ISCAS 2022)"
authors: "Md Hasibul Amin, Mohammed Elbtity, Ramtin Zand"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["MRAM", "Memristor(generic)"]
models: ["MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["ir-drop-parasitics", "tiling-partitioning", "analog-mvm", "weight-mapping", "nonlinear-functions", "crossbar-architecture", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 2
citations_overall: 13
priority_score: 4.7
doi: "https://doi.org/10.1109/iscas48785.2022.9937884"
pdf: "../../06_Nonidealities_and_Reliability/2022_Amin_ParasiticsPartitioning_ISCAS.pdf"
fulltext: "../fulltext/2022_Amin_ParasiticsPartitioning_ISCAS.txt"
---

# Parasitics-Partitioning

**Interconnect Parasitics and Partitioning in Fully-Analog In-Memory Computing Architectures** — IEEE International Symposium on Circuits and Systems (ISCAS 2022) (2022)

## TL;DR
SPICE study showing interconnect RC parasitics collapse MNIST accuracy of a 400x120x84x10 MLP to about 15% on fully-analog IMC (MVM plus sigmoid in-array), and an analog horizontal/vertical partitioning scheme recovers 94.84% (vs ~97% digital CPU) at higher power.

## Summary
Fully-analog IMC architectures (IMAC) compute both MVM and nonlinear activations in the array with differential amplifiers and memristive/SOT-MRAM sigmoid neurons, removing ADCs/DACs, but analog signals traverse the whole network and are sensitive to wire parasitics. The authors model wire resistance (size-dependent resistivity using Fuchs-Sondheimer and Mayadas-Shatzkes models) and capacitance (Sakurai-Tamaru) from a 14nm PTM FinFET layout (lambda 9nm) of an SOT-MRAM synapse bitcell. A layer is split into subarrays by horizontal partitioning (HP: inputs divided, partial currents accumulated across subarrays in the analog domain via switch blocks/DEMUX) and vertical partitioning (VP: output columns divided), shortening interconnects. A 400x120x84x10 MLP for 20x20 MNIST is simulated in SPICE with 32x32 subarrays across partition counts and with a deliberately non-ideal larger bitcell layout.

## Contributions
- Interconnect parasitic model for fully-analog IMC subarrays
- Analog horizontal and vertical partitioning that keeps computation in the analog domain
- Accuracy/power trade-off analysis over partition counts and bitcell layout

## Key claims (stable IDs)
- **2022_Amin_ParasiticsPartitioning_ISCAS#C1** — Without parasitic mitigation the MLP reaches only about 15% MNIST accuracy — _support:_ SPICE simulation, unpartitioned — _loc:_ Table I, Conclusion
- **2022_Amin_ParasiticsPartitioning_ISCAS#C2** — HP=[16,8,8], VP=[8,8,1] gives 94.84% accuracy, close to ~97% digital CPU — _support:_ 32x32 subarrays — _loc:_ Table I, Fig. 5
- **2022_Amin_ParasiticsPartitioning_ISCAS#C3** — Partitioning compensates for a poor bitcell layout — _support:_ ~55% accuracy drop at HP=[7,2,2]/VP=[2,2,1] reduced to <1% drop at HP=[16,8,8]/VP=[8,8,1] — _loc:_ Table II

## Results
- Higher partition counts raise accuracy because interconnect length and parasitic resistance fall
- Cost: extra circuitry and higher power consumption, and sparser subarray utilization (Fig. 5)

## Key numbers
- tech_node: 14nm PTM FinFET
- array_size: 32x32 subarrays
- accuracy: 94.84% MNIST (vs ~97% CPU; ~15% unpartitioned)
- bits_adc: none (fully analog)

## Datasets / benchmarks
MNIST

## Limitations
- Tiny MLP on MNIST only, simulation only
- Single device family (SOT-MRAM synapses) and fixed 14nm PTM
- No device variation or noise considered
- Utilization and power overhead grows with partitioning

## Remarks
Short ISCAS paper making a narrow but concrete mapping point: tile/partition size is a first-order accuracy knob under parasitics, trading utilization and power for accuracy. Scaling to deeper or transformer-scale models is unverified.

## Cites (in collection, 2)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "With the increased computational demands of machine learning (ML) workloads, in-memory computing (IMC) [1] architectures have attracted considerable attention to address the processor-memory bottleneck in conventional von Neumann architectures."
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _motivation_: "One of the major factors limiting their wide use in practical ML applications is the large and energy-hungry signal conversion units required to change the computation domain from analog-to-digital (and vice versa) to compute the nonlinear vector operations, e.g. activation functions in DNNs [9]."

## Cited by (in collection, 1)
- [2022_Amin_XbarPartitioning_JETCAS](2022_Amin_XbarPartitioning_JETCAS.md) Xbar-Partitioning (2022)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2022_Amin_ParasiticsPartitioning_ISCAS.pdf](../../06_Nonidealities_and_Reliability/2022_Amin_ParasiticsPartitioning_ISCAS.pdf)
- Full text: [../fulltext/2022_Amin_ParasiticsPartitioning_ISCAS.txt](../fulltext/2022_Amin_ParasiticsPartitioning_ISCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iscas48785.2022.9937884
