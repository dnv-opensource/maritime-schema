---
layout: home
---
<div class="inline">
    <img src="{{ '/assets/images/logo.svg' | relative_url }}" alt="Site Logo" width="100" height="100">
    <h1>maritime-schema</h1>
     <img src="https://img.shields.io/badge/{{ site.version }}-brightgreen.svg" alt="Version Badge"
                style="margin-left: 10px;">
</div>

<br>

**maritime-schema** is a DNV initiative that establishes open formats and interfaces for collision avoidance testing, enabling industry collaboration in the field of Autonomous and Remotely Operated Ships.

The goal is to enable industry partners to share maritime traffic situations, and the resulting collision avoidance maneuvers to these situations.

The following schemas / file formats are defined within the maritime-schema:

1. **[Traffic Situation]({{ site.baseurl }}{% link pages/traffic_situation.md %})**
<br>
[![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)](#)  [![](https://img.shields.io/badge/version-{{ site.trafficSituation_version }}-brightgreen)](#)
<br>
Stores the initial scenario. Includes a planned route for an *own ship*, and pre-defined paths for *target ships*.

2. **[Situation Output]({{ site.baseurl }}{% link pages/situation_output.md %})**
<br>
[![JSON](https://img.shields.io/badge/JSON-000?logo=json&logoColor=fff)](#) [![](https://img.shields.io/badge/version-{{ site.situationOutput_version }}-brightgreen)](#)
<br>
The solution to a traffic situation, produced by a collision avoidance system. 

3. **[Simulation Output]({{ site.baseurl }}{% link pages/simulation_output.md %})**
<br>
[![](https://img.shields.io/badge/Arrow-ffea00?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0naHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmcnIHhtbG5zOnhsaW5rPSdodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rJyBjbGFzcz0nc3ZnbGl0ZScgd2lkdGg9JzEzNTAuMDBwdCcgaGVpZ2h0PScxMTgxLjI1cHQnIHZpZXdCb3g9JzAgMCAxMzUwLjAwIDExODEuMjUnPgo8ZGVmcz4KICA8c3R5bGUgdHlwZT0ndGV4dC9jc3MnPjwhW0NEQVRBWwogICAgLnN2Z2xpdGUgbGluZSwgLnN2Z2xpdGUgcG9seWxpbmUsIC5zdmdsaXRlIHBvbHlnb24sIC5zdmdsaXRlIHBhdGgsIC5zdmdsaXRlIHJlY3QsIC5zdmdsaXRlIGNpcmNsZSB7CiAgICAgIGZpbGw6IG5vbmU7CiAgICAgIHN0cm9rZTogIzAwMDAwMDsKICAgICAgc3Ryb2tlLWxpbmVjYXA6IHJvdW5kOwogICAgICBzdHJva2UtbGluZWpvaW46IHJvdW5kOwogICAgICBzdHJva2UtbWl0ZXJsaW1pdDogMTAuMDA7CiAgICB9CiAgXV0+PC9zdHlsZT4KPC9kZWZzPgo8cmVjdCB3aWR0aD0nMTAwJScgaGVpZ2h0PScxMDAlJyBzdHlsZT0nc3Ryb2tlOiBub25lOyBmaWxsOiBub25lOycvPgo8ZGVmcz4KICA8Y2xpcFBhdGggaWQ9J2NwTUM0d01Id3hNelV3TGpBd2ZEQXVNREI4TVRFNE1TNHlOUT09Jz4KICAgIDxyZWN0IHg9JzAuMDAnIHk9JzAuMDAnIHdpZHRoPScxMzUwLjAwJyBoZWlnaHQ9JzExODEuMjUnIC8+CiAgPC9jbGlwUGF0aD4KPC9kZWZzPgo8ZyBjbGlwLXBhdGg9J3VybCgjY3BNQzR3TUh3eE16VXdMakF3ZkRBdU1EQjhNVEU0TVM0eU5RPT0pJz4KPHJlY3QgeD0nMC4wMCcgeT0nMC4wMCcgd2lkdGg9JzEzNTAuMDAnIGhlaWdodD0nMTE4MS4yNScgc3R5bGU9J3N0cm9rZS13aWR0aDogMC43NTsnIC8+Cjxwb2x5Z29uIHBvaW50cz0nMTY4Ljc1LDE2OC43NSA1OTAuNjIsNTkwLjYyIDE2OC43NSwxMDEyLjUwIDE2OC43NSw4NDMuNzUgNDIxLjg4LDU5MC42MiAxNjguNzUsMzM3LjUwIDE2OC43NSwxNjguNzUgJyBzdHlsZT0nc3Ryb2tlLXdpZHRoOiAxLjA3OyBmaWxsOiAjMDAwMDAwOycgLz4KPHBvbHlnb24gcG9pbnRzPSc0NjQuMDYsMTY4Ljc1IDg4NS45NCw1OTAuNjIgNDY0LjA2LDEwMTIuNTAgNDY0LjA2LDg0My43NSA3MTcuMTksNTkwLjYyIDQ2NC4wNiwzMzcuNTAgNDY0LjA2LDE2OC43NSAnIHN0eWxlPSdzdHJva2Utd2lkdGg6IDEuMDc7IGZpbGw6ICMwMDAwMDA7JyAvPgo8cG9seWdvbiBwb2ludHM9Jzc1OS4zOCwxNjguNzUgMTE4MS4yNSw1OTAuNjIgNzU5LjM4LDEwMTIuNTAgNzU5LjM4LDg0My43NSAxMDEyLjUwLDU5MC42MiA3NTkuMzgsMzM3LjUwIDc1OS4zOCwxNjguNzUgJyBzdHlsZT0nc3Ryb2tlLXdpZHRoOiAxLjA3OyBmaWxsOiAjMDAwMDAwOycgLz4KPC9nPgo8L3N2Zz4=)](#)
 [![](https://img.shields.io/badge/version-{{ site.simulationOutput_version }}-brightgreen)](#)
<br>
If ship motions are simulated, the resulting data can be stored using the [Apache Arrow](https://arrow.apache.org/) tables defined in this section. 


4. **[Marzip]({{ site.baseurl }}{% link pages/marzip.md %})**
<br>
[![](https://img.shields.io/badge/marzip-ccea00?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIiBzdHJva2U9ImN1cnJlbnRDb2xvciIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIGNsYXNzPSJsdWNpZGUgbHVjaWRlLWZpbGUtYXJjaGl2ZSI+PHBhdGggZD0iTTEwIDEydi0xIi8+PHBhdGggZD0iTTEwIDE4di0yIi8+PHBhdGggZD0iTTEwIDdWNiIvPjxwYXRoIGQ9Ik0xNCAydjRhMiAyIDAgMCAwIDIgMmg0Ii8+PHBhdGggZD0iTTE1LjUgMjJIMThhMiAyIDAgMCAwIDItMlY3bC01LTVINmEyIDIgMCAwIDAtMiAydjE2YTIgMiAwIDAgMCAuMjc0IDEuMDEiLz48Y2lyY2xlIGN4PSIxMCIgY3k9IjIwIiByPSIyIi8+PC9zdmc+)](#)
 [![](https://img.shields.io/badge/version-{{ site.marzip_version }}-brightgreen)](#)
<br>
A Container file which stores the individual files together


<link rel="stylesheet" href="{{ '/assets/css/styles.css' | relative_url }}">
