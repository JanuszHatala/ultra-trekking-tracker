# Reverting to Legacy App UI Structure

The previous implementation successfully introduced the new **Topological Checkpoint Engine** (which automatically slices the GPX based on peaks/valleys) and the **Dynamic Dataset Injection** (which styles the app based on JSON). However, it stripped away the familiar split-screen desktop layout, map controls, missing tabs, and detailed data columns that are crucial for the tracking experience. 

This plan addresses rewriting the React front-end to match the legacy HTML/JS layout exactly. The topological engine and React component structure will be preserved, but the layout and features will be scaled up.

## Proposed Changes

### 1. App Layout Architecture
The `App.jsx` layout will be rewritten to match the legacy responsive grid:
- **Desktop**: A `flex flex-row` layout. 
  - Left pane (`w-[45%]`) containing the Leaflet Map.
  - Middle resizer (draggable handle).
  - Right pane (`flex-1`) containing the tabs and scrollable content.
- **Mobile**: The map will sit sticky at the top (`h-[33vh]`), while the right pane flows below it.

### 2. Map Features (`MapRenderer.jsx`)
- Re-color the GPX track to red (`#ef4444`) to match legacy.
- Add Map controls using `react-leaflet` extensions or custom DOM overlays:
  - Zoom in/out buttons on the left.
  - Toggle Map Visibility button (only on mobile).
  - "Start GPS Tracking" arrow button (hooks into `navigator.geolocation` to follow user).
  - Checkpoint markers will be recreated as circular badges with the section number inside, featuring a green border, just like legacy.

### 3. Overview Tab & Settings Panel
- The Settings panel will be fully recreated:
  - Start Time input (`type="time"`).
  - GPS Interval select dropdown.
  - Download Offline Map button (with cache visualizer).
  - PL / EN toggle.
- Challenge Parameters panel will be hooked up to the newly added fields in `dataset.json`:
  - 🗓️ Date
  - 🏃‍♂️ Weight
  - ❤️ Target BPM
  - ⏱️ Goal Time
- GPS Tracker Card will be restored to show "Moja Pozycja" with a progress bar, current section, and ETA.
- The `ElevationProfile.jsx` canvas will be updated to:
  - Add green dots (`arc`) at checkpoint coordinates.
  - Expose an `onHover` callback that passes the hovered `dist` back up to `App.jsx`, which will then drop a temporary marker on the Leaflet map to sync the map to the chart hover.

### 4. Data Table Expansion (`DataTable.jsx`)
The data table columns will be expanded to match the legacy tracker:
- **KM** (with map pin icon to snap GPS to that point).
- **TIME**: Elapsed time + Delta time for section.
- **AVG TOTAL**: Pace (min/km) + Speed (km/h) from start.
- **SECTION AVG**: Pace (min/km) + Speed (km/h) for the section.
- **ELE**: Increment (+m) + Total Ascend (Σ +m).
- **ACTION**: Text from LLM.
- **PROFILE**: A small `<canvas>` sparkline drawn for that specific section chunk.

### 5. Restoring Missing Tabs
We will add `Tests.jsx` and `Training.jsx` to render the newly added JSON dataset schemas. `RichTabRenderer.jsx` will be used for Tactics, Inventory, Schedule, Tests, and Training.

## User Review Required

> [!WARNING]
> This requires a significant rewrite of `App.jsx`, `DataTable.jsx`, and `MapRenderer.jsx`. The topological math services `GpsEngine.js` will remain untouched as they work perfectly.

> [!IMPORTANT]
> The Prompt 2 (LLM Strategist) schema has already been updated to generate the `challengeParameters`, `tests`, and `training` blocks so the React app has data to fill those restored tabs. I will regenerate the MSB dataset based on this new prompt before implementing the UI, so we have real data to test with.

## Verification Plan
1. Delete the old `v2_unified` UI components.
2. Regenerate the `dataset.json` with the new Prompt 2 to include Tests, Training, and Challenge Parameters.
3. Build the split-screen layout and test resizing.
4. Implement the complex Data Table and verify all columns calculate correctly (using `GpsEngine.calculateETAs`).
5. Ensure Map hover sync works seamlessly with the Elevation Profile.
6. Verify offline map caching buttons are wired up.
7. Provide the development URL for manual testing.
