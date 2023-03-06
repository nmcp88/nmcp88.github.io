---
title: Compiling for Spatial Computation Architectures

subtitle: This work is about compiling C code to systolic arrays via source-to-source.

# Summary for listings and search engines
summary: This work is about compiling C code to systolic arrays via source-to-source.

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
- RISC-V
- Binary Translation
- Compilers

categories:
- Thesis
---

### Context

With the rise of the internet of things, much more data needs to be processed in edge devices (e.g., sensors, cameras, routers, etc) to prevent large data transfers to central servers. However, these devices are typically not very powerful computationally, and it is not trivial to replace them with high end devices (e.g. multi-core giga-hertz processors, GPUs, etc) due to power consumption limits. 

One type of computation machine are spatial arrays, also known as coarse-grain arrays (CGRAs) or systolic arrays. These machines are matrixes of units that perform operations in parallel. A 4x4 matrix has 16 units, meaning 16 operations in parallel in the best case. In theory, these devices promise higher performance for lower power. 

However, many issues related to abstraction, programming, and compilation exist, since there is no established language, compiler, or model (Podobas2020, Lin2019, Zhao2020). 

While CPUs have established compilers and languages like C, where a sequence of operations is executed one at a time in the processor, the spatial nature of the arrays introduces several challenges. What language to use? If some code executes on a main processor, and some code on the array, how to interface the devices? Via an explicit API? What compiler to use? 

### Objectives

This work targets this model: a CPU has a spatial array attached as a peripheral (i.e., like a GPU), and standard C code is written for an application.

This work aims to devise a compilation flow for this model where some functions in the C code are compiled for the array. To do this, source-to-source tools developed in-house (Bispo2020) will be used to automatically replace specific functions with calls to the array. 

### Novel Aspects

This type of computation machine has been studied at length, but there is no established compilation flow. 

This is due to the several types of array layouts and architectures which influence compilation; due to no established interface between arrays and host system, and due to the fact that no existing language has been widely adopted for this type of machine.

Providing a high-level approach by compiling standard C code, and proposing an abstraction layer addresses some of these issues.


### Proposed Work Plan

- Familiarization with existing tools for source-to-source transformations, and techniques for operation mapping/scheduling (During first semester) 
- Definition of the set of pragmas to aid in source conversion
- Parsing C code into an intermediate representation (using existing tools in the lab), and schedule the function onto a target array architecture
- Replacing the original C code with calls to the architecture, based on the generated schedule
- Evaluating the resulting speedups and scheduling time based on the architecture specification (i.e., number of units)
- Writting the dissertation
- Writting a scientific publication

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Podobas2020) A Survey on Coarse-Grained Reconfigurable Architectures From a Performance Perspective - https://ieeexplore.ieee.org/document/9149601

- (Liu2019) A Survey of Coarse-Grained Reconfigurable Architecture and Design: Taxonomy, Challenges, and Applications" - https://dl.acm.org/doi/abs/10.1145/3357375 

- (Zhao2019) Towards Higher Performance and Robust Compilation for CGRA Modulo Scheduling," in IEEE Transactions on Parallel and Distributed Systems, https://ieeexplore.ieee.org/document/9075353

- (Bispo2020) Clava: C/C++ source-to-source compilation using LARA, SoftwareX", Volume 12, 2020, https://doi.org/10.1016/j.softx.2020.100565

