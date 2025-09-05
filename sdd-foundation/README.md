# SDD Foundation

Single source of truth for:
- Constitution (Articles I–IX)
- Reusable prompts for multi-agent workflow
- Reusable GitHub Actions workflows (via `workflow_call`)
- Helper scripts (specify/plan/tasks wrappers, adoption & utilities)

## Versioning
Tag releases `v1`, `v1.1`, etc. Consumer repos should pin to a tag in `uses:` blocks.

---
## Guardrails: simple • secure • efficient • token-aware
- **Simple**: one reusable workflow `quality-gate.yml` bundles QoS + OPA; jobs are short and tool-backed.
- **Secure**: Schemathesis uses `${{ secrets.SCHEMA_AUTH_HEADER }}` if present; no secrets in repo.
- **Efficient**: agents operate on diffs/files via MCP stubs; CI reads JSON artifacts instead of code.
- **Token-aware**: prompts are phase- and diff-scoped; `token_ledger.py` records usage per feature.
