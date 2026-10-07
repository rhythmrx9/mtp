---
id: W4383753658
key: 2023_Liu_ERABS_TC
title: "ERA-BS: Boosting the Efficiency of ReRAM-Based PIM Accelerator With Fine-Grained Bit-Level Sparsity"
short: "ERA-BS"
year: 2023
venue: "TC"
venue_full: "IEEE Transactions on Computers"
authors: "Fangxin Liu, Wenbo Zhao, Zongwu Wang, Yongbiao Chen, Xiaoyao Liang, Li Jiang"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: algorithm+simulation
topics: ["pruning-sparsity", "bit-slicing", "energy-efficiency", "crossbar-architecture", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 9
citations_overall: 15
priority_score: 3.34
doi: "https://doi.org/10.1109/tc.2023.3290869"
pdf: null
fulltext: null
---

# ERA-BS

**ERA-BS: Boosting the Efficiency of ReRAM-Based PIM Accelerator With Fine-Grained Bit-Level Sparsity** — IEEE Transactions on Computers (2023)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
ERA-BS exploits fine-grained bit-level sparsity in both static weights (via an adaptive bit-flip + exponent-based quantization scheme) and dynamic activations (via crossbar-aware pruning) to shrink ReRAM crossbar footprint, claiming up to 43x/78x/73x energy/area/throughput gains over ISAAC and 5.3x/7.2x/32x gains over PIM-Prune.

## Summary
ReRAM crossbar accelerators are limited by constrained concurrent MAC throughput (rows/columns usable at once) and costly high-precision ADCs, and conventional DNN sparsity is hard to exploit in a fixed crossbar structure, especially activation sparsity. ERA-BS targets the correlation between bit-level sparsity (in weights and activations) and crossbar performance. It proposes a bit-flip scheme combined with exponent-based quantization that adaptively flips mapped-weight bits to free redundant crossbar space with little accuracy loss or hardware overhead, plus an architecture that shrinks crossbar footprint so more arrays can be used in parallel. For activations, it adds a dynamic sparsity exploitation scheme (crossbar-aware activation pruning plus runtime hardware support) that exploits the tightly coupled crossbar structure. Together, static weight-bit sparsity and dynamic activation sparsity are both exploited at fine (bit-level) granularity to raise performance and cut energy with reportedly negligible overhead. Across a range of networks, ERA-BS is reported to reach up to 43x energy efficiency, 78x area efficiency, and 73x throughput versus ISAAC, and 5.3x/7.2x/32x versus the more recent PIM-Prune baseline, with similar or higher accuracy.

## Contributions
- A bit-flip scheme combined with exponent-based quantization that adaptively frees redundant crossbar cell space from sparse weight bits with minimal accuracy loss
- A crossbar architecture that integrates the bit-level sparsity techniques to physically shrink crossbar footprint for denser array packing
- A dynamic activation sparsity exploitation scheme (crossbar-aware activation pruning + runtime hardware) tailored to the crossbar's tightly coupled structure
- Joint exploitation of fine-grained static (weight) and dynamic (activation) bit-level sparsity in a ReRAM PIM accelerator
- Large reported efficiency gains over both a classic (ISAAC) and a recent sparsity-aware (PIM-Prune) ReRAM baseline

## Key claims (stable IDs)
- **2023_Liu_ERABS_TC#C1** — ERA-BS achieves large efficiency gains over ISAAC — _support:_ up to 43x energy efficiency, 78x area efficiency, 73x throughput vs. ISAAC — _loc:_ Abstract
- **2023_Liu_ERABS_TC#C2** — ERA-BS outperforms the more recent PIM-Prune sparsity-aware ReRAM design with comparable or better accuracy — _support:_ 5.3x energy efficiency, 7.2x area efficiency, 32x performance gain vs. PIM-Prune, with similar or higher accuracy — _loc:_ Abstract

## Results
- Up to 43x energy efficiency, 78x area efficiency, 73x throughput vs. ISAAC
- 5.3x energy efficiency, 7.2x area efficiency, 32x performance vs. PIM-Prune, similar/higher accuracy

## Limitations
- Analysis based on abstract only (full text not accessible); the mechanics of the bit-flip/exponent quantization scheme, benchmark network list, and exact accuracy deltas could not be verified
- Very large claimed speedups (up to 78x area efficiency) are relative to the authors' own re-implementation/assumptions for ISAAC and PIM-Prune baselines, which cannot be independently checked from the abstract

## Remarks
This is an algorithm+architecture co-design paper for sparsity exploitation in ReRAM crossbars, positioned against the well-known ISAAC baseline and the more recent PIM-Prune sparsity accelerator; its distinguishing idea is treating sparsity at bit-level granularity (both static weight bits via adaptive bit-flipping/exponent quantization, and dynamic activation bits via crossbar-aware pruning) rather than at the tensor/channel level. The headline multiplicative gains (up to 78x) are large enough to warrant scrutiny of baseline fidelity once the full text is available; this entry should be revisited with full text if accuracy-critical mapping comparisons are needed.

## Cites (in collection, 9)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2018_Chen_65nm1MbReRAMMacro_ISSCC](2018_Chen_65nm1MbReRAMMacro_ISSCC.md) 65nm 1Mb ReRAM nvCIM Macro (2018)
- [2018_Liang_CrossbarAwarePruning_IEEEAccess](2018_Liang_CrossbarAwarePruning_IEEEAccess.md) Crossbar-Aware Pruning (2018)
- [2019_Ankit_PUMA_ASPLOS](2019_Ankit_PUMA_ASPLOS.md) PUMA (2019)
- [2019_Chou_CASCADE_MICRO](2019_Chou_CASCADE_MICRO.md) CASCADE (2019)
- [2021_Yuan_FORMS_ISCA](2021_Yuan_FORMS_ISCA.md) FORMS (2021)
- [2021_Liu_BitTransformer_ICCAD](2021_Liu_BitTransformer_ICCAD.md) Bit-Transformer (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2023_Liu_ERABS_TC.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tc.2023.3290869
