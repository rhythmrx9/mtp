---
id: W4386100686
key: 2023_Ambrogio_IBMAnalogAISpeechChip_Nature
title: "An analog-AI chip for energy-efficient speech recognition and transcription"
short: "IBM Analog-AI Speech Chip (RNNT)"
year: 2023
venue: "Nature"
venue_full: "Nature"
authors: "Stefano Ambrogio, Pritish Narayanan, Atsuya Okazaki, Andrea Fasoli, Charles Mackin, Kohji Hosokawa, Akiyo Nomura, T. Yasuda, A. Chen, Alexander M. Friz, Masatoshi Ishii, Jose Luquin et al."
category: "02 Fabricated Chips & Macros"
devices: ["PCM"]
models: ["LSTM/RNN", "MLP", "Speech"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "analog-mvm", "recurrent-models", "weight-mapping", "tiling-partitioning", "dataflow-pipelining", "conductance-drift", "energy-efficiency"]
analysis_basis: full-text
in_original_review: true
cited_by_in_collection: 15
cites_in_collection: 9
citations_overall: 239
priority_score: 12.37
doi: "https://doi.org/10.1038/s41586-023-06337-5"
pdf: "../../02_Fabricated_Chips_and_Macros/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.pdf"
fulltext: "../fulltext/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.txt"
---

# IBM Analog-AI Speech Chip (RNNT)

**An analog-AI chip for energy-efficient speech recognition and transcription** — Nature (2023)

## TL;DR
A 14nm chip with 34 PCM tiles (35M devices) and a parallel 2D-mesh duration-format fabric achieves software-equivalent end-to-end keyword spotting (86.14%) and near-SWeq MLPerf RNNT speech transcription (9.258% WER vs 7.452% SW baseline) across five chips with up to 12.4 TOPS/W.

## Summary
The chip has 34 analog tiles, each a 512x2048 PCM crossbar (four PCM per unit cell; 4-PCM or denser 2-PCM per weight), with analog peripheral capacitors for integration, duration-format (PWM) input/output via six input/output landing pads with SRAM, a circuit-switched 2D mesh with multicast for tile-to-tile transfer of 512-element vectors, ramp-based time-to-digital conversion, and per-tile local controllers. There are no on-chip digital cores; auxiliary ops (vector-vector products, activations, joint network) run off-chip on FPGAs/x86. Weights are programmed iteratively row-wise. KWS (fully-connected, hardware-aware trained with AIHWKit, pruned to 1,024 inputs) uses four tiles with an AB method (apply x on W then -x on -W) to cancel peripheral asymmetries; a frame takes 2.4 us. The MLPerf RNNT (45M weights; encoder LSTMs, decoder embedding+LSTMs, joint FC) is mapped without extra retraining across five chips (>140M PCM); a software quantization sensitivity analysis picks per-layer mapping, the joint-FC is kept digital, and a weight-expansion technique (insert random matrix M and pseudoinverse) improves SNR for the most sensitive layer (Enc-LSTM0). Power is measured per chip and system efficiency projected with synthesized 14nm digital pipelines.

## Contributions
- First demonstration of >140 analog-AI tiles combined with massively parallel inter-tile communication via a 2D mesh
- SWeq end-to-end KWS using fully analog set-up and AB method
- Near-SWeq MLPerf RNNT on 45M weights over 5 chips with layer-wise sensitivity-guided mapping
- Weight-expansion technique for noise-sensitive layers
- Measured power/TOPS-per-W and system-level projection

## Key claims (stable IDs)
- **2023_Ambrogio_IBMAnalogAISpeechChip_Nature#C1** — KWS reaches SWeq accuracy end-to-end on analog hardware — _support:_ 86.14% vs MLPerf iso-accuracy limit 85.88%; 2.4 us per frame; 7x faster than best prior case — _loc:_ Fig. 3g / Sec. KWS
- **2023_Ambrogio_IBMAnalogAISpeechChip_Nature#C2** — RNNT on five chips yields 9.475% WER with original weights and 9.258% with weight expansion — _support:_ SW baseline 7.452%; SWeq limit 8.378%; 98.1% of SW accuracy — _loc:_ Fig. 5b,f
- **2023_Ambrogio_IBMAnalogAISpeechChip_Nature#C3** — PCM drift for >1 week raises WER only to 9.894% (0.4% absolute) without recalibration — _support:_ 9.475 -> 9.894% — _loc:_ Fig. 5c
- **2023_Ambrogio_IBMAnalogAISpeechChip_Nature#C4** — Chip 4 sustains 12.4 TOPS/W; halving integration time gives 15.4 TOPS/W with ~1% extra WER — _support:_ Fig. 6a,b — _loc:_ Fig. 6
- **2023_Ambrogio_IBMAnalogAISpeechChip_Nature#C5** — System projection: 6.94 TOPS/W sustained; 546.6 samples/s/W (6.704 TOPS/W) at 3.57 W with weight expansion, 14x better than best MLPerf submission — _support:_ as stated; real-time factor 8e-5, 500 us per query — _loc:_ Fig. 6c-f

## Results
- 35M PCM / 34 tiles per chip; >140M PCM and 45M weights over 5 chips
- Peak analog-tile efficiency 20.0 TOPS/W falling to 6.94 TOPS/W sustained after communication, incomplete tile use and digital compute
- Analog:digital op ratio 325:1 (conventional) and 88:1 (weight expansion)
- Quantizing Enc-LSTM0 to 3.5 bits gives 42% WER; weight expansion reduces to 7.9% in simulation
- Communication error in 2D mesh never exceeds 5 ns (1M random durations)

## Key numbers
- tech_node: 14nm CMOS + PCM BEOL
- array_size: 512x2048 PCM per tile; 34 tiles
- energy_eff: 12.4 TOPS/W chip-sustained (chip 4); 6.94 TOPS/W projected system
- throughput: 2.1 us per RNNT chip step; 2.4 us per KWS frame
- accuracy: 9.258% WER Librispeech (RNNT); 86.14% KWS
- bits_weight: 2 or 4 PCM per weight
- bits_adc: UINT8 duration-format I/O

## Datasets / benchmarks
Librispeech, Google Speech Commands, MLPerf RNNT, MLPerf KWS

## Limitations
- No on-chip digital compute or SRAM for auxiliary ops; vector-vector products, activations and joint network done off-chip
- System-level energy/performance partly projected from simulated digital pipelines
- Weight expansion adds digital preprocessing and area
- RNNT is an LSTM transducer, not a transformer; attention needs digitization not demonstrated
- Chip-by-chip sequential evaluation; WER degradation of 1.8% vs software baseline

## Remarks
A landmark measured-silicon result showing multi-chip analog-AI at industrial model scale (45M weights), with practical techniques (sensitivity-based layer mapping, weight expansion, AB cancellation) transferable to transformers/SLMs. Its explicit remark that transformer attention requires digitization foreshadows later IBM work on LM mapping. Evidence is strong for FC/LSTM models but not for attention or KV caches; compare with HERMES core and Joshi PCM inference.

## Use in the original review
- F2 (High confidence): Analog CIM has moved past simulation to fabricated, measured multi-core silicon in both PCM and RRAM: IBM's 14 nm chip, IBM's 64-core HERMES chip, and NeuRRAM. HERMES's 400 GOPS/mm² in 4-phase mode is more than 15× higher than previous multi-core resistive-memory AIMC chips.
- F3 (High confidence): Measured on-chip accuracy is close to software but not free, and the penalty grows with model scale — from full software-equivalence on keyword spotting, to <1 pp on ResNet-9, to 1.8 pp on ALBERT/GLUE, to a missed equivalence threshold on a 45M-weight RNN-T.

## Cites (in collection, 9)
- [2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS](2018_Marinella_MultiscaleCoDesignReRAMTraining_JETCAS.md) Multiscale Co-Design ReRAM Training (2018) — _contrasts/critiques_: "However, several NVM compute-in-memory studies have focused on the macro-level32,34,39,40,41, without accounting for data transport, control or chip infrastructure (such as clocking) costs. They are also usually at a much smaller scale ... than the work here."
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "Analog in-memory computing (analog-AI)3–7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _uses-method-or-tool_: "To make the network more resilient to analog noise23–26, we retrained it while including weight and"
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Analog-AI HW avoids these inefficiencies by leveraging arrays of non-volatile memory (NVM) to perform the ‘multiply and accumulate computation’ (MAC) operations which dominate these workloads directly in the memory3–7."
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _uses-method-or-tool_: "To program PCM devices, a parallel programming scheme is used (Fig. 1f) so that all 512 weights in the same row are updated at the same time4."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _uses-method-or-tool_: "To make the network more resilient to analog noise23–26, we retrained it while including weight and"
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Analog in-memory computing (analog-AI)3–7 can provide better energy efficiency by performing matrix–vector multiplications in parallel on ‘memory tiles’."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022) — _background_: "Analog-AI HW avoids these inefficiencies by leveraging arrays of non-volatile memory (NVM) to perform the ‘multiply and accumulate computation’ (MAC) operations which dominate these workloads directly in the memory3–7."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _extends/builds-on_: "A highly heterogeneous and programmable accelerator architecture for analog AI has been introduced20 for which system-level performance assessments have predicted energy efficiencies 40–140 times higher than those of cutting-edge graphics processing units."

## Cited by (in collection, 15)
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "AIMC accelerators that are based on resistive memory device technologies such as Phase Change Memory (PCM)5–8 , Resistive Random Access Memory (ReRAM)9–12 , and Magnetic Random Access Memory (MRAM)13 , have shown great promise in accelerating and reducing the power consumption of deep learning systems."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci](2025_Buchel_MoE3DAnalogInMemoryComputing_NatCompSci.md) MoE on 3D AIMC (2025) — _background_: "Notable progress has already been made in addressing these issues through large-scale demonstrations of 2D AIMC architectures22,23, and these solutions are expected to be applicable to 3D AIMC as well."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _background_: "IBM recently demonstrated two chips and one architectural extension using PCM-base AIMC on 14nm CMOS [12], [13], [19], as summarized in Table I."
- [2025_Leroux_GainCellAnalogAttention_NatCompSci](2025_Leroux_GainCellAnalogAttention_NatCompSci.md) Gain-Cell Analog Attention (2025) — _background_: "To mitigate this issue, charge-based integration is an energy-efficient alternative35,36."
- [2025_Martemucci_FeCapMemristorHM_NatElectron](2025_Martemucci_FeCapMemristorHM_NatElectron.md) FeCAP-Memristor Hybrid Memory (2025) — _background_: "In addition, memristor-based architectures can leverage in-memory computing to minimize data movement to greatly reduce energy consumption 1,2,5–10."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _baseline/comparison_: "The prior work on the demonstration of the Recurrent Neural Network Transducer (RNNT) model in this analog accelerator achieved the efficiency of 6-7 TOPS/W, a 14 × improvement over conventional digital accelerators8."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "In some scenarios involving simple activation functions such as ReLU, the generated time pulse can be clipped and consumed downstream as the pulse-width input for the next NN layer, avoiding the intermediate analogue-to-digital and digital-to-time steps entirely33,72."
- [2026_Jiang_HighAccuracyMemristorCIM_NatMater](2026_Jiang_HighAccuracyMemristorCIM_NatMater.md) High-Accuracy Memristor CIM Review (2026) — _data/numbers_: "Matrix expansion13 introduces redundancy by expanding a small weight matrix into a larger one, reducing the word error rate from 42 to 7.9% on LibriSpeech with MLPerF RNNT13."
- [2026_Vasilopoulos_AIMCforLLMInference_IMW](2026_Vasilopoulos_AIMCforLLMInference_IMW.md) AIMC for LLM Inference (IMW 2026) (2026) — _background_: "A wide range of devices have been explored for AIMC, including phasechange memory (PCM) [13], [14], resistive random-access memory (RRAM) [15], magnetoresistive random-access memory (MRAM) [16], and Flash [17], [18], showing promising results in terms of compute density and efficiency."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _data/numbers_: "Recently, a large Recurrent Neural Network Tranducer (RNNT) model (Fig. 4a) was demonstrated [19], using 5 chips to encode 45M weights using >140M PCM devices."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _data/numbers_: "Recently, a large Recurrent Neural Network Tranducer (RNNT) model (Fig. 2a) was demonstrated [28], using 5 chips to encode 45M weights using >140M PCM devices."
- [2025_Buchel_AnalogFoundationModels_NeurIPS](2025_Buchel_AnalogFoundationModels_NeurIPS.md) Analog Foundation Models (2025) — _background_: "In order to store larger neural networks fully on-chip, a more scalable memory technology must be used, which is why researchers explored AIMC with dense Non-Volatile Memory (NVM) such as embedded flash [18], Phase Change Memory (PCM) [19, 20], ReRAM [21, 22], or MRAM [23]."
- [2024_Boybat_HeterogeneousPCMAimcNPU_IEDM](2024_Boybat_HeterogeneousPCMAimcNPU_IEDM.md) Heterogeneous PCM-AIMC NPU (2024)
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.pdf](../../02_Fabricated_Chips_and_Macros/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.pdf)
- Full text: [../fulltext/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.txt](../fulltext/2023_Ambrogio_IBMAnalogAISpeechChip_Nature.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1038/s41586-023-06337-5
