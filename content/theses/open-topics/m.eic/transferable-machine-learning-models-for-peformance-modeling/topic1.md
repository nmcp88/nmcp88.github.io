---
title: Transferable Machine Learning Models for Performance Modeling

subtitle: This work is about applying machine learning to generate transferable models for performance estimation for CPUs.

# Summary for listings and search engines
summary: This work is about applying machine learning to generate transferable models for performance estimation for CPUs.

# Link this post with a project
projects: []

# Date published
date: "2021-10-26T00:00:00Z"

# Date updated
lastmod: "2021-10-26T00:00:00Z"

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
- Performance Modeling
- Machine Learning
- Source analysis

categories:
- Thesis

# NOTE: if we dont have multi-threaded benchmarks, we can just launch several threads with the same polybench or livermore loop!

---

### Context

Performance modeling in general is useful as a tool to predict the performance (runtime). Performance predictions are useful, for example, for CPU designers to predict the runtime of a set of benchmarks, without requiring long execution times for large benchmarks. Inversely, we can use a model to predict the runtime of new code on an existing CPU. 

Models may helps us compare the execution time of the same algorithms on different CPUs (with different features, like frequency, cache size, threads, etc), without long execution times. 

Efficient models may also help scheduling of workloads on server clusters with multiple CPUs, where a scheduler can use the models to decide what CPU is best for a specific workload. 

### Objectives

This work is about attempting to extract features about the code and the devices, and then determining if a model can be learned which can predict the execution time based on those features. The work will rely on an existing tool for source-to-source analysis (Bispo2020, Sousa2021), which already performs some feature extraction. 

The main objective is to train models which can predict the runtime of arbitrary code kernels (i.e., functions) for a specific CPU, without requiring actual execution. Performance modeling has uses in benchmark design, runtime scheduling for HPC systems, and software design for predicting expected performance.

### Novel Aspects

Prior work done in the laboratory has evaluated this type of machine learning for embedded systems (with FPGAs), using a limited feature set (Sousa2021). This work will build on this knowledge to generate transferable models for prediction of CPU performance. Additional features may include a CPU characteristics, and baseline profiling of CPU performance as per some approaches in the state-of-the-art.

Relative to the state-of-the-art, existing approaches have demonstrated that performance can be prediceted with machine learning, but focus on predicting performance on specific benchmarks for new CPUs. 

This work will explore the viability of predicting the runtime of algorithms which were not used to train the model (i.e., arbitrary user code), and the possibility of transfering pre-trained models between CPUs. We will attempt to arrive at a distributable format for CPU performance models. This may constitute a scientific contribution as a component for future modeling of heterogeneous HPC systems.

In order to create a reutilizable model, the work may rely on established file formats like ONNX, and popular machine learning libraries like PyTorch.

### Proposed Work Plan

- Prepare a benchmark suite of several kernels
- Improve the current feature extraction to include more features from the source code (for example, implicit parallelism, number of memory accesses etc)
- Configure and experimental setup which allows for the kernels to be run under several conditions (i.e., problem size, number of threads, type of data, etc)
- Train inference models which predict runtime based on algorithm train set and CPU features
- Evaluate the accuracy of the models using a test set 
- Evaluate the accuracy of transfered models
- Writting the dissertation
- Writting a scientific publication

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Wang2019) Predicting New Workload or CPU Performance by Analyzing Public Datasets - https://doi.org/10.1145/3284127

- (Vanishree2020) CPU Performance Modeling through Analysis of Primitive Operations - https://ieeexplore.ieee.org/abstract/document/9070898

- (Bispo2020) Clava: C/C++ source-to-source compilation using LARA, SoftwareX", Volume 12, 2020, https://doi.org/10.1016/j.softx.2020.100565

- (Sousa2021) Runtime Management of Heterogeneous Compute Resources in Embedded Systems, Master's Thesis, Faculty of Engineering of the University of Porto

- (Lopez2018) Predicting Computer Performance Based on Hardware Configuration Using Multiple Neural Networks - https://ieeexplore.ieee.org/document/8614157

