# Profile hygiene

## Status (2026-09-07)

| Action | Via this connector | Via `gh` script |
|--------|--------------------|-----------------|
| Profile README + REPO_MAP | **Done** (merged) | — |
| Archive noise repos | **Blocked** (no `update_repository` / archive scope) | `scripts/profile-hygiene.sh` |
| Set topics on core | **Blocked** (no topics API in connector) | same script |
| Star core repos | **Blocked** (403) | optional |

## Run locally (one shot)

```bash
gh auth login   # as sahiixx
cd /path/to/sahiixx   # this profile repo
bash scripts/profile-hygiene.sh
```

### What the script archives (safe list)

`7` · `Bag` · `Big` · `Bvvh` · `Gsje` · `H` · `Hh` · `SHADOW` · `studious-sniffle` · `X` · `X1` · `Xxxxxxx` · `nextjs-ai-chatbotg`

**Not archived (keep):**
- `f` — Workers AI gateway
- `Fixfiz` / `Fixfizx` / `Y` / `Genxai` — non-trivial size or labeled experiments

### Topics applied to core

All core products get `sahiixx` plus role tags (`opa`, `edge`, `lead-machine`, …).

## After running

1. Confirm archived: [archived:true](https://github.com/sahiixx?tab=repositories&q=archived%3Atrue)
2. Confirm topics: [topic:sahiixx](https://github.com/sahiixx?tab=repositories&q=topic%3Asahiixx)
3. Optionally pin: agency · proxy · e2e · os · portfolio · os-docs

## Connector note

To allow agents to archive/topic without a local script, reconnect GitHub with **Administration** (or repo edit) scopes for the integration.
