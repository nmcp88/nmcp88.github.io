---
title: Indoor Bluetooth Low Energy Direction Finding via Circular Antenna Array

subtitle: This work is about indoor localization using Angle-of-Arrival in Blueetooth receivers.

# Summary for listings and search engines
summary: This work is about indoor localization using Angle-of-Arrival in Blueetooth receivers.

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
- Bluetooth
- Localization

categories:
- Thesis
---

### Context

This proposal is presented in the context of a tracking system for forklifts based on Bluetooth beacons. The beacons are placed at fixed locations in a factory floor, and periodically send packets with their ID. The forklift is a moving vehicle, equipped with an antenna array which receives the beacons and can determine its stationary position on the warehouse floor by knowing the relative Angles-of-Arrival (AoA) of each incoming beacon.

This work will address the implementation, design, and validation of a Bluetooth Low Energy (BLE) receiver device equipped with an antenna array (with 8 antennas). Based on phase differences of the same incoming signal, as observed by different antennas, the position of the receiver can be calculated assuming that the absolute positions of the fixed BLE beacons are known. 

Relying on BLE + AoA for indoor location provides a novel low-cost solution for indoor locatization, which currently relies on costly systems which require additional infrastructure, like Ultra Wide Band. 

### Objectives

This work will focus on the use of Bluetooth Low Energy (BLE) devices, and on the Angle-of-Arrival (AoA) of BLE transmissions to calculate the indoor location of a mobile receiver. 

### Proposed Work Plan

- Implementing the retreival of phase samples from the antenna array
- Implementing the necessary algorithms for calculation of phase differences for antenna pairs
- Transmission of data via UART to the host PC
- Implementing the calculation of the Angle-of-Arrival of each BLE transmission from the phase differences
- Characterizing the operation of the antenna array device
- Writting the dissertation

### Details

- Status: Completed
- Student: Catarina Alexandra Rodrigues Marques

#### References

- (Cominelli2019) Dead on Arrival: An Empirical Study of The Bluetooth 5.1 Positioning System. - https://doi.org/10.1145/3349623.3355475

- (NordicSemiconductors2020) White Paper - Direction Finding v1.1 - https://infocenter.nordicsemi.com/pdf/nwp_036.pdf

- (Pimenta2020), Master's Thesis, Indoor location based on AoA and Bluetooth Low Energy - https://repositorio-aberto.up.pt/handle/10216/132946

