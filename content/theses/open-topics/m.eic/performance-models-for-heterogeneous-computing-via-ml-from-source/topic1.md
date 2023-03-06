---
title: Performance Models for Heterogeneous Computing via Machine Learning from Source Analysis

subtitle: This work is about applying machine learning to performance modeling of applications from source code.

# Summary for listings and search engines
summary: This work is about applying machine learning to performance modeling of applications from source code.

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

For good performance, reliance on parallelism is increasingly important. One type of device that can implement demanding functions (also called “kernels”) with parallel computation are Field-Programmable-Gate-Arrays (FPGAs). Recent tools support the compilation of languages like C and C++ into circuits that run on the FPGA, and execute the kernel calculations in parallel. These are called High-Level-Synthesis (HLS) tools.

This means that a heterogeneous system, with a CPU + FPGA, can execute part of an application on the CPU, and part on the FPGA. The functions that are  chosen to execute on the FPGA are called “accelerated functions”. Properly dividing the work between the two devices will result in a reduced total execution time.

In this context, there are two main problems: 1) the C/C++ code must be modified before being compiled to the FPGA, so that the performance is optimized, and 2) it is difficult to predict which device will be faster (CPU or FPGA) for all possible input arguments to the function. This work will develop models to perform this prediction by extracting features from the source code, to use as machine learning features.

### Objectives

This work will improve an existing approach which extracts features from source code (Sousa2021, Sousa2022). The features are extracted using source analysis (Bispo2020), and will be used to implement machine learning models to predict which device will be faster based on input arguments: the CPU, or the FPGA.

New features to extract from the source code may include: the expected number of memory accesses, the dataflow graph of the code, and characteristics of the device (i.e., number of cores, frequency, etc).

We will then evaluate if the actual execution time matches the model, and if the model can be used to predict the runtime of kernels that were not used to train it.

### Novel Aspects

Prior work done in the laboratory has evaluated this type of machine learning for FPGA performance prediction, using a limited feature set (Sousa2021), and unoptimized FPGA kernels. This work will: 1) improve the FPGA implementations and, 2) extend the feature set and train an improved ML model.

Execution time prediction using machine learning has seen recent efforts in the state of the art (Sun2020), but has some limitations. For example: at least partial execution is required, the analysis is performed after compilation, and the source features are not generalizable for arbitrary C/C++ code.

### Proposed Work Plan

- Choose 2 or 3 simple kernels (a matrix multiplication, a k-means implementation, etc)
- Manually optimize the kernels for High-Level-Synthesis (HLS) to run on the FPGA
- Run the functions in CPU and on FPGA, with different function arguments. Record the execution times (that is, make the dataset for the machine learning step)
- Extract features from the source code, to make the machine learning model to predict execution times. This step will use the current feature extraction (Sousa2021, Sousa2022), but will add more features (for example, number of memory accesses, support for “if-else” inside loops, etc)
- Use ML to predict the fastest device based on the features (i.e., which will be fastest based on function arguments); existing frameworks like TensorFlow (Python), or Deeplearning4j (Java), can be used.

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Bispo2020) [Clava: C/C++ source-to-source compilation using LARA”, SoftwareX, Volume 12, 2020](https://doi.org/10.1016/j.softx.2020.100565)
- (Sousa2021) [Runtime Management of Heterogeneous Compute Resources in Embedded Systems”, MsC Thesis, Faculty of Engineering of the University of Porto](https://repositorio-aberto.up.pt/handle/10216/137152)
- (Sousa2022) [A Flexible HLS Hoeffding Tree Implementation for Runtime Learning on FPGA," *IEEE MELECON*, Palermo, Italy, 2022]https://ieeexplore.ieee.org/document/9843092)
- (Sun2020) [Automated Performance Modeling of HPC Applications Using Machine Learning”, in IEEE Transactions on Computers, 2020](https://ieeexplore.ieee.org/document/8956059)

