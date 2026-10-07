---
id: W2996781237
key: 2019_Han_ERALSTM_TPDS
title: "ERA-LSTM: An Efficient ReRAM-Based Architecture for Long Short-Term Memory"
short: "ERA-LSTM"
year: 2019
venue: "TPDS"
venue_full: "IEEE Transactions on Parallel and Distributed Systems (2019)"
authors: "Jianhui Han, He Liu, Mingyu Wang, Zhaolin Li, Youhui Zhang"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["recurrent-models", "crossbar-architecture", "nonlinear-functions", "weight-mapping", "dataflow-pipelining"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 7
citations_overall: 36
priority_score: 5.53
doi: "https://doi.org/10.1109/tpds.2019.2962806"
pdf: null
fulltext: null
---

# ERA-LSTM

**ERA-LSTM: An Efficient ReRAM-Based Architecture for Long Short-Term Memory** — IEEE Transactions on Parallel and Distributed Systems (2019) (2019)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ERA-LSTM uses ReRAM-based analog approximate computing for LSTM's element-wise operations alongside crossbar dot products, plus a multi-tile mapping scheme and crossbar-friendly pruning, to cut ADC demand and outperform FPGA- and ReRAM-based LSTM accelerators by up to 103.6x and 6.1x respectively.

## Summary
The paper targets the ADC overhead of ReRAM processing-in-memory LSTM accelerators, which dominates power consumption in prior designs that compute LSTM's element-wise (gate) operations digitally. Based on a dataflow analysis of the LSTM computation, ERA-LSTM proposes performing the element-wise computations using ReRAM-based analog approximate computing instead of digital logic, combined with the standard crossbar dot-product computation, in a unified LSTM processing tile that significantly reduces the number of ADCs required. The paper also presents a mapping scheme to deploy large-scale LSTM models across multiple processing tiles, and an architecture enhancement supporting crossbar-friendly LSTM pruning for further efficiency gains. A fine-tuning scheme and approximator design optimization are used to control the accuracy impact of the analog approximate element-wise computation and hardware constraints.

## Contributions
- Use of ReRAM-based analog approximate computing for LSTM's element-wise (gate) operations, integrated with crossbar dot-product computation in a single processing tile
- A significant reduction in required ADCs compared to prior ReRAM LSTM accelerators with digital element-wise computation
- A mapping scheme to deploy large-scale LSTM models efficiently across multiple processing tiles
- An architecture enhancement supporting crossbar-friendly LSTM pruning, with a fine-tuning scheme to recover accuracy lost to approximation and hardware constraints

## Key claims (stable IDs)
- **2019_Han_ERALSTM_TPDS#C1** — ERA-LSTM substantially outperforms FPGA-based LSTM accelerators — _support:_ outperforms two state-of-the-art FPGA-based LSTM accelerators by 103.6x and 35.9x, respectively — _loc:_ Abstract
- **2019_Han_ERALSTM_TPDS#C2** — ERA-LSTM is more efficient than a prior ReRAM-based LSTM accelerator using digital element-wise computation — _support:_ 6.1x more efficient compared with a state-of-the-art ReRAM-based LSTM accelerator with digital element-wise computation — _loc:_ Abstract
- **2019_Han_ERALSTM_TPDS#C3** — Fine-tuning and approximator design optimization mitigate the accuracy impact of hardware constraints and approximation errors — _support:_ experiments demonstrate that the impact of hardware constraints and approximation errors on inference accuracy can be effectively reduced by the proposed fine-tuning scheme and by optimizing the design of the approximator — _loc:_ Abstract

## Results
- 103.6x and 35.9x efficiency improvement over two FPGA-based LSTM accelerators
- 6.1x improvement in efficiency over a state-of-the-art ReRAM-based LSTM accelerator with digital element-wise computation

## Limitations
- Analysis based on the abstract only; details of the approximate computing error model, ADC reduction factor, and benchmark LSTM sizes could not be verified from the full text
- Analog approximate computing for element-wise operations inherently trades some numerical accuracy for efficiency, requiring fine-tuning to recover accuracy (extent not independently verifiable here)

## Remarks
ERA-LSTM is a relevant data point for RNN/LSTM-specific crossbar mapping: unlike CNN-focused accelerators (ISAAC, PRIME), it explicitly tackles the element-wise (sigmoid/tanh-gated) operations that dominate LSTM's non-MAC compute, using ReRAM analog approximation to avoid a second round of digital logic and ADC conversions. Because only the abstract was available, the specific approximate-computing technique, fine-tuning procedure, and quantitative accuracy loss figures should be checked against the full TPDS paper before being cited beyond the headline speedup numbers.

## Cites (in collection, 7)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Long_ReRAMRnnPim_TVLSI](2018_Long_ReRAMRnnPim_TVLSI.md) ReRAM RNN PIM (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2017_Ankit_TraNNsformer_ICCAD](2017_Ankit_TraNNsformer_ICCAD.md) TraNNsformer (2017)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 2)
- [2021_Han_PolyhedralPIMCompiler_JETC](2021_Han_PolyhedralPIMCompiler_JETC.md) Polyhedral PIM Compiler (2021) — _background_: "Some memristor-based accelerators provide co-located MM and activation units [12, 33] to reduce the amount of data movement, and others directly implement fused operators to benefit from the efficient peripheral circuit design [18, 24]."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _uses-method-or-tool_: "We adopt a similar NoC implementation proposed in a prior work [31]."

## Files
- PDF: not available locally (save as `papers/03_Crossbar_Accelerator_Architectures/2019_Han_ERALSTM_TPDS.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tpds.2019.2962806
