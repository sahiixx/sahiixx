# Sahiixx

<div align="center">

## UAE-first agentic revenue OS for Dubai real estate

**I build AI systems that convert real estate leads into closings — lead intake, qualification, viewing orchestration, broker copilots, and investor reporting.**

🌍 Dubai, UAE · 🤖 Agentic AI · 🏢 Real Estate · 🎙️ Voice AI

[<img src="https://img.shields.io/badge/GitHub-sahiixx-181717?logo=github&style=flat-square">](https://github.com/sahiixx)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)]()
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)]()
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)]()

</div>

---

## 🎯 Now (Next 6–12 Months)

Shipping **SAHIIXX OS** as the operating system for Dubai real estate revenue teams.

Current milestones:
1. **Lead-to-qualification pipeline** — WhatsApp/Telegram/website intake → AI qualification → CRM-ready records
2. **Viewing orchestration** — GEO-optimized property matching → automated scheduling → broker handoff
3. **Broker copilot** — Voice-first assistant for follow-ups, objections, and investor reporting
4. **Pilot deployment** — 60-day pilots with 1–2 Dubai brokerages

---

## 🚀 Flagship System: SAHIIXX OS

**Target user:** Dubai real estate brokerages, developers, and investor offices.

**Workflow:** Lead enters via any channel → AI qualifies intent and budget → system matches properties by location/preference → viewing scheduled automatically → broker gets a pre-briefed lead → investor report generated.

**Outcome:** Less lead leakage, faster viewings, higher broker productivity, and clearer investor reporting.

**Status:** Alpha — core agents running, pilot conversations active.

**Start here:**
- [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) — multi-agent runtime
- [`sahiix-os`](https://github.com/sahiixx/sahiix-os) — product surface / CRM UI
- [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) + [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — message bus + orchestrator

<!-- Add live demo when ready: [Watch walkthrough](YOUR_LOOM_LINK) · [Request demo](YOUR_FORM_LINK) -->

---

## 🏗️ How Everything Connects

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           SAHIIXX OS Architecture                            │
└─────────────────────────────────────────────────────────────────────────────┘

   UI / Voice Layer                    Agent Layer                     Infra Layer
   ─────────────────                   ───────────                     ───────────
   ┌──────────────┐                   ┌──────────────┐              ┌──────────────┐
   │  sahiix-os   │◄─────────────────►│sahiixx-agency│─────────────►│ sahiixx-bus  │
   │  (React UI)  │                   │(OPA router)  │              │(pub/sub)     │
   └──────────────┘                   └──────────────┘              └──────┬───────┘
          ▲                                    ▲                           │
          │                                    │                           ▼
   ┌──────────────┐                   ┌──────────────┐              ┌──────────────┐
   │  friday-os   │                   │sovereign-    │              │sahiix-agi    │
   │(voice-first  │                   │swarm-v2      │              │(coordination │
   │ assistant)   │                   │(multi-agent  │              │ layer)       │
   └──────────────┘                   │ runtime)     │              └──────────────┘
                                      └──────┬───────┘                     │
                                             │                              ▼
                                             ▼                       ┌──────────────┐
                                      ┌──────────────┐              │sahiixx-titans│
                                      │sahiixx-      │              │memory        │
                                      │geoflow-agent │              │sahiixx-graph-│
                                      │(GEO match)   │              │sight         │
                                      └──────────────┘              └──────────────┘
```

**One concrete workflow:**

```
WhatsApp lead
    │
    ▼
sahiixx-agi — intent + budget extraction
    │
    ▼
sahiixx-geoflow-agent — property matching by location + preferences
    │
    ▼
sovereign-swarm-v2 — viewing scheduling + broker notification
    │
    ▼
sahiix-os — broker sees pre-qualified lead + recommended properties
    │
    ▼
sahiixx-graph-sight — reporting + trust graph for investor follow-up
```

---

## 🏢 Problem + Market

Dubai real estate moves fast, but most brokerages still run on manual follow-up:

- **Lead leakage:** Inquiries come in across WhatsApp, Instagram, portals, and websites — many never get logged or followed up.
- **Slow qualification:** Brokers spend 30–60 minutes per lead before knowing if it’s serious.
- **Viewing friction:** Matching properties, coordinating schedules, and rescheduling eats broker bandwidth.
- **Weak reporting:** Investors and developers lack real-time visibility into pipeline and performance.

**How SAHIIXX OS attacks each:**
- Unified intake + AI logging across all channels
- Automated qualification scoring and routing
- GEO + preference matching with auto-scheduling
- Live dashboards and investor-ready reports

**Market context:**
- AED 919 billion Dubai real estate market (2025)
- Federal mandate: 50% agentic AI in UAE government within 2 years
- Dubai private sector 100% agentic AI initiative announced May 2026

---

## 📈 Traction / Proof Points

- 🧪 **200+ repos** in the sahiixx ecosystem under active development
- 🏗️ **Flagship systems** in alpha: `sovereign-swarm-v2`, `sahiix-os`, `friday-os`
- 🎯 **Vertical focus:** Dubai real estate revenue infrastructure
- 🤝 **Pilot conversations** with brokerages and investor offices in Dubai

*Real pilot metrics will be added here as 60-day pilots close.*

---

## 🤝 What I’m Looking For

- **1–2 Dubai brokerages** for a 60-day SAHIIXX OS pilot
- **1 infrastructure engineer** with multi-agent / FastAPI / Redis experience
- **1 sales / GTM lead** who knows Dubai real estate
- **Technical collaborators** on voice AI, trust graphs, and vertical AI OS

**If you’re building in Dubai real estate or agentic AI, [let’s talk](#).**

<!-- Add booking link: [Book a 20-min call](YOUR_CALENDLY_LINK) -->

---

## 🛡️ Operational Guarantees

Building for production brokerage workflows means taking these seriously:

- **Observability:** Every agent run is traced through `sahiixx-bus` with structured logs
- **Failure modes:** Agents degrade gracefully; high-stakes decisions route to human brokers
- **Data governance:** Tenant and lead data isolated by brokerage; no cross-tenant leakage
- **Security:** Branch protection, Dependabot alerts, and dependency updates enabled across active repos
- **Compliance:** Designed around UAE data-residency and real-estate advertising requirements

---

## 💻 Tech Stack

![Python](https://img.shields.io/badge/python-%233776AB.svg?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![TypeScript](https://img.shields.io/badge/typescript-%23007ACC.svg?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![NodeJS](https://img.shields.io/badge/node.js-6DA55F?style=for-the-badge&logo=node.js&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

---

## 📊 GitHub Stats

<div align="center">

![](https://github-readme-stats.vercel.app/api?username=sahiixx&theme=dark&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=sahiixx&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=sahiixx&theme=dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

</div>

---

## 🗺️ Full Ecosystem

<details>
<summary>Expand to see the complete repo map</summary>

### Core Infrastructure
| Project | Role |
|---|---|
| [sahiixx-bus](https://github.com/sahiixx/sahiixx-bus) | Central message bus — pub/sub backbone for all agents |
| [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) | OPA orchestrator — auto-discovers & routes across repos |
| [sovereign-swarm-v2](https://github.com/sahiixx/sovereign-swarm-v2) | Multi-agent OS — Dubai RE runtime, n8n, Telegram bot |
| [sahiix-agi](https://github.com/sahiixx/sahiix-agi) | AGI coordination layer — FastAPI + Redis + Qdrant |

### Intelligence Modules
| Project | Role |
|---|---|
| [sahiixx-titans-memory](https://github.com/sahiixx/sahiixx-titans-memory) | Surprise-weighted persistent memory |
| [sahiixx-graph-sight](https://github.com/sahiixx/sahiixx-graph-sight) | Neo4j trust graph + AST code context |
| [sahiixx-geoflow-agent](https://github.com/sahiixx/sahiixx-geoflow-agent) | GEO optimization for Dubai listings |
| [sahiixx-clearwing](https://github.com/sahiixx/sahiixx-clearwing) | Autonomous pentesting swarm |

### Interfaces
| Project | Role |
|---|---|
| [friday-os](https://github.com/sahiixx/friday-os) | Voice-first personal AI OS |
| [saas-agent-platform](https://github.com/sahiixx/saas-agent-platform) | Multi-tenant agent SaaS |
| [sahiix-os](https://github.com/sahiixx/sahiix-os) | Real estate automation workspace UI |
| [moltworker](https://github.com/sahiixx/moltworker) | OpenClaw runtime on Cloudflare Workers |

</details>

---

## 🚀 Quick Start for Devs

```bash
# Clone the core stack
git clone https://github.com/sahiixx/sovereign-swarm-v2.git
git clone https://github.com/sahiixx/sahiixx-bus.git
git clone https://github.com/sahiixx/sahiix-os.git

# See the multi-agent runtime
 cd sovereign-swarm-v2 && cat README.md
```

*For non-technical visitors: [request a demo](#) or [book a call](#).*
