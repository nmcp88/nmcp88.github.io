---
title: Runtime Management of Heterogeneous Compute Resources in Embedded Systems
subtitle: This major objective of this thesis is to design and implement a runtime software and/or hardware mechanism capable of determining which accelerators should be loaded onto the FPGA, and when they should be loaded. 

# Summary for listings and search engines
summary: This major objective of this thesis is to design and implement a runtime software and/or hardware mechanism capable of determining which accelerators should be loaded onto the FPGA, and when they should be loaded. 

# Link this post with a project
projects: []

# Date published
date: "2021-09-01T00:00:00Z"

# Featured image
# Place an image named `featured.jpg/png` in this page's folder and customize its options here.
#image:
#  caption: 'Image credit: [**Unsplash**](https://unsplash.com/photos/CpkOjOcXdUY)'
#  focal_point: ""
#  placement: 2
#  preview_only: false

type: book

authors:
- admin

tags:
- FPGA
- High Level Synthesis
- Machine Learning
- OpenCL

categories:
- Thesis
---

### Motivation

In the embedded domain, it is not uncommon for compute platforms to be heterogeneous. That is, to contain a main processor, and several specialized co-processors for specific function. It is up to the programmer to understand the underlying hardware platform and schedule workload onto different components, and to synchronize their behavior. 

One of the platforms used for this kind of approach are Field-Programmable-Gate-Arrays (FPGAs). Since manual hardware design is a difficult process, approaches like High-Level Synthesis automatically generate circuit descriptions from functions written in C/C++ code. 

This major objective of this thesis is to design and implement a runtime software and/or hardware mechanism capable of determining which accelerators should be loaded onto the FPGA, and when they should be loaded. The autonomous decision making will use data such as: the values of the arguments of the functions that are being called, the order in which the functions are called, the execution time of the accelerators, the temporal overhead of switching accelerators via DPR, and others. 

### Proposed Work Plan

- Designing the base embedded system to apply the runtime resource management to. This will be done on the Xilinx ZCU102 Development Board. The hardcore ARM processor will host the application code, and the FPGA side will host the several accelerator slots;
- From a set of compute kernels, create the respective accelerator modules using High-Level Synthesis; multiple accelerators per function should be generated, each with different design parameters (e.g., throughput, size, reconfiguration time, etc);
- Develop, either in software, hardware, or a mixed design, a methodology for random forest selection which can determine when and which accelerators to load into which slots. 

### Details

- Status: Completed
- Student: [Luís Miguel de Sousa](https://sigarra.up.pt/feup/pt/vld_entidades_geral.entidade_pagina?pct_codigo=201605770)
- [Thesis Document](https://sigarra.up.pt/feup/pt/ESTAGIOS_ALUNOS.ENTRADA?p_aluno_id=123893)
- [GitHub Repository](https://github.com/Sleepy105/Hoeffding-Tree)

