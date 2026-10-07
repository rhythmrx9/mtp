---
id: W4390576773
key: 2024_Bai_eFlashIMCSoC_TCAD
title: "An End-to-End In-Memory Computing System Based on a 40-nm eFlash-Based IMC SoC: Circuits, Toolchains, and Systems Co-Design Framework"
short: "eFlash IMC SoC Toolchain"
year: 2024
venue: "TCAD"
venue_full: "IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems"
authors: "Tianshuo Bai, Wanru Mao, Guangyao Wang, Hanjie Liu, Aifei Zhang, Shihang Fu, Shuaikai Liu, Jianchao Hu, Xitong Yang, Biao Pan, Wei W. Xing, Wang Kang"
category: "02 Fabricated Chips & Macros"
devices: ["Flash"]
models: ["CNN"]
lm_models: []
param_scale: ""
slm: false
evidence: measured-silicon
topics: ["chip-demo", "compiler-software-stack", "quantization", "weight-mapping", "cnn-accelerator"]
analysis_basis: abstract-only
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 7
citations_overall: 12
priority_score: 5.88
doi: "https://doi.org/10.1109/tcad.2024.3349502"
pdf: null
fulltext: null
---

# eFlash IMC SoC Toolchain

**An End-to-End In-Memory Computing System Based on a 40-nm eFlash-Based IMC SoC: Circuits, Toolchains, and Systems Co-Design Framework** — IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems (2024)

> ⚠ Analysis based on the abstract only (no full text was available). Treat claims/numbers below as unverified.

## TL;DR
Presents an end-to-end circuit-toolchain-system co-design framework (QAT quantization, operator optimization, and ILP-based mapping) for a 40nm eFlash-based in-memory-computing SoC, validated on real voice-recognition, speech-noise-reduction, and person-detection tasks on fabricated silicon.

## Summary
The paper addresses the practical gap between IMC (in-memory computing) chip technology and usable deployment toolchains for real applications: without efficient toolchains, canonical DNNs cannot be reliably mapped onto IMC chips at production quality. The authors propose a co-designed framework spanning circuit, toolchain, and system layers: (a) an 8-bit hardware-friendly Quantization-Aware Training (QAT) method converting floating-point networks to fixed-point for the eFlash IMC array, (b) an operator optimization technique to raise computing precision when executing models on the IMC chip (addressing array/device nonidealities), and (c) an Integer-Linear-Programming (ILP)-based mapping strategy to improve utilization of the IMC array's computation resources. The framework is evaluated end-to-end on the authors' own fabricated 40nm eFlash-based IMC SoC across three real edge-AI tasks: voice recognition, speech noise reduction, and person detection, demonstrating that the co-design stack delivers competitive accuracy directly on silicon.

## Contributions
- Proposes an integrated circuit + toolchain + system co-design framework targeting a specific fabricated eFlash IMC SoC, rather than a software-only or simulation-only mapping tool
- 8-bit hardware-friendly Quantization-Aware Training (QAT) scheme tailored to IMC array fixed-point constraints
- An operator optimization technique to recover computing precision lost to IMC array nonidealities
- An ILP-based mapping strategy to improve utilization of IMC array compute resources
- End-to-end validation across three distinct real applications (voice recognition, speech noise reduction, person detection) on real 40nm eFlash IMC silicon

## Key claims (stable IDs)
- **2024_Bai_eFlashIMCSoC_TCAD#C1** — The proposed QAT + operator-optimization + ILP-mapping toolchain achieves over 94.60% voice recognition accuracy in a quiet environment on the fabricated 40nm eFlash IMC SoC. — _support:_ measured accuracy figure — _loc:_ Experimental results section
- **2024_Bai_eFlashIMCSoC_TCAD#C2** — Voice recognition accuracy remains at 87.27% under white-noise conditions on the chip. — _support:_ measured accuracy figure — _loc:_ Experimental results section
- **2024_Bai_eFlashIMCSoC_TCAD#C3** — False recognition rate for voice recognition is below 1 per 24 hours on the fabricated chip. — _support:_ measured false-recognition-rate figure — _loc:_ Experimental results section
- **2024_Bai_eFlashIMCSoC_TCAD#C4** — The framework improves Perceptual Evaluation of Speech Quality (PESQ) for noise reduction by 21.53%. — _support:_ measured PESQ improvement — _loc:_ Experimental results section
- **2024_Bai_eFlashIMCSoC_TCAD#C5** — Person detection achieves 97.80% accuracy on the fabricated IMC SoC. — _support:_ measured accuracy figure — _loc:_ Experimental results section

## Results
- Voice recognition: >94.60% accuracy (quiet), 87.27% accuracy (white noise), <1 false recognition per 24 hours, on 40nm eFlash IMC SoC silicon
- Speech noise reduction: 21.53% PESQ improvement
- Person detection: 97.80% accuracy

## Limitations
- Full text not available for this analysis; results summarized here are taken verbatim from the abstract and not independently verified against tables/figures or compared quantitatively with a floating-point/digital baseline
- Evaluated tasks (voice recognition, speech noise reduction, person detection) are relatively small edge-AI workloads; scalability to larger CNNs/transformers on this eFlash platform is not addressed in the abstract
- Device technology (eFlash) nonidealities (retention, endurance, programming granularity) and their quantitative impact are not detailed in the abstract

## Remarks
This paper is notable for being an industrial-style, full-stack (circuit+toolchain+system) demonstration on a genuinely fabricated eFlash IMC SoC rather than a pure simulation study, which strengthens its evidentiary value for the thesis's mapping/compilation chapter as a real deployment case study. However, because only the abstract was reviewed, the specific contributions of the ILP-mapping and operator-optimization techniques relative to simpler baselines, and the degree of accuracy loss relative to floating-point models, could not be assessed and should be checked in the full TCAD 2024 text before being cited in detail.

## Cites (in collection, 7)
- [2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron](2018_Ielmini_IMCResistiveSwitchingDevices_NatElectron.md) Ielmini-Wong IMC review (2018)
- [2018_Zhu_MISCA_ICCAD](2018_Zhu_MISCA_ICCAD.md) MISCA (2018)
- [2020_Joshi_PCMNoiseInject_NatCommun](2020_Joshi_PCMNoiseInject_NatCommun.md) Joshi PCM Inference (2020)
- [2020_Yao_FullyHardwareMemristorCNN_Nature](2020_Yao_FullyHardwareMemristorCNN_Nature.md) Tsinghua mCNN (2020)
- [2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol](2020_Sebastian_MemoryDevicesInMemoryComputing_NatNanotechnol.md) Sebastian IMC Review (2020)
- [2016_Shafiee_ISAAC_ISCA](2016_Shafiee_ISAAC_ISCA.md) ISAAC (2016)
- [2022_Mackin_WeightProgrammingOptimisation_NatCommun](2022_Mackin_WeightProgrammingOptimisation_NatCommun.md) DWE Weight Programming (2022)

## Files
- PDF: not available locally (save as `papers/02_Fabricated_Chips_and_Macros/2024_Bai_eFlashIMCSoC_TCAD.pdf`)
- Full text: none
- DOI: https://doi.org/10.1109/tcad.2024.3349502
