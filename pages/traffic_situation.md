---
layout: default
title: Traffic Situation
permalink: /traffic_situation/
---

# Traffic Situation

## Introduction
A **Traffic Situation** describes a situation in the maritime domain with actors and elements. This typically consists of an own ship (ego ship) and a target ships (non-ego ships). The own ship must take appropriate actions to avoid collisions with target ships.

<div class="button-container">

<a id="schema-link" href="/docs/schema/traffic_situation.html">
<button id="fullscreen-button" class="btn" name="button">
    <i data-lucide="file-json"></i> &nbsp; View Schema
</button>
</a>

<a id="download-schema-link" href="/schema/traffic_situation.json" download>
        <button id="download-schema-button" class="btn" name="button">
            <i data-lucide="download"></i> &nbsp; Download Schema
        </button>
    </a>
</div>


&nbsp;
## Example

<a id="download-schema-link" href="/schema/traffic_situation_example.json" download>
        <button id="download-example-button" class="btn" name="button">
            <i data-lucide="download"></i> &nbsp; Example JSON
        </button>
    </a>


```js
{
    "version": "0.0.7",
    "title": "Example",
    "description": "An example traffic situation.",
    "startTime": "2025-01-01T00:00:00",
    "ownShip": {
        "initial": {
            "position": {
                "lon": 10.59,
                "lat": 58.61
            },
            "sog": 10.0,
            "cog": 199.0,
            "heading": 200.0,
            "navStatus": "Under way using engine"
        },
        "waypoints": [
            {
                "position": {
                    "lon": 10.59,
                    "lat": 58.61
                }
            },
            {
                "position": {
                    "lon": 10.282925767380412,
                    "lat": 58.13799537029509
                }
            }
        ],
        "static": {
            "id": 0,
            "mmsi": 999999999,
            "imo": 9999999,
            "name": "Fishing Boat 1",
            "dimensions": {
                "length": 100.0,
                "width": 20.0,
                "a": 50.0,
                "b": 50.0,
                "c": 10.0,
                "d": 10.0
            },
            "shipType": "Fishing"
        }
    },
    "targetShips": []
}
```

<!-- ## Waypoints
Waypoints follow the general conventions of the *[Route plan exchange format](https://cirm.org/rtz-xml-schemas)*. 

## Modelling Speed Changes

Each waypoint leg can have a `sog` property. This can be set to a single value. However, this does not allow for smooth speed changes between waypoints. To model speed changes, the following parameters can be used:

`data.sog.value` New leg speed.

`data.sog.interpPrev` Distance before the leg change, to start 
interpolating to the new value.

`data.sog.interpNext` Distance after the leg change, to start interpolating to the new value.

`data.sog.interpMethod` Method to use for interpolation. 


<img src="/assets/images/Interpolation1.png" alt="Interpolation" width="400"/>

<img src="/assets/images/Interpolation2.png" alt="Interpolation" width="500"/>

-->

<script src="https://unpkg.com/lucide@latest"></script>

<script>
lucide.createIcons();
</script>


<link rel="stylesheet" href="{{ '/assets/css/styles.css' | relative_url }}"> 
