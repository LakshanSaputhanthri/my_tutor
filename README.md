# AWS CLF-C02 Bridge

Study material and apps for AWS certification exams. The first page lets you pick the exam:

- **CLF-C02** (Cloud Practitioner) — lessons, words, keyword game and mock exams, in Sinhala with English technical terms.
- **SAA-C03** (Solutions Architect – Associate) — practice questions by exam domain.

Progress is saved separately per exam. To refresh the imported question banks: `node tools/sync-cloudcertprep.js [clf|saa|all]`, then `make content`.

| Folder | What it is |
| --- | --- |
| `episodes/` | 6 podcast scripts (Nadee & Kasun conversations) with practice questions — the main content |
| `app/content/` | Extra content: Mock Exam 2 (`mock2.md`), cheat sheet, words / patterns / bridge questions (`bridge.json`) |
| `app/` | Web app (PWA). `build.js` builds both apps from the content |
| `flutter_app/` | Android app (Flutter), fully offline — see `flutter_app/README.md` |

## Commands (make)

Run these in a terminal in this folder. Type `make` to list them.

| Command | What it does |
| --- | --- |
| `make setup` | Installs Java 17, Android SDK and Flutter into `D:\DevTools` (once, ~3 GB) |
| `make doctor` | Checks Flutter + Android are ready |
| `make content` | Rebuilds lessons and questions from the content files |
| `make serve` | Runs the web app at http://localhost:5173 |
| `make web` | Builds the web app + zip |
| `make analyze` | Checks the Flutter code |
| `make apk` | Builds the Android app → `aws-bridge.apk` |
| `make run` | Runs the app on your Pixel (USB debugging on) |
| `make install` | Installs `aws-bridge.apk` on your Pixel |
| `make clean` | Deletes build outputs |

**Pixel USB setup (for `make run` / `make install`):** Settings → About phone → tap *Build number* 7 times → back → System → Developer options → turn on **USB debugging** → connect the USB cable → tap **Allow** on the phone.

## Build everything

```
make content
```

This creates:
- `app/dist/` — the installable web app (upload to GitHub Pages)
- `app/artifact.html` — single-file web version
- `flutter_app/assets/content.json` — content for the Flutter app

## Preview the web app

```
node app/serve.js
```

Then open http://localhost:5173

## Build the Android APK

See `flutter_app/README.md` (GitHub cloud build, or `flutter_app/build_apk.ps1` on this PC).
