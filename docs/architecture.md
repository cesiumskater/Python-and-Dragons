# Architecture Overview

A high-level guide to how **The Verdant Code** is built. It is distilled from the
game's release notes and source headers and is meant to orient contributors —
read it before adding or modifying a lesson. (Exact class and method names have
been stable across the v2.x line; treat this as a conceptual map rather than a
line-level API reference.)

## The big picture

The entire game ships as a **single, self-contained Python file** with **no
external dependencies** (standard library only). That is a deliberate design
choice: a learner can download one `.py` file and run it with nothing but Python
installed.

```
┌──────────────────────────────────────────────────────────┐
│                      The Verdant Code                      │
│                                                            │
│   ┌────────────┐   selects   ┌──────────────────────────┐ │
│   │ Game engine │ ──────────► │  Lesson registry (Acts)  │ │
│   │  + menus    │             │  Act 0 … Act IX          │ │
│   └─────┬───────┘             └────────────┬─────────────┘ │
│         │                                  │ instantiates  │
│         │ reads/writes              ┌──────▼─────────────┐ │
│   ┌─────▼───────┐                   │  Lesson (base)     │ │
│   │ Save system │                   │   • teach()        │ │
│   │  (JSON)     │                   │   • challenge()    │ │
│   └─────────────┘                   └────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

## Core components

### Game engine & progress
A central engine drives the main menu, mode selection, and the lesson loop, and
owns a **progress** object (historically `GameProgress`) that tracks the player's
state: name, current Act/scene, completed (and skipped) lessons, XP, level,
character title, reputation, and story flags.

### The `Lesson` model
Every lesson is a class that inherits from a common **`Lesson`** base class and
implements two methods:

- **`teach()`** — presents the narrative + instructional content for the topic
  (explanations, runnable examples, key concepts, 3–5 common pitfalls, best
  practices, and real-world applications).
- **`challenge()`** — an interactive check (quiz / code challenge) that awards XP
  on success and gates progression.

This uniform shape is what makes the game extensible: a new topic is just a new
`Lesson` subclass.

### The registry & Acts
Lessons are organized into **10 Acts (0–IX)** and registered so the engine can
load them dynamically by Act. A factory/registry maps a topic ID to its `Lesson`
class; topics not yet authored historically fell back to a `GenericLesson` stub.
Adding a lesson means implementing the class **and** registering it — forgetting
the second step is exactly the bug that left Act IX inaccessible in v1.2.2.

| Act | Title | Focus |
|-----|-------|-------|
| 0 | The Awakening | Setup, terminal, first program, errors |
| I | The Ancient Glyphs | Variables, types, operators, I/O |
| II | The Tome of Collections | Lists, tuples, sets, dicts, strings |
| III | The Branching Paths | Conditionals and loops |
| IV | The Art of Incantations | Functions |
| V | The Ancient Scrolls | Files, exceptions, modules |
| VI | The Constructor's Forge | Object-oriented programming |
| VII | The Algorithmic Arena | Algorithms & Big-O |
| VIII | The Professional's Forge | Git, testing, packaging, CI/CD |
| IX | The Master's Path | Metaclasses, async, patterns, finale |

### Play modes
The game offers two modes:

- **Story Mode** — the full RPG experience with auto-save, XP, progression, and
  narrative. Lessons unlock as you complete prior Acts.
- **Reference Mode** — a save-free browser for quickly looking up any topic.

### Save system
Progress persists to a **JSON** file. The save format is versioned and was
designed to auto-upgrade older saves (introduced in v1.2.0's "Save System v2.0"),
building on the cross-platform, multi-slot, atomic-write, backup-capable design
that dates back to the v0.0.2 Serpent's Code work. A representative save record:

```json
{
  "player_name": "Grixle Mossroot",
  "current_act": 2,
  "completed_lessons": ["hello_world", "variables"],
  "xp": 150,
  "level": 3,
  "character_title": "Apprentice Coder",
  "reputation": 25,
  "story_flags": {}
}
```

> Save files are ignored by git (see `.gitignore`: `verdant_code_save.json`,
> `game_progress_*.json`) so player progress never gets committed.

## Adding a lesson (the pattern)

1. **Create a `Lesson` subclass** for the topic, implementing `teach()` and
   `challenge()`.
2. **Register it** with its topic ID in the appropriate Act so the engine can
   find it (don't leave it as a `GenericLesson`).
3. **Keep the narrative voice** — lessons are framed in the world of Fraylon
   (Elder Willowbyte mentoring, the Iron Wyrm as the looming threat).
4. **Include the full kit** — examples, key concepts, common pitfalls, best
   practices, and a working challenge.
5. **Verify it compiles and runs** before committing. Historically the most
   common breakage was quote-delimiter conflicts inside triple-quoted teaching
   text — prefer `"""` for the outer string when the content itself contains
   `'''` examples.

## Conventions

- **Python 3.8+**, standard library only.
- **PEP 8** style and **PEP 20** (Zen of Python) spirit — the game literally
  teaches these, so the codebase should model them.
- Per-lesson content typically runs 400–700 lines, which is why the single file
  is large (~123k lines in the Master Edition).
