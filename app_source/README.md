# Wyrypa V2 Unified Engine

This directory contains the new React/Vite-based **Unified Tracking Engine** for Wyrypa Ultra-Trekking events. 

The goal of this engine is to replace the legacy statically generated Python scripts with a modern, dynamic, JSON-driven application capable of parsing topological route data, executing offline Leaflet maps, and tracking live GPS progress accurately without relying on network connectivity.

## Documentation

Full architectural documentation, Product Requirements, and feature walkthroughs can be found in the root `docs/` directory:

- [Product Requirements Document (PRD)](../../docs/v2_prd.md)
- [Current Architecture (Pre-V2 state)](../../docs/current_architecture.md)
- [V2 Walkthrough & Changelog](../../docs/walkthrough.md)
- [Route Analysis Prompt](../../docs/route_analysis_prompt.md)

## Tech Stack

- **React 18** (UI and Component Tree)
- **Vite** (Build Tool & Dev Server)
- **Leaflet & React-Leaflet** (Offline Map Rendering)
- **LocalForage** (IndexedDB Storage for offline datasets)
- **Tailwind CSS** (Styling)

## Local Development

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build
```

The production output will be generated inside the `dist/` directory, ready to be deployed as a Progressive Web App (PWA).
