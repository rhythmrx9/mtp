---
id: W3111989171
key: 2020_Shin_TOPAR_ICCAD
title: "A thermal-aware optimization framework for ReRAM-based deep neural network acceleration"
short: "TOPAR"
year: 2020
venue: "ICCAD"
venue_full: "39th IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2020)"
authors: "Hyein Shin, Myeonggu Kang, Lee‐Sup Kim"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG", "LSTM/RNN", "Other"]
lm_models: ["2-layer stacked LSTM (256 neurons) on WikiText-2"]
param_scale: "<1M (toy LSTM LM)"
slm: false
evidence: simulation
topics: ["thermal", "endurance-retention", "conductance-drift", "calibration-compensation", "weight-mapping", "bit-slicing", "peripheral-circuits"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 3
cites_in_collection: 5
citations_overall: 23
priority_score: 5.27
doi: "https://doi.org/10.1145/3400302.3415665"
pdf: "../../06_Nonidealities_and_Reliability/2020_Shin_TOPAR_ICCAD.pdf"
fulltext: "../fulltext/2020_Shin_TOPAR_ICCAD.txt"
---

# TOPAR

**A thermal-aware optimization framework for ReRAM-based deep neural network acceleration** — 39th IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2020) (2020)

## TL;DR
TOPAR lowers ReRAM accelerator temperature through offline weight decomposition, column reordering and weight adjustment (up to 2.39x endurance) and compensates temperature-induced conductance change online with current-mirror gain (<1% accuracy loss on 2-bit cells).

## Summary
ReRAM endurance drops to 0.026x between 300K and 380K and conductance is temperature-sensitive, so hot arrays hurt lifetime and accuracy; array power is proportional to the sum of cell conductances. Prior work either maps big weights to cold cells with periodic rewrites (not scalable, harms endurance) or downgrades bit width (HR3AM), which fails on realistic 1-4 bit cells because LSB errors are amplified by shift-and-add. TOPAR has three offline steps on the conventional positive/negative-array ISAAC-like design: (1) thermal-aware weight decomposition chooses, among equivalent positive/negative and multi-cell decompositions of each weight, the one minimising conductance sum (power); (2) thermal-aware column reordering balances load between arrays using a small 4:4 router and registers, with limited reordering range so there is no performance loss; (3) fine-grained weight adjustment. Online, a thermal sensor network feeds a temperature decoder that selects a current-mirror multiplier (1.0x to 2.0x in 0.1 steps) applied in the analog domain after analog subtraction of the positive/negative arrays, one compensator per array pair. Evaluation: 2-bit cells, 64x64 arrays, 8-bit ADC/1-bit DAC, 1.2 GHz, HotSpot thermal simulation at 300K ambient, 8-bit weights/inputs, five models (ResNet18/50, VGG16 on ImageNet; 2-layer LSTM-256 on WikiText-2; NCF on MovieLens) in a PyTorch bit-level simulator that perturbs conductance with temperature; endurance model 4.14e8 writes at 300K with lifetime set by first failure at peak temperature.

## Language models evaluated
- Models: 2-layer stacked LSTM (256 neurons) on WikiText-2
- Scale: <1M (toy LSTM LM)

## Contributions
- TOPAR: offline plus online thermal optimisation targeting both endurance and accuracy
- Three-stage offline optimisation: thermal-aware weight decomposition, column reordering, fine-grained weight adjustment
- Current-mirror analog error compensation usable on low-resolution (1-4 bit) cells and large DNNs
- Evaluation on five DNNs including an LSTM and a recommender, with overhead analysis

## Key claims (stable IDs)
- **2020_Shin_TOPAR_ICCAD#C1** — Offline optimisation lowers average array temperature — _support:_ 3.9K-7.4K reduction (TOPAR-I vs baseline) — _loc:_ Sec. 4.2 / Fig. 8(a)
- **2020_Shin_TOPAR_ICCAD#C2** — Temperature variance between arrays reduced — _support:_ 34.9%-52.1% reduction — _loc:_ Sec. 4.2 / Fig. 8(b)
- **2020_Shin_TOPAR_ICCAD#C3** — Endurance improves up to 2.39x — _support:_ 1.53x-2.39x across five benchmarks (2-bit cells) — _loc:_ Sec. 4.3 / Fig. 9
- **2020_Shin_TOPAR_ICCAD#C4** — Accuracy within 1% of the 300K result, unlike bit-width downgrading (HR3AM) — _support:_ <1% degradation for all benchmarks — _loc:_ Sec. 4.4 / Table 2

## Results
- Average temperature drops 3.9K-7.4K vs baseline across five networks (Fig. 8a)
- Endurance 1.53x-2.39x; for ResNet50 with 1-4 bit cells 1.38x-1.73x (Figs. 9, 10b)
- <1% top-1/perplexity/hit-ratio degradation with full TOPAR; TOPAR without offline optimisation 'reasonable but not original accuracy' (Table 2)
- Column-reordering hardware: 0.012% area, 0.021% power of accelerator (65nm scaled to 32nm) (Sec. 4.6)

## Key numbers
- tech_node: 32nm (overheads scaled from 65nm)
- array_size: 64x64
- accuracy: <1% degradation vs 300K baseline
- bits_weight: 8b weights on 2b cells
- bits_adc: 8b (1b DAC)

## Datasets / benchmarks
ImageNet, WikiText-2, MovieLens

## Limitations
- Simulation only (HotSpot + bit-level PyTorch simulator), no fabricated hardware
- Requires on-array thermal sensors and analog compensation circuitry; compensation range limited to 1x-2x
- Models are CNNs, a tiny LSTM and NCF; no transformers
- Temperature-conductance model abstracted from literature; weight decomposition choice assumes dual-array (positive/negative) design

## Remarks
One of few works that treat thermal behaviour as a first-class ReRAM non-ideality and jointly optimise lifetime and accuracy; the analog-domain compensation argument (digital correction after ADC is too late) is notable. Its LSTM/WikiText-2 case is the only language-model result and is tiny; temperature drift is relevant for dense LM crossbars at high utilisation but is not studied there. Followed up by WRAP in the collection.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _uses-method-or-tool_: "In the ReRAM-based DNN accelerator, weights of DNNs are allocated into ReRAM arrays as stated in [11]."
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _uses-method-or-tool_: "We evaluate TOPAR, a thermal-aware optimization framework, based on the practical configuration of ReRAM-based DNN accelerator with 2bit cell resolution and 64x64 array size [2, 12]."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _motivation_: "Furthermore, according to our observation, the thermal problems get more severe in ReRAM with low cell resolution (1-4bit), which is regarded as a realistic ReRAM compared to ideal ReRAM with high cell resolution (7-8bit) [2, 3, 11, 18]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The resolution of ADC and DAC is set as 8bit and 1bit by following the result from [2]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "Among various platforms of PIM, ReRAM is widely regarded as a proper platform for PIM with its intrinsic characteristic of matrix-vector multiplication [2, 11, 18]."

## Cited by (in collection, 3)
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023)
- [2022_Chen_WRAP_DATE](2022_Chen_WRAP_DATE.md) WRAP (2022)
- [2022_Shin_FaultFree_TC](2022_Shin_FaultFree_TC.md) Fault-Free (2022)

## Files
- PDF: [../../06_Nonidealities_and_Reliability/2020_Shin_TOPAR_ICCAD.pdf](../../06_Nonidealities_and_Reliability/2020_Shin_TOPAR_ICCAD.pdf)
- Full text: [../fulltext/2020_Shin_TOPAR_ICCAD.txt](../fulltext/2020_Shin_TOPAR_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3400302.3415665
