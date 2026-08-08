# Gold Apple

> A local-first Personal Computing Intelligence Layer.

Gold Apple is an intelligent software platform designed to understand a computer, its projects, repositories, services, applications, dependencies, data, processes, development history, and operational state as one connected system.

Gold Apple is not intended to be another chatbot.

Its purpose is to create an intelligence layer above the computer that can observe, understand, explain, diagnose, secure, test, and eventually assist with operating complex computing environments.

## Vision

Modern computers contain enormous amounts of fragmented context.

Source code exists in repositories.

Runtime information exists in logs.

Dependencies exist in package managers.

History exists in Git.

Infrastructure exists in containers and cloud platforms.

Security information exists in scanners and operating-system permissions.

Architectural knowledge often exists only in a developer's head.

Gold Apple connects these fragments into a coherent computational model.

The long-term objective is for a user to be able to ask:

"Why did this application stop working yesterday?"

and receive an evidence-backed explanation derived from:

- repository history
- file changes
- dependency changes
- runtime logs
- configuration
- environment differences
- processes
- services
- containers
- tests
- operating-system events
- previous incidents
- known project architecture

Gold Apple should understand what happened, why it happened, what is affected, and what safe actions are available.

## Core Principle

Gold Apple follows:

Observe -> Understand -> Correlate -> Explain -> Simulate -> Act -> Verify -> Remember

Actions should become progressively more autonomous only as confidence, permissions, safety controls, and verification mechanisms improve.

## Product Principles

### Local First

User data should remain on the user's machine whenever technically practical.

Cloud services are optional extensions rather than fundamental requirements.

### Evidence Before Assertion

Gold Apple must distinguish between:

- observed facts
- inferred conclusions
- hypotheses
- recommendations
- executed actions

### Read Before Write

The system begins primarily as an observer.

Write capabilities are introduced progressively and must be controlled by permissions and safety policies.

### Reversible Operations

Where practical, Gold Apple should prefer operations that can be rolled back.

### Security by Design

Security is an architectural requirement, not an afterthought.

### Explainability

Important diagnoses and actions should contain evidence showing how the conclusion was reached.

### User Sovereignty

The user owns:

- their data
- their project knowledge
- their machine
- their history
- their configuration
- their AI provider choices

## Gold Apple Systems

### GoldenCore

The central orchestration and reasoning system.

Responsibilities include:

- task decomposition
- capability orchestration
- permission enforcement
- evidence aggregation
- planning
- action coordination
- verification

### GoldenGraph

The machine knowledge graph.

Represents entities and relationships such as:

- repositories
- files
- modules
- services
- processes
- dependencies
- commits
- developers
- containers
- ports
- APIs
- databases
- environments
- configuration
- incidents

### GoldenEye

Observability and diagnostic intelligence.

Responsible for understanding:

- logs
- processes
- resource utilization
- services
- crashes
- runtime state
- network activity
- system events

### GoldenGit

Repository and software-history intelligence.

Responsible for:

- Git analysis
- branch relationships
- commit history
- regression investigation
- change attribution
- release history
- dependency-change correlation

### GoldenShield

Security intelligence.

Responsible for:

- secret detection
- dependency risk
- vulnerability information
- configuration weaknesses
- permissions
- attack-surface visibility
- security recommendations

### GoldenForge

Build and delivery intelligence.

Responsible for:

- builds
- tests
- packaging
- CI/CD
- release readiness
- deployment workflows
- build diagnostics

### GoldenMemory

Durable knowledge and historical intelligence.

Stores:

- architectural decisions
- previous incidents
- successful fixes
- user-approved knowledge
- project history
- system observations
- operational patterns

### GoldenLab

Safe experimentation environments.

Used for:

- dependency upgrades
- migrations
- refactors
- patches
- configuration changes
- reproduction environments
- potentially destructive experimentation

before applying changes to the actual system.

## Initial Platform

The first development target is macOS.

The architecture should remain portable enough for future Linux and Windows support.

## Initial Product Strategy

Gold Apple will initially operate in read-only mode.

Phase one focuses on:

1. discovering the local computing environment
2. indexing software projects
3. understanding Git repositories
4. constructing the knowledge graph
5. correlating development information
6. answering questions using evidence

Autonomous modification comes later.

## Project Status

Pre-development architecture and product specification.

No production implementation should begin until the Phase 0 architecture, security, data, permission, and MVP decisions have been reviewed.

## Documentation

See `/docs` for product and engineering specifications.

See `/specs` for individual subsystem specifications.

See `AGENTS.md` for repository-specific AI engineering instructions.

## Working Philosophy

Gold Apple should not merely tell the user that something is broken.

It should ultimately be able to explain:

- what changed
- what failed
- when it failed
- why it likely failed
- what else is affected
- how confident the diagnosis is
- how the problem can be reproduced
- what solutions exist
- what risks each solution carries
- how a proposed solution was verified

That is the standard against which the system should be designed.
