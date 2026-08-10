# Permission Model

**Status: FOUNDATION — NOT IMPLEMENTED.** This document defines a reviewable Phase 0 contract; it does not describe shipped behavior.

## Purpose

Define the permission model decisions needed to preserve local-first operation, evidence provenance, least privilege, privacy, reversibility, and honest public status.

## Policy

- Every input has a source, authorization scope, sensitivity class, and retention rule.
- Every output distinguishes observed fact from inference and exposes limitations.
- Network, execution, write, and persistence authority are separate grants.
- Failures are explicit, observable, cancellable where possible, and never converted into false success.
- Security and privacy tests are acceptance requirements, not post-release additions.

## MVP and V1 boundary

MVP includes only what is explicitly listed in `docs/product/MVP_SCOPE.md`. V1 follows `docs/product/V1_SCOPE.md`. Any broader behavior remains research until an ADR, threat review, requirements, and test plan are approved.

## Open decisions

Owner, measurable acceptance criteria, operational budget, supported matrix, abuse cases, and migration/rollback details must be resolved before implementation.
