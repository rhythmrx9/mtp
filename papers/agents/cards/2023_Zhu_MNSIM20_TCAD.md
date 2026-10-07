---
id: W4323022446
key: 2023_Zhu_MNSIM20_TCAD
title: "MNSIM 2.0: A Behavior-Level Modeling Tool for Processing-In-Memory Architectures"
short: "MNSIM 2.0"
year: 2023
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023)"
authors: "Zhenhua Zhu, Hanbo Sun, Tongxin Xie, Yu Zhu, Guohao Dai, Lixue Xia, Dimin Niu, Xiaoming Chen, Xiaobo Sharon Hu, Yu Kevin Cao, Yuan Xie, Huazhong Yang et al."
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM", "Generic-NVM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["simulator", "peripheral-circuits", "crossbar-architecture", "hardware-aware-training", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 9
cites_in_collection: 12
citations_overall: 72
priority_score: 7.3
doi: "https://doi.org/10.1109/tcad.2023.3251696"
pdf: null
fulltext: null
---

# MNSIM 2.0

**MNSIM 2.0: A Behavior-Level Modeling Tool for Processing-In-Memory Architectures** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2023) (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
MNSIM 2.0 is a behavior-level PIM modeling/simulation tool with a unified analog+digital memory-array model, PIM-aware NN training/quantization flow, and flexible scheduling, validated against fabricated PIM macros to within ~3.8-5.5% error.

## Summary
Successor to the widely used MNSIM simulator, built to address the need for efficient, flexible design-space exploration tools for Processing-In-Memory (PIM) accelerators as NN models and PIM hardware design spaces both grow. At the hardware level, MNSIM 2.0 provides a hierarchical, configurable and extensible modeling structure, including (per the abstract) the first unified PIM memory array model able to describe both digital and analog PIM arrays within the same framework. At the algorithm level, it supports accuracy simulation of PIM-based NN inference accounting for architecture and device non-idealities, and integrates a PIM-oriented NN training/quantization flow intended to recover performance lost to those non-idealities. At the scheduling level, it adopts a universal scheduling description meant to be compatible with multiple different mapping/scheduling strategies, rather than hard-coding one dataflow. The tool is validated against measurements from fabricated PIM macros, reporting a relative modeling error of about 3.8-5.5%, and the authors present case studies using MNSIM 2.0 for design-space exploration, device-parameter sensitivity analysis and architecture-design insight discovery.

## Contributions
- A hierarchical, configurable, extensible behavior-level PIM modeling framework (successor to MNSIM)
- A unified memory-array model spanning both digital and analog PIM arrays
- A PIM-oriented NN training and quantization flow integrated into the simulation loop to improve achievable performance
- A universal scheduling description compatible with multiple scheduling strategies
- Validation against fabricated PIM macros with reported ~3.8-5.5% modeling error, plus case studies for design-space exploration

## Key claims (stable IDs)
- **2023_Zhu_MNSIM20_TCAD#C1** — MNSIM 2.0's behavior-level model matches measured silicon PIM macros closely — _support:_ relative modeling error rate of 3.8-5.5% against fabricated PIM macros — _loc:_ Abstract
- **2023_Zhu_MNSIM20_TCAD#C2** — The tool enables productive design-space exploration and device/architecture insight discovery — _support:_ case studies on PIM design-space exploration, device-parameter influence analysis, and architecture insight discovery (per abstract) — _loc:_ Abstract / case studies

## Results
- Relative modeling error rate of 3.8-5.5% versus fabricated PIM macros (exact figure as stated in abstract)

## Limitations
- Abstract-only analysis in this record: no full text available, so method details (exact unified array model, training/quantization algorithm, scheduling description) could not be independently verified
- As a behavior-level simulator, it trades some circuit-level fidelity for speed/flexibility compared to SPICE-level tools

## Remarks
MNSIM 2.0 is a successor to one of the most cited open PIM simulation frameworks (original MNSIM is an in-set reference of this paper) and is itself cited by many later PIM compiler/simulator papers in this collection (CoMN, CiMLoop, PIMCOMP, PIMapping, etc.), indicating it functions as infrastructure the field builds on. Because only the abstract was available for this analysis, specific quantitative claims beyond the headline validation error could not be extracted; a full-text pass would be valuable given the tool's apparent influence.

## Cites (in collection, 12)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017)
- [2018_Lin_DLRSIM_ICCAD](2018_Lin_DLRSIM_ICCAD.md) DL-RSIM (2018)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Sun_EnergyEfficientQuantReg_ASPDAC](2020_Sun_EnergyEfficientQuantReg_ASPDAC.md) Quantized+Regularized PIM Training (2020)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2022_Zheng_PIMulatorNN_TCAD](2022_Zheng_PIMulatorNN_TCAD.md) PIMulator-NN (2022)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Cited by (in collection, 9)
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _contrasts/critiques_: "Unfortunately, some prior models may use inaccurate fixed-energy or fixed-power models [8, 9, 13] that do not model data-value-dependence."
- [2024_Sun_PIMCOMP_TCAD](2024_Sun_PIMCOMP_TCAD.md) PIMCOMP (TCAD) (2024) — _background_: "Due to the limited precision of crossbar array cells, high-precision weights usually need multiple crossbar arrays to store collaboratively [27]."
- [2025_Malekar_PimLlm_MWSCAS](2025_Malekar_PimLlm_MWSCAS.md) PIM-LLM (1-bit LLMs) (2025) — _uses-method-or-tool_: "To simulate the PIM component and assess its latency and energy consumption, we used MNSIM 2.0 [39] with 256 × 256 RRAM crossbars and 45nm 8-bit ADCs [40]."
- [2024_Han_CoMN_TCAD](2024_Han_CoMN_TCAD.md) CoMN (2024)
- [2025_Zhou_IMCsim_DAC](2025_Zhou_IMCsim_DAC.md) IMCsim (2025)
- [2025_Zhu_PIMapping_TCAD](2025_Zhu_PIMapping_TCAD.md) PIMapping (2025)
- [2025_Guo_NIPA_ICCAD](2025_Guo_NIPA_ICCAD.md) NIPA (2025)
- [2026_Wang_TriCIM_TVLSI](2026_Wang_TriCIM_TVLSI.md) TriCIM (2026)
- [2026_Zuo_Harmony_ISQED](2026_Zuo_Harmony_ISQED.md) Harmony (2026)

## Files
- PDF: not available locally (save as `papers/08_Simulation_and_Benchmarking_Frameworks/2023_Zhu_MNSIM20_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2023.3251696
