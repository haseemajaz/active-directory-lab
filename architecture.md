# Architecture — Active Directory Lab

## Flow

```
data/demo_users.json  →  ad_lab.py: audit()  →  findings (severity, finding, remediation)
docs/lab-setup.md     →  how to build the real lab this simulates
docs/hardening-checklist.md  →  the baseline the audit checks against
```

## What the audit checks, and why

| Check | Risk it catches |
|---|---|
| Disabled user still in a privileged group | Re-enabled accounts inherit admin rights |
| Privileged account without MFA | One phished password = domain admin |
| Service account password never expires | Long-lived credential, rarely monitored |
| No logon in 90+ days | Stale accounts are quiet attack paths |
| Password minimum below 12 / no lockout | Weak baseline policy |

## Design decisions

- **Simulator, not a real AD client.** A portfolio repo that requires a Windows domain to run is unusable for most reviewers. The audit logic is the transferable part; the real lab is documented in `docs/lab-setup.md`.
- **Fictional data only.** No real usernames, no real passwords, no hashes.
- **`audit()` is pure.** It takes a dict and returns findings, so it is trivially testable.
