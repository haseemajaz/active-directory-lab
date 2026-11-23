# Lab Setup — building the real Active Directory lab

This is a build guide, not a script. Build it in a private virtual network with no internet routing to production systems.

## Topology

| VM | Role | Notes |
|---|---|---|
| DC01 | Domain Controller, DNS | Windows Server, `demo.corp.local` |
| CLIENT01 | Windows 10/11 client | Domain-joined, for logon testing |
| Optional: SRV01 | File / member server | For service-account practice |

Use VirtualBox, VMware, or Hyper-V. Keep the lab on a host-only / NAT network.

## Build steps

1. Install Windows Server on DC01, set a static IP, install the AD DS role.
2. Promote DC01 to a domain controller for `demo.corp.local`, install DNS.
3. Create an organisational unit structure, for example `OU=Users`, `OU=Service Accounts`, `OU=Workstations`.
4. Create test users and groups matching `data/demo_users.json`: a normal user, a Domain Admin, a service account, and a stale/disabled account.
5. Join CLIENT01 to the domain and log on as each test user.
6. Apply the hardening checklist (`docs/hardening-checklist.md`) and re-run the audit mindset: who is privileged, who has MFA, what is stale.

## Hardening checklist

- MFA required for all privileged accounts
- Password minimum length 12+, lockout after 5 failed attempts
- No disabled accounts in privileged groups
- Service account passwords rotated on a schedule, never set to never-expire without a documented reason
- Stale accounts disabled after 90 days, deleted after review
- Domain Admins group kept to 2–3 named people, no day-to-day use
- Audit logging on, and logs forwarded somewhere the domain admins cannot delete

## Teardown

Snapshot the VMs before each exercise so you can reset. Never join a production machine to a lab domain.
