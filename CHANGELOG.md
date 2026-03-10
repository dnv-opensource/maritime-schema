# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.2.0] - 2026-03-05

### Changed

- **Breaking** (Situation Output): Renamed `systemUnderTest.eventData[].route` to `systemUnderTest.eventData[].waypoints` for clarity and consistency.
- **Breaking** (Situation Output): Removed the `trafficSituation` key from the Situation Output.
- **Breaking** (Traffic Situation): made `ownShip.waypoints` a required field.
- (Traffic Situation): made `ownShip.initial` fields optional.
- (Situation Output): `simulator.eventData` items now use the base `Event` type instead of a stricter `SimulatorEvent` type, allowing additional properties.
- For simplicity, a single version number is used across all schemas in `maritime-schema`. 

### Removed

- (Situation Output): Removed the `SimulatorEvent` type constraint on `simulator.eventData[]` items (replaced by generic `Event` type).
- (Situation Output): Removed `creationTime` key.



### Fixed

- Updated property descriptions within `*.static.dimensions`, `systemUnderTest.eventData[].targetShips[]`, and `*.initial` (ship state fields).

## [0.1.0] - 2025-02-14

### Changed

- The maritime-schema repo now hosts the json schemata, and supporting HTML documentation. Pydantic classes have moved to the [ship-traffic-gen](https://github.com/dnv-opensource/ship-traffic-generator/blob/main/src/trafficgen/types.py) repository.