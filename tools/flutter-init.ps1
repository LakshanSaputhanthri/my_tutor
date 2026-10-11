# Generates the Android project files for flutter_app (only once), with the app name and icon.
$ErrorActionPreference = 'Stop'
. "$PSScriptRoot\env.ps1"
Set-Location "$PSScriptRoot\..\flutter_app"

if (Test-Path 'android') { Write-Host 'Android project already exists.'; return }

flutter create --project-name aws_bridge --org com.awsbridge --platforms android .
Remove-Item -ErrorAction SilentlyContinue test\widget_test.dart
foreach ($d in 'mdpi', 'hdpi', 'xhdpi', 'xxhdpi', 'xxxhdpi') {
  Copy-Item "branding\mipmap-$d\ic_launcher.png" "android\app\src\main\res\mipmap-$d\ic_launcher.png" -Force
}
$manifest = 'android\app\src\main\AndroidManifest.xml'
$xml = [IO.File]::ReadAllText((Resolve-Path $manifest))
[IO.File]::WriteAllText((Resolve-Path $manifest), $xml.Replace('android:label="aws_bridge"', 'android:label="AWS Bridge"'))
Write-Host 'Android project created.'
