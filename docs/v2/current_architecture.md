# Current System Architecture: Wyrypa Ultra-Trekking

This document serves as a reference point for the current state of the Wyrypa applications before the migration to a unified, data-driven architecture.

## 1. Business / User Level Overview

### What the App Does
Wyrypa is a specialized companion application for extreme ultra-trekking events (e.g., 75km and 100km marches). It replaces traditional paper maps, printed schedules, and mental math during exhausting physical challenges.

### Key Functionalities
- **Live GPS Tracking:** Displays the user's current location on a map via a pulsing accuracy ring, dynamically calculates distance and "off route" status, and actively synchronizes with the route table to highlight the current section.
- **Offline Capabilities:** Allows downloading map tiles and operating completely without an internet connection in remote areas.
- **Dynamic Route Table:** A comprehensive waypoint table showing:
  - Section numbers mapped directly to map checkpoints (Start point is 'S').
  - Distance covered and remaining.
  - Estimated time of arrival (ETA) based on planned pace and actual start time.
  - Deadlines and cut-offs.
  - Actionable instructions for each section (e.g., "Eat 300 kcal", "Change socks", "Switch headlamp batteries").
- **Elevation Profiling:** Visualizes the elevation profile and highlights the user's current position on the profile.
- **Event Preparation:** Contains reference data for the user before the event:
  - **Inventory:** Checklists for gear, clothing, electronics, and food.
  - **Tactics:** High-level strategy for pacing, nutrition, and rest.
  - **Training & Tests:** Logs of preparation hikes and fitness tests.
- **Hub Downloader:** A native Android shell that fetches available routes from GitHub, saves them locally, and acts as an offline launcher.

---

## 2. Technical Architecture

### Current Paradigm: Static Site Generation
Currently, there is no single "Engine" that loads external data. Instead, the application relies on a **Code Generation** paradigm.

- **The Generators:** `build_standalone.py` (100km) and `build_standalone_75km.py` (75km).
- **The Process:** 
  1. The Python script contains hardcoded data arrays representing waypoints, inventory, schedule, and tactics.
  2. It reads a local `.gpx` file and parses the coordinates and elevation.
  3. It injects all of this data directly into massive strings of HTML and JavaScript.
  4. It outputs a standalone, monolithic `index.html` file into a specific folder (`/100k`, `/75k`).
- **The Delivery:** The generated folders are pushed to GitHub Pages. The Native Android App (Hub) downloads these folders verbatim and runs them locally.

### Pros and Cons of Current Architecture
**Pros:**
- Incredibly fast to load (everything is in one file).
- Zero database or backend required.
- Easy to host on GitHub Pages.

**Cons:**
- **Code Duplication:** The entire UI logic, map rendering engine, and GPS tracking code is duplicated inside both `build_standalone.py` and `build_standalone_75km.py`. Fixing a bug requires fixing it in multiple Python scripts.
- **Hard to Scale:** Adding a new route requires writing a new Python script, copying over thousands of lines of HTML string concatenation, and manually editing the hardcoded data structures within the Python code.
- **Tightly Coupled:** The data (which socks to wear at km 45) is hardcoded inside the presentation logic (the HTML table generator).

---

## 3. Data Currently Hardcoded (To be Externalized)

To move to a Unified App, the following elements currently locked inside Python must become dynamic JSON/YAML data sets:

1. **Route Metadata:** Title, subtitle, total distance, total ascend, time limit.
2. **GPX Track:** The raw coordinate path.
3. **Waypoints (The Table):** Distances, estimated paces, specific tactical notes, elevation changes, cut-off times.
4. **Inventory Checklists:** Equipment and food.
5. **Tactics & Strategy:** Textual rules for the route.
6. **Training Schedule:** Pre-event preparation milestones.
7. **Offline Map Boundaries:** The bounding box for the map downloader.
