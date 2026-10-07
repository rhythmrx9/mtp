---
id: W7166819412
key: 2026_Rahman_AttentionUnderAttack_ACL
title: "Attention Under Attack: Analog Noise Effects and Mechanistic Vulnerabilities in Transformer Models"
short: "AttentionUnderAttack"
year: 2026
venue: "ACL"
venue_full: "Annual Meeting of the Association for Computational Linguistics (ACL, short papers), 2026"
authors: "Mafizur Rahman, Lijun Qian"
category: "11 Small Language Models on Analog / NVM In-Memory Hardware"
devices: ["PCM", "ReRAM"]
models: ["BERT", "Transformer", "GPT/LLM"]
lm_models: ["BERT-base", "DistilBERT", "ALBERT", "RoBERTa-base", "DeBERTa-large", "Phi-3-mini", "Llama-3.2-1B (8-bit)"]
param_scale: "66M-1.3B (plus Phi-3-mini ~3.8B)"
slm: true
evidence: simulation
topics: ["language-models", "attention", "transformer-accelerator", "read-write-noise", "conductance-drift", "adc-dac", "noise-injection", "simulator"]
analysis_basis: full-text
in_original_review: false
cited_by_in_collection: 0
cites_in_collection: 0
citations_overall: 0
priority_score: 8.0
doi: "https://doi.org/10.18653/v1/2026.acl-short.21"
pdf: "../../11_Small_Language_Models_on_AIMC/2026_Rahman_AttentionUnderAttack_ACL.pdf"
fulltext: "../fulltext/2026_Rahman_AttentionUnderAttack_ACL.txt"
---

# AttentionUnderAttack

**Attention Under Attack: Analog Noise Effects and Mechanistic Vulnerabilities in Transformer Models** — Annual Meeting of the Association for Computational Linguistics (ACL, short papers), 2026 (2026)

## TL;DR
AIHWKIT (PCM-calibrated) simulation of pretrained NLP transformers shows 1-3 point drops on SST-2/MNLI, 3-6 point drops on SQuAD, and identifies Q/K/V projections and upper-layer attention as the most analog-noise-sensitive parts while FFNs are comparatively robust.

## Summary
The paper asks how analog in-memory noise perturbs internal attention behaviour of NLP transformers, which prior AIMC studies (mostly vision/CNN) ignore. All linear layers of pretrained BERT-base, DistilBERT, ALBERT, RoBERTa-base and DeBERTa-large are converted to AIHWKIT AnalogLinear modules (weights mapped to conductances, 256-size tiles, column-wise scaling, weight clip 1.0), with digital input quantized by DACs and ADC-digitized outputs summed across tiles; biases stay digital and global drift compensation is on. The noise config is fixed (weight-modifier std 0.05, read noise 0.0175, output noise 0.04, PCM programming/read/drift scaling 1.0), inference-only without noise-aware fine-tuning, three seeds. RQ1 benchmarks end-to-end accuracy on SST-2, MNLI and SQuAD v1.1 (plus Phi-3-mini and Llama-3.2-1B 8-bit on ARC-Easy zero-shot at three noise levels). RQ2 isolates one submodule at a time (others made ideal) and measures per-head KL divergence and attention-entropy shift versus digital. Results: encoder classification drops 1-3 points, SQuAD 3-6, decoder LLMs 2-3% at medium noise and up to ~7% at high; Q/K/V most vulnerable, divergence grows monotonically with depth and attention becomes more diffuse (positive entropy shift).

## Language models evaluated
- Models: BERT-base, DistilBERT, ALBERT, RoBERTa-base, DeBERTa-large, Phi-3-mini, Llama-3.2-1B (8-bit)
- Scale: 66M-1.3B (plus Phi-3-mini ~3.8B)
- Note: AIHWKIT (PCM-calibrated) simulation of analog noise on BERT-base, DistilBERT, ALBERT, RoBERTa, DeBERTa-large, plus Phi-3-mini and Llama-3.2-1B (8-bit) on ARC-Easy. Analog MVM in crossbars, linear layers only.

## Contributions
- First fine-grained study of analog-noise vulnerability inside pretrained NLP transformers (submodule, head, layer level)
- Submodule isolation protocol: noise applied to one projection type while all others are ideal
- Attention-level metrics (per-head KL divergence, entropy shift) linking noise to attention scattering
- Extension to decoder LLMs (Phi-3-mini, Llama-3.2-1B) on ARC-Easy at three noise levels

## Key claims (stable IDs)
- **2026_Rahman_AttentionUnderAttack_ACL#C1** — Q, K and V projections are the most noise-sensitive submodules across tasks and architectures; FFN layers are comparatively robust. — _support:_ largest drops when isolated; FFN smaller degradation on SST-2/MNLI — _loc:_ RQ2, Fig. 2
- **2026_Rahman_AttentionUnderAttack_ACL#C2** — Analog degradation grows with task difficulty: classification 1-3 pts, SQuAD 3-6 pts. — _support:_ e.g. MNLI BERT 84->83, RoBERTa 87->85, DeBERTa 91->89; SQuAD drops 3-6 F1/EM — _loc:_ Table 1
- **2026_Rahman_AttentionUnderAttack_ACL#C3** — Attention vulnerability concentrates in higher layers and analog noise scatters attention. — _support:_ layer-wise KL grows monotonically with depth; more heads have positive entropy change — _loc:_ Fig. 3b-c (RoBERTa SQuAD)
- **2026_Rahman_AttentionUnderAttack_ACL#C4** — Decoder LLM degradation scales smoothly with noise: ~1-3 pts at low/medium, up to ~7 at high. — _support:_ Phi-3 -1.3/-2.6/-7.1; Llama-3.2-1B -1.4/-2.6/-6.4 across modifier std 0.025/0.05/0.10 — _loc:_ Table 2

## Results
- Encoder models lose 1-3 points on SST-2 and MNLI under medium noise (Table 1), with DeBERTa MNLI loss rising 0.48 -> 1.40
- SQuAD: RoBERTa and DeBERTa lose 3-6 points in both F1 and EM
- ARC-Easy zero-shot: Phi-3-mini drops 1.3/2.6/7.1 and Llama-3.2-1B 1.4/2.6/6.4 points at 0.5x/1x/2x noise (Table 2)
- Layer-wise KL divergence between digital and analog attention rises monotonically with depth, peaking in final layers

## Key numbers
- array_size: 256 tile size
- accuracy: BERT MNLI 84->83; Phi-3-mini ARC-Easy -2.6 pts at medium noise

## Datasets / benchmarks
SST-2, MNLI, SQuAD v1.1, ARC-Easy

## Limitations
- Simulation only (AIHWKIT), no fabricated hardware; authors say trends are indicative, not absolute
- Single fixed noise configuration for encoders; no noise-aware training or mitigation evaluated
- Decoder evidence is thin: one benchmark (ARC-Easy), two models, no perplexity or generation metrics
- No energy or latency measurements
- Reported numbers rounded to integers in Table 1; table text extraction is partly garbled

## Remarks
A cheap diagnostic of where to protect transformer weights (Q/K/V projections, upper layers) when mapping small language models to PCM-like crossbars, consistent with intuition that attention is noise-sensitive. Evidence is simulator-only and mitigation is left open, so it motivates rather than demonstrates selective digital fallback or hardware-aware training; compare with hardware-aware training and measured-chip LM papers in the collection.

## Files
- PDF: [../../11_Small_Language_Models_on_AIMC/2026_Rahman_AttentionUnderAttack_ACL.pdf](../../11_Small_Language_Models_on_AIMC/2026_Rahman_AttentionUnderAttack_ACL.pdf)
- Full text: [../fulltext/2026_Rahman_AttentionUnderAttack_ACL.txt](../fulltext/2026_Rahman_AttentionUnderAttack_ACL.txt) (page markers `=== page N ===`)
- DOI: https://doi.org/10.18653/v1/2026.acl-short.21
