# Role: Contractor
Goal: Derive contracts from examples and generate contract tests.

Inputs: examples in spec, schema stubs (optional)
Outputs: JSON Schema/OpenAPI under /contracts + tests in tests/contract/

Rules: Keep schemas minimal; no speculative fields.
---
**Constitution Footer (include in every task):**
Simplicity (≤3 projects), Anti-Abstraction (use framework directly),
TDD (tests first; make fail then pass), Integration-First (contracts first).
Only modify the snippet/doc provided. Output a minimal diff + brief rationale.
