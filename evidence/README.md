# AWS lab evidence — 25 screenshots

Put the **original 25 PNG screenshots** directly in this directory, preserving the exact filenames listed below. These images are **not included** in the documentation starter. Once added, change each status to `✓ Added / reviewed` after verifying that the image corresponds to its filename and is safe to publish.

**Sanitize before publishing:** inspect terminal output, `.env` or database connection strings, passwords, tokens, private keys, AWS account details, instance public IPs, personal identifiers, and console account menus. Crop or blur sensitive areas; do not simply rename sensitive files.

### Network setup

| # | Expected file | Status |
|---:|---|---|
| 01 | `01-vpc-resource-map.png` | ☐ Add & review |
| 02 | `02-web-security-group.png` | ☐ Add & review |
| 03 | `03-database-security-group.png` | ☐ Add & review |
| 04 | `04-rds-subnet-group-created.png` | ☐ Add & review |

### RDS configuration

| # | Expected file | Status |
|---:|---|---|
| 05 | `05-rds-private-connectivity.png` | ☐ Add & review |
| 06 | `06-rds-database-encryption.png` | ☐ Add & review |
| 07 | `07-rds-database-deployed.png` | ☐ Add & review |
| 08 | `08-rds-connectivity-security.png` | ☐ Add & review |

### EC2 and application

| # | Expected file | Status |
|---:|---|---|
| 09 | `09-ec2-web-server.png` | ☐ Add & review |
| 10 | `10-ec2-ssh-connected.png` | ☐ Add & review |
| 11 | `11-ec2-rds-postgresql-connection.png` | ☐ Add & review |
| 12 | `12-flask-application-running.png` | ☐ Add & review |
| 13 | `13-flask-health-check.png` | ☐ Add & review |
| 14 | `14-startupexcuses-web-application.png` | ☐ Add & review |
| 15 | `15-startupexcuses-submit-and-vote.png` | ☐ Add & review |

### Gunicorn and systemd

| # | Expected file | Status |
|---:|---|---|
| 16 | `16-gunicorn-running.png` | ☐ Add & review |
| 17 | `17-gunicorn-systemd-service.png` | ☐ Add & review |
| 18 | `18-systemd-restart-health-check.png` | ☐ Add & review |

### Security groups and routes

| # | Expected file | Status |
|---:|---|---|
| 19 | `19-web-security-group-rules.png` | ☐ Add & review |
| 20 | `20-database-security-group-rules.png` | ☐ Add & review |
| 21 | `21-private-subnet-route-table-az1.png` | ☐ Add & review |
| 22 | `22-private-subnet-route-table-az2.png` | ☐ Add & review |
| 23 | `23-private-subnet-association-az2.png` | ☐ Add & review |
| 24 | `24-private-subnet-association-az1.png` | ☐ Add & review |
| 25 | `25-public-route-table-internet-gateway.png` | ☐ Add & review |

## Quality checks

1. Each screenshot actually proves its numbered claim (for example `11` shows a successful DB connection, `25` shows the public route to the Internet Gateway).
2. Screenshots `05` and `08` verify that RDS is not publicly accessible; `19` and `20` show the **actual** inbound security-group rules.
3. Screenshots `21`–`24` show local-only route tables and the expected private subnet associations.
4. No screenshot shows live credentials, unredacted secrets, SSH keys, or unrelated personal information.
5. Run `scripts/check-evidence.ps1` from the repository root to list any missing or unexpected screenshot files.

If the images do not show a particular security control clearly, do not claim it is verified in the README.
