# Expo local-notification test (sandbox)

A throwaway test for issue #10 (platform decision). It is not part of the scheduler.

## Question

Does a reminder scheduled by an Expo app arrive when the app is fully closed?

## What it does

`App.js` has one button. Tapping it asks for notification permission, then schedules one local notification 60 seconds later with `scheduleNotificationAsync` and a `DATE` trigger. The screen shows when the reminder was scheduled and when it is due.

## Result: one trial, 2026-11-03

| | |
|---|---|
| Device | iPhone, iOS 26.6, Expo Go (SDK 58) |
| App state after scheduling | Fully closed (swiped away in the app switcher) |
| Scheduled at | 8:01 PM |
| Due at | 8:02 PM |
| Arrived | 8:02 PM |
| How arrival was measured | Watched the phone clock and counted; precise to the minute |

The reminder arrived while the app was closed. The notification is handed to iOS, and iOS delivers it, so the app does not need to be running. This is one trial only. Reliability under other conditions (phone locked, Focus on, Low Power Mode, after a restart) is Milestone 3.

## Dependency

- `expo-notifications` (~58.1.7): schedules local notifications through the operating system. It was installed with `npx expo install` so its version matches SDK 58.

## Known issues, not fixed

- `npm install` reports 11 moderate vulnerabilities. They were not fixed because `npm audit fix --force` would change Expo's pinned versions and break the SDK match. This is sandbox code; recheck when the scheduler is built.
- Expo Go warns that `expo-notifications` is "not fully supported" and that Android push notifications were removed. Neither affects local notifications on iOS. A development build would remove the limitation.
- Metro warns "Unable to resolve manifest assets" (icons and fonts). This is harmless for this test.

## Lessons

- Check the SDK version Expo Go supports (in Expo Go's settings) before creating the project. The project was first made on SDK 54 and would not load, because Expo Go was on 58.0.
- On SDK 58, `--tunnel` needs an Expo account signed in on both the phone and the CLI.
- In WSL, `npx expo login` crashed while opening the Windows browser (most likely because `cmd.exe` splits the URL at each `&`). `npx expo login --no-browser` works; type the password at the prompt, never as a flag. The session token is saved in `~/.expo/state.json` (owner-only permissions), outside the repository.
- WSL2 sits behind NAT, so the phone cannot reach Metro over the local network; `--tunnel` is needed.

## Run it

~~~
cd sandbox/expo-local-notification
npm install
npx expo login --no-browser
npx expo start --tunnel
~~~

In Expo Go, choose "Enter URL manually" and type the `exp://` address shown in the terminal.

## Template files

- `LICENSE` is the MIT notice from Expo's project template (650 Industries, Inc.). It covers the files the template generated (`index.js`, `app.json`, `assets/` and the project setup). It is kept because the MIT license requires the notice to stay with the code.
- The template also created an `AGENTS.md` with instructions for AI coding agents. It was removed before the first commit: it did not include this repository's security rules, it told agents to fetch web pages and follow their links, and it ran `eas-cli@latest` unpinned. Its useful rules (install with `npx expo install`, check the docs for the SDK version in use, and Expo Go only includes its bundled native modules) will move into the root `AGENTS.md`.
