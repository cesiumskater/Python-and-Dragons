# 🐉 Python and Dragons

> Learn Python by saving a world. A single-file, dependency-free text RPG that
> teaches real programming through an epic fantasy adventure — known in-universe
> as **The Verdant Code**.

![Latest](https://img.shields.io/badge/latest-v2.2.0-green.svg)
![Lessons](https://img.shields.io/badge/lessons-181-blue.svg)
![Acts](https://img.shields.io/badge/acts-10%20(0--IX)-purple.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none%20(stdlib)-brightgreen.svg)

> **This README is the single source of truth for the project.** Deeper material
> lives in [`docs/`](docs/) and the full change history in [`CHANGELOG.md`](CHANGELOG.md),
> but start here.

---

## Overview

**Python and Dragons** is a story-driven Python learning game. You play
**Grixle Mossroot**, a scrappy goblin druid who must master the *Language of
Nature* (Python) to save the world of **Fraylon** from the Iron Wyrm and the
Cult of the Dragon. Guided by the treant **Elder Willowbyte**, you progress from
absolute beginner to *Mythic Hero* across **10 Acts** and **181 lessons** —
every concept tied to a story beat, every challenge a step toward saving the
world.

It is **one self-contained Python file** with **no external dependencies** — a
learner can download it and run it with nothing but Python installed.

- 🎓 **A real curriculum** — from "what is Python?" to async, design patterns,
  metaclasses, and professional tooling.
- ⚔️ **Wrapped in an RPG** — XP, levels, hero ranks, reputation, achievements,
  and a complete narrative arc.
- ✅ **Graded for real** — every lesson ends in a scored quiz you must actually
  pass (see [Features](#features)).

---

## Features

| Feature | Description |
|---|---|
| 🗺️ **181 lessons across 10 Acts** | A full path from setup (Act 0) to mastery (Act IX), each with story, teaching, and a challenge. |
| ✅ **Graded challenges** | Every lesson ends in a 3-question quiz; you must answer a majority correctly to earn XP and advance. |
| 📖 **Two play modes** | **Story Mode** (full quest, saves progress) and **Reference Mode** (browse any topic freely, no saves). |
| 🧭 **Skill assessment** | A first-run wizard recommends your starting Act so beginners and experienced devs both start in the right place. |
| 📈 **RPG progression** | Earn XP (~2,000 total), climb skill levels (Novice → Legendary) and hero ranks (Unknown Wanderer → Mythic Hero of Fraylon), and build reputation. |
| 💾 **Robust saves** | Auto-save after each lesson plus manual save; corrupt saves recover gracefully. |
| ⚙️ **Settings** | Toggle hints, auto-save, and lesson-skipping, persisted to your save. |
| 🧩 **Zero dependencies** | Pure Python standard library; runs on Windows, macOS, and Linux. |

---

## The Story

> *"Young Grixle Mossroot, welcome to Mossroot Grove. The world of Fraylon is in
> grave danger. You must learn the Language of Nature — what mortals call
> 'Python' — to stop the Cult of the Dragon."* — Elder Willowbyte

Your journey takes you from the **Mossroot Grove** through the port city of
**Mallport**, the **Library of Thorns**, the **Iron Sanctum**, the **Forge of
Mastery**, and finally the **Master's Path** — where the Iron Wyrm awaits. Each
location maps to a set of Python skills, and the finale is a two-part boss battle
you can only win by writing real code in your head.

---

## How to Play / Quick Start

The current release lives in [`v2.2.0/`](v2.2.0/). From the repository root:

```bash
python "v2.2.0/The Verdant Code 2.2.0.py"
```

On first run, a setup wizard runs a short **skill assessment** and lets you name
your hero. Then you reach the **main menu**:

```
  1. Story Mode (Full quest with saves)
  2. Reference Mode (Browse topics, no saves)
  3. Retake Skill Assessment
  4. View Hero Status
  5. Settings
  6. Credits
  7. Exit Game
```

**A lesson plays out as:** read the narrative intro → study the teaching content
(examples, key concepts, common pitfalls, best practices) → answer the
**challenge** quiz → earn XP and advance. Pass the challenge and your progress
auto-saves; miss it and you can review and try again.

---

## Installation

**Requirements:** Python **3.8+** (3.11+ recommended). No third-party packages —
the game uses only the standard library.

```bash
# 1. Get the code
git clone https://github.com/cesiumskater/Python-and-Dragons.git
cd Python-and-Dragons

# 2. (Optional) confirm your Python version
python --version        # should be 3.8 or newer

# 3. Play
python "v2.2.0/The Verdant Code 2.2.0.py"
```

A built-in **Pre-Flight Check** verifies your Python version, OS, terminal, file
permissions, and (optionally) Git before the game starts.

---

## Gameplay & Learning Path

The curriculum spans 10 Acts. The skill assessment will drop you at a sensible
starting point, but you can jump to any Act from Story Mode.

| Path | Acts | Focus | Lessons |
|------|------|-------|---------|
| **Beginner** | 0 – II | Setup, variables, types, collections | 46 |
| **Intermediate** | III – V | Control flow, functions, files & exceptions | 53 |
| **Advanced** | VI – VII | OOP, algorithms, Big-O thinking | 32 |
| **Professional** | VIII | Git, testing, packaging, debugging, CI/CD | 30 |
| **Master** | IX | Metaclasses, async, design patterns — and the final battle | 20 |

**Progression systems:**

- **XP** — ~10 XP per lesson (with a bonus finale), ~2,000 XP total.
- **Skill level** (by XP): Novice → Apprentice → Adept → Expert → Master → Legendary.
- **Hero rank** (by reputation): Unknown Wanderer → … → **Mythic Hero of Fraylon**.

---

## Saving & Progress

Story Mode keeps your progress in a JSON save file:

- **File:** `verdant_code_save.json`, written to your current working directory.
- **When:** automatically after each completed lesson (if auto-save is on), and
  on demand via *Save game manually*.
- **What's stored:** hero name, current Act, completed/skipped lessons, XP,
  reputation, skill level, hero rank, achievements, time played, preferences, and
  the game version.
- **Resilience:** a missing or corrupted save is detected and reset to a fresh
  start rather than crashing.
- **Reference Mode never saves** — it's a safe sandbox for browsing topics.

> Save files are intentionally **git-ignored** (see [`.gitignore`](.gitignore)),
> so your personal progress is never committed.

---

## Version History

Python and Dragons evolved through three eras, growing from a 5-quest prototype
into a 181-lesson learning epic. The world (Fraylon), hero (Grixle), and mentor
(Elder Willowbyte) stayed consistent throughout — scope and polish are what
changed.

- **🐍 Era 1 — The Serpent's Code (`v0.0.x`):** the origin. A single-file
  prototype with 5 quests and the foundational save system.
- **🌿 Era 2 — The Verdant Code (`v1.1.x` → `v1.3.0`):** renamed and expanded
  into dual Story/Reference modes, a rich narrative, a career-prep curriculum
  (Acts 0, VIII, IX), and finally all 181 lessons.
- **⚔️ Era 3 — Master Edition (`v2.0.0` → `v2.2.0`):** the production era —
  rebrand, thousands of tests, PEP 8/20 compliance, and code cleanup.

| Version | Era | Highlights |
|---------|-----|------------|
| `v0.0.4` | Serpent's Code | 5-quest prototype; world of Fraylon; save system |
| `v1.1.5` | Verdant Code | Dual modes, Unicode lesson, list mini-game; 153 topics |
| `v1.2.0` | Verdant Code | "Zero to Enterprise": Acts 0, VIII, IX; skill assessment |
| `v1.3.0` | Verdant Code | All 181 lessons registered; Act IX finale |
| `v2.0.0` | Master Edition | Rebrand; syntax fixes; production-ready |
| `v2.1.x` | Master Edition | Bug fixes, PEP 8/20, thousands of tests |
| **`v2.2.0`** | **Master Edition** | **Current** — code cleanup + QA hardening |

Earlier releases are no longer kept as folders in the tree (that caused ~140 MB
of duplication); each is preserved in git history and recoverable by tag or
commit. See the **[release map](docs/versions.md)** and the full
**[CHANGELOG](CHANGELOG.md)**.

---

## Repository Layout

```
Python-and-Dragons/
├── README.md                  # You are here — the single source of truth
├── CHANGELOG.md               # Consolidated, version-by-version history
├── docs/                      # Deeper documentation (see docs/README.md)
│   ├── architecture.md        #   how the game is built
│   ├── version-history.md     #   full evolution + cleanup strategy
│   └── versions.md            #   release → tag → commit recovery map
├── scripts/
│   └── create-release-tags.sh # publish per-release git tags / Releases
└── v2.2.0/
    └── The Verdant Code 2.2.0.py   # the current, runnable game (single file)
```

Only the **current** release ships in the tree. Every earlier version lives in
git history — see [`docs/versions.md`](docs/versions.md) to retrieve any of them.

---

## Documentation

| Document | Purpose |
|----------|---------|
| [CHANGELOG.md](CHANGELOG.md) | Every notable change, version by version |
| [docs/architecture.md](docs/architecture.md) | How the game is built (engine, lessons, Acts, modes, saves) |
| [docs/version-history.md](docs/version-history.md) | The full evolution narrative + repo cleanup strategy |
| [docs/versions.md](docs/versions.md) | A map for recovering any historical version |

---

## Contributing

This is an educational project by **Danny (Cesium) P.** Issues and suggestions
are welcome via GitHub.

To add or change a lesson, follow the `Lesson` pattern described in
[docs/architecture.md](docs/architecture.md): subclass `Lesson`, implement
`teach()` and a graded `challenge()`, register it in the Act registry, and keep
the Fraylon narrative voice. Please confirm the file still compiles
(`python -m py_compile`) and that your challenge can both pass (correct answers)
and fail (wrong answers) before submitting.

---

## License

Python and Dragons has historically been described as an open-source educational
project. A formal `LICENSE` file has **not** yet been added to the repository;
until one is, please treat the code as "all rights reserved by the author" for
redistribution purposes and reach out before reusing it commercially. Adding an
explicit license is tracked as an open item in
[docs/version-history.md](docs/version-history.md#known-inconsistencies--open-items).

---

**Created by Danny (Cesium) P.**

*"In the beginning was the Code, and the Code was with Python, and the Code was
Python."* — Elder Willowbyte, First Treant of Mossroot Grove 🌳
