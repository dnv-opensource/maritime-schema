# maritime-schema
Python package containing data classes and corresponding JSON schemata for common types used in generating traffic scenarios and testing of autonomy

maritime-schema supports
* ..


## Installation

```sh
pip install .
```

## Usage Example

API:

```py
from maritime_schema import ...
```

CLI:

```sh
maritime-schema ...
```

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

5. Setup your development environment to locate Python source codes:

    For example, Visual Studio Code on Windows assumes the Python environment is specified in a `.env` file. <br>
    If you are developing and running the Python code from VSCode, make sure to create a `.env` file in the maritime-schema root folder with below content. <br>
    Set the path for `PROJ_DIR` to where your maritime-schema folder is on your system. <br>
    _Note_: `.env` is part of `.gitignore`, such that you do not commit your `.env` file to the repository.

    ```ini
    PROJ_DIR=<path-to-maritime-schema-root-dir>
    PYTHONPATH=${PROJ_DIR}/src
    ```

6. Test that the installation works (in the maritime-schema root folder):

    ```sh
    (.venv) $ pytest .
    ```

## Meta

Copyright (c) 2024 [DNV](https://www.dnv.com) [open source](https://github.com/dnv-opensource)

Author One - [@LinkedIn](https://www.linkedin.com/in/authorone) - author.one@dnv.com

Author Two - [@LinkedIn](https://www.linkedin.com/in/authorthree) - author.two@dnv.com

Claas Rostock - [@LinkedIn](https://www.linkedin.com/in/claasrostock/?locale=en_US) - claas.rostock@dnv.com

Distributed under the MIT license. See [LICENSE](LICENSE.md) for more information.

[https://github.com/dnv-opensource/maritime-schema](https://github.com/dnv-opensource/maritime-schema)

## Contributing

1. Fork it (<https://github.com/AuthorOne/maritime-schema/fork>)
2. Create your branch (`git checkout -b my-branch-name`)
3. Commit your changes (`git commit -am 'place a descriptive commit message here'`)
4. Push to the branch (`git push origin my-branch-name`)
5. Create a new Pull Request in GitHub

For your contribution, please make sure you follow the [STYLEGUIDE](STYLEGUIDE.md) before creating the Pull Request.

<!-- Markdown link & img dfn's -->
[maritime_schema_docs]: https://AuthorOne.github.io/maritime-schema/README.html
