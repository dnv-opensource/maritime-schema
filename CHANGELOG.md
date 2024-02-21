# Changelog

All notable changes to the [maritime-schema] project will be documented in this file.<br>
The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
* README.md : Under `Development Setup`, added a step to install current package in "editable" mode, using the pip install -e option.
This removes the need to manually add /src to the PythonPath environment variable in order for debugging and tests to work.

### Removed
* VS Code settings: Removed the setting which added the /src folder to PythonPath. This is no longer necessary. Installing the project itself as a package in "editable" mode, using the pip install -e option, solves the issue and removes the need to manually add /src to the PythonPath environment variable.

### Changed
* Moved all project configuration from setup.cfg to pyproject.toml
* Moved all tox configuration from setup.cfg to tox.ini.
* Moved pytest configuration from pyproject.toml to pytest.ini
* Deleted setup.cfg

### Dependencies
* updated to black[jupyter]==24.1  (from black[jupyter]==23.12)
* updated to version: '==24.1'  (from version: '==23.12')
* updated to ruff==0.2.1  (from ruff==0.1.8)
* updated to pyright==1.1.350  (from pyright==1.1.338)
* updated to sourcery==1.15  (from sourcery==1.14)


## [0.0.1] - 2024-01-11

* Initial release

### Added

* added this

### Changed

* changed that

### Dependencies

* updated to some_package_on_pypi>=0.1.0

### Fixed

* fixed issue #12345

### Deprecated

* following features will soon be removed and have been marked as deprecated:
    * function x in module z

### Removed

* following features have been removed:
    * function y in module z


<!-- Markdown link & img dfn's -->
[unreleased]: https://github.com/dnv-opensource/maritime-schema/compare/v0.0.2...HEAD
[0.0.2]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.1...v0.0.2
[0.0.1]: https://github.com/dnv-opensource/maritime-schema/releases/tag/v0.0.1
[maritime-schema]: https://github.com/dnv-opensource/maritime-schema
