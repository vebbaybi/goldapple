# MVP Scope

## Promise

Given an explicitly authorized, trusted VS Code workspace and a developer-initiated investigation, Golden Apple correlates local project structure, Git history, dependencies, VS Code diagnostics, and explicitly supplied or approved build/test failure output into an evidence-backed explanation.

## Included

- TypeScript VS Code client and authenticated local Python runtime
- workspace consent and restricted-mode behavior
- supported local Git repositories and bounded project discovery
- dependency manifest/lockfile parsing without installing dependencies
- diagnostics and approved command-output ingestion
- typed evidence, cited claims, confidence, and investigation export
- local SQLite persistence and user-approved memory
- OpenAI-first provider gateway with local-only degradation

## Excluded

No autonomous edits, command execution, background machine monitoring, containers/cloud discovery, generalized OS control, browser capture, token, wallet, blockchain, marketplace, agent SDK, or Proof of Useful Work. Authentication is included only if owner review confirms an MVP need; local-only use must remain architecturally possible.

## Acceptance

A deterministic golden fixture with a known dependency regression produces the expected observation and bounded inference, cites the relevant commit, manifest/lockfile delta, diagnostic, and failing test output, exposes missing evidence, transmits nothing without consent, and retains only approved knowledge.
