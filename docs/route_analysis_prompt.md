# Wyrypa Analytical Prompts

This document contains **two separate prompts** designed to be used in two different LLM sessions. 

The first prompt builds your physiological profile based on historical data. You save this profile and reuse it.
The second prompt uses your saved profile and a new GPX track to generate the app's `dataset.json`.

**CRITICAL REQUIREMENT:** 
The data you generate must be **extremely detailed, rigorous, and professional**. Do not generate casual or scanty content. For sections like `schedule`, `training`, `rules`, and `equipment`, provide comprehensive, in-depth guidelines, detailed hourly breakdowns, extensive training routines, and a full list of required gear. The user relies on this data for a serious ultra-trekking 100km+ challenge, so the level of detail must reflect the severity and extreme nature of the event.

Given the GPX parameters and the user profile below, your task is to generate a JSON response that conforms to the provided schema.

***

## Prompt 1: The Profile Builder (Use once, update occasionally)
*Use this prompt to deeply analyze your past performances and create a persistent "User Profile Document".*

**Copy and paste this into the LLM:**

```text
You are an expert sports physiologist and ultra-trekking analyst. 
My goal is to create a persistent "Ultra-Trekking User Profile" document that I can use in the future to plan new routes.

I am going to provide you with:
1. GPX tracks from my past extreme endurance challenges.
2. The final times and results of those challenges, and importantly, whether they were "casual hikes" or "extreme races" with time limits, so you can gauge my absolute maximum capacity vs my comfort pace.
3. My personal notes regarding those tracks (crises, nutrition issues, weather, how I recovered, my weight, etc.).

Your Task:
1. Extract my baseline pace on flat terrain for both casual and race efforts.
2. Calculate my pace drop-off on ascents (min/km per 100m climb) and my pace on descents.
3. Calculate my "fatigue curve" (cardiac drift, pace degradation per 20km).
4. Analyze my nutrition strategy and summarize what works and what causes crises.

Output:
Do not write a generic summary. Produce a highly structured markdown document titled "Wyrypa User Profile". This document must contain specific metrics, formulas, and tactical rules tailored to me. It must be detailed enough that another AI can use it to perfectly predict my pace on a completely new track.
```

***

## Prompt 2: The Challenge Analyst (Use for every new route)
*Use this prompt when you want to plan a new route. Feed it your saved User Profile from Prompt 1, the new GPX file, and any new constraints.*

**Copy and paste this into the LLM:**

```text
You are an expert ultra-trekking master tactician, nutritionist, and UI designer. Your goal is to help me prepare for a new extreme endurance event by creating a highly personalized `dataset.json` for my Wyrypa Tracker app.

I will provide you with:
1. My detailed "Ultra-Trekking User Profile" (which dictates my pacing, fatigue curve, and nutrition rules).
2. The raw `.gpx` file for the new challenge.
3. Constraints for this specific race (date, time limit, mandatory gear, expected weather).

Your Task:

Step 1: Information Gathering
- Before proceeding, ASK ME how many weeks I have to prepare for this challenge and how many days a week I can train.
- Wait for my response.

Step 2: Strategy & Cross-referencing
- **CRITICAL TIME LIMIT CHECK:** If the race has a strict time constraint (e.g., 100km in 24h) and my natural physiological profile indicates a collision or risk of missing the cut-off, you MUST adjust the strategy. 
- Formulate an aggressive mitigation plan (e.g., strictly limiting break times, instructing to eat while walking).
- Formulate a strict, continuous nutrition plan. Calculate exact carbohydrate, sodium, and hydration needs per segment.
- **CRITICAL**: Provide highly granular action items in `actionTimeline`. Break down instructions every 1 hour or 30 minutes (e.g., "0.0-1.0h", "1.0-2.0h"), rather than grouping them into massive multi-hour blocks. This is essential for continuous pacing.

Step 3: Present your findings to me for approval. Include the proposed Training Plan (based on the timeframe I gave you in Step 1) to elevate my abilities for this specific challenge.

Step 4: JSON Generation
Once I approve, generate the output. It must be ONLY valid JSON matching the exact schema below.

**SCHEMA & UI RULES:**
- All textual fields MUST be generated in both English and Polish (`_en` and `_pl` suffixes).
- **CRITICAL:** Do NOT attempt to calculate mathematical waypoints or 5km chunks from the GPX. The V2 React Engine will parse the GPX and do the math. Your job is ONLY to provide the human Strategy, Inventory, and UI formatting.
- You must act as the UI Designer. Assign exact `themeColor` (e.g., "red", "orange", "lime", "cyan", "blue", "purple", "gray"), `icon` (emojis), and `displayMode` ("pills" or "list") to make the data look beautiful in the React app.

SCHEMA:
```json
{
  "route_id": "unique-route-id",
  "title_pl": "Nazwa Trasy",
  "title_en": "Route Name",
  "subtitle_pl": "Lokalizacja / Nazwa Wydarzenia",
  "subtitle_en": "Location / Event Name",
  "themeColor": "lime",
  "metadata": {
    "totalDistanceKm": 100.5,
    "totalAscendM": 3200,
    "timeLimitHours": 24,
    "difficulty": "hard"
  },
  "challengeParameters": {
    "date": "2026-07-10",
    "weightKg": "80",
    "targetBpm": "130-145",
    "goalTime": "< 24h"
  },
  "actionTimeline": [
    {
      "startElapsedHours": 0.0,
      "endElapsedHours": 2.0,
      "action_pl": "Wypij 500ml izotoniku, zjedz 1 żel.",
      "action_en": "Drink 500ml isotonic, eat 1 gel."
    }
  ],
  "tactics": [
    {
      "title_pl": "Płasko (< 8%)",
      "title_en": "Flat (< 8%)",
      "description_pl": "Tempo 12:30 - 13:30 min/km.",
      "description_en": "Pace 12:30 - 13:30 min/km.",
      "themeColor": "emerald",
      "icon": "▶"
    }
  ],
  "inventory": [
    {
      "category_pl": "Jedzenie Stałe",
      "category_en": "Solid Food",
      "themeColor": "orange",
      "displayMode": "pills",
      "items": [
        { "text_pl": "6-8 Kanapek", "text_en": "6-8 Sandwiches", "icon": "🥪" },
        { "text_pl": "10 Żeli", "text_en": "10 Energy gels", "icon": "🍯" }
      ]
    },
    {
      "category_pl": "Suplementacja i Rescue",
      "category_en": "Supplementation & Rescue",
      "themeColor": "red",
      "displayMode": "list",
      "items": [
        { "text_pl": "SaltStick Caps: 30 kaps", "text_en": "SaltStick Caps: 30 caps", "icon": "💊", "isCritical": false },
        { "text_pl": "Rescue Protocol: 1 saszetka Glukozy pod język", "text_en": "Rescue Protocol: 1 sachet Glucose under tongue", "icon": "🚑", "isCritical": true }
      ]
    }
  ],
  "schedule": [
    {
      "startKm": 0,
      "endKm": 25,
      "title_en": "Continuous march.",
      "title_pl": "Marsz ciągły.",
      "dotColor": "gray"
    },
    {
      "startKm": 60,
      "endKm": 60,
      "title_pl": "Przepak",
      "title_en": "Drop Bag",
      "description_pl": "...",
      "description_en": "...",
      "dotColor": "red",
      "badges_pl": ["Jedzenie", "Zapas"],
      "badges_en": ["Food", "Spares"]
    }
  ],
  "tests": [
    {
      "title_pl": "Test A: 70 km (Balast 12 kg)",
      "themeColor": "blue",
      "description_en": "Gear and digestion test over long distance.",
      "description_pl": "Test sprzętowy i trawienny na długim dystansie.",
      "steps": [
        { "text_en": "0 - 30 km: Full supplementation regime test.", "text_pl": "0 - 30 km: Test pełnego reżimu suplementacji." }
      ],
      "goal_en": "Finish around 16.5 - 17.5h",
      "goal_pl": "Ukończenie w granicach 16.5 - 17.5h"
    }
  ],
  "training": [
    { 
      "activity_en": "MTB Bike (1x week 45-60 min)", 
      "activity_pl": "Rower MTB (1x tydz. 45-60 min)",
      "description_en": "Strength training. Steep climbs, low RPM.",
      "description_pl": "Trening siłowy. Sztywne podjazdy, niskie RPM.",
      "icon": "🚵‍♂️"
    }
  ]
}
```
```
