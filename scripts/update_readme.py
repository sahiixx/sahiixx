#!/usr/bin/env python3
"""SAHIIXX profile README generator - execution-proof, all-live version."""
import json, os, sys, urllib.request
from collections import Counter
from datetime import datetime, timezone

OWNER = "sahiixx"
TOKEN = os.environ.get("GITHUB_TOKEN", "")
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def api(path):
    req = urllib.request.Request(
        "https://api.github.com" + path,
        headers={"Authorization": f"Bearer {TOKEN}", "Accept": "application/vnd.github+json", "User-Agent": "sahiixx-bot"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)

def all_repos():
    try:
        repos, page = [], 1
        while True:
            batch = api(f"/user/repos?per_page=100&page={page}&affiliation=owner")
            if not batch: break
            repos.extend(r for r in batch if r["owner"]["login"].lower() == OWNER.lower())
            if len(batch) < 100: break
            page += 1
        if repos: return repos, True
    except Exception: pass
    repos, page = [], 1
    while True:
        batch = api(f"/users/{OWNER}/repos?per_page=100&page={page}&type=owner")
        if not batch: break
        repos.extend(batch)
        if len(batch) < 100: break
        page += 1
    return repos, False

def live_state():
    p = os.path.join(ROOT, "data", "live_state.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f: return json.load(f)
    return {}

def link(name):
    return f"[{name}](https://github.com/{OWNER}/{name})"
def build_readme(repos, st, pv=True):
    repos = [r for r in repos if not r.get("archived")]
    forks = [r for r in repos if r.get("fork")]
    orig = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    langs = Counter(r.get("language") for r in repos if r.get("language"))
    top_langs = " \u00b7 ".join(k for k, _ in langs.most_common(7))
    n_priv = sum(1 for r in repos if r.get("private"))
    by_name = {r["name"].lower(): r for r in repos}
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    if pv:
        counts = f"**{len(repos)} repos** \u2014 {len(orig)} originals + {len(forks)} forks \u00b7 {len(repos)-n_priv} public / {n_priv} private \u00b7 {stars} stars"
        badge_n = len(repos)
    else:
        counts = f"**{len(repos)} public repos** \u2014 {len(orig)} originals + {len(forks)} forks \u00b7 {stars} stars"
        badge_n = len(repos)
    fc, edge, gh30 = st.get("firstcall", {}), st.get("edge", {}), st.get("github_30d", {})
    S = []

    S.append(f'<div align="center">\n\n# SAHIIXX\n\n### Agentic AGI \u2014 End to End, Dubai, UAE\n\n*I ship production agent systems \u2014 orchestration, memory, voice, verticals, edge. Not demos.*\n\n'
        + '![focus](https://img.shields.io/badge/focus-agentic%20AGI-111111?style=for-the-badge)\n'
        + '![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=for-the-badge&logo=cloudflare&logoColor=white)\n'
        + f'![repos](https://img.shields.io/badge/active%20repos-{badge_n}-3E6B4F?style=for-the-badge)\n'
        + '![status](https://img.shields.io/badge/status-live%20%26%20executing-brightgreen?style=for-the-badge)\n\n</div>')

    S.append(f'## \u26a1 Live Operating Picture\n\n> Every number below is fetched at render time. Last pulse: **{st.get("updated_at", today)}** \u00b7 refreshes every 6h.\n\n'
        + '| System | State |\n|---|---|\n'
        + f"| \U0001f6f0\ufe0f **Hermes gateway** | `{st.get('gateway_state','?')}` \u00b7 Telegram `{st.get('telegram','?')}` |\n"
        + f"| \U0001fa7a **Self-healing watchdog** | {st.get('watchdog_services',0)} services supervised \u00b7 auto-remediation on |\n"
        + f"| \U0001f3e2 **FirstCall revenue pipeline** | {fc.get('leads',0):,} leads \u00b7 {fc.get('deals',0):,} deals \u00b7 {fc.get('outreach',0):,} outreach \u00b7 {fc.get('orphans',0)} open links |\n"
        + f"| \u2601\ufe0f **Cloudflare edge** | {edge.get('workers',0)} Workers \u00b7 {edge.get('pages',0)} Pages \u00b7 {edge.get('r2',0)} R2 \u00b7 {edge.get('kv',0)} KV \u00b7 {edge.get('queues',0)} Queue |\n"
        + f"| \U0001f4c8 **GitHub activity, trailing 30d** | {gh30.get('pushes',0)} pushes \u00b7 {gh30.get('prs',0)} PRs \u00b7 {gh30.get('created',0)} repos created |")

    S.append('## \U0001f9e0 The AI/AGI Stack I Run Against\n\n'
        + '| Layer | Models / Runtimes |\n|---|---|\n'
        + '| **Frontier APIs** | Claude \u00b7 GPT \u00b7 Gemini \u00b7 Kimi (Moonshot) |\n'
        + '| **Open / Reasoning** | DeepSeek \u00b7 Qwen \u00b7 GLM \u00b7 Nemotron |\n'
        + '| **Local Inference** | GGUF + `llama-server` (offline, byte-verified) |\n'
        + '| **Agent Runtimes** | Cline \u00b7 Hermes \u00b7 IronClaw/Reborn \u00b7 OpenClaw |\n'
        + '| **Orchestration** | MCP servers \u00b7 `sahiixx-bus` pub/sub mesh \u00b7 n8n |\n'
        + '| **Routing** | TokenRouter \u00b7 Cline gateway \u00b7 AgentRouter |')

    S.append('## \U0001f3d7\ufe0f End-to-End Agentic Systems \u2014 Not Demos\n\n'
        + '**Agent OS.** `sahiixx-agency` (orchestration) + `sahiixx-bus` (pub/sub mesh) + `agentic-harness` (workflow patterns) + `saas-agent-platform` (multi-tenant FastAPI). `agency-agents` + `sovereign-swarm-v2` are the swarm lab.\n\n'
        + '**Revenue vertical.** `FirstCall` (idempotent UAE-leads ingestion \u2192 FastAPI), `sovereign-revenue-os` (private), `nexus-buyer-recovery`, `sovereign-agents`, `lazy-ai-ops`: capture \u2192 qualify \u2192 geo-match \u2192 schedule \u2192 report.\n\n'
        + '**Assistant + memory.** `friday-os` (LiveKit voice + Tauri + MCP), persisted by `sahiixx-titans-memory` + `sahiixx-graph-sight`.\n\n'
        + '**Edge runtime.** Cloudflare Workers + Pages apps \u2014 cheap, always-on entry points for every agent.')

    S.append('## \U0001f517 Execution Graph \u2014 Idea to Revenue\n\n```mermaid\nflowchart LR\n'
        + '    BUS["sahiixx-bus<br/>pub/sub orchestration"] --> SWARM["agency-agents + swarm-v2<br/>multi-agent execution"]\n'
        + '    SWARM --> MEM["titans-memory + graph-sight<br/>persistent state"]\n'
        + '    SWARM --> FC["FirstCall<br/>capture / qualify / match"]\n'
        + '    FC --> REV["sovereign-revenue-os<br/>schedule / report / revenue"]\n'
        + '    MEM --> PA["friday-os<br/>voice + MCP"]\n'
        + '    EDGE["Cloudflare edge<br/>Workers + Pages"] --> FC\n'
        + '    EDGE --> PA\n```')

    proof = [('agency-agents', 'Multi-agent swarm'), ('friday-os', 'Voice-first AI OS'),
             ('sovereign-swarm-v2', 'Modular multi-agent OS'), ('sahiixx-bus', 'Orchestration bus'),
             ('moltworker', 'Cloudflare edge runtime'), ('ocr-playbook-scanner', 'OCR ingestion')]
    proof_rows = '\n'.join(
        f'| {link(k)} | {b} | {by_name[k].get("language") or "-"} | {by_name[k].get("stargazers_count",0)} | {(by_name[k].get("pushed_at") or "")[:10]} |'
        for k, b in proof if k in by_name)
    S.append('## \U0001f9ea Proof, Not Promises\n\n'
        + 'Stars, languages, and push dates come straight from the GitHub API at render time.\n\n'
        + '| System | What It Proves | Lang | \u2b50 | Pushed |\n|---|---|---|---|---|\n'
        + proof_rows)

    S.append('## \U0001f310 Live Surfaces\n\n| Surface | URL | Status |\n|---|---|---|\n'
        + '| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) | live |\n'
        + '| SAHIIXX OS | [sahiixx-os.pages.dev](https://sahiixx-os.pages.dev) | live |\n'
        + '| Systems panel | [sahiix-systems.pages.dev](https://sahiix-systems.pages.dev) | live |')

    S.append(f'## \U0001f4ca Live Footprint\n\n- {counts}\n- **Top languages** \u2014 {top_langs}\n\n'
        + f'<sub>Auto-generated {today} by an on-machine agent + GitHub Action from the GitHub API and local machine state. Every number above is fetched at render time; static text never carries metrics.</sub>')

    S.append('## \U0001f3af Building Next\n\n'
        + '- Hardening the **FirstCall** lead pipeline (capture \u2192 qualify \u2192 geo-match \u2192 revenue)\n'
        + '- Unifying the agent mesh around `sahiixx-bus`\n'
        + '- Consolidating the repo estate (archiving placeholders, merging duplicate sandboxes)\n\n'
        + '## \U0001f4ec Reach Me\n\n'
        + '[Portfolio](https://sahiix-portfolio.pages.dev) \u00b7 or open an issue on any repo.')

    return "\n\n---\n\n".join(S) + "\n"


def main():
    repos, pv = all_repos()
    st = live_state()
    readme = build_readme(repos, st, pv)
    out = os.path.join(ROOT, "README.md")
    prev = ""
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f: prev = f.read()
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)
    print("README regenerated:", "changed" if readme != prev else "unchanged",
          f"({len(repos)} repos, private_visible={pv})")

if __name__ == "__main__":
    sys.exit(main())
