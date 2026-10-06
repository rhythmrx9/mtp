# Analog AI hardware — paper collection

A curated, citation-linked collection of **274 peer-reviewed papers** on running AI models on analog / in-memory
hardware (PCM, ReRAM/memristor crossbars, charge-domain CIM) and on **mapping models onto crossbar arrays**.

**Start here: open [`index.html`](index.html) in a browser.** It works offline (no server needed) and has:

- **Citation graph**: every paper as a node, coloured by category, with arrows from citing paper to cited paper.
  *Network* view clusters papers by category. *Timeline* view puts years on x and categories in lanes.
  Click a node to open its panel.
- **Paper panel**: TL;DR, summary, contributions, key claims (each with its supporting number and section),
  results, limitations, critical remarks, then two lists. *Cites in this collection* gives the exact sentence where
  this paper cites each one and why (background, baseline, builds on…). *Cited by in this collection* gives the
  sentence where each later paper cites it. Links to the local PDF, the DOI and OpenAlex.
- **Library**: a sortable table per category folder.
- **Categories**: what each folder covers, its most-cited and newest papers, and which other categories it draws on.
- **Review findings**: the 15 verified findings and 5 refuted claims from the original "Analog Silicon for Language
  Models" review, each linked to the papers it rests on.

## Folder layout

| Folder | What's in it |
|---|---|
| `01_Surveys_and_Foundations/` | Reviews and perspectives: the memory wall, device requirements, the state of analog AI |
| `02_Fabricated_Chips_and_Macros/` | Measured silicon: PCM/RRAM chips, ISSCC/JSSC CIM macros, Nature-family demonstrations |
| `03_Crossbar_Accelerator_Architectures/` | ISAAC, PRIME, PipeLayer, PUMA and later tile/pipeline/ISA architectures |
| `04_Transformers_and_LLMs/` | Transformer & attention accelerator architectures on crossbars/CIM/PIM: dynamic operands, write endurance, hybrid and 3D designs |
| `05_Mapping_Compilation_and_Dataflow/` | Weight/layer mapping, tiling, crossbar allocation, compilers, scheduling, dataflow |
| `06_Nonidealities_and_Reliability/` | Variation, drift, noise, IR drop, stuck-at faults, thermal effects, write-verify |
| `07_Hardware_Aware_Training_and_Robustness/` | Noise-aware training, fine-tuning, drift regularisation, analog NAS, calibration |
| `08_Simulation_and_Benchmarking_Frameworks/` | NeuroSim, MNSIM, AIHWKit, RxNN, GENIEx, CiMLoop; analog-vs-digital benchmarking |
| `09_ADCs_Peripherals_Quantization_Sparsity/` | ADC cost, ADC-less designs, partial-sum and mixed-precision quantization, pruning |
| `10_On_Chip_and_Analog_Training/` | In-situ / analog training, mixed-precision training, training accelerators |
| `11_Small_Language_Models_on_AIMC/` | **Small language models on analog / NVM in-memory hardware**: BERT-family, GPT-2, Llama-1B–8B, Phi, ternary/1-bit LLMs and KV caches on PCM, ReRAM, FeFET/FeRAM, MRAM and gain cells (chips, hardware-aware training, adapters, noise robustness, accelerators). Each paper's panel lists the exact models and parameter scale tested. |

Each folder has a `README.md` table: year, paper, venue, one-line TL;DR, and a link to the PDF (or its DOI).

PDFs are named `{year}_{FirstAuthor}_{ShortName}_{Venue}.pdf`, e.g. `2016_Shafiee_ISAAC_ISCA.pdf`.

## Missing PDFs

Only papers with a legitimate open copy (publisher open access, arXiv, author or institutional pages) were
downloaded. Most IEEE Xplore and ACM DL papers are paywalled. [`_data/missing_pdfs.md`](_data/missing_pdfs.md) lists
each missing paper with its DOI and the exact path to save it under, **ranked by importance and relevance** (priority tier + a one-line reason), so you know what to download first. After you download some through your
institution, run:

```
python3 _tools/build_index.py
```

The index will then link to them.

## How the collection was built

1. **Seeds**: the peer-reviewed sources of the "Analog Silicon for Language Models" review
   (claude.ai artifact). Its arXiv-only preprints, blogs and trade press were dropped.
2. **Expansion, hop 1**: every reference of every seed, plus every paper citing a seed (OpenAlex).
3. **Expansion, hop 2**: every paper citing one of the important hop-1 papers. These are relevant, highly cited
   works such as ISAAC, PRIME, PipeLayer, PUMA and NeuroSim.
4. **Filtering**: about 13,000 candidates were filtered three ways:
   - **Venue**: IEEE/ACM journals and conferences, Nature/Science family, NeurIPS/ICML/ICLR, DATE/DAC/ICCAD/ISCA/
     MICRO/HPCA/ASPLOS, ISSCC/IEDM/VLSI, and a few established Wiley/AIP/IOP journals. arXiv-only, MDPI, Frontiers
     and similar were excluded.
   - **Relevance**: the paper needs both a hardware term and an AI term, plus a mapping/architecture term.
   - **Curation by hand**: digital SRAM/DRAM-PIM, graph processing and materials-only device papers were dropped.
     Must-have classics were added: Prezioso 2015, Ambrogio 2018, Yao 2020, MNSIM, Haensch 2019.
5. **Analysis**: each paper's full text (or its abstract where no open copy exists, flagged *abstract-based* in the
   page) was read for summary, claims, results, limitations and remarks. In-collection citation sentences were
   extracted from the bibliography numbering of the citing paper.

6. **SLM extension (Oct 2026)**: an added search for small/large language models on analog and NVM in-memory hardware.
   It combined about 30 OpenAlex queries, the citers and references of the LLM-on-AIMC papers already in the collection, and web searches.
   The candidates were filtered to reputable venues (Crossref-verified) and to analog/NVM hardware, which excluded digital SRAM/DRAM/in-flash designs.
   This added 24 papers. 20 existing papers whose focus is deploying language models moved from folder 04 into the new folder 11.
   Notable arXiv-only preprints were left out by the venue rule; see the note at the end of `11_Small_Language_Models_on_AIMC/README.md`.

`_data/library.json` holds all of this as one machine-readable file. `_tools/build_index.py` regenerates the index data,
every folder README and the ranked missing-PDF table from it.
