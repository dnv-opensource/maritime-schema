# maritime-schema
Python package containing data classes and corresponding JSON schemata for common types used in generating traffic scenarios and testing of autonomous navigation systems.

The data classes in the package are implemented as data models using the [pydantic](https://docs.pydantic.dev/) framework. <br>
All data classes reside in subpackage `maritime_schema.types` and can be imported from there.


## Installation

```sh
pip install maritime-schema
```

## Usage Example

API:

```py
from maritime_schema.types import ...
```

CLI:

The JSON schemata are contained in the repository in folder ./schema
If you did not clone the repository but installed the maritime-schema package as a dependency in your project you can call `publish-schema` on the command line to (re-)generate the schemata:

```sh
publish-schema
```

The `publish-schema` command will generate the JSON schemata in `(current working directory)/schema` <br>
and a corresponding html documentation of the schemata in `(current working directory)/docs/schema`


_For more examples and usage, please refer to maritime-schema's [documentation][maritime_schema_docs]._

## Development Setup

1. Install Python 3.9 or higher, i.e. [Python 3.10](https://www.python.org/downloads/release/python-3104/) or [Python 3.11](https://www.python.org/downloads/release/python-3114/)

2. Update pip and setuptools:

    ```sh
    python -m pip install --upgrade pip setuptools
    ```

3. git clone the maritime-schema repository into your local development directory:

    ```sh
    git clone https://github.com/dnv-opensource/maritime-schema path/to/your/dev/maritime-schema
    ```

4. In the maritime-schema root folder:

    Create a Python virtual environment:

    ```sh
    python -m venv .venv
    ```

    Activate the virtual environment:

    ..on Windows:

    ```sh
    > .venv\Scripts\activate.bat
    ```

    ..on Linux:

    ```sh
    source .venv/bin/activate
    ```

    Update pip and setuptools:

    ```sh
    (.venv) $ python -m pip install --upgrade pip setuptools
    ```

    Install maritime-schema's dependencies:
    ```sh
    (.venv) $ pip install -r requirements-dev.txt
    ```
    This should return without errors.

    Finally, install maritime-schema itself, yet not as a regular package but as an _editable_ package instead, using the pip install option -e:
    ```sh
    (.venv) $ pip install -e .
    ```

5. Test that the installation works (in the maritime-schema root folder):

    ```sh
    (.venv) $ pytest .
    ```

## Meta

Copyright (c) 2024 [DNV](https://www.dnv.com) AS. All rights reserved.

Minos Hemrich - minos.hemrich@dnv.com

Tom Arne Pedersen - tom.arne.pedersen@dnv.com

Claas Rostock - [@LinkedIn](https://www.linkedin.com/in/claasrostock/?locale=en_US) - claas.rostock@dnv.com

Distributed under the MIT license. See [LICENSE](LICENSE.md) for more information.

[https://github.com/dnv-opensource/maritime-schema](https://github.com/dnv-opensource/maritime-schema)

## Contributing

1. Fork it (<https://github.com/dnv-opensource/maritime-schema/fork>)
2. Create your branch (`git checkout -b my-branch-name`)
3. Commit your changes (`git commit -am 'place a descriptive commit message here'`)
4. Push to the branch (`git push origin my-branch-name`)
5. Create a new Pull Request in GitHub

For your contribution, please make sure you follow the [STYLEGUIDE](STYLEGUIDE.md) before creating the Pull Request.

<!-- Markdown link & img dfn's -->
[maritime_schema_docs]: https://dnv-opensource.github.io/maritime-schema/README.html
