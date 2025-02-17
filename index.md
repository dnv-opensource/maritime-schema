---
layout: default
title: maritime-schema
---
<div class="inline">
    <img src="{{ '/assets/images/logo.svg' | relative_url }}" alt="Site Logo" width="100" height="100">
    <h1>maritime-schema</h1>
</div>

<br>


**maritime-schema** is a DNV initiative that establishes open formats and interfaces for collision avoidance testing, enabling industry collaboration in the field of Autonomous and Remotely Operated Ships.

The goal is to enable industry partners to share maritime traffic situations, and collision avoidance manuevers (or solutions) to these. 

The following schemas / file formats are defined within the maritime-schema:

1. **[Traffic Situation]({{ site.baseurl }}{% link pages/traffic_situation.md %})**
<br>
[![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)](#)  [![](https://img.shields.io/badge/version-{{ site.trafficSituation_version }}-blue)](#)
<br>
Stores the initial scenario. Includes a planned route for an *own ship*, and pre-defined paths for *target ships*.

2. **[Situation Output]({{ site.baseurl }}{% link pages/situation_output.md %})**
<br>
[![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)](#) [![](https://img.shields.io/badge/version-{{ site.situationOutput_version }}-blue)](#)
<br>
The solution to a traffic situation, produced by a collision avoidance system. 

2. **[Marzip]({{ site.baseurl }}{% link pages/marzip.md %})**
<br>
[![](https://img.shields.io/badge/binary-ffea00?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWJpbmFyeSI+PHJlY3QgeD0iMTQiIHk9IjE0IiB3aWR0aD0iNCIgaGVpZ2h0PSI2IiByeD0iMiIvPjxyZWN0IHg9IjYiIHk9IjQiIHdpZHRoPSI0IiBoZWlnaHQ9IjYiIHJ4PSIyIi8+PHBhdGggZD0iTTYgMjBoNCIvPjxwYXRoIGQ9Ik0xNCAxMGg0Ii8+PHBhdGggZD0iTTYgMTRoMnY2Ii8+PHBhdGggZD0iTTE0IDRoMnY2Ii8+PC9zdmc+)](#)
 [![](https://img.shields.io/badge/version-{{ site.marzip_version }}-blue)](#)
<br>
If ship motions are simulated, and the data generated is large, marzip files allow for efficient encoding of timeseries data. 


<link rel="stylesheet" href="{{ '/assets/css/styles.css' | relative_url }}">
