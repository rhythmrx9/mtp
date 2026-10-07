---
id: W7134813260
key: 2026_Wu_HaLoRA_TODAES
title: "Hardware-aware Low-Rank Adaptation for Large Language Models Based on Hybrid Compute-in-Memory Architecture"
short: "HaLoRA"
year: 2026
venue: "TODAES"
venue_full: "ACM Transactions on Design Automation of Electronic Systems"
authors: "Taiqiang Wu, Chenchen Ding, Weitao Zhou, Yuxin Cheng, Xincheng Feng, Shuqi Wang, Wendong Xu, Chufan Shi, Zhengwu Liu, Ngai Wong"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "SRAM-digital"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["Qwen2.5-0.5B", "LLaMA-3.2-1B", "LLaMA-3.2-3B"]
param_scale: "0.5B-3.2B"
slm: true
evidence: algorithm+simulation
topics: ["llm-adapters-lora", "noise-injection", "hardware-aware-training", "heterogeneous-analog-digital", "language-models", "read-write-noise", "stuck-at-faults", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 12
citations_overall: 4
priority_score: 9.92
doi: "https://doi.org/10.1145/3801559"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Wu_HaLoRA_TODAES.pdf"
fulltext: "../fulltext/2026_Wu_HaLoRA_TODAES.txt"
---

# HaLoRA

**Hardware-aware Low-Rank Adaptation for Large Language Models Based on Hybrid Compute-in-Memory Architecture** — ACM Transactions on Design Automation of Electronic Systems (2026)

## TL;DR
HaLoRA maps frozen pretrained LLM weights to noisy RRAM CIM and the LoRA branch to noise-free digital SRAM CIM, and trains the LoRA branch with a noise-trajectory-gap loss, recovering up to 22.7 average-score points at sigma=0.02 (LLaMA-3.2 1B: 63.1 vs 40.4) at about 3% of A100 energy.

## Summary
LoRA-finetuned LLMs have a distinctive split: the huge task-agnostic backbone (1235.8M params in LLaMA-3.2 1B) versus a tiny trainable LoRA branch (1.9M, ~0.15%). The paper places the backbone on dense, energy-efficient but noisy 1T1R RRAM analog CIM and the LoRA branches plus attention MatMul (dynamic, write-heavy) on 10T-SRAM digital CIM, with a SoftMax dynamic processor in the digital domain (Fig. 2-3). Because RRAM read noise corrupts the backbone, HaLoRA injects Gaussian noise into the frozen W0 during LoRA finetuning (resampled every 400 steps, sigma=0.01 in training, weights partitioned into 64x64 tiles) and adds a regularizer that minimizes a noise-agnostic upper bound on the gap between ideal and noisy LoRA optimization trajectories (mu=0.1). Experiments finetune Qwen2.5-0.5B and LLaMA-3.2 1B/3B (rank 4, 170k commonsense samples, q/k/v/up/down) and evaluate six commonsense benchmarks at sigma in {0.005,0.01,0.02} with five seeds, plus stuck-at faults. Hardware energy/area are estimated with XPEsim and published chip data for W8A8 with 8-bit ADC ENOB. HaLoRA consistently beats vanilla LoRA in accuracy and variance under noise; the hybrid design costs 18.1 mJ (1B) / 51.3 mJ (3B) for 512 tokens versus 550.5 / 1666.8 mJ on an A100.

## Language models evaluated
- Models: Qwen2.5-0.5B, LLaMA-3.2-1B, LLaMA-3.2-3B
- Scale: 0.5B-3.2B
- Note: LoRA-finetuned Qwen2.5-0.5B and LLaMA-3.2 1B/3B (SLM scale) evaluated with injected RRAM noise in simulation, with energy modeled for hybrid RRAM (analog CIM) + SRAM digital CIM versus A100 GPU.

## Contributions
- Framework deploying LoRA-finetuned LLMs on hybrid RRAM (backbone) + SRAM (LoRA, MatMul) CIM
- HaLoRA: noise-injected LoRA training plus a loss minimizing an upper bound on the ideal-vs-noisy LoRA trajectory gap
- Evaluation on Qwen2.5-0.5B and LLaMA-3.2 1B/3B over six commonsense tasks, multiple noise levels, noise types (Gaussian, SAF)
- Hardware simulation of energy and area vs A100, RRAM-only and SRAM-only deployments

## Key claims (stable IDs)
- **2026_Wu_HaLoRA_TODAES#C1** — HaLoRA surpasses LoRA by 22.7 average points at sigma=0.02 on LLaMA-3.2 1B — _support:_ 63.1 vs 40.4 avg — _loc:_ Sec. 1, Table 6
- **2026_Wu_HaLoRA_TODAES#C2** — Hybrid deployment costs ~3% of A100 energy — _support:_ 18.1 mJ vs 550.5 mJ (1B), 51.3 vs 1666.8 mJ (3B), 512 tokens — _loc:_ Table 6
- **2026_Wu_HaLoRA_TODAES#C3** — Hybrid area is ~10% of SRAM-only and 1.1% above RRAM-only (3B) — _support:_ 1.011x vs 10x — _loc:_ Table 6
- **2026_Wu_HaLoRA_TODAES#C4** — LoRA branch adds negligible energy — _support:_ 0.54% (1B) and 0.42% (3B) of block energy on SRAM; RRAM arrays 72.83%/78.66% — _loc:_ Fig. 7

## Results
- LLaMA-3.2 3B average at sigma 5e-3/1e-2/2e-2: HaLoRA 81.2/80.7/78.4 vs LoRA-on-RRAM 79.7/77.9/64.9 (Table 6)
- LLaMA-3.2 1B: HaLoRA 67.2/66.3/63.1 vs LoRA-on-RRAM 60.9/57.0/40.4 (Table 6)
- Noise sigma=0.02 lowers vanilla LoRA avg by 21.7 (1B) and 15.8 (3B) (Table 3)
- With SAF 0% HaLoRA beats LoRA on all six tasks, e.g. ARC-e 73.33 vs 67.06 (Fig. 6, Qwen2.5-0.5B)

## Key numbers
- array_size: 64x64 tiles (noise partition)
- energy_eff: 18.1 mJ / 512 tokens (LLaMA-3.2 1B), 51.3 mJ (3B)
- accuracy: 63.1 avg at sigma=0.02 (LLaMA-3.2 1B)
- bits_weight: 8b
- bits_adc: 8b ENOB

## Datasets / benchmarks
ARC-e, ARC-c, OBQA, SIQA, WinoGrande, PIQA

## Limitations
- Simulation only: noise is injected Gaussian / stuck-at, no fabricated hybrid chip
- Energy/area from XPEsim and reported chip data with simplifying assumptions (one weight per RRAM cell, 8-bit ADC ENOB, no GB-scale capacity solved)
- Noise assumed i.i.d. zero-mean Gaussian; no drift or IR-drop
- Models up to 3B only; commonsense reasoning tasks only

## Remarks
Algorithm+simulation paper; robustness numbers come from real finetuning runs with noise but hardware claims are projections. The split of static noisy backbone on analog NVM and a small, accurate adapter on digital SRAM is a practical pattern for mapping SLMs to crossbars and complements papers that harden the whole backbone. Claims the method can use measured chip noise signatures but does not demonstrate this.

## Cites (in collection, 12)
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _uses-method-or-tool_: "Additionally, following the block-wise linear mapping characteristics of weights on physical RRAM crossbars [50], we partitioned the corresponding weights into 64×64 blocks to align with conventional memory tile dimensions."
- [2022_Yang_FullCircuitMemristorTransformer_TCASI](2022_Yang_FullCircuitMemristorTransformer_TCASI.md) Full-Circuit Memristor Transformer (2022) — _motivation_: "For attention blocks, dynamic matrix-matrix multiplication (MatMul) necessitates extensive write-verify operations in RRAM [47, 48]."
- [2022_Krishnan_HybridRRAMSRAM_TCAD](2022_Krishnan_HybridRRAMSRAM_TCAD.md) Hybrid RRAM/SRAM IMC (2022) — _background_: "Existing work related to CIM has investigated the implementation of small-scale neural networks [1, 7, 8]."
- [2023_Sridharan_X-Former_TVLSI](2023_Sridharan_X-Former_TVLSI.md) X-Former (2023) — _background_: "In this paper, we propose deploying finetuned LLMs on hybrid CIM, leveraging both the energy efficiency and computational density of RRAM and the noise-free computation of SRAM [64, 65]."
- [2024_Wen_MemristorSRAMCIMFusion_Science](2024_Wen_MemristorSRAMCIMFusion_Science.md) Memristor-SRAM CIM Fusion (2024) — _background_: "These hybrid designs typically partition computational tasks based on the characteristics of each memory device: deploying high-precision, frequently updated operations on SRAM while allocating computation-intensive yet structurally simple operations to RRAM [1, 56]."
- [2023_Liu_HARDSEA_TVLSI](2023_Liu_HARDSEA_TVLSI.md) HARDSEA (2023) — _background_: "Among them, RRAM-SRAM hybrid architectures have attracted significant attention by combining the high energy efficiency of RRAM with accurate computation of SRAM [1, 54–56]."
- [2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature](2025_Khwa_MixedPrecisionMemristorSRAMCIM_Nature.md) Khwa Mixed-Precision Memristor-SRAM CIM (2025) — _background_: "Existing work related to CIM has investigated the implementation of small-scale neural networks [1, 7, 8]."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _motivation_: "While the RRAM-only strategy suffers from inherent noise and complex write-verify operations [40], the SRAM-only strategy is limited by its volatility and low storage density [41]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _motivation_: "While the RRAM-only strategy suffers from inherent noise and complex write-verify operations [40], the SRAM-only strategy is limited by its volatility and low storage density [41]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _data/numbers_: "For the analog RRAM macros, based on noise levels reported in published RRAM chip studies [51, 52], the standard deviation of the injected Gaussian noise can be set within the range of 0.01 to 0.02."
- [2025_Dhingra_Atleus_TCAD](2025_Dhingra_Atleus_TCAD.md) Atleus (2025) — _background_: "In this paper, we propose deploying finetuned LLMs on hybrid CIM, leveraging both the energy efficiency and computational density of RRAM and the noise-free computation of SRAM [64, 65]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "In practical CIM deployment, input-related errors are typically managed at the circuit or architecture level using techniques like dynamic range scaling or error-compensating ADCs [68]."

## Cited by (in collection, 2)
- [2026_Holla_ROSETTA_JETCAS](2026_Holla_ROSETTA_JETCAS.md) ROSETTA (2026)
- [2026_Sharma_HatFi_VTS](2026_Sharma_HatFi_VTS.md) HATFI (2026)

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Wu_HaLoRA_TODAES.pdf](../../11_Small_Language_Models_on_AIMC/2026_Wu_HaLoRA_TODAES.pdf)
- Full text: [../fulltext/2026_Wu_HaLoRA_TODAES.txt](../fulltext/2026_Wu_HaLoRA_TODAES.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3801559
