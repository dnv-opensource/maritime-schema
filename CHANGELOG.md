# Changelog

All notable changes to the [maritime-schema] project will be documented in this file.<br>
The changelog format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [0.0.7 2025-02-14]

### Dependencies

### Added
-Initial setup with Jekyll and Minima theme.
-Added github-pages gem for GitHub Pages support.
-Included essential Jekyll plugins: jekyll-feed, jekyll-remote-theme, jekyll-sitemap, and jekyll-seo-tag.
-Added tzinfo and tzinfo-data for Windows and JRuby platforms.
-Included wdm gem for performance boost on Windows.
-Locked http_parser.rb gem to v0.6.x for JRuby builds.
-Added unf and webrick gems.

### Changed
- The maritime-schema repo now hosts the json schemata, and supporting HTML documentation. Pydantic classes have moved to the [ship-traffic-gen](https://github.com/dnv-opensource/ship-traffic-generator/blob/main/src/trafficgen/types.py) repository. 