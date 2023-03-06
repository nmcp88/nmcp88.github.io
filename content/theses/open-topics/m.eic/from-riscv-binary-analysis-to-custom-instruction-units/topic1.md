---
title: From RISC-V Binary Analysis to Custom Instruction Units

subtitle: This work is about implementing complier-like steps to transform sequences of instructions into custom instructions.

# Summary for listings and search engines
summary: This work is about implementing complier-like steps to transform sequences of instructions into custom instructions.

# Link this post with a project
projects: []

# Date published
date: "2023-04-02T00:00:00Z"

# Date updated
lastmod: "2023-04-02T00:00:00Z"

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

draft: yes

type: book

authors:
- admin

tags:
- RISC-V
- Binary Analysis
- Heterogeneous Computing

categories:
- Thesis
---

### Context

Edge devices are limited in computing power and available battery. One solution to better power/performance ratio is the use of specialized hardware (1). The RISC-V is a rising family of open-source processors designed for configurability and extension. This work continues previous work (2,3,4) already capable of generating HDL from RISC-V binaries parsed from instruction traces.

### Objectives

Using execution traces of applications using on an existing framework (2), this work will first devise a data structure to represent the trace graph of (parts of) a program containing multiple instructions. The main objectives will be;

- Gather “hot” instruction sequences (+1 instruction) from traces
- Use/improve existing in-house tools to generate HDL to implement the custom instructions (https://github.com/specs-feup/specs-hw)
- Integrate the custom units into a baseline RISC-V
- Evaluate baseline vs. acceleration in terms of execution time and power (this may be done relying on recent past work [4])

### Novel Aspects

ior work done in the laboratory has significantly established the framework for exploration of new hardware compilation techniques. Defining an interchangable trace graph format, capable of being subject to optimizations and transformations is a significant step for future work.

The RISC-V is a rising family of open-source processors designed for configurability and extension, projected to outnumber ARM and x86  processors by 2025 in some spaces. Since it is open-source, a large  eco-system of reusable designs exists for research and commercial use.  Developing compilation techniques for future RISC-V based heterogeneous systems for future compute.

### Proposed Work Plan

- Studying related work on similar heterogeneous hardware approaches (1)
- Studying the existing framework and code base (2) an plan code structure to develop 
- Gather repeated instruction sequences from RISC-V traces using a set of benchmarks
- Generate the hardware to execute the custom instructions
- Estimate speedup (and optionally power) gains by simulation of 
software only execution vs accelerated execution; this may be done 
relying on recent past work (4)
- Writting the dissertation

### Details

- Status: Open!
- Student: None (yet).

#### References

- (1) Nuno Paulino, João Canas Ferreira, and João M. P. Cardoso. 2020. Improving Performance and Energy Consumption in Embedded Systems via Binary Acceleration: A Survey. ACM Comput. Surv. 53, 1, Article 6 (January 2021), 36 pages. https://doi.org/10.1145/3369764
- (2) https://github.com/specs-feup/specs-hw/, https://pepcc.inesctec.pt
- (3) João Conceição, 2021, Generating Hardware Modules via Binary Translation of RISC-V Binaries, https://repositorio-aberto.up.pt/handle/10216/140767
- (4) https://github.com/specs-feup/specs-chisel/

