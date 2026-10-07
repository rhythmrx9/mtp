---
id: W4310449176
key: 2022_Wen_RRAMReadDisturb_DFT
title: "Evaluating Read Disturb Effect on RRAM based AI Accelerator with Multilevel States and Input Voltages"
short: "RRAM Read Disturb"
year: 2022
venue: "DFT"
venue_full: "IEEE International Symposium on Defect and Fault Tolerance in VLSI and Nanotechnology Systems (DFT 2022)"
authors: "Jianan Wen, Andrea Baroni, Eduardo Pérez, Markus Ulbricht, Christian Wenger, Milos D. Krstic"
category: "06 Non-idealities, Reliability & Fault Tolerance"
devices: ["ReRAM"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: device-experiment
topics: ["endurance-retention", "read-write-noise", "conductance-drift", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 5
citations_overall: 12
priority_score: 3.78
doi: "https://doi.org/10.1109/dft56152.2022.9962345"
pdf: null
fulltext: null
---

# RRAM Read Disturb

**Evaluating Read Disturb Effect on RRAM based AI Accelerator with Multilevel States and Input Voltages** — IEEE International Symposium on Defect and Fault Tolerance in VLSI and Nanotechnology Systems (DFT 2022) (2022)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Measures RRAM read-disturb-induced conductance drift at the device level and simulates its impact on LeNet-5/VGG-7 inference accuracy, finding that differential-pair weight mapping is more robust than single-device mapping.

## Summary
RRAM crossbars used for analog in-memory MAC computation suffer read disturb: repeated read operations with multilevel input voltages gradually drift device conductance and introduce errors over time. The authors measure this effect on fabricated RRAM devices with multilevel conductance states under different input (read) voltages, then feed the measured drift and device-to-device variability statistics into accuracy simulations of two CNN inference workloads, LeNet-5 on MNIST and VGG-7 on CIFAR-10. They compare single-device weight mapping against a differential-pair mapping scheme for robustness to the combined read-disturb and variability effects. The paper is a device-characterization-plus-system-simulation study rather than a full chip demonstration, aimed at quantifying how an underappreciated non-ideality (disturb from repeated analog reads, not just programming noise) degrades deployed DNN accuracy over operational lifetime.

## Contributions
- Experimental measurement of RRAM read disturb (conductance drift) as a function of input/read voltage and conductance level on real devices
- Incorporation of measured disturb statistics plus device-to-device variability into an accuracy simulation pipeline for CNN inference
- Benchmarking of LeNet-5/MNIST and VGG-7/CIFAR-10 under the combined non-ideality model
- Comparison of single-ended vs. differential-pair weight mapping schemes for disturb robustness

## Key claims (stable IDs)
- **2022_Wen_RRAMReadDisturb_DFT#C1** — Read disturb causes measurable conductance drift in RRAM devices that depends on applied input voltage and conductance state — _support:_ device measurements described in abstract/methodology — _loc:_ Sec. on device measurement (abstract-only, page unknown)
- **2022_Wen_RRAMReadDisturb_DFT#C2** — Differential-pair weight mapping is more robust to read disturb and device variability than direct/single mapping — _support:_ stated as main result in abstract — _loc:_ Results (abstract-only, page unknown)

## Results
- Qualitative result only available from abstract: differential-pair mapping yields better robustness to read disturb and variability than single-device mapping for LeNet-5/MNIST and VGG-7/CIFAR-10 (no specific accuracy numbers available without full text)

## Limitations
- Abstract-only basis: no numeric accuracy/drift figures available for this entry
- Short conference paper (DFT) — likely limited to a small number of device samples and two CNN benchmarks
- Read disturb is characterized for a specific RRAM technology; generalization to other oxide/device stacks is unclear

## Remarks
This is a device-level reliability study that complements the broader non-ideality/noise-robustness literature (ISAAC, PRIME-era architectures) by isolating read disturb specifically, which is distinct from programming/retention noise usually modeled in mapping-robustness papers. Without full text the quantitative strength of the claims (how much accuracy drop, over how many reads) cannot be verified here; the abstract indicates it is a measured-device-plus-simulation study, which gives it more credibility than a purely analytical treatment, but the finding (differential mapping helps) is consistent with and reinforces general practice in the field (e.g., differential encoding used in PCM/RRAM chips like IBM's analog AI core and Tsinghua's RRAM macro) rather than being a novel mapping technique itself.

## Cites (in collection, 5)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev](2020_Xiao_AnalogArchitecturesNVM_ApplPhysRev.md) Xiao Analog NVM Review (2020)
- [2021_Yu_CIMChipsDeepLearning_CASMag](2021_Yu_CIMChipsDeepLearning_CASMag.md) CIM Chips for Deep Learning (2021)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2016_Chi_PRIME_ISCA](2016_Chi_PRIME_ISCA.md) PRIME (2016)

## Files
- PDF: not available locally (save as `papers/06_Nonidealities_and_Reliability/2022_Wen_RRAMReadDisturb_DFT.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/dft56152.2022.9962345
