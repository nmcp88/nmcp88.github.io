---
title: Performance Modeling for HPC through Machine Learning from Source Code

subtitle: This work is about applying machine learning to performance modeling of applications on different targets.

# Summary for listings and search engines
summary: This work is about applying machine learning to performance modeling of applications on different targets.

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
- HPC
- Machine Learning
- Source analysis
- Heterogeneous Computing

categories:
- Thesis
---

### Context

HPC systems are growing in complexity. For good performance, reliance on parallelism is necessary. However, predicting performance for parallel programs is a difficult task, as it depends on algorithm design (the code itself), the problem size (potentially many functions arguments), and the characteristics of the target device. Since HPC systems may be heterogeneous, and contain many CPUs, many GPUs, and even FPGAs, it is difficult to know which device will be faster for a specific function and a specific problem size. 

Executing a target algorithm for many problem sizes (including very large sizes) on all devices for different configurations to determine which is best is possible, but requires a very long time which makes iterative development and evaluation impossible.

So, performance models are important in HPC systems, so that designers can understand the expected performance of a given code for several problem sizes on a given machine, without executing the code and having to wait. Models are also useful in terms of scheduling for HPC at runtime, since a particular task can be scheduled on the best device taking into account the problem size and available resources on the HPC cluster. 

### Objectives

This work is about attempting to extract features about the code and the devices, and then determining if a model can be learned which can predict the execution time based on those features.

The work will rely on an existing tool for source-to-source analysis (Bispo2020), which already performs some feature extraction. The new features to add must be studied, but may include information on the expected number of memory accesses, the dataflow graph of the code, and characteristics of the device (i.e., number of CPU cores, frequency, amount of RAM, etc).

We will then evaluate if the actual execution time matches the model, and if the model can be used to predict the runtime of algorithms that were not used to train it.

### Novel Aspects

Prior work done in the laboratory has evaluated this type of machine learning for embedded systems (with FPGAs), using a limited feature set (Sousa2021). This work will apply this to an HPC context, and develop a more sophisticated model.

Relative to the state-of-the-art, research on model prediction for HPC using machine learning has seen recent efforts (Sun2020, Hao2019, Frank2014). Some of the weaknesses include: at least partial execution is required to predict the execution time, the models focus on the Intel MPI library, they do not consider resource usage (when used for scheduling), rely on post-compilation analysis, or use a non-generalizable feature set.

### Proposed Work Plan

- Select two/three simple target functions for analysis (i.e., a matrix multiplication kernel, a k-means implementation, etc)
- Design fast implementations of each algorithm for each target device (the CPU, a GPU, and an FPGA)
- Characterize the runtime of each function on each device, based on function arguments (that is, determine the ground truth)
- Improve the current feature extraction to include more features from the source code (for example, implicit parallelism, number of memory accesses etc)
- Design a machine learning model which can predict the fastest device based on this feature set (i.e., which device is fastest based on function arguments)
- (Optional: improve the model with features such as resource occupancy, i.e., is the GPU busy etc)
- Writting the dissertation
- Writting a scientific publication

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Sun2020) Automated Performance Modeling of HPC Applications Using Machine Learning, in IEEE Transactions on Computers, vol. 69, no. 5, pp. 749-763, 1 May 2020, doi: 10.1109/TC.2020.2964767. https://ieeexplore.ieee.org/document/8956059

- (Bispo2020) Clava: C/C++ source-to-source compilation using LARA, SoftwareX", Volume 12, 2020, https://doi.org/10.1016/j.softx.2020.100565

- (Sousa2021) Runtime Management of Heterogeneous Compute Resources in Embedded Systems, Master's Thesis, Faculty of Engineering of the University of Porto

- (Hao2019) Multi-Parameter Performance Modeling Based on Machine Learning with Basic Block Features. 316-323. 10.1109/ISPA-BDCloud-SustainCom-SocialCom48970.2019.00054. https://ieeexplore.ieee.org/document/9047415

- (Frank2014) Algorithm runtime prediction: Methods & evaluation, Artificial Intelligence, Volume 206, 2014, https://doi.org/10.1016/j.artint.2013.10.003.

