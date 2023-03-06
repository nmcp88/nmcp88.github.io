---
title: Accelerated Pattern Matching for Big Data

subtitle: This work is about accelerating algorithms for Big Data and internet security.

# Summary for listings and search engines
summary: This work is about accelerating algorithms for Big Data and internet security.

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
- OpenCL
- Regex
- Big Data
- Network Security

categories:
- Thesis
---

### Context

Regular expressions (known shortly as regex) describe search patterns that we wish to find in a sequence of input (for example, text). Regex allows for many different types of patterns to be matched (i.e., specific words, repetitions of groups of words, etc), and is widely used in data mining, text processors, and network processing.

In big data analytics, large volumes of data need to be processed to collect meta data. Using software implementations may be too slow and may consume significant energy.  In network processing, regex is used to filter out harmful traffic such as DDoS attacks, or to filter out malicious content using a set of known regex rules. Since the amount of internet traffic is increasing more and more, it is important to evaluate the regexes as fast as possible, to reduce latency and energy consumed by servers and routers. 

### Objectives

This work will implement fast and energy efficient pattern matching engines on hardware accelerators. Specifically, on FPGA based data center accelerators using OpenCL.

We will evaluate the performance using state-of-the-art datasets.

### Novel Aspects

Although hardware implementations for regular expression matching have been studied on FPGAs, most are done using low-level hardware design. Only recently did high abstraction levels like C/C++ and OpenCL appear for PCI-express based FPGA cards. The most significant study is as recent as 2021 (Callanan2021). 

This work will attempt to improve on the existing results of the state-of-the-art, and on previous recent results obtained by us, using a data center accelerator (Xilinx2020). One limitation of hardware implementations of regex is the support for "back references" (matching with a previous part of the input string itself). We will also attempt to address this limitation.

### Proposed Work Plan

- Literature review on regular expressions, and hardware implementations of regular expression matching (Callanan2021)
- Familiarization with the accelerator card (Xilinx2020)

- Implement OpenCL based code to match regular expressions
- (Optional) Explore solution for back reference support
- Evaluate the throughput of the implementation
- Writing the dissertation
- Writing a scientific article (depending on results)

### Details

- Status: Open!
- Student: None (yet).

#### References

- (Callanan2021),  Accelerating Regular-Expression Matching on FPGAs with High-Level Synthesis  - https://doi.org/10.1145/3456669.3456716

- (Gogte2016) HARE: Hardware accelerator for regular expressions, 2016 - https://ieeexplore.ieee.org/document/7783747

- (Xilinx2020) https://www.xilinx.com/products/boards-and-kits/alveo/u250.html

