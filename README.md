# Maritime Schema

[**maritime-schema**](https://dnv-opensource.github.io/maritime-schema/) is a DNV initiative that establishes open formats and interfaces for collision avoidance testing, enabling industry collaboration in the field of Autonomous and Remotely Operated Ships.

The goal is to enable industry partners to share maritime traffic situations, and collision avoidance manuevers (or solutions) to these. 

Schemas and their corresponding documentation can be viewed [here](https://dnv-opensource.github.io/maritime-schema/).

- Schemas are located in the `schema` folder: 

    - [`schema/traffic_situation.json`](docs/schema/traffic_situation.html)
    - [`schema/situation_output.json`](docs/schema/traffic_situation.html)

- Schema HTML documentation is located in the `docs/schema` folder. 

    - [`docs/schema/traffic_situation.html`](docs/schema/traffic_situation.html)
    - [`docs/schema/situation_output.html`](docs/schema/traffic_situation.html)


**Note**  
Prior to release 0.0.7, maritime-schema also included pydantic classes for creating a schema in python. These have been migrated to [ship-traffic-gen](https://github.com/dnv-opensource/ship-traffic-generator/blob/main/src/trafficgen/types.py).



## Bulding the site

This repository contains the source code for the maritime-schema static site, built with Jekyll and hosted on GitHub Pages.

To build this site, please follow the instructions below.

### Prerequisites

Make sure you have the following installed on your local machine:

- Ruby
- Bundler
- Jekyll

### Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/dnv-opensource/maritime-schema.git
    cd maritime-schema
    ```

2. **Install the dependencies:**

    ```sh
    bundle install
    ```

### Usage

To serve the site locally, run:

```sh
bundle exec jekyll serve