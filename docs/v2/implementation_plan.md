# Product Requirements Document (PRD) & Implementation Plan: Unified App

## 1. Goal
Transition the Wyrypa Tracker from a system of hardcoded, duplicated "generator" scripts into a single **Unified Web App Engine**. This engine will dynamically load and render specific "Trekking Datasets," decoupling the presentation/tracking logic from the route data.

## 2. Core Mechanics & Functionalities
The unified engine will support all existing functionalities, but process them dynamically:

1. **Dynamic Engine:** A single `index.html` built with React/Vite that expects a `dataset.json` file.
2. **Graceful Degradation (Defaults):** If a dataset is missing a section (e.g., no "Training Schedule" provided), the engine simply hides that UI tab. If specific pace data is missing, it falls back to a global default pace.
3. **Common User Profile (Local Storage):** A settings panel where the user configures global parameters (weight, default pace on flat terrain, heart rate zones). This is saved in the phone's local storage and used as a fallback.
4. **Offline Map Management:** The engine will read map boundaries from the dataset and manage offline tile caching for that specific bounding box.
5. **Route Selector (Hub Integration):** The Android App (Hub) will download the Engine *once*, and then download *Datasets* (JSON + GPX) for specific routes, dramatically reducing app size and update times.

### B. The Dataset Format (Bilingual & Timeline-based)
Each route will be defined by `dataset.json`. Based on your feedback, we are making two massive architectural improvements:
1. **Bilingual by Design**: The JSON will contain dual-language keys (e.g., `action_pl` and `action_en`) so the Engine can instantly switch languages completely offline without needing a translation service.
2. **Time-Based Action Timeline**: Instead of binding tactical notes strictly to physical waypoints (peaks), the JSON will contain a separate `actionTimeline`. For example: "Between hour 0:00 and 2:00, drink 500ml". The UI Engine will dynamically cross-reference the estimated elapsed time of each waypoint with the timeline, and automatically attach the correct actions to the correct rows in the table.

## 3. Architecture & Project Structure
To ensure you can use both the old app and the new app during the transition, we will strictly separate them:

- `legacy_generators/` *(Optional move later)*: We will leave the current scripts and folders intact for now so the old Android App continues to function normally.
- `v2_unified/`: The root for the new system.
  - `v2_unified/engine/`: The React/Vite source code.
  - `v2_unified/android/`: The new native Android project (Capacitor).
  - `v2_unified/datasets/`: Folders containing `route.json` and `track.gpx` for each route.

### C. GitHub Pages Deployment
The new V2 React Engine will be fully compatible with GitHub Pages. We will configure Vite to output a static bundle. The `datasets` folder will simply live in the `public/` directory, allowing the web version of the app to fetch them via standard HTTP requests. This means you can use the app directly from your browser just like the legacy apps!

## 4. The Analytics Process (Prompt Pattern)
We have split the prompts into two distinct stages:
- **Prompt 1 (Profile Builder)**: Extracts your physiological data and crisis-management history into a reusable document.
- **Prompt 2 (Challenge Analyst)**: Uses your Profile + GPX to generate the bilingual JSON, the time-based action timeline, and explicit training/nutrition regimens.

## 5. Android Background Reliability (Native Plugin)
*Addressing your question about WebViews:* Yes, Android OS aggressively kills WebViews because they consume a lot of RAM. Rewriting the entire app in pure Native Kotlin would take weeks and destroy our ability to run it on GitHub Pages. 
**The Solution:** We will use a hybrid approach. We will stick with Capacitor for the UI, but we will install a **Native Background Geolocation Plugin** (`@capacitor-community/background-geolocation`). 
- This plugin runs pure native Java code as a persistent Foreground Service.
- Even if Android kills the WebView UI, the native plugin stays alive and continues tracking your GPS.
- When you reopen the app, the WebView simply asks the native plugin for the location history. This gives us 100% native reliability without rewriting the UI!

## 6. Execution Roadmap

1. **Phase 0: Legacy App Fix:** Update `build_standalone.py` to aggressively save tracking/downloading states to `localStorage` and automatically resume them on WebView reload. We will rebuild the old APK once to give you a stable version immediately.
2. **Phase 1: Data Definition:** Define the `dataset.json` schema and create the Prompt Pattern artifact. You will test the prompt on a new GPX file.
3. **Phase 2: Engine Initialization:** Bootstrap the `v2_unified/engine` with React, Vite, and Tailwind.
4. **Phase 3: Migration:** Convert the old 100km and 75km data into the new `dataset.json` format.
5. **Phase 4: UI Development:** Build the dynamic tables, map renderer, and offline caching in React.
6. **Phase 5: Native App (V2):** Wrap the new engine in a new Capacitor Android project utilizing the native Background Geolocation plugin for bulletproof background tracking.
