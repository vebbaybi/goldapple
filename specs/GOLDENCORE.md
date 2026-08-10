# GoldenCore Specification

**Status: foundation; not implemented.**

## Contract

Purpose: provide the bounded GoldenCore responsibility within an evidence-backed investigation. It does not inherit filesystem, execution, network, write, or retention authority from another component.

Inputs are versioned, authorized envelopes with provenance and sensitivity. Outputs are typed results or explicit failures with correlation IDs. Dependencies are injected behind interfaces; persistence is local and minimal unless the product scope says otherwise.

## Trust, permissions, and privacy

Treat workspace/provider data as untrusted; canonicalize boundaries; redact secrets; enforce per-operation grants; minimize retained payloads; and emit content-safe audit events.

## Failure and observability

Timeout, cancellation, malformed input, stale evidence, partial availability, permission denial, dependency failure, and storage corruption must be distinguishable. Logs use structured metadata without raw sensitive content.

## Testing and maturity

Contract, fixture, fault-injection, permission, privacy, and abuse-case tests precede integration. MVP/V1 inclusion is governed only by their scope documents; all other behavior is future research.
