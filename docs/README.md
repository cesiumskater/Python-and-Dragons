# Documentation

Welcome to the documentation for **Python and Dragons** (*The Verdant Code*).
This folder is the single, canonical home for project documentation. The many
`.md` files inside individual `vX.Y.Z/` folders are **historical snapshots** kept
with their releases; the documents here are the living, maintained references.

## Contents

| Document | What it covers |
|----------|----------------|
| [version-history.md](version-history.md) | The full evolution narrative across all three eras, the recommended strategy for taming version sprawl, the future roadmap, and a list of known inconsistencies / open items. |
| [architecture.md](architecture.md) | How the game is built: the core engine, the `Lesson` model, the Act/registry system, the two play modes, and the save system. Read this before adding a lesson. |
| [versions.md](versions.md) | A guided map of every version folder in the repository and the notable files inside each one. |

See also, at the repository root:

- **[../README.md](../README.md)** — project overview, quick start, and a summary
  Version History.
- **[../CHANGELOG.md](../CHANGELOG.md)** — the consolidated, version-by-version
  change history.

## How this documentation is organized

```
.
├── README.md          # Front door: overview + quick start + version summary
├── CHANGELOG.md       # Granular, per-version change log
└── docs/
    ├── README.md      # This index
    ├── version-history.md
    ├── architecture.md
    └── versions.md
```

The principle: **one canonical place per kind of information.** Quick orientation
lives in the root README; granular change records live in the CHANGELOG; deeper
reference and history live here in `docs/`.
