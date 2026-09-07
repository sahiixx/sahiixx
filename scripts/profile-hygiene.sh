#!/usr/bin/env bash
# SAHIIXX profile hygiene — run once with: gh auth status && bash scripts/profile-hygiene.sh
# Requires: GitHub CLI (gh) authenticated as sahiixx
set -euo pipefail

OWNER="sahiixx"

# ── 1. Archive noise (safe list — empty / degenerate names only) ─────────────
# Skipped on purpose: f (Workers AI gateway), Fixfiz*, Y (non-trivial size)
NOISE=(
  "7"
  "Bag"
  "Big"
  "Bvvh"
  "Gsje"
  "H"
  "Hh"
  "SHADOW"
  "studious-sniffle"
  "X1"
  "Xxxxxxx"
  "X"
  "nextjs-ai-chatbotg"
)

echo "=== Archiving noise repos ==="
for repo in "${NOISE[@]}"; do
  if gh repo view "$OWNER/$repo" --json name -q .name >/dev/null 2>&1; then
    echo "  archive $OWNER/$repo"
    gh repo archive "$OWNER/$repo" --yes 2>/dev/null || \
      gh api -X PATCH "repos/$OWNER/$repo" -f archived=true >/dev/null
  else
    echo "  skip (missing) $repo"
  fi
done

# ── 2. Topics on core products ───────────────────────────────────────────────
echo "=== Setting topics on core ==="

put_topics() {
  local repo="$1"
  shift
  local names=("$@")
  local json
  json=$(printf '%s\n' "${names[@]}" | jq -R . | jq -s '{names: .}')
  echo "  topics $repo → ${names[*]}"
  gh api -X PUT "repos/$OWNER/$repo/topics" \
    -H "Accept: application/vnd.github.mercy-preview+json" \
    --input - <<<<"$json" >/dev/null
}

put_topics sahiixx-agency          sahiixx opa multi-agent lead-machine fastapi orchestration
put_topics sahiix-proxy            sahiixx edge proxy governance termux jwt
put_topics sahiixx-e2e             sahiixx e2e playwright lead-machine testing
put_topics sahiixx-os              sahiixx os command-center typescript
put_topics sahiix-portfolio        sahiixx portfolio nexus pilots
put_topics sahiix-os-docs          sahiixx docs architecture stack
put_topics systems-panel           sahiixx dashboard status astro
put_topics agentic-harness         sahiixx agents harness azure-foundry
put_topics agentic-harness-integration sahiixx agents harness integration
put_topics sahiixx-bus             sahiixx bus pubsub mcp
put_topics sahiixx-titans-memory   sahiixx memory titans
put_topics sahiixx-graph-sight     sahiixx graph neo4j
put_topics friday-os               sahiixx voice assistant mcp
put_topics sovereign-swarm-v2      sahiixx swarm multi-agent dubai real-estate
put_topics sahiixx-geoflow-agent   sahiixx geo dubai real-estate
put_topics sahiixx-clearwing       sahiixx security pentest
put_topics sahiix-agi              sahiixx agi coordination
put_topics sahiixx                 sahiixx profile readme
put_topics saas-agent-platform     sahiixx saas multi-tenant agents
put_topics moltworker              sahiixx cloudflare workers openclaw

echo "=== Done ==="
echo "Verify: https://github.com/sahiixx?tab=repositories&q=archived%3Atrue"
echo "Core topics: https://github.com/sahiixx?tab=repositories&q=topic%3Asahiixx"
