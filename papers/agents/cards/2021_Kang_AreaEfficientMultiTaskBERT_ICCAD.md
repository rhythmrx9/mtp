---
id: W4200149283
key: 2021_Kang_AreaEfficientMultiTaskBERT_ICCAD
title: "A Framework for Area-efficient Multi-task BERT Execution on ReRAM-based Accelerators"
short: "Area-Efficient Multi-Task BERT"
year: 2021
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021)"
authors: "Myeonggu Kang, Hyein Shin, Jaekang Shin, Lee‐Sup Kim"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["ReRAM"]
models: ["BERT", "Transformer"]
lm_models: ["BERT-base", "BERT-large", "RoBERTa-base", "DistilBERT"]
param_scale: "66M-340M"
slm: true
evidence: simulation
topics: ["language-models", "weight-mapping", "quantization", "pruning-sparsity", "transformer-accelerator", "energy-efficiency", "llm-adapters-lora"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 4
citations_overall: 4
priority_score: 9.42
doi: "https://doi.org/10.1109/iccad51958.2021.9643471"
pdf: "../../11_Small_Language_Models_on_AIMC/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.pdf"
fulltext: "../fulltext/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.txt"
---

# Area-Efficient Multi-Task BERT

**A Framework for Area-efficient Multi-task BERT Execution on ReRAM-based Accelerators** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2021) (2021)

## TL;DR
A training-free framework that stores one shared BERT base model plus heavily compressed task-specific deltas (near-ternary quantisation + output-channel hard-sharing) on ReRAM arrays, cutting multi-task BERT area to 0.26x of baseline (8 GLUE tasks) with 0.1 average GLUE score change in accuracy mode.

## Summary
Multi-task BERT (one fine-tuned model per NLP task) is costly on ReRAM accelerators because all weights must be pre-programmed on arrays, so area grows linearly with the number of tasks. The authors observe that each fine-tuned model has cosine similarity >0.99 with the pre-trained base model, so task-specific(t) = fine-tuned(t) - base has few non-zero elements (2.6-42%) of average magnitude about 1 (8-bit, GLUE), and that tasks differ in error resiliency (CoLA/RTE fragile, SST-2/WNLI robust). A two-stage compressor first applies near-ternary quantisation (clip to the lowest precision, in steps of the ReRAM cell resolution, that keeps cosine similarity >= 0.95; most tasks end ternary) and then selective hard-sharing, which removes output channels (i.e. bitlines, the unit that actually saves ReRAM area) from the delta so those channels reuse base-model weights; a profiler uses K-means clustering of task error resiliency and a user mode (acc/opt/agg) to set max_prec(t) and selective_factor(t). At inference the base-model array and the compressed delta arrays run in parallel and are summed in a modified global shift-and-add block with metadata for removed channels. Evaluation uses a cycle-level ISAAC-based simulator (32nm, 128x128 arrays, 1 bit/cell, 8b ADC, 1b DAC, 8-bit inputs and weights) with BERT-base on eight GLUE tasks, accuracy computed in PyTorch without analog noise.

## Language models evaluated
- Models: BERT-base, BERT-large, RoBERTa-base, DistilBERT
- Scale: 66M-340M
- Note: Multi-task BERT models on a ReRAM-based accelerator model; specific BERT size not stated in the available text.

## Contributions
- Characterisation of multi-task BERT: fine-tuned models highly correlated with the base model, deltas small and sparse, and task-dependent error resiliency
- Training-free, ReRAM-aware two-stage compressor (near-ternary quantisation + selective hard-sharing of output channels) with a profiler
- Hardware support via a modified shift-and-add summing base and task-specific results (<0.1% area and energy overhead)
- Evaluation across cell resolutions and base models (BERT-large, RoBERTa-base, DistilBERT) and comparison with five GPU-oriented multi-task compression methods

## Key claims (stable IDs)
- **2021_Kang_AreaEfficientMultiTaskBERT_ICCAD#C1** — Fine-tuned BERT is almost identical to its base model — _support:_ cosine similarity 0.991-0.999 across GLUE tasks; task-specific non-zero ratio 2.6-42.0%, avg magnitude 1.00-1.35 — _loc:_ Sec. III-A, Fig. 4
- **2021_Kang_AreaEfficientMultiTaskBERT_ICCAD#C2** — Area reduction grows with number of tasks without added latency — _support:_ MTacc area 0.62x, 0.37x, 0.26x at 2, 4, 8 tasks; MTopt/MTagg up to 77%/79% reduction — _loc:_ Sec. IV-D1, Fig. 14
- **2021_Kang_AreaEfficientMultiTaskBERT_ICCAD#C3** — Accuracy preserved without retraining — _support:_ GLUE average 78.7 baseline vs 78.8 (MTacc), 78.0 (MTopt, -0.7), 76.0 (MTagg, -2.7) — _loc:_ Sec. IV-C, Fig. 13
- **2021_Kang_AreaEfficientMultiTaskBERT_ICCAD#C4** — Existing multi-task BERT compression methods are unsuited to ReRAM — _support:_ Table II: all require training; some do not reduce area or increase latency — _loc:_ Sec. IV-F, Table II

## Results
- Area up to 74% lower (0.26x) for 8 tasks with MTacc and BERT-base; BERT-large 74%, RoBERTa-base 76%, DistilBERT 63% reductions (Fig. 16b)
- Near-ternary quantisation needs 1.12 cells per task-specific element (0.14x baseline); MTopt 0.86 (0.11x), MTagg 0.65 (0.08x) (Fig. 12)
- Area-normalised throughput up to 3.9x (MTacc) and 4.9x (MTagg); area-normalised energy efficiency up to 3.4x and 4.5x (Fig. 15)
- At 1-bit/cell MTNQ area is 0.26x of baseline versus 0.38x (2-bit) and 0.63x (4-bit) (Fig. 16a)
- With a single task the framework needs more area than baseline because base and delta are stored separately

## Key numbers
- tech_node: 32nm (ISAAC-style simulator)
- array_size: 128x128, 1 bit/cell
- energy_eff: up to 3.4x area-normalised (MTacc), 4.5x (MTagg)
- throughput: up to 3.9x area-normalised (MTacc), 4.9x (MTagg)
- accuracy: GLUE avg 78.8 (MTacc) vs 78.7 baseline; -0.7 (opt), -2.7 (agg)
- bits_weight: 8b base; near-ternary task-specific
- bits_adc: 8b ADC, 1b DAC

## Datasets / benchmarks
GLUE (CoLA, SST-2, MRPC, STS-B, QQP, MNLI, WNLI, RTE)

## Limitations
- Cycle-level architectural simulation only; accuracy is digital (PyTorch), no ReRAM variation, drift or ADC noise included
- Only encoder-only BERT-family models on GLUE (110M-340M); no generative or decoder models
- Benefit only appears with multiple tasks (area worse than baseline for one task); base-model is still stored at full precision
- Gains concentrate on 1-bit/cell cells; smaller at higher cell resolutions
- Compression quality relies on cosine similarity thresholds (0.95, per-task selective factors) chosen heuristically

## Remarks
An early, ReRAM-aware treatment of the multi-task/adapter-like deployment problem for language models; the shared-base-plus-sparse-delta idea parallels LoRA/adapter ideas and is relevant to deploying many fine-tuned SLMs on non-volatile arrays where reprogramming is expensive. Evidence is architectural simulation with ideal analog arithmetic, so it says nothing about noise robustness of the deltas, which are ternary and could be especially noise-sensitive. Later work in the collection (MGen) builds on it.

## Cites (in collection, 4)
- [2017_Xia_MNSIM_TCAD](2017_Xia_MNSIM_TCAD.md) MNSIM (2017) — _background_: "The ReRAM-based accelerators [3], [20], [27] are proposed to solve the data communication issue by adopting in-memory computation."
- [2020_Yang_ReTransformer_ICCAD](2020_Yang_ReTransformer_ICCAD.md) ReTransformer (2020) — _background_: "By exploiting in-memory computation, the ReRAM-based accelerator enables energy-efficient execution of a single BERT model [29]."
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016) — _uses-method-or-tool_: "The simulator is based on ISAAC [20] configuration with 32nm process node, and it utilizes positive and negative arrays to store weight parameters."
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016) — _background_: "The ReRAM-based accelerators [3], [20], [27] are proposed to solve the data communication issue by adopting in-memory computation."

## Cited by (in collection, 2)
- [2025_Zhao_RACE-IT_ICCD](2025_Zhao_RACE-IT_ICCD.md) RACE-IT (2025) — _background_: "In-memory Computing (IMC) stands out as a promising solution to alleviate the computational and memory challenges posed by Transformer models [6–8]."
- [2023_Kang_MGen_TC](2023_Kang_MGen_TC.md) MGen (2023)

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.pdf](../../11_Small_Language_Models_on_AIMC/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.pdf)
- Full text: [../fulltext/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.txt](../fulltext/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iccad51958.2021.9643471
