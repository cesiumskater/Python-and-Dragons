# Changelog

All notable changes to **Python and Dragons** (*The Verdant Code*) are recorded
here. The format is based on [Keep a Changelog](https://keepachangelog.com/),
and the project aims to follow [Semantic Versioning](https://semver.org/).

> **About the dates:** dates are taken from each version's own release notes and
> reflect the project's narrative timeline. The git history shows every release
> was committed in January 2026. Where a version's documentation disagreed with
> itself, the conflict is noted. This file consolidates the per-version
> changelogs that previously lived in scattered `vX.Y.Z/` folders.

---

## [Unreleased] — Repository maintenance

Documentation and repository housekeeping; no gameplay changes.

### Added
- Root `README.md` (with a Version History section), consolidated `CHANGELOG.md`,
  and a `docs/` folder (index, version history, architecture, release map).
- `scripts/create-release-tags.sh` to publish a git tag (and optional draft
  GitHub Release) for every documented version.
- Annotated git tags for all releases `v0.0.4` … `v2.2.0` (created locally;
  **push pending** — the sandbox proxy blocks tag pushes; run the script above).

### Changed
- **Removed version sprawl:** the 18 historical version folders (`v0.0.X` …
  `v2.1.6`) were deleted from the working tree, shrinking it from ~149 MB to
  ~9 MB. Every release remains recoverable from git history by tag or commit SHA
  (see [docs/versions.md](docs/versions.md)). Only the current release (`v2.2.0/`)
  stays in the tree.

### Fixed
- Reconciled the current release file's version metadata to `2.2.0` (header
  docstring, `VERSION` constant, and `RELEASE_DATE`); it previously reported
  `2.1.3` / `2.1.6`.
- Captured the legacy `Save updates 0_0_2.txt` note as the `[0.0.2]` entry below,
  then removed the redundant file.

## [2.2.0] — 2026-01-23 (Current)

### Changed
- Code cleanup pass on the Master Edition codebase.

> The version-metadata inconsistency originally noted here (header `2.1.3` /
> `VERSION` `2.1.6` vs. release `2.2.0`) was resolved in the Unreleased
> maintenance section above.

## [2.1.6] — 2026-01-07

### Changed
- Comprehensive testing verification across all 181 lessons.

## [2.1.5] — 2026-01-07

### Changed
- Improved Reference Mode lesson flow.

## [2.1.4] — 2026-01-07

### Fixed
- Menu navigation fixes.

## [2.1.3] — 2026-01-06

### Changed
- Comprehensive testing verification — 5,611 automated tests passing.

## [2.1.2] — 2026-01-06

### Changed
- PEP 8 and PEP 20 compliance verified.

## [2.1.1] — 2026-01-06

### Changed
- Comprehensive testing verification — 3,439 automated tests passing.

## [2.1.0] — 2026-01-06

### Fixed
- General bug fixes.

### Changed
- PEP 8 style improvements.

### Added
- `.gitignore` for Python cache and save files.

## [2.0.0] — 2026-01-04 — "Master Edition"

### Changed
- **Rebranded** to *The Verdant Code 2.0 — Master Edition*; declared
  production-ready. (Note: this is a MAJOR bump for a primarily metadata +
  quality release; no breaking API changes were introduced.)
- Version metadata updated to 2.0.0 throughout.

### Fixed
- Carried in the fixes that made v1.3.0 actually compile and run:
  - Resolved 1,391 quote-delimiter conflicts.
  - Resolved 119+ nested triple-quote issues.
  - Corrected remaining syntax errors; verified compilation.

### Verified
- All 181 lessons tested; zero runtime errors; PEP 8 / PEP 20 compliance
  confirmed; save/load, menu navigation, and story init tested.

### Notes
- Save files are fully backward/forward compatible with v1.3.0.

## [1.3.0] — 2026-01-01 — "The Complete Journey"

### Added
- **Complete Act IX — The Master's Path**: 20 advanced lessons (metaclasses,
  descriptors, AST, protocols, async, advanced generators/context managers, the
  four design-pattern families, memory management, performance, security,
  architecture, concurrency, distributed systems) culminating in the two-part
  **Final Battle**.
- Act IX lesson registration in the game registry; complete storyline resolution
  and epilogue.

### Changed
- Total lesson count: **181** (was 80 wired up in v1.2.2).
- Total XP available: **2,715** (was ~1,000).
- Header/documentation updated to reflect all Acts 0–IX.

### Fixed
- Removed **7 duplicate lesson classes** (~4,081 lines) that were bloating the
  file (DesignPatterns Structural/Behavioral/Functional, MemoryManagement,
  PerformanceOptimization, SecurityBestPractices, ArchitecturePatterns).
- File size reduced from 127,425 → 123,344 lines.

### Known Issues (at release)
- Quote-delimiter conflicts in some `teach()` methods prevented compilation; a
  bundled `fix_quotes.py` utility was provided. These were fully resolved in
  v2.0.0.

## [1.2.2] — 2025-12-25

### Added
- Act IX lessons authored (lessons 3–20 across multiple modules).
- Lesson template standards and storyline-progression documentation.

### Status
- Acts 0–VIII complete (**161 lessons**); Act IX defined but **not yet
  registered** (inaccessible to players until v1.3.0).
- 127,425 lines total.

### Known Issues (at release)
- Duplicate class definitions causing file bloat.
- Version info still reporting only 80 lessons complete.

## [1.2.1] — 2025

### Changed
- Onboarding and quickstart refinements; release-notes documentation.

## [1.2.0] — 2025-12-22 — "From Zero to Enterprise"

### Added
- **Act 0 — The Awakening** (6 lessons): what Python is, installing Python,
  terminal basics, editors/IDEs, Hello World, understanding errors.
- **Act VIII — The Forge of Mastery** (enterprise skills): Git & GitHub, virtual
  environments, packaging, project structure, unit testing, `pdb`, PEP 8 /
  linting, logging, configuration, CI/CD.
- **Act IX — The Master's Path** (initial advanced topics): metaclasses &
  descriptors, design patterns, decorators & context managers, generators &
  iterators, async/await, Flask & Django intros, performance optimization.
- **Skill Assessment System**: a 10-question quiz that recommends a starting Act.
- **Skip System**: per-lesson skip plus a 3-question test-out quiz; skipped
  lessons tracked separately.
- Portfolio projects (CLI task manager, CSV data analyzer, web scraper).
- Pre-flight environment check; "Common Pitfalls" section for every lesson.
- New docs: onboarding, enterprise roadmap, proposed lessons, assessment,
  executive summary, implementation notes, quickstart.

### Changed
- **Save System v2.0**: versioned save format with auto-upgrade of older saves;
  corruption protection. Backward compatible with v1.1.5 saves.
- Act I reordered for "quick wins first" (Hello World → I/O → Errors → Zen).
- Type hints and docstrings added throughout the core systems.

## [1.1.5] — 2025-12-22 — "The Lost Language"

### Added
- **RepresentingTextLesson** — Unicode/UTF-8, `ord()`/`chr()`, encode/decode.
- **ListGamesLesson** — an interactive "Corrupted Catacombs" dungeon-crawler
  mini-game built from list operations.
- "Lost Language of Nature" narrative framework tying every concept to the
  world-saving mission; richer Act introductions.

### Changed
- Topic registry grew to **153** topics; both new lessons wired into the
  LessonFactory (no longer GenericLesson stubs).

### Notes
- Existing save files remain compatible.

## [1.1.3 – 1.1.4] — 2025

### Added
- Comprehensive topic coverage; dual Story/Reference modes; cybersecurity topics;
  auto-save.
- Expanded storyline summaries and an enhanced table of contents.

### Fixed
- Navigation improvements and assorted bug fixes.

## [1.1.2] — 2025

### Added
- Cybersecurity topics and the Zen of Python lesson.
- Story-mode demo and game-fixes documentation.

## [1.1.0] — "2024-10-01" — The Verdant Code (Enhanced Edition)

### Added
- **Renamed** from *The Serpent's Code* to *The Verdant Code*.
- Story Mode with save/load; Reference Mode for quick lookup.
- Table-of-contents navigation; XP and progression system.
- Cybersecurity topic integration.

---

## The Serpent's Code era (`v0.0.x`)

The original prototype, titled **The Serpent's Code**, created by "Danny &
Claude." It established the world of Fraylon and the core game engine.

## [0.0.2] — 2025 — Robust Save System

> Recovered from the legacy dev note `Save updates 0_0_2.txt` and turned into a
> proper changelog entry.

### Added
- **Cross-platform save locations** with sensible per-OS defaults and a
  current-directory fallback when the home folder isn't writable:
  - Windows: `%APPDATA%/SerpentsCode/saves/`
  - macOS: `~/Library/Application Support/SerpentsCode/saves/`
  - Linux: `~/.local/share/SerpentsCode/saves/`
- **Multiple save slots** — 3 manual slots (each showing player name, level, XP,
  and last-saved time) plus a separate autosave slot.
- **Backup & recovery** — automatic backup before overwriting a save, with
  recovery from corrupted saves.
- **Atomic writes** — saves are written to a temp file first, then moved into
  place, to avoid half-written/corrupted save files.
- **Import / export** — portable save files for sharing or moving between
  machines.
- **Quick-save** support during gameplay.

### Changed
- Replaced the basic save routine with the robust save system described above;
  added clearer error messages and a permission check before saving.

## [0.0.0 – 0.0.1] — 2025 — Initial Prototype

> Summarized from `v0.0.X/v_0_0_0_Features.txt`.

### Added
- First single-file release of *The Serpent's Code*.
- **5 playable quests** (of 19 planned): The Mossy Burrow (variables & print),
  The Corrupted Creek (conditionals), The Talking Toad (input & string methods),
  The Arcane Archive (lists & indexing), The Ritual of Balance (functions &
  returns).
- Core systems: game engine + menu, code validator with safe execution,
  JSON save/load, XP and leveling, achievement tracking, narrative integration.

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/): MAJOR for
incompatible changes, MINOR for backward-compatible features, PATCH for
backward-compatible fixes.

> **Historical note:** version numbers in this project have not always tracked
> SemVer strictly (e.g., v2.0.0 was largely a rebrand + quality release rather
> than a breaking change). Entries above describe what actually changed.
