# SAHIIXX · AI Systems Architect

**Dubai, UAE · AIOS · Hireable**  
Building an autonomous **AI operating system** for agents, edge governance, and Dubai real-estate revenue ops.

```text
Profile  →  Stack map  →  Core products  →  Inventory truth
```

---

## North star

| Pillar | What it is | Flagship repo |
|--------|------------|---------------|
| **OPA** | One-Person Agency — dispatch, adapters, MessageBus | [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) |
| **Edge** | JWT, rate-limit, WATI, Termux governance | [`sahiix-proxy`](https://github.com/sahiixx/sahiix-proxy) |
| **Lead Machine** | Capture → Qualify → Match (Dubai RE) | Agency + [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) |
| **OS shell** | Command center UI | [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os) |
| **App Builder** | Private TanStack/Vite sandbox | [`agno`](https://github.com/sahiixx/agno) *(private)* |
| **Revenue vertical** | Sovereign / NEXUS revenue OS | `sovereign-revenue-os` *(private)* |

Canonical architecture: **[SAHIIX Stack v2.1](https://github.com/sahiixx/sahiix-os-docs/blob/master/SAHIIX_STACK_v2.1.md)**  
Living inventory: **[REPO_MAP.md](./REPO_MAP.md)**

---

## Stack (v2.1) — one diagram

```text
L7  EXPERIENCE     sahiixx-os · portfolio · systems-panel · agno · Jarvis/CLI
L6  VERTICALS      Sovereign Revenue OS · NEXUS · Lead Machine · friday-os · geoflow
L5  AGENT RUNTIME  sahiixx-agency (OPA) · bus · titans-memory · graph-sight
L4  HARNESS        agentic-harness · Azure Foundry model routing
L3  EDGE           sahiix-proxy (JWT · rate · WATI · Termux)
L2  INTEGRATION    n8n · Hermes/MCP · f-worker-ai · Ollama · adapters
L1  DATA           Neon · Redis · Qdrant · Titans · GraphSight
L0  INFRA          Cloudflare · Azure · Docker/GHCR · Vercel · Termux
```

### Runtime table

| Layer | Repo | Role | Status |
|-------|------|------|--------|
| L5 | [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) | OPA + Lead Machine specialists + `api.asgi` | Active |
| L3 | [sahiix-proxy](https://github.com/sahiixx/sahiix-proxy) | Edge governance | Active |
| L4 | [agentic-harness](https://github.com/sahiixx/agentic-harness) | Shared agent patterns | Active |
| L7 | [sahiixx-os](https://github.com/sahiixx/sahiixx-os) | OS shell | Active |
| L7 | [sahiix-portfolio](https://github.com/sahiixx/sahiix-portfolio) | Public face + pilots | Active |
| L7 | [systems-panel](https://github.com/sahiixx/systems-panel) | Module status UI | Active |
| QA | [sahiixx-e2e](https://github.com/sahiixx/sahiixx-e2e) | Playwright + Lead Machine contracts | Active |
| Docs | [sahiix-os-docs](https://github.com/sahiixx/sahiix-os-docs) | Stack architecture | Active |
| L7 | [agno](https://github.com/sahiixx/agno) | App Builder *(private)* | Active |
| L6 | sovereign-revenue-os | Revenue OS *(private)* | Active |

**Lead Machine:** Capture + Qualify + GeoMatch **live** (HTTP `/opa/lead/*` via `api.asgi`). Scheduling / Reporting next.

---

## How this GitHub is structured

| Bucket | Count (public) | Meaning |
|--------|----------------|---------|
| **Core SAHIIX** | ~25 | Own products — keep green |
| **Original experiments** | ~45 | Prototypes, one-offs, naming noise |
| **Forks (reference)** | ~145 | Upstream study clones — not products |
| **Total public** | **216** | GitHub profile total |
| **Private** | additional | `agno`, revenue OS, etc. |

**Rule:** if it’s not in the runtime table or [REPO_MAP.md](./REPO_MAP.md) “Core” section, treat it as **study or sandbox**, not production.

---

## Core product map (source of truth)

### Runtime & agents
- [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — OPA orchestrator  
- [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) — pub/sub bus  
- [`agentic-harness`](https://github.com/sahiixx/agentic-harness) · [`agentic-harness-integration`](https://github.com/sahiixx/agentic-harness-integration)  
- [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory) · [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight)  
- [`friday-os`](https://github.com/sahiixx/friday-os) · [`sahiix-agi`](https://github.com/sahiixx/sahiix-agi) · [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2)

### Edge, quality, surface
- [`sahiix-proxy`](https://github.com/sahiixx/sahiix-proxy) · [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) · [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing)  
- [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os) · [`sahiix-portfolio`](https://github.com/sahiixx/sahiix-portfolio) · [`systems-panel`](https://github.com/sahiixx/systems-panel) · [`sahiix-os-docs`](https://github.com/sahiixx/sahiix-os-docs)

### Verticals
- [`sahiixx-geoflow-agent`](https://github.com/sahiixx/sahiixx-geoflow-agent) · NEXUS / Sovereign *(private where applicable)*

---

## Tech

**Languages:** Python · TypeScript · Go · Rust · Java · Kotlin  
**Agents:** OPA adapters · ADK / OpenAI Agents *(forks for study)* · MCP  
**Web:** React · TanStack Start · Vite · Astro · Next  
**Cloud:** Azure Foundry · Cloudflare · Vercel · Docker · Termux edge

---

## Start here

| Goal | Go to |
|------|--------|
| Architecture | [SAHIIX Stack v2.1](https://github.com/sahiixx/sahiix-os-docs/blob/master/SAHIIX_STACK_v2.1.md) |
| Run agents | [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) (`api.asgi`) |
| Edge | [sahiix-proxy](https://github.com/sahiixx/sahiix-proxy) |
| E2E / contracts | [sahiixx-e2e](https://github.com/sahiixx/sahiixx-e2e) |
| Full repo map | [REPO_MAP.md](./REPO_MAP.md) |
| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) |

---

## Hygiene (ongoing)

1. **Core** stays in the runtime table and gets CI + docs.  
2. **Forks** stay forks — don’t market them as SAHIIX products.  
3. **Noise** (single-letter names, empty experiments) → archive or private when convenient.  
4. **Private** production systems stay private; profile only names them.

---

**[@sahiixx](https://github.com/sahiixx)** · AI Systems Architect · SAHIIX Stack v2.1
