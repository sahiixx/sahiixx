<div align="center">

# SAHIIXX

### AI researcher · systems architect · founder-builder

I design the operating layer for AI-native products: model routing, agent runtimes, tool-use systems, memory, approval gates, and production verification.

![focus](https://img.shields.io/badge/focus-AI%20research%20%26%20systems-111111?style=for-the-badge)
![stack](https://img.shields.io/badge/stack-Azure%20%7C%20Cloudflare%20%7C%20OpenAI-5A67D8?style=for-the-badge)
![agents](https://img.shields.io/badge/agents-MCP%20%2B%20tool%20use%20%2B%20voice-00C2A8?style=for-the-badge)
![status](https://img.shields.io/badge/status-building%20%26%20shipping-brightgreen?style=for-the-badge)

</div>

---

## Operating thesis

I build systems where LLMs become dependable software components, not isolated chat interfaces.

My work sits at the intersection of:

- model evaluation and routing
- agent orchestration and bounded action loops
- persistent memory and retrieval architectures
- human-in-the-loop approval systems
- developer tooling and production-grade verification
- product surfaces that turn AI into usable workflows

The goal is not AI hype. The goal is reliable execution under uncertainty.

---

## Current technical stack

| Layer | Stack | Notes |
|---|---|---|
| Models | Azure AI Foundry, OpenAI, Anthropic, Google models, local open-weight inference | Model-agnostic orchestration and capability-based routing |
| Runtime | Agent loops, tool invocation, retries, state management, memory | Built for bounded execution and safe automation |
| Interfaces | Voice, browser, desktop, operator dashboards | Human-centered AI surfaces with structured input and approval gates |
| Protocols | MCP, A2A, event buses, pub/sub, service bridges | Connecting tools, services, and agents into a coherent system |
| Infra | Cloudflare Workers, Pages, R2, KV, Queues, Neon, edge deployments | Fast iteration with deployable product surfaces |
| Product tech | React, Hono, tRPC, Drizzle, LiveKit, Tauri | Modern stack for AI-native products |

---

## Research and systems focus

### Agentic systems
- routing by capability rather than provider identity
- tool allowlists and permissioned execution paths
- task decomposition, retries, and state continuity
- memory architectures for durable context and retrieval
- orchestration patterns for real-world operational work

### Trust and production readiness
- contract-first interfaces and schema validation
- evaluation across traditional, generative, and foundation-model lanes
- verification before deployment, not after the fact
- human approval for writes, financial decisions, and operational actions
- evidence-based system claims over narrative-heavy AI positioning

### Founder-builder lens
The most valuable AI systems are not the largest models. They are the ones that convert model intelligence into reliable operating leverage:

- reduced manual toil
- clearer decision support
- safe automation with review paths
- product interfaces people can trust
- measurable business workflows instead of toy demos

---

## Core ecosystem

### Agent orchestration
- [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — dispatch, task orchestration, and operator workflows
- [`agentic-harness`](https://github.com/sahiixx/agentic-harness) — reusable agent patterns and verification gates
- [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) — event-driven orchestration backbone
- [`agency-agents`](https://github.com/sahiixx/agency-agents) — multi-agent experiments and swarm patterns
- [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) — governance-focused swarm runtime

### Intelligence and memory
- [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory) — memory systems and persistent context design
- [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) — graph and semantic context exploration

### Product surfaces
- [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os) — operator command center and AI interface layer
- [`friday-os`](https://github.com/sahiixx/friday-os) — voice-first assistant and personal AI OS
- [SAHIIX OS](https://sahiixx-os.pages.dev) — live public product surface
- [Portfolio](https://sahiix-portfolio.pages.dev) — systems and product narrative

### Verification and hardening
- [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e) — release verification across model capability lanes
- [`sahiixx-production-hardening`](https://github.com/sahiixx/sahiixx-production-hardening) — action, event, and routing contract hardening
- [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing) — evidence-first validation and security-minded verification

### Domain workflow
- NEXUS — real-estate operations pipeline integrating intake, ranking, outreach, and approval workflows

---

## Capability map

| Layer | Capability | Representative projects |
|---|---|---|
| Model layer | Deterministic rules, generative models, embeddings, structured output, vision | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e), [`agentic-harness`](https://github.com/sahiixx/agentic-harness) |
| Runtime layer | Routing, bounded workflows, retries, evaluation, memory, approval gating | [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency), [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) |
| Protocol layer | Event envelopes, pub/sub, MCP, A2A, edge gateways | [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus), [`moltworker`](https://github.com/sahiixx/moltworker) |
| Intelligence layer | Persistent memory, semantic routing, retrieval, graph context | [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory), [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) |
| Product layer | Voice, desktop, web operator surfaces and workflow products | [`friday-os`](https://github.com/sahiixx/friday-os), [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os), NEXUS |
| Delivery layer | Contract-first verification, CI gates, edge deployments, evidence-based security | [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e), [`sahiixx-production-hardening`](https://github.com/sahiixx/sahiixx-production-hardening) |

---

## Engineering principles

- Contract-first: validate shape, identity, and service boundaries before trusting runtime behavior
- Model-agnostic: route based on capability and constraints rather than vendor preference
- Deterministic before autonomous: prefer rules and measurable systems before adding complex loops
- Bounded by default: enforce timeouts, retry budgets, tool restrictions, and approvals
- Human-centered execution: keep product actions reviewable and accountable
- Evidence over hype: label live, shipped, local, in-dev, and conceptual work transparently

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
| [sahiixx-os](https://github.com/sahiixx/sahiixx-os) | Full-stack AI command center built with React, Hono, tRPC, Drizzle, Neon | Public surface |
| [agentic-harness](https://github.com/sahiixx/agentic-harness) | Reusable agent workflows and evaluation patterns | Shipped |
| [sahiixx-e2e](https://github.com/sahiixx/sahiixx-e2e) | Contract-driven verification across tool, model, and workflow tiers | Shipped |
| [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) | Task orchestration, dispatch, and operator tooling | Shipped/local |
| [sahiixx-bus](https://github.com/sahiixx/sahiixx-bus) | Event bus architecture across services and agent boundaries | Shipped/local |
| [friday-os](https://github.com/sahiixx/friday-os) | Voice-first assistant and memory-backed personal AI operating layer | Shipped |
| [agency-agents](https://github.com/sahiixx/agency-agents) | Multi-agent orchestration and governance experiments | Active experiment |
| [moltworker](https://github.com/sahiixx/moltworker) | Lightweight gateway and workflow patterns in Cloudflare runtime | Shipped experiment |

---

## Bottom line

I work at the intersection of AI research and product engineering: building usable systems that make model intelligence operationally reliable, observable, and economically valuable.

---

## Reach me

[Portfolio](https://sahiix-portfolio.pages.dev) · [GitHub](https://github.com/sahiixx) · open an issue on any repo or reach out through the portfolio

<sub>Top active languages: Python · TypeScript · JavaScript · HTML · Go · Rust · Kotlin · Generated 2026-10-22 by the profile workflow.</sub>
