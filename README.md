# 09 — Active Directory Lab

**Area:** Security Engineering · **Stack:** Python 3.10+ (standard library only) · **Status:** Portfolio starter, safe local demo

## What it does

A real Active Directory lab needs Windows Server, virtual machines, and licences. This starter gives you the security thinking first, in a form you can run anywhere:

- `ad_lab.py` loads a fictional directory (`data/demo_users.json`) and audits it:
  - Privileged accounts (Domain Admins, Enterprise Admins) and who holds them
  - Service accounts with old / never-expiring passwords
  - Users with no MFA, disabled accounts still in privileged groups
  - Stale accounts (no logon in 90+ days)
  - Password policy gaps against a documented baseline
- `docs/lab-setup.md` is the full build guide for a real lab: two Windows Server VMs, a client VM, and the hardening steps, so an employer can see you know the real thing, not just the simulator.
- `docs/hardening-checklist.md` is the checklist the audit is built from.

## What an employer sees

- You can enumerate privilege, spot the accounts that matter, and explain why each finding is a risk
- You can write a lab build guide, not just run one
- Your audit output is a report with owners and remediation, not a dump

## How to run

```bash
cd 09-active-directory-lab
python3 ad_lab.py
python3 ad_lab.py --input data/demo_users.json --format json
```

## Try it yourself

Edit `data/demo_users.json`: give `svc_backup` a recent password change, remove `temp_admin` from Domain Admins, enable MFA for `alice`, re-run, and watch the findings drop.

## Safety

Educational only. All users, groups, and passwords in the demo data are fictional. Never run audit tooling against a real directory without written permission from its owner, and never collect real credentials.
