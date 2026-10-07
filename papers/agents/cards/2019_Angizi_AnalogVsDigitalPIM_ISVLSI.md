---
id: W2974067241
key: 2019_Angizi_AnalogVsDigitalPIM_ISVLSI
title: "Accelerating Deep Neural Networks in Processing-in-Memory Platforms: Analog or Digital Approach?"
short: "Analog vs Digital PIM"
year: 2019
venue: "ISVLSI"
venue_full: "IEEE Computer Society Annual Symposium on VLSI (ISVLSI 2019)"
authors: "Shaahin Angizi, Zhezhi He, Dayane Alfenas Reis, Xiaobo Sharon Hu, Wilman Tsai, Shy Jay Lin, Deliang Fan"
category: "08 Simulation, Modeling & Benchmarking"
devices: ["ReRAM", "MRAM", "SRAM-analog", "SRAM-digital", "DRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["benchmarking", "simulator", "crossbar-architecture", "adc-dac", "peripheral-circuits", "energy-efficiency", "quantization"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 1
cites_in_collection: 5
citations_overall: 42
priority_score: 4.54
doi: "https://doi.org/10.1109/isvlsi.2019.00044"
pdf: "../../08_Simulation_and_Benchmarking_Frameworks/2019_Angizi_AnalogVsDigitalPIM_ISVLSI.pdf"
fulltext: "../fulltext/2019_Angizi_AnalogVsDigitalPIM_ISVLSI.txt"
---

# Analog vs Digital PIM

**Accelerating Deep Neural Networks in Processing-in-Memory Platforms: Analog or Digital Approach?** — IEEE Computer Society Annual Symposium on VLSI (ISVLSI 2019) (2019)

## TL;DR
Bottom-up NVSim/CACTI-based comparison of analog ReRAM-crossbar PIM against digital bulk-bitwise PIM (SOT-/STT-MRAM, ReRAM, SRAM, DRAM) at iso-capacity (32 Mb) and iso-computation (LeNet-5, 1:8 bit) shows analog crossbars pay heavily in peripherals and write cost: SOT-/STT-MRAM use 15.8x/17.3x less energy than analog ReRAM.

## Summary
The paper contrasts two ways to do DNN inference in memory: analog current-mode MACs in a ReRAM crossbar (differential positive/negative arrays, DACs, TIAs, differential 8-bit ADC) and quantized/binarized networks executed with bulk bitwise (N)AND/(N)OR and full-adder operations in digital memories (Ambit/DRISA DRAM, Neural Cache SRAM, GraphS-style ReRAM, STT-MRAM CMP-PIM, SOT-MRAM). A cross-layer evaluation stack was built: device-level cell configs from NVSim defaults (ReRAM, SRAM) plus MRAM/DRAM cells, a 256x256 circuit-level simulation, NVSim/CACTI with a custom PIM library for array-level numbers, and an application-level DNN simulator. Iso-memory-capacity compares a 32 Mb single-bank unit on eleven metrics (Table I). Iso-computation maps quantized LeNet-5 (MNIST; weights:activations 1:8, first and last layer full precision) and reports area, energy (split into write-back and read-based ops) and latency (Table II). Analog crossbars need no write-back of intermediate data for MACs but need matrix splitting and large add-on logic.

## Contributions
- First cross-technology, cross-layer quantitative framework comparing analog crossbar and digital in-memory bulk-logic PIM for DNNs
- Iso-capacity and iso-computation comparisons across SOT-MRAM, STT-MRAM, ReRAM, SRAM, DRAM and analog ReRAM
- Breakdown of write-back versus read-based operation energy for PIM execution

## Key claims (stable IDs)
- **2019_Angizi_AnalogVsDigitalPIM_ISVLSI#C1** — Peripheral circuits dominate the analog ReRAM crossbar's area — _support:_ buffers and DAC/ADC > 85% of computational area; M/C ratio 1.33 for analog ReRAM vs 23.53 for SOT-MRAM PIM; crossbar computational area 2.5 mm2 vs 0.4 mm2 digital ReRAM — _loc:_ Sec. V-A / Table I
- **2019_Angizi_AnalogVsDigitalPIM_ISVLSI#C2** — Analog ReRAM has the shortest read latency but the longest write latency — _support:_ read 1.48 ns, write 20.9 ns — _loc:_ Sec. V-A / Table I
- **2019_Angizi_AnalogVsDigitalPIM_ISVLSI#C3** — On LeNet-5, SOT-MRAM and STT-MRAM digital PIM save energy vs analog crossbar — _support:_ 15.8x and 17.3x lower energy (0.85 and 0.78 uJ vs 13.5 uJ) — _loc:_ Sec. V-B / Table II
- **2019_Angizi_AnalogVsDigitalPIM_ISVLSI#C4** — SRAM PIM leaks far more than ReRAM PIM — _support:_ ~14.5x vs digital ReRAM and ~9x vs analog ReRAM — _loc:_ Sec. V-A

## Results
- Table II (LeNet-5 conv layers): area mm2 SOT 0.018, STT 0.012, digital ReRAM 0.0097, SRAM 0.64, DRAM 0.16, analog ReRAM 0.06
- Energy uJ: SOT 0.85, STT 0.78, digital ReRAM 1.9, SRAM 1.6, DRAM 2.1, analog ReRAM 13.5
- Latency ms: SOT 0.9, STT 1.8, digital ReRAM 1.3, SRAM 0.7, DRAM 13.5, analog ReRAM 5.8
- Analog crossbar logic part is ~4x larger than its memory area due to matrix splitting and ADC/DAC
- DRAM Ambit addition needs >14 memory cycles to avoid overwriting data

## Key numbers
- array_size: 256x256 (circuit sim); 32 Mb single bank
- energy_eff: 13.5 uJ analog ReRAM vs 0.78-0.85 uJ MRAM PIM (LeNet-5 conv)
- bits_weight: 1b weights : 8b activations
- bits_adc: 8b

## Datasets / benchmarks
MNIST (LeNet-5)

## Limitations
- Single tiny benchmark (LeNet-5/MNIST) with 1-bit weights and 8-bit activations
- Analog non-idealities (IR drop, noise, SAF) described but not modelled in the comparison
- Digital PIM numbers rely on assumed operation counts without parallelism techniques
- Energy for analog crossbar penalised by write-back assumptions and large ADC/DAC; modern low-ADC-overhead designs not considered
- No transformers or language models

## Remarks
A small but honest apples-to-apples reminder that the analog advantage in ReRAM crossbars depends heavily on peripheral overhead and on weight precision, a point that carries over to AIMC for LMs where multi-bit weights and activations favor analog. Results at 1-bit weights are a poor match for modern 4-8 bit LM inference, so the conclusion favoring digital MRAM PIM should not be generalised. Useful as background for the analog-vs-digital CIM debate in the collection.

## Cites (in collection, 5)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017) — _background_: "PipeLayer [15] achieves the speedup and energy saving of 42.45× and 7.17×, respectively, compared with a GPU platform on average."
- [2019_He_NoiseInjectionAdaption_DAC](2019_He_NoiseInjectionAdaption_DAC.md) NIA / PytorX (2019) — _motivation_: "However, many non-ideal effects, such as IR-drop (i.e., wire resistance), Stuck-At-Fault (SAF), thermal noise, shot and random telegraph noise [16], are hampering the progress of real hardware implementation of large-scale DNNs on ReRAM crossbar-based accelerators."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _background_: "For example, ISAAC [14] architecture improves throughput and energy by 14.8× and 5.5×, respectively, relative to a well-known ASIC architecture."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "More importantly, its currentmode weighted summation operation intrinsically matches the dominant Multiplication-and-Accumulation (MAC) in the artificial neural network, making it one of the most promising candidates as the basic computing unit for neural network accelerator design [6]."
- [2020_Jain_RxNN_TCAD](2020_Jain_RxNN_TCAD.md) RxNN (2020) — _background_: "Many recent works have investigated such issues with either hardware or software solutions [11, 17]."

## Cited by (in collection, 1)
- [2024_Qu_CIMMLC_ASPLOS](2024_Qu_CIMMLC_ASPLOS.md) CIM-MLC (2024) — _background_: "For example, when comparing SRAM[26] and ReRAM, although both have similar latency for read operations, the cost of writing data is considerably higher in ReRAM [3]."

## Files
- PDF: [../../08_Simulation_and_Benchmarking_Frameworks/2019_Angizi_AnalogVsDigitalPIM_ISVLSI.pdf](../../08_Simulation_and_Benchmarking_Frameworks/2019_Angizi_AnalogVsDigitalPIM_ISVLSI.pdf)
- Full text: [../fulltext/2019_Angizi_AnalogVsDigitalPIM_ISVLSI.txt](../fulltext/2019_Angizi_AnalogVsDigitalPIM_ISVLSI.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/isvlsi.2019.00044
