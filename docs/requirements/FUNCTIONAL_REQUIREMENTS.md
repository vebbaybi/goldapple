# Functional Requirements

| ID | Requirement | MVP | Verification |
| --- | --- | --- | --- |
| GA-FR-001 | The client shall require explicit workspace authorization before discovery. | Yes | integration |
| GA-FR-002 | The system shall operate in limited mode when VS Code Workspace Trust is absent. | Yes | integration |
| GA-FR-003 | Discovery shall remain within canonical authorized roots. | Yes | security |
| GA-FR-004 | The system shall ingest supported Git, manifest, diagnostic, and approved output evidence. | Yes | contract |
| GA-FR-005 | Each material finding shall cite one or more evidence records. | Yes | acceptance |
| GA-FR-006 | Findings shall distinguish observations, inferences, hypotheses, and recommendations. | Yes | acceptance |
| GA-FR-007 | External model transmission shall require configured provider consent and minimization. | Yes | privacy |
| GA-FR-008 | Durable memory shall require explicit user approval and support deletion. | Yes | lifecycle |
| GA-FR-009 | Investigations shall disclose unavailable or conflicting evidence. | Yes | acceptance |
| GA-FR-010 | Users shall be able to export an investigation with provenance and redaction. | V1 | integration |
