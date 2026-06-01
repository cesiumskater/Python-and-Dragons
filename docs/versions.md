# Release Map & History Recovery

> 📖 New here? Start with the main [README](../README.md) — the project's single source of truth.

The repository previously kept a separate `vX.Y.Z/` folder for every release
(~140 MB of duplicated game files). Those historical folders have been **removed
from the working tree** to keep the repo lean — but **nothing was lost**. Every
release is preserved in git history and can be retrieved at any time.

Only the **current** release lives in the tree, under [`v2.2.0/`](../v2.2.0/).

For the *why* and the broader strategy, see
[version-history.md](version-history.md#documentation--cleanup-strategy).

---

## How to retrieve any historical version

Each release is recoverable two ways. **Tags** are the friendly handle; the
**commit SHA** always works even if tags haven't been pushed yet.

```bash
# By tag (after the tags have been pushed — see note below):
git checkout v1.3.0           # working tree now contains the old V1.3.0/ folder

# By commit SHA (always works, no tags required):
git checkout 54daf0e          # the "Historical Releases" snapshot (all v0–v1.3.0 folders)

# Just extract one folder without switching branches:
git restore --source=54daf0e --staged --worktree -- "V1.3.0"
# (older git: git checkout 54daf0e -- "V1.3.0")
```

> **Note on tags:** annotated tags for every version were created during cleanup
> but **could not be pushed** from the cleanup environment (the sandbox git proxy
> rejects tag pushes with HTTP 403). Run
> [`scripts/create-release-tags.sh`](../scripts/create-release-tags.sh) from a
> machine with push access to publish them (and, with `--releases`, to create
> draft GitHub Releases). Until then, use the commit SHAs below.

## Release → tag → commit map

| Version | Tag | Commit | Lived in folder | Notes |
|---------|-----|--------|-----------------|-------|
| Prototype (Serpent's Code) | `v0.0.4` | `54daf0e` | `v0.0.X/` | 5 prototype iterations (`v0_0_0`–`v0_0_4`) |
| 1.1.0 | `v1.1.0` | `54daf0e` | `v1.1.0/` | Enhanced Edition: Story/Reference modes, TOC |
| 1.1.1 | `v1.1.1` | `54daf0e` | `v1.1.1/` | |
| 1.1.2 | `v1.1.2` | `54daf0e` | `v1.1.2/` | Cybersecurity topics, Zen of Python |
| 1.1.3 | `v1.1.3` | `54daf0e` | `v1.1.3/` | |
| 1.1.4 | `v1.1.4` | `54daf0e` | `v1.1.4/` | (game file retained the 1.1.3 name) |
| 1.1.5 | `v1.1.5` | `54daf0e` | `v1.1.5/` | "The Lost Language": Unicode + list mini-game |
| 1.2.0 | `v1.2.0` | `54daf0e` | `v1.2.0/` | "Zero to Enterprise": Acts 0, VIII, IX; assessment |
| 1.2.1 | `v1.2.1` | `54daf0e` | `v1.2.1/` | Onboarding polish |
| 1.2.2 | `v1.2.2` | `54daf0e` | `v1.2.2/` | Acts 0–VIII complete; Act IX authored. (Also held ~96 MB of backup/fix-script clutter — not carried forward.) |
| 1.3.0 | `v1.3.0` | `54daf0e` | `V1.3.0/` | "The Complete Journey": all 181 lessons registered |
| 2.0.0 | `v2.0.0` | `e106f29` | `v2.0.0/` | Master Edition; syntax/quote fixes; production-ready |
| 2.1.0 | `v2.1.0` | `3897384` | `v2.1.0/` | Bug fixes, PEP 8 |
| 2.1.1 | `v2.1.1` | `2c27165` | `v2.1.1/` | 3,439 tests passing |
| 2.1.2 | `v2.1.2` | `539c6c4` | `v2.1.2/` | PEP 8 & PEP 20 |
| 2.1.3 | `v2.1.3` | `dd3f0a1` | `v2.1.3/` | 5,611 tests passing |
| 2.1.4 | `v2.1.4` | `1b84552` | `v2.1.4/` | Menu navigation fixes |
| 2.1.5 | `v2.1.5` | `8c0de0e` | `v2.1.5/` | Reference Mode lesson flow |
| 2.1.6 | `v2.1.6` | `4bcdaaa` | `v2.1.6/` | Testing verification |
| **2.2.0** | `v2.2.0` | `8ea1d67` | **`v2.2.0/` (current, in tree)** | Code cleanup — the release you can run today |

> The historical `v0–v1.3.0` releases all entered the repository in a single
> "Historical Releases" commit (`54daf0e`), so their tags share that commit.
> Checking it out yields a tree containing all of those folders at once.

## What's in the tree today

```
Python-and-Dragons/
├── README.md
├── CHANGELOG.md
├── docs/
├── scripts/create-release-tags.sh   # publish the per-release tags/Releases
└── v2.2.0/                           # the current, runnable release
```

> The original prototype (`Pythons and Dragons1.0.py`) and a stale sample save
> (`game_progress.json`) used to sit at the root; both were removed for a clean
> root and remain recoverable from history (e.g.
> `git checkout 8ea1d67 -- "Pythons and Dragons1.0.py"`).

## Quick reference: which file do I run?

- **Just want to play?** → `v2.2.0/The Verdant Code 2.2.0.py`
- **Want a historical version?** → check out its commit/tag from the table above.
- **Studying the evolution?** → see [version-history.md](version-history.md#at-a-glance)
  and the [CHANGELOG](../CHANGELOG.md).
