# Maritime Schema

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE.md)
[![Version](https://img.shields.io/badge/version-0.2.0-blue.svg)](https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.2.0)

[**maritime-schema**](https://dnv-opensource.github.io/maritime-schema/) is a DNV initiative that establishes open formats and interfaces for collision avoidance testing, enabling industry collaboration in the field of Autonomous and Remotely Operated Ships.

The goal is to enable industry partners to share maritime traffic situations, and solutions (collision avoidance maneuvers) to these situations.

> **Full documentation and interactive schema viewers are available at [dnv-opensource.github.io/maritime-schema](https://dnv-opensource.github.io/maritime-schema/).**

## Schemas

| Schema | Description | File |
|--------|-------------|------|
| **Traffic Situation** | Stores the initial scenario with own ship waypoints and target ship paths. | [`schemas/traffic_situation.json`](schemas/traffic_situation.json) |
| **Situation Output** | The solution produced by a collision avoidance system. | [`schemas/situation_output.json`](schemas/situation_output.json) |
| **Simulation Output** | Ship motion simulation data stored as Apache Arrow tables. | See [documentation](https://dnv-opensource.github.io/maritime-schema/simulation_output) |
| **Marzip** | A container file format that bundles multiple schema files together. | See [documentation](https://dnv-opensource.github.io/maritime-schema/marzip) |

## Examples

Example JSON files conforming to each schema are provided in the [`examples/`](examples/) folder:

- [`examples/traffic_situation.json`](examples/traffic_situation.json) — A sample traffic situation scenario
- [`examples/situation_output.json`](examples/situation_output.json) — A sample collision avoidance output

## Website

The documentation can be found  at [dnv-opensource.github.io/maritime-schema](https://dnv-opensource.github.io/maritime-schema/).
## Related Projects

- [ship-traffic-generator](https://github.com/dnv-opensource/ship-traffic-generator) — Python library for generating traffic situations. Includes pydantic classes that were previously part of this repo (prior to v0.0.7).

## License

This project is licensed under the [MIT License](LICENSE.md).

Copyright (c) 2026 [DNV](https://www.dnv.com)
