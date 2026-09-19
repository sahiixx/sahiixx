# SAHIIXX

**AI Systems Architect — Dubai, UAE**

I build autonomous agent systems: one operating system of agents, vertical AI products, and the edge infrastructure that runs them.

![focus](https://img.shields.io/badge/focus-agentic%20AI-111111?style=flat-square)
![edge](https://img.shields.io/badge/edge-Cloudflare-A2663A?style=flat-square)
![repos](https://img.shields.io/badge/repos-240-3E6B4F?style=flat-square)
![status](https://img.shields.io/badge/status-building-brightgreen?style=flat-square)

---

## What I'm building

**An agent operating system.** The runtime layer is `sahiixx-agency` (orchestration) + `sahiixx-bus` (pub/sub mesh) + `agentic-harness` (workflow patterns) + `saas-agent-platform` (multi-tenant FastAPI). `agency-agents` and `sovereign-swarm-v2` are the swarm lab.

**A Dubai real-estate revenue vertical.** `FirstCall` (idempotent UAE-leads ingestion → FastAPI), `sovereign-revenue-os`, `nexus-buyer-recovery`, `sovereign-agents` and `lazy-ai-ops` run the pipeline: capture → qualify → geo-match → schedule → report. Mostly private — this is the commercial side.

**A personal assistant with voice + memory.** `friday-os` (LiveKit voice + Tauri + MCP) backed by `sahiixx-titans-memory` and `sahiixx-graph-sight` for persistence and knowledge.

**An edge runtime on Cloudflare.** 9 Workers (`moltbot-sandbox*`, `lead-hunter*`, `opencla`, `f`) and 4 Pages apps — cheap, always-on entry points for agents.

---

## How it connects

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

## Live surfaces

| Surface | URL | Status |
|---|---|---|
| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) | live |
| SAHIIXX OS | [sahiixx-os.pages.dev](https://sahiixx-os.pages.dev) | live |
| Systems panel | [sahiix-systems.pages.dev](https://sahiix-systems.pages.dev) | live |

Edge: 9 Workers · 4 Pages · 3 R2 · 1 KV · 1 Queue.

---

## By the numbers

- **240 repos** — 94 originals + 146 forks · 218 public / 22 private · 31 stars
- **Top languages** — Python · TypeScript · JavaScript · HTML · Go · Rust · Kotlin
- **Open source** — 332 merged PRs, mostly kept green by automation

<sub>Counts from a read-only scrape of this account, 2026-09-19.</sub>

---

## Currently

- Hardening the **FirstCall** lead pipeline (capture → qualify → geo-match → revenue)
- Unifying the agent mesh around `sahiixx-bus`
- Consolidating the repo estate (archiving placeholders, merging duplicate sandboxes)

## Reach me

[Portfolio](https://sahiix-portfolio.pages.dev) · or open an issue on any repo.
