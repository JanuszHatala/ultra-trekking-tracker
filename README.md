# 100km Ultra-Trekking Tracker Dashboard

An interactive, installable mobile-optimized PWA application designed for preparation and real-time offline strategy tracking during a 100km ultra-trekking challenge.

## Features
- **Interactive Checkpoint Timeline**: Zoom and focus on specific checkpoints, pacing, and scheduled actions.
- **Dynamic Track Highlights**: Clicking on any table row highlights that specific GPX section on the Leaflet map in blue.
- **Pace and Elevation Charts**: In-depth analysis of elevation profiles, tempo decay models, and slope-based limits.
- **Offline Support (PWA)**: Automatically caches all Leaflet maps, styles, scripts, and track details to remain functional on-trail in areas without cell coverage.
- **Language Toggle**: Full support for both Polish and English.

## File Structure
- `index.html`: The main web application page (compiled standalone HTML containing all assets).
- `build_standalone.py`: A Python compiler script that downloads dependencies, reads the GPX track, and bundles everything into the final single file.
- `wyrypa-100km.gpx`: The official route GPX coordinates.
- `manifest.json`: Configuration for mobile installation (PWA support).
- `sw.js`: Service worker code caching crucial files for offline functionality.
- `icon-192.svg` & `icon-512.svg`: Beautiful matching branding launcher icons.

## How to Build/Update
If you change the GPX track or want to update parameters in `build_standalone.py`, compile the app by running:
```bash
python build_standalone.py
```
This updates `index.html` (the homepage), `Ultra100_standalone.html`, and `manifest.json` automatically.
