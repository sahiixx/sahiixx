<div align="center">

# SAHIIXX

### AI systems architect · agentic infrastructure · model-native workflows

I design the systems layer between models and real-world operations: routing, tool execution, memory, approval gates, live interfaces, and production-grade verification.

![focus](https://img.shields.io/badge/focus-AI%20systems-111111?style=for-the-badge)
![edge](https://img.shields.io/badge/stack-Azure%20%7C%20Cloudflare%20%7C%20OpenAI-5A67D8?style=for-the-badge)
![ai](https://img.shields.io/badge/AI-Agents%20%2B%20MCP%20%2B%20voice-00C2A8?style=for-the-badge)
![status](https://img.shields.io/badge/status-building%20%26%20shipping-brightgreen?style=for-the-badge)

</div>

---

## Current operating picture

> Snapshot: 2026-10-22. This profile stays grounded in public evidence, shipped code, and live interfaces rather than hype-driven claims.

| Signal | Evidence-backed state |
|---|---|
| 🧭 Repository estate | 224 public repositories · 52 unarchived originals · 148 unarchived forks · 24 archived |
| 🧠 Core architecture | `sahiixx-agency`, `agentic-harness`, `sahiixx-bus`, `friday-os`, `sahiixx-os` |
| 🌐 Public OS surface | [SAHIIX OS](https://sahiixx-os.pages.dev) · React + Hono + tRPC + Drizzle + Neon |
| 🎙️ AI interfaces | [Jarvis](https://sahiixx-os.pages.dev/jarvis) + voice, tools, and approval layers |
| 🏢 Production vertical | NEXUS real-estate workflow with intake, ranking, outreach, and humans-in-the-loop |
| 🧪 Verification | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) validates model and workflow behavior through contract-based checks |
| 🔒 Operating rule | `live` = reachable or documented public surface; `shipped` = code exists; `in-dev` stays labeled |

---

## What I build

I build AI systems that are usable, observable, and bounded by design.

- Model routing across providers and deployment types
- Agent orchestration with tool allowlists, retries, and approval gates
- Memory layers for persistent context, retrieval, and task continuity
- Voice, desktop, and web interfaces for AI-powered work
- Domain workflows that connect AI to real business operations
- Verification systems that prove behavior instead of just claiming it

This is not “chat with a model.” It is a systems layer for AI-native execution.

---

## Latest AI + infrastructure stack

| Layer | Current stack | Notes |
|---|---|---|
| Models | Azure AI Foundry, OpenAI, Anthropic, Google models, local open models | Model-agnostic routing with provider configuration and capability matching |
| Runtime | Agent loops, tools, orchestration, memory, task execution | Bounded workflows, retries, and structured execution |
| Interfaces | Voice, browser, desktop, operator dashboards | Human-centered AI surfaces with approvals and observability |
| Protocols | MCP, A2A, event buses, pub/sub, service bridges | Interoperability between tools, agents, and services |
| Data + infra | Neon, Cloudflare, R2, KV, Queues, Pages, Workers | Edge-first deployment and low-friction operator tooling |
| Product stack | React, Hono, tRPC, Drizzle, LiveKit, Tauri | Modern UI + runtime architecture for real products |

### AI focus areas

- Agentic orchestration and workflow design
- Tool-use safety and permission boundaries
- Long-running task execution with state persistence
- Retrieval + memory for grounded decision support
- Voice-first interfaces and operator copilots
- Verification, replay, and evidence-based deployment

---

## Core systems and repos

### Agent orchestration
- [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — dispatch, routing, and operational task orchestration
- [`agentic-harness`](https://github.com/sahiixx/agentic-harness) — reusable agent workflow patterns and verification gates
- [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) — event-driven orchestration backbone
- [`agency-agents`](https://github.com/sahiixx/agency-agents) — multi-agent experiments and swarm patterns
- [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) — governance-oriented swarm runtime

### Memory and intelligence
- [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory) — persistent memory and context systems
- [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) — graph and semantic context exploration

### Product surfaces and interfaces
- [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os) — public command center / operator layer
- [`friday-os`](https://github.com/sahiixx/friday-os) — voice-first assistant and AI desktop experience
- [SAHIIX OS](https://sahiixx-os.pages.dev) — live product surface
- [Portfolio](https://sahiix-portfolio.pages.dev) — portfolio and systems overview

### Verification and production hardening
- [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) — contract-driven verification for models and product behavior
- [`sahiixx-production-hardening`](https://github.com/sahiixx/sahiixx-production-hardening) — canonical contracts for events, routing, revenue flows, and action gates
- [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing) — evidence-first security and verification work

### Domain workflow
- NEXUS — real-estate lead flow and AI operational workflow across intake, ranking, outreach, and approval

---

## Capability map

| Layer | Capability | Representative projects |
|---|---|---|
| Model layer | Traditional rules, generative models, embeddings, structured output, vision | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e), [`agentic-harness`](https://github.com/sahiixx/agentic-harness) |
| Runtime layer | Routing, bounded workflows, retries, evaluation, memory, approval gating | [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency), [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) |
| Protocol layer | Event envelopes, pub/sub, MCP, A2A, gateway bridges | [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus), [`moltworker`](https://github.com/sahiixx/moltworker) |
| Intelligence layer | Persistent memory, graph context, retrieval, semantic routing | [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory), [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) |
| Product layer | Voice, desktop, web command center, domain workflows | [`friday-os`](https://github.com/sahiixx/friday-os), [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os), NEXUS |
| Delivery layer | Contract-first E2E, CI gates, edge deployment, security and evidence | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e), [`sahiixx-production-hardening`](https://github.com/sahiixx/sahiixx-production-hardening) |

---

## Engineering principles

- Contract-first design: validate events, identities, schemas, and service boundaries
- Model-agnostic routing: keep provider names in config and match by capability
- Deterministic before autonomous: rules and evaluations before complex loops
- Bounded by default: timeouts, retries, budgets, and approval checks
- Human-gated actions: acknowledgements for writes, finances, system changes, and operations
- Evidence over hype: separate live, shipped, local, in-dev, and concept work clearly

---

## Public surfaces

| Surface | URL | State |
|---|---|---|
| Portfolio | [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev) | live |
| SAHIIX OS | [sahiixx-os.pages.dev](https://sahiixx-os.pages.dev) | live public surface |
| Systems panel | [sahiix-systems.pages.dev](https://sahiix-systems.pages.dev) | public dashboard |

---

## Proof, not promises

| System | What it demonstrates | State |
|---|---|---|
| [sahiixx-os](https://github.com/sahiixx/sahiixx-os) | Full-stack command center with React, Hono, tRPC, Drizzle, Neon | Public surface |
| [agentic-harness](https://github.com/sahiixx/agentic-harness) | Agent workflow patterns and verification-first routing | Shipped |
| [sahiixx-e2e](https://github.com/sahiixx/sahiixx-e2e) | Contract-based release verification across traditional, generative, and foundation-model lanes | Shipped |
| [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) | CLI/API/MCP-oriented dispatch and task orchestration | Shipped/local |
| [sahiixx-bus](https://github.com/sahiixx/sahiixx-bus) | Unified orchestration bus across services and agent boundaries | Shipped/local |
| [friday-os](https://github.com/sahiixx/friday-os) | Voice-first, memory-persistent personal AI OS | Shipped |
| [agency-agents](https://github.com/sahiixx/agency-agents) | Multi-agent orchestration and swarm experiments | Active experiment |
| [moltworker](https://github.com/sahiixx/moltworker) | OpenClaw gateway patterns on Cloudflare Workers | Shipped experiment |

---

## AI stack in one sentence

I work at the intersection of frontier models, local inference, orchestration, memory, approval systems, and product-grade delivery — building AI that is useful, observable, and operationally honest.

---

## Reach me

[Portfolio](https://sahiix-portfolio.pages.dev) · [GitHub](https://github.com/sahiixx) · open an issue on any repo or reach out through the portfolio

<sub>Top active languages: Python · TypeScript · JavaScript · HTML · Go · Rust · Kotlin · Generated 2026-10-22 by the profile workflow.</sub>
