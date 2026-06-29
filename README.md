# Sahiixx

<div align="center">

# SAHIIXX

### **UAE-first agentic revenue OS for Dubai real estate**

**Converting real estate leads into closings with autonomous AI — intake, qualification, viewing orchestration, broker copilots, and investor reporting.**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-sahiix--estate-22c55e?style=for-the-badge&logo=cloudflare)](https://austin-alternate-inkjet-oregon.trycloudflare.com/)
[![GitHub](https://img.shields.io/badge/GitHub-sahiixx-181717?style=for-the-badge&logo=github)](https://github.com/sahiixx)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)]()
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=twitter&logoColor=white)]()

</div>

---

## 🎯 Now

Building **SAHIIXX OS** — a vertical AI operating system for Dubai real estate brokerages, developers, and investor offices.

**Current focus:**
1. Unified lead intake across WhatsApp, Telegram, and web
2. AI qualification scoring (intent, budget, timeline)
3. GEO-optimized viewing orchestration
4. Voice-first broker copilot and investor reporting
5. 60-day pilots with Dubai brokerages

---

## 🚀 Flagship System

**SAHIIXX OS** replaces manual brokerage operations with one autonomous revenue layer.

| Stage | What happens | Component |
|---|---|---|
| **Lead intake** | Inquiry captured from any channel | `sahiix-agi` |
| **Qualification** | Intent, budget, timeline extracted and scored | `sahiix-agi` + `sahiixx-titans-memory` |
| **Matching** | GEO + preference property matching | `sahiixx-geoflow-agent` |
| **Scheduling** | Automated viewing orchestration | `sovereign-swarm-v2` |
| **Broker handoff** | Pre-briefed lead in CRM workspace | `sahiix-os` |
| **Reporting** | Investor-ready pipeline reports | `sahiixx-graph-sight` |

**Start here:**
- [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) — multi-agent runtime
- [`sahiix-os`](https://github.com/sahiixx/sahiix-os) — broker workspace UI
- [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) + [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — bus + orchestrator

**Live demo:** [austin-alternate-inkjet-oregon.trycloudflare.com](https://austin-alternate-inkjet-oregon.trycloudflare.com/)

---

## 🏢 Why This Matters Now

**Market timing:**
- Dubai PropTech raised **AED 1.2 billion** from 2020–2025 across 78 rounds
- **Q1 2026:** 42,800 Dubai transactions, values up **18% YoY**
- **Dubai PropTech Hub (2025):** targeting **AED 4.5B** market growth over 5 years
- **DLD REES platform** connects PropTech firms directly to official registry data
- **DLD blockchain registry** cuts title transfer from 60 days to ~7 days
- **Prop-AI** raised **$1.5M pre-seed** in June 2025 for AI real estate infrastructure
- Tokenized/fractional real estate now holds **AED 750M+** in assets

**The gap:** most brokerages still run on WhatsApp threads, spreadsheets, and manual follow-up while the market accelerates.

---

## ⚡ The Problem

| Pain point | Cost today | SAHIIXX OS fix |
|---|---|---|
| Lead leakage | Inquiries lost across WhatsApp, Instagram, portals | Unified intake + AI logging |
| Slow qualification | 30–60 min per lead before a broker knows if it's real | Automated intent/budget/timeline scoring |
| Viewing friction | Matching, scheduling, rescheduling drains broker time | GEO + preference matching with auto-scheduling |
| Weak reporting | Investors lack real-time pipeline visibility | Live dashboards + investor reports |

---

## 🛠️ Architecture

```
        UI / Voice                     Agent Layer                      Infra Layer
    ┌─────────────────┐            ┌─────────────────┐            ┌─────────────────┐
    │   sahiix-os     │◄──────────►│ sahiixx-agency  │───────────►│  sahiixx-bus    │
    │  (broker CRM)   │            │ (OPA router)    │            │ (message bus)   │
    └─────────────────┘            └─────────────────┘            └────────┬────────┘
    ┌─────────────────┐                      ▲                              │
    │   friday-os     │                      │                              ▼
    │ (voice copilot) │                      │                       ┌─────────────────┐
    └─────────────────┘                      │                       │   sahiix-agi    │
                                             │                       │(coordination)   │
                                             ▼                       └────────┬────────┘
                                      ┌─────────────────┐                      │
                                      │ sovereign-swarm │                      ▼
                                      │ (multi-agent    │            ┌─────────────────┐
                                      │  runtime)       │            │ sahiixx-titans  │
                                      └────────┬────────┘            │ memory          │
                                               │                     │ sahiixx-graph-  │
                                               ▼                     │ sight           │
                                      ┌─────────────────┐            └─────────────────┘
                                      │ sahiixx-        │
                                      │ geoflow-agent   │
                                      │ (GEO matching)  │
                                      └─────────────────┘
```

---

## 📈 Traction

- 🧪 **200+ repos** in the sahiixx ecosystem under active development
- 🏗️ **Flagship systems in alpha:** `sovereign-swarm-v2`, `sahiix-os`, `friday-os`
- 🌐 **Dubai-focused** vertical stack for AED 919B real estate market
- 🤝 **Pilot conversations active** with brokerages and investor offices
- ✅ **Production hardening:** PM2, health checks, branch protection, Dependabot enabled
- 🚀 **Live demo deployed** via Cloudflare tunnel

---

## 💻 Tech Stack

![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![JavaScript](https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/react-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![NodeJS](https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)

---

## 🤝 What I'm Looking For

- **1–2 Dubai brokerages** for a 60-day SAHIIXX OS pilot
- **1 infrastructure engineer** — FastAPI / Redis / multi-agent systems
- **1 sales / GTM lead** — Dubai real estate network
- **Pre-seed / angel funding** to accelerate pilots and team

<!-- Add booking link: [Book a 20-min call](YOUR_CALENDLY_LINK) -->

---

## 🛡️ Operational Guarantees

- **Observability:** every agent run traced through `sahiixx-bus`
- **Failure modes:** agents degrade gracefully; high-stakes decisions route to humans
- **Data governance:** tenant and lead data isolated by brokerage
- **Security:** branch protection and Dependabot enabled across active repos
- **Compliance:** designed around UAE data-residency and real-estate advertising requirements

---

## 📊 GitHub Stats

<div align="center">

![](https://github-readme-stats.vercel.app/api?username=sahiixx&theme=dark&hide_border=false&include_all_commits=true&count_private=true)<br/>
![](https://github-readme-streak-stats.herokuapp.com/?user=sahiixx&theme=dark&hide_border=false)<br/>
![](https://github-readme-stats.vercel.app/api/top-langs/?username=sahiixx&theme=dark&hide_border=false&include_all_commits=true&count_private=true&layout=compact)

</div>

---

## 🚀 Quick Start

```bash
git clone https://github.com/sahiixx/sovereign-swarm-v2.git
git clone https://github.com/sahiixx/sahiixx-bus.git
git clone https://github.com/sahiixx/sahiix-os.git
```

*For pilots or demos: [request access](#).*

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
