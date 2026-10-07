# Topic: llm-adapters-lora

6 papers, most important first.

| key (→ card) | year | venue | cat | devices | evidence | basis | cited-by | TL;DR |
|---|---|---|---|---|---|---|---|---|
| [2026_Li_AHWA-LoRA_NeuromorphComputEng](../cards/2026_Li_AHWA-LoRA_NeuromorphComputEng.md) | 2026 | NeuromorphComputEng | 11 | PCM | algorithm+simulation | F | 0 | AHWA-LoRA keeps pretrained transformer weights fixed on PCM AIMC tiles and trains only digital LoRA adapters under simulated hardware noise, matching full hardw |
| [2026_Wu_HaLoRA_TODAES](../cards/2026_Wu_HaLoRA_TODAES.md) | 2026 | TODAES | 11 | ReRAM,SRAM-digital | algorithm+simulation | F | 2 | HaLoRA maps frozen pretrained LLM weights to noisy RRAM CIM and the LoRA branch to noise-free digital SRAM CIM, and trains the LoRA branch with a noise-trajecto |
| [2025_Dhingra_Atleus_TCAD](../cards/2025_Dhingra_Atleus_TCAD.md) | 2025 | TCAD | 04 | ReRAM,SRAM-digital | simulation | F | 3 | Atleus is a 3D heterogeneous edge accelerator that keeps frozen pre-trained transformer weights on ReRAM crossbars and runs dynamic attention products and LoRA  |
| [2021_Kang_AreaEfficientMultiTaskBERT_ICCAD](../cards/2021_Kang_AreaEfficientMultiTaskBERT_ICCAD.md) | 2021 | ICCAD | 11 | ReRAM | simulation | F | 2 | A training-free framework that stores one shared BERT base model plus heavily compressed task-specific deltas (near-ternary quantisation + output-channel hard-s |
| [2025_Chen_EdramRramZoFinetune_IMW](../cards/2025_Chen_EdramRramZoFinetune_IMW.md) | 2025 | IMW | 11 | RRAM,eDRAM (MOM, In2O3 FET gain cell) | simulation | A | 0 | Reliability-aware analog MLC eDRAM-RRAM CIM for zeroth-order LM fine-tuning, with 12x bit density over prior MLC eDRAM and further 5x density, 2x retention from |
| [2025_Qin_NVCiMPT_DATE](../cards/2025_Qin_NVCiMPT_DATE.md) | 2025 | DATE | 11 | ReRAM,FeFET | algorithm+simulation | F | 0 | NVCiM-PT stores per-sample optimal prompt-tuning virtual tokens (OVTs) in NVM crossbars with noise-aware training and retrieves them by an in-memory scaled sear |
