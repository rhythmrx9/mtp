---
id: W7127342328
key: 2026_Xiao_RoboPIM_TCAD
title: "RoboPIM: A ReRAM-Based Accelerator for LLM-Based Robotics Applications via Dynamic Task Slicing"
short: "RoboPIM"
year: 2026
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2026"
authors: "Wenjing Xiao, Jianyu Wang, Dan Chen, Huize Li, Mohsen Guizani, Min Chen, Thomas Wu"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["Transformer", "BERT", "GPT/LLM", "Other"]
lm_models: ["BERT (S/B)", "GPT-2 (up to Large)", "DeepSeek-R1 (lightweight, scales per Table III)"]
param_scale: ""
slm: true
evidence: simulation
topics: ["crossbar-architecture", "tiling-partitioning", "scheduling", "pruning-sparsity", "weight-mapping", "transformer-accelerator", "energy-efficiency", "edge-ai"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 3
citations_overall: 1
priority_score: 8.21
doi: "https://doi.org/10.1109/tcad.2026.3660201"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Xiao_RoboPIM_TCAD.pdf"
fulltext: "../fulltext/2026_Xiao_RoboPIM_TCAD.txt"
---

# RoboPIM

**RoboPIM: A ReRAM-Based Accelerator for LLM-Based Robotics Applications via Dynamic Task Slicing** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems, 2026 (2026)

## TL;DR
RoboPIM is a ReRAM accelerator with mixed 128x128 and 16x16 crossbars, dynamic task slicing and two-stage scheduling for LLM-based robotics, giving 6.85x speedup over ReBERT on LLMs and 2.85x over RoboShape on robot dynamics gradients.

## Summary
LLM-based robotics mixes dense transformer matmuls with block-sparse robot-dynamics matrices whose structure depends on robot topology, and scales range from a few to thousands of dimensions, leaving large crossbars underutilized and wasting peripheral energy. RoboPIM places 32 crossbars of 128x128 and 8 of 16x16 in each compute unit (8 CUs per PE, 32 PEs; 0T1R 2-bit MLC cells, 8-bit ADC, 2-bit DAC). A dynamic task slicing scheme (S2D-Slicing for sparse blocks, D2C-Slicing for dense matrices) cuts matrices into slices that match crossbar sizes and skips zero blocks; a two-stage scheduler with per-size heaps assigns slices to small or large crossbars trading energy for performance. For robot dynamics (inverse-dynamics gradients, RNEA), static matrices (inertia, motion subspace, per-timestep transforms) are pre-written once and independent additive terms run on separate crossbars. A cycle-accurate simulator with Ramulator (HBM 7 pJ/bit), CACTI 7 and ISAAC-derived ADC/DAC models is compared with Xeon CPU, V100 GPU, ReBERT and RoboShape (FPGA).

## Language models evaluated
- Models: BERT (S/B), GPT-2 (up to Large), DeepSeek-R1 (lightweight, scales per Table III)
- Scale: —
- Note: ReRAM crossbar (analog MVM) accelerator for matrix multiplications in LLM-based robotics pipelines; LLM configurations and scale unspecified in abstract; marginal LM focus (robot dynamics matmuls).

## Contributions
- First ReRAM architecture with multiple crossbar sizes for LLM-based robotics
- Dynamic task slicing handling topology-dependent sparsity and varied scales
- Two-stage scheduling to raise crossbar utilization
- Evaluation across robots (iiwa, HyQ, Baxter) and BERT/GPT-2/DeepSeek-R1 LLMs

## Key claims (stable IDs)
- **2026_Xiao_RoboPIM_TCAD#C1** — 6.85x speedup over ReBERT on LLM inference (up to 10.58x on GPT2-L) — _support:_ Fig. 9(a) — _loc:_ Sec. V-B3
- **2026_Xiao_RoboPIM_TCAD#C2** — 2.85x faster than RoboShape on robot dynamics gradients — _support:_ Fig. 9(b) — _loc:_ Sec. V-B4
- **2026_Xiao_RoboPIM_TCAD#C3** — 93.36x and 435.99x less energy than CPU and GPU on LLMs; 2.35x vs ReBERT — _support:_ Fig. 10(a) — _loc:_ Sec. V-B5
- **2026_Xiao_RoboPIM_TCAD#C4** — Small 16x16 crossbars are 1.47x more energy efficient than large ones and give 6.48x higher cell utilization than 64x64 — _support:_ energy breakdown — _loc:_ Fig. 11, Sec. V-C

## Results
- 26.02x and 51.03x performance vs CPU and GPU on LLM inference
- Robot dynamics: 3.96x/9.43x latency vs CPU/GPU; energy saving 14.22x/80.56x/4.87x vs CPU/GPU/RoboShape
- ADC dominates area; ADC needs 128 sampling cycles per large-crossbar row readout

## Key numbers
- array_size: 128x128 and 16x16
- energy_eff: 93.36x vs CPU, 435.99x vs GPU (LLMs)
- throughput: 6.85x vs ReBERT
- bits_weight: 2b MLC cells
- bits_adc: 8b

## Datasets / benchmarks
iiwa, HyQ, Baxter

## Limitations
- Pure simulation; no accuracy or noise evaluation (non-idealities only motivate 2-bit MLC)
- Writes of dynamic operands remain a bottleneck (read:write ratio sweep, Fig. 15)
- LLMs are small/lightweight models; model configuration table not recoverable from extracted text
- Baselines are CPU/GPU/ReBERT/FPGA, no comparison with other crossbar-size-adaptive designs

## Remarks
A mapping/scheduling paper where the language-model angle is mainly workload framing; the useful lesson is that heterogeneous crossbar sizes plus slice-to-crossbar matching improve utilization and energy for small matrices. No evidence on accuracy under analog noise.

## Cites (in collection, 3)
- [2018_Yu_NeuroInspiredComputingENVM_ProcIEEE](2018_Yu_NeuroInspiredComputingENVM_ProcIEEE.md) Yu eNVM Neuro-Inspired Review (2018) — _background_: "FPGAs and ASICs suffer from high data movement [28] during memoryintensive LLM inference, and static/dynamic random access memory (SRAM) PIMs [29, 30] are limited by low density and significant leakage/refresh power, which are prohibitive for energy-constrained robotics."
- [2021_Kang_WindowSelfAttentionReRAM_TCAD](2021_Kang_WindowSelfAttentionReRAM_TCAD.md) Window Self-Attention ReRAM (2021) — _baseline/comparison_: "We compare RoboPIM with the state-of-the-art design for four typical platform: ... 3) ReBERT [38], a state-of-the-art ReRAM-based accelerator for transformer-based LLMs; and 4) RoboShape [13], a state-of-the-art FPGA accelerator for robotics applications."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The resolution of ADCs and DACs is 8 and 2 bit, respectively, and their area and power specifications are based on [37]."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Xiao_RoboPIM_TCAD.pdf](../../11_Small_Language_Models_on_AIMC/2026_Xiao_RoboPIM_TCAD.pdf)
- Full text: [../fulltext/2026_Xiao_RoboPIM_TCAD.txt](../fulltext/2026_Xiao_RoboPIM_TCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/tcad.2026.3660201
