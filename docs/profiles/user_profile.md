# **WYRYPA USER PROFILE: ENDURANCE & BIOMECHANICAL SPECIFICATION**

**User ID:** Janusz H.

**System Load Configuration (System Load):**
- Body Weight (M_body): 75 kg
- Pack Weight (M_load): 12 kg (Standard for full autonomy/winter conditions)
- Total System Mass (M_system): 87 kg

## **1. PHYSIOLOGICAL & CARDIOVASCULAR PROFILE**
- Resting Heart Rate (HR_rest): 80 bpm
- Maximum Heart Rate (HR_max): 170 bpm
- Aerobic Background Zone (Zone 2 - Aerobic Engine): 125 bpm - 140 bpm
- Anaerobic Threshold (Anaerobic Threshold): 150 bpm - 155 bpm

### **Critical Heart Rate Rule (HR Limit Rule):**
Any sustained effort exceeding a heart rate of 155 bpm under a 12 kg load triggers rapid glycogen depletion in the muscles. This guarantees hitting the "wall" (complete energy depletion) in under 90 minutes. On steep climbs, the heart rate must be kept strictly below this limit, even if it means drastically slowing down.

## **2. MATHEMATICAL PACING MODEL (ADJUSTED FOR 12 KG LOAD)**
To calculate the estimated segment time, use the following algorithm. It is optimized for the biomechanics of walking with a heavy backpack.

### **Main Segment Time Formula:**
`Segment_Time_Minutes = ((Distance_km * Base_Pace) + (Total_Ascent_meters / 100 * Ascent_Penalty) - (Total_Descent_meters / 100 * Descent_Bonus)) * Fatigue_Multiplier * Weather_Multiplier`

#### **Model Constants & Historical Baselines:**
- **Comfort Base Pace:** 12.5 min/km (equivalent to a speed of 4.8 km/h) on flat terrain (slope up to 2%).
- **Race Base Pace:** 11.0 min/km (speed of 5.45 km/h).
- **Observed Ultra Baseline Pace (Flat/Mild Terrain):** ~13:45 to 14:15 min/km.
- **Ascent Penalty:** +15.0 minutes added to the segment time for every 100 meters of positive elevation gain (UP). *(Observed on steep ascents: pace drops to ~16:00 min/km).*
- **Descent Bonus:** -4.0 minutes subtracted from the segment time for every 100 meters of elevation loss (DOWN).
- **Descent Speed Cap (Knee Protection):** Due to heavy load-bearing forces on knee joints and metatarsals under a 12 kg pack, descent speed is strictly capped at **13.5 min/km** (speed of 4.4 km/h). Going faster drastically accelerates tissue and joint damage.

## **3. SLOPE BUCKETS & STRATEGIC PACING**
Recommended pacing frameworks based on terrain slope (S - slope in %):

1. **Flat Terrain and Plateaus (S from 0% to 5%):**
   - Method: Dynamic, long stride. Relaxed arms, poles used only to maintain rhythm.
   - Target Pace: 11:45 to 13:00 min/km.
2. **Moderate Climb (S from 6% to 12%):**
   - Method: Power hiking. Active, strong stride, poles begin to take on weight.
   - Target Pace: 13:30 to 16:30 min/km.
3. **Steep Climb (S from 13% to 19%):**
   - Method: Short, power stride. Poles work very hard, absorbing up to 20% of total mass.
   - Target Pace: 16:30 to 22:00 min/km.
4. **Extreme Climbs and "Walls" (S above 20%):**
   - Method: Very short stride ("strength step"). Focus solely on rhythmic breathing and heart rate control (max 145 bpm).
   - Target Pace: Slower than 22:00 min/km.

## **4. FATIGUE CURVE & BIOMECHANICAL BARRIERS**

### **A. Dynamic Fatigue Multiplier (Fatigue Decay)**
Performance drop-off (accumulated fatigue) is modeled as a linear function of the total distance covered:
`Fatigue_Multiplier = 1.0 + (Fatigue_Coefficient * Cumulative_Distance_km)`

- **Standard Fatigue Coefficient (Optimal Fueling):** 0.002
  - *Historical observation:* The pace degrades by roughly +30 to +45 seconds/km after 60km. In the final 20km of a 100km race, pace holds steady at ~14:20 min/km despite fatigue.
- **Crisis Fatigue Coefficient (Dehydrated/Unfueled):** If you neglect hydration or carbohydrate intake, this coefficient doubles to **0.004**, causing a crippling 30% pace slowdown at kilometer 75.

### **B. Biomechanic Foot Pain Point (FPP)**
- **Historical Limit (Without orthotic insoles & in the rain):** 45 km - 50 km.
- **Degradation Mechanism:** Dynamic compression of the metatarsal fat pads. Once this threshold is crossed, the bones press directly onto the plantar nerves and fascia, triggering a paralyzing, burning pain.
- **Impact of Moisture (Rain):** Skin maceration reduces the skin's resistance to shear forces by 90%. This accelerates foot pain and blisters by about 10 km (moving the FPP to 35 km - 40 km).
- **New Orthotic Insoles Target:** Distributing the pressure across the entire sole. Target FPP upon full adaptation: **70+ km**.

## **5. NUTRITION & HYDRATION PROTOCOL (Target: 60-80g Carbs/h)**

### **A. Approved Fuels**
- **Hyper-Mix (Maltodextrin + Fructose 2:1):** Main source of carbohydrates. 1 flask is consumed approximately every 4-5 hours (or every 20-25km).
- **Energy Gels (Liquid type):** Fast sugars.
- **Salty Snacks (Kabanosy, Crackers, Peanuts):** Essential to break up the sweet taste.
- **Solid Food Window:** Consumed early in the race only (e.g., Sandwich at km 15, Banana at km 35).
- **Transition to Liquids Only:** By km 85, solid food is completely stopped. The stomach only accepts Energy Gels and liquids from this point to the finish line.

### **B. Banned Products**
- **Heavy, high-fat solid meals:** Causes food to sit in the stomach, resulting in immediate nausea and acute energy loss.
- **Large amounts of plain water without salt:** Leads directly to severe quad and calf cramps.

### **C. Sodium & Anti-Cramp Protocol**
- **General Rule:** Always wash down solid food with water containing salt or electrolytes. 
- **Baseline Dosage:** 2x SaltStick capsules are taken every 4-5 hours to prevent cramps.
- **Crisis Dosage:** Add a generous pinch (approx. 1g) of table salt to each Hyper-Mix bag. If racing during summer daylight or out of capsules, place a pinch of salt directly on your tongue.

## **6. TACTICAL CRISIS MANAGEMENT (Historical 100k Triggers)**
- **Night Crisis (circa km 45, 05:20 AM):** Sleep deprivation hits hard. Protocol: Drink Red Bull #1 + Glucose 1WW.
- **Heat Crisis (circa km 80, 14:11 PM):** If racing during summer daylight. Protocol: Red Bull #2 + Max Salt + Liquid only.
- **Footwear/Hygiene (The "Przepak"):** A mandatory 30-minute drop-bag break occurs around 60% of the distance (km 60). Actions: Change shoes, eat hot soup, access drop bag.
- **Micro-breaks:** 5-minute stops are utilized for critical maintenance (e.g., changing socks at km 25) rather than pure rest.

## **7. RECOVERY & READINESS PROTOCOL (HRV-Guided)**
This protocol monitors cardiovascular readiness and protects against overtraining based on Morning HRV (Heart Rate Variability, specifically the RMSSD parameter).

### **A. Readiness Rule:**
Do not perform any training session above Zone 1 (heart rate above 120 bpm) if your 7-day rolling average RMSSD falls below the lower boundary of your baseline envelope:
`RMSSD_7day_rolling_average < RMSSD_baseline_lower_boundary`

### **B. Standard HRV Measurement Protocol:**
1. **Timing:** Daily, immediately after waking up and using the restroom.
2. **Position:** Seated.
3. **Hardware:** A heart rate chest strap (e.g., Polar H10) or a high-quality optical camera reading.
4. **Duration:** Exactly 3 minutes of quiet, natural breathing.

## **8. SYSTEM PROFILE CONFIGURATION (JSON Block)**
```json
{  
 "profile": {  
 "athlete": "Janusz H.",  
 "mass_body_kg": 75,  
 "mass_gear_kg": 12,  
 "metrics": {  
 "hr_rest": 80,  
 "hr_max": 170,  
 "hr_z2_min": 125,  
 "hr_z2_max": 140  
 },  
 "pacing_model": {  
 "pace_base_min_km": 12.5,  
 "ascent_penalty_min_100m": 15.0,  
 "descent_bonus_min_100m": 4.0,  
 "descent_speed_limit_min_km": 13.5,  
 "fatigue_coefficient_beta": 0.002  
 },  
 "hydration": {  
 "fluid_limit_ml_h": 400,  
 "sodium_target_mg_l": 750  
 },  
 "nutrition": {  
 "carbs_target_g_h": 65,  
 "carb_ratio_malto_fructose": "2:1"  
 }  
 }  
}
```
