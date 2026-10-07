---
id: W4416429523
key: 2025_Jeon_OptiRange_ICCAD
title: "OptiRange: An Efficient ReRAM-Based PIM Accelerator with ADC Resolution Optimization"
short: "OptiRange"
year: 2025
venue: "ICCAD"
venue_full: "IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2025)"
authors: "Seong-Won Jeon, Gisan Ji, Yeonggeon Kim, Youngjun Park, Sangyeon Kim, Sungju Ryu"
category: "09 ADCs, Peripherals, Quantization & Sparsity"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: simulation
topics: ["adc-dac", "crossbar-architecture", "peripheral-circuits", "energy-efficiency", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 8
citations_overall: 0
priority_score: 3.0
doi: "https://doi.org/10.1109/iccad66269.2025.11240769"
pdf: null
fulltext: null
---

# OptiRange

**OptiRange: An Efficient ReRAM-Based PIM Accelerator with ADC Resolution Optimization** — IEEE/ACM International Conference on Computer-Aided Design (ICCAD 2025) (2025)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
OptiRange is a ReRAM PIM accelerator that lowers ADC resolution/energy without hurting accuracy or throughput by rebalancing crossbar cell values (split-the-burden) and dynamically adapting the ADC's operating range per column at runtime.

## Summary
The paper targets the ADC energy/throughput tradeoff in ReRAM-based processing-in-memory (PIM) DNN accelerators: existing approaches that lower ADC resolution or share ADCs across columns save energy but hurt throughput. OptiRange introduces a 'split-the-burden' (STB) algorithm that manipulates crossbar cell values (without changing the represented weights) to shrink large cell values and recenter the column-sum distribution near zero, which reduces the number of low-resistance-state cells and lets the hardware use a lower fixed ADC resolution while preserving accuracy. On top of this, a dynamic ADC range (DAR) mechanism picks the optimal ADC operating range per column at the software level at runtime, skipping redundant ADC conversion cycles, and an ADC range-based grouping (AG) strategy manages synchronization across columns with different dynamic latencies to keep system throughput high. Together these weight-preserving cell manipulation and adaptive ADC techniques are evaluated against conventional ReRAM-based accelerators in simulation, showing improved overall performance (energy and throughput) while maintaining accuracy and model flexibility.

## Contributions
- Split-the-burden (STB) algorithm that reshapes crossbar cell-value/column-sum distributions without altering represented weights, enabling lower fixed ADC resolution
- Dynamic ADC range (DAR) adaptation that selects per-column ADC operating ranges at runtime and skips redundant conversion cycles
- ADC range-based grouping (AG) strategy to manage the resulting variable per-column latencies and preserve system throughput
- Combines these into OptiRange, an accelerator design claimed to jointly improve ADC energy efficiency and throughput versus prior resolution-reduction/ADC-sharing methods

## Key claims (stable IDs)
- **2025_Jeon_OptiRange_ICCAD#C1** — STB's cell manipulation lowers the hardware-level fixed ADC resolution needed while improving accuracy relative to unmodified mapping — _support:_ Abstract states STB 'significantly lowers the hardware-level fixed ADC resolution and improving accuracy' — _loc:_ Abstract
- **2025_Jeon_OptiRange_ICCAD#C2** — OptiRange achieves better energy efficiency and throughput jointly, unlike prior methods that trade one for the other — _support:_ Abstract: 'enhances both energy efficiency and throughput while maintaining accuracy and model flexibility' — _loc:_ Abstract

## Results
- No specific quantitative speedup/energy numbers available from the abstract alone; full text was not accessible

## Limitations
- Full text not accessible to this reviewer (no open preprint found); specific experimental numbers, baselines, and benchmark models could not be verified beyond the abstract
- Evidence basis is simulation; no fabricated silicon reported

## Remarks
Abstract-only assessment: a legitimate open copy could not be located (ICCAD proceedings are not downloadable from this environment and no arXiv preprint was found). The core idea — reshaping cell/column-sum distributions to cut required ADC resolution, then adaptively narrowing the per-column ADC range at runtime — is a reasonable and fairly novel combination of a weight-preserving mapping trick with dynamic ADC control, addressing a well-known ADC energy/throughput bottleneck in ReRAM crossbar accelerators (as in ISAAC-style designs). Without the full text, the magnitude of the claimed gains and the fairness of the baseline comparisons cannot be independently verified.

## Cites (in collection, 8)
- [2017_Song_PipeLayer_HPCA](2017_Song_PipeLayer_HPCA.md) PipeLayer (2017)
- [2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC](2020_Liu_FullyIntegratedAnalogReRAMCIM_ISSCC.md) Liu ISSCC'20 Analog ReRAM CIM (2020)
- [2021_Rasch_AIHWKIT_AICAS](2021_Rasch_AIHWKIT_AICAS.md) AIHWKit (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2022_Wan_NeuRRAM_Nature](2022_Wan_NeuRRAM_Nature.md) NeuRRAM (2022)
- [2023_Andrulis_RAELLA_ISCA](2023_Andrulis_RAELLA_ISCA.md) RAELLA (2023)
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023)
- [2024_Rasch_cTTv2AGADTraining_NatCommun](2024_Rasch_cTTv2AGADTraining_NatCommun.md) c-TTv2/AGAD (2024)

## Files
- PDF: not available locally (save as `papers/09_ADCs_Peripherals_Quantization_Sparsity/2025_Jeon_OptiRange_ICCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/iccad66269.2025.11240769
