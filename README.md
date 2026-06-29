# Sahiixx

<div align="center">

## UAE-first agentic revenue OS for Dubai real estate

**I build autonomous AI systems that convert real estate leads into closings — intake, qualification, viewing orchestration, broker copilots, and investor reporting.**

🌍 Dubai, UAE · 🤖 Agentic AI · 🏢 Real Estate · 🎙️ Voice AI

[<img src="https://img.shields.io/badge/GitHub-sahiixx-181717?logo=github&style=flat-square">](https://github.com/sahiixx)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-%230077B5.svg?logo=linkedin&logoColor=white)]()
[![Twitter](https://img.shields.io/badge/Twitter-%231DA1F2.svg?logo=Twitter&logoColor=white)]()
[![YouTube](https://img.shields.io/badge/YouTube-%23FF0000.svg?logo=YouTube&logoColor=white)]()

</div>

---

## 🚀 Start Here

| | |
|---|---|
| **Flagship system** | [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) — multi-agent runtime for Dubai real estate |
| **Product surface** | [`sahiix-os`](https://github.com/sahiixx/sahiix-os) — broker workspace and CRM UI |
| **Architecture** | [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) + [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — message bus + orchestrator |

<!-- Replace with real links when ready:
**Live demo:** [Watch 2-min walkthrough](YOUR_LOOM) · [Request pilot access](YOUR_FORM)
-->

---

## 🎯 Now

Shipping **SAHIIXX OS** in the next 6–12 months as Dubai brokerages adopt agentic AI.

Current milestones:
1. **Unified lead intake** — WhatsApp / Telegram / web → one qualification pipeline
2. **AI qualification** — intent, budget, timeline scoring before a broker touches it
3. **GEO-optimized viewing orchestration** — match, schedule, and resend automatically
4. **Voice-first broker copilot** — follow-ups, objections, and investor reporting
5. **60-day pilots** — 1–2 Dubai brokerages

---

## 🏢 The Market Opportunity

**Why Dubai, why now:**
- UAE AI agents market: **$97.2M in 2025 → projected $2.72B by 2033** (Grand View Research)
- UAE AI agents CAGR: **49.4%** (2025–2030)
- Global AI in real estate: **$303B in 2025 → $989B by 2029** (34.4% CAGR)
- Global PropTech funding hit **$16.7B in 2025** (+67.9% YoY)
- Agentic AI is moving from pilots to **mainstream adoption in 2026–2027**
- Dubai Land Department’s **Mo’asher index** and open data are becoming the backbone for AI pricing and matching tools
- Major portals (Property Finder, Bayut) are rolling out **AI agent copilots** for brokers in 2026
- **AED 919 billion** Dubai real estate market (2025)

**The wedge:** brokerages still run on manual follow-up while the market and regulators are accelerating AI adoption.

---

## ⚡ The Problem

Dubai real estate moves fast, but operations lag:

| Pain point | Cost | How SAHIIXX OS fixes it |
|---|---|---|
| **Lead leakage** | Inquiries from WhatsApp, Instagram, portals, web never get logged or followed up | Unified intake + AI logging across all channels |
| **Slow qualification** | 30–60 minutes per lead before knowing if it’s serious | Automated intent, budget, and timeline scoring |
| **Viewing friction** | Matching, scheduling, and rescheduling eats broker bandwidth | GEO + preference matching with auto-scheduling |
| **Weak reporting** | Investors lack real-time pipeline visibility | Live dashboards and investor-ready reports |

---

## ⚙️ How It Works

```
Lead Intake          Qualification         Viewing Ops           Broker Copilot        Reporting
     │                      │                      │                      │                    │
     ▼                      ▼                      ▼                      ▼                    ▼
 WhatsApp /            sahiixx-agi           sahiixx-              friday-os            sahiixx-graph-sight
 Website /             (FastAPI + Redis      geoflow-agent         (voice-first         (trust graph +
 Telegram              + Qdrant)             (GEO matching)        personal AI OS)      AST context)
     │                      │                      │                      │                    │
     └──────────────────────┴──────────────────────┴──────────────────────┘────────────────────┘
                                          │
                                          ▼
                               sahiixx-bus (central message backbone)
                                          │
                                          ▼
                               sahiixx-agency (OPA orchestrator)
```

**Concrete workflow:** WhatsApp lead → `sahiixx-agi` extracts intent/budget → `sahiixx-geoflow-agent` matches properties → `sovereign-swarm-v2` schedules viewing → broker sees pre-briefed lead in `sahiix-os` → `sahiixx-graph-sight` generates investor report.

---

## 📈 Traction

- 🧪 **200+ repos** in active development across the sahiixx ecosystem
- 🏗️ **Flagship systems in alpha:** `sovereign-swarm-v2`, `sahiix-os`, `friday-os`
- 🎯 **Vertical focus:** Dubai real estate revenue infrastructure
- 🤝 **Pilot conversations active** with brokerages and investor offices
- 📊 **Market timing aligned** with UAE agentic AI growth and DLD open-data initiatives

*Real pilot metrics will be added here as 60-day pilots close.*

---

## 🤝 What I’m Looking For

- **1–2 Dubai brokerages** for a 60-day SAHIIXX OS pilot
- **1 infrastructure engineer** — FastAPI / Redis / multi-agent systems
- **1 sales / GTM lead** — Dubai real estate network
- **Technical collaborators** — voice AI, trust graphs, vertical AI OS
- **Pre-seed / angel funding** to accelerate pilots and team

<!-- Add contact link: [Book a 20-min call](YOUR_CALENDLY_LINK) -->

---

## 🛡️ Built for Production Brokerage Workflows

- **Observability:** every agent run traced through `sahiixx-bus`
- **Failure modes:** agents degrade gracefully; high-stakes decisions route to humans
- **Data governance:** tenant and lead data isolated by brokerage
- **Security:** branch protection and Dependabot enabled across active repos
- **Compliance:** designed around UAE data-residency and real-estate advertising requirements

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
<summary>Expand to see all repos</summary>

### Core Infrastructure
- [sahiixx-bus](https://github.com/sahiixx/sahiixx-bus) — central message bus
- [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) — OPA orchestrator
- [sovereign-swarm-v2](https://github.com/sahiixx/sovereign-swarm-v2) — multi-agent runtime
- [sahiix-agi](https://github.com/sahiixx/sahiix-agi) — coordination layer

### Intelligence
- [sahiixx-titans-memory](https://github.com/sahiixx/sahiixx-titans-memory) — persistent memory
- [sahiixx-graph-sight](https://github.com/sahiixx/sahiixx-graph-sight) — trust graph
- [sahiixx-geoflow-agent](https://github.com/sahiixx/sahiixx-geoflow-agent) — GEO matching
- [sahiixx-clearwing](https://github.com/sahiixx/sahiixx-clearwing) — security swarm

### Interfaces
- [friday-os](https://github.com/sahiixx/friday-os) — voice-first AI OS
- [sahiix-os](https://github.com/sahiixx/sahiix-os) — real estate workspace UI
- [saas-agent-platform](https://github.com/sahiixx/saas-agent-platform) — multi-tenant SaaS
- [moltworker](https://github.com/sahiixx/moltworker) — OpenClaw on Workers

</details>

---

## 🚀 Quick Start

```bash
git clone https://github.com/sahiixx/sovereign-swarm-v2.git
git clone https://github.com/sahiixx/sahiixx-bus.git
git clone https://github.com/sahiixx/sahiix-os.git
```

*For pilots or demos: [request access](#).*
