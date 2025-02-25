---
layout: default
title: Marzip
header_pages: 2
permalink: /marzip/
---

# Marzip

## Introduction

Marzip is a container format for storing collision avoidance related files. This is a normal zip file that
uses a custom extension (`.marzip`) to indicate the data stored is from the maritime domain. 

The following files make-up a marzip file: 

| **File**                 | **Description**                                 |
|--------------------------|-------------------------------------------------|
| `manifest.json`          | manifest file containing the marzip version.     |
| `traffic_situation.json` | the traffic situation, described [here]({% link pages/traffic_situation.md %}).          |
| `situation_output.json`  | the situation output, described [here]({% link pages/situation_output.md %}).           |
| `ship_static.arrow`      | part of the simulation output, described [here]({% link pages/simulation_output.md %}).  |
| `time_series.arrow`      | part of the simulation output, described [here]({% link pages/simulation_output.md %}).  |


## Compression 

To compress the marzip file, `DEFLATE` compression, or no compression (`STORE`)
can be used. To maximize compatibility, it is discouraged to use other compression types. 