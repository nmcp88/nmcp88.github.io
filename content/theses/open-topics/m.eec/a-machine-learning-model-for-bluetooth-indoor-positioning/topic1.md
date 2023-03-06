---
title: A Machine Learning Model for Indoor Positioning of Bluetooth Receivers

subtitle: This work is about applying machine learning to indoor location and tracking.

# Summary for listings and search engines
summary: This work is about applying machine learning to indoor location and tracking.

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
- Bluetooth
- Machine Learning
- Localization

categories:
- Thesis
---

### Context

This proposal is presented in the context of a tracking system for forklifts (and other indoor factory floor machinery) based on Bluetooth beacons. The beacons are placed at fixed locations in a factory floor, and periodically send packets with their ID.

The forklift is a moving vehicle, equipped with an antenna array which receives the beacons and can determine its stationary position on the warehouse floor by knowing the relative Angles-of-Arrival (AoA) of each incoming beacon. For example, if the factory has one Bluetooth beacon in each corner of a square floor, the forklift can compute its position after receiving all 4 beacons. By knowing the Angle-of-Arrival of each transmission, the position of the forklift can be determined. 

### Objectives

This work aims to study machine learning models to estimate the Angle-of-Arrival of transmissions, based on data related to the phase of the signals that is captured by the antenna array of a receiver board.

### Proposed Work Plan

- Estimation of angle of arrival from phase differences
- Generate synthetic datasets (with different levels of noise) for use in a regression algorithm which can estimate an Angle-of-Arrival from a set of phase differences
- Design an adequate regression algorithm (decision tree, SVM, NN, etc)
- Tune and evaluate the classification accuracy of the model 

- Estimation of final receiver position from a set of angles (i.e., outputs of the previous classifier)
- Generate datasets where a set of angles corresponds to a given ground-truth position
- Design an adequate regression algorithm (decision tree, SVM, NN, etc)
- Tune and evaluate the classification accuracy of the model

- Experiment with integration of the inference model with an existing position and tracking simulator and/or an existing receiver board with 8 antennas, and evaluate the achievable positioning accuracy 

### Details

- Status: Open!
- Student: None (yet).


