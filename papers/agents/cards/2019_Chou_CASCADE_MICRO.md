---
id: W2979663695
key: 2019_Chou_CASCADE_MICRO
title: "CASCADE"
short: "CASCADE"
year: 2019
venue: "MICRO"
venue_full: "ACM/IEEE 52nd Annual International Symposium on Microarchitecture (MICRO 2019)"
authors: "Teyuh Chou, Wei Tang, Jacob Botimer, Zhengya Zhang"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["CNN", "LSTM/RNN", "MLP", "VGG", "ResNet"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "adc-dac", "peripheral-circuits", "weight-mapping", "dataflow-pipelining", "energy-efficiency", "recurrent-models", "analog-mvm"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 15
cites_in_collection: 8
citations_overall: 89
priority_score: 7.97
doi: "https://doi.org/10.1145/3352460.3358328"
pdf: "../../03_Crossbar_Accelerator_Architectures/2019_Chou_CASCADE_MICRO.pdf"
fulltext: "../fulltext/2019_Chou_CASCADE_MICRO.txt"
---

# CASCADE

**CASCADE** — ACM/IEEE 52nd Annual International Symposium on Microarchitecture (MICRO 2019) (2019)

## TL;DR
CASCADE cascades MAC RRAM arrays into buffer RRAM arrays through TIAs so partial sums are buffered and accumulated in analog (R-Mapping), cutting A/D conversions from 256 to 10 per 16 cycles and giving 3.5x lower energy than an ADC-based and 11.0x lower than an SA-based in-RRAM design at competitive throughput.

## Summary
The paper argues that in-RRAM computation is limited by multi-bit A/D conversion (ISAAC's 8-bit ADCs are estimated at 58% of power and 31% of area) and by digital accumulation of the many partial sums produced when large layers (e.g. 9,216 accumulations for AlexNet FC) are split across 64x64 to 256x256 crossbars with bit-sliced weights and bit-serial inputs. CASCADE uses 64x64 MAC RRAM arrays with 1-bit cells, 1 input bit per cycle and a 6-bit bit-line resolution chosen for noise tolerance (6-bit BL needs ~25 dB SNR versus ~35 dB for a PipeLayer-like 11-bit BL at 90% MLP accuracy). Transimpedance amplifiers (TIAs) convert BL currents to voltages that directly drive buffer RRAM arrays; the R-Mapping scheme stores analog partial sums in a buffer RRAM (15 rows by 30 columns per MAC subsection) so accumulation happens in memory, and the 30 BLs are grouped so low-order groups are summed in analog summing amplifiers and fed as carry-in to the MSB group, leaving 10 ADC conversions (6 to 10 bit) at the very end. Evaluation is simulation: 65 nm CMOS and 65 nm RRAM model, ISAAC component models scaled, 80 APU blocks each with 80 64x64 arrays, 32 TIAs per array and 7 shared ADCs (3.2 MB weight capacity, 25.6 GB/s DDR4 I/O), against ADC-based (ISAAC-like) and SA-based (PRIME-like) references on 10 DNNs and 1 RNN (AlexNet, VGG-A/B/C, MSRA-A/B/C, GoogLeNet, ResNet, DeepFace, NeuralTalk).

## Contributions
- Low-resolution (6-bit) BL design chosen for variation/noise tolerance with a quantified resolution vs SNR trade-off
- R-Mapping scheme that performs partial-sum accumulation inside buffer RRAM arrays
- Analog summation of low-order bit groups to bypass A/D conversion, reducing conversions from 256 to 10 per 16 cycles
- TIA interface cascading MAC to buffer arrays, supporting DNN, RNN (LSTM) and SNN

## Key claims (stable IDs)
- **2019_Chou_CASCADE_MICRO#C1** — CASCADE reduces energy versus ADC- and SA-based in-RRAM architectures — _support:_ average 3.5x lower than ADC-based, 11.0x lower than SA-based — _loc:_ Sec. 4.3 / Fig. 11a
- **2019_Chou_CASCADE_MICRO#C2** — Throughput is competitive or better — _support:_ 1.86x vs ADC-based, 17.83x vs SA-based — _loc:_ Sec. 4.3 / Fig. 11b
- **2019_Chou_CASCADE_MICRO#C3** — The TIA interface is far cheaper than ADC/SA interfaces — _support:_ 77.5x lower energy than ADC interface, 325.4x than SA interface — _loc:_ Sec. 4.3 / Fig. 12
- **2019_Chou_CASCADE_MICRO#C4** — Lower BL resolution gives more noise margin at equal accuracy — _support:_ 90% MLP accuracy needs 25 dB SNR (6-bit BL) vs 35 dB (11-bit BL, PipeLayer config) — _loc:_ Sec. 3.5 / Fig. 9

## Results
- 3.5x energy reduction vs ADC-based, 11.0x vs SA-based (average over 11 benchmarks, Fig. 11a)
- 1.86x / 17.83x throughput vs ADC-based / SA-based (Fig. 11b)
- A/D conversions reduced from 256 per 16 cycles to 10 per 16 cycles (Sec. 4.1)
- Peak computation density ~101 GOPs/s/mm2 reported for H64-T32-A7 R80 config (Fig. 10, number partially extracted)
- TIA interface energy 77.5x lower than ADC interface

## Key numbers
- tech_node: 65nm
- array_size: 64x64
- energy_eff: 3.5x vs ADC-based baseline
- throughput: 1.86x vs ADC-based
- bits_weight: 1b cells, 16b weights
- bits_adc: 6-10b (10 conversions); 6b BL

## Datasets / benchmarks
ImageNet, AlexNet, VGG-A/B/C, MSRA-A/B/C, GoogLeNet, ResNet, DeepFace, NeuralTalk

## Limitations
- Simulation/analytical only with scaled component models; no fabricated chip
- Noise tolerance analysed via lumped BL SNR and a 2-layer MLP, not full-network device-variation Monte Carlo
- 1-bit RRAM cells and 64x64 arrays increase array count and weight replication overhead
- CNN/RNN workloads only; no attention or language models
- Reference architectures re-implemented under equal assumptions, may differ from published designs

## Remarks
CASCADE is an influential idea for reducing the ADC and digital-accumulation tax by staying in the analog domain, a theme revisited by later hybrid analog/digital designs (BRAHMS, TIMELY, Neural-PIM). Its low-bit-per-cell, low-BL-resolution stance aligns with how silicon macros are actually built, but evidence is simulated. The partial-sum problem it addresses grows for LLM-sized matrices, so it is conceptually relevant to mapping SLM weights, though attention's dynamic operands are not handled.

## Cites (in collection, 8)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "2.2 In-RRAM Computation ISAAC [38], PRIME [12] and PipeLayer [41] are three recently published architectures for implementing DNN and RNN through in-RRAM computation."
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018) — _uses-method-or-tool_: "Our evaluations were done using a 65nm technology and a 65nm RRAM model from [8]."
- [2019_Xue_1MbMultibitReRAMCIM_ISSCC](2019_Xue_1MbMultibitReRAMCIM_ISSCC.md) 1Mb Multibit ReRAM CIM Macro (2019) — _background_: "The latest PIM chips, including the ones based on SRAM [3, 14, 47] and the ones based on RRAM [45], chose to digitize only the most significant bits (MSBs) to reduce the cost of A/D conversion."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _baseline/comparison_: "PRIME [12] uses sense amplifiers (SAs) instead of conventional ADCs to reduce area."
- [2015_Burr_PCM165kSynapseNetwork_TED](2015_Burr_PCM165kSynapseNetwork_TED.md) PCM 165k-Synapse Network (2015) — _background_: "The simple and elegant in-RRAM dot product has been projected to achieve impressive performance and efficiency [5, 11, 21, 26, 29, 35]."
- [2015_Prezioso_MemristorPerceptron_Nature](2015_Prezioso_MemristorPerceptron_Nature.md) Prezioso Memristor Perceptron (2015)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)

## Cited by (in collection, 15)
- [2020_Li_TIMELY_ISCA](2020_Li_TIMELY_ISCA.md) TIMELY (2020) — _contrasts/critiques_: "Although a recent R2 PIM accelerator, CASCADE [15], has adopted analog buffers, it only uses analog ReRAM buffer to reduce the number of A/D conversions, thereby minimizing computational energy."
- [2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE](2023_Smagulova_ResistiveNeuralHardwareAccelerators_ProcIEEE.md) Resistive Neural Hardware Accelerators (2023) — _data/numbers_: "The CASCADE architecture implemented an analog partial sum accumulation and achieved a peak performance of 101 GOPS/mm2 [38]."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _contrasts/critiques_: "Recent work has optimized the performance and energy of bit-sliced accelerators [6, 14, 42, 49], but rarely evaluates the effect of system-level design decisions on inference accuracy."
- [2021_Cao_NeuralPIM_TC](2021_Cao_NeuralPIM_TC.md) Neural-PIM (2021) — _baseline/comparison_: "Strategy B (Fig. 3(b)) buffers analog partial sums from all input cycles before the quantization, capturing the scheme adopted by CASCADE [2]."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _background_: "ReRAM crossbar is emerging as a promising solution to mitigate problems such as memory wall, owing to its high memory accessing bandwidth and high density [4, 6, 9, 10, 19–23]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _contrasts/critiques_: "Alternatively, other designs use efficient lower-resolution ADCs to process high-resolution analog values from crossbars [5, 7, 24]."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _extends/builds-on_: "CASCADE [8] exploits TIAs to convert accumulated currents into write voltages, which then are applied to cascaded buffer arrays for multiply-and-add operations."
- [2021_Song_BRAHMS_DAC](2021_Song_BRAHMS_DAC.md) BRAHMS (2021)
- [2022_Liu_IVQ_TCAD](2022_Liu_IVQ_TCAD.md) IVQ (2022)
- [2023_Liu_ERABS_TC](2023_Liu_ERABS_TC.md) ERA-BS (2023)
- [2024_Xu_ReHarvest_TACO](2024_Xu_ReHarvest_TACO.md) ReHarvest (2024)
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024)
- [2024_Zhao_LightCIM_TCAD](2024_Zhao_LightCIM_TCAD.md) Light-CIM (2024)
- [2024_Gu_VariationTolerantOUFramework_TCASI](2024_Gu_VariationTolerantOUFramework_TCASI.md) Variation-Tolerant OU Framework (2024)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2019_Chou_CASCADE_MICRO.pdf](../../03_Crossbar_Accelerator_Architectures/2019_Chou_CASCADE_MICRO.pdf)
- Full text: [../fulltext/2019_Chou_CASCADE_MICRO.txt](../fulltext/2019_Chou_CASCADE_MICRO.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1145/3352460.3358328
