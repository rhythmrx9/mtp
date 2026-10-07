---
id: W2811080765
key: 2018_Long_ReRAMRnnPim_TVLSI
title: "ReRAM-Based Processing-in-Memory Architecture for Recurrent Neural Network Acceleration"
short: "ReRAM RNN PIM"
year: 2018
venue: "TVLSI"
venue_full: "IEEE Transactions on Very Large Scale Integration (VLSI) Systems"
authors: "Yun Long, Taesik Na, Saibal Mukhopadhyay"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["LSTM/RNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["recurrent-models", "crossbar-architecture", "peripheral-circuits", "tiling-partitioning", "weight-mapping"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 8
cites_in_collection: 5
citations_overall: 123
priority_score: 7.32
doi: "https://doi.org/10.1109/tvlsi.2018.2819190"
pdf: null
fulltext: null
---

# ReRAM RNN PIM

**ReRAM-Based Processing-in-Memory Architecture for Recurrent Neural Network Acceleration** — IEEE Transactions on Very Large Scale Integration (VLSI) Systems (2018)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
A ReRAM-based processing-in-memory architecture redesigned specifically for recurrent neural networks (rather than reused CNN-oriented designs) reports roughly 79x computing-efficiency improvement over a GPU baseline, with device-level guidance on required read-noise, resistance, and write-latency margins.

## Summary
The paper presents an RNN accelerator built on ReRAM-based processing-in-memory (PIM), distinguishing itself from prior ReRAM accelerators that targeted convolutional neural networks by redesigning the architecture and dataflow to suit RNN structure. It evaluates system throughput and energy efficiency using detailed circuit and device characterization, supports reprogrammability, and introduces an RNN-friendly pipeline to raise throughput. Reported results (abstract-level) show an average 79x improvement in computing efficiency over a GPU baseline. The authors also derive device-level design constraints from their simulation: read-noise standard deviation should stay below 0.2, device resistance should be at least 1 MOhm, and device write latency should be minimized to preserve both accuracy and efficiency.

## Contributions
- A ReRAM-based processing-in-memory architecture redesigned specifically for RNN acceleration, rather than adapting a CNN-oriented crossbar design
- An RNN-friendly pipeline intended to increase system throughput over naive crossbar mapping of RNN computation
- Reprogrammable crossbar design to support different RNN workloads
- Device/circuit-level characterization translated into concrete device design constraints (noise, resistance, write latency) needed for accurate and efficient RNN inference

## Key claims (stable IDs)
- **2018_Long_ReRAMRnnPim_TVLSI#C1** — The proposed ReRAM PIM RNN accelerator achieves large average throughput/efficiency gains over a GPU baseline — _support:_ 79x improvement of computing efficiency compared with a GPU baseline (reported in abstract) — _loc:_ Abstract
- **2018_Long_ReRAMRnnPim_TVLSI#C2** — Device noise and resistance must be bounded for the RNN accelerator to maintain accuracy and efficiency — _support:_ simulation indicates read noise standard deviation should be < 0.2, device resistance should be at least 1 MOhm, and write latency should be minimized — _loc:_ Abstract

## Results
- ~79x average computing-efficiency improvement vs. GPU baseline (abstract-level figure; full-text methodology not available to verify benchmark details)

## Limitations
- Full text was not accessible (IEEE Xplore paywalled, no legitimate open-access copy found); this entry is based on title/abstract only, so method details, exact benchmarks, and all numeric results beyond the headline figure could not be verified
- Evidence basis appears to be simulation with device-characterization parameters rather than a fabricated chip

## Remarks
Abstract-only analysis: could not locate a legitimate open copy (not on arXiv/OpenReview/author pages indexed by OpenAlex/Semantic Scholar; IEEE Xplore is not accessible from this environment), so claims beyond the abstract are not verified. The paper is notable in the mapping/architecture literature as an early (2018) example of specializing a ReRAM PIM accelerator for RNN/LSTM workloads rather than reusing CNN-oriented crossbar designs (e.g., ISAAC, PRIME), and is cited by later ReRAM-based RNN/LSTM and Transformer accelerator work (ERA-LSTM, ReTransformer) as prior art for recurrent-workload mapping on ReRAM. Given the abstract-only basis, the 79x efficiency figure and the device-constraint thresholds (noise std < 0.2, R >= 1 MOhm) should be treated as reported but unverified pending access to the full text.

## Cites (in collection, 5)
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 8)
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _background_: "A ReRAM-based PIM design for RNN [20] extends to RNN acceleration with multiplier arrays and special function units to handle element-wise multiplication and nonlinear functions."
- [2021_Yang_CFMESMO_ICCAD](2021_Yang_CFMESMO_ICCAD.md) CF-MESMO / ReSNA (2021) — _background_: "ReRAM-based accelerators for fast and efficient DNN training and inferencing have been extensively studied [3–8]."
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _background_: "We sort out the designs of recent CIM accelerators from three dimensions: memory device, architecture hierarchy, and programming interface, and summarize them in Figure 1 [4, 6, 13, 18, 19, 21, 23, 28, 29, 33, 34, 39, 43, 46–51]."
- [2019_Liu_XB-Sim_CAL](2019_Liu_XB-Sim_CAL.md) XB-Sim (2019)
- [2019_Han_ERALSTM_TPDS](2019_Han_ERALSTM_TPDS.md) ERA-LSTM (2019)
- [2021_Sun_UnaryOptimalMapping_TCAD](2021_Sun_UnaryOptimalMapping_TCAD.md) Unary Optimal Mapping (2021)
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021)
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)

## Files
- PDF: not available locally (save as `papers/03_Crossbar_Accelerator_Architectures/2018_Long_ReRAMRnnPim_TVLSI.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tvlsi.2018.2819190
