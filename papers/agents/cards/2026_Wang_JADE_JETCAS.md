---
id: W7143500069
key: 2026_Wang_JADE_JETCAS
title: "JADE: Joint Architecture-Dataflow Exploration for LLM Inference on Heterogeneous In- and Near-Memory Computing Systems"
short: "JADE"
year: 2026
venue: "JETCAS"
venue_full: "IEEE Journal on Emerging and Selected Topics in Circuits and Systems"
authors: "Yimin Wang, Zhen Wu, Yue Jiet Chong, Xuanyao Fong"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM", "SRAM-digital"]
models: ["Transformer", "GPT/LLM"]
lm_models: ["Llama-3.2-1B", "Llama-3-8B", "Llama-2-13B"]
param_scale: "1B-13B"
slm: true
evidence: simulation
topics: ["language-models", "attention", "kv-cache", "tiling-partitioning", "weight-mapping", "dataflow-pipelining", "heterogeneous-analog-digital", "transformer-accelerator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.1109/jetcas.2026.3679018"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Wang_JADE_JETCAS.pdf"
fulltext: "../fulltext/2026_Wang_JADE_JETCAS.txt"
---

# JADE

**JADE: Joint Architecture-Dataflow Exploration for LLM Inference on Heterogeneous In- and Near-Memory Computing Systems** — IEEE Journal on Emerging and Selected Topics in Circuits and Systems (2026)

## TL;DR
JADE is a Python framework that co-explores architecture (IMC/NMC organisation, mesh/H-tree topology) and dataflow (matrix-multiplication unrolling, attention variants) for LLM inference on spatial RRAM-IMC plus near-memory systems, evaluated on Llama 3.2-1B, Llama 3-8B and Llama 2-13B.

## Summary
LLM inference needs both static weight MMs, well suited to IMC, and dynamic MMs on run-time generated K/V data, which need flexible near-memory computing (NMC). Existing IMC/NMC LLM accelerators use fixed architectures and model-specific dataflow. JADE defines four design factor categories: computing/memory organisation (core-level homogeneous or heterogeneous), interconnect topology, matrix-multiplication unrolling and mapping, and attention mechanism (MHA vs GQA, original vs FlashAttention fusion). A unified MM tiling/unrolling representation drives virtual mapping, physical mapping (inter-matrix placement and intra-tile layout of weights/KV scratchpads) and a dataflow generator that routes collective patterns (reduction, broadcast, all-reduce) on mesh or H-tree interconnects with reduction adders in the routers. Weights are statically mapped onto 128x128 RRAM crossbar IMC cores (area/power from Peng et al. TCAS-I 2020), while attention score computation runs on digital NMC cores with scratchpads; digital logic is synthesised in Verilog at 45 nm and scratchpads modelled with CACTI. Three design configurations (HOMM, HEMM, HETM, naming intra-tile topology for IMC then NMC) are compared on critical path, communication overhead and throughput. Analog non-idealities and accuracy are not modelled; this is a latency/throughput/energy architecture study.

## Language models evaluated
- Models: Llama-3.2-1B, Llama-3-8B, Llama-2-13B
- Scale: 1B-13B
- Note: Only the abstract was available; it names no specific LLMs or scales, exploring IMC/NMC architecture-dataflow co-design.

## Contributions
- Extended IMC/NMC LLM accelerator design space covering compute, memory and communication, allowing homogeneous vs heterogeneous comparisons
- Unified MM tiling and unrolling representation aware of IMC/NMC differences and attention-head operation flows
- Dataflow routing based on collective communication patterns and mesh/H-tree topologies
- Case studies on kernel fusion, MHA vs GQA, prefill vs decode, and scalability

## Key claims (stable IDs)
- **2026_Wang_JADE_JETCAS#C1** — FlashAttention shortens the critical path but does not reduce communication overhead on spatially distributed-memory IMC/NMC architectures — _support:_ Fig. 11 vs Fig. 12 — _loc:_ Sec. V-C
- **2026_Wang_JADE_JETCAS#C2** — GQA reduces both critical path and communication overhead versus MHA — _support:_ Figs. 11-12; temporal multiplexing of K/V adopted for memory efficiency — _loc:_ Sec. V-D
- **2026_Wang_JADE_JETCAS#C3** — Critical path grows ~2x when model size grows 8x (Llama 3.2-1B to Llama 3-8B) — _support:_ Scaling scales with se*sl or sh*sl rather than se*sh*sl — _loc:_ Sec. V-F1
- **2026_Wang_JADE_JETCAS#C4** — Decode is the bottleneck because token-level pipelining is only available in prefill — _support:_ Table III prefill/decode throughput on Llama 3-8B and 2-13B (HOMM) — _loc:_ Sec. V-E
- **2026_Wang_JADE_JETCAS#C5** — Reduction logic in IMC cores is cheap in area but not in energy — _support:_ 1-3% of macro area, 15-35% of energy — _loc:_ Sec. V-B, Fig. 10

## Results
- Router/reduction logic: 1-3% of IMC macro area and 15-35% of energy (16 IMC cores, Fig. 10)
- Critical path rises about 2x for 8x model growth from Llama 3.2-1B to Llama 3-8B (Fig. 11)
- JADE outperforms prior IMC-based LLM accelerators (TransPIM, Cambricon-LLM) in throughput and energy efficiency but lags wafer-scale systems (WaferLLM) due to resource provisioning (Table IV, numeric values not recoverable from extracted text)
- H-tree is efficient for aggregating IMC outputs but poorly suited to NMC and emerging attention; hybrid mesh/tree topologies suggested

## Key numbers
- tech_node: 45nm (digital synthesis)
- array_size: 128x128

## Limitations
- Architecture-level simulation only; no silicon and no analog accuracy modelling (noise, drift, ADC, quantisation effects on LM quality)
- IMC core fixed to 128x128 RRAM taken from prior work; crossbar size matched to Llama head width (128)
- All-reduce for partitioned heads not evaluated
- IMC capacity limits max model size; scale-out and long-context K/V offloading left as future work
- Tables III and IV numeric contents are not present in the extracted text

## Remarks
A useful system-level counterpart to accuracy-focused AIMC LLM work: it shows how static projection/FFN weights map to RRAM crossbars while dynamic attention and KV cache stay in digital NMC. Evidence is simulation with calibrated digital blocks and borrowed analog parameters. It addresses 1B-13B models, but says nothing about their accuracy under analog noise; pair with category 11 noise-robustness papers.

## Cites (in collection, 7)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019) — _contrasts/critiques_: "Existing memory-centric dataflow exploration frameworks [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25] are predominantly tailored for conventional neural networks (NNs) and fall short in addressing the design challenges of LLMs."
- [2019_Peng_WeightMappingDataflowPIM_TCAS-I](2019_Peng_WeightMappingDataflowPIM_TCAS-I.md) Weight Mapping Dataflow PIM (2019) — _uses-method-or-tool_: "The area and power of the IMC core, featuring a 128 × 128 RRAM crossbar array, are adopted from [36]."
- [2022_Zhou_TransPIM_HPCA](2022_Zhou_TransPIM_HPCA.md) TransPIM (2022) — _baseline/comparison_: "These works include wafer-scale accelerators [14] and IMC-focused work [41], [42]. This work achieves better performance compared to the previous IMC-based works, thanks to the hybrid IMC-NMC design catered for both the dynamic and static data, as well as the dedicated router design."
- [2022_Yang_AERO_JETCAS](2022_Yang_AERO_JETCAS.md) AERO (2022) — _contrasts/critiques_: "Existing memory-centric dataflow exploration frameworks [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25] are predominantly tailored for conventional neural networks (NNs) and fall short in addressing the design challenges of LLMs."
- [2023_Wang_IMCPELevelMappingBenchmark_JETCAS](2023_Wang_IMCPELevelMappingBenchmark_JETCAS.md) IMC PE-Level Mapping Benchmark (2023) — _contrasts/critiques_: "Existing memory-centric dataflow exploration frameworks [15], [16], [17], [18], [19], [20], [21], [22], [23], [24], [25] are predominantly tailored for conventional neural networks (NNs) and fall short in addressing the design challenges of LLMs."
- [2023_Li_CPSAA_TCAD](2023_Li_CPSAA_TCAD.md) CPSAA (2023) — _contrasts/critiques_: "Though prior works have shown IMC/NMC-based systems for LLM acceleration, most only support model-specific dataflow with custom architectural design [5], [6], [7], falling short in terms of system and dataflow flexibility to diverse models."
- [2024_Luo_H3DTransformer_TODAES](2024_Luo_H3DTransformer_TODAES.md) H3DTransformer (2024) — _background_: "This necessitates a joint utilization of IMC and NMC architectures [5], [6], [7], [8], [9], [10], and a tightly-coupled IMC/NMC design becomes essential to effectively support the hybrid data-stationarity patterns inherent in LLM workloads."

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Wang_JADE_JETCAS.pdf](../../11_Small_Language_Models_on_AIMC/2026_Wang_JADE_JETCAS.pdf)
- Full text: [../fulltext/2026_Wang_JADE_JETCAS.txt](../fulltext/2026_Wang_JADE_JETCAS.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/jetcas.2026.3679018
