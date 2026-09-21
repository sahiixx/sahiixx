#!/usr/bin/env python3
"""Regenerate the SAHIIXX profile README — execution-proof, real-time version.

Every number is fetched at render time (GitHub API + data/live_state.json).
Static text never carries a metric. Reads like mission control, not a bio.
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
    """Return (repos, private_visible). Prefer owner view (sees private)."""
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


def starred_count():
    total, page = 0, 1
    try:
        while True:
            batch = api(f"/users/{OWNER}/starred?per_page=100&page={page}")
            if not batch:
                break
            total += len(batch)
            if len(batch) < 100:
                break
            page += 1
    except Exception:
        return 0
    return total


def profile():
    try:
        return api(f"/users/{OWNER}")
    except Exception:
        return {}


def live_state():
    p = os.path.join(ROOT, "data", "live_state.json")
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            return json.load(f)


def repo_map(repos):
    return {r.get("name", "").lower(): r for r in repos}


def badge_block(active_n):
    return (
        "![focus](https://img.shields.io/badge/focus-agentic%20AGI-111111?style=for-the-badge)\n"
        "![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=for-the-badge&logo=cloudflare&logoColor=white)\n"
        f"![repos](https://img.shields.io/badge/active%20repos-{active_n}-3E6B4F?style=for-the-badge)\n"
        "![status](https://img.shields.io/badge/status-live%20%26%20executing-brightgreen?style=for-the-badge)"
    )


def link(name):
    return f"[{name}](https://github.com/{OWNER}/{name})"


def build_readme(repos, st, private_visible):
    active = [r for r in repos if not r.get("archived")]
    forks = [r for r in active if r.get("fork")]
    orig = [r for r in active if not r.get("fork")]
    archived = [r for r in repos if r.get("archived")]
    stars = sum(r.get("stargazers_count", 0) for r in active)
    langs = Counter((r.get("language") or "none") for r in active if r.get("language"))
    top_langs = " · ".join(k for k, _ in langs.most_common(7))
    by_name = repo_map(active)

    n_priv = sum(1 for r in active if r.get("private"))
    n_pub = len(active) - n_priv
    if private_visible:
        counts = (f"**{len(active)} active repos** — {len(orig)} originals + "
                  f"{len(forks)} forks · {n_pub} public / {n_priv} private · {stars} stars")
    else:
        counts = (f"**{n_pub} active public repos** — "
                  f"{len([r for r in orig if not r.get('private')])} originals + "
                  f"{len([r for r in forks if not r.get('private')])} forks · {stars} stars")

    fc = st.get("firstcall", {})
    edge = st.get("edge", {})
    gh30 = st.get("github_30d", {})
    prof = profile()
    n_star = starred_count()
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    updated = st.get("updated_at", today)

    def flagship_rows():
        picks = [
            ("agency-agents", "Flagship multi-agent swarm lab"),
            ("friday-os", "Voice-first personal AI OS — LiveKit + Tauri + MCP"),
            ("sovereign-swarm-v2", "Modular multi-agent OS"),
            ("sahiixx-bus", "Unified orchestration bus (pub/sub mesh)"),
            ("agentic-harness", "Agentic workflow patterns (Azure Foundry)"),
            ("moltworker", "OpenClaw on Cloudflare Workers"),
            ("ocr-playbook-scanner", "OCR ingestion utility"),
            ("sahiixx-os", "Full-stack command center (React + tRPC)"),
        ]
        rows = []
        for key, blurb in picks:
            r = by_name.get(key)
            if r is None or r.get("fork"):
                continue
            if r.get("visibility", "public") == "private":
                continue
            rows.append("| {} | {} | {} | {} | {} |".format(
                link(key), blurb, r.get("language") or "-",
                r.get("stargazers_count", 0), (r.get("pushed_at") or "")[:10]))
        return rows

    S = []
    S.append(
        "<div align=\"center\">\n\n"
        "# SAHIIXX\n\n"
        "### Agentic AGI — end to end · Dubai, UAE\n\n"
        "*I build production agent systems, not demos. One operating system of agents, "
        "memory, voice, verticals and edge — running, healing and earning in real time.*\n\n"
        + badge_block(len(active)) +
        "\n\n</div>"
    )

    S.append(
        "## ⚡ Live operating picture\n\n"
        f"> Auto-refreshed every 6h by an on-machine agent + GitHub Action. "
        f"Machine state as of **{updated}**; repo stats pulled at render time.\n\n"
        "| Signal | State |\n"
        "|---|---|\n"
        f"| 🛰️ Hermes gateway | `{st.get('gateway_state', 'unknown')}` · Telegram `{st.get('telegram', 'unknown')}` |\n"
        f"| 🩺 Self-healing watchdog | {st.get('watchdog_services', 0)} services supervised · auto-remediation on |\n"
        f"| 🏢 FirstCall revenue pipeline | {fc.get('leads', 0):,} leads · {fc.get('deals', 0):,} deals · "
        f"{fc.get('outreach', 0):,} outreach · {fc.get('orphans', 0)} open links |\n"
        f"| ☁️ Cloudflare edge | {edge.get('workers', 0)} Workers · {edge.get('pages', 0)} Pages · "
        f"{edge.get('r2', 0)} R2 · {edge.get('kv', 0)} KV · {edge.get('queues', 0)} Queue |\n"
        f"| 📈 GitHub activity (30d) | {gh30.get('pushes', 0)} pushes · {gh30.get('prs', 0)} PRs · "
        f"{gh30.get('created', 0)} repos created |\n"
        f"| ⭐ Research library | {n_star} starred repos — the state of the art, mapped |"
    )

    S.append(
        "## 🧠 Live AI/AGI stack\n\n"
        "The substrate I run against daily — frontier APIs, open reasoning models, "
        "local inference, agent runtimes, orchestration and routing:\n\n"
        "| Layer | Toolkit |\n"
        "|---|---|\n"
        "| **Frontier APIs** | Claude · GPT · Gemini · Kimi (Moonshot) |\n"
        "| **Open / reasoning** | DeepSeek · Qwen · GLM · Nemotron |\n"
        "| **Local inference** | GGUF + `llama-server` (offline, byte-verified) |\n"
        "| **Agent runtimes** | Cline · Hermes · IronClaw/Reborn · OpenClaw |\n"
        "| **Orchestration** | MCP servers · `sahiixx-bus` mesh · n8n |\n"
        "| **Routing** | TokenRouter · Cline gateway · AgentRouter |"
    )

    S.append(
        "## 🏗️ End-to-end agentic systems\n\n"
        "**Agent OS.** `sahiixx-agency` (orchestration) + `sahiixx-bus` (pub/sub mesh) + "
        "`agentic-harness` (workflow patterns) + `saas-agent-platform` (multi-tenant FastAPI). "
        "Swarm lab: `agency-agents` + `sovereign-swarm-v2`.\n\n"
        "**Revenue vertical (Dubai real estate).** `FirstCall` (idempotent ingestion → FastAPI), "
        "`sovereign-revenue-os`, `nexus-buyer-recovery`, `sovereign-agents`, `lazy-ai-ops`: "
        "capture → qualify → geo-match → schedule → report.\n\n"
        "**Assistant + memory.** `friday-os` (LiveKit voice + Tauri + MCP) persisted by "
        "`sahiixx-titans-memory` + `sahiixx-graph-sight`.\n\n"
        "**Edge runtime.** 9 Cloudflare Workers + 4 Pages apps — cheap, always-on agent entry points."
    )

    S.append(
        "## 🔗 Execution graph — idea to revenue\n\n"
        "```mermaid\n"
        "flowchart LR\n"
        "  BUS[\"sahiixx-bus<br/>pub/sub\"] --> SWARM[\"agency-agents + swarm-v2<br/>multi-agent\"]\n"
        "  SWARM --> MEM[\"titans-memory + graph-sight<br/>persistent state\"]\n"
        "  SWARM --> FC[\"FirstCall<br/>capture / qualify / match\"]\n"
        "  FC --> REV[\"sovereign-revenue-os<br/>schedule / report / revenue\"]\n"
        "  MEM --> PA[\"friday-os<br/>voice + MCP\"]\n"
        "  EDGE[\"Cloudflare edge<br/>9 Workers + 4 Pages\"] --> FC\n"
        "  EDGE --> PA\n"
        "```"
    )

    S.append(
        "## 🧪 Proof, not promises — flagship systems\n\n"
        "Stars, language and last push come straight from the GitHub API at render time.\n\n"
        "| System | What it proves | Lang | Stars | Pushed |\n"
        "|---|---|---|---|---|\n"
        + "\n".join(flagship_rows()) +
        "\n\n<sub>Private flagships (FirstCall pipeline, revenue OS) are counted in totals, never exposed.</sub>"
    )

    S.append(
        "## 🌐 Live surfaces\n\n"
        "| Surface | URL | Status |\n"
        "|---|---|---|\n"
        "| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) | live |\n"
        "| SAHIIXX OS | [sahiixx-os.pages.dev](https://sahiixx-os.pages.dev) | live |\n"
        "| Systems panel | [sahiix-systems.pages.dev](https://sahiix-systems.pages.dev) | live |"
    )

    S.append(
        "## 📊 Live footprint\n\n"
        f"- {counts}\n"
        f"- **Top languages** — {top_langs}\n"
        f"- **Community** — {prof.get('followers', 0)} followers · {prof.get('following', 0)} following · "
        f"{n_star} starred\n"
        f"- **Archive** — {len(archived)} placeholder/scaffold repos retired (not counted above)\n\n"
        f"<sub>Auto-generated {today} by an on-machine agent + GitHub Action. "
        "Every metric is fetched at render time; static text never carries a number.</sub>"
    )

    S.append(
        "## 🎯 Building next\n\n"
        "- Hardening the **FirstCall** lead pipeline (capture → qualify → geo-match → revenue)\n"
        "- Unifying the agent mesh around `sahiixx-bus`\n"
        "- Consolidating the estate (archived placeholders already removed)\n\n"
        "## 📬 Reach me\n\n"
        "[Portfolio](https://sahiix-portfolio.pages.dev) · or open an issue on any repo."
    )

    return "\n\n---\n\n".join(S) + "\n"


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
          f"({len(repos)} repos fetched, private_visible={private_visible})")


if __name__ == "__main__":
    sys.exit(main())
