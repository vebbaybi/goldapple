# Golden Apple White Paper

**Version 0.1 — Phase 0 working paper, 2026-08-10**  
**Status: architecture and research. Golden Apple has no released runtime, network, marketplace, or token.**

## 1. Abstract

Golden Apple proposes a local-first intelligence layer that turns fragmented developer evidence into explainable investigations. Its first proof is a read-only VS Code workflow for diagnosing development failures. A longer research path explores portable agent provenance and useful-work coordination without making blockchain or a token a product dependency.

## 2–5. Problem, motivation, and vision

Development truth is split among source trees, Git history, dependency graphs, diagnostics, terminals, build systems, configuration, and human memory. General conversational interfaces can summarize fragments but often hide provenance and authority boundaries. Golden Apple instead models an investigation: authorized evidence is captured, normalized, related, and cited by claims. The motivating question is “Why did this application stop working yesterday?” A credible answer identifies changes, failures, affected scope, uncertainty, reproduction evidence, and safe next steps.

## 6. Product principles

Local first; evidence before assertion; read before write; least privilege; explicit authorization; reversible operations; verification before success claims; security and privacy by design; user sovereignty; provider independence; no silent upload; and architecture before autonomy are normative. See [Product Principles](PRODUCT_PRINCIPLES.md).

## 7–8. Local-first system architecture

The first client is a TypeScript VS Code extension. A separately installed Python local runtime owns discovery, normalization, correlation, policy, and local persistence. Authenticated versioned IPC prevents the extension UI from becoming an ambient privileged authority. SQLite stores local structured state. Rust is reserved for a future measured native boundary; PostgreSQL is limited to an optional account/control plane. These are Proposed decisions, not shipped components.

GoldenCore orchestrates; GoldenGraph relates evidence; GoldenEye normalizes diagnostics and approved runtime output; GoldenGit explains history; GoldenShield defines defensive controls; GoldenForge normalizes build/test evidence; GoldenMemory retains approved knowledge; GoldenLab is a future simulation boundary.

## 9. Evidence model

Evidence carries provenance, capture time, scope, integrity digest, parser version, authorization, sensitivity, and retention. Claims are observations, inferences, hypotheses, or recommendations and cite evidence IDs. Models produce candidate interpretations, never evidence. Conflicts and missing evidence remain visible.

## 10–11. Trust, permissions, and security

Reading, executing, transmitting, writing, and retaining are separate permissions. Workspace text is hostile input and cannot grant authority. The design anticipates prompt injection, secret exfiltration, malicious configuration, path escape, IPC impersonation, dependency compromise, evidence tampering, over-retention, and compromised providers. Host compromise remains a fundamental residual risk.

## 12. AI architecture

An OpenAI-first but provider-independent gateway receives task-specific, minimized context only after policy and consent. Provider features, retention, region, and tool behavior are explicit capability metadata. Local-only operation must remain useful. The user sees concise justification, evidence, assumptions, uncertainty, and actions—not private model chain-of-thought.

## 13. GoldenGraph

GoldenGraph is a typed domain model, not a premature graph-database decision. It relates workspaces, repositories, commits, files, dependencies, diagnostics, runs, evidence, claims, and investigations. SQLite adjacency tables are the starting proposal; scale and query evidence may later justify a dedicated engine.

## 14–15. VS Code-first progression

The VSIX is the first interface, not the platform boundary. The MVP proves one trusted, user-initiated, read-only investigation. V1 adds supported ecosystems, operational hardening, accessible UX, provider controls, deletion/reset, signed artifacts, and support policy. Controlled actions require a later permissions, simulation, rollback, and verification program.

## 16–18. Golden Agent Protocol, identity, and provenance

Future research proposes a protocol describing an agent's stable identifier, controller, versioned capability manifest, policy needs, software provenance, attestation references, and revocation. User-facing presentation may be Mr Goldenapple, Mrs Goldenapple, or the neutral Unicorn persona; presentation is not authorization identity. Agent claims must remain bound to the software, model/provider, policy, evidence, and operator context that produced them.

## 19–23. Network, useful work, receipts, reputation, and marketplace

An optional Golden Apple Network could coordinate independently operated agents where cross-party verification creates real value. Proof of Useful Work must measure an externally verifiable task outcome rather than raw compute or self-reported effort. A Work Receipt may commit to request class, acceptance criteria, artifacts, verification, parties, timestamps, and dispute state while keeping private work off-chain. Reputation must be task-specific, decay-aware, appealable, and resistant to self-dealing. Marketplace design must address discovery, licensing, sandboxing, payments, disputes, malicious publishers, and jurisdictional constraints before implementation.

## 24–27. Token, economics, 1807, and treasury

No token is approved. Candidate utility—settlement, staking against service quality, or governance—must outperform existing payments and non-transferable reputation without creating adoption friction or regulatory harm. Emissions cannot substitute for demand. The 1807 relationship is proposed as a broader portfolio/ecosystem context; entity ownership, brand rights, governance, conflicts, and financial flows remain unresolved. Any treasury requires a charter, mandate limits, transparent accounting, custody controls, conflicts policy, audit, and emergency procedures.

## 28–29. Privacy and Web3 security

Source code, prompts, raw evidence, secrets, personal data, and detailed outputs stay off-chain. Even hashes can leak linkage and must be opt-in and minimized. Smart contracts introduce key compromise, upgrade abuse, oracle manipulation, replay, Sybil attacks, collusion, wash work, denial of service, economic exploits, and immutable privacy failures. Formal review, fuzzing, invariants, staged limits, monitoring, pause/recovery, and independent audit are prerequisites—not guarantees.

## 30. Governance

Near-term governance is maintainer-led with transparent ADRs, issue review, security escalation, and release gates. Progressive decentralization is a possible outcome only when independent participation, operational maturity, and capture resistance are demonstrated.

## 31–33. Risks, limitations, and legal review

Model error, incomplete evidence, user over-trust, malicious repositories, provider dependence, performance, cross-platform complexity, unsustainable scope, governance capture, and premature economics are material risks. Golden Apple cannot guarantee causality, detect evidence that was never captured, or protect a fully compromised host. Qualified review is required for licensing, trademarks, privacy, AI processing, source-code handling, crypto assets, custody, money transmission, KYC/AML, sanctions, tax, marketplace payouts, consumer protection, and jurisdictional rules. This paper is not legal or investment advice.

## 34. Roadmap

Foundation → VSIX shell/local handshake → discovery/evidence store → evidence adapters → cited investigation MVP → V1 hardening → controlled-action research → native/cross-system research → agent protocol/SDK → optional network/marketplace → useful-work experiments → possible progressive decentralization. No dates or token event are promised.

## 35. Future research

Research priorities include causal confidence calibration, privacy-preserving context selection, deterministic evidence replay, graph query benchmarks, secure local IPC, cross-platform sandboxing, agent capability attestation, useful-work verification, Sybil resistance, dispute mechanisms, and economic simulation.

## 36. Conclusion

Golden Apple's defensible value is not personality or automation alone. It is a trustworthy chain from authorized observation to cited explanation, then—only when justified—to safe, verified action. The repository must prove that chain locally before pursuing a network around it.
