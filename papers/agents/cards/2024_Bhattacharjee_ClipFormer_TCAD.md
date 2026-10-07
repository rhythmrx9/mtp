---
id: W4401070622
key: 2024_Bhattacharjee_ClipFormer_TCAD
title: "ClipFormer : Key–Value Clipping of Transformers on Memristive Crossbars for Write Noise Mitigation"
short: "ClipFormer"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)"
authors: "Abhiroop Bhattacharjee, Abhishek Moitra, Priyadarshini Panda"
category: "04 Transformer & Attention Accelerators (CIM / PIM)"
devices: ["ReRAM"]
models: ["ViT", "Transformer"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["attention", "kv-cache", "transformer-accelerator", "read-write-noise", "noise-injection", "hardware-aware-training", "weight-mapping", "device-variation"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 9
citations_overall: 5
priority_score: 6.45
doi: "https://doi.org/10.1109/tcad.2024.3435762"
pdf: "../../04_Transformers_and_LLMs/2024_Bhattacharjee_ClipFormer_TCAD.pdf"
fulltext: "../fulltext/2024_Bhattacharjee_ClipFormer_TCAD.txt"
---

# ClipFormer

**ClipFormer : Key–Value Clipping of Transformers on Memristive Crossbars for Write Noise Mitigation** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024) (2024)

## TL;DR
Shows that write noise on dynamically written K and V matrices makes pre-trained ViTs (DeiT-S) fragile on RRAM crossbars and proposes ClipFormer, a training-free conductance shift-and-clip of K/V that lifts DeiT-S non-ideal ImageNet accuracy from 22.59% to 64.05% at write-noise factor gamma=5.

## Summary
In attention, K and V are computed from the input and must be written into crossbars at inference time, so write noise (not only read noise) corrupts S(QK^T)V; in CNNs weights are pre-programmed and write noise is absent. The authors model write noise as G' = G + gamma*sqrt((G-Gmin)(Gmax-Gmin))*N(0,sigma^2) with gamma in {3,4,5}, so larger conductances suffer larger noise. ClipFormer (Algorithm 1) maps K and V to conductances then (I) subtracts alpha*Gmin (alpha>=1) and floors at Gmin, and (II) clips at beta*Gmax (0<beta<=1), shifting the conductance distribution toward low values and cutting write-noise variance. It needs no extra hardware or retraining and can be stacked on variation-aware training (VAT). Evaluation uses the authors' ViT-X framework: matrices partitioned into 64x64 RRAM crossbars (2 bits/cell, Rmin = 100 kohm, ON/OFF 100), 8-bit weights via bit-slicing and 8-bit inputs bit-serial, NeuroSim-style area/energy estimation; softmax, LayerNorm and GELU are digital. Models are pre-trained DeiT-S, Sparse DeiT-S (token pruned) and LV-ViT-S on ImageNet-1k. SNR of S(QK^T)V improves by ~1.5-1.9 dB.

## Contributions
- Identification of write noise on dynamically generated K/V as the main vulnerability of transformers on NVM crossbars
- ClipFormer: training-free, hardware-agnostic K/V conductance transformation (alpha, beta)
- ViT-X framework for non-ideal ViT inference with energy/area estimation of attention
- Demonstration that ClipFormer composes with VAT and reduces attention area/energy by fewer bit-slice crossbars

## Key claims (stable IDs)
- **2024_Bhattacharjee_ClipFormer_TCAD#C1** — ClipFormer substantially recovers DeiT-S accuracy under write noise without retraining — _support:_ gamma=5: 22.59% -> 64.05% (standard-trained, alpha=2, beta=0.25); gamma=4: 54.82% -> 68.81%; software baseline 79.76% — _loc:_ Table II
- **2024_Bhattacharjee_ClipFormer_TCAD#C2** — ClipFormer on top of VAT adds further gains — _support:_ VAT DeiT-S at gamma=5: 57.50% -> 69.21% — _loc:_ Table II / Sec. VI
- **2024_Bhattacharjee_ClipFormer_TCAD#C3** — Inference-only ClipFormer is competitive with 5x-training-cost VAT on Sparse DeiT-S — _support:_ gamma=5: 60.91% (ClipFormer on standard) vs 55.8% (VAT, no ClipFormer) vs 68.1% (VAT+ClipFormer) — _loc:_ Table III
- **2024_Bhattacharjee_ClipFormer_TCAD#C4** — ClipFormer lowers attention area and energy — _support:_ ~7-8% reduction in total attention area and energy; +11.71% (DeiT-S) / +4.34% (LV-ViT-S) accuracy at gamma=5 — _loc:_ Sec. VI-E / Fig. 10, Conclusion

## Results
- DeiT-S standard training, non-ideal accuracy without -> with ClipFormer: gamma=3 71.06 -> 74.64; gamma=4 54.82 -> 68.81; gamma=5 22.59 -> 64.05 (Table II)
- DeiT-S with VAT: gamma=3 76.04 -> 76.76; gamma=4 71.24 -> 74.8; gamma=5 57.50 -> 69.21 (Table II)
- Sparse DeiT-S standard: gamma=5 16.54 -> 60.91; token-pruned ViTs are more vulnerable than unpruned
- RRAM crossbars vs 64x64 digital SRAM IMC for ViT attention: ~5.1x less area, ~2.3x less energy (Fig. 1a)
- SNR of attention-block output improved ~1.5-1.9 dB (Fig. 7)
- VAT costs ~5x training complexity; ClipFormer has none (Table III)

## Key numbers
- array_size: 64x64
- energy_eff: ~2.3x attention energy reduction vs SRAM IMC (Fig. 1a)
- accuracy: DeiT-S 64.05% at gamma=5 with ClipFormer (22.59% without; SW 79.76%)
- bits_weight: 8b (2b/cell bit-sliced)

## Datasets / benchmarks
ImageNet-1k

## Limitations
- Vision transformers only (DeiT-S, LV-ViT-S, ImageNet); no language models or decoder attention with long sequences
- Simulation with an analytic write-noise model; no measured device data or silicon
- alpha/beta must be tuned per noise level (e.g. beta=0.25 at high gamma)
- Read noise and IR drop handled lightly; softmax/LayerNorm/GELU assumed digital and ideal
- Clipping reduces dynamic range of K/V, whose accuracy cost is only evaluated empirically

## Remarks
A useful, clearly reasoned observation that the dynamic operands of attention make write noise a first-order issue, which is a core obstacle for putting attention (and KV-cache) on NVM and argues for either low-conductance encoding or keeping K/V in SRAM/DRAM-like digital or low-noise analog memory. The method is simple and training-free, but evidence is ViT/ImageNet simulation; whether it transfers to autoregressive LM KV caches is untested. Pairs with hybrid approaches in the collection (e.g. analog attention with gain-cell memory) that avoid NVM writes for K/V.

## Cites (in collection, 9)
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _uses-method-or-tool_: "These voltages interact with the synaptic device conductances (Gij), as shown in Fig. 3, resulting in the generation of a current (following Ohm's Law) [5, 22]."
- [2021_Roy_TxSim_TVLSI](2021_Roy_TxSim_TVLSI.md) TxSim (2021) — _uses-method-or-tool_: "The noisy conductance G′ under write noise [12, 25] is given as G′ = G + ñW , where the write noise ñW is modelled as:"
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _background_: "Previous works have demonstrated the effectiveness of using NVM devices with higher ON/OFF ratios to reduce read variations during inference of deep neural networks [14], [29]–[31]."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _baseline/comparison_: "Fig. 1(a) presents a radar chart that compares a ViT model inferred on analog RRAM crossbars against digital SRAM-based IMC arrays [14] (devoid of read and write non-idealities)."
- [2021_Bhattacharjee_NEAT_TCAD](2021_Bhattacharjee_NEAT_TCAD.md) NEAT (2021) — _uses-method-or-tool_: "In step- 2 , we partition these matrices into multiple NVM crossbars of size 64×64 [13, 22]."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _background_: "Recent works [7–10] have proposed compact, energy-efficient and lowlatency implementations of transformers on IMC architectures using efficiency-driven hardware optimizations and architectural modifications."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _background_: "Previous works have demonstrated the effectiveness of using NVM devices with higher ON/OFF ratios to reduce read variations during inference of deep neural networks [14], [29]–[31]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "Recent works [7–10] have proposed compact, energy-efficient and lowlatency implementations of transformers on IMC architectures using efficiency-driven hardware optimizations and architectural modifications."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _background_: "These nonidealities primarily arise from the NVM devices (such as stochastic read and write noise), resulting in inaccurate MVMs in the crossbars and thereby, reduced inference accuracy for AI workloads [11], [13], [15]."

## Cited by (in collection, 1)
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _background_: "In particular, to mitigate data-transfer overhead of weights loading, several approaches leverage either near-memory or in-memory computing (IMC)17–21."

## Files
- PDF: [../../04_Transformers_and_LLMs/2024_Bhattacharjee_ClipFormer_TCAD.pdf](../../04_Transformers_and_LLMs/2024_Bhattacharjee_ClipFormer_TCAD.pdf)
- Full text: [../fulltext/2024_Bhattacharjee_ClipFormer_TCAD.txt](../fulltext/2024_Bhattacharjee_ClipFormer_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2024.3435762
