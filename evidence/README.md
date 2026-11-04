# AWS lab evidence — 25 screenshots

Put the **original 25 PNG screenshots** directly in this directory, preserving the exact filenames listed below. These images are **not included** in the documentation starter. Once added, change each status to `✓ Added / reviewed` after verifying that the image corresponds to its filename and is safe to publish.

**Sanitize before publishing:** inspect terminal output, `.env` or database connection strings, passwords, tokens, private keys, AWS account details, instance public IPs, personal identifiers, and console account menus. Crop or blur sensitive areas; do not simply rename sensitive files.


### Network setup

| # | Evidence screenshot | Status |
|---:|---|---|
| 01 | [01-vpc-resource-map.png](01-vpc-resource-map.png) | ✅ Added & sanitized |
| 02 | [02-web-security-group.png](02-web-security-group.png) | ✅ Added & sanitized |
| 03 | [03-database-security-group.png](03-database-security-group.png) | ✅ Added & sanitized |
| 04 | [04-rds-subnet-group-created.png](04-rds-subnet-group-created.png) | ✅ Added & sanitized |

### RDS configuration

| # | Evidence screenshot | Status |
|---:|---|---|
| 05 | [05-rds-private-connectivity.png](05-rds-private-connectivity.png) | ✅ Added & sanitized |
| 06 | [06-rds-database-encryption.png](06-rds-database-encryption.png) | ✅ Added & sanitized |
| 07 | [07-rds-database-deployed.png](07-rds-database-deployed.png) | ✅ Added & sanitized |
| 08 | [08-rds-connectivity-security.png](08-rds-connectivity-security.png) | ✅ Added & sanitized |

### EC2 and application

| # | Evidence screenshot | Status |
|---:|---|---|
| 09 | [09-ec2-web-server.png](09-ec2-web-server.png) | ✅ Added & sanitized |
| 10 | [10-ec2-ssh-connected.png](10-ec2-ssh-connected.png) | ✅ Added & sanitized |
| 11 | [11-ec2-rds-postgresql-connection.png](11-ec2-rds-postgresql-connection.png) | ✅ Added & sanitized |
| 12 | [12-flask-application-running.png](12-flask-application-running.png) | ✅ Added & sanitized |
| 13 | [13-flask-health-check.png](13-flask-health-check.png) | ✅ Added & sanitized |
| 14 | [14-startupexcuses-web-application.png](14-startupexcuses-web-application.png) | ✅ Added & sanitized |
| 15 | [15-startupexcuses-submit-and-vote.png](15-startupexcuses-submit-and-vote.png) | ✅ Added & sanitized |

### Gunicorn and systemd

| # | Evidence screenshot | Status |
|---:|---|---|
| 16 | [16-gunicorn-running.png](16-gunicorn-running.png) | ✅ Added & sanitized |
| 17 | [17-gunicorn-systemd-service.png](17-gunicorn-systemd-service.png) | ✅ Added & sanitized |
| 18 | [18-systemd-restart-health-check.png](18-systemd-restart-health-check.png) | ✅ Added & sanitized |

### Security groups and routes

| # | Evidence screenshot | Status |
|---:|---|---|
| 19 | [19-web-security-group-rules.png](19-web-security-group-rules.png) | ✅ Added & sanitized |
| 20 | [20-database-security-group-rules.png](20-database-security-group-rules.png) | ✅ Added & sanitized |
| 21 | [21-private-subnet-route-table-az1.png](21-private-subnet-route-table-az1.png) | ✅ Added & sanitized |
| 22 | [22-private-subnet-route-table-az2.png](22-private-subnet-route-table-az2.png) | ✅ Added & sanitized |
| 23 | [23-private-subnet-association-az2.png](23-private-subnet-association-az2.png) | ✅ Added & sanitized |
| 24 | [24-private-subnet-association-az1.png](24-private-subnet-association-az1.png) | ✅ Added & sanitized |
| 25 | [25-public-route-table-internet-gateway.png](25-public-route-table-internet-gateway.png) | ✅ Added & sanitized |


## Quality checks

1. Each screenshot actually proves its numbered claim (for example `11` shows a successful DB connection, `25` shows the public route to the Internet Gateway).
2. Screenshots `05` and `08` verify that RDS is not publicly accessible; `19` and `20` show the **actual** inbound security-group rules.
3. Screenshots `21`–`24` show local-only route tables and the expected private subnet associations.
4. No screenshot shows live credentials, unredacted secrets, SSH keys, or unrelated personal information.
5. Run `scripts/check-evidence.ps1` from the repository root to list any missing or unexpected screenshot files.

If the images do not show a particular security control clearly, do not claim it is verified in the README.
