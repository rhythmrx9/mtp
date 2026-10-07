---
id: W3195245399
key: 2021_Narayanan_FullyOnChipMAC14nmPCM_TED
title: "Fully On-Chip MAC at 14 nm Enabled by Accurate Row-Wise Programming of PCM-Based Weights and Parallel Vector-Transport in Duration-Format"
short: "IBM 14nm PCM Analog AI Chip"
year: 2021
venue: "TED"
venue_full: "IEEE Transactions on Electron Devices, vol. 68, no. 12 (2021)"
authors: "Pritish Narayanan, Stefano Ambrogio, Atsuya Okazaki, Kohji Hosokawa, Hsinyu Tsai, Akiyo Nomura, T. Yasuda, Charles Mackin, Scott C. Lewis, Alexander M. Friz, Masatoshi Ishii, Yasuteru Kohda et al."
category: "02 Fabricated Chips & Macros"
devices: ["PCM"]
models: ["MLP", "LSTM/RNN"]
lm_models: ["1-layer LSTM (hidden 128) char-level on Alice in Wonderland"]
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "macro", "write-verify-programming", "analog-mvm", "adc-dac", "device-variation", "conductance-drift", "recurrent-models"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 22
cites_in_collection: 5
citations_overall: 85
priority_score: 10.03
doi: "https://doi.org/10.1109/ted.2021.3115993"
pdf: "../../02_Fabricated_Chips_and_Macros/2021_Narayanan_FullyOnChipMAC14nmPCM_TED.pdf"
fulltext: "../fulltext/2021_Narayanan_FullyOnChipMAC14nmPCM_TED.txt"
---

# IBM 14nm PCM Analog AI Chip

**Fully On-Chip MAC at 14 nm Enabled by Accurate Row-Wise Programming of PCM-Based Weights and Parallel Vector-Transport in Duration-Format** — IEEE Transactions on Electron Devices, vol. 68, no. 12 (2021) (2021)

## TL;DR
IBM's 14 nm all-analog PCM inference test chip with 512x512-weight tiles (4 PCMs per weight), ADC-free duration-format 2-D mesh and row-wise closed-loop tuning reaching <3% weight error, running a fully on-chip two-layer MNIST net (97.13% vs 97.73% software) and an LSTM stable over 10,000 characters.

## Summary
The paper addresses what is needed to build large analog-NVM inference systems: large high-yield arrays, accurate MACs, reconfigurable routing and scalable weight programming. The chip contains PCM tiles, each storing 512x512 weights, where each weight uses four GST mushroom-cell PCM conductances (G+, G-, g+, g-) integrated above foundry 14 nm CMOS. Activations are pulse-width (duration) encoded and routed tile-to-tile on a reconfigurable parallel 2-D mesh; there are no ADCs, instead column capacitors integrate current and a common ramp plus per-column comparators convert voltage back to duration, which also implements bounded ReLU/hard-sigmoid/hard-tanh. Weights are programmed by a row-wise closed-loop tuning (CLT) algorithm: voltage-amplitude and pulse-duration programming with per-cell proportionality constants alpha and secondary conductances to fix over/undershoot, tuning up to 512 weights concurrently using the same circuit path as inference. Evaluation covers PCM device-to-device and cycle-to-cycle variability, programming precision (<3% average weight error, >3 effective bits), a two-tile 512-252-10 MNIST network with hard-sigmoid between tiles, bias-row offset calibration, and a 128-hidden LSTM for Alice in Wonderland character prediction with activations and vector ops on an FPGA, plus drift over three days.

## Language models evaluated
- Models: 1-layer LSTM (hidden 128) char-level on Alice in Wonderland
- Scale: —

## Contributions
- 14 nm PCM analog inference chip with 512x512-weight tiles and reconfigurable ADC-free duration-format 2-D mesh
- Row-wise closed-loop tuning (CLT) programming executing on up to 512 weights concurrently with <3% weight error
- Fully on-chip multi-tile two-layer MNIST demonstration with in-situ activation functions
- LSTM inference showing resilience to error accumulation over 10,000 characters, and negligible drift impact over 3 days

## Key claims (stable IDs)
- **2021_Narayanan_FullyOnChipMAC14nmPCM_TED#C1** — Row-wise CLT achieves accurate weight transfer on 512x512 tiles — _support:_ average weight error <3%, >3 effective bits — _loc:_ Sec. IV, Fig. 9(j,k)
- **2021_Narayanan_FullyOnChipMAC14nmPCM_TED#C2** — Fully on-chip two-layer MNIST reaches near-software accuracy — _support:_ 97.13% experimental vs 97.73% software; mixed HW-SW with ideal MAC 97.55% — _loc:_ Sec. V, Fig. 10(d)
- **2021_Narayanan_FullyOnChipMAC14nmPCM_TED#C3** — On-chip MAC error increases only slightly vs weight-programming error and LSTM remains stable over long sequences — _support:_ ~1.2-1.4% increase in MAC-error sigma from mixed HS to on-chip; 2.2% increase due to feedback over up to 10,000 characters; cross-entropy 2.24 vs 1.89 software — _loc:_ Sec. V, Fig. 14-15
- **2021_Narayanan_FullyOnChipMAC14nmPCM_TED#C4** — Drift had negligible impact over three days — _support:_ no loss degradation on-chip MACs at day 1 vs day 3 — _loc:_ Fig. 16
- **2021_Narayanan_FullyOnChipMAC14nmPCM_TED#C5** — Duration transport across tiles is accurate — _support:_ <+/-1 tick (~1.2 ns) error up to six tiles — _loc:_ Fig. 1(d)

## Results
- Weight-programming error <3% average on 512x512 tiles (>3-bit effective precision)
- Two-layer MNIST (512-252-10) on-chip: 97.13% vs 97.73% software (~0.6% degradation)
- LSTM (hidden 128, Alice in Wonderland): on-chip cross-entropy 2.24 vs 1.89 software; 2.2% extra MAC error from error feedback over up to 10,000 characters
- No loss degradation from drift between day 1 and day 3

## Key numbers
- tech_node: 14nm
- array_size: 512x512 weights per tile (4 PCM per weight)
- accuracy: 97.13% MNIST (software 97.73%)
- bits_weight: >3 effective bits (<3% error)
- bits_adc: ADC-free (duration format, 8-bit duration capture, 1 tick ~1.2 ns)

## Datasets / benchmarks
MNIST, Alice in Wonderland character prediction

## Limitations
- Small networks only (MNIST MLP, 128-unit LSTM); embedding/output layers, activations and vector ops for LSTM done off-chip on FPGA
- No energy-efficiency or throughput metrics reported (stated as future work)
- Drift evaluated only over three days; long-term drift left to ongoing studies
- Absence of ADCs reduces flexibility and complicates calibration; offset calibration via bias rows
- Programming requires FPGA-in-the-loop CLT

## Remarks
Device- and array-level companion to IBM's 14 nm multi-tile line (leading to the HERMES-style and 2023 Nature speech chip). Its lasting contributions are the parallel row-wise programming, which makes loading large arrays practical, and duration-encoded inter-tile transport avoiding ADC/DAC between layers. The LSTM character-prediction experiment is an early sequential language-task demonstration, although tiny; it motivates later work on transformers and LMs on PCM tiles in category 11.

## Cites (in collection, 5)
- [2018_Ambrogio_PCUAnalogueMemoryTraining_Nature](2018_Ambrogio_PCUAnalogueMemoryTraining_Nature.md) PCM+Capacitor Analog Training (2018) — _background_: "This involves using either arrays of capacitors [10] or resistive non-volatile memory (NVM) [11]-[18] for accelerating Multiply-ACcumulate (MAC) operations, which account for the vast majority of computations in several DNNs (see [9])."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "Drift mitigation will need a multi-pronged approach across device engineering [22], programming procedure, circuit slope correction [23] as well as algorithms, including drift-aware training approaches- [17], [24], [25]."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "This involves using either arrays of capacitors [10] or resistive non-volatile memory (NVM) [11]-[18] for accelerating Multiply-ACcumulate (MAC) operations, which account for the vast majority of computations in several DNNs (see [9])."
- [2019_Ambrogio_PCMDriftInference_IEDM](2019_Ambrogio_PCMDriftInference_IEDM.md) PCM Drift Inference (2019) — _background_: "Drift mitigation will need a multi-pronged approach across device engineering [22], programming procedure, circuit slope correction [23] as well as algorithms, including drift-aware training approaches- [17], [24], [25]."
- [2021_Kariyappa_NoiseResilientDNN_TED](2021_Kariyappa_NoiseResilientDNN_TED.md) Noise-Resilient DNN (2021) — _background_: "Drift mitigation will need a multi-pronged approach across device engineering [22], programming procedure, circuit slope correction [23] as well as algorithms, including drift-aware training approaches- [17], [24], [25]."

## Cited by (in collection, 22)
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "Although experimental results on ReRAM-based IMC systems have already been demonstrated [23]–[25], complete IMC systems based on PCM crossbar arrays had been lacking till recently [26], [27]."
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022) — _uses-method-or-tool_: "The significance factor can be implemented in a number of ways, but is limited to discrete values in this case, which can be readily implemented by multiplying the pulse durations of the input activations applied to the MSP relative to the LSP30,31."
- [2022_Garofalo_HeterogeneousIMCCluster_JETCAS](2022_Garofalo_HeterogeneousIMCCluster_JETCAS.md) Heterogeneous IMC Cluster (2022) — _data/numbers_: "The programming of the IMA is done in a diagonal [27] or row-wise [39] fashion, therefore takes considerably larger time (20× to 30× higher) than merely performing a parallel MVM."
- [2022_Haensch_CIMNVMCodesignReview_AdvMater](2022_Haensch_CIMNVMCodesignReview_AdvMater.md) CIM-NVM-Codesign-Review (2022) — _background_: "It has been shown, however, that individual direct write introduces errors that cannot easily be compensated [65]."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _baseline/comparison_: "Analog weight storage offers high weight density and the ability to operate more rows simultaneously (demonstrated up to 512) (refs 21, 25). However, this approach suffers from accuracy degradation because of the noisy analog weights and higher latency due to the need of slow high resolution analog-to-digital converters."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _uses-method-or-tool_: "To program PCM devices, a parallel programming scheme is used (Fig. 1f) so that all 512 weights in the same row are updated at the same time4."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _contrasts/critiques_: "However, our analysis only assumes one pair of conductances per weight —since many existing AIMC designs provide multiple pairs of PCM devices per weight44,47, such additional redundancy can potentially counteract such stringent device yield requirements."
- [2023_LeGallo_AIHWKit_APLMachLearn](2023_LeGallo_AIHWKit_APLMachLearn.md) AIHWKit (2023) — _background_: "When performing MVMs, the conductance of NVM elements are usually linearly mapped to a range of weight values, and it is assumed that a typical pulse-width modulation of the voltage input5,6 can be approximated by a time average (so that x corresponds to the mean voltage given)."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _background_: "Published macros often use SRAM [17, 20], DRAM [31, 32], ReRAM [18, 30, 33], or STTRAM [34]."
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024) — _background_: "Many recent AIMC prototype chip-building efforts to date have been focused on accelerating the inference phase of deep neural networks (DNNs) trained in digital6-12."
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _background_: "AIMC can be implemented in various ways, for example, using volatile memory [9] or non-volatile memory (NVM) for weight storage; storing one or multiple bits of weights per memory device; and reading memory arrays using analog read voltages [10] or a constant voltage with analog durations [11]."
- [2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun](2025_Chen_ALBERTOn14nmAnalogAIChip_NatCommun.md) ALBERT on 14nm PCM Chip (2025) — _uses-method-or-tool_: "In this work, we map the weights of one ALBERT layer onto a single PCM-based analog inference chip that we have demonstrated recently34."
- [2025_Singh_AIMCTileDesign_NatElectron](2025_Singh_AIMCTileDesign_NatElectron.md) AIMC Tile Design (2025) — _background_: "In some scenarios involving simple activation functions such as ReLU, the generated time pulse can be clipped and consumed downstream as the pulse-width input for the next NN layer, avoiding the intermediate analogue-to-digital and digital-to-time steps entirely33,72."
- [2023_Burr_AnalogAITransformers_IEDM](2023_Burr_AnalogAITransformers_IEDM.md) Burr-AnalogAI-LM-IEDM23 (2023) — _background_: "By exploiting such weight stationarity over short timespans with Volatile Memories (VMs) – SRAM or e-DRAM [6, 8] – or over longer timespans with slower, finite-endurance NonVolatile Memories (NVMs) – Flash [9], Resistive-RAM [10], or phase-change memory (PCM) [11, 12] – such CIM approaches can offer high throughput, low latency, and high energy-efficiency [6, 7, 8]."
- [2025_Burr_AnalogAILowLatencyLM_CICC](2025_Burr_AnalogAILowLatencyLM_CICC.md) Analog-AI LLM Accelerators (CICC) (2025) — _background_: "By exploiting such weight stationarity over short timespans with Volatile Memories (VMs) – SRAM or e-DRAM [7, 9] – or over longer timespans with slower, finite-endurance Non-Volatile Memories (NVMs) – Flash [10], Resistive-RAM [11], or phase-change memory (PCM) [12, 13] – such CIM approaches can offer high throughput, low latency, and high energy-efficiency [7, 8, 9]."
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2023_Antolini_PCMDriftHWSWMitigation_JETCAS](2023_Antolini_PCMDriftHWSWMitigation_JETCAS.md) PCM-Drift-HWSW-Mitigation (2023)
- [2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS](2023_Frank_PCMDriftEnergyAccuracyImpact_IRPS.md) PCM Drift Energy-Accuracy Impact (2023)
- [2023_Bruschi_AIMCResNet18Manycore_DATE](2023_Bruschi_AIMCResNet18Manycore_DATE.md) AIMC-ResNet18-Manycore (2023)
- [2024_Aguirre_MemristorANNHWReview_NatCommun](2024_Aguirre_MemristorANNHWReview_NatCommun.md) Memristor ANN HW Review (2024)
- [2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS](2022_Okazaki_PCM14nmAnalogAccelerator_ISCAS.md) PCM14nm (2022)

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2021_Narayanan_FullyOnChipMAC14nmPCM_TED.pdf](../../02_Fabricated_Chips_and_Macros/2021_Narayanan_FullyOnChipMAC14nmPCM_TED.pdf)
- Full text: [../fulltext/2021_Narayanan_FullyOnChipMAC14nmPCM_TED.txt](../fulltext/2021_Narayanan_FullyOnChipMAC14nmPCM_TED.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/ted.2021.3115993
