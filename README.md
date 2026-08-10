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

Today, Codex should **not start building Golden Apple features**.

Its first job should be to turn the entire vision into a **development-grade foundation repository** that another senior engineer could clone, read, understand, validate, and begin implementing without guessing what Golden Apple is supposed to become.

The rule for Phase 0 should be:

> **Document the complete destination. Architect for the destination. Scope implementation around V1. Scope delivery around the MVP. Do not prematurely implement future systems.**

That distinction matters.

Golden Apple may eventually become a Web3-enabled developer intelligence platform, agent protocol, marketplace, Proof of Useful Work network, and crypto economy. But the **first shipped product is Golden Apple VSIX**, and inside V1 there must be an even smaller **MVP**.

## What Codex should accomplish today

By the end of this foundation phase, the repository should contain six things:

1. a complete product definition
2. an approved architecture
3. a complete engineering and operational doctrine
4. a traceable V1 and MVP specification
5. a comprehensive testing and security strategy
6. future Web3/network architecture documented without contaminating MVP implementation

No placeholder nonsense like:

> "Implement authentication later."

Instead:

> Authentication is required for V1. MVP uses mechanism X. Device registration follows Y. Token handling follows Z. Repository contents remain local unless permission P is granted.

That level of precision.

---

# 1. Codex first audits the repository

Before changing anything, Codex should inspect:

* current README
* existing files
* current Git history
* branches
* `.gitignore`
* licenses
* package files
* existing docs
* existing architecture
* existing CI
* current repository status
* existing secrets or unsafe committed material
* duplicate or contradictory documentation

Then produce:

`docs/audits/FOUNDATION_AUDIT.md`

It should explicitly state:

* what already exists
* what is usable
* what is incomplete
* what conflicts
* what needs restructuring
* what must not be destroyed
* what assumptions were made

No broad deleting or rewriting simply because Codex prefers a different layout.

---

# 2. Establish the Golden Apple doctrine

Create a small group of documents that sit above everything else.

## `VISION.md`

This defines the final destination.

It should cover:

* developer/computing intelligence
* local-first operation
* evidence-based reasoning
* machine understanding
* safe autonomous operation
* Golden Agent Protocol
* future Web3 network
* agent marketplace
* Proof of Useful Work
* agent ownership
* provenance
* reputation
* developer earnings
* token-enabled economy
* The 1807 platform economics
* long-term multi-platform runtime

This document is not restricted to V1.

---

## `PRODUCT_PRINCIPLES.md`

Codex should formalize principles such as:

* Local First
* Evidence Before Assertion
* Read Before Write
* Least Privilege
* Explicit Authorization
* Reversible Operations
* Verify Before Declaring Success
* User Sovereignty
* Provider Independence
* No Silent Cloud Upload
* No Unverifiable Diagnosis
* Secure by Default
* Blockchain Only Where Useful
* No Token-Driven Product Decisions
* Graceful Degradation
* Observable Operations
* Reproducibility
* Traceability

These become engineering constraints.

---

## `GLOSSARY.md`

Very important.

Define exactly what we mean by:

* Golden Apple
* GoldenCore
* GoldenGraph
* GoldenEye
* GoldenGit
* GoldenShield
* GoldenForge
* GoldenMemory
* GoldenLab
* Golden Runtime
* Golden Agent
* Golden Agent Protocol
* Golden Apple Network
* Work Receipt
* Proof of Useful Work
* Agent Identity
* Publisher
* Evidence
* Observation
* Inference
* Hypothesis
* Action
* Verification
* Workspace
* Project
* Machine
* Device
* Local data
* Cloud data

Without a glossary, terminology will drift.

---

# 3. Define complete scope, then separate MVP from V1

Codex should create:

`docs/product/FULL_PRODUCT_SCOPE.md`

This describes everything Golden Apple could eventually become.

Then:

`docs/product/V1_SCOPE.md`

Then:

`docs/product/MVP_SCOPE.md`

And:

`docs/product/OUT_OF_SCOPE.md`

That gives us four layers.

## Full product

Includes:

* VS Code
* CLI
* native runtime
* macOS
* Windows
* Linux
* system observation
* Git intelligence
* diagnostics
* security
* build intelligence
* safe actions
* sandboxing
* agent SDK
* marketplace
* Web3 network
* Proof of Useful Work
* crypto economy

## V1

V1 should remain substantially smaller.

I would currently define V1 around:

* VSIX
* local Golden runtime
* account authentication
* workspace authorization
* repository discovery
* Git intelligence
* project structure analysis
* dependency discovery
* diagnostics ingestion
* terminal/build/test failure capture
* evidence correlation
* question/investigation interface
* project memory
* permissions
* local storage
* OpenAI model integration
* provider abstraction
* basic cloud account API
* security boundaries
* audit trail

## MVP

The MVP should prove one central promise:

> **Golden Apple understands a VS Code project well enough to investigate a development failure and produce an evidence-backed explanation.**

MVP should therefore concentrate on:

* install `.vsix`
* authenticate
* authorize workspace
* inspect repository
* inspect Git
* understand project structure
* inspect dependencies
* receive VS Code diagnostics
* consume approved terminal/test/build output
* construct local project context
* ask Golden Apple a question
* correlate evidence
* produce diagnosis
* cite evidence
* express confidence
* distinguish fact/inference/hypothesis
* remember approved project knowledge

No autonomous fixing in the MVP.

That is an excellent first product.

---

# 4. User documentation

Codex should identify all major users.

Create:

`docs/product/PERSONAS.md`

At minimum:

* individual developer
* student developer
* senior engineer
* maintainer
* DevOps/platform engineer
* security engineer
* development team
* agent developer, future
* marketplace publisher, future
* marketplace customer, future

Then:

`docs/product/USER_JOURNEYS.md`

and:

`docs/product/USER_STORIES.md`

The stories should not be random aspirational statements.

Every MVP story should eventually map into an executable feature.

Example relationship:

```text
US-GIT-004
    ↓
features/git/regression_analysis.feature
    ↓
Scenario IDs
    ↓
steps
    ↓
implementation capability
    ↓
automated tests
```

---

# 5. Requirements system

Create:

`docs/requirements/FUNCTIONAL_REQUIREMENTS.md`

`docs/requirements/NON_FUNCTIONAL_REQUIREMENTS.md`

`docs/requirements/SECURITY_REQUIREMENTS.md`

`docs/requirements/PRIVACY_REQUIREMENTS.md`

`docs/requirements/PERFORMANCE_REQUIREMENTS.md`

`docs/requirements/RELIABILITY_REQUIREMENTS.md`

`docs/requirements/ACCESSIBILITY_REQUIREMENTS.md`

`docs/requirements/COMPATIBILITY_REQUIREMENTS.md`

`docs/requirements/COMPLIANCE_REQUIREMENTS.md`

Each requirement should have an ID.

For example:

`GA-FR-001`

`GA-SEC-014`

`GA-NFR-021`

That allows traceability.

---

# 6. System architecture

This should be one of the largest areas.

Codex should create:

`docs/architecture/SYSTEM_ARCHITECTURE.md`

Cover:

```text
VS Code Extension
        │
        ▼
Local Communication Layer
        │
        ▼
Golden Runtime
        │
        ├── GoldenCore
        ├── GoldenGraph
        ├── GoldenGit
        ├── GoldenEye
        ├── GoldenShield
        ├── GoldenForge
        └── GoldenMemory
        │
        ▼
Model Gateway
```

And separately:

```text
Golden Apple Account Platform
        │
        ├── Identity
        ├── Devices
        ├── Subscription
        ├── Provider configuration
        └── Optional synchronization
```

Then future architecture:

```text
Golden Agent Protocol
        │
        ▼
Golden Apple Network
        │
        ├── Agent Registry
        ├── Work Receipts
        ├── Reputation
        ├── Marketplace
        ├── Settlement
        └── Token
```

---

# 7. Architecture Decision Records

Create `/docs/adr/`.

Codex should start ADRs for decisions including:

* ADR-001 Monorepo
* ADR-002 TypeScript for VSIX
* ADR-003 Python intelligence runtime
* ADR-004 Rust native runtime boundary
* ADR-005 PostgreSQL cloud database
* ADR-006 SQLite local persistence
* ADR-007 local-first architecture
* ADR-008 OpenAI-first provider-independent model gateway
* ADR-009 GitHub Actions CI/CD
* ADR-010 Base/EVM Web3 direction
* ADR-011 Solidity smart contracts
* ADR-012 blockchain-selective architecture
* ADR-013 Web3 not required for MVP
* ADR-014 VSIX before native application
* ADR-015 Golden Apple as first Golden Agent implementation

These are decisions, not marketing documents.

---

# 8. Detailed subsystem specifications

Create `/specs`.

Each subsystem gets its own contract.

For example:

```text
specs/
    golden-core.md
    golden-graph.md
    golden-eye.md
    golden-git.md
    golden-shield.md
    golden-forge.md
    golden-memory.md
    golden-lab.md
    model-gateway.md
    permissions.md
    evidence-system.md
    local-runtime.md
    vscode-client.md
```

Each should define:

* responsibility
* inputs
* outputs
* interfaces
* failure modes
* trust assumptions
* persistence
* observability
* security
* tests
* MVP relevance
* V1 relevance
* future relevance

---

# 9. Data architecture

Create:

`docs/data/DATA_ARCHITECTURE.md`

`docs/data/DATA_CLASSIFICATION.md`

`docs/data/LOCAL_STORAGE.md`

`docs/data/CLOUD_STORAGE.md`

`docs/data/RETENTION_POLICY.md`

`docs/data/SCHEMA_STRATEGY.md`

`docs/data/MIGRATION_STRATEGY.md`

`docs/data/BACKUP_RECOVERY.md`

Golden Apple could touch extremely sensitive information.

Every data class should be classified.

For example:

* public
* project internal
* sensitive
* secret
* credential
* personal
* cryptographic
* ephemeral

Codex should explicitly specify what Golden Apple **must never persist**.

---

# 10. GoldenGraph specification

Create:

`docs/architecture/GOLDEN_GRAPH.md`

Define entities like:

* machine
* workspace
* repository
* file
* symbol
* dependency
* commit
* branch
* service
* process
* port
* container
* build
* test
* failure
* incident
* configuration
* environment
* developer
* agent
* evidence

And relationships between them.

This is foundational to Golden Apple's intelligence.

---

# 11. Evidence and reasoning architecture

This is one of the most important documents.

Create:

`docs/ai/EVIDENCE_MODEL.md`

Golden Apple must differentiate:

```text
OBSERVED
INFERRED
HYPOTHESIS
RECOMMENDATION
PROPOSED_ACTION
EXECUTED_ACTION
VERIFIED_RESULT
```

Every important diagnosis should have:

* evidence source
* timestamp
* confidence
* provenance
* relationship to conclusion
* verification status

Also create:

`docs/ai/REASONING_POLICY.md`

Not chain-of-thought.

This defines the **product-level reasoning behavior**.

---

# 12. AI architecture

Create:

`docs/ai/AI_ARCHITECTURE.md`

`docs/ai/MODEL_GATEWAY.md`

`docs/ai/CONTEXT_ENGINEERING.md`

`docs/ai/TOOL_SYSTEM.md`

`docs/ai/MEMORY_POLICY.md`

`docs/ai/HALLUCINATION_CONTROLS.md`

`docs/ai/PROVIDER_ABSTRACTION.md`

`docs/ai/AI_SAFETY_BOUNDARIES.md`

Golden Apple should never simply feed an entire repository into an LLM.

Codex should define context selection, retrieval, evidence packaging and token-budget behavior.

---

# 13. VSIX specification

Create:

`docs/platform/VSIX_PRODUCT_SPEC.md`

And:

`docs/platform/VSIX_ARCHITECTURE.md`

Define:

* activation
* authentication
* workspace consent
* command palette actions
* sidebar
* investigation view
* evidence view
* project view
* status bar
* diagnostic integration
* terminal boundaries
* notifications
* permissions UI
* settings
* error handling
* telemetry consent
* local runtime lifecycle
* extension updates

This is our first actual product.

---

# 14. Security foundation

Codex needs to behave like a security engineer here.

Create:

`docs/security/THREAT_MODEL.md`

`docs/security/SECURITY_ARCHITECTURE.md`

`docs/security/PERMISSION_MODEL.md`

`docs/security/TRUST_BOUNDARIES.md`

`docs/security/SECRET_HANDLING.md`

`docs/security/SECURE_STORAGE.md`

`docs/security/SUPPLY_CHAIN_SECURITY.md`

`docs/security/INCIDENT_RESPONSE.md`

`docs/security/VULNERABILITY_MANAGEMENT.md`

`SECURITY.md`

Threats should include:

* malicious repositories
* prompt injection embedded in code
* poisoned README/instructions
* dependency attacks
* command injection
* symlink attacks
* path traversal
* malicious terminal output
* stolen API keys
* compromised extensions
* compromised agents
* poisoned memory
* model exfiltration attempts
* malicious MCP/tool responses
* privilege escalation
* insecure localhost APIs
* Web3 wallet attacks
* smart contract attacks

---

# 15. Git culture

Codex should define the repository's Git doctrine.

Create:

`docs/engineering/GIT_WORKFLOW.md`

Include:

* protected `main`
* feature branches
* conventional commit policy
* PR requirements
* required reviews later
* required status checks
* merge strategy
* release branches if needed
* hotfix policy
* rollback
* signed releases
* tags
* versioning
* changelog
* branch cleanup

Also:

`CONTRIBUTING.md`

`CODE_OF_CONDUCT.md`

`CHANGELOG.md`

---

# 16. Development engineering culture

Create:

`docs/engineering/DEVELOPMENT_PROCESS.md`

Define:

```text
Requirement
    ↓
User Story
    ↓
BDD Feature
    ↓
Architecture / ADR
    ↓
Implementation
    ↓
Unit Tests
    ↓
Integration Tests
    ↓
Security Validation
    ↓
Acceptance
    ↓
Release Evidence
```

Codex should not implement functionality lacking traceability.

---

# 17. Database engineering culture

Create:

`docs/database/DATABASE_ENGINEERING.md`

Cover:

* migrations
* schema ownership
* migration reviews
* forward migrations
* rollback strategy
* test databases
* seed policy
* production migration safety
* indexing
* constraints
* foreign keys
* data validation
* backups
* disaster recovery
* retention
* observability
* connection management

---

# 18. Testing doctrine

This deserves a full hierarchy.

Create:

`docs/testing/TEST_STRATEGY.md`

Cover:

* unit
* property
* contract
* integration
* BDD
* system
* end-to-end
* security
* performance
* regression
* compatibility
* migration
* recovery
* fuzzing
* smart-contract testing
* release acceptance

Also:

`docs/testing/BDD_STRATEGY.md`

`docs/testing/TEST_DATA_POLICY.md`

`docs/testing/COVERAGE_POLICY.md`

`docs/testing/RELEASE_ACCEPTANCE.md`

Golden Apple should have **quality gates**, not merely coverage percentages.

---

# 19. Initial feature files

Codex should establish the BDD structure, but not fabricate functionality.

Something like:

```text
features/
    authentication/
    workspace/
    repository/
    git/
    diagnostics/
    investigations/
    evidence/
    memory/
    permissions/
    security/
```

These should correspond only to MVP/V1 behavior currently specified.

Future Web3 scenarios can live separately as specifications and remain tagged appropriately.

---

# 20. DevSecOps

Create:

`docs/operations/DEVSECOPS.md`

The pipeline should eventually include:

* formatting
* lint
* type checking
* unit tests
* integration tests
* BDD tests
* secret scanning
* SAST
* dependency scanning
* container scanning
* license scanning
* SBOM
* artifact signing
* provenance
* packaging
* release gates

---

# 21. CI/CD

Create:

`docs/operations/CI_CD.md`

And establish GitHub Actions foundations for the repository structure, even if many packages do not exist yet.

No fake green checks.

Only runnable checks for existing components.

Future checks get documented rather than pretending to execute.

---

# 22. Shipping and release engineering

Create:

`docs/release/RELEASE_STRATEGY.md`

`docs/release/VERSIONING.md`

`docs/release/ARTIFACT_POLICY.md`

`docs/release/ROLLBACK.md`

`docs/release/RELEASE_CHECKLIST.md`

Eventually artifacts include:

* VSIX
* Python runtime
* Rust binaries
* Docker images
* smart-contract artifacts
* hashes
* SBOM
* signatures
* provenance

---

# 23. Observability

Create:

`docs/operations/OBSERVABILITY.md`

Golden Apple needs to observe itself.

Define:

* logs
* metrics
* traces
* errors
* correlation IDs
* investigation IDs
* local telemetry
* optional remote telemetry
* privacy boundaries
* performance metrics
* failure metrics

---

# 24. Web3 architecture

This should be documented seriously now.

Create:

```text
docs/web3/
    NETWORK_VISION.md
    WEB3_ARCHITECTURE.md
    GOLDEN_AGENT_PROTOCOL.md
    AGENT_IDENTITY.md
    AGENT_REGISTRY.md
    AGENT_PROVENANCE.md
    AGENT_REPUTATION.md
    PROOF_OF_USEFUL_WORK.md
    WORK_RECEIPTS.md
    MARKETPLACE.md
    MARKETPLACE_ECONOMICS.md
    WALLET_ARCHITECTURE.md
    SMART_ACCOUNT_STRATEGY.md
    SMART_CONTRACT_ARCHITECTURE.md
    ONCHAIN_OFFCHAIN_BOUNDARIES.md
    TOKEN_UTILITY.md
    TOKENOMICS.md
    TREASURY.md
    REWARD_SYSTEM.md
    STAKING_MODEL.md
    SYBIL_RESISTANCE.md
    GOVERNANCE.md
    WEB3_SECURITY.md
    WEB3_THREAT_MODEL.md
    WEB3_TEST_STRATEGY.md
    NETWORK_ROADMAP.md
```

But these documents should clearly say:

**Future architecture, not MVP implementation.**

---

# 25. Golden Agent Protocol

This deserves its own specification.

Every future Golden Agent should eventually declare:

* immutable identity
* publisher
* version
* capabilities
* permissions
* tool access
* model requirements
* filesystem access
* network access
* memory behavior
* expected inputs
* outputs
* evidence model
* verification strategy
* resource limits
* dependencies
* runtime compatibility
* pricing
* provenance
* signatures
* reputation
* security classification

Golden Apple itself becomes the first reference implementation.

---

# 26. Proof of Useful Work

This should become a serious protocol document rather than cryptocurrency terminology.

Codex should define:

```text
Task
 ↓
Execution
 ↓
Evidence
 ↓
Verification
 ↓
Work Receipt
 ↓
Cryptographic Commitment
 ↓
Settlement / Reputation
```

And answer:

* what counts as work
* what makes work useful
* who verifies
* how verification is challenged
* how duplicate work is handled
* how fake work is prevented
* how reward farming is prevented
* privacy
* disputes
* reputation
* economic settlement

---

# 27. Token documentation

Even though we intend to work on the platform token, Codex should **design before deploy**.

Documents:

`TOKEN_UTILITY.md`

`TOKENOMICS.md`

`TOKEN_LIFECYCLE.md`

`TOKEN_RISK_ANALYSIS.md`

`TREASURY_POLICY.md`

`DISTRIBUTION_POLICY.md`

`ECONOMIC_ATTACKS.md`

`MARKETPLACE_SETTLEMENT.md`

`REWARD_EMISSIONS.md`

No arbitrary token supply.

No "1 billion because crypto projects use 1 billion."

Every parameter needs a rationale.

---

# 28. Golden Apple White Paper

Absolutely.

I would make this a major document:

`WHITEPAPER.md`

This is not supposed to be a marketing brochure.

It should eventually contain:

1. Abstract
2. Problem
3. Motivation
4. Golden Apple vision
5. Developer intelligence problem
6. Local-first architecture
7. Golden Apple architecture
8. Golden Agent model
9. Evidence architecture
10. Trust and permissions
11. Golden Agent Protocol
12. Golden Apple Network
13. Proof of Useful Work
14. Work Receipts
15. Agent provenance
16. Reputation
17. Marketplace
18. Token utility
19. Network economics
20. Treasury
21. Security
22. Privacy
23. Governance
24. Development phases
25. Risks and limitations
26. Future research
27. Conclusion

There should also eventually be a rendered PDF version, but Markdown should remain the authoritative editable source.

---

# 29. Business documents

Technical architecture alone is insufficient.

Create:

`docs/business/BUSINESS_MODEL.md`

`docs/business/MONETIZATION.md`

`docs/business/PRICING_STRATEGY.md`

`docs/business/MARKETPLACE_ECONOMICS.md`

`docs/business/COMPETITIVE_POSITIONING.md`

`docs/business/GO_TO_MARKET.md`

`docs/business/PLATFORM_STRATEGY.md`

`docs/business/NETWORK_EFFECTS.md`

`docs/business/RISK_REGISTER.md`

The business model must distinguish:

* Golden Apple subscription revenue
* hosted AI revenue/costs
* marketplace fees
* future agent services
* token/network economics
* treasury
* developer payouts

---

# 30. Legal and governance planning

Without pretending Codex is a lawyer, it can document what needs professional review.

Create:

`docs/governance/LEGAL_REVIEW_REGISTER.md`

Cover:

* privacy
* developer source code
* AI outputs
* marketplace licensing
* agent liability
* intellectual property
* crypto assets
* marketplace payouts
* token classification
* tax
* custody
* KYC/AML possibility
* sanctions
* consumer protection
* jurisdiction

Anything unresolved gets explicitly marked **requires legal counsel**.

---

# 31. Roadmap

Create:

`ROADMAP.md`

But make it capability-based.

I see something like:

```text
Phase 0
Foundation

Phase 1
VSIX MVP

Phase 2
VSIX V1 Developer Intelligence

Phase 3
Controlled Actions

Phase 4
Golden Native Runtime

Phase 5
Cross-System Intelligence

Phase 6
Golden Agent Protocol

Phase 7
Agent SDK

Phase 8
Golden Apple Network

Phase 9
Marketplace

Phase 10
Proof of Useful Work Economy

Phase 11
Progressive Decentralization
```

Not dates Codex invents.

---

# 32. Traceability matrix

This is one of the strongest things Codex can create.

`docs/TRACEABILITY_MATRIX.md`

Every important V1 requirement maps:

```text
Requirement
→ User Story
→ Feature
→ Scenario
→ Component
→ Test
→ Security Control
→ Release Gate
```

This prevents documentation drift.

---

# 33. Project governance

Create:

`AGENTS.md`

This becomes the engineering constitution for AI agents working on Golden Apple.

It should instruct Codex and future agents to:

* inspect before modifying
* never claim validation not performed
* avoid placeholders disguised as implementations
* preserve evidence
* follow architecture
* use feature branches
* maintain traceability
* test changes
* run security checks
* update correlated documentation
* never silently weaken security
* never bypass tests
* never fabricate dependencies
* never commit secrets
* avoid unnecessary frameworks
* respect local-first requirements
* distinguish MVP/V1/future scope
* use ADRs for architectural changes

This document matters enormously because Mr Golden Apple will repeatedly operate inside this repository.

---

# 34. Repository structure

After foundation work, I would expect something roughly like:

```text
gold-apple/
├── README.md
├── WHITEPAPER.md
├── VISION.md
├── PRODUCT_PRINCIPLES.md
├── ROADMAP.md
├── GLOSSARY.md
├── AGENTS.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
│
├── apps/
│   ├── vscode/
│   └── web/
│
├── services/
│   ├── intelligence/
│   └── api/
│
├── crates/
│   └── golden-runtime/
│
├── packages/
│   ├── shared-types/
│   └── agent-protocol/
│
├── contracts/
│
├── features/
│
├── tests/
│
├── specs/
│
├── docs/
│   ├── product/
│   ├── requirements/
│   ├── architecture/
│   ├── adr/
│   ├── ai/
│   ├── data/
│   ├── database/
│   ├── security/
│   ├── testing/
│   ├── engineering/
│   ├── operations/
│   ├── release/
│   ├── platform/
│   ├── web3/
│   ├── business/
│   ├── governance/
│   └── audits/
│
└── .github/
    ├── workflows/
    ├── ISSUE_TEMPLATE/
    └── PULL_REQUEST_TEMPLATE.md
```

Empty architecture directories should not be populated with fake implementations merely to make the tree look impressive.

---

# What Codex should NOT do today

It should **not**:

* build GoldenCore
* implement smart contracts
* deploy a token
* write marketplace contracts
* create fake APIs
* scaffold 15 microservices
* add Kubernetes
* create meaningless Docker infrastructure
* introduce Neo4j just because GoldenGraph exists
* create browser extensions
* build desktop applications
* claim security verification without running it
* invent test results
* create hundreds of useless BDD scenarios
* implement future agents
* add random AI frameworks
* produce AI-generated corporate filler

The goal today is **foundation quality, not repository size**.

---

# The standard I would set for Mr Golden Apple

Codex should approach this repository simultaneously as:

**Product Architect**
Understands who Golden Apple serves and why.

**Software Architect**
Defines boundaries, contracts and dependency directions.

**AI Systems Engineer**
Designs model usage, context, evidence, tools and memory.

**Security Engineer**
Treats untrusted repositories, prompts, processes and agents as hostile inputs.

**Database Engineer**
Designs persistence and lifecycle intentionally.

**Git Engineer**
Maintains disciplined history and branch practices.

**DevOps Engineer**
Builds reproducible development and CI environments.

**DevSecOps Engineer**
Makes security part of delivery.

**QA Engineer**
Establishes traceability and testing layers.

**Release Engineer**
Defines how artifacts become trusted releases.

**Web3 Architect**
Understands contracts, wallets, provenance, settlement and network security.

**Protocol Designer**
Designs Golden Agents and Proof of Useful Work independently from implementation hype.

**Operations Engineer**
Plans observability, incidents, recovery and lifecycle operations.

**Technical Writer**
Makes all of those systems correlate.

The important part is that these are not separate piles of Markdown.

They form one chain:

> **Vision → Product → Requirements → Architecture → Security → Data → Stories → BDD → Implementation → Tests → CI → Release → Operations → Evidence**

And the future Web3 chain becomes:

> **Golden Agent Protocol → Identity → Work → Evidence → Verification → Work Receipt → Reputation → Marketplace → Settlement → Token Economy**

If we establish this properly first, **we will be able to start Golden Apple development from a controlled engineering baseline instead of discovering the architecture while writing the product.**

That is what I would make Mr Golden Apple accomplish in the first foundation pass.


For Golden Apple, I would lock the stack around **TypeScript + Python + PostgreSQL + Rust + Solidity**, with each language doing the job it is strongest at. VS Code officially recommends TypeScript for extension development, and its extension API gives us access to workspace state, commands, diagnostics, terminals, tree views and other editor surfaces we need for the first client. ([Visual Studio Code][1])

### Golden Apple core stack

| Layer                     | Technology                                                  | Role                                                      |
| ------------------------- | ----------------------------------------------------------- | --------------------------------------------------------- |
| VS Code client            | **TypeScript, Node.js, VS Code Extension API**              | First Golden Apple interface and `.vsix`                  |
| VSIX UI                   | **TypeScript + VS Code Webview API**                        | Golden Apple panel, investigations, evidence, permissions |
| Local intelligence        | **Python 3.13+**                                            | GoldenCore orchestration, reasoning, analysis, tools      |
| Local native/system layer | **Rust**                                                    | Secure OS/process/filesystem/CLI integration              |
| AI integration            | **OpenAI API initially, provider abstraction from day one** | Reasoning and tool use                                    |
| API backend               | **FastAPI + Pydantic**                                      | Golden Apple account/cloud APIs                           |
| Relational DB             | **PostgreSQL**                                              | users, projects, devices, subscriptions, metadata         |
| Local DB                  | **SQLite**                                                  | local project metadata, incidents, evidence, settings     |
| Vector/search             | **PostgreSQL + pgvector initially**                         | semantic project memory                                   |
| Graph intelligence        | **PostgreSQL graph-style model initially**                  | GoldenGraph                                               |
| Cache/jobs                | **Redis**                                                   | sessions, rate limiting, background queues                |
| Async workers             | **Celery or Dramatiq**                                      | cloud jobs, indexing, asynchronous analysis               |
| Auth                      | **OAuth 2.0 / OIDC + passkeys**                             | Golden Apple identity                                     |
| Containers                | **Docker**                                                  | reproducible services/tests                               |
| CI/CD                     | **GitHub Actions**                                          | tests, builds, VSIX packaging, releases                   |
| Observability             | **OpenTelemetry + Prometheus + structured logs**            | Golden Apple itself                                       |
| Web dashboard             | **Next.js + TypeScript**                                    | accounts, devices, billing, marketplace later             |
| Package management        | `npm/pnpm` + `pip`                                          | language-specific dependency management                   |

The actual `.vsix` should remain TypeScript because the VS Code Extension API is fundamentally a JavaScript API, and Microsoft specifically presents TypeScript as the preferred development experience. ([Visual Studio Code][2])

## Why Python stays important

I would **not** attempt to write the Golden Apple intelligence engine entirely in TypeScript.

Python should run:

**GoldenCore**

* reasoning orchestration
* investigation planning
* evidence correlation
* model adapters
* tool orchestration

**GoldenGit**

* repository analysis
* regression investigation
* dependency history
* commit correlation

**GoldenEye intelligence**

* log analysis
* diagnostics
* anomaly correlation

**GoldenShield intelligence**

* scanner orchestration
* findings correlation
* risk assessment

**GoldenForge**

* build/test analysis
* CI reasoning
* failure correlation

**GoldenMemory**

* retrieval
* embeddings
* incident knowledge
* architectural memory

The VSIX communicates with this local intelligence runtime instead of containing the entire brain.

That gives us:

```text
VS Code
   │
   ▼
Golden Apple VSIX
TypeScript
   │
   │ local IPC
   ▼
Golden Apple Local Runtime
Python
   │
   ├── GoldenCore
   ├── GoldenGraph
   ├── GoldenGit
   ├── GoldenEye
   ├── GoldenShield
   ├── GoldenForge
   └── GoldenMemory
```

Later, Rust sits underneath the Python layer where we need stronger control over the host machine.

## Why Rust

Rust becomes extremely useful once Golden Apple starts moving outside VS Code.

It can eventually handle:

* process inspection
* secure subprocess execution
* filesystem watchers
* sockets
* ports
* service inspection
* native daemon
* OS event collection
* sandbox boundaries
* credential storage integration
* resource monitoring
* IPC
* secure privilege separation

Eventually:

```text
VSIX / CLI / Desktop
        │
        ▼
   GoldenCore
     Python
        │
        ▼
 Golden Runtime
      Rust
        │
        ▼
 macOS / Windows / Linux
```

Python remains the intelligence layer.

Rust becomes the machine layer.

That separation is extremely appropriate for what Golden Apple is trying to become.

---

# AI stack

I would make Golden Apple **OpenAI-first, provider-independent**.

Meaning:

```text
GoldenCore
     │
     ▼
Model Gateway
     │
 ┌───┼──────────────┐
 │   │              │
OpenAI          Local Models
FIRST             LATER
                  │
             Other Providers
                  LATER
```

Golden Apple itself should own:

* context construction
* tool definitions
* permissions
* memory
* evidence
* investigation state
* model routing
* verification
* agent lifecycle

The LLM should **not own the application architecture**.

That means changing models later does not mean rewriting Golden Apple.

---

# GoldenGraph

This is one place where I would resist overengineering V1.

We do **not need Neo4j immediately**.

Start with PostgreSQL/SQLite representations for:

```text
Repository
 ├── contains → File
 ├── has → Commit
 ├── depends_on → Package
 ├── exposes → API
 └── executes → Service

Commit
 ├── modified → File
 ├── introduced → Dependency
 └── associated_with → Incident

Service
 ├── runs_as → Process
 ├── listens_on → Port
 ├── depends_on → Database
 └── emits → Log
```

Once GoldenGraph reaches genuinely graph-heavy workloads, we can evaluate Neo4j, Memgraph or another graph engine.

Do not add a graph database just because the subsystem is called `GoldenGraph`.

---

# Local communication

For V1:

**VSIX ↔ Golden Runtime**

I would use a local authenticated IPC/API layer.

Potentially:

```text
VSIX
 │
 ├── JSON-RPC
 │
 └── authenticated localhost channel
          │
          ▼
    Golden Runtime
```

Later we can move sensitive/native calls into Rust IPC.

Golden Apple must never leave an unauthenticated localhost administrative API exposed.

---

# Web platform

The web application is not Golden Apple's brain.

It is the **Golden Apple account/platform interface**.

I would use:

**Next.js + TypeScript**

for:

* account management
* device management
* subscription
* billing
* API usage
* security/session management
* model configuration
* project sync controls
* marketplace later
* developer dashboard later
* agent publishing later
* wallet linking later

Golden Apple should remain usable locally even when this web dashboard isn't open.

---

# Web3 stack

Here's where I think we can make a very clean technical decision.

### Chain

My current candidate would be:

**Base**

not Ethereum L1 for routine Golden Apple operations.

Base is EVM-compatible, provides smart contract and wallet infrastructure, and its current documentation explicitly includes agent-related development and agentic payment material. ([Base documentation][3])

We can prototype entirely on **Base Sepolia** before anything touches mainnet.

### Smart contracts

**Solidity**

Solidity remains the native choice for EVM-compatible smart contracts. ([Solidity Programming Language][4])

### Contract development

I would evaluate:

**Foundry**

for contract building, testing, fuzzing and deployment.

Then:

**OpenZeppelin Contracts**

for established ERC implementations and security primitives.

We should not manually reinvent ERC contracts.

### Web3 client

**viem**

for TypeScript blockchain interaction.

Then we can integrate wallet/account infrastructure into the Next.js platform.

### Wallet architecture

We need both:

**external wallets**
and eventually
**smart accounts / embedded onboarding**

Base currently documents an ERC-4337-compatible smart wallet architecture, which fits the longer-term possibility of hiding much of the ugly wallet UX from ordinary developers. ([Base documentation][5])

---

# What actually goes on-chain

Very little.

This is crucial.

### On-chain

Eventually:

* Agent identifier
* developer/publisher identity reference
* agent version hash
* provenance hash
* ownership
* licenses
* marketplace settlement
* work-receipt commitments
* reputation commitments
* staking
* rewards
* token transfers
* treasury activity

### Off-chain

Everything large or private:

* source code
* prompts
* model conversations
* terminal output
* repository content
* logs
* full work evidence
* AI models
* binaries
* agent packages
* vector embeddings
* private user data

The blockchain stores **proofs/references**, not someone's entire Git repository.

---

# Golden Agent stack

This should exist conceptually from V1 even though third-party agents come much later.

I would define a portable **Golden Agent Manifest**.

Something structurally equivalent to:

```text
Agent
 ├── identity
 ├── publisher
 ├── version
 ├── capabilities
 ├── permissions
 ├── tools
 ├── supported models
 ├── memory policy
 ├── network policy
 ├── filesystem policy
 ├── execution policy
 ├── evidence policy
 ├── verification policy
 ├── pricing policy
 └── provenance
```

Golden Apple itself implements that specification first.

Then later:

```text
Golden Apple
    │
    └── Golden Agent Protocol
              │
       ┌──────┼──────┐
       │      │      │
    Agent A Agent B Agent C
       │      │      │
       └──────┼──────┘
              │
        Marketplace
```

---

# Proof of Useful Work stack

I would **not create a new blockchain consensus mechanism**.

Golden Apple PoUW should be an application-level protocol.

For example:

```text
Agent receives task
        ↓
Work execution
        ↓
Evidence generated
        ↓
Verification performed
        ↓
Work Receipt
        ↓
Receipt hashed
        ↓
Commitment recorded on-chain
        ↓
Reputation / payment / reward
```

The actual evidence stays off-chain.

The chain receives something like:

```text
task hash
agent identity
publisher
result hash
verification hash
timestamp
work class
economic settlement
```

That gives us cryptographic provenance without spending absurd amounts of blockchain storage.

---

# Testing stack

Testing needs to be unusually aggressive because Golden Apple can eventually touch people's machines.

### Python

* `pytest`
* `pytest-asyncio`
* Hypothesis
* coverage.py

### TypeScript

* Vitest
* VS Code Extension Test Runner
* Playwright for web surfaces

### BDD

Keep **Behave** for Golden Apple user-level/system behavior.

That aligns well with:

```text
User Story
   ↓
Feature
   ↓
Scenario
   ↓
Step
   ↓
Automated Validation
```

### Smart contracts

* Foundry unit tests
* fuzz tests
* invariant tests
* fork tests
* static analysis
* Slither
* Echidna where appropriate

### Security

* Semgrep
* CodeQL
* Trivy
* Gitleaks
* dependency scanning
* SBOM generation
* smart-contract static analysis

---

# CI/CD

Stay with **GitHub Actions**.

Pipelines eventually become something like:

```text
PR
 │
 ├── Python lint/type/test
 ├── TypeScript lint/type/test
 ├── VSIX integration tests
 ├── Rust check/test
 ├── Solidity compile/test/fuzz
 ├── security scanning
 ├── secret scanning
 ├── dependency scanning
 ├── SBOM
 └── package validation
```

Main/release additionally produces:

```text
.vsix
Python runtime package
Rust runtime binaries
Docker images
Web deployment
Smart contract artifacts
checksums
provenance attestations
```

---

# Repository strategy

I strongly favour a **monorepo** initially.

Something conceptually like:

```text
gold-apple/
│
├── apps/
│   ├── vscode/
│   ├── web/
│   ├── cli/             future
│   └── desktop/         future
│
├── services/
│   ├── api/
│   ├── intelligence/
│   └── worker/
│
├── crates/
│   └── golden-runtime/
│
├── packages/
│   ├── agent-protocol/
│   ├── shared-types/
│   └── sdk/             future
│
├── contracts/
│   ├── registry/
│   ├── marketplace/
│   ├── work-receipts/
│   └── token/
│
├── features/
├── tests/
├── docs/
├── specs/
└── infrastructure/
```

Not because all of those components should be implemented now, but because the **architectural boundaries can exist before the components do**.

---

## The stack I'd lock today

If we had to freeze the core decisions before Mr Golden Apple touches the repo:

**Frontend / VSIX:** TypeScript
**Web:** Next.js
**Core AI:** Python
**Native systems:** Rust
**API:** FastAPI
**Database:** PostgreSQL
**Local storage:** SQLite
**Semantic retrieval:** pgvector
**Cache/queues:** Redis
**AI:** OpenAI-first abstraction
**Containers:** Docker
**CI/CD:** GitHub Actions
**Infrastructure:** Terraform later
**Telemetry:** OpenTelemetry
**Blockchain:** Base
**Contracts:** Solidity
**Contract tooling:** Foundry
**Web3 libraries:** viem
**Wallet standard:** EOA + ERC-4337-capable architecture later
**Testing:** pytest + Hypothesis + Vitest + Behave + Playwright + Foundry
**Security:** CodeQL + Semgrep + Trivy + Gitleaks + Slither
**Architecture:** local-first, cloud-optional, blockchain-selective.

And importantly, **no browser extension belongs in the foundational stack right now**. VSIX first. CLI/native runtime is the logical expansion. Browser integration should earn its place with a concrete use case.

This stack gives Golden Apple a realistic path from **one VS Code agent in 2026 to an actual agent platform and Web3 developer economy later**, without requiring us to rewrite the foundation when the marketplace arrives. ([Visual Studio Code][1])

[1]: https://code.visualstudio.com/api/references/vscode-api?utm_source=chatgpt.com "VS Code API | Visual Studio Code Extension API"
[2]: https://code.visualstudio.com/api/get-started/extension-anatomy?utm_source=chatgpt.com "Extension Anatomy"
[3]: https://docs.base.org/get-started/base?utm_source=chatgpt.com "Base Documentation"
[4]: https://www.soliditylang.org/?utm_source=chatgpt.com "Home | Solidity Programming Language"
[5]: https://docs.base.org/base-account/reference/onchain-contracts/smart-wallet?utm_source=chatgpt.com "Smart Wallet - Base Documentation"

