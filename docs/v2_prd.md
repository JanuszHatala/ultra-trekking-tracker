# V2 React Engine: Full UI Legacy Match PRD

## Core Objective
Recreate and enhance the exact UI layout, tab structure, and map behavior of the legacy app while replacing the static data layer with the new **Topological GPX Engine** and LLM-driven `dataset.json`. The new system builds topological checkpoints dynamically and powers the UI with extensive JSON datasets generated via strict prompts.

## Architecture
- **Data Engine**: `GpsEngine.js` parses GPX files, calculates Haversine distances, and runs a Topological Checkpoint Algorithm (Anchored Sliding Window) to find peaks, valleys, and distance markers.
- **Storage**: `StorageEngine.js` manages local state with `localforage`, aggressively clearing the cache when new datasets or GPX files are loaded to prevent stale topology crashes.
- **Offline Maps**: `MapOfflineService.js` and `sw.js` (Service Worker) intercept tile requests, fetch, and cache map tiles (zooms 11-17 with dynamic buffering) via the browser Cache API for 100% offline navigation.
- **Live GPS Tracking**: `GpsTrackingService.js` manages `navigator.geolocation`, throttles updates based on a user-defined interval, intelligently snaps to the nearest GPX path, and provides real-time distance and accuracy metrics.
- **State Management**: React state in `App.jsx` controls the selected/hovered section, map visibility, and synchronization between the Data Table and MapRenderer.

## UI / UX Specifications

### Split-Screen Layout
- **Left Pane (Map)**: `45%` width on desktop, sticky top 33vh on mobile.
- **Resizer**: Draggable handle between panes.
- **Right Pane (Content)**: `55%` width, contains the Title, Language Switcher, and Tab Bar.

### Map Capabilities (`MapRenderer.jsx`)
- Render GPX trace in **RED** (`#ef4444`).
- **Checkpoints:** Numbered circle markers matching the section numbers. The initial Start point is marked with an "S". Clicking a marker reveals a popup containing:
  - Checkpoint Name, Distance, Total Ascent
  - ETA
  - Action/Tactical advice derived from the action timeline
  - *Note:* The display of this popup can be suppressed via the `Auto-open map popup` setting (default off on mobile).
- **Live GPS Tracking:** Driven solely by `gpsState`, displaying a pulsing ring indicating accuracy and an inner dot indicating route status (green for on-route, yellow for off-route). Live position is automatically synced to the map and Data Table highlighting.
- **Hover/Tracking Effects:** Hovering over a section in the Data Table or moving via Live GPS tracking highlights the corresponding polyline section and adds a pulsing red `MapHoverSync` marker at the checkpoint destination.
- **Overlay Controls:** Floating action buttons for hiding the map, showing current GPS position via `getCurrentPosition` panning, fitting track to view (Maximize), and toggling live GPS tracking (Navigation).
- **Route Elevation Profile:** Full-width profile with slope-colored stroke:
  - Red: Steep uphill (>15%)
  - Orange: Uphill (5% to 15%)
  - Lime Green: Flat (-5% to 5%)
  - Dark Green: Downhill (-15% to -5%)
  - Blue: Steep downhill (<-15%)
- **Hover Sync:** Hovering over the elevation profile renders a pink dot on the main map.
- **Interactions**: Map dynamically pans or fits bounds based on table row hovering or clicking.

### Tab Structure
1. **Overview**:
   - **Settings Panel**: Start Time picker, GPS Interval dropdown, Download Offline Map button (wired to `MapOfflineService` with real progress bar, retry logic, resume capability, and visible `Tile Cache Stats`), Auto-open map popup toggle, and a pill-style active PL/EN language toggle switch.
   - **Challenge Parameters**: Read from `dataset.json` (Date, Weight, Target BPM, Goal Time).
   - **GPS Tracker Card ("My Position")**: Displays when a section is pinned. Shows distance progress bar, Current Section name, live **Pace vs Plan** delta, and exact clock **ETA**, both calculated dynamically based on the configurable `Start Time`.
2. **Data Table**:
   - **First Row**: The initial `0 km` point is visually stripped from the table to prevent confusion; only actual sections are shown.
   - **Columns**: 
     - `Nr` (Styled circle with section number)
     - `KM` (Cumulative distance + Section length secondary info + MapPin icon)
     - `Time` (Total ETA + Section time)
     - `Avg Total` (Pace + km/h)
     - `Section Avg` (Pace + km/h)
     - `ELEVATION` (Total Accumulated Gain + Section Ascent/Descent)
     - `Action` (Dynamically aggregated text from the Action Timeline)
     - `Profile` (Sparkline canvas showing elevation mini-chart)
   - **Summary Row**: The table footer (`<tfoot>`) displays totals for Distance, ETA, Average Pace, Average Speed, and Total Gain/Loss.
   - **Interactions**: 
     - Row hover highlights the section on the map (temporary overlay).
     - Row click "pins" the section for tracking, explicitly overriding the live GPS tracking and displaying it in the GPS Tracker Card in the Overview tab. Clicking again unpins it.
     - Live GPS Tracking automatically evaluates the current section based on position and highlights the corresponding row in real-time.
     - Clicking the Sparkline Profile opens a full-screen Modal displaying a larger, detailed view of that section's elevation profile.
3. **Schedule**: Detailed timeline format from LLM dataset, divided by phases, describing exact pacing, mental strategies, and drop-bag protocols.
4. **Tactics**: Recreated from legacy hardcoded text (e.g., Uphills, Downhills, Flat conservation, Crisis protocols).
5. **Inventory**: Rendered as Pills and Critical Item lists (Mandatory Gear, Nutrition, Medical) from LLM dataset.
6. **Tests**: Pre-race testing protocols (e.g., Gear tests, 50km load tests).
7. **Training**: Pre-race training plan (e.g., Base Building, Tapering).

## Dataset Expansion (`msb_dataset.json`)
The `dataset.json` must be generated using the strictest level of detail via the `route_analysis_prompt.md`, yielding a comprehensive tactical document rather than a minimal MVP. It includes:
- Extrapolated `actionTimeline` with hourly granularity.
- Rigorous `schedule` outlining phases of the race.
- `tactics`, `inventory`, `tests`, and `training` nodes filled with professional-level ultra-trekking advice and protocols.
