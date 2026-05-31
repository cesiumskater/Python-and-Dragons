#!/usr/bin/env bash
#
# create-release-tags.sh
# -----------------------
# Recreates and pushes one annotated git tag per documented release of
# Python and Dragons (The Verdant Code), and optionally creates a matching
# DRAFT GitHub Release for each.
#
# Why this script exists:
#   The historical version folders (v0.0.X … v2.1.6) were removed from the
#   working tree to tame ~140 MB of version sprawl. Every version is still
#   fully preserved in git history (see the commit map below). These tags make
#   each release easy to find and check out again, e.g.:
#       git checkout v1.3.0     # tree still contains the V1.3.0/ folder
#
#   Tags could not be pushed from the environment that performed the cleanup
#   (the sandbox git proxy returns HTTP 403 on tag pushes), so run this from a
#   machine that has push access to the repository.
#
# Usage:
#   ./scripts/create-release-tags.sh            # create + push tags only
#   ./scripts/create-release-tags.sh --releases # also create draft GitHub Releases (needs `gh`)
#
set -euo pipefail

MAKE_RELEASES=false
[[ "${1:-}" == "--releases" ]] && MAKE_RELEASES=true

# version <TAB> commit <TAB> message
# Historical v0–v1.3.0 all entered the repo in the single "Historical Releases"
# commit (54daf0e); the v2.x line maps 1:1 to its own commits.
read -r -d '' RELEASES <<'EOF' || true
v0.0.4	54daf0e	The Serpent's Code — prototype era (v0.0.0–0.0.4)
v1.1.0	54daf0e	The Verdant Code v1.1.0 (historical release)
v1.1.1	54daf0e	The Verdant Code v1.1.1 (historical release)
v1.1.2	54daf0e	The Verdant Code v1.1.2 (historical release)
v1.1.3	54daf0e	The Verdant Code v1.1.3 (historical release)
v1.1.4	54daf0e	The Verdant Code v1.1.4 (historical release)
v1.1.5	54daf0e	The Verdant Code v1.1.5 (historical release)
v1.2.0	54daf0e	The Verdant Code v1.2.0 (historical release)
v1.2.1	54daf0e	The Verdant Code v1.2.1 (historical release)
v1.2.2	54daf0e	The Verdant Code v1.2.2 (historical release)
v1.3.0	54daf0e	The Verdant Code v1.3.0 (historical release)
v2.0.0	e106f29	The Verdant Code 2.0.0 — Master Edition
v2.1.0	3897384	The Verdant Code 2.1.0 — bug fixes & PEP 8
v2.1.1	2c27165	The Verdant Code 2.1.1 — testing verification (3,439 tests)
v2.1.2	539c6c4	The Verdant Code 2.1.2 — PEP 8 & PEP 20 compliance
v2.1.3	dd3f0a1	The Verdant Code 2.1.3 — testing verification (5,611 tests)
v2.1.4	1b84552	The Verdant Code 2.1.4 — menu navigation fixes
v2.1.5	8c0de0e	The Verdant Code 2.1.5 — Reference Mode lesson flow
v2.1.6	4bcdaaa	The Verdant Code 2.1.6 — testing verification
v2.2.0	8ea1d67	The Verdant Code 2.2.0 — code cleanup
EOF

while IFS=$'\t' read -r tag commit message; do
  [[ -z "$tag" ]] && continue
  if git rev-parse -q --verify "refs/tags/$tag" >/dev/null; then
    echo "tag $tag already exists, skipping"
  else
    echo "creating tag $tag -> $commit"
    git tag -a "$tag" "$commit" -m "$message"
  fi
done <<< "$RELEASES"

echo "pushing tags..."
git push origin --tags

if $MAKE_RELEASES; then
  if ! command -v gh >/dev/null; then
    echo "ERROR: GitHub CLI (gh) not found; install it or create releases manually." >&2
    exit 1
  fi
  while IFS=$'\t' read -r tag commit message; do
    [[ -z "$tag" ]] && continue
    echo "creating DRAFT release for $tag"
    gh release create "$tag" \
      --draft \
      --title "$message" \
      --notes "See [CHANGELOG.md](../blob/main/CHANGELOG.md) for the full notes for this release."
  done <<< "$RELEASES"
fi

echo "done."
