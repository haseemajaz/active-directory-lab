# Hardening Checklist — Active Directory

Use this as the baseline for the audit in `ad_lab.py` and for the real lab in `docs/lab-setup.md`.

- [ ] MFA required for Domain Admins, Enterprise Admins, Schema Admins
- [ ] No disabled accounts in any privileged group
- [ ] No service account with password-never-expires unless documented and reviewed quarterly
- [ ] Password minimum length 12 or more
- [ ] Account lockout after 5 failed attempts, 30-minute lockout
- [ ] No account with last logon over 90 days ago left enabled
- [ ] Domain Admins limited to 2–3 named people
- [ ] Admin accounts never used for daily email / browsing
- [ ] Audit policy enabled: logon events, account management, policy changes
- [ ] Backups tested by restoring to an isolated VM, not just by checking the backup job succeeded
