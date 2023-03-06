---
title: Specializing RISC-V Cores for Performance and Power

subtitle: This work is about customizing RISC-V processors with custom units.

# Summary for listings and search engines
summary: This work is about customizing RISC-V processors with custom units.

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

The internet-of-things is on the rise, creating a large volume of data that needs to be moved into a central server to be processed. An alternative is to process data as much as possible on the edge, instead of the server, reducing data transfers, and providing a faster response time for edge services. For example, machine learning inference from image data on the edge.

However, edge devices (like cameras, routers, drones, phones etc), are limited (in comparison to power servers) of power and compute power. This prevents the true rise of edge computing. One solution to better power/performance ratio is the use of more efficient hardware. Hardware is specialized for a task consumes less power, and is faster to execute. 

### Objectives

The RISC-V is a rising family of open-source processors designed for configurability and extension. 

This work aims to: 1) add custom units to a RISC-V to achieve faster runtimes and lower power consumption, to 2) validate the design on FPGA, and (optionally, depending on time) 3) to reduce area usage by using runtime circuit reconfiguration (i.e., Dynamic Partial Reconfiguration on FPGA) 

### Proposed Work Plan

- Familiarization with core concepts like Dynamic Partial Reconfiguration (DPR), the RISC-V, and existing tools an designs too be used as starting points (for example, the RISC-V Mini https://github.com/ucb-bar/riscv-mini, or the Gem5 processor simulator or alternatives)
- Preparing a set of benchmarks to use for validation in the work
- Preparing the first version of the state of the art 

- Generate a set of custom units for the RISC-V from graph analysis
- Implement the units in a modern HDL design language such as Chisel3
- Integrate the units into an open source Risc-V design
- Evaluate the area and performance of the design versus the original, (with and without reconfiguration if time allows) 

### Details

- Status: Completed!
- Student: [Henrique Sousa](https://sigarra.up.pt/feup/pt/fest_geral.cursos_list?pv_num_unico=201604227).
- [Thesis Document](https://repositorio-aberto.up.pt/handle/10216/144547)

#### References

- (UCBerkley's Chipyard Framework)[https://github.com/ucb-bar/chipyard/] (creators of the Risc-V)
- (Plastiras2018) Edge Intelligence: Challenges and Opportunities of Near-Sensor Machine Learning Applications - https://ieeexplore.ieee.org/document/8445118
- (Dao2020) FlexBex: A RISC-V with a Reconfigurable Instruction Extension - https://ieeexplore.ieee.org/document/9415607
- (Charaf2021) RV-CAP: Enabling Dynamic Partial Reconfiguration for FPGA-Based RISC-V System-on-Chip -
https://ieeexplore.ieee.org/document/9460688
- (Flamand2018) GAP-8: A RISC-V SoC for AI at the Edge of the IoT - https://ieeexplore.ieee.org/document/8445101
- (Sordillo2021) Customizable Vector Acceleration in Extreme-Edge Computing: A RISC-V Software/Hardware Architecture Study on VGG-16 Implementation - https://www.mdpi.com/2079-9292/10/4/518 

