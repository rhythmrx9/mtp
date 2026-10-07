---
id: W4391164199
key: 2024_Han_CoMN_TCAD
title: "CoMN: Algorithm-Hardware Co-Design Platform for Nonvolatile Memory-Based Convolutional Neural Network Accelerators"
short: "CoMN"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Lixia Han, Renjie Pan, Zheng Zhou, Hairuo Lu, Yiyang Chen, Haozhang Yang, Peng Cheng Huang, Guangyu Sun, Xiaoyan Liu, Jinfeng Kang"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["simulator", "compiler-software-stack", "cnn-accelerator", "hardware-aware-training"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 11
citations_overall: 15
priority_score: 6.15
doi: "https://doi.org/10.1109/tcad.2024.3358220"
pdf: null
fulltext: null
---

# CoMN

**CoMN: Algorithm-Hardware Co-Design Platform for Nonvolatile Memory-Based Convolutional Neural Network Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
CoMN is a GUI-based algorithm-hardware co-design platform for NVM-based CIM CNN accelerators, providing an automatic CNN-to-chip mapper, joint accuracy/energy/latency/area evaluators, a nonideality- and energy-aware retraining 'algorithm adapter', and a hardware microarchitecture/circuit design-space optimizer.

## Summary
The paper addresses the complexity of co-designing NVM-based compute-in-memory (CIM) CNN accelerators, where the design space spans algorithm (model/weights), mapping, microarchitecture, and circuit levels, and design decisions at one level interact strongly with others, making ad hoc single-level design methodologies inefficient. CoMN is proposed as an integrated, browser-accessible platform with four main components: (1) a mapper that automatically maps CNN models onto CIM chips by optimizing pipelining, weight transformation, partitioning, and placement; (2) joint accuracy and performance evaluators that estimate accuracy, energy, latency, and area together, capturing cross-level design dependencies; (3) an algorithm adapter that retrains CNN weights to be more hardware-robust and energy-efficient via nonideality-aware training and energy-aware training under an energy budget; and (4) a hardware optimizer that searches the microarchitecture/circuit design space early in the design process. The authors demonstrate the platform through case studies showing it supports algorithm-hardware mapping, hardware-aware algorithm adaptation, hardware configuration exploration, and combined co-design, and make the tool publicly accessible online.

## Contributions
- Integrated, GUI-accessible algorithm-hardware co-design platform (CoMN) spanning model, mapping, microarchitecture, and circuit levels for NVM-based CIM CNN accelerators
- Automatic CNN-to-chip mapper optimizing pipeline scheduling, weight transformation, partitioning, and placement
- Joint accuracy/energy/latency/area evaluation framework that accounts for cross-level design dependencies rather than evaluating each level in isolation
- An 'algorithm adapter' performing nonideality-aware and energy-aware retraining of CNN weights to improve hardware accuracy within an energy budget
- A hardware optimizer for early-stage search of microarchitecture and circuit design choices
- Publicly hosted, browser-accessible deployment of the platform for use by other designers

## Key claims (stable IDs)
- **2024_Han_CoMN_TCAD#C1** — CoMN enables effective algorithm-hardware mapping, hardware-aware algorithm adaptation, hardware configuration exploration, and combined co-design in case studies. — _support:_ case-study demonstrations described in abstract — _loc:_ Case studies section (not verified in full text)
- **2024_Han_CoMN_TCAD#C2** — Jointly modeling accuracy, energy, latency, and area across design levels is necessary because of strong cross-level design dependencies in NVM-based CIM CNN accelerators. — _support:_ motivation and evaluator design rationale — _loc:_ Introduction / platform design rationale

## Results
- No specific quantitative benchmark numbers (e.g., speedup/energy-efficiency figures) are given in the abstract; the contribution is the platform/tooling and its qualitative demonstration via case studies

## Limitations
- Full text not available for this analysis; the abstract does not provide quantitative results, so the platform's accuracy of accuracy/energy/latency/area prediction versus ground truth (e.g., SPICE or silicon) is unknown from this review
- As a flexible platform paper, it may rely on simplified device/circuit models similar to other CIM DSE frameworks (e.g., NeuroSim-family tools); the fidelity of its nonideality-aware training versus real device characterization is unclear from the abstract alone
- Evaluated only on CNNs per the abstract; no evidence of support for transformers/LLMs

## Remarks
CoMN sits alongside other co-design/benchmarking frameworks (DNN+NeuroSim, MNSIM) in this collection as infrastructure for exploring the CIM CNN accelerator design space, distinguished by its explicit four-stage pipeline (mapper, joint evaluator, algorithm adapter, hardware optimizer) and public GUI/online access. Because only the abstract was available, the analysis here is necessarily qualitative; a follow-up read of the full text would be needed to assess how its accuracy/energy models are validated and how it compares quantitatively to NeuroSim-style tools already in the collection.

## Cites (in collection, 11)
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020)
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2023_Zhu_MNSIM20_TCAD](2023_Zhu_MNSIM20_TCAD.md) MNSIM 2.0 (2023)

## Cited by (in collection, 3)
- [2025_Krestinskaya_CIMNAS_TCASAI](2025_Krestinskaya_CIMNAS_TCASAI.md) CIMNAS (2025) — _contrasts/critiques_: "In contrast, CIM-based design space exploration focuses on identifying the optimal CIM hardware parameters for deploying a fixed neural network model [18, 19, 23]."
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2024_Han_CoMN_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2024.3358220
