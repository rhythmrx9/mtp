---
id: W4417092543
key: 2025_Buchel_AnalogFoundationModels_NeurIPS
title: "Analog Foundation Models"
short: "Analog Foundation Models"
year: 2025
venue: "NeurIPS"
venue_full: "39th Conference on Neural Information Processing Systems (NeurIPS 2025)"
authors: "Julian Büchel, Iason Chalas, Giovanni Acampa, An Chen, Omobayode I. Fagbohungbe, Hsinyu Tsai, Kaoutar El Maghraoui, Manuel Le Gallo, Abbas Rahimi, Abu Sebastian"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM", "ReRAM"]
models: ["GPT/LLM", "Transformer"]
lm_models: ["Phi-3-mini-4k-instruct (3.8B)", "Llama-3.2-1B-Instruct"]
param_scale: "1B–3.8B"
slm: true
evidence: algorithm+simulation
topics: ["language-models", "hardware-aware-training", "noise-injection", "quantization", "adc-dac", "analog-mvm", "write-verify-programming", "heterogeneous-analog-digital"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 2
cites_in_collection: 12
citations_overall: 2
priority_score: 12.26
doi: "https://doi.org/10.52202/085713-2044"
pdf: "../../11_Small_Language_Models_on_AIMC/2025_Buchel_AnalogFoundationModels_NeurIPS.pdf"
fulltext: "../fulltext/2025_Buchel_AnalogFoundationModels_NeurIPS.txt"
---

# Analog Foundation Models

**Analog Foundation Models** — 39th Conference on Neural Information Processing Systems (NeurIPS 2025) (2025)

## TL;DR
Distillation-based hardware-aware training on 20B self-generated tokens makes Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct robust to PCM-chip programming noise plus static 8-bit input and globally fixed 8-bit output quantization, cutting the average accuracy drop vs FP16 from 8.01%/9.81% to 3.81%/4.58% (Table 1).

## Summary
Off-the-shelf LLMs lose accuracy on noisy, low-precision AIMC hardware, and prior HWA training was only shown on small CNN/RNN/encoder models with full access to training data. The paper adapts the LLM-QAT pipeline: the pre-trained model samples synthetic text (20B tokens via vLLM), and the analog model is trained by knowledge distillation from the original FP16 model using AIHWKIT-Lightning. HWA features are learnable static 8-bit input ranges (DAC, initialised by EMA of kappa*std), globally fixed 8-bit output ranges (ADC, identical across layers, trained with STE), per-channel additive Gaussian weight noise (gamma 0.02-0.03 of per-channel max) and iterative weight clipping after each optimizer step (alpha*std). Assumed hardware: heterogeneous accelerator with static-weight linear layers in analog crossbars (weights proportional to conductance), while attention, activations, norms and KV-cache stay digital FP16. Evaluation uses a noise model of a 64-core PCM AIMC chip (programming noise dominant; Le Gallo et al.) plus generic Gaussian noise, with 10 seeds, over 12 benchmarks (MMLU, GSM8K, BoolQ, HellaSwag, MedQA, AGIEval, ARC-C/E, ANLI, IFEval, XSTest, MATH-500). Analog FMs beat LLM-QAT and SpinQuant under noise, can be RTN-quantized to W4 for digital hardware, and scale better with test-time compute (up to +4.74% on MATH-500).

## Language models evaluated
- Models: Phi-3-mini-4k-instruct (3.8B), Llama-3.2-1B-Instruct
- Scale: 1B–3.8B
- Note: Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct (SLM scale) trained hardware-aware and evaluated under simulated AIMC noise (AIHWKIT-Lightning) and digital low-bit baselines; GPUs used for training.

## Contributions
- Data-generation and HWA distillation pipeline that turns pre-trained LLMs into analog foundation models without original pre-training data
- Two released analog models (Phi-3-mini-4k-instruct, Llama-3.2-1B-Instruct) reaching W4A8-level accuracy under hardware-realistic PCM noise and static I/O quantization
- Broad 12-benchmark evaluation incl. instruction following and safety, with 10 noise seeds
- Byproduct: models are also robust to RTN 4-bit weight quantization for low-precision digital hardware
- Evidence of equal or better test-time compute scaling than W4A8 QAT models

## Key claims (stable IDs)
- **2025_Buchel_AnalogFoundationModels_NeurIPS#C1** — Off-the-shelf LLMs lose 8.01% (Phi-3-mini) and 9.81% (Llama-3.2-1B) average accuracy under PCM-chip programming noise alone — _support:_ 21.43% / 23.2% drop on GSM8K — _loc:_ Sec. 4.1, Table 1
- **2025_Buchel_AnalogFoundationModels_NeurIPS#C2** — Analog FMs reduce the average gap to FP16 to 3.81% (Phi-3) and 4.58% (Llama-1B) including static 8-bit input and globally static 8-bit output quantization — _support:_ gap reduced by up to 12.87% on hard tasks vs LLM-QAT — _loc:_ Sec. 4.1, Table 1
- **2025_Buchel_AnalogFoundationModels_NeurIPS#C3** — For LLMs weight clipping gives more noise robustness than noise injection, and the combination is best — _support:_ clipping maps small weights to higher-SNR conductances in the PCM model — _loc:_ Sec. 3.1, Appendix C/D
- **2025_Buchel_AnalogFoundationModels_NeurIPS#C4** — Globally static 8-bit ADC ranges cost only 0.2-0.5% average accuracy when trained with plain STE — _support:_ contrasts with >400 perplexity increase reported by Zhang et al. with simple QAT — _loc:_ Sec. 3.1, Appendix C
- **2025_Buchel_AnalogFoundationModels_NeurIPS#C5** — Analog FMs show better test-time-compute scaling than W4A8 LLM-QAT models — _support:_ up to +4.74% on MATH-500; gap to original shrinks 0.4% (Phi-3) and 3.58% (Llama-1B) as n grows — _loc:_ Sec. 4.4, Fig. 4

## Results
- Average accuracy drop under hw noise: 8.01%->3.81% (Phi-3-mini) and 9.81%->4.58% (Llama-3.2-1B) (Table 1)
- SpinQuant W4 models are less noise robust than the off-the-shelf FP16 model; e.g. SpinQuant SI8-W4 Phi-3 drops to 29.67 avg under hw noise (Table 1)
- Training: 20B tokens, 96 V100 GPUs, ~230 h (Phi-3) and ~90 h (Llama-1B)
- Noise injection and I/O quantization make the linear kernel ~3x slower; slower convergence (Appendix H)
- Gains from more training tokens saturate around 20B (Appendix B)

## Key numbers
- accuracy: Avg gap to FP16 3.81% (Phi-3-mini-4k) / 4.58% (Llama-3.2-1B) under PCM noise
- bits_weight: W16 analog (noise-injected); W4 RTN for digital
- bits_adc: 8b output, 8b static input

## Datasets / benchmarks
MMLU, GSM8K, BoolQ, HellaSwag, MedQA, AGIEval, ARC-Challenge, ARC-Easy, ANLI, IFEval, XSTest, MATH-500

## Limitations
- Hardware is idealised: attention, activations and KV-cache stay in digital FP16; no energy/latency measurement
- Noise model dominated by programming noise from one PCM chip; read noise/drift tested only in an extra experiment
- Resource-intensive training (20B tokens, ~230 GPU-hours x 96 V100); only 1B and 3.8B models
- Remaining gap to FP16 is large on reasoning tasks (GSM8K, MATH-500)
- Evaluated by simulation, not on a real AIMC chip

## Remarks
Currently the strongest evidence that HWA training scales from small CNN/BERT models to instruction-tuned billion-scale LLMs, with unusually broad benchmarking and multi-seed noise evaluation. Useful lessons for crossbar mapping are that fixed global ADC ranges and static DAC ranges are handled cheaply with STE, and that weight clipping to use high-SNR conductances matters more than noise injection. The authors themselves point to HWA low-rank adaptation to cut training cost (followed by later LoRA-for-AIMC work in the collection). System-level benefit is not quantified here and must come from architecture papers.

## Use in the original review
- F4 (High confidence): Hardware-aware training — injecting realistic device noise during training or fine-tuning — is the field's dominant and empirically validated mitigation, and it now scales to pre-trained LLMs. On under 1% of pre-training tokens, Phi-3-mini-4k-instruct and Llama-3.2-1B-Instruct retained accuracy comparable to 4-bit-weight / 8-bit-activation quantized baselines under hardware-realistic analog noise — a gap off-the-shelf LLMs cannot close on their own.

## Cites (in collection, 12)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Analog in-Memory Computing (AIMC) addresses both compute efficiency and data movement by performing fully-parallel Matrix-Vector Multiplications (MVMs) in the analog domain [13, 14] on stored weight matrices, without having to move the weight data to an external processor (see figure 1)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _background_: "In order to store larger neural networks fully on-chip, a more scalable memory technology must be used, which is why researchers explored AIMC with dense Non-Volatile Memory (NVM) such as embedded flash [18], Phase Change Memory (PCM) [19, 20], ReRAM [21, 22], or MRAM [23]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "The efficacy of these methods has been successfully validated on recently developed AIMC chips [19–21] for small CNNs and RNNs with less than 50 million parameters."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "In order to store larger neural networks fully on-chip, a more scalable memory technology must be used, which is why researchers explored AIMC with dense Non-Volatile Memory (NVM) such as embedded flash [18], Phase Change Memory (PCM) [19, 20], ReRAM [21, 22], or MRAM [23]."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _motivation_: "This can yield up to three orders of magnitude higher energy efficiency compared to state-of-the-art GPUs when running Mixture of Experts (MoE)-based LLMs [26]."
- [2020_Nandakumar_PCMWeightPrecision_IEDM](2020_Nandakumar_PCMWeightPrecision_IEDM.md) PCM Weight Precision (2020) — _background_: "Static weight noise (does not get resampled during inference) is mainly due to programming noise, which is the conductance error from the target weight that remains after a device has been programmed with an iterative read-write-verify programming scheme [27]."
- [2019_Nandakumar_PCMDeviceModels_ICECS](2019_Nandakumar_PCMDeviceModels_ICECS.md) PCM Device Models (2019) — _background_: "Dynamic weight noise sources whose magnitude vary as a function of time include read noise [28] – due to analog 1/f noise of devices and circuits – and temporal conductance drift, which is the decrease in device conductance over time that is notably observed in PCM devices [33]."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _contrasts/critiques_: "Previous works that study HWA training for AIMC-based hardware are limited to CNNs [35, 48, 49], RNNs [37], LSTMs [37, 49, 50], GANs [51] and small encoder-only transformers [37, 52]."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _extends/builds-on_: "However, in contrast to many reduced-precision training papers that assume that the quantization ranges can be dynamically recomputed per-token [43, 44], AIMC typically uses static ranges [37, 45]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _background_: "The result is then send to either another AIMC core, a Digital Processing Unit (DPU), or a RISC-V in a heterogeneous multi-core architecture [41, 42]."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _contrasts/critiques_: "Previous works that study HWA training for AIMC-based hardware are limited to CNNs [35, 48, 49], RNNs [37], LSTMs [37, 49, 50], GANs [51] and small encoder-only transformers [37, 52]."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _uses-method-or-tool_: "Finally, to test the robustness to other types of noise, we conducted experiments where we inject read noise and apply conductance drift according to a publicly available noise model based on hardware [73]."

## Cited by (in collection, 2)
- [2026_Li_AHWA-LoRA_NeuromorphComputEng](2026_Li_AHWA-LoRA_NeuromorphComputEng.md) AHWA-LoRA (2026) — _uses-method-or-tool_: "During inference, we evaluated model robustness against Gaussian noise applied to weights, following methodologies established in prior studies22,28."
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _extends/builds-on_: "In recent works, we have shown that analog hardware-aware training [23] and posttraining adaptation [24] can effectively mitigate these effects, suggesting that accuracy is not the fundamental barrier to deploying AIMC for LLM inference."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2025_Buchel_AnalogFoundationModels_NeurIPS.pdf](../../11_Small_Language_Models_on_AIMC/2025_Buchel_AnalogFoundationModels_NeurIPS.pdf)
- Full text: [../fulltext/2025_Buchel_AnalogFoundationModels_NeurIPS.txt](../fulltext/2025_Buchel_AnalogFoundationModels_NeurIPS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.52202/085713-2044
