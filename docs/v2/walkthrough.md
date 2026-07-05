# Walkthrough: Full Legacy UI Rewrite (V2)

The Wyrypa V2 Tracker now preserves the dynamic Topological Checkpoint Engine, while perfectly matching the robust, split-screen UI of the original app.

## Changes Made

### 1. Simulated Dataset
- Generated a highly granular `msb_dataset.json` simulating an LLM output from the newly updated Prompt 2. 
- The dataset now includes `challengeParameters`, `tests`, `training`, and a highly detailed `actionTimeline` broken down every hour.
### 2. Dual-Pane Architecture
- **App.jsx** was completely rewritten to feature a dynamic flexbox grid.
- **Desktop View**: The screen splits horizontally. Left side contains the sticky Map (45% width). Right side contains the header and scrollable tabs.
- **Mobile View**: The Map sits sticky at the top (`33vh`), with content rolling underneath it.
- **Resizer**: A central dragger handle was added, allowing you to fluidly resize the map pane up to 80% of the screen width.

### 3. Missing Map Controls Restored
- **Markers**: The GPX trace is now painted Red (`#ef4444`). Standard blue Leaflet pins were replaced by custom circular divs featuring a green border and the numerical sequence of the checkpoint.
- **Controls**: Zoom controls are pinned to the top left. A toggle button ("Show/Hide Map") was added for mobile views. A GPS crosshair button was added to toggle user tracking.
- **Hover Sync**: `ElevationProfile` and `DataTable` row hovers now trigger a pink glowing marker on the Leaflet map and aggressively pan the map to that location.

### 4. Overview Tab & Components
The `Overview.jsx` component was extracted to neatly house:
- The Settings Panel: Start Time, GPS Interval, "Download Offline Map" (with mock progress bar).
- The Challenge Parameters Panel: Date, Weight, Target BPM, Goal Time (fed straight from the new JSON schema).
- The Elevation Profile Canvas: Upgraded to draw circular checkpoints and emit hover coordinates.

### 5. Detailed Data Table
`DataTable.jsx` was rewritten from scratch to restore your analytical columns:
- **KM** (Hovering displays the pink map pin).
- **TIME**: Elapsed time in orange, with section time delta below it.
- **AVG TOTAL**: Total average pace and speed from the start line.
- **SECTION AVG**: Highlighted section pace and speed.
- **ELEVATION**: Total elevation with `+` ascent and `-` descent details.
- **ACTION**: Granular LLM instructions matching the ETA window.
- **PROFILE**: Inline HTML5 `<canvas>` rendering small, accurate sparklines of the specific GPX chunk.

### 6. New Tabs
- Created `Tests.jsx` and `Training.jsx` tabs to consume and render the new pre-race data schemas defined in the prompt.

## Verification Results
- `npm run build` executed and passed with 0 errors or warnings. The Vite build bundles cleanly.
- Tested resizing logic and tab rendering.

## Next Steps
You can navigate to `C:\DevWorkspaces\jh\ProjektyIT\Ultra-Trekking-Analisys\v2_unified\engine\` and run `npm run dev` to see the new tracker live in your browser. Verify the offline map capabilities, UI flow, and data mapping.

### 7. UI & UX Polish
- **Cache Invalidation**: StorageEngine cache key logic was upgraded from `v2` to `v4` to force a wipe of stale topological calculations.
- **Dynamic Checkpoint Naming**: Topological engine checkpoints now include their exact section number and distance bounds (e.g., `Section 1 (KM 0.0 - 5.3) (Peak)`), providing immediate context in the UI.
- **Language Toggle**: Replaced the static EN/PL text button with a modern, pill-style switch that visually highlights the active language with the app's vibrant lime-green color.
- **Map Marker Alignment**: The initial starting point on the map is now labeled "S", allowing all subsequent checkpoints to perfectly match their corresponding section numbers from the Data Table.
- **Data Table Pinning Fixed**: Resolved an issue where the map's hover state overrode the pinning state; you can now successfully click a row to lock it into the GPS Tracker Card, and click again to unlock.
