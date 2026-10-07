---
id: W3042493405
key: 2020_Li_TIMELY_ISCA
title: "Timely: Pushing Data Movements And Interfaces In Pim Accelerators Towards Local And In Time Domain"
short: "TIMELY"
year: 2020
venue: "ISCA"
venue_full: "ACM/IEEE 47th Annual International Symposium on Computer Architecture (ISCA 2020)"
authors: "Weitao Li, Pengfei Xu, Yang Katie Zhao, Haitong Li, Yuan Xie, Yingyan Lin"
category: "03 Crossbar Accelerator Architectures"
devices: ["ReRAM"]
models: ["CNN", "ResNet", "VGG", "MLP"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["crossbar-architecture", "adc-dac", "peripheral-circuits", "dataflow-pipelining", "energy-efficiency", "analog-mvm", "cnn-accelerator", "noise-injection"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 13
cites_in_collection: 8
citations_overall: 86
priority_score: 7.79
doi: "https://doi.org/10.1109/isca45697.2020.00073"
pdf: "../../03_Crossbar_Accelerator_Architectures/2020_Li_TIMELY_ISCA.pdf"
fulltext: "../fulltext/2020_Li_TIMELY_ISCA.txt"
---

# TIMELY

**Timely: Pushing Data Movements And Interfaces In Pim Accelerators Towards Local And In Time Domain** — ACM/IEEE 47th Annual International Symposium on Computer Architecture (ISCA 2020) (2020)

## TL;DR
TIMELY cuts input/Psum data-movement and DAC/ADC energy in ReRAM PIM with analog local buffers, time-domain interfaces and only-once-input-read mapping, achieving 21 TOPs/W (8-bit) peak, over 10x PRIME energy efficiency and up to 736.6x throughput in simulation with <=0.1% accuracy loss.

## Summary
The paper observes that ReRAM PIM accelerators (PRIME, ISAAC, PipeLayer) still waste energy on moving inputs and partial sums (up to 83% in PRIME) and on DAC/ADC interfaces (61% of ISAAC energy, Fig. 4). TIMELY addresses this with three ideas: (1) analog local buffers (X-subBufs and P-subBufs) between crossbars so inputs and Psums stay in the analog/time domain, (2) time-domain interfaces using 8-bit DTCs/TDCs (shared by gamma rows/columns) instead of DACs/ADCs, and (3) an only-once-input-read (O2IR) mapping that reads each input once and forwards it horizontally across crossbars in a sub-Chip. Weights are stored in ReRAM crossbars (BxB cells), a sub-Chip is a grid of crossbars with I-adders and charging-and-comparison units for time-domain dot products, and sub-Chips connect via a bus with digital shift/add and pooling. Evaluation uses an in-house simulator with 65 nm CMOS peripheral parameters (silicon-verified DTC/TDC, Cadence-simulated buffers), 40 MHz clock, 106 sub-Chips (91 mm2 vs ISAAC 88 mm2), 15 CNN/DNN benchmarks, and baselines PRIME and ISAAC (plus PipeLayer/AtomLayer from reported numbers). Accuracy is checked by adding Monte-Carlo-derived Gaussian circuit noise during training/inference, with 12 cascaded X-subBufs chosen to keep loss <=0.1%.

## Contributions
- Analog local buffers inside ReRAM crossbar fabric to maximize analog data locality without hurting computational density
- Time-domain interfacing (DTC/TDC) reducing per-conversion energy, combined with ALBs to reduce number of conversions
- O2IR mapping that reads every input only once
- Ablation and generalization studies of ALB, TDI and O2IR; benchmarking against PRIME, ISAAC, PipeLayer and AtomLayer on 15 benchmarks

## Key claims (stable IDs)
- **2020_Li_TIMELY_ISCA#C1** — TIMELY improves peak energy efficiency by over 10x versus PRIME and computational density by over 6.4x versus PipeLayer — _support:_ 21.00 TOPs/W (8-bit) vs PRIME 2.10; 38.33 TOPs/(s mm2); improvements 10x-49.3x energy efficiency across baselines — _loc:_ Table IV, Sec. VI-B
- **2020_Li_TIMELY_ISCA#C2** — Throughput up to 736.6x and computational density up to 31.2x higher than PRIME — _support:_ abstract — _loc:_ Abstract / Sec. VI
- **2020_Li_TIMELY_ISCA#C3** — System-level accuracy loss stays <=0.1% despite analog buffers and time-domain circuits — _support:_ Monte-Carlo Cadence noise as Gaussian noise, 12 cascaded X-subBufs (error sqrt(12) eps) — _loc:_ Sec. VI-B Accuracy
- **2020_Li_TIMELY_ISCA#C4** — Computational energy is only 17% of PRIME chip energy; data movement and DAC/ADC dominate — _support:_ Fig. 4: analog comp (DAC/ADC) 61%, comm 19%, memory 12% in ISAAC; PRIME inputs 36%, Psums/outputs 47% — _loc:_ Fig. 4

## Results
- Peak 21.00 TOPs/W for 8-bit MAC (TIMELY-a) and 6.90 TOPs/W for 16-bit (TIMELY-b), vs PRIME 2.10, ISAAC 0.38, PipeLayer 0.14, AtomLayer 0.68 TOPs/W
- Improvement 10.0x vs PRIME, 18.2x vs ISAAC, 49.3x vs PipeLayer, 10.1x vs AtomLayer (Table IV, as parsed); average 10x/14.8x vs PRIME/ISAAC per the previous analysis
- Computational density 38.33 TOPs/(s mm2) (8-bit), up to 31.2x over baselines; throughput up to 736.6x
- Area 91 mm2 for 106 sub-Chips vs ISAAC 88 mm2
- <=0.1% inference accuracy loss with circuit-level noise

## Key numbers
- tech_node: 65nm CMOS peripherals
- energy_eff: 21.00 TOPs/W (8-bit); 6.90 TOPs/W (16-bit)
- throughput: up to 736.6x PRIME
- accuracy: <=0.1% loss
- bits_adc: 8-bit DTC/TDC

## Datasets / benchmarks
VGG-D, ResNet-18/50/101/152, SqueezeNet, MSRA-3, ImageNet CNNs (15 benchmarks, Table III)

## Limitations
- Entirely simulated; no fabricated TIMELY chip
- Baseline numbers for PipeLayer and AtomLayer taken from their papers; only PRIME and ISAAC re-simulated
- Accuracy tested only on CNN/DNN image models with Gaussian noise assumption and noise-aware training
- Analog buffer chains (12 cascaded X-subBufs) may accumulate error under real PVT/drift; ReRAM device non-idealities largely not modelled beyond circuit noise
- No transformers or language models

## Remarks
TIMELY shifts the optimization target from the MAC array to data movement and conversion periphery, and O2IR is a concrete mapping strategy tied to dataflow. Headline gains are relative to PRIME/ISAAC-era baselines and are simulation-only, so real-silicon validation is missing. The analog-buffer idea contrasts with CASCADE, which uses analog buffers only to reduce A/D conversions. For LM mapping it is relevant mainly as a model of conversion/data-movement energy, not as an attention-capable design.

## Cites (in collection, 8)
- [2017_Chen_AcceleratorFriendlyTraining_DATE](2017_Chen_AcceleratorFriendlyTraining_DATE.md) Accelerator-friendly training (2017) — _background_: "To address this challenge, TIMELY not only leverages algorithm resilience of CNNs/DNNs to counter hardware vulnerability [9], [48], [81], but also minimize potential errors introduced by hardware, thereby achieving the optimal trade-off between energy efficiency and accuracy."
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _baseline/comparison_: "Compared with representative R2 PIM accelerators (see Table IV), TIMELY can improve energy efficiency by over 10x (over PRIME [14]) and the computational density by over 6.4x (over PipeLayer [62])."
- [2017_Liu_DefectRescuing_DAC](2017_Liu_DefectRescuing_DAC.md) Defect Rescuing (2017) — _background_: "To address this challenge, TIMELY not only leverages algorithm resilience of CNNs/DNNs to counter hardware vulnerability [9, 48, 81], but also minimize potential errors introduced by hardware"
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "resistive-random-access-memory-(ReRAM)-based PIM (R2 PIM) accelerators have gained extensive research interest due to ReRAM's high density (e.g. 25x-50x higher over SRAM [71, 79])."
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019) — _contrasts/critiques_: "Although a recent R2 PIM accelerator, CASCADE [15], has adopted analog buffers, it only uses analog ReRAM buffer to reduce the number of A/D conversions, thereby minimizing computational energy."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "Among PIM accelerators on various memory technologies [14, 42, 43, 56, 58, 62, 66, 78], resistive-random-access-memory-(ReRAM)-based PIM (R2 PIM) accelerators have gained extensive research interest"
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _motivation_: "Fig. 4. (a) The number of input/Psum accesses, (b) energy breakdown of PRIME [14], and (c) energy breakdown of ISAAC [58]."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _baseline/comparison_: "However, the energy efficiency of R2 PIM accelerators (such as PRIME [14], ISAAC [58], and PipeLayer [62]) is still limited due to two bottlenecks (see Fig. 1 (b)): (1) although the weights are kept stationary in memory, the energy cost of data movements due to inputs and Psums is still large (as high as 83% in PRIME [14])"

## Cited by (in collection, 13)
- [2021_Yuan_PruningDifferentialMapping_ISQED](2021_Yuan_PruningDifferentialMapping_ISQED.md) Pruning + Differential Mapping (2021) — _background_: "Recent work, TIMELY [23] saves the energy cost of data movements and D/A and A/D domain conversion by enhancing analog data locality to keep computations in analog domain."
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021) — _background_: "Besides, the recent work TIMELY [23] is proposed to enhance the analog data C."
- [2022_Xiao_AnalogAccuracyStudy_CASMag](2022_Xiao_AnalogAccuracyStudy_CASMag.md) Analog Accuracy Study (2022) — _contrasts/critiques_: "Recent work has optimized the performance and energy of bit-sliced accelerators [6, 14, 42, 49], but rarely evaluates the effect of system-level design decisions on inference accuracy."
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021) — _background_: "ReRAM crossbar is emerging as a promising solution to mitigate problems such as memory wall, owing to its high memory accessing bandwidth and high density [4, 6, 9, 10, 19–23]."
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023) — _contrasts/critiques_: "Alternatively, other designs use efficient lower-resolution ADCs to process high-resolution analog values from crossbars [5, 7, 24]."
- [2023_Gao_StaticWeightProgScheduling_TECS](2023_Gao_StaticWeightProgScheduling_TECS.md) Static Weight-Programming Scheduling (2023) — _background_: "Processing-in-memory (PIM) -based accelerators can perform in-situ computation and eliminate the data movement between memory and processing elements [1, 4, 8, 11, 23]."
- [2023_Li_CrossbarAllocationOpt_TODAES](2023_Li_CrossbarAllocationOpt_TODAES.md) Crossbar Allocation Framework (2023) — _background_: "In fact, plenty of works have demonstrated that ReRAM-based architectures can effectively accelerate CNNs with higher energy efficiency (e.g., [1, 7, 8, 15, 22-25, 28-30, 33, 34]), compared with conventional complementary metal-oxide-semiconductor (CMOS) based CNN accelerators."
- [2024_Andrulis_CiMLoop_ISPASS](2024_Andrulis_CiMLoop_ISPASS.md) CiMLoop (2024) — _uses-method-or-tool_: "The Library Plug-In models a library of components used in various CiM works [2, 6, 18, 29, 37, 38, 40, 44, 51, 57]."
- [2024_Xu_ReCAT_TODAES](2024_Xu_ReCAT_TODAES.md) ReCAT (2024) — _uses-method-or-tool_: "We use the parameters of analog input buffers and analog adders according to TIMELY [27], and adopt the TIA design in CASCADE [8] to cascade crossbar arrays."
- [2024_Moitra_TReX_TETC](2024_Moitra_TReX_TETC.md) TReX (2024) — _uses-method-or-tool_: "Additionally, to reduce the ADC precision, we follow input and weight splitting paradigms similar to prior works [7], [34]."
- [2025_Hou_NORA_DATE](2025_Hou_NORA_DATE.md) NORA (2025) — _background_: "To break the memory wall, computing in memory (CIM), which avoids intensive data transfer by directly executing matrix-vector multiplications (MVM) in memory devices, has been applied to DNN acceleration [2], [8], [17]–[20], [29], [34], [35]."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022)
- [2025_Hou_SAGE_ICCAD](2025_Hou_SAGE_ICCAD.md) SAGE (2025)

## Files
- PDF: [../../03_Crossbar_Accelerator_Architectures/2020_Li_TIMELY_ISCA.pdf](../../03_Crossbar_Accelerator_Architectures/2020_Li_TIMELY_ISCA.pdf)
- Full text: [../fulltext/2020_Li_TIMELY_ISCA.txt](../fulltext/2020_Li_TIMELY_ISCA.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isca45697.2020.00073
