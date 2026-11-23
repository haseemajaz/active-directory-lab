#!/usr/bin/env python3
"""Active Directory Lab — audit simulator (safe local demo).

Audits a fictional directory JSON: privileged groups, stale accounts,
service accounts, MFA gaps, and password policy. Standard library only.
No real AD, no LDAP, no credentials.
"""
import argparse
import json
import sys
from datetime import date, timedelta
from pathlib import Path

PRIVILEGED = {"Domain Admins", "Enterprise Admins", "Schema Admins"}
STALE_DAYS = 90


def audit(directory):
    findings = []
    today = date.fromisoformat(directory.get("as_of", "2026-11-23"))
    for user in directory.get("users", []):
        name = user["name"]
        groups = set(user.get("groups", []))
        privileged = groups & PRIVILEGED
        if privileged and user.get("disabled"):
            findings.append(("High", f"{name} is disabled but still in {sorted(privileged)}",
                             "Remove disabled accounts from privileged groups."))
        if privileged and not user.get("mfa", False):
            findings.append(("High", f"Privileged account {name} has no MFA",
                             "Require MFA for all privileged accounts."))
        if user.get("service_account") and user.get("password_never_expires"):
            findings.append(("Medium", f"Service account {name} password never expires",
                             "Rotate service account passwords on a schedule."))
        last = user.get("last_logon")
        if last and (today - date.fromisoformat(last)).days > STALE_DAYS:
            findings.append(("Low", f"{name} has not logged on in over {STALE_DAYS} days",
                             "Disable stale accounts, then delete after review."))
        if not user.get("mfa", False) and not user.get("service_account") and not privileged:
            findings.append(("Medium", f"{name} has no MFA",
                             "Enrol the user in MFA."))
    policy = directory.get("password_policy", {})
    if policy.get("min_length", 99) < 12:
        findings.append(("Medium", "Password minimum length is below 12 characters",
                         "Set minimum length to 12 or more."))
    if not policy.get("lockout_after_failures"):
        findings.append(("Medium", "No account lockout policy",
                         "Set lockout after 5 failed attempts."))
    return findings


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", default="data/demo_users.json")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    directory = json.loads(Path(args.input).read_text())
    findings = audit(directory)
    if args.format == "json":
        print(json.dumps([{"severity": s, "finding": f, "remediation": r}
                          for s, f, r in findings], indent=2))
    else:
        print(f"Domain: {directory.get('domain')}  Findings: {len(findings)}")
        for severity, finding, remediation in findings:
            print(f"  [{severity}] {finding}\n        Fix: {remediation}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
