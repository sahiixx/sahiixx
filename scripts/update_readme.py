#!/usr/bin/env python3
"""Regenerate the profile README from live GitHub data + data/live_state.json.

Runs in GitHub Actions (stdlib only) and locally. Reads:
  - GitHub API           -> repo counts, languages, stars (via GITHUB_TOKEN)
  - data/live_state.json -> machine-local signals (published by a local task)
Writes README.md.
"""
import json
import os
import sys
import urllib.request
from collections import Counter
from datetime import datetime, timezone

OWNER = "sahiixx"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def api(path):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "sahiixx-readme-bot",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def all_repos():
    """Return (repos, private_visible).

    Prefers the authenticated owner view (includes private repos). Falls back
    to the public-only user view when the token is not the account owner
    (e.g. Actions' GITHUB_TOKEN, which is scoped to a bot).
    """
    try:
        repos, page = [], 1
        while True:
            batch = api(f"/user/repos?per_page=100&page={page}&affiliation=owner")
            if not batch:
                break
            repos.extend(r for r in batch
                         if r["owner"]["login"].lower() == OWNER.lower())
            if len(batch) < 100:
                break
            page += 1
        if repos:
            return repos, True
    except Exception:
        pass

    repos, page = [], 1
    while True:
        batch = api(f"/users/{OWNER}/repos?per_page=100&page={page}&type=owner")
        if not batch:
            break
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return repos, False


def live_state():
    p = os.path.join(ROOT, "data", "live_state.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)
    return {}


def build_readme(repos, st, private_visible=True):
    forks = [r for r in repos if r.get("fork")]
    orig = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    langs = Counter((r.get("language") or "none") for r in repos if r.get("language"))
    top_langs = " · ".join(k for k, _ in langs.most_common(7))

    n_priv = sum(1 for r in repos if r.get("private"))
    if private_visible:
        counts = (f"- **{len(repos)} repos** — {len(orig)} originals + "
                  f"{len(forks)} forks · {len(repos) - n_priv} public / "
                  f"{n_priv} private · {stars} stars")
        badge_n = len(repos)
    else:
        counts = (f"- **{len(repos)} public repos** — {len(orig)} originals + "
                  f"{len(forks)} forks · {stars} stars")
        badge_n = len(repos)

    fc = st.get("firstcall", {})
    edge = st.get("edge", {})
    gh30 = st.get("github_30d", {})
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    gw_row = (
        f"| 🛰️ **Hermes gateway** | `{st.get('gateway_state', 'unknown')}` · "
        f"Telegram `{st.get('telegram', 'unknown')}` |"
    )
    wd_row = (
        f"| 🩺 **Self-healing watchdog** | "
        f"{st.get('watchdog_services', 0)} services supervised · auto-remediation on |"
    )
    fc_row = (
        f"| 🏢 **FirstCall pipeline** | "
        f"{fc.get('leads', 0):,} leads · {fc.get('deals', 0):,} deals · "
        f"{fc.get('outreach', 0):,} outreach · {fc.get('orphans', 0)} orphans |"
    )
    edge_row = (
        f"| ☁️ **Cloudflare edge** | "
        f"{edge.get('workers', 0)} Workers · {edge.get('pages', 0)} Pages · "
        f"{edge.get('r2', 0)} R2 · {edge.get('kv', 0)} KV · {edge.get('queues', 0)} Queue |"
    )
    pulse_row = (
        f"| 📈 **GitHub pulse (30d)** | "
        f"{gh30.get('pushes', 0)} pushes · {gh30.get('prs', 0)} PRs · "
        f"{gh30.get('created', 0)} repos created |"
    )

    return f"""<div align="center">

# SAHIIXX

### AI Systems Architect — Dubai, UAE

*Building an operating system of autonomous agents — from edge runtime to revenue verticals.*

![focus](https://img.shields.io/badge/focus-agentic%20AI%20%C2%B7%20AGI-111111?style=for-the-badge)
![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=for-the-badge&logo=cloudflare&logoColor=white)
![repos](https://img.shields.io/badge/repos-{badge_n}-3E6B4F?style=for-the-badge)
![status](https://img.shields.io/badge/status-live%20%26%20building-brightgreen?style=for-the-badge)

</div>

---

## ⚡ Live now

> Auto-refreshed every 6h by a local agent + GitHub Action. Last update: **{st.get('updated_at', today)}**.

| Signal | State |
|---|---|
{gw_row}
{wd_row}
{fc_row}
{edge_row}
{pulse_row}

---

## 🧠 AI / AGI stack — what I run against

Live models, agents and infra I build with daily:

| Layer | Providers / models |
|---|---|
| **Frontier APIs** | Claude · GPT · Gemini · Kimi (Moonshot) |
| **Open / reasoning** | DeepSeek · Qwen · GLM · Nemotron |
| **Local inference** | GGUF + `llama-server` (offline bundle, byte-verified) |
| **Agent runtimes** | Cline · Hermes · IronClaw/Reborn · OpenClaw |
| **Orchestration** | MCP servers · `sahiixx-bus` pub/sub mesh · n8n |
| **Routing** | TokenRouter · Cline gateway · AgentRouter |

---

## 🏗️ What I'm building

**An agent operating system.** The runtime layer is `sahiixx-agency` (orchestration) + `sahiixx-bus` (pub/sub mesh) + `agentic-harness` (workflow patterns) + `saas-agent-platform` (multi-tenant FastAPI). `agency-agents` and `sovereign-swarm-v2` are the swarm lab.

**A Dubai real-estate revenue vertical.** `FirstCall` (idempotent UAE-leads ingestion → FastAPI), `sovereign-revenue-os`, `nexus-buyer-recovery`, `sovereign-agents` and `lazy-ai-ops` run the pipeline: capture → qualify → geo-match → schedule → report. Mostly private — this is the commercial side.

**A personal assistant with voice + memory.** `friday-os` (LiveKit voice + Tauri + MCP) backed by `sahiixx-titans-memory` and `sahiixx-graph-sight` for persistence and knowledge.

**An edge runtime on Cloudflare.** 9 Workers (`moltbot-sandbox*`, `lead-hunter*`, `opencla`, `f`) and 4 Pages apps — cheap, always-on entry points for agents.

---

## 🔗 How it connects

```mermaid
flowchart TD
    AG[Agent Frameworks<br/>agency-agents · sovereign-swarm-v2<br/>sahiixx-agency · sahiixx-bus · agentic-harness]
    RE[Real-Estate Revenue<br/>FirstCall · sovereign-revenue-os<br/>nexus-buyer-recovery · lazy-ai-ops]
    PA[Assistant / Voice<br/>friday-os · friday-tony-stark · SHADOW]
    MEM[Memory / Knowledge<br/>titans-memory · graph-sight · Trust-graph-]
    EDGE[Edge Runtime<br/>moltworker · moltbot-sandbox* · opencla · lead-hunter*]
    INF[Infra<br/>sahiix-proxy · api-server · dev-helper]

    AG --> RE
    AG --> PA
    AG --> MEM
    EDGE --> RE
    INF --> EDGE
```

---

## 🌐 Live surfaces

| Surface | URL | Status |
|---|---|---|
| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) | 🟢 live |
| SAHIIXX OS | [sahiixx-os.pages.dev](https://sahiixx-os.pages.dev) | 🟢 live |
| Systems panel | [sahiix-systems.pages.dev](https://sahiix-systems.pages.dev) | 🟢 live |

---

## 📊 By the numbers

- {counts.lstrip('- ')}
- **Top languages** — {top_langs}
- **Open source** — 332 merged PRs, mostly kept green by automation

<sub>Auto-generated {today} by a local agent + GitHub Action from live GitHub / Cloudflare / machine state.</sub>

---

## 🎯 Currently

- Hardening the **FirstCall** lead pipeline (capture → qualify → geo-match → revenue)
- Unifying the agent mesh around `sahiixx-bus`
- Consolidating the repo estate (archiving placeholders, merging duplicate sandboxes)

## 📬 Reach me

[Portfolio](https://sahiix-portfolio.pages.dev) · or open an issue on any repo.
"""


def main():
    repos, private_visible = all_repos()
    st = live_state()
    readme = build_readme(repos, st, private_visible)
    out = os.path.join(ROOT, "README.md")
    prev = ""
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            prev = f.read()
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)
    print("README regenerated:",
          "changed" if readme != prev else "unchanged",
          f"({len(repos)} repos, private_visible={private_visible})")


if __name__ == "__main__":
    sys.exit(main())