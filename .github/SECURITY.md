# Security policy

## Reporting a vulnerability

To report a security issue, either report it privately
[on GitHub](https://github.com/termcolor/termcolor/security) (preferred) or through the
[Tidelift security contact](https://tidelift.com/security). Do not open a public issue.

## Incident response plan

### 1. Triage

- Acknowledge the report to the reporter.
- Reproduce and assess severity.
- Open a private GitHub Security Advisory if confirmed.
- If necessary, yank the affected versions on PyPI (`pip install termcolor` will skip
  yanked versions, but explicit pins still work).
- If the release contains malicious code (for example, supply chain compromise), delete
  it from PyPI entirely so it cannot be installed at all.

### 2. Fix

- Develop a fix in a private fork via the Security Advisory.
- Include a regression test.
- Request a CVE through the GitHub Advisory if applicable.

### 3. Release and disclosure

- Merge the fix and publish a patch release to PyPI.
- Publish the GitHub Security Advisory to notify users.
- Credit the reporter (unless they prefer anonymity).
- Include details in the release notes.

## Supported versions

Security fixes are only applied to the latest release.
