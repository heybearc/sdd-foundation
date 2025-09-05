# MCP Servers (Stubs)

This folder documents suggested Model Context Protocol (MCP) servers that agents can call:
- **github/**: Read diffs, list PRs/issues, post comments (for Cost/QoS summaries).
- **files/**: Fetch specific files (spec sections, plans) by path so agents avoid loading whole repos.
- **metrics/**: Expose CI artifacts (size.json, perf.json, lhci.json) for QoSGuardian.
- **contracts/**: Run contract tools (schemathesis, dredd) and expose JSON summaries.
- **policy/**: Evaluate OPA/Conftest policies and return pass/fail with messages.

Use these as *interfaces*. Actual server implementations can be swapped without changing agent prompts.
