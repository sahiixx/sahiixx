# Sahiixx

<div align="center">

# AI Systems Architect

### **UAE-first agentic revenue OS for Dubai real estate**

**Converting real estate leads into closings with autonomous AI — intake, qualification, viewing orchestration, broker copilots, and investor reporting.**

> **🌐 Portfolio**: [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev/) | **📊 GitHub**: [@sahiixx](https://github.com/sahiixx) | **🚀 200+ Repos** | **33+ Agents** | **100% Python**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-sahiix--estate-22c55e?style=for-the-badge&logo=cloudflare)](https://counting-sail-fri-totals.trycloudflare.com/)
[![Agency](https://img.shields.io/badge/OPA-Orchestrator-7B61FF?style=for-the-badge&logo=github)](https://github.com/sahiixx/sahiixx-agency)
[![Multi-Agent](https://img.shields.io/badge/Sovereign%20Swarm-v2.0-00D4FF?style=for-the-badge&logo=github)](https://github.com/sahiixx/sovereign-swarm-v2)
[![Voice AI](https://img.shields.io/badge/Friday%20OS-Voice%20First-FF6B9D?style=for-the-badge&logo=github)](https://github.com/sahiixx/friday-os)

</div>

---

## 🎯 Building SAHIIXX OS

A **vertical AI operating system** for Dubai real estate brokerages, developers, and investor offices. 

**The Mission:** Replace manual brokerage operations with autonomous AI — from lead intake to closing.

**Current Status:**
- 🧪 **200+ repos** under active development (47 original, 122+ curated forks)
- 🏗️ **Flagship systems in alpha:** `sovereign-swarm-v2`, `sahiix-os`, `friday-os`
- 🌐 **Dubai-focused** vertical for AED 919B real estate market
- 🤝 **Pilot conversations active** with brokerages & investor offices
- ✅ **Production-hardened:** PM2, health checks, branch protection, Dependabot

---

## 🚀 The Stack

### **Agent Infrastructure**
| System | Role | Language |
|--------|------|----------|
| [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) | Multi-agent runtime (100/100 test coverage) | Python |
| [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) | OPA orchestrator (170+ repos) | Python + FastAPI |
| [`sahiix-agi`](https://github.com/sahiixx/sahiix-agi) | Coordination & signal layer | Python |
| [`agency-agents`](https://github.com/sahiixx/agency-agents) | 33+ specialized agents | Python |

### **Intelligence Layer**
| System | Purpose |
|--------|---------|
| [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory) | Persistent agent memory & recall |
| [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) | Trust graph & relationship mapping |
| [`sahiixx-geoflow-agent`](https://github.com/sahiixx/sahiixx-geoflow-agent) | GEO-optimized property matching |
| [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing) | Security & compliance swarm |

### **Interfaces & Frontends**
| System | Purpose | Stack |
|--------|---------|-------|
| [`sahiix-os`](https://github.com/sahiixx/sahiix-os) | Broker CRM workspace | React + TypeScript |
| [`friday-os`](https://github.com/sahiixx/friday-os) | Voice-first AI OS | Python + WebRTC |
| [`moltworker`](https://github.com/sahiixx/moltworker) | Telegram/Discord gateway | Cloudflare Workers |
| [`saas-agent-platform`](https://github.com/sahiixx/saas-agent-platform) | Multi-tenant SaaS | Next.js |

### **Infrastructure**
| System | Function |
|--------|----------|
| [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) | Central message bus (Redis) |
| [`bifrost-gateway`](https://github.com/sahiixx/bifrost-gateway) | API gateway & routing |
| [`ae-lead-scraper`](https://github.com/sahiixx/ae-lead-scraper) | UAE property data aggregation |

---

## 💼 Real Estate AI Engine

### **The Problem**
| Pain Point | Cost Today | SAHIIXX Fix |
|---|---|---|
| Lead leakage | Inquiries lost across WhatsApp, Instagram, portals | Unified intake + AI logging |
| Slow qualification | 30–60 min per lead before broker knows if it's real | Automated intent/budget/timeline scoring |
| Viewing friction | Matching, scheduling, rescheduling drains broker time | GEO + preference matching with auto-scheduling |
| Weak reporting | Investors lack real-time pipeline visibility | Live dashboards + investor reports |

### **The Market (Q1 2026 Dubai)**
- **AED 176.7B** in sales, ~48K transactions (+23.4% YoY)
- **AED 1,949/sqft** average; off-plan ~70%
- **120K+ new units** in 2026
- **Golden Visa** (AED 2M+) driving foreign investment
- **DLD blockchain** cuts title transfer from 60→7 days
- **Dubai PropTech Hub** targeting AED 4.5B market growth

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
                                      │ (multi-agent    │            ┌──��──────────────┐
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

## 📈 Traction & Achievements

- 🧪 **200+ repos** across AI agents, infra, and real estate stack
- 🏗️ **Flagship systems in alpha:** sovereign-swarm-v2, sahiix-os, friday-os
- 🌐 **Dubai-focused** vertical stack designed for AED 919B market
- 🤝 **Pilot conversations** with 3+ Dubai brokerages & investor offices
- ✅ **Production hardening:** PM2, health checks, branch protection, Dependabot
- 🚀 **Live demo deployed** via Cloudflare tunnel (end-to-end E2E pipeline)
- 📊 **Goldmine Protocol:** RFM-scored CRM with 4-tier contact system
- 🔐 **Licensed RE Agent** at APEX Estates (operational credentials)
- 🐍 **100% Python codebase** — FastAPI, LangChain, async-first architecture

---

## 💻 Tech Stack

![Python](https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Redis](https://img.shields.io/badge/redis-DC382D?style=for-the-badge&logo=redis&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/typescript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
![React](https://img.shields.io/badge/react-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white)
![Cloudflare](https://img.shields.io/badge/Cloudflare-F38020?style=for-the-badge&logo=cloudflare&logoColor=white)
![Docker](https://img.shields.io/badge/docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=for-the-badge&logo=neo4j&logoColor=white)

---

## 🤝 What I'm Building Toward

- **AI Revenue OS for real estate:** autonomous lead-to-close pipeline
- **Multi-agent coordination:** sovereign-swarm + OPA orchestrator
- **Dubai-first expansion:** 1-2 pilot brokerages for 60-day deployment
- **Infrastructure scale:** 200+ repos → production agency
- **Voice-first interfaces:** friday-os as primary broker interaction layer

**Looking for:**
- **1–2 Dubai brokerages** for SAHIIXX OS pilots (60-day, AED 50k–80k)
- **Infrastructure engineer** (FastAPI/Redis/multi-agent systems)
- **Sales/GTM lead** (Dubai PropTech network)
- **Pre-seed/angel funding** for team & pilots

---

## 🛡️ Operational Guarantees

- **Observability:** every agent run traced through `sahiixx-bus`
- **Failure modes:** graceful degradation; high-stakes decisions route to humans
- **Data governance:** tenant & lead data isolated by brokerage
- **Security:** branch protection & Dependabot enabled across active repos
- **Compliance:** built for UAE data-residency & real-estate advertising requirements
- **Monitoring:** PM2 health checks, Sentry error tracking, structured logging
- **Language:** 100% Python core — FastAPI, asyncio, LangChain orchestration

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
# Clone core systems
git clone https://github.com/sahiixx/sovereign-swarm-v2.git
git clone https://github.com/sahiixx/sahiixx-bus.git
git clone https://github.com/sahiixx/sahiixx-agency.git
git clone https://github.com/sahiixx/sahiix-os.git

# View live demo (Cloudflare tunnel)
# https://counting-sail-fri-totals.trycloudflare.com/
```

---

## 🗺️ Full Ecosystem (200+ Repos)

<details>
<summary>Core Orchestration (5 repos)</summary>

- [`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) — OPA router & orchestrator
- [`sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2) — Multi-agent runtime
- [`sahiix-agi`](https://github.com/sahiixx/sahiix-agi) — Coordination layer
- [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus) — Message bus (Redis)
- [`agency-agents`](https://github.com/sahiixx/agency-agents) — 33+ specialized agents

</details>

<details>
<summary>Intelligence & Memory (4 repos)</summary>

- [`sahiixx-titans-memory`](https://github.com/sahiixx/sahiixx-titans-memory) — Persistent memory
- [`sahiixx-graph-sight`](https://github.com/sahiixx/sahiixx-graph-sight) — Trust graphs
- [`sahiixx-geoflow-agent`](https://github.com/sahiixx/sahiixx-geoflow-agent) — GEO matching
- [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing) — Security swarm

</details>

<details>
<summary>Real Estate Specific (6 repos)</summary>

- [`sahiix-os`](https://github.com/sahiixx/sahiix-os) — Broker CRM workspace
- [`friday-os`](https://github.com/sahiixx/friday-os) — Voice AI copilot
- [`ae-lead-scraper`](https://github.com/sahiixx/ae-lead-scraper) — Dubai property scraper
- [`Coral-BlackboxAI-Agent`](https://github.com/sahiixx/Coral-BlackboxAI-Agent) — Coral protocol bridge
- [`Fixfiz`](https://github.com/sahiixx/Fixfiz) — NOWHERE.AI platform
- [`v0-nowire-os-blueprint`](https://github.com/sahiixx/v0-nowire-os-blueprint) — Nowire OS

</details>

<details>
<summary>Integrations & Gateways (4 repos)</summary>

- [`moltworker`](https://github.com/sahiixx/moltworker) — Telegram/Discord gateway
- [`bifrost-gateway`](https://github.com/sahiixx/bifrost-gateway) — API gateway
- [`saas-agent-platform`](https://github.com/sahiixx/saas-agent-platform) — Multi-tenant SaaS
- [`SHADOW`](https://github.com/sahiixx/SHADOW) — Coral protocol swarm

</details>

<details>
<summary>Plus 122+ Curated Forks</summary>

Forks of: LangChain, AutoGen, CrewAI, n8n, OpenManus, Llama, Qwen, LLaVA, browser-use, goose, rowboat, openclaw, hermes-agent, and more for research & reference.

</details>

---

## 📞 Get in Touch

- **Portfolio:** [sahiix-portfolio.pages.dev](https://sahiix-portfolio.pages.dev/)
- **GitHub:** [@sahiixx](https://github.com/sahiixx)
- **Live Demo:** [Cloudflare Tunnel](https://counting-sail-fri-totals.trycloudflare.com/)
- **Repo ID:** 1220420024

---

## 📄 License

MIT — Open for collaboration on real estate AI & multi-agent systems.
