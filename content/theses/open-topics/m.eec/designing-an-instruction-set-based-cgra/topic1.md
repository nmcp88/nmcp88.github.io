---
title: Designing an Instruction Set Based Coarse Grain Accelerator

subtitle: This work is about abstracting CGRA architectures via a proposal for a common ISA.

# Summary for listings and search engines
summary: This work is about abstracting CGRA architectures via a proposal for a common ISA.

# Link this post with a project
projects: []

# Date published
date: "2021-10-20T00:00:00Z"

# Date updated
lastmod: "2021-10-20T00:00:00Z"

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
- CGRAs
- Compilers
- Languages

categories:
- Thesis
---

### Context

With the rise of the internet of things, much more data needs to be processed in edge devices (e.g., sensors, cameras, routers, etc) to prevent large data transfers to central servers. However, these devices are typically not very powerful computationally, and it is not trivial to replace them with high end devices (e.g. multi-core giga-hertz processors, GPUs, etc) due to power consumption limits.

The key to a better power-performance tradeoff is specialized hardware. However, specialized hardware is difficult to design. Instead, there is an emerging interest in a category of devices which are promising for generic parallel computation: coarse-grain-reconfigurable-arrays (CGRAs).

CGRAs are matrixes of blocks which perform calculations and pass data to their neighbours in the matrix. All blocks execute in parallel, so a great potential for acceleration exists (Podobas2020, Liu2019). CGRAs are promising to accelerate specific functions in a program in a very efficient way (in the same way that GPUs accelerate very specific matrix calculations).

But one of the existing problems with CGRAs is the lack of a good programming model which makes their use easy, both in terms of generating programs for them, and in terms of connecting them to a main CPU. 

### Objectives

This work aims to: 1) define a set of instructions to abstract away hardware details of a CGRA, and 2) to implement a CGRA which can be controlled by those instructions, and to 3) evaluate the design.

An standard instruction set for CGRAs would allow for easy compilation of arbitrary programs onto them, allowing for wide application in edge and IoT devices which need good computing at low power. 

### Proposed Work Plan

- Familiarization with core concepts like CGRAs, and existing tools an designs too be used as starting points or reference (for example, the Gemmini CGRA generator https://github.com/ucb-bar/gemmini, and the Chisel3 hardware design language)
- Preparing a set of benchmarks to use for validation in the work
- Preparing the first version of the state of the art 

- Design a set of control instructions to control a generic CGRA design, including defining the current configuration, starting and stoping execution, etc
- Implement a new (or extend an existing) CGRA design which is parametrizable and can be controlled with the designed ISA
- Implement the CGRA microcode which configures the CGRA to perform calculations from the benchmarks
- Validate the design via simulation
- Synthesize the design for hardware (for example a 45nm library) and evaluate the area and power 

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Podobas2020) "A Survey on Coarse-Grained Reconfigurable Architectures From a Performance Perspective" - https://ieeexplore.ieee.org/document/9149601

- (Liu2019) "A Survey of Coarse-Grained Reconfigurable Architecture and Design: Taxonomy, Challenges, and Applications" - https://dl.acm.org/doi/abs/10.1145/3357375

- [UC Berkely's Gemmini](https://github.com/ucb-bar/gemmini)

- (Lopes2021) Coarse-Grained Reconfigurable Computing with the Versat Architecture - https://www.mdpi.com/2079-9292/10/6/669

