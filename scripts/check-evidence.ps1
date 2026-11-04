# Checks expected screenshot filenames without modifying files.
$ErrorActionPreference = "Stop"
$repo = Split-Path -Parent $PSScriptRoot
$evidence = Join-Path $repo "evidence"
$expected = @(
  "01-vpc-resource-map.png",
  "02-web-security-group.png",
  "03-database-security-group.png",
  "04-rds-subnet-group-created.png",
  "05-rds-private-connectivity.png",
  "06-rds-database-encryption.png",
  "07-rds-database-deployed.png",
  "08-rds-connectivity-security.png",
  "09-ec2-web-server.png",
  "10-ec2-ssh-connected.png",
  "11-ec2-rds-postgresql-connection.png",
  "12-flask-application-running.png",
  "13-flask-health-check.png",
  "14-startupexcuses-web-application.png",
  "15-startupexcuses-submit-and-vote.png",
  "16-gunicorn-running.png",
  "17-gunicorn-systemd-service.png",
  "18-systemd-restart-health-check.png",
  "19-web-security-group-rules.png",
  "20-database-security-group-rules.png",
  "21-private-subnet-route-table-az1.png",
  "22-private-subnet-route-table-az2.png",
  "23-private-subnet-association-az2.png",
  "24-private-subnet-association-az1.png",
  "25-public-route-table-internet-gateway.png"
)

$missing = @()
foreach ($name in $expected) {
    if (-not (Test-Path -LiteralPath (Join-Path $evidence $name) -PathType Leaf)) {
        $missing += $name
    }
}

$unexpected = @(Get-ChildItem -LiteralPath $evidence -Filter "*.png" -File | Where-Object { $_.Name -notin $expected } | Select-Object -ExpandProperty Name)
Write-Host "Found $($expected.Count - $missing.Count)/$($expected.Count) expected screenshots."
if ($missing.Count) {
    Write-Host "Missing:"
    $missing | ForEach-Object { Write-Host "  $_" }
}
if ($unexpected.Count) {
    Write-Host "Unexpected PNG files (review manually):"
    $unexpected | ForEach-Object { Write-Host "  $_" }
}
if ($missing.Count -eq 0 -and $unexpected.Count -eq 0) {
    Write-Host "Evidence filenames complete. REVIEW IMAGES for secrets before pushing."
} else {
    Write-Host "Add/correct screenshots before calling evidence complete."
}
