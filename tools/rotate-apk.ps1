# Saves a freshly built APK as aws-bridge-<timestamp>.apk and keeps only the latest two (previous + latest).
param(
  [Parameter(Mandatory)][string]$Source,
  [Parameter(Mandatory)][string]$OutDir,
  [int]$Keep = 2
)
$ErrorActionPreference = 'Stop'

$name = 'aws-bridge-{0:yyyyMMdd-HHmmss}.apk' -f (Get-Date)
Copy-Item $Source (Join-Path $OutDir $name) -Force

Get-ChildItem $OutDir -Filter 'aws-bridge*.apk' |
  Sort-Object LastWriteTime -Descending |
  Select-Object -Skip $Keep |
  ForEach-Object { Remove-Item $_.FullName -Force; Write-Host "Removed old APK: $($_.Name)" }

Write-Host "APK ready: $(Join-Path $OutDir $name)"
