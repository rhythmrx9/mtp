# 03 · Crossbar Accelerator Architectures

Architecture-level designs that build DNN accelerators out of crossbar tiles (ISAAC, PRIME, PipeLayer, PUMA and successors): tiles, pipelines, ISAs, heterogeneous analog+digital systems.

16 papers. Open `../index.html` for summaries, claims, remarks and citation contexts.

| Year | Paper | Venue | TL;DR | File |
|---|---|---|---|---|
| 2024 | **** Heterogeneous Embedded Neural Processing Units Utilizing PCM-Based Analog In-Memory Computing |  |  | [DOI](https://doi.org/10.1109/iedm50854.2024.10873479) (no open PDF) |
| 2023 | **** End-to-End DNN Inference on a Massively Parallel Analog In Memory Computing Architecture |  |  | [2023_Bruschi_EndToEndDnnInference.pdf](2023_Bruschi_EndToEndDnnInference.pdf) |
| 2022 | **** A Heterogeneous In-Memory Computing Cluster for Flexible End-to-End Inference of Real-World Deep Neural Networks | IEEE Journal on Emerging and Selected Topics in Circuits and Systems |  | [2022_Garofalo_AHeterogeneousInMemoryComputing.pdf](2022_Garofalo_AHeterogeneousInMemoryComputing.pdf) |
| 2022 | **** A Heterogeneous and Programmable Compute-In-Memory Accelerator Architecture for Analog-AI Using Dense 2-D Mesh | IEEE Transactions on Very Large Scale Integration (VLSI) Systems |  | [DOI](https://doi.org/10.1109/tvlsi.2022.3221390) (no open PDF) |
| 2022 | **** ALPINE: Analog In-Memory Acceleration with Tight Processor Integration for Deep Learning | IEEE Transactions on Computers |  | [2022_Klein_AlpineAnalogInMemoryAcceleration.pdf](2022_Klein_AlpineAnalogInMemoryAcceleration.pdf) |
| 2021 | **** BRAHMS: Beyond Conventional RRAM-based Neural Network Accelerators Using Hybrid Analog Memory System |  |  | [DOI](https://doi.org/10.1109/dac18074.2021.9586247) (no open PDF) |
| 2021 | **** FORMS: Fine-grained Polarized ReRAM-based In-situ Computation for Mixed-signal DNN Accelerator |  |  | [2021_Yuan_FormsFineGrainedPolarizedReram.pdf](2021_Yuan_FormsFineGrainedPolarizedReram.pdf) |
| 2020 | **** Timely: Pushing Data Movements And Interfaces In Pim Accelerators Towards Local And In Time Domain |  |  | [2020_Li_TimelyPushingDataMovementsAnd.pdf](2020_Li_TimelyPushingDataMovementsAnd.pdf) |
| 2019 | **** CASCADE |  |  | [DOI](https://doi.org/10.1145/3352460.3358328) (no open PDF) |
| 2019 | **** ERA-LSTM: An Efficient ReRAM-Based Architecture for Long Short-Term Memory | IEEE Transactions on Parallel and Distributed Systems |  | [DOI](https://doi.org/10.1109/tpds.2019.2962806) (no open PDF) |
| 2019 | **** FloatPIM |  |  | [2019_Imani_Floatpim.pdf](2019_Imani_Floatpim.pdf) |
| 2019 | **** PUMA |  |  | [2019_Ankit_Puma.pdf](2019_Ankit_Puma.pdf) |
| 2018 | **** ReRAM-Based Processing-in-Memory Architecture for Recurrent Neural Network Acceleration | IEEE Transactions on Very Large Scale Integration (VLSI) Systems |  | [DOI](https://doi.org/10.1109/tvlsi.2018.2819190) (no open PDF) |
| 2017 | **** PipeLayer: A Pipelined ReRAM-Based Accelerator for Deep Learning |  |  | [DOI](https://doi.org/10.1109/hpca.2017.55) (no open PDF) |
| 2016 | **ISAAC** ISAAC: A Convolutional Neural Network Accelerator with In-Situ Analog Arithmetic in Crossbars | ISCA | First full-fledged memristor-crossbar CNN accelerator with an inter-layer pipeline, bit-serial inputs, 2-bit cells and a weight-flipping encoding that saves one ADC bit; reports 14.8x throughput, 5.5x lower energy and 7.5x computational density vs DaDianNao. | [2016_Shafiee_ISAAC_ISCA.pdf](2016_Shafiee_ISAAC_ISCA.pdf) |
| 2016 | **PRIME** PRIME: A Novel Processing-in-Memory Architecture for Neural Network Computation in ReRAM-Based Main Memory | ISCA | Processing-in-memory architecture in which some ReRAM main-memory subarrays can switch between storage and analog NN computation; reports about 2360x speedup and 895x energy saving over a CPU+NPU co-processor baseline with only 5.76% area overhead. | [2016_Chi_PRIME_ISCA.pdf](2016_Chi_PRIME_ISCA.pdf) |
