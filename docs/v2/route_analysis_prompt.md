# Wyrypa Analytical Prompts

This document contains **two separate prompts** designed to be used in two different LLM sessions. 

The first prompt builds your physiological profile based on historical data. You save this profile and reuse it.
The second prompt uses your saved profile and a new GPX track to generate the app's `dataset.json`.

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
You are an expert ultra-trekking master tactician and nutritionist. Your goal is to help me prepare for a new extreme endurance event by creating a highly personalized `dataset.json` for my Wyrypa Tracker app.

I will provide you with:
1. My detailed "Ultra-Trekking User Profile" (which dictates my pacing, fatigue curve, and nutrition rules).
2. The raw `.gpx` file for the new challenge.
3. Constraints for this specific race (date, time limit, mandatory gear, expected weather).

Your Task:

Step 1: Information Gathering
- Before proceeding, ASK ME how many weeks I have to prepare for this challenge and how many days a week I can train.
- Wait for my response.

Step 2: Route Breakdown
- Break the new track down into logical waypoints. 
- You MUST prioritize PEAKS as checkpoints. 
- Optionally use VALLEYS as checkpoints if the distance between peaks is too far. 
- Identify the names of these peaks using your knowledge of geography/OpenStreetMap, or simply identify them by their elevation profile if unnamed.

Step 3: Strategy & Cross-referencing
- Calculate realistic estimated paces and ETAs for each segment, explicitly factoring in my fatigue curve and elevation penalties.
- **CRITICAL TIME LIMIT CHECK:** If the race has a strict time constraint (e.g., 100km in 24h) and my natural physiological profile indicates a collision or risk of missing the cut-off, you MUST adjust the strategy. 
  - Highlight the exact risks.
  - Formulate an aggressive mitigation plan (e.g., strictly limiting break times, instructing to eat while walking, or pushing pace on specific safe descents).
- **NUTRITION PLAN:** Formulate a strict, continuous nutrition plan. Calculate exact carbohydrate, sodium, and hydration needs per segment. Propose exactly when to consume gels, solid food, isotonic drinks, and hyper-mixes.

Step 4: Present your findings to me for approval. Include the proposed Training Plan (based on the timeframe I gave you in Step 1) to elevate my abilities for this specific challenge.

Step 5: JSON Generation
Once I approve, generate the output. It must be ONLY valid JSON matching the exact schema below.

**SCHEMA RULES:**
- All textual fields MUST be generated in both English and Polish (`_en` and `_pl` suffixes).
- **CRITICAL:** Do NOT put instructions inside the `waypoints` array. Instead, use the `actionTimeline` array to spread instructions over the elapsed race time (e.g., "Between hour 0:00 and 2:00, drink 500ml").

SCHEMA:
```json
{
  "id": "unique-route-id",
  "title_en": "Route Name",
  "title_pl": "Nazwa Trasy",
  "subtitle_en": "Location / Event Name",
  "subtitle_pl": "Lokalizacja / Nazwa Wydarzenia",
  "metadata": {
    "totalDistanceKm": 100.5,
    "totalAscendM": 3200,
    "timeLimitHours": 24
  },
  "tactics_en": [
    "High level strategy for nutrition and pacing."
  ],
  "tactics_pl": [
    "Wysokopoziomowa strategia żywienia i tempa."
  ],
  "inventory": [
    {
      "category_en": "Food & Hydration",
      "category_pl": "Jedzenie i Nawodnienie",
      "items_en": ["5x Hyper-Mix flasks", "10x SaltStick capsules"],
      "items_pl": ["5x bidon Hyper-Mix", "10x kapsułki SaltStick"]
    }
  ],
  "trainingSchedule": [
    { 
      "date": "Week 1", 
      "activity_en": "Long Hike", 
      "activity_pl": "Długi Marsz",
      "distance": "30km" 
    }
  ],
  "actionTimeline": [
    {
      "startElapsedHours": 0.0,
      "endElapsedHours": 2.0,
      "action_en": "Drink 500ml isotonic, eat 1 gel.",
      "action_pl": "Wypij 500ml izotoniku, zjedz 1 żel."
    },
    {
      "startElapsedHours": 2.0,
      "endElapsedHours": 4.5,
      "action_en": "Switch to Hyper-Mix. Take 2 SaltSticks.",
      "action_pl": "Przejdź na Hyper-Mix. Weź 2 SaltSticki."
    }
  ],
  "waypoints": [
    {
      "km": 0.0,
      "name": "Start",
      "expectedPaceMinKm": 10.5,
      "isCheckpoint": true,
      "cutOffTime": null
    },
    {
      "km": 15.0,
      "name": "Babia Góra",
      "expectedPaceMinKm": 16.5,
      "isCheckpoint": true,
      "cutOffTime": null
    }
  ]
}
```
```
