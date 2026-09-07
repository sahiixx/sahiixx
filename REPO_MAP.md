# SAHIIXX Repository Map

> Generated from public GitHub inventory · 2026-09-07  
> Profile: [@sahiixx](https://github.com/sahiixx) · **216 public** repos (~71 original, ~145 forks)

This file is the **structured index** of the account. The profile README stays short; this map holds the taxonomy.

---

## 1. Design principles

| Principle | Practice |
|-----------|----------|
| **Products ≠ forks** | Only non-fork, owned repos are “products” |
| **Layers over folders** | Organize by SAHIIX Stack layer (L0–L7), not by language |
| **Core is small** | ~15–25 repos deserve continuous attention |
| **Forks are library** | 145 upstream clones for study — not marketed as SAHIIX |
| **Noise is explicit** | Short-name / empty experiments listed so they can be archived |

---

## 2. Inventory summary

| Class | Approx. count | Action |
|-------|---------------|--------|
| Core runtime / edge / surface / vertical | ~25 | Keep green |
| Supporting original | ~20 | Maintain or merge |
| Experimental / noise originals | ~25 | Archive candidates |
| Forks (reference) | ~145 | Leave as forks |
| **Public total** | **216** | — |
| Private (e.g. agno, revenue OS) | n (auth) | Document by name only |

**Languages (public):** Python ~67 · TypeScript ~57 · JS ~13 · Go ~8 · Rust ~7 · other

---

## 3. Core map (by stack layer)

### L7 — Experience
| Repo | Role |
|------|------|
| [sahiixx-os](https://github.com/sahiixx/sahiixx-os) | OS command center |
| [sahiix-portfolio](https://github.com/sahiixx/sahiix-portfolio) | Public portfolio + pilots |
| [systems-panel](https://github.com/sahiixx/systems-panel) | Live module status |
| [sahiix-os-docs](https://github.com/sahiixx/sahiix-os-docs) | Architecture docs (Stack v2.1) |
| [sahiixx](https://github.com/sahiixx/sahiixx) | Profile README + this map |
| **agno** *(private)* | App Builder workspace |

### L6 — Verticals
| Repo | Role |
|------|------|
| **sovereign-revenue-os** *(private)* | Dubai RE revenue OS |
| [sovereign-swarm-v2](https://github.com/sahiixx/sovereign-swarm-v2) | Multi-agent swarm |
| [sahiixx-geoflow-agent](https://github.com/sahiixx/sahiixx-geoflow-agent) | GEO / listings agent |
| [friday-os](https://github.com/sahiixx/friday-os) | Voice-first personal OS |
| Lead Machine | Implemented inside **sahiixx-agency** (`/opa/lead/*`) |

### L5 — Agent runtime
| Repo | Role |
|------|------|
| [sahiixx-agency](https://github.com/sahiixx/sahiixx-agency) | **OPA** — dispatch, adapters, Lead Machine |
| [sahiixx-bus](https://github.com/sahiixx/sahiixx-bus) | Message bus |
| [sahiixx-titans-memory](https://github.com/sahiixx/sahiixx-titans-memory) | Persistent memory |
| [sahiixx-graph-sight](https://github.com/sahiixx/sahiixx-graph-sight) | Trust / AST graph |
| [sahiix-agi](https://github.com/sahiixx/sahiix-agi) | AGI coordination layer |
| [agency-agents](https://github.com/sahiixx/agency-agents) | Agent experiments |

### L4 — Harness
| Repo | Role |
|------|------|
| [agentic-harness](https://github.com/sahiixx/agentic-harness) | Shared patterns + Foundry routing |
| [agentic-harness-integration](https://github.com/sahiixx/agentic-harness-integration) | Integration pack |

### L3 — Edge & governance
| Repo | Role |
|------|------|
| [sahiix-proxy](https://github.com/sahiixx/sahiix-proxy) | JWT · rate · WATI · Termux |

### QA / security
| Repo | Role |
|------|------|
| [sahiixx-e2e](https://github.com/sahiixx/sahiixx-e2e) | Playwright + Lead Machine contracts |
| [sahiixx-clearwing](https://github.com/sahiixx/sahiixx-clearwing) | Security swarm |

### Other owned platforms
| Repo | Role |
|------|------|
| [saas-agent-platform](https://github.com/sahiixx/saas-agent-platform) | Multi-tenant agent SaaS |
| [moltworker](https://github.com/sahiixx/moltworker) | OpenClaw on Workers |
| [f](https://github.com/sahiixx/f) | Workers AI gateway |

---

## 4. Fork library (not products)

~145 forks for **study / upstream tracking**. Examples:

- **Agent frameworks:** `adk-python`, `adk-samples`, `openai-agents-js`, `openai-agents-python`, `browser-use`, …
- **Infra / tools:** `workers-sdk`, `codex`, `chrome-devtools-mcp`, …
- **Apps:** `n8n`-adjacent, chat UIs, etc.

**Do not** list forks as SAHIIX flagships. Star or topic them upstream when useful.

---

## 5. Experimental / noise (archive candidates)

Owned repos with weak naming or unclear product role (non-exhaustive):

`7`, `Bag`, `Big`, `Bvvh`, `H`, `Hh`, `X`, `X1`, `Xxxxxxx`, `Y`, `Gsje`, `SHADOW`, `studious-sniffle`, `Fixfiz`, `Fixfizx`, `nextjs-ai-chatbotg`, …

**Recommendation:** archive or privatize; keep Core map clean.

---

## 6. Topic / naming conventions (suggested)

| Topic | Use on |
|-------|--------|
| `sahiixx` | All core products |
| `opa` | Agency / dispatch |
| `lead-machine` | Capture / qualify / match |
| `edge` | Proxy / Termux |
| `dubai` / `real-estate` | Verticals |
| `fork-study` | Optional on forks |

Repo names: prefer `sahiixx-*` or `sahiix-*` for anything that ships.

---

## 7. Relationship diagram (core only)

```text
                    [sahiix-portfolio] [systems-panel] [sahiixx-os] [agno]
                                      \       |       /
                                       \      |      /
                                        [sahiix-os-docs]
                                              |
         [sahiix-proxy] ---- JWT/rate ----> [sahiixx-agency / OPA]
                                              |
                    +-------------------------+-------------------------+
                    |                         |                         |
              Lead Machine              [sahiixx-bus]            [agentic-harness]
           capture/qualify/match              |                         |
                    |                   memory/graph                 Foundry
                    v                         v
              [sahiixx-e2e]              titans / graph-sight
```

---

## 8. Maintenance checklist

- [ ] Profile README only links **Core** + Stack doc  
- [ ] New product → add to Core map + Stack v2.1  
- [ ] New fork → leave unlabeled or `fork-study`  
- [ ] Quarterly: archive noise names  
- [ ] Private cores named in README, not expanded  

---

**SAHIIX Stack v2.1 · structured profile · less noise, clearer products**
