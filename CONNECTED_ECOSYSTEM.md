# 🌐 SAHIIXX — Connected Ecosystem Architecture

> **167 repositories. One mind. Infinite agents.**

This document maps every repository in the `sahiixx` GitHub ecosystem, connecting the dots between original projects, forked enhancements, integration bridges, and deployment surfaces.

---

## 🧠 Executive Summary

The sahiixx ecosystem is a **layered AI infrastructure stack** built around a single principle: *autonomous agents should orchestrate everything*. At the center is **The Agency** (`agency-agents`) — a 152-agent Claude-powered swarm. Every other repository either feeds into it, deploys from it, or extends its capabilities across specific domains, protocols, and surfaces.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         🧠 THE AGENCY (agency-agents)                        │
│              152 Agents · Claude Sonnet 4.6 · A2A · MCP · JARVIS v3         │
├─────────────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌──────────────────┐  │
│  │   VOICE AI  │  │   MEMORY    │  │   SECURITY  │  │   REAL ESTATE    │  │
│  │ JARVIS v3   │  │ Titans+LTM  │  │ Audit Swarm │  │ Dubai Pipeline   │  │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └────────┬─────────┘  │
│         │                │                │                  │            │
│  ┌──────┴────────────────┴────────────────┴──────────────────┴──────────┐  │
│  │                    MULTI-AGENT ORCHESTRATION LAYER                     │  │
│  │    friday-os · sovereign-swarm-v2 · goose-aios · deepagents SDK       │  │
│  └──────┬────────────────┬────────────────┬──────────────────┬──────────┘  │
│         │                │                │                  │            │
│  ┌──────┴──────┐  ┌─────┴──────┐  ┌──────┴──────┐  ┌────────┴─────────┐ │
│  │  PROTOCOLS  │  │  FRONTEND  │  │  AUTOMATION │  │  INFRASTRUCTURE  │ │
│  │ A2A · MCP   │  │ Next.js    │  │ n8n Bus     │  │ Cloudflare       │ │
│  │ Coral · SSE │  │ Tauri      │  │ Workflows   │  │ Workers · Vercel │ │
│  └─────────────┘  └────────────┘  └─────────────┘  └──────────────────┘ │
│         │                │                │                  │            │
│  ┌──────┴────────────────┴────────────────┴──────────────────┴──────────┐  │
│  │                     KNOWLEDGE & INTELLIGENCE LAYER                     │  │
│  │  system-prompts · prompt patterns · docs · trust graph · lead scraper   │  │
│  └────────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 🏛️ Architecture Layers

### Layer 1: The Core Brain (`agency-agents`)

**Repository:** [`sahiixx/agency-agents`](https://github.com/sahiixx/agency-agents)  
**Language:** Python  
**Status:** CI Green ✅ | 19/19 Tests Passing  
**Role:** Central orchestrator and reasoning engine

The Agency is the **central nervous system** of the entire ecosystem. It hosts:

- **152 specialized agents** across 14 domains (PM, Backend, Frontend, QA, Security, DevOps, Core, etc.)
- **JARVIS v3** voice assistant stack (Twilio + local TTS)
- **Titans-inspired surprise-weighted long-term memory**
- **Google A2A v0.3 protocol** for cross-agent communication
- **19 LangChain-compatible MCP tools**
- **Multi-provider abstraction** (Claude, Ollama, OpenAI, Google ADK, AutoGen)
- **9 integration bridges** to external repos (documented in `integrations/`)

**Key Files:**
- `agency.py` — Unified orchestrator & CLI entry point
- `swarm_orchestrator.py` — Sequential delegation pipeline
- `sovereign_agency_swarm.py` — Full-stack + AI pipeline
- `real_estate_swarm.py` — Dubai real estate pipeline
- `security_audit_swarm.py` — Security audit pipeline
- `a2a_protocol.py` — Google A2A protocol implementation
- `mcp_tools.py` — 19 MCP tools
- `integrations/` — Bridges to 9 external repos

---

### Layer 2: AI Operating Systems (Runtime Surfaces)

These repos provide **different runtime environments** for The Agency's agents — voice-first, local-only, or modular swarm OS.

#### 2A. FRIDAY OS (`friday-os`)
**Repository:** [`sahiixx/friday-os`](https://github.com/sahiixx/friday-os)  
**Language:** Python + TypeScript (Tauri desktop)  
**Role:** Voice-first, memory-persistent, MCP-powered personal AI OS

FRIDAY OS consolidates patterns from **OpenJarvis, SUPER AGI, AIOS-Local, agency-agents, and claude-code-best-practice** into one shippable surface:

```
CLI + LiveKit voice + Tauri desktop + Claude Code plugin
```

**Stack:**
- Python backend (`friday/`)
- Tauri desktop app (`desktop/`)
- LiveKit voice integration
- Reads persona from `~/.openjarvis/{SOUL,USER,MEMORY}.md`
- Inherits The Agency's orchestration patterns

**Connection to Agency:**
- FRIDAY OS is The Agency's **voice-first consumer interface**
- Uses the same memory system (Titans-inspired)
- Can trigger Agency missions via CLI or voice

#### 2B. Sovereign Swarm v2 (`sovereign-swarm-v2`)
**Repository:** [`sahiixx/sovereign-swarm-v2`](https://github.com/sahiixx/sovereign-swarm-v2)  
**Language:** Python  
**Role:** Modular Multi-Agent OS — 45 modules across 6 functional domains

```
sovereign_swarm/
├── agents/       # Agent profiles, spawning, HITL, scheduling
├── infra/        # Event bus, memory, LLM client, platform detection
├── intelligence/ # Orchestration, routing, reputation, healing, evolution
├── protocols/    # MCP server, A2A cards, Hermes messenger, OpenClaw gateway
├── safety/       # Safety council, audit, budget, observe, alerts
├── cli.py        # CLI entrypoint
├── repl.py       # Interactive REPL with 15+ commands
└── tests.py      # 33 tests across 6 suites
```

**Connection to Agency:**
- Sovereign Swarm is The Agency's **production-grade runtime**
- Provides the safety council, cost management, and healing layers
- Bridges to OpenClaw, Hermes, and Coral Protocol

#### 2C. Goose AIOS (`goose-aios`)
**Repository:** [`sahiixx/goose-aios`](https://github.com/sahiixx/goose-aios)  
**Language:** Python  
**Role:** Local-first AI assistant powered by Ollama

Runs entirely offline — no cloud, no API keys, no data leaving the machine.

**Connection to Agency:**
- Goose AIOS is The Agency's **privacy-first local deployment**
- Uses Ollama models instead of Claude API
- Can run the same agent definitions locally

---

### Layer 3: Industry Applications (Vertical Domains)

These repos apply The Agency's intelligence to specific industries.

#### 3A. SAHIIX OS (`sahiix-os`)
**Repository:** [`sahiixx/sahiix-os`](https://github.com/sahiixx/sahiix-os)  
**Language:** JavaScript  
**Role:** AI-powered real estate automation workspace for Dubai

**Connection to Agency:**
- Uses The Agency's real estate swarm (`real_estate_swarm.py`)
- Integrates with Dubai property data pipelines

#### 3B. NOWHERE.AI (`Fixfiz` / `Fixfizx`)
**Repository:** [`sahiixx/Fixfizx`](https://github.com/sahiixx/Fixfizx)  
**Language:** Python (FastAPI) + React  
**Role:** Production-grade digital services platform for Dubai/UAE

**Stack:**
- FastAPI backend
- React frontend
- MongoDB persistence
- Stripe AED payments
- Twilio SMS
- SendGrid email
- Multi-tenancy + JWT auth + RBAC

**Connection to Agency:**
- NOWHERE.AI exposes REST APIs for the same 5 agent functions The Agency runs
- The Agency's `biz-sales`, `biz-mkt`, `biz-content`, `biz-analytics`, `biz-ops` agents call NOWHERE.AI via MCP tools:
  - `qualify_lead_nowhere`
  - `dubai_market_analysis`
  - `create_campaign_nowhere`
- **Integration doc:** `agency-agents/integrations/nowhere-ai-platform-bridge.md`

#### 3C. UAE Lead Scraper (`ae-lead-scraper---`)
**Repository:** [`sahiixx/ae-lead-scraper---`](https://github.com/sahiixx/ae-lead-scraper---)  
**Language:** Python  
**Role:** UAE property lead scraper

**Connection to Agency:**
- The Agency's `scrape_ae_leads` tool connects to this scraper
- Feeds leads into NOWHERE.AI platform

---

### Layer 4: Communication & Gateway Bridges

These repos connect The Agency to end-users across messaging platforms and protocols.

#### 4A. Moltworker (`moltworker`)
**Repository:** [`sahiixx/moltworker`](https://github.com/sahiixx/moltworker)  
**Language:** JavaScript (Cloudflare Workers)  
**Role:** OpenClaw gateway on Cloudflare — Telegram/Discord/Slack/Web

**Architecture:**
```
The Agency Swarm (LangGraph / deepagents)
     │
     ▼ trigger_moltbot_mission() MCP tool
     │
     ▼ HTTP POST to Moltbot Admin API
┌──────────────────────────────────────────┐
│  Cloudflare Worker (moltworker/src/)     │
│  - Proxies HTTP/WebSocket traffic        │
│  - Admin UI at /_admin/                  │
│  - API endpoints at /api/*                 │
└──────────────┬───────────────────────────┘
     │
     ▼ Telegram / Discord / Slack / Web
```

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/moltworker-gateway-bridge.md`
- The Agency's `trigger_moltbot_mission` MCP tool fires missions to Moltworker
- One mission → every channel simultaneously

#### 4B. HermesClaw (`hermesclaw`)
**Repository:** [`sahiixx/hermesclaw`](https://github.com/sahiixx/hermesclaw)  
**Role:** WeChat dual-gateway proxy for Hermes + OpenClaw

**Connection:**
- Bridges The Agency to WeChat (China's dominant messaging platform)
- Works alongside Moltworker for Asian market coverage

#### 4C. Coral Protocol Bridge (`Coral-BlackboxAI-Agent`)
**Repository:** [`sahiixx/Coral-BlackboxAI-Agent`](https://github.com/sahiixx/Coral-BlackboxAI-Agent)  
**Language:** Python  
**Role:** Cross-framework agent communication via Coral Protocol SSE

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/coral-protocol-bridge.md`
- Enables The Agency's agents to talk to LangChain, LangGraph, AutoGen, CrewAI agents
- Uses SSE-based async messaging with thread-based routing

#### 4D. SHADOW Swarm (`SHADOW`)
**Repository:** [`sahiixx/SHADOW`](https://github.com/sahiixx/SHADOW)  
**Role:** Coral Protocol swarm — Voice→Code→Review→Log pipeline

**Architecture:**
```
Voice Input → Whisper Agent → Shadow Agent → Reviewer Agent → Notion Agent → Slack Agent
```

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/shadow-swarm-bridge.md`
- The Agency delegates voice-to-code or research-to-documentation pipelines to SHADOW
- Specialist subswarm for voice-driven workflows

---

### Layer 5: Frontend & Deployment Surfaces

These repos provide the UI and deployment infrastructure for The Agency's outputs.

#### 5A. Next.js AI Chatbot (`nextjs-ai-chatbot` / `nextjs-ai-chatbotg`)
**Repository:** [`sahiixx/nextjs-ai-chatbot`](https://github.com/sahiixx/nextjs-ai-chatbot)  
**Language:** TypeScript (Next.js)  
**Role:** Vercel AI SDK-powered chat interface wired to The Agency

**Architecture:**
```
User types in chat UI (Next.js)
     │
     ▼ POST /api/chat
     │
     ▼ Vercel AI SDK (useChat hook → streaming response)
     │
     ▼ Agency route handler (app/api/chat/route.ts)
     │
     ▼ HTTP SSE → agency live_server.py
     │
The Agency Swarm (deepagents / LangGraph)
     └── pm → backend → qa → security → core (Claude Reasoning Gate)
     │
     ▼ streamed tokens back to browser
```

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/nextjs-chatbot-deployment.md`
- Every chat message routes through the full Agency swarm
- Real-time streaming with tool calls and multi-preset support

#### 5B. Nowire OS Frontend (`v0-nowire-os-blueprint`)
**Repository:** [`sahiixx/v0-nowire-os-blueprint`](https://github.com/sahiixx/v0-nowire-os-blueprint)  
**Language:** TypeScript (Next.js + shadcn/ui)  
**Role:** Next.js CRM/OS interface auto-generated by v0.app

**Stack:**
- Next.js App Router
- shadcn/ui + Tailwind CSS
- Auto-syncs with v0.app on every deploy
- Deployed to Vercel

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/nowire-os-frontend.md`
- Surfaces real estate dashboards, Dubai B2B pipelines, AI mission results
- Auto-deploys every time v0.app generates a new component

#### 5C. Cloudflare Deployment Templates
**Repositories:**
- `react-router-starter-template` — React Router v7 + Cloudflare Pages
- `containers-template` — Cloudflare Containers
- `examples-hello-world` — Hello World Workers
- `examples-with-fresh` — Fresh (Deno) on Cloudflare

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/cloudflare-deployment-templates.md`
- The Agency's Cloudflare Deployment Specialist agent knows all these templates
- Can scaffold, configure, and deploy any project to Workers/Pages/D1/R2/Containers

---

### Layer 6: Automation & Workflow Bus

#### 6A. n8n Ecosystem
**Repositories:**
- `n8n` — Core workflow automation platform
- `n8n-free-templates` — 200+ ready-to-import n8n workflows
- `n8n-workflows-1` — 2,053 professionally organized workflows
- `ultimate-n8n-ai-workflows` — 3,400+ AI workflows
- `n8n-docs` — Documentation

**Connection to Agency:**
- **Integration doc:** `agency-agents/integrations/n8n-agency-bus.md`
- n8n is The Agency's **event and trigger bus**
- Any n8n workflow can launch a full multi-agent mission via webhook:
  ```
  n8n Workflow Trigger
        │
        ▼ POST /webhook/agency
  ┌─────────────────────────────────────────────┐
  │  Agency Webhook Receiver (n8n_trigger tool) │
  │  workflow_tag → preset routing:             │
  │    "email"   → --preset full              │
  │    "slack"   → --preset moltbot           │
  │    "crm"     → --preset dubai             │
  │    "report"  → --preset research          │
  │    "security"→ --preset security          │
  └──────────────────────┬──────────────────────┘
                         │
                         ▼ The Agency Swarm
  ```
- Configured via `N8N_BASE_URL`, `N8N_API_KEY`, `N8N_WEBHOOK_PATH`

---

### Layer 7: Knowledge & Intelligence

These repos feed The Agency with patterns, prompts, and intelligence.

#### 7A. System Prompts Collection (`system-prompts-and-models-of-ai-tools`)
**Repository:** [`sahiixx/system-prompts-and-models-of-ai-tools`](https://github.com/sahiixx/system-prompts-and-models-of-ai-tools)  
**Language:** JavaScript  
**Role:** 31+ AI tool system prompts (v0, Cursor, Manus, Devin, Windsurf, VSCode Agent, etc.)

**Connection to Agency:**
- The Agency's `spy` agent and `intel` preset use this collection
- Provides competitive intelligence on how other AI tools work
- Forked from `x1xhlol/system-prompts-and-models-of-ai-tools`

#### 7B. Prompt Pattern Library (`Y`)
**Repository:** [`sahiixx/Y`](https://github.com/sahiixx/Y)  
**Language:** Python  
**Role:** 26 universal prompt patterns

**Connection to Agency:**
- The Agency's `prompt-arch` agent uses this library
- Provides reusable prompt engineering patterns

#### 7C. Trust Graph (`Trust-graph-`)
**Repository:** [`sahiixx/Trust-graph-`](https://github.com/sahiixx/Trust-graph-)  
**Language:** Python  
**Role:** Neo4j trust graph

**Connection to Agency:**
- The Agency's `trust` agent queries this graph
- `query_trust_graph` MCP tool connects to Neo4j

#### 7D. Documentation Sites (`docs`, `mintlify-docs`)
**Repositories:**
- `docs` — MDX documentation
- `mintlify-docs` — Mintlify-powered docs site

**Connection to Agency:**
- The Agency's `docs` agent generates and maintains documentation
- Deployed via Mintlify

---

### Layer 8: Developer Tools & Scaffolds

#### 8A. Zsh Kimi CLI Plugin (`zsh-kimi-cli`)
**Repository:** [`sahiixx/zsh-kimi-cli`](https://github.com/sahiixx/zsh-kimi-cli)  
**Role:** Zsh plugin integrating Kimi CLI

#### 8B. Moltbot Sandbox (`moltbot-sandbox`, `moltbot-sandboxt`, `moltbot-sandboxuu`)
**Role:** Experimental Moltbot variants

#### 8C. Telegram CRM Bot (`TelegramCrmBot`)
**Role:** Replit-hosted Telegram CRM bot

---

### Layer 9: Forked & Enhanced Ecosystem

These are **strategic forks** that sahiixx actively extends and integrates with The Agency.

| Fork | Origin | Focus | Agency Integration |
|------|--------|-------|-------------------|
| `openclaw` | openclaw/openclaw | Personal AI assistant (TypeScript) | OpenClaw gateway in sovereign-swarm-v2 |
| `goose` | aaif-goose/goose | Extensible AI agent (Rust) | AAIF/Linux Foundation project |
| `rowboat` | rowboatlabs/rowboat | AI coworker with memory (TypeScript) | Memory patterns借鉴 |
| `autogen` | microsoft/autogen | Agentic AI framework (Python) | `autogen_provider.py` in Agency |
| `langchain` | langchain-ai/langchain | LangChain framework | Core dependency |
| `llama-cookbook` | meta-llama/llama-cookbook | Llama recipes | Local model deployment |
| `openai-cookbook` | openai/openai-cookbook | OpenAI patterns | Provider abstraction |
| `Kimi-K2` | moonshotai | Kimi K2 model | Model provider |
| `Kimi-Audio` | moonshotai | Kimi Audio | Voice AI |
| `kimi-cli` | moonshotai | Kimi CLI | Zsh integration |
| `kimi-agent-sdk` | moonshotai | Kimi agent SDK | Agent framework |
| `ollama` | ollama/ollama | Local LLM runner | `ollama_provider.py` |
| `OpenManus` | manus-ai/OpenManus | Manus agent | Inspiration |
| `Perplexica` | ItzCrazyKns/Perplexica | AI search | Research augmentation |
| `public-apis` | public-apis/public-apis | API directory | Tool integration |

---

## 🔌 Integration Bridge Matrix

The `agency-agents/integrations/` directory contains **9 formal integration guides** that document how The Agency connects to other repos:

| Integration | Target Repo | Protocol | Purpose |
|------------|-------------|----------|---------|
| `nowhere-ai-platform-bridge.md` | `Fixfizx` | HTTP REST + MCP | Dubai digital services platform |
| `coral-protocol-bridge.md` | `Coral-BlackboxAI-Agent` | SSE + Coral Protocol | Cross-framework agent communication |
| `nextjs-chatbot-deployment.md` | `nextjs-ai-chatbot` | HTTP SSE + Vercel AI SDK | Chat UI frontend |
| `shadow-swarm-bridge.md` | `SHADOW` | Coral Protocol SSE | Voice→Code pipeline |
| `n8n-agency-bus.md` | `n8n` | HTTP Webhook | Workflow automation triggers |
| `cloudflare-deployment-templates.md` | `react-router-starter-template`, etc. | Wrangler CLI | Edge deployment |
| `moltworker-gateway-bridge.md` | `moltworker` | HTTP POST | Multi-channel messaging |
| `nowire-os-frontend.md` | `v0-nowire-os-blueprint` | Vercel CI/CD | Auto-generated CRM UI |
| `openclaw/README.md` | `openclaw` | SOUL.md + AGENTS.md | Personal AI workspace |

---

## 🗺️ Data Flow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER INTERFACES                                │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────────┐ │
│  │  Voice   │  │   Chat   │  │   Web    │  │ Telegram │  │    Slack     │ │
│  │ JARVISv3 │  │ Next.js  │  │ Nowire   │  │ Moltbot  │  │  Moltworker  │ │
│  │ friday-os│  │ Chatbot  │  │   OS     │  │          │  │              │ │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └────┬─────┘  └──────┬───────┘ │
│       │             │             │             │                 │         │
└───────┼─────────────┼─────────────┼─────────────┼─────────────────┼─────────┘
        │             │             │             │                 │
        └─────────────┴─────────────┴─────────────┴─────────────────┘
                                  │
                    ┌─────────────┴─────────────┐
                    │     A2A / MCP / SSE       │
                    │     Protocol Layer        │
                    └─────────────┬─────────────┘
                                  │
        ┌─────────────────────────┼─────────────────────────┐
        │                         │                         │
┌───────▼────────┐      ┌─────────▼──────────┐    ┌────────▼───────┐
│   THE AGENCY   │      │ Sovereign Swarm v2│    │  SHADOW Swarm  │
│  152 Agents    │◄────►│  Safety Council   │    │ Voice→Code     │
│ Claude Core    │      │  Cost Mgmt        │    │ Review→Log     │
│ Titans Memory  │      │  Healing          │    │ Coral Protocol │
└───────┬────────┘      └───────────────────┘    └────────────────┘
        │
        ├──────────────────────────────────────────────────────────────┐
        │                      MCP TOOL CALLS                          │
        │                                                                │
┌───────▼────────┐  ┌──────────▼─────────┐  ┌─────────▼─────────┐  ┌───▼────────────┐
│   NOWHERE.AI   │  │   n8n Webhooks     │  │  Cloudflare       │  │  Lead Scraper  │
│   Fixfizx      │  │   Automation Bus   │  │  Workers/Pages    │  │  ae-lead-scraper│
│  Stripe AED    │  │                    │  │                   │  │                │
│  Twilio SMS    │  │                    │  │                   │  │                │
└────────────────┘  └────────────────────┘  └───────────────────┘  └────────────────┘
        │
        └──────────────────────────────────────────────────────────────┐
        │                      KNOWLEDGE FEEDS                        │
        │                                                                │
┌───────▼─────────────┐  ┌──────────▼──────────┐  ┌───────▼──────────┐
│ System Prompts      │  │  Prompt Patterns    │  │   Trust Graph    │
│ Collection          │  │  Library (Y)        │  │   Neo4j          │
└─────────────────────┘  └─────────────────────┘  └──────────────────┘
```

---

## 🎯 Strategic Pillars

### Pillar 1: Multi-Agent Intelligence
- **Core:** `agency-agents` (152 agents)
- **Runtime:** `sovereign-swarm-v2` (45 modules, 6 domains)
- **Voice:** `friday-os` (LiveKit + Tauri)
- **Local:** `goose-aios` (Ollama)

### Pillar 2: Dubai/UAE Market
- **Platform:** `Fixfizx` (NOWHERE.AI)
- **Real Estate:** `sahiix-os`
- **Leads:** `ae-lead-scraper---`
- **Deployment:** Cloudflare templates (edge-near Dubai)

### Pillar 3: Workflow Automation
- **Engine:** `n8n` + `n8n-free-templates` + `n8n-workflows-1`
- **Bus:** `n8n-agency-bus.md` integration
- **Edge:** `moltworker` (Cloudflare Workers)

### Pillar 4: Cross-Protocol Communication
- **A2A:** Google A2A v0.3 in `agency-agents`
- **MCP:** 19 LangChain-compatible tools
- **Coral:** SSE-based cross-framework messaging
- **Hermes:** WeChat gateway via `hermesclaw`

### Pillar 5: Knowledge & Competitive Intelligence
- **Prompts:** `system-prompts-and-models-of-ai-tools` (31+ tools)
- **Patterns:** `Y` (26 universal patterns)
- **Trust:** `Trust-graph-` (Neo4j graph)
- **Docs:** `docs` + `mintlify-docs`

---

## 📊 Repo Count by Layer

| Layer | Original Repos | Forked Repos | Total |
|-------|---------------|--------------|-------|
| Core Brain | 1 | 0 | 1 |
| AI OS (Runtime) | 3 | 0 | 3 |
| Industry Apps | 4 | 0 | 4 |
| Communication Bridges | 4 | 0 | 4 |
| Frontend & Deployment | 5 | 0 | 5 |
| Automation Bus | 1 | 4 | 5 |
| Knowledge & Intelligence | 4 | 0 | 4 |
| Developer Tools | 4 | 0 | 4 |
| Forked Ecosystem | 0 | ~118 | ~118 |
| **TOTAL** | **~26** | **~122** | **~148** |
| Experimental/Scaffold | ~21 | — | ~21 |
| **GRAND TOTAL** | **~47** | **~122** | **~169** |

*(Note: GitHub API returns 169 repos including the `sahiixx/sahiixx` profile README repo)*

---

## 🚀 Operational Commands

```bash
# Run The Agency
 cd ~/agency-agents && python3 agency.py --mission "..."

# Run FRIDAY OS
 cd ~/friday-os && python3 -c "from friday.core import Orchestrator; print(Orchestrator().run('hello'))"

# Run Sovereign Swarm
 cd ~/sovereign-swarm-v2 && python3 -m sovereign_swarm --repl

# Sync all forks
 cd ~/sahiixx-portfolio && python3 sync_forks.py --push

# Deploy to Cloudflare
 cd ~/react-router-starter-template && npm run deploy

# Trigger n8n webhook
 curl -X POST http://localhost:5678/webhook/agency \
   -H "Content-Type: application/json" \
   -d '{"workflow_tag":"crm","payload":{...}}'
```

---

## 🔮 Vision

> *"Building the autonomous future, one agent at a time."*

The sahiixx ecosystem is designed as a **fully autonomous AI infrastructure** where:
1. **The Agency** reasons and plans
2. **Sovereign Swarm** manages safety and cost
3. **FRIDAY OS** provides voice-first interfaces
4. **n8n** automates workflows
5. **NOWHERE.AI** runs production services
6. **Moltworker** reaches users on every channel
7. **System Prompts** keeps competitive intelligence

Every repo is a node. The connections are the magic.

---

*Generated by Copilot CLI*  
*Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>*
