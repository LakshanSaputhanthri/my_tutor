# AWS Bridge — Flutter app

A fully offline Android app for the AWS Cloud Practitioner (CLF-C02) exam: 8 lessons, 64 exam-English words, 285 practice questions (including three mock exams), a keyword game, and saved progress.

The content comes from the episode files in `..\episodes`. `node ..\app\build.js` turns them into `assets/content.json`.

## Option A — Build in the cloud with GitHub (no installs on your PC)

1. Create a free account at github.com.
2. Create a new **public** repository called `aws-bridge` (don't add a README).
3. Upload **everything inside this `flutter_app` folder** (including the hidden `.github` folder) to the repository and commit to `main`.
   - Easiest with Git on your PC:
     ```
     cd D:\DevOps\podcast\flutter_app
     git init -b main
     git add .
     git commit -m "AWS Bridge app"
     git remote add origin https://github.com/YOUR-USERNAME/aws-bridge.git
     git push -u origin main
     ```
4. Open the repository → **Actions** tab. The **Build APK** job runs on its own (about 5–8 minutes).
5. When it is green, open **Releases** on the right side of the repository page and you'll find `aws-bridge.apk`.

## Option B — Build on this PC

1. Install **Flutter** (https://docs.flutter.dev/get-started/install/windows/mobile) and **Android Studio** (it installs the Android SDK and Java).
2. Run `flutter doctor` and fix anything it marks with ✗ (accept the Android licenses with `flutter doctor --android-licenses`).
3. In PowerShell:
   ```
   cd D:\DevOps\podcast\flutter_app
   .\build_apk.ps1
   ```
4. The file `aws-bridge.apk` is created in this folder.

## Install on the Google Pixel

1. Copy `aws-bridge.apk` to the phone (or open the GitHub Releases page in Chrome on the phone and download it).
2. Tap the file. Android asks to allow installs from this source → **Settings → Allow from this source** → back → **Install**.
3. Open **AWS Bridge** from your home screen. It works without internet. Progress is saved on the phone.

To move progress from the web app: Web app → Home → Progress backup → **Copy backup** → paste into the phone app's **Restore** box.

## Updating content

Edit an episode `.md` file or `app/content/*.md`, then run `node ..\app\build.js` and build again (or push to GitHub).
