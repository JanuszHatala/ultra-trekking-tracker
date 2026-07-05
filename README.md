# Wyrypa Ultra-Trekking Tracker Portal

👉 **Live Demo:** [https://januszhatala.github.io/ultra-trekking-tracker/](https://januszhatala.github.io/ultra-trekking-tracker/)

An interactive, mobile-optimized portal and strategy dashboard designed for preparation and real-time offline tracking during the Wyrypa ultra-trekking challenge. The project hosts two distinct tracking applications side-by-side.

---

## portal Entry Page (`index.html`)
The homepage is a beautiful, dark-themed gateway that allows the user to choose between:
1. **Wyrypa 100km Tracker**: Lime-themed, target goal `< 24h` pacing strategy.
2. **Wyrypa 75km Tracker**: Cyan-themed, target goal `~18.5h` pacing strategy.

---

## Core Features

- **Side-by-Side Mobile Installation (PWAs)**:
  - Both applications are independent Progressive Web Apps.
  - Configured with explicit `"id"` and `"scope"` manifest parameters and distinct service workers (`sw.js` and `sw_75.js`).
  - They install as **two separate apps** on Android and mobile home screens without overwriting or interfering with one another.
- **Unique App Branding**:
  - Custom brand launcher icons: `100k` featuring a lime circle, and `75k` featuring a cyan circle.
- **Interactive Checkpoint Timeline**:
  - Checkpoint tracking tables, pacing guidelines, elevation analysis, gear breakdowns, and tactical timelines.
  - Hovering/selecting checkpoint table rows draws glowing section overlays on the map.
- **Offline Leaflet Maps & Trailing**:
  - Standalone PWA design that caches map libraries, GPX files, styles, and tile packages.
  - Caches OpenTopoMap tiles locally using service workers for offline navigation in areas with zero cell coverage.
- **GPS Location & Tracking**:
  - Interactive "Track My Position" marker with accuracy circles.
  - **GPS Reset Button**: Theme-matched buttons (Lime in 100k, Cyan in 75k) labeled `Resetuj` (Polish) and `Reset` (English) to instantly stop tracking, clear map overlays, reset internal GPS calculations, and clean up the UI.
- **Bilingual Support**: Toggle language between Polish and English on-the-fly.

---

## File Structure

- **Portal Landing**:
  - `index.html`: Gateway page with buttons for launching the 100k or 75k apps.
- **100km App**:
  - `Ultra100_standalone.html`: Standalone application bundle for the 100km route.
  - `build_standalone.py`: Python script compiling dependencies, templates, and GPX details.
  - `wyrypa-100km.gpx`: 100km route path file.
  - `manifest.json`: 100k app manifest configuration.
  - `sw.js`: 100k app offline service worker.
  - `icon-192.svg` & `icon-512.svg`: Lime-themed launcher icons.
- **75km App**:
  - `Ultra75_standalone.html`: Standalone application bundle for the 75km route.
  - `build_standalone_75km.py`: Python script compiling the 75km tracker.
  - `wyrypa75km.gpx`: 75km route path file.
  - `manifest_75.json`: 75k app manifest configuration.
  - `sw_75.js`: 75k app offline service worker.
  - `icon-192_75.svg` & `icon-512_75.svg`: Cyan-themed launcher icons (dynamically generated).

---

## How to Build & Update

If you update parameters, GPX tracks, or layout templates, rebuild the apps using the respective compiler scripts:

### Build the 100km App
```bash
python build_standalone.py
```
*Generates/updates: `Ultra100_standalone.html`, `manifest.json`, and `sw.js`.*

### Build the 75km App
```bash
python build_standalone_75km.py
```
*Generates/updates: `Ultra75_standalone.html`, `manifest_75.json`, `sw_75.js`, `icon-192_75.svg`, and `icon-512_75.svg`.*

---

## v2 Unified React App (`v2_unified/`)
A modern, React-based (Vite) Unified Tracking Engine designed to replace the legacy standalone scripts.
- **Unified Engine**: A single app handling multiple dynamic datasets (`dataset.json`).
- **Dynamic Start Time & Pace Tracking**: Live "Pace vs Plan" delta and exact clock "ETA" calculations driven by the user's adjustable Start Time.
- **Interactive Offline Mapping**: Caches Leaflet maps with live stats monitoring, graceful tile resuming, and robust auto-centering when pinning checkpoints.
- **Modern UI**: Floating map modals (configurable for mobile), sticky tables, and responsive tracker cards.

### V2 Documentation
All product requirements, architecture notes, and progress walkthroughs for the unified engine are tracked in the `/docs/v2/` directory:
- [v2_prd.md](docs/v2/v2_prd.md)
- [current_architecture.md](docs/v2/current_architecture.md)
- [walkthrough.md](docs/v2/walkthrough.md)
- [route_analysis_prompt.md](docs/v2/route_analysis_prompt.md)

### Build the Unified App
```bash
cd v2_unified/engine
npm run build
```
*Generates: Production build inside `v2_unified/engine/dist/`.*
