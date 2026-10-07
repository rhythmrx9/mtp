---
id: W4403534421
key: 2024_Wang_LLMOnMemristorCrossbar_TPAMI
title: "Enabling Energy-Efficient Deployment of Large Language Models on Memristor Crossbar: A Synergy of Large and Small"
short: "LLM-on-Memristor-Crossbar"
year: 2024
venue: "TPAMI"
venue_full: "IEEE Transactions on Pattern Analysis and Machine Intelligence (2024)"
authors: "Zhehui Wang, Tao Luo, Cheng Liu, Weichen Liu, Rick Siow Mong Goh, Weng‐Fai Wong"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["BERT", "Transformer", "GPT/LLM", "ResNet"]
lm_models: ["BERT-Base", "BERT-Large", "Phi-1.5", "GPT-2", "T5 (hardware eval)", "LLaMa (hardware eval)", "GPT-3 (area projection)"]
param_scale: "110M-1.3B accuracy-tested; up to 175B (projection)"
slm: true
evidence: simulation
topics: ["language-models", "transformer-accelerator", "attention", "nonlinear-functions", "crossbar-architecture", "energy-efficiency", "heterogeneous-analog-digital", "weight-mapping"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 11
priority_score: 8.76
doi: "https://doi.org/10.1109/tpami.2024.3483654"
pdf: "../../11_Small_Language_Models_on_AIMC/2024_Wang_LLMOnMemristorCrossbar_TPAMI.pdf"
fulltext: "../fulltext/2024_Wang_LLMOnMemristorCrossbar_TPAMI.txt"
---

# LLM-on-Memristor-Crossbar

**Enabling Energy-Efficient Deployment of Large Language Models on Memristor Crossbar: A Synergy of Large and Small** — IEEE Transactions on Pattern Analysis and Machine Intelligence (2024) (2024)

## TL;DR
A two-crossbar architecture (small resistor-based computation crossbars plus large dense memory-style RRAM crossbars) decomposes all LLM operations into one standard sub-operation, giving up to 39x area and 18x energy savings over conventional memristor crossbars and >=68x lower area-delay product than TPU/GPU on BERT-Large with negligible GLUE accuracy loss.

## Summary
The paper targets three obstacles to running LLMs on memristor crossbars: model size beyond chip capacity (GPT-3 would need 2777 ISAAC chips), non-weight-stationary products in attention (Q x K, scores x V), and nonlinear ops (softmax, LayerNorm). Key idea: decompose every LLM operation (linear, attention, softmax, LayerNorm) into a standardized sub-operation executed by a reconfigurable 'computation crossbar' built from resistors (with a digit-wise encoding using multiple memristors per activation and low-resolution 1-bit DAC/2-bit ADC), while weights and intermediates live in 'dense crossbars' of DRAM-bank size (1k x 64k) used like memory. A digital function unit F and encoder/registers handle the rest. Evaluation: accuracy via PyTorch/Hugging Face with random-telegraph-noise fluctuation and quantization (8-bit weights/activations) on GLUE for BERT-Base/Large and on Phi-1.5 and GPT-2 benchmarks; area/energy/latency via ISAAC/PRIME/PipeLayer-style simulators at 32nm with CACTI and EDA-synthesized digital blocks, comparing with PRIME, ISAAC, PipeLayer, Vesti, TPUv4 and A100.

## Language models evaluated
- Models: BERT-Base, BERT-Large, Phi-1.5, GPT-2, T5 (hardware eval), LLaMa (hardware eval), GPT-3 (area projection)
- Scale: 110M-1.3B accuracy-tested; up to 175B (projection)
- Note: BERT-Base/Large, Phi-1.5 and GPT-2 evaluated with simulated memristor crossbar noise and 32 nm area/energy models, with GPT-3 (175B) only as an area-scaling projection.

## Contributions
- Fits an entire LLM on a single chip/package via dense RRAM crossbars
- Supports non-weight-stationary multiplication in multi-head attention
- Decomposes all LLM operations (incl. softmax, LayerNorm) into standardized sub-operations
- Robust resistor-based computation crossbar with 1-bit DAC/2-bit ADC and digit encoding
- Evaluation on BERT, Phi-1.5, GPT-2 accuracy and area/energy vs conventional memristor crossbars and TPU/GPU

## Key claims (stable IDs)
- **2024_Wang_LLMOnMemristorCrossbar_TPAMI#C1** — Up to 6x/39x area saving vs multi-bit/single-bit memristor crossbars and 18x/3x energy saving — _support:_ area 6x and 39x; energy 18x and 3x — _loc:_ Sec. 6 / Fig. 12
- **2024_Wang_LLMOnMemristorCrossbar_TPAMI#C2** — >=68x lower area-delay product and 69% lower energy than TPU/GPU on BERT-Large — _support:_ ADP 2.24 (TPU), 2.04 (GPU), 0.03 (ours) mm2.s — _loc:_ Table 10
- **2024_Wang_LLMOnMemristorCrossbar_TPAMI#C3** — Negligible accuracy loss on GLUE under <5% environmental noise — _support:_ BERT-Base baseline vs ours e.g. CoLA 58.03 vs 59.07, SST-2 93.00 vs 93.12; BERT-Large 62.63 vs 62.43 — _loc:_ Table 8
- **2024_Wang_LLMOnMemristorCrossbar_TPAMI#C4** — Tolerates 5x noise amplitude (and up to 18x with 1-bit cells) without accuracy change — _support:_ stated — _loc:_ Sec. 6.3 robustness text
- **2024_Wang_LLMOnMemristorCrossbar_TPAMI#C5** — 4-bit RRAM at 14nm could hold GPT-3's 175B parameters in 274 mm2 of cells vs 1646 mm2 DRAM, 27440 mm2 SRAM — _support:_ area arithmetic — _loc:_ Sec. 1

## Results
- Phi-1.5 vs baseline (3-cycle): WinoGrande 0.729->0.717, ARC-Easy 0.762->0.756, ARC-Challenge 0.445->0.451, PIQA 0.766->0.755, MMLU 0.418->0.394 (Table 9)
- GPT-2: WinoGrande 0.516->0.51, ARC-Easy 0.438->0.406
- Vs TPU/GPU on BERT-Large: ADP 0.03 vs 2.24/2.04 mm2.s
- Dense crossbar 1k x 64k; computation crossbars 128x128; ADC shared across 128 columns

## Key numbers
- tech_node: 32nm (14nm for density estimate)
- array_size: 128x128 computation; 1k x 64k dense
- energy_eff: 18x energy vs multi-bit crossbar; 69% lower energy vs TPU/GPU
- accuracy: BERT-Base GLUE within ~1.5 pts of baseline; Phi-1.5 MMLU 0.418->0.394
- bits_weight: 8b (INT8)
- bits_adc: 2b ADC, 1b DAC

## Datasets / benchmarks
GLUE, WinoGrande, ARC-Easy, ARC-Challenge, PIQA, HellaSwag, MMLU

## Limitations
- Entirely simulated; analytic area/energy from ISAAC-style models, no silicon
- Noise modeled as random-telegraph fluctuation with <5% amplitude; no drift, IR drop, or stuck-at faults
- Digital function unit F and registers/caches still required; its energy sensitivity not fully explored
- Accuracy evaluated only on BERT, Phi-1.5, GPT-2; larger models only in area projection
- Fine-tuning/QAT assumed; resistance ranges tuned per architecture to equalize accuracy

## Remarks
One of the few papers that explicitly confronts attention and nonlinear ops on memristor crossbars with an SLM-scale evaluation (BERT, Phi-1.5, GPT-2). The area/energy claims rest on analytical comparisons against older architectures (ISAAC, PRIME), so gains over modern digital accelerators should be read cautiously. Complements noise-focused work such as batchnorm-optimization and GENIEx-style non-ideality emulation.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _uses-method-or-tool_: "We follow the evaluation methodology employed in three highly cited works: PRIME [22], ISAAC [9], and PipeLayer [23]."
- [2018_Feinberg_DataAwareABNCodes_HPCA](2018_Feinberg_DataAwareABNCodes_HPCA.md) Data-aware AN codes (Feinberg) (2018) — _data/numbers_: "Simulation results show that the environmental noise contributes less than 5% to the signal level, which is typical for real devices [44]."
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018) — _background_: "Another design is the single-bit memristor, where we need multiple memristors to store a single weight. Examples are [20, 21]."
- [2020_Chakraborty_GENIEx_DAC](2020_Chakraborty_GENIEx_DAC.md) GENIEx (2020) — _motivation_: "However, this is challenging due to the accumulation of noise from the non-ideal behavior of memristors [45][46][47]."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "Memristor crossbars are widely considered strong competitors for traditional machine learning accelerators [3]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _motivation_: "For instance, the GPT-3 model has over 175 billion parameters, and it would require 2777 ISAAC chips [9] to store all of its parameters."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _contrasts/critiques_: "While the PRIME [22] and PipeLayer [23] approaches eliminate the need for ADCs, their input or output circuits still contain numerous capacitors, which consume a significant amount of chip area."
- [2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI](2023_Bhattacharjee_BatchnormFinetuningIMCNoise_GLSVLSI.md) BN-Finetune-IMC (2023) — _motivation_: "However, this is challenging due to the accumulation of noise from the non-ideal behavior of memristors [45][46][47]."
- [2019_Zhu_MultiPrecisionRRAMCNN_DAC](2019_Zhu_MultiPrecisionRRAMCNN_DAC.md) Multi-Precision Single-Bit RRAM (2019) — _baseline/comparison_: "In contrast, the single-bit architecture enhances memristor robustness by storing only onebit information, allowing for higher resistance levels and lower energy consumption [20]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2024_Wang_LLMOnMemristorCrossbar_TPAMI.pdf](../../11_Small_Language_Models_on_AIMC/2024_Wang_LLMOnMemristorCrossbar_TPAMI.pdf)
- Full text: [../fulltext/2024_Wang_LLMOnMemristorCrossbar_TPAMI.txt](../fulltext/2024_Wang_LLMOnMemristorCrossbar_TPAMI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tpami.2024.3483654
