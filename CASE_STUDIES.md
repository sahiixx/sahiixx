# SAHIIXX case studies

Short, evidence-backed summaries of the systems behind the profile. Status labels
describe what is publicly verifiable; they do not imply that every local or
experimental component is production-deployed.

## 1. Contract-first model verification

**Status:** shipped · [`sahiixx-e2e`](https://github.com/sahiixx/sahiixx-e2e)

The release-verification harness now separates three model classes:

- **Traditional:** deterministic classification and lead scoring when rules are enough.
- **Generative:** chat, SSE streaming and tool-call contracts.
- **Foundation:** structured output, embeddings and vision capabilities.

The default matrix is network-free and uses fixed fixtures, runtime schemas,
bounded timeouts, redacted diagnostics and provider-neutral environment
configuration. Live provider canaries activate independently when their URL,
model and secret variables are configured. The merged implementation is covered
by the repository's smoke and model-matrix CI lanes.

## 2. Bounded agent runtime patterns

**Status:** shipped/reference implementation · [`agentic-harness`](https://github.com/sahiixx/agentic-harness)

The harness keeps workflow shapes explicit: chaining, routing, parallelization,
orchestrator-workers, evaluator-optimizer and ReAct. Each pattern is designed
around injected model calls, deadlines, iteration budgets, guardrails,
self-verification and trace records. Provider routing is capability-based so
application code does not need to hard-code a deployment name.

## 3. NEXUS → OPA boundary

**Status:** contract-ready · live release gate pending

[`sahiixx-agency`](https://github.com/sahiixx/sahiixx-agency) contains the OPA
lead-machine boundary, while [`sahiixx-bus`](https://github.com/sahiixx/sahiixx-bus)
provides the event seam. The E2E repository validates LeadCreated,
LeadQualified, LeadMatched and event-envelope identity contracts, and has
explicit service-boundary tests.

The remaining gate is operational: configure reachable OPA and bus environments,
run `REQUIRE_LIVE=1 npm run test:e2e:integration`, then add durable outbox,
retry/DLQ, trace propagation, tenant isolation, consent and approval checks
before describing specialist lead agents as production.

## 4. Operator, voice and edge surfaces

**Status:** public surfaces and active experiments

- [`sahiixx-os`](https://github.com/sahiixx/sahiixx-os) provides the public
  command-center surface.
- [`friday-os`](https://github.com/sahiixx/friday-os) explores voice, desktop,
  memory and MCP interaction.
- [`moltworker`](https://github.com/sahiixx/moltworker) explores Cloudflare edge
  gateway patterns.
- [`sahiixx-clearwing`](https://github.com/sahiixx/sahiixx-clearwing) focuses on
  evidence-oriented security verification.

These projects are intentionally labeled by evidence and deployment state in
the profile rather than presented as one monolithic production system.

## Reusable references

- [Connected ecosystem map](CONNECTED_ECOSYSTEM.md)
- [Founder/service architecture](FOUNDER_SERVICE_ARCHITECTURE.md)
- [Repository map and estate policy](REPO_MAP.md)
- [Profile hygiene workflow](HYGIENE.md)
- [Full portfolio inventory](FULL_PORTFOLIO.md)
