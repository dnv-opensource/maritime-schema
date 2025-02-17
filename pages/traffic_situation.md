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

<script src="https://unpkg.com/lucide@latest"></script>

<script>
lucide.createIcons();
</script>


<link rel="stylesheet" href="{{ '/assets/css/styles.css' | relative_url }}">
