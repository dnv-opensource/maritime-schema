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
| `traffic_situation.json` | the traffic situation, described [here]({{ '/traffic_situation' | relative_url }}).          |
| `situation_output.json`  | the situation output, described [here]({{ '/situation_output' | relative_url }}).           |
| `ship_static.arrow`      | part of the simulation output, described [here]({{ '/simulation_output' | relative_url }}).  |
| `time_series.arrow`      | part of the simulation output, described [here]({{ '/simulation_output' | relative_url }}).  |

## Compression 

To compress the marzip file, `DEFLATE` compression, or no compression (`STORE`)
can be used. To maximize compatibility, it is discouraged to use other compression types. 