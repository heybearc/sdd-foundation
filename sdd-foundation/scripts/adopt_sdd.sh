#!/usr/bin/env bash
set -euo pipefail
echo "Adopting SDD into existing repo..."
mkdir -p base/memory .agent/prompts bin .github/workflows tests/contract tests/integration tests/e2e tests/unit contracts docs/adr specs policy .sdd
cat > .github/workflows/project-ci.yml <<'YAML'
name: project-ci
on: [push, pull_request]
jobs:
  spec-check:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/spec-check.yml@v1
  contracts:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/contracts.yml@v1
  tests:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/tests.yml@v1
  security:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/security.yml@v1
  cost:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/cost-report.yml@v1
  qos:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/qos.yml@v1
    with:
      qos_url: ""
      p95_budget_ms: 200
      bundle_budget_kb: 200
  opa:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/opa.yml@v1
  contracts-conformance:
    uses: {{YOUR_GH_USER}}/sdd-foundation/.github/workflows/contracts-conformance.yml@v1
    with:
      openapi_path: contracts/openapi.yaml
      base_url: ""
YAML

# seed policy + QoS defaults
cat > policy/sdd.rego <<'REGO'
package sdd

deny[msg] {
  input.unresolved > 0
  msg := sprintf("Spec contains %d unresolved [NEEDS CLARIFICATION] marker(s).", [input.unresolved])
}

deny[msg] {
  input.schema_count < 1
  msg := "No contract schemas found under /contracts."
}

deny[msg] {
  input.tests_contract_count < 1
  msg := "No contract tests found under /tests/contract."
}
REGO

cat > .sdd/qos.defaults.json <<'JSON'
{ "api": { "p95_ms": 200 }, "spa": { "bundle_kb": 200 }, "worker": { "mem_mb": 256, "time_sec": 30 } }
JSON

echo "Created CI workflow calling sdd-foundation and seeded policy/defaults."
echo "Create your first spec with: bin/new-feature \"Adopt SDD Baseline\""
