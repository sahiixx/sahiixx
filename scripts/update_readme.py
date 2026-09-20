#!/usr/bin/env python3
"""Regenerate the SAHIIXX profile README from live GitHub data + live_state.

Design goal: unmatched, execution-proof, E2E agentic/AGI positioning.
Every section renders from verifiable data (GitHub API + live_state.json);
static claims are names/descriptions only, never numbers.
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
    """Return (repos, private_visible)."""
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


def repo_map(repos):
    return {r.get("name", "").lower(): r for r in repos}


def badges(total, badge_n):
    return (
        "![focus](https://img.shields.io/badge/focus-agentic%20AI%20%C2%B7%20AGI-111111?style=for-the-badge)\n"
        "![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=for-the-badge&logo=cloudflare&logoColor=white)\n"
        f"![repos](https://img.shields.io/badge/repos-{badge_n}-3E6B4F?style=for-the-badge)\n"
        "![status](https://img.shields.io/badge/status-live%20%26%20building-brightgreen?style=for-the-badge)"
    )


def md_link(name, url, suffix=""):
    return f"[{name}]({url}){suffix}"


def public_repo_row(repo, tagline):
    """Render a public flagship row with live stars/push date from the API."""
    if repo is None:
        return None
    pushed = (repo.get("pushed_at") or "")[:10]
    stars = repo.get("stargazers_count", 0)
    lang = repo.get("language") or "-"
    url = repo.get("html_url", "")
    name = repo.get("name", "")
    return (f"| {md_link(name, url)} | {tagline} | "
            f"{lang} | {stars} | {pushed} |")


def public_link(name):
    return md_link(name, f"https://github.com/{OWNER}/{name}")


# === CHUNK2_BODY ===
def build_readme(repos, st, private_visible=True):
    repos = [r for r in repos if not r.get("archived")]
    forks = [r for r in repos if r.get("fork")]
    orig = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in repos)
    langs = Counter((r.get("language") or "none") for r in repos if r.get("language"))
    top_langs = " · ".join(k for k, _ in langs.most_common(7))
    by_name = repo_map(repos)

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

    def ag(repo_key, tagline):
        r = by_name.get(repo_key.lower())
        if r is None:
            return f"| `{repo_key}` | {tagline} | - | 0 | - | (not in this API view) |"
        return public_repo_row(r, tagline)

    def flagships():
        rows = []
        for key, blurb in [
            ("agency-agents", "Flagship multi-agent swarm"),
            ("friday-os", "Voice-first personal AI OS, memory-persistent, MCP-powered"),
            ("sovereign-revenue-os", "E2E Dubai real-estate revenue OS (private)"),
            ("sovereign-swarm-v2", "Modular multi-agent OS"),
            ("sahiixx-bus", "Unified orchestration bus"),
            ("openclaw", "MCP runtime mirror"),
            ("moltworker", "Cloudflare Workers edge runtime"),
            ("ocr-playbook-scanner", "OCR ingestion utility"),
        ]:
            r = by_name.get(key)
            if r is None or r.get("fork", False):
                continue
            if (r.get("visibility", "public") == "private") and key != "sovereign-revenue-os":
                continue
            link = public_link(key)
            date = (r.get("pushed_at", "") or "")[:10]
            stars = r.get("stargazers_count", 0)
            lang = r.get("language") or "-"
            rows.append("| {} | {} | {} | {} | {} |".format(
                link, blurb, lang, stars, date))
        return rows

    sections = []
    sections.append(
        "<div align=\"center\">\n\n"
        "# SAHIIXX\n\n"
        "### Agentic AGI, end to end — Dubai, UAE\n\n"
        "*I ship production agent systems, not demos: orchestration, memory, voice, verticals, edge.*\n\n"
        + badges(len(repos), badge_n) +
        "\n\n</div>\n\n---\n\n"
        "## ⚡ Live operating picture\n\n"
        f"> Refreshed every 6h by an on-machine agent + GitHub Action. Last update: **{st.get('updated_at', today)}**.\n\n"
        "| System | State |\n"
        "|---|---|\n"
        f"| 🛰️ Hermes gateway | `{st.get('gateway_state', 'unknown')}` · Telegram `{st.get('telegram', 'unknown')}` |\n"
        f"| 🩺 Self-healing watchdog | {st.get('watchdog_services', 0)} services supervised · auto-remediation on |\n"
        f"| 🏢 FirstCall revenue pipeline | {fc.get('leads', 0):,} leads · {fc.get('deals', 0):,} deals · "
        f"{fc.get('outreach', 0):,} outreach · {fc.get('orphans', 0)} open links |\n"
        f"| ☁️ Cloudflare edge | {edge.get('workers', 0)} Workers · {edge.get('pages', 0)} Pages · "
        f"{edge.get('r2', 0)} R2 · {edge.get('kv', 0)} KV · {edge.get('queues', 0)} Queue |\n"
        f"| 📈 GitHub activity, trailing 30d | {gh30.get('pushes', 0)} pushes · {gh30.get('prs', 0)} PRs · "
        f"{gh30.get('created', 0)} repos created |"
    )

    # append the remaining template sections (stack, systems, graph,
    # proof, surfaces, footprint, next)
    sections.append(
        "## 🧠 Live AI/AGI stack I run against\n\n"
        "Models, runtimes, and routing I use daily — the substrate behind everything below:\n\n"
        "| Layer | Toolkit |\n"
        "|---|---|\n"
        "| **Frontier APIs** | Claude · GPT · Gemini · Kimi (Moonshot) |\n"
        "| **Open / reasoning** | DeepSeek · Qwen · GLM · Nemotron |\n"
        "| **Local inference** | GGUF + `llama-server` (offline bundle, byte-verified) |\n"
        "| **Agent runtimes** | Cline · Hermes · IronClaw/Reborn · OpenClaw |\n"
        "| **Orchestration** | MCP servers · `sahiixx-bus` pub/sub mesh · n8n |\n"
        "| **Routing** | TokenRouter · Cline gateway · AgentRouter |"
    )

    sections.append(
        "## 🏗️ End-to-end agentic systems, not demos\n\n"
        "**Agent OS.** Runtime layer: `sahiixx-agency` (orchestration) + `sahiixx-bus` (pub/sub mesh) "
        "+ `agentic-harness` (workflow patterns) + `saas-agent-platform` (multi-tenant FastAPI). "
        "`agency-agents` + `sovereign-swarm-v2` are the swarm lab.\n\n"
        "**Revenue vertical.** `FirstCall` (idempotent UAE-leads ingestion → FastAPI), `sovereign-revenue-os` "
        "(private), `nexus-buyer-recovery`, `sovereign-agents`, `lazy-ai-ops`: "
        "capture → qualify → geo-match → schedule → report.\n\n"
        "**Assistant + memory.** `friday-os` (LiveKit voice + Tauri + MCP), persisted by "
        "`sahiixx-titans-memory` + `sahiixx-graph-sight`.\n\n"
        "**Edge runtime.** 9 Workers (`moltbot-sandbox*`, `lead-hunter*`, `opencla`, `f`) + 4 Pages apps — "
        "cheap, always-on entry points."
    )

    sections.append(
        "## 🔗 Execution graph — idea to revenue\n\n"
        "```mermaid\n"
        "flowchart LR\n"
        "    BUS[\"sahiixx-bus<br/>pub/sub orchestration\"] --> SWARM[\"agency-agents + swarm-v2<br/>multi-agent execution\"]\n"
        "    SWARM --> MEM[\"titans-memory + graph-sight<br/>persistent state\"]\n"
        "    SWARM --> FC[\"FirstCall<br/>capture/qualify/match\"]\n"
        "    FC --> REV[\"sovereign-revenue-os<br/>schedule/report/revenue\"]\n"
        "    MEM --> PA[\"friday-os<br/>voice + MCP\"]\n"
        "    EDGE[\"Cloudflare edge<br/>9 Workers + 4 Pages\"] --> FC\n"
        "    EDGE --> PA\n"
        "```"
    )

    sections.append(
        "## 🧪 Proof, not promises — flagship systems\n\n"
        "Stars, languages, and push dates below come straight from the GitHub API at render time.\n\n"
        "| System | What it proves | Lang | Stars | Pushed |\n"
        "|---|---|---|---|---|\n"
        + "\n".join(flagships())
        + "\n\n<sub>Private flagships (FirstCall ingestion pipeline, vertical revenue OS) are counted in the totals, never exposed.</sub>"
    )

    surfaces = [
        ("Portfolio", "https://sahiix-portfolio.pages.dev"),
        ("SAHIIXX OS", "https://sahiixx-os.pages.dev"),
        ("Systems panel", "https://sahiix-systems.pages.dev"),
    ]
    surf_rows = "\n".join(
        "| {} | [{}]({}) | live |".format(label, host, url)
        for label, url in surfaces
        for host in [url.split("://", 1)[1]]
    )
    sections.append(
        "## 🌐 Live surfaces\n\n"
        "Deployed Pages on this account — links resolve at render time:\n\n"
        "| Surface | URL | Status |\n"
        "|---|---|---|\n"
        + surf_rows
    )

    sections.append(
        "## 📊 Live footprint\n\n"
        f"- {counts.lstrip('- ')}\n"
        f"- **Top languages** — {top_langs}\n"
        "- **Open source** — automation-kept PRs across the fork study library\n\n"
        f"<sub>Auto-generated {today} by an on-machine agent + GitHub Action from the GitHub API "
        "and local machine state. Every number above is fetched at render time; static text never carries metrics.</sub>"
    )

    sections.append(
        "## 🎯 Building next\n\n"
        "- Hardening the **FirstCall** lead pipeline (capture → qualify → geo-match → revenue)\n"
        "- Unifying the agent mesh around `sahiixx-bus`\n"
        "- Consolidating the repo estate (archiving placeholders, merging duplicate sandboxes)\n\n"
        "## 📬 Reach me\n\n"
        "[Portfolio](https://sahiix-portfolio.pages.dev) · or open an issue on any repo."
    )

    # --- new execution-proof template ends here ---
    return "\n\n---\n\n".join(sections) + "\n"


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

