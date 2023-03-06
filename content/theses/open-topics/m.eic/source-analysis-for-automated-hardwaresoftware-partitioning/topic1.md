---
title: Source Analysis for Automated Hardware/Software Partitioning

subtitle: This work is about automatically identifying hotspots for acceleration via source analysis.

# Summary for listings and search engines
summary: This work is about automatically identifying hotspots for acceleration via source analysis.

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
- Machine Learning
- Source-to-source
- Heterogeneous Computing

categories:
- Thesis
---

### Context

For good performance, reliance on parallelism is increasingly important. Demanding applications can benefit from executing parts of the application in software (on the CPU), and others in devices like GPUs, or Field-Programmable-Gate-Arrays (FPGAs). Such systems are commonly called heterogeneous systems. 

Taking a so-called “sequential” application (written for a single processor in C/C++), and deciding which portions (that is, functions) can benefit from being re-written to execute on another device requires some expert knowledge and analysis of the code/algorithm. This step of the process of re-targeting an application to a heterogeneous system is typically called “hardware/software partitioning”. The objective of this work is to automate this process using a high-level analysis of source code (Bispo2020), similar to compiler analysis/optimization passes.

### Objectives

Prior work done in the laboratory has developed the extraction of a feature set (Sousa2021) from source code only, using an extensible source analysis framework (Bispo2020). The current features set is a prediction of the amount of operations (workload) which will be performed by a given function, for a given set of input arguments. However, the extraction of the features is limited to a subset of C/C++.

This work has three primary objectives: 
- 1) extending the supported set of C/C++ from which the features can be extracted (for example, supporting while loops, analysis of the expected workload based on control variables, supporting recursivity, etc);
- 2) study potential new features and implement their extraction (for example, expected number of memory accesses, or dataflow graph of the code);
- 3) use points 1) and 2) to automatically identify functions that represent a heavy workload (replacing the current manual step).

### Novel Aspects

One of the more difficult aspects of re-targeting an application for an heterogeneous system is the effort in identifying which portions of the original application can benefit the most from acceleration (in a GPU, or FPGA, for example). This type of source analysis can provide hints for software developers who are not experts in heterogeneous systems, making the development process faster and easier. In the future, the features extracted will be useful in other ways, for example, to implement machine learning models to predict performance, extending another aspect of the current work (Sousa2022).

### Proposed Work Plan

- Familiarization with the source-to-source analysis framework (Bispo2020, Clava)
- Choosing and preparing a set of functions (including functions with source constructs currently unsupported)
- Extending the extraction of the current feature set to a larger subset of C/C++
- Implementing the extraction of new features
- Use the feature analysis to identify the functions representing the bulk of the workload with a #pragma statement, for processing by further steps in the compilation flow
- (Optional) Integrate with current source-to-source flow for hardware/software partitioning

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Bispo2020) [Clava: C/C++ source-to-source compilation using LARA”, SoftwareX, Volume 12, 2020](https://doi.org/10.1016/j.softx.2020.100565)
- (Sousa2021) [Runtime Management of Heterogeneous Compute Resources in Embedded Systems”, MsC Thesis, Faculty of Engineering of the University of Porto](https://repositorio-aberto.up.pt/handle/10216/137152)
- (Sousa2022) [A Flexible HLS Hoeffding Tree Implementation for Runtime Learning on FPGA," *IEEE MELECON*, Palermo, Italy, 2022]https://ieeexplore.ieee.org/document/9843092)
- (Clava) https://specs.fe.up.pt/tools/clava/

