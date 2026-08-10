# Threat Model

## Protected assets

Source code, secrets, developer identity, repository history, diagnostics, model prompts/responses, local database, IPC credentials, account tokens, and user trust.

## Primary threats

| Threat | Boundary | Required control | MVP verification |
| --- | --- | --- | --- |
| Prompt injection in repository text | content → reasoning | Treat as data, provenance labels, tool-policy isolation | adversarial fixture tests |
| Secret exfiltration | local → provider/log | detection, minimization, deny rules, explicit preview | canary-secret tests |
| Malicious workspace execution | workspace → runtime | VS Code Workspace Trust, no implicit execution, argument-safe process API | restricted-workspace tests |
| Local IPC impersonation/replay | VSIX ↔ runtime | per-install secret, OS permissions, nonce, versioning, rate limits | protocol security tests |
| Path escape/symlink race | workspace → filesystem | canonical containment, no-follow policy, TOCTOU review | filesystem abuse tests |
| Dependency compromise | build/release | locks, provenance, scanning, review, signed artifacts | CI supply-chain gates |
| Evidence tampering | source → finding | digests, immutable capture metadata, derived lineage | integrity tests |
| Over-retention | storage | classification, TTL, deletion/reset, backup policy | lifecycle tests |

Residual risks include model error, compromised host, malicious extensions, provider compromise, and novel supply-chain attacks. A threat-model review is required at each new adapter or authority boundary.
