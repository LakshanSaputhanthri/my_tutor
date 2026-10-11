# Installs everything needed to build the Flutter Android app (safe to run again).
# Java 17, Android SDK command-line tools + packages, Flutter SDK. All under D:\DevTools (or $env:DEVTOOLS_ROOT).
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$Root = if ($env:DEVTOOLS_ROOT) { $env:DEVTOOLS_ROOT } else { 'D:\DevTools' }
$jdk = "$Root\jdk17"
$sdk = "$Root\android-sdk"
$flutter = "$Root\flutter"
function Step($m) { Write-Host "`n==> $m" -ForegroundColor Cyan }

New-Item -ItemType Directory -Force $Root, "$Root\gradle-home", "$Root\pub-cache" | Out-Null

# 1. Java 17
if (-not (Test-Path "$jdk\bin\java.exe")) {
  Step 'Installing Java 17 (Eclipse Temurin)'
  $zip = "$Root\jdk17.zip"
  curl.exe -L --fail -o $zip 'https://api.adoptium.net/v3/binary/latest/17/ga/windows/x64/jdk/hotspot/normal/eclipse'
  $tmp = "$Root\jdk17-tmp"
  New-Item -ItemType Directory -Force $tmp | Out-Null
  tar.exe -xf $zip -C $tmp
  Move-Item (Get-ChildItem $tmp -Directory | Select-Object -First 1).FullName $jdk
  Remove-Item $tmp, $zip -Recurse -Force
} else { Step 'Java 17 already installed' }

# 2. Android SDK command-line tools
if (-not (Test-Path "$sdk\cmdline-tools\latest\bin\sdkmanager.bat")) {
  Step 'Installing Android SDK command-line tools'
  $zip = "$Root\cmdline-tools.zip"
  curl.exe -L --fail -o $zip 'https://dl.google.com/android/repository/commandlinetools-win-11076708_latest.zip'
  $tmp = "$sdk\cmdline-tools-tmp"
  New-Item -ItemType Directory -Force $tmp, "$sdk\cmdline-tools" | Out-Null
  tar.exe -xf $zip -C $tmp
  Move-Item "$tmp\cmdline-tools" "$sdk\cmdline-tools\latest"
  Remove-Item $tmp, $zip -Recurse -Force
} else { Step 'Android command-line tools already installed' }

# 3. Flutter SDK (stable)
if (-not (Test-Path "$flutter\bin\flutter.bat")) {
  Step 'Downloading Flutter SDK (stable)'
  git clone --depth 1 -b stable https://github.com/flutter/flutter.git $flutter
} else { Step 'Flutter SDK already downloaded' }

# 4. Environment (this session + saved for new terminals)
Step 'Setting environment variables (user level)'
. "$PSScriptRoot\env.ps1"
foreach ($kv in @{ JAVA_HOME = $env:JAVA_HOME; ANDROID_HOME = $env:ANDROID_HOME; ANDROID_SDK_ROOT = $env:ANDROID_HOME; GRADLE_USER_HOME = $env:GRADLE_USER_HOME; PUB_CACHE = $env:PUB_CACHE }.GetEnumerator()) {
  [Environment]::SetEnvironmentVariable($kv.Key, $kv.Value, 'User')
}
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
$parts = @($userPath -split ';' | Where-Object { $_ })
foreach ($p in "$flutter\bin", "$jdk\bin", "$sdk\platform-tools", "$sdk\cmdline-tools\latest\bin") {
  if ($parts -notcontains $p) { $parts += $p }
}
[Environment]::SetEnvironmentVariable('Path', ($parts -join ';'), 'User')

# 5. Android SDK packages + licenses
Step 'Accepting Android licenses'
("y`n" * 40) | & "$sdk\cmdline-tools\latest\bin\sdkmanager.bat" --sdk_root=$sdk --licenses | Out-Null
Step 'Installing Android platform-tools, platform 35, build-tools 35'
& "$sdk\cmdline-tools\latest\bin\sdkmanager.bat" --sdk_root=$sdk 'platform-tools' 'platforms;android-35' 'build-tools;35.0.0'

# 6. Flutter first run
Step 'Configuring Flutter (first run downloads the Dart SDK)'
flutter config --no-analytics --android-sdk $sdk --jdk-dir $jdk
("y`n" * 40) | flutter doctor --android-licenses | Out-Null
flutter precache --android
flutter doctor

Write-Host "`nSetup finished. Open a NEW terminal so the PATH changes apply." -ForegroundColor Green
