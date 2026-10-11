# Puts the dev tools on PATH for the current PowerShell session. Dot-source it: . .\tools\env.ps1
$Root = if ($env:DEVTOOLS_ROOT) { $env:DEVTOOLS_ROOT } else { 'D:\DevTools' }
$env:JAVA_HOME = "$Root\jdk17"
$env:ANDROID_HOME = "$Root\android-sdk"
$env:ANDROID_SDK_ROOT = $env:ANDROID_HOME
$env:GRADLE_USER_HOME = "$Root\gradle-home"
$env:PUB_CACHE = "$Root\pub-cache"
$env:Path = "$Root\flutter\bin;$env:JAVA_HOME\bin;$env:ANDROID_HOME\platform-tools;$env:ANDROID_HOME\cmdline-tools\latest\bin;" + $env:Path
