# Daymark Planner

## Files
- `index.html`: the app
- `manifest.json`: installable-app metadata
- `sw.js`: offline cache for the hosted/local development version
- `icon.svg`: app icon

## Run on Windows
The easiest beginner-friendly option is VS Code with the Live Server extension:
1. Open this folder in VS Code (`File > Open Folder`).
2. Install the **Live Server** extension if needed.
3. Right-click `index.html` and choose **Open with Live Server**.
4. Your browser opens a local address, usually `http://127.0.0.1:5500`.

You can double-click `index.html` to preview the app, but install/offline features need localhost or HTTPS.

## Install on iPhone
For a real iPhone install, the app files need to be hosted at an HTTPS address:
1. Upload all four files to a static web host that supports HTTPS (for example, GitHub Pages).
2. Open the hosted `index.html` URL in Safari on the iPhone.
3. Tap Share, then **Add to Home Screen**.
4. Open it from the new Home Screen icon.

## Storage and backups
- Data is saved in local browser storage on that device/browser.
- Browser data is not automatically shared across devices.
- Use **Export backup** regularly. Keep the JSON backup somewhere safe.
- **Import backup** replaces the current planner data after confirmation.

## Limitations in this first version
- Reminders are visible in the app, but no notification is sent when the app is closed.
- A local web server on your PC is not automatically reachable from your iPhone; host the files over HTTPS for cross-device access.
- The app does not send your planner data to a server.
