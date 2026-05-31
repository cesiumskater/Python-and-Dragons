# Python and Dragons

> A fun, evolving Python text-based RPG that teaches programming through an epic
> fantasy adventure. Known in-universe as **The Verdant Code**.

![Latest](https://img.shields.io/badge/latest-v2.2.0-green.svg)
![Lessons](https://img.shields.io/badge/lessons-181-blue.svg)
![Acts](https://img.shields.io/badge/acts-10%20(0--IX)-purple.svg)
![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![Dependencies](https://img.shields.io/badge/dependencies-none%20(stdlib)-brightgreen.svg)

You are **Grixle Mossroot**, a scrappy goblin druid who must master the *Language
of Nature* (Python) to save the world of **Fraylon** from the Iron Wyrm and the
Cult of the Dragon. Guided by the treant **Elder Willowbyte**, you progress from
absolute beginner to *Mythic Hero* across 10 Acts and 181 lessons — every concept
tied to a story beat, every challenge a step toward saving the world.

The game is a single, self-contained Python file with **no external dependencies**.

---

## Quick Start

The current release lives in [`v2.2.0/`](v2.2.0/):

```bash
python "v2.2.0/The Verdant Code 2.2.0.py"
```

**Requirements:** Python 3.8+ (standard library only). Works on Windows, macOS,
and Linux. Your progress saves automatically to a local JSON file.

> Looking for an earlier release or the original *Serpent's Code* prototype? See
> the [version map](docs/versions.md).

---

## What You'll Learn

The curriculum spans 10 Acts, from "what is Python?" to async, design patterns,
and architecture:

| Path | Acts | Focus |
|------|------|-------|
| **Beginner** | 0–II | Setup, variables, types, collections |
| **Intermediate** | III–V | Control flow, functions, files & exceptions |
| **Advanced** | VI–VII | OOP, algorithms, Big-O thinking |
| **Professional** | VIII | Git, testing, debugging, packaging, CI/CD |
| **Master** | IX | Metaclasses, async, design patterns — and the final battle |

181 lessons · ~2,715 XP · estimated 80–120 hours of content.

---

## Repository Structure

```
Python-and-Dragons/
├── README.md                  # You are here
├── CHANGELOG.md               # Consolidated, version-by-version change history
├── docs/                      # Project documentation (see docs/README.md)
├── scripts/                   # Maintenance scripts (e.g. publishing release tags)
└── v2.2.0/                    # The current, runnable release
```

Only the **current** release lives in the tree. Every earlier release
(`v0.0.x` → `v2.1.6`) is preserved in git history and recoverable by tag or
commit — see the **[release map](docs/versions.md)**.

> **History preserved, sprawl removed.** The project used to keep a full folder
> per release (~140 MB of duplicated game files). Those folders now live only in
> git history; annotated tags mark each one (publish them with
> [`scripts/create-release-tags.sh`](scripts/create-release-tags.sh)). The full
> rationale is in
> **[docs/version-history.md](docs/version-history.md#documentation--cleanup-strategy)**.

---

## Version History

Python and Dragons has evolved through three distinct eras, growing from a
5-quest prototype into a 181-lesson learning epic. The game world (Fraylon),
hero (Grixle Mossroot), and mentor (Elder Willowbyte) have been remarkably
consistent throughout — it's the scope and polish that changed.

> Release dates below are **as documented** in each version's notes. The git
> history shows all versions were committed in January 2026; the in-file dates
> reflect the project's narrative timeline rather than commit dates. See the
> [detailed history](docs/version-history.md) for the full story and the
> [CHANGELOG](CHANGELOG.md) for granular changes.

### The Three Eras

**🐍 Era 1 — The Serpent's Code (`v0.0.x`)**
The origin. A single-file prototype titled *The Serpent's Code* with 5 playable
quests (variables, conditionals, input, lists, functions) on a framework built
for 19. Established the world of Fraylon and the save/load system.

**🌿 Era 2 — The Verdant Code (`v1.1.x` → `v1.3.0`)**
The game was renamed *The Verdant Code* and grew explosively. The `v1.1.x` line
added the dual Story/Reference modes, a rich D&D narrative, and topic-by-topic
lessons. `v1.2.x` reframed the project as a *career-preparation* system —
adding Act 0 (onboarding), Act VIII (professional tooling), Act IX (advanced
topics), a skill-assessment quiz, and a skip system. `v1.3.0` completed all 181
lessons and wired up Act IX's two-part final battle.

**⚔️ Era 3 — Master Edition (`v2.0.0` → `v2.2.0`)**
The production era. `v2.0.0` rebranded to *Master Edition* and declared the game
feature-complete. The `v2.1.x` line was pure stabilization — bug fixes, PEP 8/20
compliance, thousands of automated tests, and menu/Reference-mode polish.
`v2.2.0` is the current release, focused on code cleanup.

### At a Glance

| Version | Documented Date | Title / Theme | Highlights |
|---------|-----------------|---------------|------------|
| **v0.0.0–0.0.4** | 2025 | *The Serpent's Code* | First prototype; 5 quests; world of Fraylon; save system |
| **v1.1.0** | "2024-10-01" | The Verdant Code (Enhanced) | Story + Reference modes; TOC navigation; XP/progression |
| **v1.1.2** | 2025 | Cybersecurity & Zen | Security topics, Zen of Python, story-mode demo |
| **v1.1.3–1.1.4** | 2025 | Storyline & TOC | Expanded narrative, table of contents, bug fixes |
| **v1.1.5** | 2025-12-22 | *The Lost Language* | Unicode/encoding lesson, list mini-game; 153 topics |
| **v1.2.0** | 2025-12-22 | *Zero to Enterprise* | Act 0, Act VIII, Act IX; skill assessment; skip system; portfolio projects |
| **v1.2.1** | 2025 | Onboarding polish | Quickstart & onboarding refinements |
| **v1.2.2** | 2025-12-25 | Act IX content | Acts 0–VIII complete (161 lessons); Act IX authored |
| **V1.3.0** | 2026-01-01 | *The Complete Journey* | All 181 lessons; Act IX registered; 7 duplicate classes removed |
| **v2.0.0** | 2026-01-04 | *Master Edition* | Rebrand; production-ready; quote/syntax fixes; verified |
| **v2.1.0** | 2026-01-06 | Bug fixes | PEP 8 improvements, bug fixes |
| **v2.1.1** | 2026-01-06 | Tested | 3,439 automated tests passing |
| **v2.1.2** | 2026-01-06 | PEP compliant | PEP 8 & PEP 20 compliance verified |
| **v2.1.3** | 2026-01-06 | Tested | 5,611 automated tests passing |
| **v2.1.4** | 2026-01-07 | Navigation | Menu navigation fixes |
| **v2.1.5** | 2026-01-07 | Reference mode | Improved Reference Mode lesson flow |
| **v2.1.6** | 2026-01-07 | Tested | Comprehensive testing verification |
| **v2.2.0** | 2026-01-23 | **Current** | Code cleanup |

For the complete, granular list of changes per release, see **[CHANGELOG.md](CHANGELOG.md)**.

---

## Documentation

| Document | Purpose |
|----------|---------|
| [CHANGELOG.md](CHANGELOG.md) | Every notable change, version by version |
| [docs/version-history.md](docs/version-history.md) | The full evolution narrative + cleanup strategy |
| [docs/architecture.md](docs/architecture.md) | How the game is built (engine, lessons, saves, modes) |
| [docs/versions.md](docs/versions.md) | A map of every version folder and its key files |

---

## Contributing

This is an educational project by **Danny (Cesium) P.** Suggestions and bug
reports are welcome via GitHub Issues. When proposing changes, please target the
**current** version and follow the lesson template described in
[docs/architecture.md](docs/architecture.md).

## License

The game has historically been described as an open-source educational project.
A formal `LICENSE` file has not yet been added to the repository — see the
[open items](docs/version-history.md#known-inconsistencies--open-items) for
details.

---

*"In the beginning was the Code, and the Code was with Python, and the Code was
Python."* — Elder Willowbyte, First Treant of Mossroot Grove 🌳
