# Traceability Matrix

+All rows are **NOT IMPLEMENTED — FOUNDATION ONLY**. IDs become immutable once implementation begins.

| Requirement | Story | Feature | Scenario | Component | Test | Security control | Release gate |
| --- | --- | --- | --- | --- | --- | --- | --- |
| GA-FR-001 | GA-US-001 | Workspace consent | GA-SCN-001 authorize root | VSIX/Permission | integration | explicit scope | MVP-G1 |
| GA-FR-002 | GA-US-001 | Restricted mode | GA-SCN-002 untrusted workspace | VSIX | security | Workspace Trust | MVP-G1 |
| GA-FR-003 | GA-US-002 | Discovery | GA-SCN-003 symlink escape | Discovery | abuse | canonical containment | MVP-G2 |
| GA-FR-004 | GA-US-003 | Evidence adapters | GA-SCN-004 regression fixture | Git/Forge/Eye | contract | parser isolation | MVP-G2 |
| GA-FR-005 | GA-US-004 | Cited findings | GA-SCN-005 inspect citation | Core/Evidence | acceptance | provenance | MVP-G3 |
| GA-FR-006 | GA-US-004 | Epistemic labels | GA-SCN-006 uncertain cause | Core | calibration | honesty policy | MVP-G3 |
| GA-FR-007 | GA-US-005 | Provider boundary | GA-SCN-007 secret canary | Gateway | privacy | preview/redaction | MVP-G4 |
| GA-FR-008 | GA-US-006 | Approved memory | GA-SCN-008 delete knowledge | Memory | lifecycle | consent/retention | MVP-G4 |

Maintenance: every requirement change updates its story, feature scenario, component contract, test design, control, release gate, and affected `gaxyz` claim in the same review.
