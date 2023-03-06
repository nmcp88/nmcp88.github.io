---
title: Power Efficiency and Performance for Embedded and HPC Systems with Custom CGRAs
summary: Improve performance and power efficiency of regular computational kernels in ES and HPS systems, by efficient runtime mapping of computations to specialized CGRA, while ensuring the most transparency to the application developer.

tags:
- Hardware Acceleration
- Heterogeneous Computing

date: "2020-07-01T00:00:00Z"

# Optional external URL for project (replaces project detail page).
external_link: ""

image:
  caption: 
  focal_point: 

links:
#- icon: twitter
#  icon_pack: fab
#  name: Follow
#  url: https://twitter.com/georgecushen
url_project: "http://pepcc.inesctec.pt/"
url_code: ""
url_pdf: ""
url_slides: ""
url_video: ""

# Slides (optional).
#   Associate this project with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
#slides: example

categories:
- Projects
---

The domains of embedded systems and high-performance computing (HPC) are usually seen as distant, but some of their requirements are converging: a modern ES runs complex algorithms with high computational power; the power consumption of ever larger HPC systems requires new levels of power efficiency.

Embedded systems have adopted heterogeneous architectures, often based on reconfigurable accelerators like FPGAs or Coarse-Grained Reconfigurable Arrays (CGRAs), because they combine hardware specialization (improving performance and power efficiency) with adaptability at run-time. A similar trend towards heterogeneity is observed in HPC systems with GPUs as accelerators: HPC stakeholders have identified several challenges related to auto-tuning and self adapting systems, and power-aware resource management, matching the trends identified by ES stakeholders on the relevance of heterogeneous accelerators.

The goal of this project is to devise efficient techniques for dynamically mapping computations extracted from execution behavior to the resources of specialized reconfigurable accelerators. The techniques will identify at runtime the hotspots of program execution. They are then optimized and mapped to CGRAs tailored to the actual set of executing kernels. Whenever one hotspot needs to be executed, the accelerator is transparently invoked. The use of specialized CGRAs reduces resource usage and improves performance. The project will apply these concepts in the ES and HPC domains.

### Project Reference

Funded by FCT (Fundação para a Ciência e a Tecnologia)
- Reference: PTDC/EEI-HAC/30848/2017

