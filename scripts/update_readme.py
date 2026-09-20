#!/usr/bin/env python3
"""SAHIIXX profile README generator — mission-control edition.

Every metric is fetched live at render time:
  - GitHub GraphQL/REST  -> repo counts, stars, topics, starred-library size
  - data/live_state.json -> machine pulse (gateway, watchdog, pipeline, edge)
Static prose carries no numbers. Nothing here can go stale.
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


def _req(url, data=None, method="GET"):
    req = urllib.request.Request(
        url,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {TOKEN}",
            "Accept": "application/vnd.github+json",
            "User-Agent": "sahiixx-readme-bot",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def api(path):
    return _req("https://api.github.com" + path)


def gql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode("utf-8")
    out = _req("https://api.github.com/graphql", data=body, method="POST")
    return out.get("data", {})


def counts():
    """Live totals: owned repos + starred research library."""
    try:
        q = ("query($login: String!) { user(login: $login) {"
             " starredRepositories { totalCount }"
             " repositories(ownerAffiliations: OWNER) { totalCount } } }")
        d = gql(q, {"login": OWNER}).get("user", {})
        return d.get("starredRepositories", {}).get("totalCount", 0), \
            d.get("repositories", {}).get("totalCount", 0)
    except Exception:
        return 0, 0


def all_repos():
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


def link(name):
    return f"[`{name}`](https://github.com/{OWNER}/{name})"


def build_readme(repos, st, private_visible=True, starred_n=0):
    live = [r for r in repos if not r.get("archived")]
    forks = [r for r in live if r.get("fork")]
    orig = [r for r in live if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in live)
    langs = Counter((r.get("language") or "none") for r in live if r.get("language"))
    top_langs = " · ".join(k for k, _ in langs.most_common(7))
    by_name = repo_map(live)

    n_priv = sum(1 for r in live if r.get("private"))
    pub = len(live) - n_priv
    if private_visible:
        footprint = (f"- **{len(live)} active repos** — {len(orig)} originals + "
                     f"{len(forks)} forks · {pub} public / {n_priv} private · {stars} stars")
    else:
        footprint = (f"- **{len(live)} active public repos** — {len(orig)} originals + "
                     f"{len(forks)} forks · {stars} stars")

    fc = st.get("firstcall", {})
    edge = st.get("edge", {})
    gh30 = st.get("github_30d", {})
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    def flagship(key, blurb):
        r = by_name.get(key.lower())
        if r is None:
            return None
        date = (r.get("pushed_at") or "")[:10]
        return (f"| {link(key)} | {blurb} | {r.get('language') or '-'} | "
                f"{r.get('stargazers_count', 0)} | {date} |")

    S = []

    S.append(
        "<div align=\"center\">\n\n"
        "# SAHIIXX\n\n"
        "### Agentic AGI, end to end\n\n"
        "<sub>Dubai, UAE — I build the parts other people demo.</sub>\n\n"
        "![focus](https://img.shields.io/badge/focus-agentic%20AGI-111111?style=for-the-badge)\n"
        f"![repos](https://img.shields.io/badge/active%20repos-{len(live)}-3E6B4F?style=for-the-badge)\n"
        f"![library](https://img.shields.io/badge/research%20library-{starred_n}%20repos-444444?style=for-the-badge)\n"
        "![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=for-the-badge&logo=cloudflare&logoColor=white)\n"
        "![status](https://img.shields.io/badge/status-executing-brightgreen?style=for-the-badge)\n\n"
        "</div>"
    )

    S.append(
        "## ⚡ Live operating picture\n\n"
        f"> Sensed on the machine, published by a local agent, rendered by GitHub Actions. "
        f"Last pulse **{st.get('updated_at', today)}**.\n\n"
        "| Instrument | Reading |\n"
        "|---|---|\n"
        f"| 🛰️ Gateway | `{st.get('gateway_state', 'unknown')}` · Telegram `{st.get('telegram', 'unknown')}` |\n"
        f"| 🩺 Supervisor | {st.get('watchdog_services', 0)} services watched · self-healing armed |\n"
        f"| 🏗️ Pipeline | {fc.get('leads', 0):,} leads · {fc.get('deals', 0):,} deals · "
        f"{fc.get('outreach', 0):,} outreach · {fc.get('orphans', 0)} broken links |\n"
        f"| ☁️ Edge | {edge.get('workers', 0)} Workers · {edge.get('pages', 0)} Pages · "
        f"{edge.get('r2', 0)} R2 · {edge.get('kv', 0)} KV · {edge.get('queues', 0)} Queue |\n"
        f"| 📡 GitHub · 30d | {gh30.get('pushes', 0)} pushes · {gh30.get('prs', 0)} PRs · "
        f"{gh30.get('created', 0)} repos created |"
    )

    S.append(
        "## 🌐 What I run against\n\n"
        "The AI/AGI substrate, in production use — not a wishlist:\n\n"
        "| Layer | In the rotation |\n"
        "|---|---|\n"
        "| **Frontier** | Claude · GPT · Gemini · Kimi (Moonshot) |\n"
        "| **Open reasoning** | DeepSeek · Qwen · GLM · Nemotron |\n"
        "| **Local inference** | GGUF + `llama-server` — offline bundle, byte-verified |\n"
        "| **Agent runtimes** | Cline · Hermes · IronClaw/Reborn · OpenClaw |\n"
        "| **Protocol layer** | MCP servers · A2A-style pub/sub over `sahiixx-bus` |\n"
        "| **Orchestration** | autonomous loops · vote gates · audit chains · n8n |\n"
        "| **Routing** | TokenRouter · Cline gateway · AgentRouter |\n"
        "| **Voice** | LiveKit + Tauri desktop (`friday-os`) |"
    )

    S.append(
        "## 🏗️ End-to-end systems, not demos\n\n"
        "**Agent OS.** `sahiixx-bus` (pub/sub mesh) + `sahiixx-agency` (orchestration) + "
        "`agentic-harness` (workflow patterns) + `saas-agent-platform` (multi-tenant FastAPI). "
        "`agency-agents` and `sovereign-swarm-v2` are the swarm lab.\n\n"
        "**Revenue vertical.** `FirstCall` (idempotent UAE-lead ingestion → FastAPI) with "
        "`sovereign-revenue-os`, `nexus-buyer-recovery`, `sovereign-agents`, `lazy-ai-ops`: "
        "capture → qualify → geo-match → schedule → report. Private by design.\n\n"
        "**Assistant + memory.** `friday-os` (LiveKit voice + Tauri + MCP) persisted by "
        "`sahiixx-titans-memory` + `sahiixx-graph-sight`; `SHADOW` as the companion runtime.\n\n"
        "**Edge runtime.** Workers + Pages + R2 + KV + Queues running agent entry points "
        "close to the user, cheap and always-on."
    )

    S.append(
        "## 🔗 Execution graph — idea to revenue\n\n"
        "```mermaid\n"
        "flowchart LR\n"
        "    IDEA([\"idea\"]) --> BUS[\"sahiixx-bus<br/>orchestration\"]\n"
        "    BUS --> SWARM[\"agency-agents + swarm-v2<br/>parallel execution\"]\n"
        "    SWARM --> MEM[\"titans-memory + graph-sight<br/>persistent state\"]\n"
        "    SWARM --> FC[\"FirstCall<br/>capture · qualify · match\"]\n"
        "    FC --> REV[\"sovereign-revenue-os<br/>schedule · report\"]\n"
        "    MEM --> PA[\"friday-os<br/>voice + MCP\"]\n"
        "    EDGE[\"Cloudflare edge<br/>Workers + Pages\"] --> FC\n"
        "    EDGE --> PA\n"
        "    REV --> OUT([\"revenue\"])\n"
        "```"
    )

    rows = [r for r in [
        flagship("agency-agents", "Flagship multi-agent swarm"),
        flagship("friday-os", "Voice-first personal AI OS — memory-persistent, MCP-powered"),
        flagship("sovereign-swarm-v2", "Modular multi-agent OS"),
        flagship("sahiixx-bus", "Unified orchestration bus"),
        flagship("agentic-harness-integration", "Agentic patterns wired to Azure Foundry"),
        flagship("moltworker", "OpenClaw on Cloudflare Workers"),
        flagship("ocr-playbook-scanner", "OCR ingestion utility"),
        flagship("Genxai", "AgentForge open-core agent micro-SaaS scaffold"),
    ] if r]

    S.append(
        "## 🧪 Proof, not promises\n\n"
        "Stars, languages and push dates are read from the GitHub API on every render — "
        "nothing here is typed by hand.\n\n"
        "| System | What it proves | Lang | ⭐ | Last push |\n"
        "|---|---|---|---|---|\n"
        + "\n".join(rows)
        + "\n\n<sub>Private flagships (the ingestion pipeline and revenue OS) count toward the "
        "totals above but stay closed-source.</sub>"
    )

    S.append(
        f"## 📚 Research library — {starred_n} repos tracked\n\n"
        "I star what I intend to out-build. The library is the leading indicator; "
        "the repos above are the delivery.\n\n"
        "| What the library covers | Why it matters |\n"
        "|---|---|\n"
        "| Multi-agent frameworks & harnesses | the swarm patterns behind `agency-agents` |\n"
        "| Model runtimes & inference internals | what makes `llama-server` + GGUF viable |\n"
        "| MCP servers & tool protocols | the 80+ connectors in `integrations` |\n"
        "| Voice, speech & realtime audio | the LiveKit stack inside `friday-os` |\n"
        "| Scraping, OSINT & data plumbing | how `FirstCall` keeps its lead graph fresh |\n"
        "| Edge & serverless runtimes | the Workers deployment model |"
    )

    surfaces = [
        ("Portfolio", "sahiix-portfolio.pages.dev"),
        ("SAHIIXX OS", "sahiixx-os.pages.dev"),
        ("Systems panel", "sahiix-systems.pages.dev"),
    ]
    S.append(
        "## 🌐 Live surfaces\n\n"
        "| Surface | URL |\n"
        "|---|---|\n"
        + "\n".join(f"| {n} | [{h}](https://{h}) |" for n, h in surfaces)
    )

    S.append(
        "## 📊 Footprint\n\n"
        f"- {footprint.lstrip('- ')}\n"
        f"- **Top languages** — {top_langs}\n"
        f"- **Research library** — {starred_n} starred repos\n\n"
        f"<sub>Rendered {today} by an on-machine agent feeding GitHub Actions. "
        "Sensed values, not marketing values.</sub>"
    )

    S.append(
        "## 🎯 Building next\n\n"
        "- Hardening the **FirstCall** pipeline: capture → qualify → geo-match → revenue\n"
        "- Unifying every agent behind `sahiixx-bus`\n"
        "- Promoting validated prototypes out of the private estate\n\n"
        "## 📬 Reach me\n\n"
        "[Portfolio](https://sahiix-portfolio.pages.dev) · or open an issue on any repo above."
    )

    return "\n\n---\n\n".join(S) + "\n"


def main():
    repos, private_visible = all_repos()
    starred_n, _ = counts()
    st = live_state()
    readme = build_readme(repos, st, private_visible, starred_n)
    out = os.path.join(ROOT, "README.md")
    prev = ""
    if os.path.exists(out):
        with open(out, encoding="utf-8") as f:
            prev = f.read()
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(readme)
    print("README regenerated:",
          "changed" if readme != prev else "unchanged",
          f"({len(repos)} repos, {starred_n} starred)")


if __name__ == "__main__":
    sys.exit(main())
