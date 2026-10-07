---
id: W4285122104
key: 2022_Lee_OfflineTrainingIRDropMitigation_TCAD
title: "Offline Training-Based Mitigation of IR Drop for ReRAM-Based Deep Neural Network Accelerators"
short: "Offline Training IR-Drop Mitigation"
year: 2022
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022)"
authors: "Sugil Lee, Mohammed E. Fouda, Jongeun Lee, Ahmed M. Eltawil, Fadi Kurdahi"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["ir-drop-parasitics", "hardware-aware-training", "noise-injection", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 11
citations_overall: 17
priority_score: 3.88
doi: "https://doi.org/10.1109/tcad.2022.3177002"
pdf: null
fulltext: null
---

# Offline Training IR-Drop Mitigation

**Offline Training-Based Mitigation of IR Drop for ReRAM-Based Deep Neural Network Accelerators** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Two neural-network IR-drop predictor models, trained to match SPICE-level 'golden' validation, are incorporated into DNN training (with incremental retraining) to recover accuracy lost to interconnect IR drop in ReRAM crossbars, avoiding expensive per-design SPICE simulation.

## Summary
Technology scaling increases ReRAM crossbar interconnect resistance, causing IR drops that degrade signal integrity and limit accelerator performance; predicting this effect normally requires expensive hardware emulation or SPICE simulation. The authors propose two neural-network models that predict IR-drop impact on DNN computation, validated to track SPICE-based ('golden') DNN accuracy closely across binary and quantized neural networks. These predictor models are then embedded into the DNN training framework so the network can be retrained (including via proposed incremental training methods) to compensate for IR-drop-induced errors ahead of deployment. SPICE-validated results on datasets including CIFAR-10 and SVHN show large performance recovery relative to baseline (non-IR-drop-aware) training, closing the gap to the SPICE golden-validation accuracy.

## Contributions
- Two neural-network models that predict the accuracy/computation impact of IR drop in ReRAM crossbars without requiring per-case SPICE simulation
- Validation of these predictor models against SPICE-based ('golden') DNN accuracy across binary and quantized DNNs
- Incorporation of the IR-drop predictor models directly into the DNN training loop to retrain networks for IR-drop robustness
- Incremental training methods proposed to further improve validation accuracy of the IR-drop-aware retraining
- SPICE-based validation on CIFAR-10 and SVHN confirming large accuracy recovery close to baseline performance

## Key claims (stable IDs)
- **2022_Lee_OfflineTrainingIRDropMitigation_TCAD#C1** — The proposed IR-drop prediction models can substitute for expensive SPICE simulation while tracking SPICE-validated DNN accuracy closely. — _support:_ Prediction models show similar performance (recognition accuracy) to golden SPICE-based DNN validation across binary and quantized DNN models — _loc:_ Abstract (full text not available)
- **2022_Lee_OfflineTrainingIRDropMitigation_TCAD#C2** — Retraining DNNs using the IR-drop prediction models (with incremental training) substantially recovers accuracy lost to IR drop, even on challenging datasets. — _support:_ SPICE-simulation-validated results show very high performance improvement close to baseline performance on datasets including CIFAR-10 and SVHN — _loc:_ Abstract (full text not available)

## Results
- IR-drop predictor models match SPICE-based 'golden' DNN validation accuracy across binary and quantized DNNs (per abstract; no specific numeric accuracy given)
- Incremental IR-drop-aware retraining yields large accuracy recovery, validated via SPICE simulation, on CIFAR-10 and SVHN (per abstract; specific percentage figures not given)

## Limitations
- Analysis is abstract-only here (full text not accessible from this machine) -- the exact predictor-model architecture, crossbar/wire-resistance assumptions, and quantitative accuracy-recovery numbers are not verifiable without the full text
- Approach is evaluated via SPICE simulation as the 'golden' reference rather than measured silicon; real-chip IR-drop behavior could differ from the SPICE model used

## Remarks
Tackles IR drop -- a non-ideality that worsens specifically with technology scaling and larger crossbars -- via a learned, SPICE-free predictor embedded in training, which is an efficient alternative to the expensive per-design circuit simulation used by other IR-drop-aware training works in this collection (e.g., IR-QNN Framework, cited in-set by this same group). The approach is methodologically consistent with the broader 'hardware-aware/non-ideality-aware training' trend seen elsewhere in this collection (D-NAT, NEAT, nonideality-aware training), applied specifically to the IR-drop non-ideality; without the full text, how well the learned predictors generalize across crossbar sizes/process corners beyond the tested binary/quantized networks could not be assessed here.

## Cites (in collection, 11)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018)
- [2019_Xia_MemristiveCrossbarArrays_NatMater](2019_Xia_MemristiveCrossbarArrays_NatMater.md) Xia-Yang Memristive Crossbars (2019)
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019)
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021)
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020)
- [2020_Charan_KDRSA_JXCDC](2020_Charan_KDRSA_JXCDC.md) KD+RSA (2020)
- [2020_Fouda_IRQNNFramework_IEEEAccess](2020_Fouda_IRQNNFramework_IEEEAccess.md) IR-QNN Framework (2020)
- [2021_Huang_IRDropFaultMitigation_JEDS](2021_Huang_IRDropFaultMitigation_JEDS.md) IR-Drop Fault Mitigation RRAM (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2022_Lee_OfflineTrainingIRDropMitigation_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2022.3177002
