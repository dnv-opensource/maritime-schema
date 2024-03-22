# Changelog

All notable changes to the [maritime-schema] project will be documented in this file.<br>
The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

-   -/-


## [0.0.5] - 2024-03-22

### Changed

-   replaced black formatter with ruff formatter
-   src/maritime_schema/types/caga.py: class ShipStatic(): set the length, width, and shipType fields as Optional.
-   src/maritime_schema/types/caga.py: class TrafficSituation(): set the title field as Optional.
-   src/maritime_schema/types/caga.py: class Ship(): updated the waypoint field, so that if the class has initial data without waypoints, they will automatically be created.

### Dependencies

-   added pyproj==3.6.1 (used for geodesic calculations)
-   updated to ruff==0.3.0 (from ruff==0.2.1)
-   updated to pyright==1.1.352 (from pyright==1.1.350)
-   removed black


## [0.0.4] - 2024-02-28

### Changed

-   src/maritime_schema/types/caga.py: class Initial(): Marked several fields as optional.

## [0.0.3] - 2024-02-27

### Added

-   Created a CLI script `publish-schema`, which re-generates the schema files.
-   README.md:
    -   Added some introductory guidance.
    -   Under `Development Setup`, added a step to install current package in "editable" mode, using the pip install -e option.
        This removes the need to manually add /src to the PythonPath environment variable in order for debugging and tests to work.
-   Created an icon for the documentation
-   Added authors to README.md, pyproject.toml and to the Sphinx documentation

### Removed

-   VS Code settings: Removed the setting which added the /src folder to PythonPath. This is no longer necessary. Installing the project itself as a package in "editable" mode, using the pip install -e option, solves the issue and removes the need to manually add /src to the PythonPath environment variable.

### Changed

-   Moved all project configuration from setup.cfg to pyproject.toml
-   Moved all tox configuration from setup.cfg to tox.ini.
-   Moved pytest configuration from pyproject.toml to pytest.ini
-   Deleted setup.cfg

### Dependencies

-   updated to black[jupyter]==24.1 (from black[jupyter]==23.12)
-   updated to version: '==24.1' (from version: '==23.12')
-   updated to ruff==0.2.1 (from ruff==0.1.8)
-   updated to pyright==1.1.350 (from pyright==1.1.338)
-   updated to sourcery==1.15 (from sourcery==1.14)

## [0.0.2] - 2024-01-11

-   Test release

## [0.0.1] - 2024-01-11

-   Initial release

### Added

-   added this

### Changed

-   changed that

### Dependencies

-   updated to some_package_on_pypi>=0.1.0

### Fixed

-   fixed issue #12345

### Deprecated

-   following features will soon be removed and have been marked as deprecated:
    -   function x in module z

### Removed

-   following features have been removed:
    -   function y in module z

<!-- Markdown link & img dfn's -->
[unreleased]: https://github.com/dnv-opensource/maritime-schema/compare/v0.0.5...HEAD
[0.0.5]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.4...v0.0.5
[0.0.4]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.3...v0.0.4
[0.0.3]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.2...v0.0.3
[0.0.2]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.1...v0.0.2
[0.0.1]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.1
[maritime-schema]: https://github.com/dnv-opensource/maritime-schema
