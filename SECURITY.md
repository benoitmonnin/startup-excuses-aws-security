# Security and public GitHub publishing checklist

This README and architecture diagram are not a security audit. The application source code and all 25 original screenshots were not available for inspection when this documentation starter was prepared.

## Before making the repository public

- [ ] Verify the project directory contains **no** `.env` / `.env.*` secrets, `*.pem` or SSH private keys, AWS access keys, database passwords, tokens or connection strings with credentials.
- [ ] Review all Flask source files, shell history excerpts, configuration files and dependency manifests.
- [ ] Review **every screenshot** for credentials, identifiable account details and sensitive terminal output; crop or redact locally.
- [ ] Check `git status --short` and `git diff --cached --name-only` to confirm which files will be published.
- [ ] Use a dedicated secret scanner (for example, `gitleaks` or `trufflehog`) on the folder and Git history if one is available. Manual checks and `.gitignore` alone are insufficient.
- [ ] Confirm that RDS has no public access and that port 5432 is restricted to the EC2 security group.
- [ ] Restrict or disable public SSH access; never publish your private SSH key.
- [ ] Confirm the README does not claim controls, HTTPS, multi-AZ deployment or production readiness not demonstrated by the evidence.

## Example review commands (PowerShell)

```powershell
git status --short
git diff --cached --name-only
git diff --cached --check
# Show ALL tracked files including hidden files:
git ls-files
# If installed: scan current directory and Git repository using gitleaks.
gitleaks git .
```

Gitleaks versions can differ: consult `gitleaks --help` for the syntax installed locally.

## If a secret was committed

1. Revoke/rotate the credential **immediately** (change database password, revoke AWS key, replace SSH key).
2. Remove the secret from files and Git history before making the repository public. A new commit alone does not erase prior exposure.
3. Review access and cloud billing for unexpected activity.
4. Do not paste the credential into chats, issues or pull requests while troubleshooting.

## Recommended longer-term controls

Use AWS Systems Manager or tightly restricted admin access, AWS IAM roles for instance permissions, AWS Secrets Manager/SSM Parameter Store for application secrets, secure DB connections, HTTPS/TLS for public endpoints, least-privilege SGs and automated security checks. These are recommended improvements, **not assertions** about this lab.
