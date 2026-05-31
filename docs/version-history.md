# Version History & Evolution

This document tells the long-form story of how **Python and Dragons** grew, and
recommends a strategy for keeping that history intact while taming the "version
sprawl" the project has accumulated. For the granular, machine-readable list of
changes, see the [CHANGELOG](../CHANGELOG.md). For a per-folder map, see
[versions.md](versions.md).

---

## The evolution at a glance

The project has lived through **three eras**, each marked by a rename and a leap
in scope. Remarkably, the *world* never changed: from the very first prototype,
the story is set in **Fraylon**, you play **Grixle Mossroot** (a goblin druid),
and you learn from **Elder Willowbyte** while the **Iron Wyrm / Cult of the
Dragon** threaten the land. What changed was ambition — from a 5-quest teaching
toy to a 181-lesson "zero to professional" curriculum.

```
Era 1: The Serpent's Code      Era 2: The Verdant Code         Era 3: Master Edition
   v0.0.0 ─ v0.0.4      ──►      v1.1.0 ─ v1.3.0        ──►       v2.0.0 ─ v2.2.0
   5 quests, 1 file             dual modes, Acts 0–IX,           rebrand, tested,
   save system                  181 lessons, careers            cleaned up
```

### Era 1 — The Serpent's Code (`v0.0.x`)

The origin. A single Python file titled *The Serpent's Code* (🐍), credited to
"Danny & Claude," already set in the world of Fraylon. It shipped **5 playable
quests** on a framework designed for 19, plus the foundational systems: a game
engine and menu, a code validator with safe execution, XP/leveling, achievement
tracking, and JSON save/load.

The standout work of this era was the **save system** (originally captured in the
loose note `Save updates 0_0_2.txt`, now folded into the
[CHANGELOG as v0.0.2](../CHANGELOG.md)): cross-platform save locations, three
manual slots plus autosave, atomic writes, automatic backups, and import/export.

### Era 2 — The Verdant Code (`v1.1.0` → `v1.3.0`)

The project was renamed **The Verdant Code** (🌿) and credited to *Danny (Cesium)
P.* This era is where it grew up:

- **`v1.1.x`** introduced the dual **Story / Reference** modes, table-of-contents
  navigation, a much richer D&D narrative ("The Lost Language of Nature"), and a
  steadily growing topic registry — reaching 153 topics by `v1.1.5`, which added a
  Unicode lesson and a list-powered dungeon-crawler mini-game.
- **`v1.2.0`** was the "From Zero to Enterprise" leap: it reframed the game as a
  *career-preparation* tool by adding **Act 0** (true-beginner onboarding),
  **Act VIII** (professional tooling — Git, testing, packaging, CI/CD), and the
  first cut of **Act IX** (advanced topics). It also added a skill-assessment
  quiz, a skip/test-out system, portfolio projects, and a versioned save format.
- **`v1.2.2`** had Acts 0–VIII complete (161 lessons) with Act IX authored but not
  yet wired in.
- **`V1.3.0`** completed the journey: all **181 lessons** registered across Acts
  0–IX, the two-part final battle, and the removal of 7 duplicate classes — though
  it shipped with a known quote-delimiter bug that needed a fix utility to compile.

### Era 3 — Master Edition (`v2.0.0` → `v2.2.0`)

The production era. **`v2.0.0`** rebranded to *Master Edition*, fixed the
outstanding syntax/quote issues (1,391 quote conflicts, 119+ nested triple-quote
issues) so the game finally compiled cleanly, and declared the project
production-ready. The **`v2.1.x`** line was disciplined stabilization — bug fixes,
PEP 8/20 compliance, thousands of automated tests (3,439 by v2.1.1; 5,611 by
v2.1.3), and menu/Reference-mode polish. **`v2.2.0`** is the current release, a
code-cleanup pass.

---

## Documentation & cleanup strategy

The project's history is valuable and worth preserving — but right now it is
preserved by **keeping 20 full copies of the game in the working tree**, which has
grown the checkout to ~149 MB. This section recommends how to keep every bit of
that history while making the repository clean and navigable.

> **Guiding principle:** *git already remembers everything.* History should be
> preserved by git (commits, tags, releases), not by parallel folders in the
> working tree. The folders are a manual, lossy substitute for tooling git
> provides for free.

### The problems, concretely

1. **Working-tree bloat (~149 MB).** Twenty `vX.Y.Z/` folders each carry a full
   copy of the (multi-MB) game file.
2. **`v1.2.2/` is ~96 MB of transient artifacts.** It contains **14 multi-MB
   backup copies** of the main file (`.bak`, `.backup_final`, `.backup_surgical`,
   `.backup_before_dedup`, …) and **15 one-off `fix_*.py` quote-repair scripts**
   (`fix_quotes.py`, `fix_all_v2.py`, `surgical_quote_fix.py`, …), plus `_work`,
   `_fresh`, `_master`, and `.temp` variants. None of this is the game; it is
   debugging scaffolding that git already preserves.
3. **Documentation sprawl (~50 Markdown files).** Each version folder has its own
   `README`, and many add `FINAL_SUMMARY.md`, `EXECUTIVE_SUMMARY.md`,
   `IMPROVEMENTS_SUMMARY.md`, `TABLE_OF_CONTENTS.md`, etc. There was no single
   entry point until this cleanup added the root `README.md`, `CHANGELOG.md`, and
   this `docs/` folder.
4. **No tags or releases.** Despite extensive `RELEASE_NOTES_*.md` files, the repo
   has **no git tags and no GitHub Releases** — so the only record of "what was
   v2.1.3" is a folder name.

### Recommended strategy (in priority order)

The first two steps are pure documentation and have already been done by this
pass. The rest are recommendations that touch source/game files and so are left
for the maintainer to action deliberately.

**1. Establish a single source of truth (✅ done in this pass).**
Root `README.md` + `CHANGELOG.md` + this `docs/` folder now provide one canonical
place for orientation, change history, and reference. Per-version docs stay where
they are as historical snapshots.

**2. Make history navigable without opening folders (✅ done in this pass).**
[versions.md](versions.md) maps every folder and its notable files so the sprawl
is at least browsable.

**3. Tag every release and create GitHub Releases (recommended).**
For each released version, create an annotated git tag (e.g. `v2.2.0`) on the
commit that introduced it, and a GitHub Release using the already-written release
notes. This is the *real* mechanism for "preserving version history" — it makes
every version downloadable and diffable without keeping it in the working tree.

```bash
# Example, once per version, on the appropriate commit:
git tag -a v2.2.0 -m "The Verdant Code 2.2.0"
git push origin --tags
```

**4. Archive the historical version folders (recommended).**
Once tags/releases exist, the working tree only needs the **current** release.
Two safe options, in increasing tidiness:
   - **Minimum risk:** move all but the latest into a single `archive/` (or
     `releases/`) directory so the repo root shows only the current game.
   - **Cleanest:** remove the historical folders from the working tree entirely;
     they remain fully recoverable from their tags (`git checkout v1.3.0`).
   Either way, the canonical, runnable game lives at the root or in a single
   `latest/`-style location.

**5. Purge transient artifacts from `v1.2.2/` (recommended, high impact).**
The 14 backups and 15 `fix_*.py` scripts can be deleted outright — they are
debugging scaffolding, not releases, and git retains them. This alone reclaims
~90 MB. (Optionally, use `git filter-repo` to drop them from history if the
`.git` size ever becomes a concern; the current `.git` is only ~4.8 MB, so this
is not urgent.)

**6. Normalize naming and metadata (recommended).**
Rename `V1.3.0/` → `v1.3.0/` for consistency, and reconcile the in-file version
metadata (see open items below).

**7. Add a `.gitattributes`/Git LFS policy if large game files persist.**
If the multi-MB single-file game continues to grow, consider tracking it with
Git LFS so clones stay lean.

### Target end-state

```
Python-and-Dragons/
├── README.md            # front door (current version)
├── CHANGELOG.md         # all history, consolidated
├── docs/                # living documentation
├── the_verdant_code.py  # the current, runnable game (single file)
└── archive/             # optional: prior releases, or rely on git tags instead
```

Everything that exists today still exists — in tags, releases, and git history —
but a newcomer sees a clean, obvious project instead of twenty folders.

---

## Roadmap

Consolidated from the "future plans" scattered across historical release notes.
These are aspirations recorded by the project, not commitments:

- **GUI / web-based version** of the game.
- **Progress analytics** and visualization dashboards.
- **Community features** — custom/shared lessons, multiplayer coding challenges.
- **Mobile version** and cloud save synchronization.
- **Interview prep** — mock technical interviews, integration with job boards.

Near-term, the most valuable work is non-feature: execute the cleanup strategy
above and reconcile the metadata inconsistencies below.

---

## Known inconsistencies & open items

These are documentation/metadata issues surfaced during cleanup. They do **not**
affect gameplay, but resolving them would tighten the project considerably.

- **In-file version metadata disagrees with itself** in the current release: the
  `v2.2.0` file's header docstring says `2.1.3`, its `VERSION` constant says
  `2.1.6`, and the folder/release is `2.2.0`. These should all read `2.2.0`.
- **Conflicting release dates** in historical docs — e.g. `v1.1.5` is dated both
  `2024-11-15` (in the v1.2.0 changelog) and `2025-12-22` (in its own changelog);
  `v1.2.0` is also dated `2025-12-22`. The git history shows all commits landed in
  January 2026. The root README and CHANGELOG flag dates as "documented" rather
  than authoritative.
- **No `LICENSE` file.** The project is described as "open source / educational,"
  and one changelog references "MIT License — see LICENSE file," but no such file
  exists. Adding an explicit license would resolve the ambiguity.
- **Inconsistent folder casing:** `V1.3.0/` (capital `V`) versus the lowercase
  `vX.Y.Z` used everywhere else.
- **Project naming drift:** the repository is *Python and Dragons*, the root
  prototype file is *Pythons and Dragons1.0.py* (internally `the_verdant_code.py`),
  while the game itself is *The Serpent's Code* (v0) and then *The Verdant Code*
  (v1+). The root README treats "Python and Dragons" as the repo/project name and
  "The Verdant Code" as the game's in-universe title.

> These items are intentionally **not** auto-fixed here, because they touch source
> and game files. They are recorded so the maintainer can address them
> deliberately.
