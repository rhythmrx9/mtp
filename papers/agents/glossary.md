# Glossary, abbreviations & search synonyms

Papers use many names for the same thing. **When searching, grep all synonyms** (case-insensitive), e.g.
`grep -i -E 'reram|rram|memristi|resistive (random|switching)' agents/catalog.jsonl`.

## Computing paradigms
| term | meaning | synonyms to grep |
|---|---|---|
| IMC / CIM | in-memory computing / compute-in-memory: compute inside the memory array | `in-memory comput`, `compute-in-memory`, `computing-in-memory`, `CIM`, `IMC` |
| AIMC | analog IMC: MVM via Ohm's + Kirchhoff's laws on a conductance crossbar | `analog in-memory`, `analogue`, `AIMC`, `analog AI` |
| DIMC / digital CIM | bit-wise digital logic inside/near SRAM arrays | `digital CIM`, `DCIM`, `bit-serial` |
| PIM | processing-in-memory; often DRAM/HBM near-bank logic (digital) — not necessarily analog | `processing-in-memory`, `PIM`, `near-memory`, `NMC` |
| MVM / VMM / MAC | matrix-vector multiply / vector-matrix multiply / multiply-accumulate | `MVM`, `VMM`, `MAC`, `dot product` |
| crossbar | 2-D array of devices at row/column intersections storing a weight matrix | `crossbar`, `xbar`, `array`, `tile`, `core` |
| tile / core | one crossbar + its periphery (DAC, ADC, accumulators) | `tile`, `core`, `macro`, `PE` |
| weight stationary | weights stay programmed in arrays; only activations move | `weight-stationary`, `fully weight stationary` |

## Devices
| term | meaning | synonyms |
|---|---|---|
| PCM | phase-change memory (chalcogenide, e.g. GST); suffers conductance drift | `PCM`, `phase-change`, `phase change`, `PCRAM` |
| ReRAM | resistive RAM (metal-oxide filament) | `ReRAM`, `RRAM`, `memristor`, `memristive`, `OxRAM`, `resistive switching` |
| FeFET / FeRAM / FTJ | ferroelectric transistor / capacitor memory / tunnel junction | `FeFET`, `FeRAM`, `ferroelectric`, `HZO`, `FTJ`, `FeCap` |
| MRAM | magnetic RAM (STT/SOT) — binary, low on/off ratio | `MRAM`, `STT`, `SOT`, `spintronic` |
| ECRAM | electrochemical RAM — near-linear, symmetric updates (training) | `ECRAM`, `electrochemical` |
| gain cell | 2-3T capacitor-based volatile analog storage | `gain cell`, `gain-cell`, `eDRAM` |
| 1T1R / 2T2R / differential pair | access-transistor cell structures; differential pairs encode signed weights | `1T1R`, `2T2R`, `differential` |
| SLC / MLC | single-/multi-level cell (bits per device) | `SLC`, `MLC`, `multi-level`, `multibit` |

## Non-idealities
| term | meaning | synonyms |
|---|---|---|
| conductance drift | PCM conductance decays ~ t^-ν after programming | `drift`, `temporal drift`, `GDC` (global drift compensation) |
| read noise / programming noise | stochastic read fluctuation / error when writing a target conductance | `read noise`, `programming noise`, `write noise`, `1/f` |
| device variation | device-to-device / cycle-to-cycle spread | `variation`, `variability`, `D2D`, `C2C`, `stochastic` |
| IR drop | voltage drop along wires (parasitic resistance) | `IR drop`, `IR-drop`, `parasitic`, `wire resistance`, `line resistance`, `sneak path` |
| SAF | stuck-at fault (stuck-at-on / stuck-at-off) | `stuck-at`, `SAF`, `SA0`, `SA1`, `defect` |
| endurance / retention | max write cycles / how long a state lasts | `endurance`, `retention`, `relaxation`, `read disturb` |
| write-verify | iterative program-and-verify to hit a target conductance | `write-verify`, `program-verify`, `closed-loop programming`, `tuning` |

## Peripherals & precision
| term | meaning | synonyms |
|---|---|---|
| ADC / DAC | analog↔digital converters at array outputs/inputs — often dominant area/energy | `ADC`, `DAC`, `SAR`, `flash ADC`, `CCO`, `TDC`, `sense amp` |
| bit-slicing / bit-serial | splitting weights over devices / inputs over cycles | `bit-slic`, `bit-serial`, `shift-and-add` |
| partial sum | per-array output that must be accumulated digitally | `partial sum`, `psum` |
| TOPS/W, TOPS/mm² | energy efficiency / area efficiency | `TOPS/W`, `TOPS/mm`, `GOPS`, `EDP` |

## Training & robustness
| term | meaning | synonyms |
|---|---|---|
| HWA training | hardware-aware training: inject device noise/quantization during training | `hardware-aware`, `HWA`, `noise injection`, `noise-aware`, `variation-aware` |
| chip-in-the-loop | fine-tuning with measurements from the actual chip | `chip-in-the-loop`, `in-situ`, `on-chip fine-tun` |
| in-situ / on-chip training | weight updates performed in the analog array | `in-situ training`, `on-chip training`, `Tiki-Taka`, `outer product` |
| AIHWKit | IBM Analog Hardware Acceleration Kit (PyTorch simulator) | `aihwkit`, `AIHWKIT` |
| NeuroSim / MNSIM | circuit-level CIM benchmarking simulators | `NeuroSim`, `MNSIM`, `CiMLoop` |

## Language models
| term | meaning | synonyms |
|---|---|---|
| SLM | small language model (≈ ≤10B params: BERT-family, GPT-2, Llama-1B–8B, Phi, Qwen-small, Gemma) | `small language model`, `SLM`, `on-device LLM`, `edge LLM` |
| LLM | large language model | `LLM`, `language model`, `GPT`, `Llama`, `OPT`, `decoder` |
| KV cache | stored keys/values of past tokens in autoregressive decoding (dynamic, write-heavy) | `KV cache`, `KV-cache`, `key-value` |
| dynamic MVM | attention products where both operands change per input → crossbar rewrites | `dynamic`, `QK^T`, `MVM_Dynamic`, `compute-write-compute` |
| LoRA / adapters | small trainable low-rank modules on frozen weights | `LoRA`, `adapter`, `low-rank` |
| MoE | mixture of experts | `MoE`, `mixture of experts`, `expert` |
| ternary / 1-bit LLM | {-1,0,+1} or binary weights (e.g. BitNet b1.58) | `ternary`, `1-bit`, `1.58`, `BitNet` |
