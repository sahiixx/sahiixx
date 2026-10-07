#!/usr/bin/env python3
"""Render the profile README from GitHub inventory and source-linked claims."""

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
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "sahiixx-readme-bot"}
    if TOKEN:
        headers["Authorization"] = f"Bearer {TOKEN}"
    req = urllib.request.Request("https://api.github.com" + path, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as response:
        return json.load(response)


def all_repos():
    try:
        repos, page = [], 1
        while True:
            batch = api(f"/user/repos?per_page=100&page={page}&affiliation=owner")
            if not batch:
                break
            repos.extend(r for r in batch if r["owner"]["login"].lower() == OWNER)
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


def profile():
    try:
        return api(f"/users/{OWNER}")
    except Exception:
        return {}


def live_state():
    """Read the explicitly published machine snapshot when available."""
    path = os.path.join(ROOT, "data", "live_state.json")
    try:
        with open(path, encoding="utf-8") as file:
            value = json.load(file)
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError):
        return {}


def link(name):
    return f"[{name}](https://github.com/{OWNER}/{name})"


def build_readme(repos, state=None):
    public = [r for r in repos if not r.get("private")]
    active = [r for r in public if not r.get("archived")]
    archived = [r for r in public if r.get("archived")]
    originals = [r for r in active if not r.get("fork")]
    forks = [r for r in active if r.get("fork")]
    by_name = {r.get("name", "").lower(): r for r in active}
    langs = Counter(r.get("language") for r in active if r.get("language"))
    top_langs = " · ".join(name for name, _ in langs.most_common(7))
    public_total = profile().get("public_repos", len(public))
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    state = state or {}
    firstcall = state.get("firstcall", {})
    edge = state.get("edge", {})
    github_30d = state.get("github_30d", {})

    def proof(name, evidence, state):
        repo = by_name.get(name.lower())
        if not repo:
            return ""
        return (
            f"| {link(repo['name'])} | {evidence} | {state} | "
            f"{repo.get('language') or '-'} · {repo.get('stargazers_count', 0)} stars · "
            f"{(repo.get('pushed_at') or '')[:10] or '-'} |"
        )

    rows = "\n".join(filter(None, [
        proof("sahiixx-os", "Full-stack command center with React, Hono, tRPC, Drizzle and Neon", "Public surface"),
        proof("agentic-harness", "Reusable agent workflow patterns, verification and Azure Foundry routing", "Shipped"),
        proof("sahiixx-e2e", "Contract-first Playwright release gate with traditional, generative and foundation-model lanes", "Shipped"),
        proof("sahiixx-agency", "CLI/API/MCP-oriented repository and task dispatch", "Shipped/local"),
        proof("sahiixx-bus", "Unified orchestration bus for cross-service events and agent boundaries", "Shipped/local"),
        proof("friday-os", "Voice-first, memory-persistent personal AI OS with LiveKit, Tauri and MCP", "Shipped"),
        proof("sahiixx-production-hardening", "Canonical event, model-routing, bus, revenue and action-gate contracts", "Shipped"),
        proof("sahiixx-clearwing", "Security verification focused on evidence rather than report volume", "Active"),
        proof("agency-agents", "Multi-agent orchestration and swarm experiments", "Active experiment"),
        proof("sovereign-swarm-v2", "Modular multi-agent runtime and governance direction", "In development"),
        proof("moltworker", "OpenClaw gateway patterns on Cloudflare Workers", "Shipped experiment"),
    ]))

    sections = [
        f'''<div align="center">

# SAHIIXX

### AI systems architect · model-agnostic agent runtimes · Dubai, UAE

*I build the layer where models meet real software: routing, bounded tools, persistent state, human gates, live interfaces and domain workflows.*

![focus](https://img.shields.io/badge/focus-AI%20systems-111111?style=for-the-badge)
![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=for-the-badge&logo=cloudflare&logoColor=white)
![repos](https://img.shields.io/badge/public%20repos-{public_total}-3E6B4F?style=for-the-badge)
![status](https://img.shields.io/badge/status-building%20%26%20shipping-brightgreen?style=for-the-badge)

</div>''',
        f'''## ⚡ Current operating picture

> Snapshot: **{today}**. Repository counts are GitHub inventory data; product states are labeled from project evidence and public surfaces, not inferred from model capability.

| Signal | Evidence-backed state |
|---|---|
| 🧭 Repository estate | {public_total} public repositories · {len(originals)} unarchived originals · {len(forks)} unarchived forks · {len(archived)} archived |
| 🧠 Orchestration | `sahiixx-agency`, `agentic-harness`, `sahiixx-bus` and the swarm experiments |
| 🖥️ Public OS surface | [SAHIIX OS](https://sahiixx-os.pages.dev) · React/Hono/tRPC/Drizzle/Neon/Cloudflare |
| 🎙️ Voice + tools | [Jarvis](https://sahiixx-os.pages.dev/jarvis) route plus [`friday-os`](https://github.com/sahiixx/friday-os) |
| 🏢 Domain workflow | NEXUS real-estate lead flow · local/pilot boundary documented in the portfolio repo |
| 🧪 Model verification | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) covers traditional, generative and foundation-model capability lanes |
| 🧪 Verification rule | `live` means a reachable or documented running surface; `shipped` means code exists; `in-dev` and `concept` stay labeled |''',
        f'''## 📡 Operational pulse

> Machine-reported snapshot: **{state.get("updated_at", today)}**. These figures are telemetry from the published local state file, not product-performance guarantees.

| Signal | Snapshot |
|---|---|
| Gateway | `{state.get("gateway_state", "not reported")}` · Telegram `{state.get("telegram", "not reported")}` · `{state.get("watchdog_services", "-")}` watchdog services |
| Firstcall pipeline | `{firstcall.get("leads", "-")}` leads · `{firstcall.get("deals", "-")}` deals · `{firstcall.get("outreach", "-")}` outreach events · `{firstcall.get("orphans", "-")}` orphans |
| Edge estate | `{edge.get("workers", "-")}` Workers · `{edge.get("pages", "-")}` Pages · `{edge.get("r2", "-")}` R2 · `{edge.get("kv", "-")}` KV · `{edge.get("queues", "-")}` queues |
| GitHub activity, 30 days | `{github_30d.get("pushes", "-")}` pushes · `{github_30d.get("prs", "-")}` PRs · `{github_30d.get("created", "-")}` repositories created |''',
        '''## 🧠 AI frontier map — grounded, not hype

The current AI stack is moving from single-turn generation toward reasoning modes, tool use, memory, multimodality, agents and embodied interfaces. My work is the systems layer around those capabilities.

| Area | Current evidence | How I frame it |
|---|---|---|
| Frontier models | [OpenAI research](https://openai.com/research/), [Anthropic Claude 4](https://www.anthropic.com/news/claude-4), [Google DeepMind models](https://deepmind.google/models/) | Providers publish increasingly capable reasoning, coding, tool and multimodal systems; the application still needs routing, permissions and verification. |
| Open and local models | [Qwen3](https://qwenlm.github.io/blog/qwen3/) and local GGUF/Ollama workflows | Open weights, controllable thinking budgets and local inference are useful for cost, privacy and fallback paths. |
| AGI | [OpenAI Charter](https://openai.com/charter/) defines AGI as highly autonomous systems that outperform humans at most economically valuable work | AGI is a research target and contested definition, not a capability claim made by this profile or these repositories. |
| ASI | [Frontier safety research](https://deepmind.google/frontier-safety/) | ASI is a future-risk and governance horizon; no deployed SAHIIX system is represented as superintelligent. |

**Position:** build useful, auditable agent systems now; keep AGI and ASI claims falsifiable, sourced and separate from shipped product status.''',
        '''## 🏗️ End-to-end systems

**Orchestration.** [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) provides a dispatcher surface, [`agentic-harness`](https://github.com/sahiixx/agentic-harness) documents bounded agent patterns and Azure Foundry routing, and [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) supplies the pub/sub seam.

**Assistant + memory.** [`friday-os`](https://github.com/sahiixx/friday-os) combines voice, desktop and MCP; [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory) and [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) explore persistent and graph-backed state.

**Operator shell.** [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os) is the public command center; Jarvis adds streaming voice with read, mutate and confirmation-gated tool tiers.

**Domain vertical.** NEXUS connects Dubai real-estate intake, ranking, WhatsApp and OS import paths. The portfolio marks local workstation services and pilot boundaries explicitly; planned specialist lead agents are not described as live until they exist.''',
        '''## 🧭 Capability map

| Layer | Capability | Representative projects |
|---|---|---|
| Model layer | Traditional rules, generative models, embeddings, structured output and vision | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e), [`agentic-harness`](https://github.com/sahiixx/agentic-harness) |
| Runtime layer | Routing, bounded workflows, retries, evaluation, memory and human approval | [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency), [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) |
| Protocol layer | Event envelopes, pub/sub, MCP, A2A and gateway bridges | [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus), [`moltworker`](https://github.com/sahiixx/moltworker) |
| Intelligence layer | Persistent memory, graph context, retrieval and semantic routing | [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory), [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) |
| Product layer | Voice, desktop, web command center and domain workflows | [`friday-os`](https://github.com/sahiixx/friday-os), [`sahiixx-os`](https://github.com/sahiixx/sahiix-os), NEXUS |
| Delivery layer | Contract-first E2E, CI gates, edge deployment and evidence-based security | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e), [`sahiixx-production-hardening`](https://github.com/sahiixx/sahiixx-production-hardening), [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing) |''',
        '''## 🧪 Model-agnostic verification

[`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) is the release-verification boundary for the model layer:

| Lane | What is verified | Default mode |
|---|---|---|
| Traditional | deterministic classification and lead scoring | network-free |
| Generative | chat, SSE streaming and tool calls | mocked, with opt-in live canaries |
| Foundation | structured output, embeddings and vision | mocked, with capability-specific live canaries |

The harness uses runtime contracts, bounded timeouts, replayable fixtures, redacted diagnostics and environment-controlled provider/model IDs. A missing live profile skips only that capability; a configured endpoint fails on transport, HTTP or schema errors.''',
        '''## 🧱 Engineering principles

- **Contract-first:** validate events, identities, schemas and service boundaries at runtime.
- **Model-agnostic:** route by capability and constraints; keep provider names in configuration.
- **Deterministic before autonomous:** use rules and fixed fixtures when they solve the task; add agent loops only when measured value justifies them.
- **Bounded by default:** enforce deadlines, retries, tool allowlists, token/cost budgets and replayable idempotency keys.
- **Human-gated actions:** writes, financial actions and production changes require explicit approval paths.
- **Evidence over hype:** distinguish live, shipped, local, in-development and concept work in public documentation.''',
        '''## 🗺️ Start here

| If you want to… | Start with |
|---|---|
| See the public product surface | [SAHIIX OS](https://sahiixx-os.pages.dev) · [portfolio](https://sahiix-portfolio.pages.dev) |
| Understand the architecture | [`CONNECTED_ECOSYSTEM.md`](https://github.com/sahiixx/sahiixx/blob/main/CONNECTED_ECOSYSTEM.md) · [`FOUNDER_SERVICE_ARCHITECTURE.md`](https://github.com/sahiixx/sahiixx/blob/main/FOUNDER_SERVICE_ARCHITECTURE.md) |
| Inspect the full repository map | [`FULL_PORTFOLIO.md`](https://github.com/sahiixx/sahiixx/blob/main/FULL_PORTFOLIO.md) · [`REPO_MAP.md`](https://github.com/sahiixx/sahiixx/blob/main/REPO_MAP.md) |
| Read the evidence-backed case studies | [`CASE_STUDIES.md`](https://github.com/sahiixx/sahiixx/blob/main/CASE_STUDIES.md) |
| See verification in code | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) · [`agentic-harness`](https://github.com/sahiixx/agentic-harness) |
| Collaborate or propose an integration | Open an issue in the relevant repository or reach out through the portfolio |''',
        '''## 🔗 Execution graph

```mermaid
flowchart LR
  MODEL["Frontier / open models"] --> ROUTE["Routing + bounded tools"]
  ROUTE --> BUS["sahiixx-bus<br/>pub/sub"]
  BUS --> OS["SAHIIX OS<br/>command center"]
  BUS --> SWARM["agency-agents<br/>experiments"]
  OS --> VOICE["Jarvis + friday-os<br/>voice / MCP"]
  OS --> NEXUS["NEXUS<br/>domain workflow"]
  MEMORY["Titans memory + graph-sight<br/>persistent state"] --> OS
  HUMAN["Human approval"] --> OS
```''',
        f'''## 🧪 Proof, not promises

| System | What the repository or public surface demonstrates | State | Current GitHub signal |
|---|---|---|---|
{rows}''',
        '''## 🌐 Public surfaces

| Surface | URL | State |
|---|---|---|
| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) | live |
| SAHIIX OS | [sahiixx-os.pages.dev](https://sahiixx-os.pages.dev) | live public surface |
| Systems panel | [sahiix-systems.pages.dev](https://sahiix-systems.pages.dev) | public dashboard |''',
         f'''## 🎯 Delivery status

### Completed

- [x] Contract-first E2E release gate with traditional, generative and foundation-model lanes.
- [x] Provider/model configuration kept environment-controlled and source-linked.
- [x] Public architecture map, engineering principles and case studies.
- [x] Core repository taxonomy that separates products, experiments and fork study libraries.

### Remaining release gates

- [ ] Configure reachable OPA and bus environments and pass `REQUIRE_LIVE=1` capture → qualify → match checks.
- [ ] Make lead events durable with an outbox, idempotency, retry/DLQ and trace propagation.
- [ ] Add tenant-isolation, consent, tool-scope and approval-state checks before production scheduling or offers.
- [ ] Run the repository hygiene script with administrative scope, then keep the fork library and archive candidates current.
- [ ] Publish live model canary artifacts once capability-specific provider variables are available.

<sub>Top active languages: {top_langs or 'not available'} · Generated {today} by the profile workflow.</sub>

## 📬 Reach me

[Portfolio](https://sahiix-portfolio.pages.dev) · [GitHub](https://github.com/sahiixx) · or open an issue on any repo.''',
    ]
    return "\n\n---\n\n".join(sections) + "\n"


def main():
    repos, private_visible = all_repos()
    rendered = build_readme(repos, live_state())
    output = os.path.join(ROOT, "README.md")
    previous = open(output, encoding="utf-8").read() if os.path.exists(output) else ""
    with open(output, "w", encoding="utf-8", newline="\n") as file:
        file.write(rendered)
    print("README regenerated:", "changed" if rendered != previous else "unchanged", f"({len(repos)} repos fetched, private_visible={private_visible})")


if __name__ == "__main__":
    sys.exit(main())
