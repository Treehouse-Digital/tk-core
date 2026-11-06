# Changelog

All notable Treehouse-Digital changes to this project will be documented in this file.
This also drives the auto-release GitHub (CI) workflow.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and the `-th.#.#.#` adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html),
but (as of [0.23.9-th.1.1.0]) versioned independently from the main project version so
that compatibility and features specific to Treehouse Digital are easily tracked.


## [0.24.6-th.1.3.0] - 2026-11-06

### Changed

- Simplified changes down to just the addition of `sgtk.platform.util.env_configs(context)`


## [0.23.9-th.1.2.2] - 2026-07-20

### Fixed

- Missing `__future__` import statement that's requirement by [0.23.9-th.1.1.0]


## [0.23.9-th.1.2.1] - 2026-07-20

### Fixed

- Version naming used so it's compatible with `pip install`


## [0.23.9-th.1.2.0] - 2026-07-20

### Added

- "Auto Release" GitHub workflow to automatically create a release from the latest version in `CHANGELOG.md` when changes are pushed to the main branch.
- This `CHANGELOG.md` file to track Treehouse-Digital specific changes and releases.


## [0.23.9-th.1.1.0] - 2026-06-23

### Added

- `sgtk.platform.util.env_configs(context)` for getting raw-ish serialized values from env YAML.

### Removed

- Upstreamed shotgunsoftware#1092: `sys.modules` name now set so `exec_module()` works as expected
