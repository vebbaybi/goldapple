# System Architecture

## Context

The VS Code client presents consent, investigations, findings, and evidence navigation. A separately installed local runtime owns privileged discovery and storage. They communicate over authenticated, versioned localhost IPC with per-install credentials, origin checks, bounded messages, and no unauthenticated listener.

## Core flow

`User → VSIX consent → GoldenCore policy → evidence adapters → normalized evidence → GoldenGraph relations → investigation → cited findings → user`

The model gateway is an optional outbound boundary after redaction, minimization, disclosure, and provider policy. Local-only operation degrades reasoning breadth but preserves evidence browsing. Cloud account services are optional control-plane capabilities and never become the authoritative store for workspace content.

## Runtime boundaries

- TypeScript: VS Code integration, presentation, consent, protocol client.
- Python: investigation orchestration, adapters, evidence, provider gateway.
- SQLite: local metadata/evidence index; source artifacts remain referenced where safe.
- Rust: proposed only for a future narrow privileged/native boundary after profiling and threat review.
- PostgreSQL: proposed optional account/control-plane data, never default local project storage.

See component, deployment, IPC, trust-boundary, and failure-model documents. All components are planned.
