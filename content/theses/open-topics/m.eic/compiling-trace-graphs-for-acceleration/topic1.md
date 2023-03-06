---
title: Compiling Trace Graphs to RISC-V Accelerators

subtitle: This work is about re-compiling RISC-V instruction sequences to parallel compute engines.

# Summary for listings and search engines
summary: This work is about re-compiling RISC-V instruction sequences to parallel compute engines.

# Link this post with a project
projects: []

# Date published
date: "2021-10-28T00:00:00Z"

# Date updated
lastmod: "2021-10-28T00:00:00Z"

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
- Intermediate Representations
- RISC-V
- Binary Translation
- Compilers

categories:
- Thesis
---

### Context

The internet-of-things is on the rise, creating a large volume of data that needs to be moved into a central server to be processed. An alternative is to process data as much as possible on the edge, instead of the server, reducing data transfers, and providing a faster response time for edge services. For example, machine learning inference from image data on the edge.

However, edge devices (like cameras, routers, drones, phones etc), are limited (in comparison to power servers) of power and compute power. This prevents the true rise of edge computing. One solution to better power/performance ratio is the use of more efficient hardware. Hardware is specialized for a task consumes less power, and is faster to execute.

However, manually designing hardware modules is a time consuming and error-prone task. Future heterogeneous systems could benefit from new compilation approaches that not only compile code, by also generate the efficient hardware to run that code.

### Objectives

Using execution traces of applications using on an existing framework (Paulino2020), this work will first devise a data structure to represent the trace graph of (parts of) a program, including frequent execution paths, loops and nested loops. Secondly, compilation techniques will be employed to evaluate the possible acceleration by scheduling the workload onto compute engines capable of parallel computation.

### Novel Aspects

Prior work done in the laboratory has significantly established the framework for exploration of new hardware compilation techniques. Defining an interchangable trace graph format, capable of being subject to optimizations and transformations is a significant step for future work.

The RISC-V is a rising family of open-source processors designed for configurability and extension (UCBerkley), projected to outnumber ARM and x86 processors by 2025 in some spaces. Since it is open-source, a large eco-system of reusable designs exists for research and commercial use (UCBChipyard, RISCVMini). Developing compilation techniques for future RISC-V based heterogeneous systems for future compute. 

### Proposed Work Plan

- Devise a data structure to store multiple execution paths of a program, including loops and nested loops
- From a set of RISC-V programs into the representation, extract workload in this format via simulation, and characterize the detected patterns
- Study the possible optimization steps that can be applied to the datastructure (for example, unrolling, loop fissioning, etc)
- Provide an estimate of speedup by scheduling the workload onto a given compute engine model
- (Optional: integrate the model into a RISC-V simulator and perform a joint validation)
- Writting the dissertation
- Writting a scientific publication

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Paulino2020) Binary Translation Framework - https://github.com/specs-feup/specs-hw

- (UCBerkley) The RISC-V Instruction Set Architecture - https://bar.eecs.berkeley.edu/projects/riscv.html

- (UCBChipyard) UCBerkley's Chipyard Framework - https://github.com/ucb-bar/chipyard/

- (RISCVMini) RISC-V Mini - https://github.com/ucb-bar/riscv-mini

