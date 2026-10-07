---
id: W4416429987
key: 2025_Hou_SAGE_ICCAD
title: "SAGE: Saliency-Aware Grouping for Efficient Mapping of LLMs on Analog Compute-in-Memory"
short: "SAGE"
year: 2025
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2025)"
authors: "Y. Thomas Hou, Zhenyu Liu, Garrett Gagnon, Hsinyu Tsai, Kaoutar El Maghraoui, Geoffrey W. Burr, Liu Liu"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["Generic-NVM"]
models: ["Transformer", "GPT/LLM"]
lm_models: []
param_scale: "not specified"
slm: true
evidence: algorithm+simulation
topics: ["weight-mapping", "quantization", "language-models", "analog-mvm", "transformer-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 23
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/iccad66269.2025.11240907"
pdf: null
fulltext: null
---

# SAGE

**SAGE: Saliency-Aware Grouping for Efficient Mapping of LLMs on Analog Compute-in-Memory** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
SAGE is a training-free channel-reordering strategy for LLM fully-connected layers on analog compute-in-memory hardware that reduces output kurtosis (by grouping salient/long-tailed values together), improving signal-to-noise ratio and inference accuracy under hardware noise without retraining.

## Summary
The paper addresses the problem that analog compute-in-memory (ACIM) hardware struggles with the long-tailed, high-kurtosis activation/weight distributions typical of LLM fully-connected (FC) layers: large-amplitude 'salient values' degrade analog signal quality once quantized and exposed to system noise. SAGE (Saliency-Aware Grouping for Efficient Mapping) is proposed as a training-free strategy that reorders weight and input channels of FC layers based on their statistical characteristics, identifying kurtosis as the key factor harming analog robustness and developing a saliency-aware grouping method that reduces output kurtosis to boost SNR. A reconfigurable tile design is introduced alongside the mapping method to support mixed-precision execution and maximize crossbar array utilization across layers with heterogeneous precision needs. The approach is evaluated via ACIM simulation on multiple LLMs and benchmarks, reportedly improving both inference accuracy and energy efficiency without requiring any retraining of the model.

## Language models evaluated
- Models: —
- Scale: not specified
- Note: Only the abstract was available; LLM names/scales are not stated in the library text, targeting LLM FC-layer mapping onto analog CIM.

## Contributions
- Identifies kurtosis of per-channel output distributions as a key driver of analog-hardware noise sensitivity in LLM FC layers
- Proposes SAGE, a training-free channel-reordering/grouping method that reduces output kurtosis to improve SNR under ACIM noise and quantization
- Introduces a reconfigurable tile design supporting mixed-precision execution to maximize crossbar array utilization across layers
- Evaluates across multiple LLMs and benchmarks via ACIM simulation, reporting accuracy and energy-efficiency gains without retraining

## Key claims (stable IDs)
- **2025_Hou_SAGE_ICCAD#C1** — Reordering channels by saliency/kurtosis statistics (without any retraining) improves ACIM inference accuracy for LLMs — _support:_ Abstract: 'significantly improves inference accuracy and energy efficiency based on ACIM simulation without requiring retraining' — _loc:_ Abstract
- **2025_Hou_SAGE_ICCAD#C2** — Long-tailed, high-kurtosis activation distributions are a primary cause of degraded analog signal quality in LLM FC layers — _support:_ Abstract identifies kurtosis as 'a key factor affecting analog robustness' — _loc:_ Abstract

## Results
- No specific quantitative accuracy/energy numbers available from the abstract alone; full text was not accessible

## Limitations
- Full text not accessible to this reviewer (no open preprint found); exact benchmarks, noise models, and magnitude of improvement could not be verified
- Evaluation is simulation-based (ACIM simulator), not measured silicon

## Remarks
Abstract-only assessment: a legitimate open copy could not be located (ICCAD is not downloadable here and no arXiv preprint was found). The idea of exploiting a training-free statistical reordering of channels to tame outlier/long-tail activations is conceptually related to outlier-aware quantization work for LLMs (e.g., channel reordering/mixed precision seen in digital LLM quantization literature) but applied specifically to the SNR constraints of analog CIM arrays; this is a relevant and timely contribution to the 'mapping LLMs onto analog crossbars under noise' problem, though its quantitative strength cannot be verified without the full paper.

## Cites (in collection, 23)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019)
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2023_Li_H3DAtten_TVLSI](2023_Li_H3DAtten_TVLSI.md) H3DAtten (2023)
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023)
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2024_Yoshioka_CRCIM_JSSC](2024_Yoshioka_CRCIM_JSSC.md) CR-CIM (2024)
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025)
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025)
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025)

## Files
- PDF: not available locally (save as `papers/11_Small_Language_Models_on_AIMC/2025_Hou_SAGE_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccad66269.2025.11240907
