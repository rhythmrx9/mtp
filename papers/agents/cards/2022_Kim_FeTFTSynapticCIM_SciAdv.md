---
id: W4223592331
key: 2022_Kim_FeTFTSynapticCIM_SciAdv
title: "CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks"
short: "FeTFT Synaptic CIM"
year: 2022
venue: "SciAdv"
venue_full: "Science Advances"
authors: "Min‐Kyu Kim, Ik‐Jyae Kim, Jang‐Sik Lee"
category: "02 Fabricated Chips & Macros"
devices: ["FeFET"]
models: ["CNN", "VGG"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["analog-mvm", "chip-demo", "weight-mapping", "device-variation", "endurance-retention", "energy-efficiency", "cnn-accelerator", "on-chip-training"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 109
priority_score: 5.43
doi: "https://doi.org/10.1126/sciadv.abm8537"
pdf: "../../02_Fabricated_Chips_and_Macros/2022_Kim_FeTFTSynapticCIM_SciAdv.pdf"
fulltext: "../fulltext/2022_Kim_FeTFTSynapticCIM_SciAdv.txt"
---

# FeTFT Synaptic CIM

**CMOS-compatible compute-in-memory accelerators based on integrated ferroelectric synaptic arrays for convolution neural networks** — Science Advances (2022)

## TL;DR
Fabricated 4x9 IZO/HfZrOx ferroelectric thin-film-transistor synaptic arrays with column/row-parallel program-inhibit programming and measured 1.3%/3.7% cycle/device variation, used to run 3x3 kernel convolutions on a 64x64 image and to simulate VGG-8 on CIFAR-10 at 90.3% (ideal devices 91.0%).

## Summary
Two-terminal crossbar synapses suffer sneak paths and imprecise programming, so the authors build three-terminal FeTFT arrays (W gate lines, ALD HfZrOx ferroelectric, Mo source/drain, ALD IZO channel, <400 C anneal) with four gate lines, four source lines and nine drain lines. A program-inhibit scheme (program 4 V/10 ms on selected GL, inhibit 2 V/30 ms on unselected DLs and SLs) allows selective parallel programming and parallel weight updates (column-wise and row-wise with state-dependent amplitude) using incremental pulses (2.7-3.96 V, 20 mV step). Devices show 64 conductance levels, Gmax/Gmin of 33.1, linearity Apot = 0.8139 and Adep = 1.1464, I-V linearity ~0.95, ~4.1% conductance change over 10,000 s. Convolution kernels (3x3) are mapped to a 9x2 sub-array with differential column pairs for signed weights, inputs encoded as 0-0.1 V on drain lines, and an op-amp subtractor reads out the difference; four kernels (vertical edge, horizontal edge, mean, sharpen) process a 64x64 Lena image. A NeuroSim-style simulator then uses the measured weight-update statistics for VGG-8 on CIFAR-10.

## Contributions
- Integrated CMOS-compatible FeTFT synaptic transistor arrays (<400 C) with three-terminal access that avoids sneak paths
- Program-inhibit scheme enabling column- and row-wise parallel programming and weight update
- Measured convolution kernel realisation (differential 9x2 mapping) and image feature extraction on a 64x64 image
- VGG-8 CIFAR-10 simulation from measured device statistics giving 90.3%

## Key claims (stable IDs)
- **2022_Kim_FeTFTSynapticCIM_SciAdv#C1** — Program-inhibit pulses prevent program disturbance so selected devices can be programmed in parallel — _support:_ 4x4 FeTFTs, four patterns; 4 V/10 ms program with 2 V/30 ms inhibit — _loc:_ Fig. 1C-E, fig. S5
- **2022_Kim_FeTFTSynapticCIM_SciAdv#C2** — FeTFT weight updates are linear with low variation — _support:_ 64 levels, Gmax/Gmin 33.1, Apot 0.8139, Adep 1.1464; cycle-to-cycle ~1.3% (30 cycles); device-to-device ~3.7% (36 devices) — _loc:_ Fig. 2, Fig. 4B
- **2022_Kim_FeTFTSynapticCIM_SciAdv#C3** — Simulated VGG-8 reaches near-ideal accuracy on CIFAR-10 — _support:_ 90.3% after 100 epochs vs 91.0% for ideal synaptic devices — _loc:_ Fig. 4C, Simulation of CNN section
- **2022_Kim_FeTFTSynapticCIM_SciAdv#C4** — A 3x3 convolution consumes ~2 fJ at low conductance — _support:_ E = V^2 x G x t x n = (0.1 V)^2 x ~1 uS x 10 ns x 18 (analytical estimate, not measured) — _loc:_ Convolution section
- **2022_Kim_FeTFTSynapticCIM_SciAdv#C5** — Retention is stable — _support:_ average conductance change ~4.1% over 10,000 s, no state overlap — _loc:_ fig. S10

## Results
- Array: 4 GLs, 4 SLs, 9 DLs; 9x2 sub-array realises a 3x3 differential kernel
- I-V linearity ~0.95; remanent polarization 15.1 / -14.1 uC/cm2 on Mo/HfZrOx/W capacitor
- VGG-8 (six conv, three pooling, two FC; CIFAR-10): 90.3% vs 91.0% ideal; 91% with off-chip training scheme cited
- Estimated ~2 fJ per 3x3 convolution (10 ns pulse, 0.1 V)

## Key numbers
- array_size: 4x9 FeTFT array (4 GL, 4 SL, 9 DL)
- energy_eff: ~2 fJ per 3x3 convolution (estimated)
- accuracy: 90.3% CIFAR-10 (VGG-8, simulated) vs 91.0% ideal
- bits_weight: 64 conductance levels (~6b)

## Datasets / benchmarks
CIFAR-10, Lena 64x64 image

## Limitations
- Tiny array (4x9); CNN accuracy is simulated from device statistics, not run on hardware
- Incremental pulse scheme needs read-before-write, increasing training time and circuit complexity (acknowledged)
- Energy figure is an analytical estimate that ignores peripherals (DACs, op-amps)
- Slow 10-30 ms pulses; no IR-drop, ADC or large-array effects; only 30 endurance cycles
- Digital FeTFT-based kernel demos use static image kernels rather than trained network layers

## Remarks
Credible device/array-level evidence that three-terminal FeFET-type synapses avoid sneak paths and give parallel, linear programming, but it is far from a macro or chip. Accuracy claims rely on feeding measured statistics into a NeuroSim-type simulator, so scaling, peripheral and IR-drop issues remain untested. Useful as the FeFET column in a device comparison; irrelevant to transformers/LMs directly.

## Cites (in collection, 9)
- [2018_Hu_DotProductEngine_AdvMater](2018_Hu_DotProductEngine_AdvMater.md) HPE Dot Product Engine (2018) — _uses-method-or-tool_: "Multiplication of the intensity values of the input pixels by the kernel weights can be achieved using Ohm's law, and the accumulation can be achieved using Kirchhoff's law (20, 46)."
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "For accurate VMM operation, synaptic devices are required, which can precisely adjust the conductance states via analog conductance modulation (5, 11, 12)."
- [2017_Jerry_FeFETAnalogSynapse_IEDM](2017_Jerry_FeFETAnalogSynapse_IEDM.md) FeFET Analog Synapse (2017) — _background_: "Among the available three-terminal synaptic devices, ferroelectric transistors based on zirconium-doped hafnium oxide (HfZrOx) are advantageous because they have CMOS compatibility, fast operation speed, low operation voltages, and high scalability (33–36)."
- [2018_Li_InSituMemristorLearning_NatCommun](2018_Li_InSituMemristorLearning_NatCommun.md) Li In-situ Memristor Learning (2018) — _background_: "The analog conductance modulation characteristics of two-terminal devices are usually achieved by controlling the current of devices during the programming process (22–24)."
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020) — _background_: "In previous studies, several CIM devices with a crossbar structure have been demonstrated using two-terminal devices, such as phase-change and resistive-switching memories, as synaptic devices (13–18)."
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020) — _background_: "To overcome these limitations, compute-in-memory (CIM) has been suggested as alternative hardware for CNNs because it enables parallel data processing (5–9)."
- [2019_Peng_DNNNeuroSim_IEDM](2019_Peng_DNNNeuroSim_IEDM.md) DNN+NeuroSim V1.0 (2019) — _data/numbers_: "For an efficient CIM array, Gmax needs to be lower than 10 μS (12, 56)."
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020) — _background_: "To overcome these limitations, compute-in-memory (CIM) has been suggested as alternative hardware for CNNs because it enables parallel data processing (5–9)."
- [2020_Peng_DNNNeuroSimV2_TCAD](2020_Peng_DNNNeuroSimV2_TCAD.md) DNN+NeuroSim V2.0 (2020) — _data/numbers_: "For an efficient CIM array, Gmax needs to be lower than 10 μS (12, 56)."

## Files
- PDF: [../../02_Fabricated_Chips_and_Macros/2022_Kim_FeTFTSynapticCIM_SciAdv.pdf](../../02_Fabricated_Chips_and_Macros/2022_Kim_FeTFTSynapticCIM_SciAdv.pdf)
- Full text: [../fulltext/2022_Kim_FeTFTSynapticCIM_SciAdv.txt](../fulltext/2022_Kim_FeTFTSynapticCIM_SciAdv.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1126/sciadv.abm8537
