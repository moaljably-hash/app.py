#!/bin/bash
# Installs the directing-stickman-videos skill's Node dependencies on session start.
set -euo pipefail
SKILL_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}/.claude/skills/directing-stickman-videos"
[ -f "$SKILL_DIR/package.json" ] || exit 0
[ -d "$SKILL_DIR/node_modules" ] && exit 0
command -v npm >/dev/null 2>&1 || exit 0
cd "$SKILL_DIR" && npm ci --no-audit --no-fund --silent >/dev/null 2>&1 || echo "stickman skill: npm ci failed; run it manually in $SKILL_DIR" >&2
exit 0
