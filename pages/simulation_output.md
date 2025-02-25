---
layout: default
title: Simulation Output
header_pages: 2
permalink: /simulation_output/
---

# Simulation Output

## Introduction

The Simulation output is intended to store the ship's motion during the simulation. Data is stored in 2 tables:
1. **Time series table**: Contains timeseries data relating to ships moving (e.g position, speed, heading).
2. **Static info table**: Contains static data about each ship (e.g length, width, IMO number).


## Format

As the number of data-points generated can be large, the simulation output is stored
in [Apache Arrow](https://arrow.apache.org/) tables. These store data in a 
binary format, providing a good compromise between serialization speed and file size. The tables are named as follows:

1.  **Time series table**: `time_series.arrow`.
2.  **Static info table**: `ship_static.arrow`.

The arrow tables are serialized to a file using [*Interprocess
Communication*
(IPC)](https://arrow.apache.org/docs/format/Columnar.html#serialization-and-interprocess-communication-ipc).
There are 2 formats of IPC:

  - IPC File Format

  - IPC Streaming Format

Tables are to be written in the IPC File Format. There exist several
libraries in different programming languages (C, C++, C\#, Java,
JavaScript, Julia, MATLAB, Python, R, Ruby, Rust), which can write data
into an IPC file.

### Compression

Apache Arrow supports a range of compression formats (SNAPPY, GZIP,
BROTLI, LZ4, ZSTD). However, as compression is not available for all
implementations (such as JavaScript), it’s recommended **not** to use
any compression on the Arrow Table itself, but rather apply DEFLATE
compression on the zip file, if necessary.

### Units

Unless otherwise specified, SI and SI-derived units shall be used.

When using degrees, absolute bearings shall be used where possible.

## Versioning

The version can be specified in the table metadata. 

## Time series Arrow Table {#timeseries_arrow}

The following columns have been defined. Additional columns are allowed.


| Column Name                                                                                                     | Mapped Arrow Type       | Description                                                                                                                | required | Unit                   |
| --------------------------------------------------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------- | ---------------------- |
| id                                                                                                              | UInt32                  | An id uniquely identifies a ship.                                                                                          | true     |                        |
| timeStamp<sup>1</sup>                                                                                           | Timestamp (nanoseconds) | Timestamp stored in nanoseconds (“us”). Use nanoseconds to avoid casting issues. Time Zone can be omitted or be UTC+00:00. | true     | us                     |
| lat<sup>1</sup>                                                                                                 | Float64                 | WGS-84 latitude encoded in decimal form.                                                                                   | true     | WGS-84 decimal degrees |
| lon<sup>1</sup>                                                                                                 | Float64                 | WGS-84 longitude encoded in decimal form.                                                                                  | true     | WGS-84 decimal degrees |
| sog<sup>1</sup>                                                                                                 | Float32                 | Speed over ground in meters per second.                                                                                    | true     | knots                  |
| cog<sup>1</sup>                                                                                                 | Float32                 | Course over ground (COG) ([absolute bearing](https://en.wikipedia.org/wiki/Bearing_\(navigation\)#Absolute)).              | true     | Degrees                |
| heading<sup>1</sup>                                                                                             | Float32                 | Heading of ship's bow ([absolute bearing](https://en.wikipedia.org/wiki/Bearing_\(navigation\)#Absolute)).                 | true     | Degrees                |
| rot<sup>1</sup>                                                                                                 | Float32                 | Rate of turn of the ship.                                                                                                  | false    | Degrees per second     |
| navStatus[<sup>3</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=111) | UInt8                   | AIS Navigational status (1-15).                                                                                            | false    |                        |
| surgeAcc<sup>4</sup>                                                                                            | Float32                 | Vessel Acceleration (surge motion)                                                                                         | false    | ms-2                   |
| swayAcc<sup>4</sup>                                                                                             | Float32                 | Vessel Acceleration (sway motion)                                                                                          | false    | ms-2                   |
| heaveAcc<sup>4</sup>                                                                                            | Float32                 | Vessel Acceleration (heave motion)                                                                                         | false    | ms-2                   |
| rollAcc<sup>4</sup>                                                                                             | Float32                 | Vessel Rotational Acceleration (roll)                                                                                      | false    | rad/s-2                |
| pitchAcc<sup>4</sup>                                                                                            | Float32                 | Vessel Rotational Acceleration (pitch)                                                                                     | false    | rad/s-2                |
| yawAcc<sup>4</sup>                                                                                              | Float32                 | Vessel Rotational Acceleration (yaw)                                                                                       | false    | rad/s-2                |

<sup>1</sup> <sub>Column names originating from ISO 19848:2024.</sub>

<sup>2</sup> <sub>Column names defined by DNV.</sub>

<sup>3</sup> <sub>Defined in ITU-R M.1371-5 § 3.1.</sub>

<sup>4</sup> <sub>not yet implemented, to be considered later.</sub>

Additional fields may be added to the table. If possible, column names
shall be aligned with ISO 19848:2024.

It is recommended to sort the table first by *id*, then *timeStamp* for
maximum compatibility.

## Static Info Arrow Table {#static_arrow}

The following columns have been defined. Additional columns are allowed.

| Column Name                                                                                                                      | Mapped Arrow Type       | Used in AIS | Description                                                               | Unit   |
| -------------------------------------------------------------------------------------------------------------------------------- | ----------------------- | ----------- | ------------------------------------------------------------------------- | ------ |
| id                                                                                                                               | UInt32                  | false       | An id uniquely identifies a ship.                                         |        |
| mmsi                                                                                                                             | UInt32                  | true        | Maritime mobile service identity.                                         |        |
| imo                                                                                                                              | UInt32                  | true        | International Maritime Organization number.                               |        |
| callsign                                                                                                                         | Utf-8                   | true        | Ship callsign.                                                            |        |
| name                                                                                                                             | Utf-8                   | true        | Ship name.                                                                |        |
| stationType[<sup>1</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=138)                | UInt8                   | true        | Type of AIS Station (Class A, Class B, AtoN, etc.)                        |        |
| shipType[<sup>2</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=116)                   | UInt8                   | true        |                                                                           |        |
| cargoType[<sup>2</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=116)                  | UInt8                   | true        |                                                                           |        |
| width                                                                                                                            | Float32                 | true        | Ship width.                                                               | meters |
| length                                                                                                                           | Float32                 | true        | Ship length.                                                              | meters |
| draught                                                                                                                          | Float32                 | true        | Maximum present static draught.                                           | meters |
| typeOfPositionFixingDevice[<sup>3</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=130) | UInt8                   | true        | Type of electronic position fixing device.                                |        |
| destination<sup>5</sup>                                                                                                          | Utf-8                   | true        | The current ship destination. e.g. “Oslo”.                                |        |
| eta<sup>5</sup>                                                                                                                  | Timestamp (nanoseconds) | true        | Estimated time of arrival at the destination.                             | us     |
| a[<sup>4</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=117)                          | Float32                 | true        | Reference point for reported position and overall dimensions of ship (a). | meters |
| b[<sup>4</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=117)                          | Float32                 | true        | Reference point for reported position and overall dimensions of ship (b). | meters |
| c[<sup>4</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=117)                          | Float32                 | true        | Reference point for reported position and overall dimensions of ship (c). | meters |
| d[<sup>4</sup>](https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1371-5-201402-I!!PDF-E.pdf#page=117)                          | Float32                 | true        | Reference point for reported position and overall dimensions of ship (d). | meters |
| ownShip                                                                                                                          | Boolean                 | false       | If the given ship is the own ship.                                        |        |

<sup>1</sup> Defined in ITU-R M.1371-5 § 3.21.

<sup>2</sup> Defined in ITU-R M.1371-5 § 3.3.2.

<sup>3</sup> Defined in ITU-R M.1371-5 § 3.3.

<sup>4</sup> Defined in ITU-R M.1371-5 § 3.3.3.

<sup>5</sup> Technically not time-series data but changes infrequently.
Not currently a focus and hence kept as static data.

Additional fields may be added to the table. If possible, column names
shall be aligned with ISO 19848:2024.
