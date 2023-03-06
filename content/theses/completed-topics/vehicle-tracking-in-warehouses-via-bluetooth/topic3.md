---
title: Vehicle Tracking in Warehouses via Bluetooth Beacon Angle-of-Arrival
subtitle: The objective of this work is to determine the method which allows for near-real-time tracking of the forklift, based on the Angle-of-Arrival of the Bluetooth beacons

# Summary for listings and search engines
summary: The objective of this work is to determine the method which allows for near-real-time tracking of the forklift, based on the Angle-of-Arrival of the Bluetooth beacons

# Link this post with a project
projects: []

# Date published
date: "2021-05-04T00:00:00Z"

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
- Bluetooth
- Localization

categories:
- Thesis
---

### Motivation

This proposal is presented in the context of a tracking system for forklifts based on Bluetooth beacons. The beacons are placed at fixed locations in a factory floor, and periodically send packets with their ID. The forklift is a moving vehicle, equipped with an antenna array which receives the beacons and can determine its stationary position on the warehouse floor by knowing the relative Angles-of-Arrival (AoA) of each incoming beacon.

So, the objective of this work is to determine the method which allows for near-real-time tracking of the forklift, based on the Angle-of-Arrival of the Bluetooth beacons.

### Proposed Work Plan

- Developing the algorithm/code required to process the incoming BLE beacon data taking into account the movement of the forklift, to allow for position calculation (i.e., movement tracking)
- Feed the simulator with arbitrary room and beacon arrangements, to evaluate the tracking performance for different number of beacons, beacon density, signal strength, forklift movement speed, etc.
- Determine the efficiency of the position tracking.
- Perform real-world testing of the algorithm. A moving platform, equipped with an antenna array and embedded micro-controller executing the positioning algorithm, will be moved through a hallway with BLE beacons. The real-world position tracking will be compared to the simulator. 

### Details

- Status: Completed
- Student: [Telmo Francisco da Costa Soares](https://sigarra.up.pt/feup/pt/vld_entidades_geral.entidade_pagina?pct_id=1352300)
- [Thesis Document](https://sigarra.up.pt/feup/pt/pub_geral.show_file?pi_doc_id=289569)

