# Non-Functional Requirements

| ID | Requirement | Target / gate |
| --- | --- | --- |
| GA-NFR-001 | No silent external transmission | invariant; privacy test |
| GA-NFR-002 | Local runtime IPC is authenticated and versioned | security test before MVP |
| GA-NFR-003 | Cancellation reaches long-running discovery promptly | target defined after prototype benchmark |
| GA-NFR-004 | Corrupt or missing evidence degrades explicitly | fault-injection test |
| GA-NFR-005 | Core flows meet WCAG 2.2 AA | audit before V1 |
| GA-NFR-006 | Supported macOS and VS Code versions are release-tested | matrix before release |
| GA-NFR-007 | Logs exclude secrets and raw sensitive content by default | canary test |
| GA-NFR-008 | Local data schema supports forward migration and tested rollback/backup | migration gate |
