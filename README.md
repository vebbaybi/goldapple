# Golden Apple

> A local-first developer and personal computing intelligence layer.

Golden Apple is an open-source platform being designed to investigate development failures by correlating repository history, project structure, dependencies, diagnostics, and explicitly approved build or test output. It is not a chatbot, autonomous repair tool, released product, or deployed network.

**Current status: Phase 0 — foundation and architecture. No product runtime exists yet.**

## The promise

Golden Apple is being built to answer a difficult question with evidence:

> Why did this application stop working yesterday?

The system should eventually explain what changed, what failed, what is affected, how confident it is, and which evidence supports each important claim.

`Observe → Understand → Correlate → Explain → Simulate → Act → Verify → Remember`

Autonomy advances only when permissions, confidence, reversibility, and verification justify it.

## First product boundary

The first client will be a VS Code extension backed by a local intelligence runtime. The MVP is read-only and proves one complete investigation loop:

1. a developer explicitly authorizes a trusted workspace;
2. Golden Apple discovers project, Git, dependency, diagnostic, and approved command-output evidence;
3. an investigation correlates that evidence;
4. findings separate observations, inferences, hypotheses, and recommendations;
5. every material claim cites evidence and carries appropriate confidence;
6. only user-approved knowledge is retained locally.

No autonomous repair, background machine surveillance, token, marketplace, blockchain dependency, or generalized system control is in the MVP.

## System map

| System | Responsibility | MVP status |
| --- | --- | --- |
| GoldenCore | Investigation orchestration and policy enforcement | Planned |
| GoldenGraph | Typed project and evidence relationships | Planned |
| GoldenEye | Diagnostics and approved runtime-output ingestion | Limited MVP scope |
| GoldenGit | Repository and change-history intelligence | Planned |
| GoldenShield | Security boundaries and defensive analysis | Foundation controls only |
| GoldenForge | Build and test evidence normalization | Limited MVP scope |
| GoldenMemory | Approved, local durable knowledge | Planned |
| GoldenLab | Isolated simulation and experimentation | Post-MVP |

See [System Architecture](docs/architecture/SYSTEM_ARCHITECTURE.md), [MVP Scope](docs/product/MVP_SCOPE.md), and the [Traceability Matrix](docs/TRACEABILITY_MATRIX.md).

## Principles

- local first and no silent cloud upload
- evidence before assertion
- read before write
- least privilege and explicit authorization
- reversible operations and verification before success claims
- security and privacy by design
- user sovereignty and provider independence
- blockchain only where it creates measurable utility
- architecture before autonomy

The normative set lives in [PRODUCT_PRINCIPLES.md](PRODUCT_PRINCIPLES.md).

## Repository guide

| Area | Purpose |
| --- | --- |
| [`docs/product/`](docs/product/) | Product, user, MVP, V1, and exclusions |
| [`docs/requirements/`](docs/requirements/) | Identified functional and quality requirements |
| [`docs/architecture/`](docs/architecture/) | Components, boundaries, deployment, and failure model |
| [`docs/ai/`](docs/ai/) | Evidence, model gateway, safety, and memory policies |
| [`docs/security/`](docs/security/) | Threat model, permissions, secrets, and response |
| [`specs/`](specs/) | Subsystem contracts and maturity boundaries |
| [`docs/adr/`](docs/adr/) | Proposed and accepted architectural decisions |
| [`docs/web3/`](docs/web3/) | Future/research network architecture; not an MVP dependency |
| [`gaxyz/`](gaxyz/) | Portable, non-deploying public website package |

Start with [VISION.md](VISION.md), [ROADMAP.md](ROADMAP.md), [WHITEPAPER.md](WHITEPAPER.md), and [CONTRIBUTING.md](CONTRIBUTING.md).

## Development status

This repository contains specifications and a portable public website foundation only. Commands, packages, installations, releases, performance numbers, and screenshots must not be presented as available until implementation and release evidence exist.

## Security

Do not report vulnerabilities through a public issue. Follow [SECURITY.md](SECURITY.md). Security contact details remain an owner decision before the first release.

## License

Apache License 2.0. See [LICENSE](LICENSE). Branding and generated artwork require an explicit asset/trademark policy before external reuse; see the [legal review register](docs/governance/LEGAL_REVIEW_REGISTER.md).
