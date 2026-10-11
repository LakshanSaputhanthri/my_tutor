# Builds the Android APK on this PC. Needs Flutter + Android Studio installed (see README.md).
$ErrorActionPreference = 'Stop'
Set-Location $PSScriptRoot

node ..\app\build.js

if (-not (Test-Path 'android')) {
  flutter create --project-name aws_bridge --org com.awsbridge --platforms android .
  Remove-Item -ErrorAction SilentlyContinue test\widget_test.dart
  foreach ($d in 'mdpi','hdpi','xhdpi','xxhdpi','xxxhdpi') {
    Copy-Item "branding\mipmap-$d\ic_launcher.png" "android\app\src\main\res\mipmap-$d\ic_launcher.png" -Force
  }
  $manifest = 'android\app\src\main\AndroidManifest.xml'
  (Get-Content $manifest -Raw).Replace('android:label="aws_bridge"', 'android:label="AWS Bridge"') | Set-Content $manifest -Encoding utf8
}

flutter pub get
flutter build apk --release
Copy-Item build\app\outputs\flutter-apk\app-release.apk .\aws-bridge.apk -Force
Write-Host "Done: $PSScriptRoot\aws-bridge.apk"
