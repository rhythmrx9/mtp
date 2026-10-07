---
id: W3020710655
key: 2020_Ji_FPSAReducedArchitecture_TC
title: "A Reduced Architecture for ReRAM-Based Neural Network Accelerator and Its Software Stack"
short: "FPSA Reduced Architecture"
year: 2020
venue: "TC"
venue_full: "IEEE Transactions on Computers (TC), 2020"
authors: "Yu Ji, Zixin Liu, Youhui Zhang"
category: "05 Mapping, Compilation & Dataflow"
devices: ["ReRAM"]
models: ["CNN", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["crossbar-architecture", "compiler-software-stack", "cnn-accelerator", "dataflow-pipelining"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 3
citations_overall: 5
priority_score: 4.04
doi: "https://doi.org/10.1109/tc.2020.2988248"
pdf: null
fulltext: null
---

# FPSA Reduced Architecture

**A Reduced Architecture for ReRAM-Based Neural Network Accelerator and Its Software Stack** — IEEE Transactions on Computers (TC), 2020 (2020)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Inspired by RISC design, the Field Programmable Synapse Array (FPSA) keeps ReRAM-crossbar hardware compact (reconfigurable logic, wires and compute resources) and pushes complexity into a software stack that converts arbitrary/dynamic NNs into hardware-compatible equivalents and optimizes their scheduling/mapping, reporting up to 1000x speedup over PRIME.

## Summary
The paper addresses two limitations of prior ReRAM-based NN accelerators: performance bounded by peripheral circuits/interconnect, and accuracy/flexibility problems from device variation and the fixed in-situ computation mode. Rather than fixing these purely in hardware (which would add overhead), the authors apply a RISC-like design philosophy: keep the hardware, Field Programmable Synapse Array (FPSA), simple, dense and efficient (reconfigurable logic, wires and compute resources built from ReRAM crossbars), and move complexity into a software stack. The software converts various neural network types, including dynamic NNs, into equivalent networks that satisfy hardware constraints with negligible accuracy loss, and performs scheduling and mapping of the converted network onto the FPSA fabric. Per the abstract, evaluation against the PRIME ReRAM-based accelerator shows up to 1000x speedup.

## Contributions
- Field Programmable Synapse Array (FPSA): a reduced/compact ReRAM-crossbar-based reconfigurable hardware architecture providing dense logic, wiring, and compute resources, following a RISC-inspired hardware/software split
- A software stack that converts arbitrary and dynamic neural networks into equivalent networks meeting FPSA's hardware constraints with negligible accuracy loss
- Scheduling and mapping optimization of the converted network onto the FPSA hardware
- A full software/hardware system co-design intended to fully exploit ReRAM's potential while minimizing hardware complexity

## Key claims (stable IDs)
- **2020_Ji_FPSAReducedArchitecture_TC#C1** — The proposed FPSA software/hardware system substantially outperforms a state-of-the-art ReRAM-based NN accelerator (PRIME) — _support:_ Reported up to 1000x speedup versus PRIME (abstract) — _loc:_ Abstract
- **2020_Ji_FPSAReducedArchitecture_TC#C2** — The software conversion of networks (including dynamic NNs) to FPSA-compatible equivalents incurs negligible accuracy loss — _support:_ Stated directly in abstract: 'negligible accuracy loss' — _loc:_ Abstract
- **2020_Ji_FPSAReducedArchitecture_TC#C3** — Moving complexity to software (RISC-like design) allows the ReRAM hardware to be more compact and efficient than approaches that solve accuracy/flexibility issues purely in hardware — _support:_ Abstract argument: 'Solving these issues with hardware will further offset the performance' — _loc:_ Abstract

## Results
- Up to 1000x speedup compared to PRIME (per abstract)

## Limitations
- Only the abstract was available for this analysis (full text not accessible from this machine; IEEE Xplore is not downloadable here), so the specific benchmarks, network sizes, and conditions under which the 1000x speedup was measured could not be verified
- As an extension/journal version of conference-level FPSA work, some architectural or experimental details may be inherited from prior publications not captured here

## Remarks
Based on the abstract, this is a mapping/compilation and architecture co-design paper in the spirit of a RISC-like split between simple reconfigurable ReRAM hardware and a sophisticated software compiler/scheduler, directly targeting the flexibility limitations of fixed in-situ crossbar designs like PRIME and ISAAC. The claimed 1000x speedup over PRIME is a striking figure that, without full-text access, cannot be contextualized against workload selection or baseline configuration; this should be treated as a headline abstract claim pending verification against the full paper or its earlier (likely ISCA) conference version.

## Cites (in collection, 3)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/05_Mapping_Compilation_and_Dataflow/2020_Ji_FPSAReducedArchitecture_TC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tc.2020.2988248
