---
layout: default
title: Baseline Situations
permalink: /baseline_situations/
---

# Baseline Situations

<table>
  <tr>
    <th>Traffic Situation</th>
    <th>Link</th>
  </tr>
  {% for i in (1..55) %}
    {% assign formatted_i = i | plus: 100 | slice: -2, 2 %}
    <tr>
      <td>Traffic situation {{ formatted_i }}</td>       
      <td><a href="https://raw.githubusercontent.com/dnv-opensource/ship-traffic-generator/refs/heads/main/data/baseline_situations_generated/traffic_situation_{{ formatted_i }}.json" download>Download</a></td>
    </tr>
  {% endfor %}
</table>