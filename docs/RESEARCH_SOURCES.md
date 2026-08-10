# Phase 0 Research Sources

Research was performed on 2026-08-10. These links are supporting context; repository requirements and ADRs remain authoritative.

- [VS Code Workspace Trust extension guide](https://code.visualstudio.com/api/extension-guides/workspace-trust) — supports limited behavior in Restricted Mode and explicit gating through `workspace.isTrusted`.
- [VS Code extension runtime security](https://code.visualstudio.com/docs/configure/extensions/extension-runtime-security) — informs publisher trust, secret scanning, signatures, and extension risk.
- [SQLite Write-Ahead Logging](https://sqlite.org/wal.html) — informs the proposed local persistence and concurrency review; mode and backup behavior require prototype testing.
- [OpenAI API data controls](https://platform.openai.com/docs/models/default-usage-policies-by-endpoint) — demonstrates that retention and storage vary by endpoint and organization control, so provider capability metadata and user disclosure cannot be hardcoded assumptions.
- [Base documentation](https://docs.base.org/get-started/base) — supports research familiarity only; it does not establish a decision to deploy on Base.

No market-size statistics, legal conclusions, performance claims, or release claims were derived from research.
