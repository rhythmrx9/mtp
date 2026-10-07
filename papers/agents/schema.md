# Schema & controlled vocabularies

## Card front-matter / `catalog.jsonl` fields
| field | meaning |
|---|---|
| `id` | OpenAlex work ID (`W…`) — stable paper identifier |
| `key` | file key `{year}_{FirstAuthor}_{ShortName}_{Venue}`; same for card, full text, PDF |
| `short`, `title`, `year`, `venue`, `venue_full`, `authors`, `doi` | bibliographic data |
| `category` / `cat` | folder category, see below |
| `devices` | memory/compute technology used (vocabulary below) |
| `models` | workload model families evaluated |
| `lm_models`, `param_scale` | exact language models evaluated and their parameter range |
| `slm` | true if language models ≤ ~10B parameters are run/evaluated on (or under the noise of) analog/NVM in-memory hardware |
| `evidence` | strength/type of evidence (vocabulary below) |
| `topics` | 3–8 tags from the topic vocabulary |
| `analysis_basis` / `basis` | `full-text` (read from the PDF) or `abstract-only` (no full text available — unverified) |
| `in_original_review` / `seed` | cited by the seed literature review "Analog Silicon for Language Models" |
| `cited_by_in_collection`, `cites_in_collection` | citation counts **within this collection** |
| `citations_overall` | global citation count (OpenAlex, at collection time) |
| `priority_score` | importance × relevance score used to rank papers (category relevance, SLM focus, seed, in-collection citations, overall citations, recency, measured silicon) |
| `pdf`, `fulltext` | relative paths, or null |

Claims: `<key>#C<n>` (stable within a build; in `claims.jsonl` with `support` = number/quote and `loc` = section/figure/table).
Citations (`citations.jsonl`): `from` cites `to`; `context` = verbatim citing sentence from the citing paper; `purpose` ∈
background · motivation · baseline/comparison · uses-method-or-tool · extends/builds-on · contrasts/critiques · data/numbers.

## Categories (folders)
| id | folder | scope |
|---|---|---|
| 01 | 01_Surveys_and_Foundations | reviews, perspectives, foundations of IMC |
| 02 | 02_Fabricated_Chips_and_Macros | measured silicon: chips, CIM macros |
| 03 | 03_Crossbar_Accelerator_Architectures | ISAAC/PRIME/PipeLayer/PUMA-style crossbar accelerators |
| 04 | 04_Transformers_and_LLMs | transformer & attention accelerator architectures on CIM/PIM |
| 05 | 05_Mapping_Compilation_and_Dataflow | weight/layer mapping, tiling, compilers, scheduling, dataflow |
| 06 | 06_Nonidealities_and_Reliability | variation, drift, noise, IR drop, faults, programming |
| 07 | 07_Hardware_Aware_Training_and_Robustness | noise-aware training, calibration, NAS, robustness |
| 08 | 08_Simulation_and_Benchmarking_Frameworks | simulators, modelling tools, benchmarking |
| 09 | 09_ADCs_Peripherals_Quantization_Sparsity | ADC/DAC cost, quantization, pruning, sparsity |
| 10 | 10_On_Chip_and_Analog_Training | in-situ / analog training |
| 11 | 11_Small_Language_Models_on_AIMC | (small) language models on analog/NVM in-memory hardware |

## `evidence`
`measured-silicon` (results measured on a fabricated chip) > `device-experiment` (measured devices/arrays, rest simulated) >
`algorithm+simulation` / `simulation` (simulator or hardware model) > `analytical` > `survey` (review/perspective; projections are not results).

## `devices`
PCM · ReRAM · Memristor(generic) · FeFET · FeRAM · MRAM · ECRAM · Flash · SRAM-analog · SRAM-digital · Charge/Capacitor · Gain-cell · DRAM · Generic-NVM · None

## `models`
MLP · CNN · ResNet · VGG · MobileNet · LSTM/RNN · Transformer · BERT · ViT · GPT/LLM · MoE · GNN · Speech · SNN · Other

## `topics`
analog-mvm · crossbar-architecture · chip-demo · macro · weight-mapping · tiling-partitioning · compiler-software-stack ·
dataflow-pipelining · scheduling · nas-codesign · adc-dac · peripheral-circuits · quantization · mixed-precision ·
pruning-sparsity · bit-slicing · ir-drop-parasitics · device-variation · conductance-drift · read-write-noise · stuck-at-faults ·
endurance-retention · thermal · write-verify-programming · hardware-aware-training · noise-injection · chip-in-the-loop ·
calibration-compensation · on-chip-training · attention · kv-cache · transformer-accelerator · language-models ·
llm-adapters-lora · moe · nonlinear-functions · heterogeneous-analog-digital · 3d-integration · chiplets · simulator ·
benchmarking · survey · energy-efficiency · security-robustness · recurrent-models · cnn-accelerator · edge-ai
