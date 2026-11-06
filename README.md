# Treehouse Digital's fork of tk-core

Custom fork of [shotgunsoftware/tk-core](https://github.com/shotgunsoftware/tk-core). Use by editing
[tk-config-default2:core/core_api.yml](https://github.com/shotgunsoftware/tk-config-default2/blob/master/core/core_api.yml)
to:

```yaml
location:
  type: github_release
  organization: Treehouse-Digital
  repository: tk-core
  version: 0.23.9-th.1.2.0
```

For standalone, use [pip Git VCS URL](https://pip.pypa.io/en/stable/topics/vcs-support/#vcs-support)

```bash
pip install 'git+https://github.com/Treehouse-Digital/tk-core@0.23.9-th.1.2.0'
```

## Developing

### Syncing with SG

Then `cd` into this repo and add [shotgunsoftware/tk-core](https://github.com/shotgunsoftware/tk-core) as the `upstream` remote, which we'll then use as pull only (one-time setup):

```bash
cd /path/to/tk-core
git remote add upstream git@github.com:shotgunsoftware/tk-core.git
git remote set-url --push upstream PUSH-NOT-ALLOWED
git remote update
```

Afterwards, suppose new SG/upstream version tag `v1.2.3` appears, merge the latest version tag into our changes before tagging and pushing both SG's tag, our updated `master` and our Rez-compatible tag back to our fork (origin)

```bash
git checkout -B master origin/master  # Force sync with our GitHub fork
git merge v1.2.3
git tag 1.2.3-th.1.0.0  # Rez-compatible version number
git push origin master v1.2.3 1.2.3-th.1.0.0  # Push branch, SG tag and our tag
```

Optionally, then go to https://github.com/Treehouse-Digital/tk-core/releases/new and
create a new release with the `1.2.3-th.1.0.0` tag.

### Additional changes

Each change should branch off SG's `v#.#.#` tag as per above. The branch should be
named `th-#.#.#` i.e. `th-0.23.2` when branching off SG `v0.23.2`.

`master` branch should point to the latest tip of `th-#.#.#` where possible.

Any additional changes can then be made and pushed to the `th-#.#.#` branch
(and `master` if latest) and released as using sem-ver version numbering after a
`-th.` segment. Be sure to update the changelog below.

## Versioning

Starting from `0.23.9-th.1.1.0`, our own `-th.#.#.#` versioning stream is independent of SG's `v#.#.#`, but includes it in the full version number/tag for clarity on what SG version each `th` release is based on.

> [!NOTE]
> Although `#.#.#-th.#.#.#` is used on GitHub, it's not a valid [Python packaging Version name](https://packaging.python.org/en/latest/specifications/version-specifiers).
>
> `#.#.#+th.#.#.#` is used instead internally during `pip install`.

See:

- [Releases](https://github.com/Treehouse-Digital/tk-core/releases)
- [CHANGELOG.md](https://github.com/Treehouse-Digital/tk-core/blob/master/CHANGELOG.md)

----

[![Supported VFX Platform: CY2022 - CY2026](https://img.shields.io/badge/VFX_Reference_Platform-CY2022_|_CY2023_|_CY2024_|_CY2025_|_CY2026-blue)](http://www.vfxplatform.com/ "Supported VFX Reference Platform versions")
[![Supported Python versions: 3.9, 3.10, 3.11, 3.13](https://img.shields.io/badge/Python-3.9_|_3.10_|_3.11_|_3.13-blue?logo=python&logoColor=f5f5f5)](https://www.python.org/ "Supported Python versions")
[![Reference Documentation](http://img.shields.io/badge/doc-reference-blue.svg)](http://developer.shotgridsoftware.com/tk-core)

[![Build Status](https://dev.azure.com/shotgun-ecosystem/Toolkit/_apis/build/status/shotgunsoftware.tk-core?branchName=master)](https://dev.azure.com/shotgun-ecosystem/Toolkit/_build/latest?definitionId=38&branchName=master)
[![codecov](https://codecov.io/gh/shotgunsoftware/tk-core/branch/master/graph/badge.svg)](https://codecov.io/gh/shotgunsoftware/tk-core)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

# Flow Production Tracking Core API

This repository represents the Flow Production Tracking Core API.

## Getting started with the Flow Production Tracking

Installing the Flow Production Tracking is normally done via our
Flow Production Tracking App Store. For detailed instructions on how to get started
with Toolkit, head over to our support site:
https://help.autodesk.com/view/SGDEV/ENU/?contextId=PG_INTEGRATIONS_TOOLKIT_OVERVIEW

## Reference Documentation and Release Notes

For our *latest released API Documentation*, head over to the Toolkit App Store:
https://help.autodesk.com/view/SGDEV/ENU/?contextId=SA_INTEGRATIONS_USER_GUIDE

For legacy/historical information about older releases, see:
https://github.com/shotgunsoftware/tk-core/wiki/Release-Notes

Release Notes for the Core API can be found here:
https://github.com/shotgunsoftware/tk-core/releases
