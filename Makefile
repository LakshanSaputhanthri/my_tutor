# AWS CLF-C02 Bridge — build & run commands (Windows, GNU make). Type `make` to see them.
SHELL := powershell.exe
.SHELLFLAGS := -NoProfile -ExecutionPolicy Bypass -Command

ENV := . ./tools/env.ps1;
APK := flutter_app/build/app/outputs/flutter-apk/app-release.apk

.DEFAULT_GOAL := help
.PHONY: help setup doctor content serve web init get analyze apk run devices install clean

help:
	@Write-Host 'make setup     Install Java 17, Android SDK and Flutter (once, ~3 GB, into D:\DevTools)'
	@Write-Host 'make doctor    Check that Flutter and Android are ready'
	@Write-Host 'make content   Build lessons and questions from episodes/ and app/content/'
	@Write-Host 'make serve     Run the web app at http://localhost:5173'
	@Write-Host 'make web       Build the web app and zip it (app/aws-bridge-app.zip)'
	@Write-Host 'make get       Prepare the Flutter project (Android files + packages)'
	@Write-Host 'make analyze   Check the Flutter code for errors'
	@Write-Host 'make apk       Build the Android app -> aws-bridge.apk'
	@Write-Host 'make devices   List connected phones'
	@Write-Host 'make run       Run the app on the connected Pixel (USB debugging on)'
	@Write-Host 'make install   Install aws-bridge.apk on the connected Pixel'
	@Write-Host 'make clean     Delete build outputs'

setup:
	./tools/setup-windows.ps1

doctor:
	$(ENV) flutter doctor -v

content:
	node app/build.js

serve: content
	node app/serve.js

web: content
	Compress-Archive -Path app/dist/* -DestinationPath app/aws-bridge-app.zip -Force; Write-Host 'Web app: app/dist  Zip: app/aws-bridge-app.zip'

init: content
	./tools/flutter-init.ps1

get: init
	$(ENV) Set-Location flutter_app; flutter pub get

analyze: get
	$(ENV) Set-Location flutter_app; flutter analyze

apk: get
	$(ENV) Set-Location flutter_app; flutter build apk --release
	./tools/rotate-apk.ps1 -Source $(APK) -OutDir .

devices:
	$(ENV) flutter devices

run: get
	$(ENV) Set-Location flutter_app; flutter run

install:
	$(ENV) adb install -r (Get-ChildItem aws-bridge*.apk | Sort-Object LastWriteTime -Descending | Select-Object -First 1).FullName

clean:
	$(ENV) Set-Location flutter_app; flutter clean
	Remove-Item -Recurse -Force -ErrorAction SilentlyContinue app/dist, aws-bridge*.apk
