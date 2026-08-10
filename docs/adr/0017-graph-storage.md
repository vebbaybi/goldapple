# ADR-0017: Graph Storage

- Status: Proposed
- Date: 2026-08-10

## Context

Golden Apple needs a reviewable decision for graph storage while the repository contains no product implementation.

## Decision

Adopt this direction as the Phase 0 default, subject to prototype validation before acceptance.

## Alternatives considered

A single-process product, a different technology, deferring the choice, and a managed/cloud-first design were considered. Detailed benchmarks remain outstanding.

## Reasoning

The proposal best supports local-first control, narrow trust boundaries, portability, testability, and incremental delivery under current assumptions.

## Consequences and risks

The decision adds integration and maintenance cost and may change after threat modeling, profiling, ecosystem research, or legal review. No implementation should treat a Proposed ADR as irreversible certainty.
