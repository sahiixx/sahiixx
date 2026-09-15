# SAHIIXX — Connected Ecosystem Map

**Source:** read-only scrape of GitHub user `sahiixx` (fork-inclusive, 238 repos) + Cloudflare account `37009577de6a11bcf8747f72ce923a4f` · **Built:** 2026-09-15

This document connects the dots: it groups every repo into a cluster, records the evidence for each connection, and maps code → runtime.

---

## 1. The three spines

| Spine | Naming thread | Meaning | Anchor repos |
|---|---|---|---|
| **SAHIIXX OS** | `sahiixx` / `sahiix` | The umbrella: command centre, dashboards, the OS idea | `sahiixx`, `sahiixx-os`, `sahiix-os`, `systems-panel` |
| **Sovereign / NEXUS** | `sovereign-*`, `nexus-*`, `lead-*` | Dubai real-estate revenue vertical (the commercial thesis) | `sovereign-revenue-os`, `nexus-buyer-recovery`, `sovereign-agents` |
| **FRIDAY / moltbot** | `friday*`, `moltbot*`, `openclaw` | Personal assistant + edge runtime lineage | `friday-os`, `moltworker`, `moltbot-sandbox` |

---

## 2. Originals (93) by cluster — with evidence

| Cluster | n | Repos | Evidence for grouping |
|---|---|---|---|
| Identity / umbrella | 6 | `sahiixx`, `sahiixx-os`, `sahiix-os`, `systems-panel`, `app`, `open` | name + `sahiixx` topic; `sahiixx-os` description names Cloudflare |
| Edge / runtime | 6 | `moltworker`, `moltbot-sandbox`, `moltbot-sandboxt`, `moltbot-sandboxuu`, `opencla`, `f` | name family; matched to live Workers (§4) |
| Agent frameworks & orchestration | 16 | `agency-agents`, `sovereign-swarm-v2`, `sahiixx-agency`, `sahiixx-bus`, `saas-agent-platform`, `agentic-harness`, `agentic-harness-integration`, `sahiix-agi`, `sahiixx-clearwing`, `agents-for-multi-agent-systems`, `Coral-BlackboxAI-Agent`, `sahiixx-geoflow-agent`, `Genxai`, `codex-self`, `kimi-core`, `sahiixx-bus-backup` | topics `multi-agent`, `mcp`, `swarm`, `sahiixx`; descriptions |
| Dubai real-estate revenue | 11 | `sovereign-revenue-os`, `nexus-buyer-recovery`, `sovereign-agents`, `sovereign-prompt-pack`, `lazy-ai-ops`, `sahiix-os-docs`, `sahiix-portfolio`, `ae-lead-scraper---`, `campaigns`, `UAE-deal-`, `v0-nowire-os-blueprint` | descriptions explicitly say Dubai real estate; branch `claude/dubai-lead-scraper-setup-*` |
| Memory / knowledge / trust graph | 12 | `sahiixx-titans-memory`, `sahiixx-graph-sight`, `Trust-graph-`, `racx-reflection-pipeline`, `docs`, `mintlify-docs`, `ca-context7`, `https-github.com-x1xhlol-system-prompts-and-models-of-ai-tools`, `Xxxxxxx`, `X1`, `Fixfiz`, `Fixfizx` | topics `memory`, `knowledge-graph`, `trust-graph`; name |
| Personal assistant / voice | 4 | `friday-os`, `friday-tony-stark`, `SHADOW`, `goose-aios` | descriptions (LiveKit voice, MCP) |
| Infra / dev-ops | 5 | `sahiix-proxy`, `api-server`, `dev-helper`, `dev-test`, `myproject` | descriptions (edge proxy, Termux, servers) |
| Templates / scaffolds | 11 | `nextjs`, `nextjs-ai-chatbot`, `nextjs-ai-chatbotg`, `nextjs-boilerplate`, `react-router-starter-template`, `workflows-starter-template`, `containers-template`, `examples-hello-world`, `examples-with-fresh`, `express-js-on-vercel`, `v0-sahiixx-v0-nowhere.x` | description "template/starter" |
| Hygiene / placeholders | 13 | `Sahiix`, `H`, `Bag`, `Big`, `Gsje`, `Y`, `Hh`, `X`, `XXX`, `7`, `Bvvh`, `mbjv`, `studious-sniffle` | single-token names, no description |
| Unclassified | 9 | `ocr-playbook-scanner`, `ca-firecrawl`, `serene-jellyfish-nap`, `sahiixx-e2e`, `agno`, `-ai-idea-spark-`, `sahiix-ai`, `buzz`, `musical-octo-journey` | mixed; several newer (Sep 2026) |

---

## 3. Fork study library (145) by family

| Family | n | Members |
|---|---|---|
| OpenAI official samples & realtime | 17 | `openai-cookbook`, `openai-realtime-console`, `openai-structured-outputs-samples`, `openai-agents-python`, `openai-agents-js`, `openai-realtime-solar-system`, `openai-realtime-agents`, `openai-cua-sample-app`, `openai-cs-agents-demo`, `openai-responses-starter-app`, `openai-realtime-twilio-demo`, `openai-support-agent-demo`, `openai-testing-agent-demo`, `openai-fm`, `privacy-sandbox-samples`, `privacy-sandbox-demos`, `codex` |
| Agent frameworks (upstream) | 22 | `autogen`, `langchain`, `langflow`, `deer-flow`, `goose`, `genkit`, `motia`, `swarm`, `browser-use`, `bytebot`, `OpenManus`, `OpenManusahiix`, `Open-AutoGLM`, `Multi-Agent-Demo`, `claude-agent-sdk-python`, `fable-orchestrator`, `rowboat`, `shannon`, `hermes-agent`, `botpress`, `autogenous`, `awesome-agentic-patterns` |
| Reference / awesome lists | 31 | `build-your-own-x`, `public-apis`, `the-book-of-secret-knowledge`, `system_prompts_leaks`, `ollama`, `next.js`, `node`, `gin`, `awesome`, `awesome-agents-for-multi-agent-systems`, `awesome-coderabbit`, `prompts.chat`, `cookbook`, `docsb`, `content`, `community`, `lift`, `fides`, `trufflehog`, `auth-js`, `copilot-sdk`, `RuView`, `Hoku`, `ClueArk`, `CoPaw`, `GodsView`, `T3MP3ST`, `fuck-u-code`, `airecon`, `bitbucket`, `compass-ai-travel-planning-sample-flutter` |
| LLM app / data tooling | 15 | `lobe-chat`, `Perplexica`, `airllm`, `Stirling-PDF`, `Real-Time-Voice-Cloning`, `llama-cookbook`, `Dolphin`, `DeepSpeech`, `SQLBot`, `MoneyPrinterTurbo`, `ai-chatbot`, `turtledove`, `ucp`, `worldmonitor`, `x-algorithm` |
| Android / Kotlin / mobile | 12 | `voice-quickstart-android`, `pocketpal-ai`, `Valdi`, `SophiApp`, `android-sms-gateway`, `android-browser-helper`, `AboutLibraries`, `AnnotatedText`, `androidsvg`, `LazyVim`, `react-camera-kit`, `Ghost-Downloader-3` |
| MCP & tooling | 10 | `openclaw`, `nix-openclaw`, `chrome-devtools-mcp`, `cli`, `workers-sdk`, `skills`, `coreutils`, `servers`, `registry`, `clawhub` |
| n8n workflow ecosystem | 7 | `n8n`, `n8n-docs`, `n8n-free-templates`, `n8n-workflows-1`, `awesome-n8n-templates`, `ultimate-n8n-ai-workflows`, `activepieces` |
| Kimi / Moonshot | 7 | `Kimi-K2`, `Kimi-VL`, `Kimi-Audio`, `kimi-cli`, `kimi-agent-sdk`, `MoonshotAI-Cookbook`, `zsh-kimi-cli` |
| Qwen / ModelScope | 4 | `Qwen3-VL`, `Qwen3-Omni`, `modelscope`, `ms-swift` |
| Other / curated | 20 | `UI-TARS-desktop`, `rasa`, `adk-python`, `adk-java`, `adk-samples`, `llm-council`, `open-design`, `OpenWA`, `500-AI-Agents-Projects`, `oz-agent-action`, `fix-react2shell-next`, `coral-server`, `coral-studio`, `capnweb`, `ai-pr-reviewer`, `bifrost`, `ruflo`, `haikus-for-codespaces`, `friday-tony-stark-demo`, `system-prompts-and-models-of-ai-tools` |

---

## 4. Code → runtime (Cloudflare)

| Cloudflare | Kind | Linked repo | Match |
|---|---|---|---|
| `sahiix-portfolio.pages.dev` | Pages | `sahiix-portfolio` | EXACT (repo cites the URL) |
| `sahiixx-os.pages.dev` | Pages | `sahiixx-os` | EXACT |
| `sahiix-systems.pages.dev` | Pages | `systems-panel` | LIKELY |
| `500-ai-agents-projects.pages.dev` | Pages | — | UNMATCHED |
| worker `moltbot-sandbox` / `…t` / `…uu` | Worker | same-named repos | EXACT |
| worker `f` | Worker | `f` | EXACT |
| worker `opencla` | Worker | `opencla` | EXACT |
| worker `moltbot-sandboxh` / `…u`, `lead-hunter`, `lead-hunter-simple` | Worker | — | UNMATCHED |
| R2 `moltbot-data` | R2 | worker `moltbot-sandbox` | LIKELY |
| KV `sahiixx-os-memory` | KV | `sahiixx-os` | LIKELY |
| R2 `nvc`, `cloudflare-managed-*`; Queue `gudgg25` | — | — | UNMATCHED |

---

## 5. Gaps & caveats

- **Thin / aspirational:** the security vertical (`sahiixx-clearwing` + fork `airecon`) has no deployed surface; `sahiixx-bus-backup` is a backup with no counterpart.
- **No DNS zones:** every live surface is a default `*.pages.dev` / `*.workers.dev` name.
- **Duplicates to merge:** `moltbot-sandbox` / `…t` / `…uu`; `Fixfiz` / `Fixfizx`; `nextjs-ai-chatbot` / `…g`; `sahiix-os` vs `sahiixx-os`.
- **Fork links are family-level**, not verified parent→fork (search results don't expose the parent), so treat grouping as indicative.
- Unmatched live resources (`lead-hunter*`, `500-ai-agents-projects`, `nvc`) have no repo in the snapshot — deployed from local or unversioned code.
