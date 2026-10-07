---
id: W4410584352
key: 2025_Hou_NORA_DATE
title: "NORA: Noise-Optimized Rescaling of LLMs on Analog Compute-in-Memory Accelerators"
short: "NORA"
year: 2025
venue: "DATE"
venue_full: "Design, Automation and Test in Europe Conference (DATE 2025)"
authors: "Y. Thomas Hou, Hsinyu Tsai, Kaoutar El Maghraoui, Tayfun Gokmen, Geoffrey W. Burr, Liu Liu"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM"]
models: ["GPT/LLM"]
lm_models: ["OPT-1.3B", "OPT-2.7B", "OPT-6.7B", "OPT-13B", "LLaMA-2-7B", "LLaMA-3-8B", "Mistral-7B-v1.0"]
param_scale: "1.3B-13B"
slm: true
evidence: algorithm+simulation
topics: ["language-models", "quantization", "adc-dac", "noise-injection", "calibration-compensation", "analog-mvm", "weight-mapping", "simulator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 16
citations_overall: 4
priority_score: 10.29
doi: "https://doi.org/10.23919/date64628.2025.10993217"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Hou_NORA_DATE.pdf"
fulltext: "../fulltext/2025_Hou_NORA_DATE.txt"
---

# NORA

**NORA: Noise-Optimized Rescaling of LLMs on Analog Compute-in-Memory Accelerators** — Design, Automation and Test in Europe Conference (DATE 2025) (2025)

## TL;DR
First systematic sensitivity study of LLMs to analog CIM noise (LLMs resilient to weight noise but sensitive to ADC/DAC quantization and additive Gaussian I/O noise) plus NORA, a SmoothQuant-like per-channel rescaling that moves the burden from activations to weights, bringing OPT-6.7B/13B on simulated PCM CIM to <1% accuracy loss versus ~30% without it.

## Summary
Directly mapping LLMs to analog CIM tiles degrades accuracy because activations contain outliers (e.g., kurtosis 113.61 for Mistral-7B layer-2 activations versus 1.25 for weights) that clash with low-resolution ADC/DAC and existing noise/bound management, and hardware-aware training is prohibitive for billion-parameter models. The authors use AIHWKIT (512x512 tiles, 7-bit DAC and ADC, output noise 0.04, IR-drop scale 1.0, short-term weight noise 0.0175) with all nn.Linear layers converted to AnalogLinear (weights on PCM tiles), while normalization, activations and self-attention run in digital full precision. A sensitivity study (Fig. 3) scales each non-ideality to equal MSE and finds additive output/input Gaussian noise and ADC/DAC quantization most harmful (OPT especially to quantization), while IR-drop, short-term read noise, S-shaped nonlinearity and programming noise barely matter. NORA adds a per-channel factor s_k = max|x_k|^lambda / max|w_k|^(1-lambda), computed offline from a Pile calibration set, dividing input channels before the DAC and multiplying the corresponding weight rows before programming; this tightens the input distribution (lower kurtosis) and shrinks alpha*gamma, increasing the output current into the ADC and so SNR. It is a post-training method with no fine-tuning, evaluated on Lambada word prediction.

## Language models evaluated
- Models: OPT-1.3B, OPT-2.7B, OPT-6.7B, OPT-13B, LLaMA-2-7B, LLaMA-3-8B, Mistral-7B-v1.0
- Scale: 1.3B-13B
- Note: OPT-6.7B evaluated on simulated analog CIM hardware with noise-optimized rescaling (below 10B, SLM scale).

## Contributions
- First systematic sensitivity study of LLM accuracy to analog CIM non-idealities (OPT, LLaMA, Mistral)
- Insight that LLMs are input/output-noise sensitive but weight-noise resilient, with OPT most sensitive to quantization due to activation outliers
- NORA: post-training noise-optimized rescaling that moves the non-ideality burden from activations to weights, needing no hardware-aware training
- Analysis via kurtosis and output-current (alpha*gamma) showing improved SNR and fewer clipping/saturation events

## Key claims (stable IDs)
- **2025_Hou_NORA_DATE#C1** — LLMs are most sensitive to additive Gaussian I/O noise and ADC/DAC quantization and are robust to IR-drop, short-term read noise, programming noise and S-shape nonlinearity — _support:_ Fig. 3: scaling these to 0.0027 MSE on 4096x4096 map gives no accuracy drop — _loc:_ Sec. III-A, Fig. 3
- **2025_Hou_NORA_DATE#C2** — NORA brings OPT-6.7B and OPT-13B to <1% accuracy loss versus FP, compared with ~30% loss naive (OPT-2.7B loses >40% naive) — _support:_ Lambada accuracy — _loc:_ Abstract, Sec. V-A, Fig. 5a
- **2025_Hou_NORA_DATE#C3** — LLaMA-2-7B, LLaMA-3-8B and Mistral-7B retain accuracy with NORA — _support:_ LLaMA-2 87.99 vs 89.04; LLaMA-3 81.33 vs 82.92; Mistral 86.55 vs 87.41 (Lambada acc %) — _loc:_ Table III
- **2025_Hou_NORA_DATE#C4** — NORA recovers ~75% of the ADC-quantization-induced and ~10% of the DAC-induced accuracy drop on OPT-6.7B, and 60-70% of drop from additive output noise on OPT — _support:_ equal-MSE noise scaling — _loc:_ Sec. V-B, Fig. 5b-c

## Results
- Naive analog (Table II settings): catastrophic degradation, >40% drop for OPT-2.7B
- NORA: <1% loss for OPT-6.7B/13B, <1.6% for LLaMA-2/3, <1% for Mistral-7B (Lambada)
- Lambada accuracy digital vs NORA: LLaMA-2-7B 89.04 -> 87.99; LLaMA-3-8B 82.92 -> 81.33; Mistral-7B 87.41 -> 86.55
- Input kurtosis drops sharply after NORA with slightly higher weight kurtosis; alpha*gamma reduced, giving larger ADC input current

## Key numbers
- array_size: 512x512 tiles
- accuracy: <1% loss OPT-6.7B/13B vs ~30% naive; Lambada 87.99% LLaMA-2-7B, 81.33% LLaMA-3-8B, 86.55% Mistral-7B
- bits_weight: analog PCM (continuous)
- bits_adc: 7b ADC, 7b DAC

## Datasets / benchmarks
Lambada, The Pile (calibration)

## Limitations
- Simulation only (AIHWKIT), no hardware; PCM drift ignored in main results and gains shrink after 1 h of drift for some models (stated)
- No models above 13B; only Lambada word-prediction task evaluated
- Self-attention, normalization and activations assumed digital full-precision; attention matmuls not on analog tiles
- Digital pre/post scaling per channel adds overhead not quantified; lambda tuning/calibration details limited
- Short 4-page paper; sensitivity done per-noise rather than jointly with drift

## Remarks
Directly relevant to the collection's SLM theme: it moves beyond the BERT-scale (110M) studies of Rasch et al. to 1.3B-13B decoder LLMs and shows the key lever is activation-outlier handling at the DAC/ADC boundary rather than weight noise, consistent with IBM's earlier finding that input/output noise dominates. As a SmoothQuant adaptation it is training-free and cheap, but evidence is simulation with a single metric, and drift/ReRAM variants are untested. Together with HWA-training works it frames outlier-aware scaling as a complement to noise-aware fine-tuning for analog LLMs.

## Cites (in collection, 16)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "However, most previous works [11]–[13], [28] require hardware-aware training, which is non-trivial, if not prohibitive for LLMs with large number of parameters."
- [2019_Imani_FloatPIM_DAC](2019_Imani_FloatPIM_DAC.md) FloatPIM (2019) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _motivation_: "First, input and output activations on CIM devices have to be quantized into lower precision compared with digital cores due to the energy and area constraints of high-resolution Analog/Digital converters [2], [26]."
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020) — _background_: "Early work on Analog CIM accelerators mostly focus on the precision of weight-programming [3], [22], [23], which provides a mutual understanding of Analog CIM working mechanism and robust on-tile data storage."
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021) — _uses-method-or-tool_: "We use the analog in-memory hardware acceleration kit (AIHWKIT) [27] to evaluate model accuracy on Analog CIM tiles."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _contrasts/critiques_: "However, most previous works [11]–[13], [28] require hardware-aware training, which is non-trivial, if not prohibitive for LLMs with large number of parameters."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _background_: "Furthermore, weight programming [3], [21], [22], as well as weight-related long-term non-ideality compensation techniques [14], [28], are well studied."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _uses-method-or-tool_: "Hence, for transformer models, the self-attention is deployed on digital tiles or digital cores [9], [18], [20]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _contrasts/critiques_: "However, most previous works [11]–[13], [28] require hardware-aware training, which is non-trivial, if not prohibitive for LLMs with large number of parameters."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _extends/builds-on_: "Prior studies on hardware-aware training consider a diverse set of non-idealities such as quantization noise, weight drifting, programming noise, IR drop, device non-linearity, and additive noise [11], [28]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _contrasts/critiques_: "Hence, the noise management and bound management in previous works [7], [14], [28] could become less effective in LLMs due to the input distribution, as shown in Figure 1, and will be further discussed in Section II and Section III."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _uses-method-or-tool_: "Hence, for transformer models, the self-attention is deployed on digital tiles or digital cores [9], [18], [20]."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _motivation_: "Though NVM cells could be reprogrammed, the programming of NVM devices is too expensive [17], [34]."

## Cited by (in collection, 3)
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _extends/builds-on_: "To study the impact of post-training optimization techniques, we used the full AIHWKit to study the accuracy and noise-resilience of OPT, Llama, and Mistral models ranging from 2.7-13B weights [26]."
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _extends/builds-on_: "In recent works, we have shown that analog hardware-aware training [23] and posttraining adaptation [24] can effectively mitigate these effects, suggesting that accuracy is not the fundamental barrier to deploying AIMC for LLM inference."
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Hou_NORA_DATE.pdf](../../11_Small_Language_Models_on_AIMC/2025_Hou_NORA_DATE.pdf)
- Full text: [../fulltext/2025_Hou_NORA_DATE.txt](../fulltext/2025_Hou_NORA_DATE.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.23919/date64628.2025.10993217
