---
title: Generating Hardware Modules via Binary Translation of RISC-V Binaries

subtitle: This work is about using binary translation to create custom units for RISC-V processor pipelines.

# Summary for listings and search engines
summary: This work is about using binary translation to create custom units for RISC-V processor pipelines.

# Link this post with a project
projects: []

# Date published
date: "2021-10-18T00:00:00Z"

# Date updated
lastmod: "2021-10-18T00:00:00Z"

# Is this an unpublished draft?
draft: false

# Show this page in the Featured widget?
featured: false

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
- RISC-V
- Binary Translation
- Compilers

categories:
- Thesis
---

### Motivation

An application's performance can be maximized. In the embedded domain, this design philosophy involves analyzing the target application, determining the portions of code which represent a large portion of computation, and designing hardware modules which replicate the functionality of the code/function. However, manually designing hardware modules is a time consuming and error-prone task. 

The major objective of this thesis is to automatically generate hardware modules for embedded applications, based on profiled application information. This capability will be integrated into an [existing framework](https://github.com/specs-feup/specs-hw/). The framework supports several Instruction Set Architectures, but this work will focus on applications compiled for the RISC-V. 

This work is expected to extend the framework with hardware generation and validation features, and to estimate the speedups and resource usage that would be achievable if the generated hardware was used in practice. 

### Proposed Work Plan

- Support for interpretation of RISC-V instruction streams
- Defining the pseudo-instruction code for the instructions in the RISC-V ISA
- Designing and implementing an interchangeable/complementary AST <-> CDFG representation of the detected sequences of instructions
- Converting small example ASTs/graphs into Verilog, based on whichever specific hardware design is to be explored (code for generation of Verilog is already partially completed)
- Generating test benches for the modules, and comparing the simulated output to the expected results, based on the known behavior of the translated instructions
- Perform an evaluation of potential speedups that could be attained using the automated hardware generation, for a small set of benchmarks compiled for the RISC-V 

### Details

- Status: Completed
- Student: [João Miguel Curado Conceição](https://sigarra.up.pt/feup/pt/fest_geral.cursos_list?pv_num_unico=201506202)
- [Thesis Document](https://repositorio-aberto.up.pt/handle/10216/140767)