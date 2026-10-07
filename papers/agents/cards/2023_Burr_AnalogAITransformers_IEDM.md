---
id: W4391594670
key: 2023_Burr_AnalogAITransformers_IEDM
title: "Design of Analog-AI Hardware Accelerators for Transformer-based Language Models (Invited)"
short: "Burr-AnalogAI-LM-IEDM23"
year: 2023
venue: "IEDM"
venue_full: "IEEE International Electron Devices Meeting (IEDM), 2023 (invited)"
authors: "Geoffrey W. Burr, Hsinyu Tsai, William Simon, Irem Boybat, Stefano Ambrogio, C.-E. Ho, Z.-W. Liou, Malte J. Rasch, Julian Büchel, Pritish Narayanan, T. Gordon, Shilpa Jain et al."
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM", "SRAM-digital"]
models: ["Transformer", "BERT", "LSTM/RNN", "Speech"]
lm_models: ["BERT-base", "BERT-large", "ALBERT-base", "RoBERTa-base", "GPT-3 (as motivating example)"]
param_scale: "110M-340M (BERT-base/large modeled)"
slm: true
evidence: analytical
topics: ["language-models", "transformer-accelerator", "heterogeneous-analog-digital", "chip-demo", "hardware-aware-training", "dataflow-pipelining", "write-verify-programming", "energy-efficiency"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 2
cites_in_collection: 7
citations_overall: 10
priority_score: 9.66
doi: "https://doi.org/10.1109/iedm45741.2023.10413767"
pdf: "../../11_Small_Language_Models_on_AIMC/2023_Burr_AnalogAITransformers_IEDM.pdf"
fulltext: "../fulltext/2023_Burr_AnalogAITransformers_IEDM.txt"
---

# Burr-AnalogAI-LM-IEDM23

**Design of Analog-AI Hardware Accelerators for Transformer-based Language Models (Invited)** — IEEE International Electron Devices Meeting (IEDM), 2023 (invited) (2023)

## TL;DR
IBM invited review of PCM analog-AI accelerators for Transformer language models (architecture, wafer-scale testing, chip demos, HWA training), with a performance model showing fully weight-stationary (FWS) PCM systems deliver about 6x raw throughput and 7x lower latency than partially weight-stationary (PWS) SRAM-style CIM at similar TOPS/mm^2 and TOPS/W.

## Summary
The paper argues that large fully-connected layers (in-projection, out-projection, FC1, FC2) dominate Transformer LLM compute, so analog NVM tiles performing MAC through Ohm's and Kirchhoff's laws are well suited, while attention (scaling as S^2) and special functions remain in digital compute-cores. It describes the Analog Fabric: PCM tiles, heavy/light compute-cores, SRAM scratchpads and a circuit-switched 2D mesh with Border-Guard circuits; activations are converted to pulse durations and outputs digitized by current-controlled-oscillator ADCs. Because NVM is slow and endurance-limited to program, systems must be fully weight-stationary, with a unique device for every weight. A prior study found 40x-140x better energy efficiency than an A100 at batch 8. Wafer-scale testing screens PCM arrays by the sharpness of SET and RESET conductance CDFs (contrast >5x). Chip demos recapped: a 5-chip RNN-T with 45M weights on more than 140M PCM devices (less than 2% WER degradation on LibriSpeech, 14x estimated system benefit vs MLPerf GPU entries) and a 64-tile PCM chip running an LSTM image-captioning network with software-equivalent BLEU. HWA training results are summarized for RNN-T, BERT-base, ALBERT-base (less robust due to weight sharing) and RoBERTa-base on GLUE, with near-software-equivalent BERT-base accuracy until about one year of drift. A performance simulator compares FWS chiplet-stacked systems with a PWS SRAM-like system for BERT-base/large at S=128, b=8 assuming identical tile characteristics (100 TOPS/W, 40 ns integration, 8-bit activations, 4-bit equivalent weights).

## Language models evaluated
- Models: BERT-base, BERT-large, ALBERT-base, RoBERTa-base, GPT-3 (as motivating example)
- Scale: 110M-340M (BERT-base/large modeled)
- Note: Invited overview from IBM on analog-NVM (PCM) accelerators targeting the large fully-connected layers of Transformer-based LLMs; compute is analog in-memory MAC. Abstract-only: specific model sizes not verified; scope is BERT/LLM-class Transformers, with chip-demo evidence from IBM's PCM chips.

## Contributions
- Overview of Analog-AI accelerator design for Transformer LMs spanning architecture, wafer-scale test, chip demos and HWA training.
- Wafer-scale testing method for PCM analog arrays using SET/RESET CDF sharpness.
- Quantitative FWS vs PWS comparison on BERT-base and BERT-large.
- New HWA-training result for RoBERTa-base on GLUE.

## Key claims (stable IDs)
- **2023_Burr_AnalogAITransformers_IEDM#C1** — FWS systems give about 6x higher raw throughput and 7x faster latency than PWS while keeping TOPS/mm^2 and energy efficiency roughly equal. — _support:_ Table 3: 4.95x/6.02x faster, 6.75x/7.16x lower latency, 1.06x energy efficiency, 0.93-0.94x area efficiency, 5.3x/6.4x larger — _loc:_ Sec. VII, Table 3, Conclusion
- **2023_Burr_AnalogAITransformers_IEDM#C2** — Analog-AI architecture can be 40x-140x more energy efficient than NVIDIA A100 at batch 8. — _support:_ from prior study [16] — _loc:_ Sec. III
- **2023_Burr_AnalogAITransformers_IEDM#C3** — 5-chip RNN-T with 45M weights on >140M PCM devices achieved <2% WER degradation. — _support:_ Librispeech, 14x system benefit vs MLPerf GPU — _loc:_ Sec. V
- **2023_Burr_AnalogAITransformers_IEDM#C4** — HWA fine-tuning gives software-equivalent BERT-base GLUE accuracy up to about one year of PCM drift; ALBERT is less robust. — _support:_ Table 2 (values garbled in extraction) — _loc:_ Sec. VI, Table 2

## Results
- Tile assumption: 100 TOPS/W, 40 ns integration, 10.9 TOPS/mm^2 (matching/exceeding SRAM CIM tiles).
- FWS maximal throughput and efficiency reached at batch size as low as b=2 without padding short sequences.
- Expect same accuracy as digital systems using about 4-bit weights and 8-bit activations.

## Key numbers
- tech_node: 14nm (PCM tile circuit simulations)
- energy_eff: 100 TOPS/W tile; 40x-140x vs A100 (batch 8)
- throughput: FWS 4.95-6.02x higher than PWS; 7x lower latency
- accuracy: RNN-T <2% WER degradation; BERT-base GLUE near software up to 1 year drift
- bits_weight: 4b equivalent
- bits_adc: CCO-based ADC; 8b excitations

## Datasets / benchmarks
GLUE, LibriSpeech, Switchboard (SWB300), image captioning (BLEU)

## Limitations
- Invited overview with little new data; much is recap of IBM prior work.
- Performance model is analytical/simulated with assumed identical tile characteristics; no measured Transformer on silicon.
- Only BERT-class encoders modeled; GPT-scale decoders discussed qualitatively, and attention/KV handling stays digital.
- Table 2 numeric accuracy values are garbled in the extracted text.

## Remarks
Important framing for the collection: for PCM analog-AI, weights must be resident (FWS), which implies chiplet-scale tile counts for LMs but yields latency advantages that PWS SRAM-CIM cannot match. The claim rests on a simulator with identical tile specs, so it favors FWS by construction on throughput; area and energy parity is the actual finding. Complements Le Gallo's 64-core chip, Jain's fabric architecture and Rasch's HWA training in the collection.

## Cites (in collection, 7)
- [2021_Narayanan_FullyOnChipMAC14nmPCM_TED](2021_Narayanan_FullyOnChipMAC14nmPCM_TED.md) IBM 14nm PCM Analog AI Chip (2021) — _background_: "By exploiting such weight stationarity over short timespans with Volatile Memories (VMs) – SRAM or e-DRAM [6, 8] – or over longer timespans with slower, finite-endurance NonVolatile Memories (NVMs) – Flash [9], Resistive-RAM [10], or phase-change memory (PCM) [11, 12] – such CIM approaches can offer high throughput, low latency, and high energy-efficiency [6, 7, 8]."
- [2022_Khaddam-Aljameh_HERMES-Core_JSSC](2022_Khaddam-Aljameh_HERMES-Core_JSSC.md) HERMES-Core (2022) — _background_: "By exploiting such weight stationarity over short timespans with Volatile Memories (VMs) – SRAM or e-DRAM [6, 8] – or over longer timespans with slower, finite-endurance NonVolatile Memories (NVMs) – Flash [9], Resistive-RAM [10], or phase-change memory (PCM) [11, 12] – such CIM approaches can offer high throughput, low latency, and high energy-efficiency [6, 7, 8]."
- [2022_Shanbhag_IMCBenchmarking_OJSSCS](2022_Shanbhag_IMCBenchmarking_OJSSCS.md) IMC-Benchmarking (2022) — _background_: "Recently, numerous researchers are exploring Compute-In-Memory (CIM) approaches [6, 7, 8] to increase energy-efficiency by performing Multiply-Accumuate (MAC) operations within ON-chip memory “Tiles,” thus markedly reducing the motion of model-weights and partial sums."
- [2022_Jain_AnalogAI2DMesh_TVLSI](2022_Jain_AnalogAI2DMesh_TVLSI.md) Analog-AI-2DMesh (2022) — _extends/builds-on_: "We recently introduced a highly programmable Analog-AI and Compute-In-Memory accelerator architecture [16], which utilizes a highly specialized set of Compute-cores and Tiles arranged within a common building block known as an Analog Fabric (AF) (Fig. 2), together with SRAM scratchpads, IO blocks, and a 2D Mesh on top of the building blocks."
- [2023_LeGallo_IBMHERMESChip_NatElectron](2023_LeGallo_IBMHERMESChip_NatElectron.md) IBM HERMES 64-core (2023) — _data/numbers_: "On a second chip, we integrated CCO-based ADCs (one per integration-row) into PCM-based CIM-Tiles [21] (Fig. 5)."
- [2023_Ambrogio_IBMAnalogAISpeechChip_Nature](2023_Ambrogio_IBMAnalogAISpeechChip_Nature.md) IBM Analog-AI Speech Chip (RNNT) (2023) — _data/numbers_: "Recently, a large Recurrent Neural Network Tranducer (RNNT) model (Fig. 4a) was demonstrated [19], using 5 chips to encode 45M weights using >140M PCM devices."
- [2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun](2023_Rasch_HWATrainingLargeScaleAIMC_NatCommun.md) HWA Training for Large-scale AIMC (2023) — _data/numbers_: "HWA training can greatly enhance the robustness of a variety of deep neural networks (DNNs) including recurrent neural networks (RNNs), and transformers (Table 2) as well as convolutional neural networks (CNNs) (not shown here, see Ref [18, 21])."

## Cited by (in collection, 2)
- [2025_Tsai_AnalogAILLMAccelerators_IMW](2025_Tsai_AnalogAILLMAccelerators_IMW.md) Analog AI for LLMs (IBM IMW'25) (2025) — _data/numbers_: "Figure 1 shows an example of mapping one BERT Large layer onto the architecture [21], with projected 40-140x energy efficiency benefits compared to A100 GPUs."
- [2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng](2025_Lammie_AIMCSoftwareStacks_NatRevElectrEng.md) AIMC Software Stacks (2025)

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2023_Burr_AnalogAITransformers_IEDM.pdf](../../11_Small_Language_Models_on_AIMC/2023_Burr_AnalogAITransformers_IEDM.pdf)
- Full text: [../fulltext/2023_Burr_AnalogAITransformers_IEDM.txt](../fulltext/2023_Burr_AnalogAITransformers_IEDM.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.1109/iedm45741.2023.10413767
