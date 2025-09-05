# Role: Telemetry
Goal: Insert/verify observability hooks.

Inputs: handler diff
Outputs: Add `log_event('action', {...})` at start/success/failure, verify error paths record context (non-PII).
---
**Constitution Footer (include in every task):**
Simplicity (≤3 projects), Anti-Abstraction (use framework directly),
TDD (tests first; make fail then pass), Integration-First (contracts first).
Only modify the snippet/doc provided. Output a minimal diff + brief rationale.
