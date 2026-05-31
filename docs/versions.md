# Version Folder Map

A guided index of every versioned folder in the repository. Each `vX.Y.Z/` folder
is a **frozen historical snapshot** of that release — its game file plus the
documentation written for it at the time. This map lets you find what you need
without opening twenty folders.

For the *why* behind keeping (and eventually archiving) these folders, see the
[cleanup strategy](version-history.md#documentation--cleanup-strategy).

> **Legend:** 🎮 = runnable game file · 📄 = documentation · 🧰 = dev/utility
> scripts (not part of the game)

---

## Root-level (legacy)

| File | Notes |
|------|-------|
| 🎮 `Pythons and Dragons1.0.py` | The original single-file prototype (internally `the_verdant_code.py`). Player "Grixle", Act 1 start. |
| `game_progress.json` | A sample/legacy save for the root prototype. |
| 📄 `Save updates 0_0_2.txt` | Legacy dev note on the save system — now captured in the [CHANGELOG (v0.0.2)](../CHANGELOG.md). Safe to remove once you're happy it's preserved there. |

## Era 1 — The Serpent's Code

### `v0.0.X/`
The original prototype line.

- 🎮 `serpents_and_dragons_v0_0_0.py` … `_v0_0_4.py` — the five iterations of *The
  Serpent's Code*.
- 📄 `v_0_0_0_Features.txt` — the original feature list (5 quests + core systems).
- `game_progress.json` — sample save.

## Era 2 — The Verdant Code (v1)

### `v1.1.0/` — Enhanced Edition
- 🎮 `the_verdant_code_1.1.0.py`
- 📄 `README_ENHANCED.md`, `IMPROVEMENTS_SUMMARY.md`, `TOPICS_VERIFIED.md`

### `v1.1.1/`
- 🎮 `the_verdant_code_1.1.1.py`
- 📄 `README_ENHANCED.md`, `IMPROVEMENTS_SUMMARY.md`, `TOPICS_VERIFIED.md`

### `v1.1.2/` — Cybersecurity & Zen
- 🎮 `the_verdant_code_1.1.2.py`
- 📄 `CYBERSECURITY_TOPICS_ADDED.md`, `ZEN_OF_PYTHON_ADDED.md`,
  `GAME_FIXES_SUMMARY.md`, `STORY_MODE_DEMO.md`

### `v1.1.3/`
- 🎮 `the_verdant_code_1.1.3.py`
- 📄 `STORYLINE_SUMMARY.md`, `TABLE_OF_CONTENTS.md`, `FINAL_SUMMARY.md`

### `v1.1.4/`
- 🎮 `the_verdant_code_1.1.3.py` *(note: file retains the 1.1.3 name)*
- 📄 `STORYLINE_SUMMARY.md`, `TABLE_OF_CONTENTS.md`, `FINAL_SUMMARY.md`

### `v1.1.5/` — "The Lost Language"
- 🎮 `the_verdant_code_1.1.5.py`
- 📄 `README.md`, `CHANGELOG.md`, `RELEASE_NOTES_v1.1.5.md`, `STORYLINE.md`,
  `INDEX.md`, `IMPLEMENTATION_SUMMARY.md`

### `v1.2.0/` — "From Zero to Enterprise"
The most documentation-heavy release (13 Markdown files).
- 🎮 `the_verdant_code_1.2.0_demo.py`, `portfolio_project_task_manager.py`
- 📄 `README.md`, `CHANGELOG_v1.2.0.md`, `EXECUTIVE_SUMMARY.md`, `ASSESSMENT.md`,
  `BEGINNER_ONBOARDING.md`, `ENTERPRISE_SKILLS_ROADMAP.md`, `PROPOSED_LESSONS.md`,
  `IMPLEMENTATION_NOTES.md`, `IMPLEMENTATION_ROADMAP.md`, `PROJECT_STATUS.md`,
  `DELIVERABLES_SUMMARY.md`, `QUICKSTART.md`, `START_HERE.md`

### `v1.2.1/`
- 🎮 `the_verdant_code_1.2.1.py`
- 📄 `README.md`, `RELEASE_NOTES.md`, `QUICKSTART.md`, `BEGINNER_ONBOARDING.md`,
  `ENTERPRISE_SKILLS_ROADMAP.md`

### `v1.2.2/` — ⚠️ heaviest cleanup target (~96 MB)
Acts 0–VIII complete; Act IX authored. This folder also accumulated a large
amount of **transient debugging scaffolding** that is not part of the game.
- 🎮 `the_verdant_code_1.2.2.py` (and `_COMPLETE.py`)
- 📄 `README.md`, `STORYLINE_PROGRESSION.md`, `LESSON_TEMPLATE_STANDARDS.md`
- 🧰 **~14 backup copies** (`*.bak`, `*.backup_*`, `*.before_fix`, `*.temp`, plus
  `_work`/`_fresh`/`_master` variants) and **~15 `fix_*.py` quote-repair scripts**
  (`fix_quotes.py`, `fix_all_v2.py`, `surgical_quote_fix.py`, …), test scripts,
  and Act IX lesson-generation scripts. **Candidates for deletion** — git
  preserves them. See the [cleanup strategy](version-history.md#recommended-strategy-in-priority-order).

### `V1.3.0/` — "The Complete Journey" *(note the capital `V`)*
All 181 lessons; shipped with the known quote bug + a fix utility.
- 🎮 `the_verdant_code_1.3.0.py` (and `_clean.py`, `_fixed.py`)
- 📄 `README.md`, `CHANGELOG.md`, `RELEASE_NOTES.md`, `MAINTENANCE_GUIDE.md`,
  `VERSION_1.3.0_COMPLETE.md`
- 🧰 `fix_quotes.py`, `diagnose.py`, `find_all_mismatches.py`, `test_game.py`, and
  several `create_*`/`*_quote_fix.py` build scripts.

## Era 3 — Master Edition (v2)

### `v2.0.0/` — Master Edition
- 🎮 `The Verdant Code 2.0.py`
- 📄 `README.md`, `RELEASE_NOTES_V2.0.0.md`, `VERSION_2.0.0_COMPLETE.md`

### `v2.1.0/` – `v2.1.3/`
Each contains the release's game file plus a `README.md`:
- 🎮 `The Verdant Code 2.1.0.py` … `2.1.3.py`
- 📄 `README.md` (badges note the tests passing / PEP compliance per release)

### `v2.1.4/`, `v2.1.5/`, `v2.1.6/`
Game file only (no per-folder README):
- 🎮 `The Verdant Code 2.1.4.py` / `2.1.5.py` / `2.1.6.py`

### `v2.2.0/` — Current release
- 🎮 `The Verdant Code 2.2.0.py`
- ⚠️ In-file version metadata is stale here (header says `2.1.3`, `VERSION`
  constant says `2.1.6`); see [open items](version-history.md#known-inconsistencies--open-items).

---

## Quick reference: which file do I run?

- **Just want to play?** → `v2.2.0/The Verdant Code 2.2.0.py`
- **Want the original prototype?** → `v0.0.X/serpents_and_dragons_v0_0_4.py`
- **Studying the evolution?** → walk the table in
  [version-history.md](version-history.md#at-a-glance) or the [CHANGELOG](../CHANGELOG.md).
