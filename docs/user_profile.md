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

To calculate the estimated segment time, use the following algorithm. It is optimized for the biomechanics of walking with a heavy backpack and avoids complex LaTeX formatting, making it fully readable by any AI and text exporter.

### **Main Segment Time Formula:**

Segment_Time_Minutes = ((Distance_km _ Base_Pace) + (Total_Ascent_meters / 100 _ Ascent_Penalty) - (Total_Descent_meters / 100 _ Descent_Bonus)) _ Fatigue_Multiplier \* Weather_Multiplier

#### **Model Constants:**

- **Comfort Base Pace:** 12.5 min/km (equivalent to a speed of 4.8 km/h) on flat terrain (slope up to 2%).
- **Race Base Pace:** 11.0 min/km (speed of 5.45 km/h).
- **Ascent Penalty:** +15.0 minutes added to the segment time for every 100 meters of positive elevation gain (UP).
- **Descent Bonus:** -4.0 minutes subtracted from the segment time for every 100 meters of elevation loss (DOWN).
  - _Descent Speed Cap (Knee Protection):_ Due to heavy load-bearing forces on knee joints and metatarsals under a 12 kg pack, descent speed is strictly capped. The maximum allowed pacing on descents is 13.5 min/km (speed of 4.4 km/h). Going faster drastically accelerates tissue and joint damage.

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

Fatigue_Multiplier = 1.0 + (Fatigue_Coefficient \* Cumulative_Distance_km)

- **Standard Fatigue Coefficient (Optimal Fueling):** 0.002
  - Example: At kilometer 50, pace slows down by 10% (multiplier 1.1). At kilometer 75, it slows down by 15% (multiplier 1.15). This assumption holds true only with flawless nutrition and hydration.
- **Crisis Fatigue Coefficient (Dehydrated/Unfueled):** If you neglect hydration or carbohydrate intake, this coefficient doubles to **0.004**, causing a crippling 30% pace slowdown at kilometer 75.

### **B. Biomechanic Foot Pain Point (FPP)**

- **Historical Limit (Without orthotic insoles & in the rain):** 45 km - 50 km.
- **Degradation Mechanism:** Dynamic compression of the metatarsal fat pads. Once this threshold is crossed, the bones press directly onto the plantar nerves and fascia, triggering a paralyzing, burning pain.
- **Impact of Moisture (Rain):** Skin maceration (softening of the epidermis) reduces the skin's resistance to shear forces by 90%. This accelerates foot pain and blisters by about 10 km (moving the FPP to 35 km - 40 km).
- **New Orthotic Insoles Target:** Distributing the pressure across the entire sole, supporting both the longitudinal and transverse arches. Target FPP upon full adaptation: **70+ km**.

## **5. NUTRITION & HYDRATION PROTOCOL (Target: 60-80g Carbs/h)**

### **A. Approved Fuels (High performance, zero gastrointestinal issues)**

- **Hyper-Mix (Maltodextrin + Fructose in a 2:1 ratio):** Main source of carbohydrates. Absorbed via two independent intestinal transporters, preventing digestive blockages.
- **Energy Gels (preferably Liquid type):** Fast, simple sugars to swallow quickly without requiring large amounts of water.
- **Salty Snacks (Kabanosy, Crackers, Salted Peanuts):** Essential to break up the sweet taste (preventing nausea) and as a natural source of sodium.

### **B. Banned Products (Guaranteed gastrointestinal crisis)**

- **Heavy, high-fat solid meals (fatty shelter soups, traditional heavy dishes):** During heavy exertion, blood is shunted away from the digestive tract to the working leg muscles. Eating heavy fat causes food to sit in the stomach, resulting in immediate nausea and acute energy loss.
- **Large amounts of plain water without salt:** Flushes out sodium from the system (hyponatremia), leading directly to severe quad and calf cramps.

### **C. Sodium & Anti-Cramp Protocol**

- **General Rule:** Always wash down solid food with water containing salt or electrolytes.
- **Dosage:** Add a generous pinch (approx. 1g) of table salt to each Hyper-Mix bag. If you run out of electrolyte capsules during hot weather or cramps, place a pinch of salt directly on your tongue and wash it down with clean water from your bladder.

## **6. RECOVERY & READINESS PROTOCOL (HRV-Guided)**

This protocol monitors cardiovascular readiness and protects against overtraining based on Morning HRV (Heart Rate Variability, specifically the RMSSD parameter).

### **A. Readiness Rule:**

Do not perform any training session above Zone 1 (heart rate above 120 bpm) if your 7-day rolling average RMSSD falls below the lower boundary of your baseline envelope:

RMSSD_7day_rolling_average < RMSSD_baseline_lower_boundary

### **B. Standard HRV Measurement Protocol:**

1. **Timing:** Daily, immediately after waking up and using the restroom.
2. **Position:** Seated (prevents false readings caused by parasympathetic saturation, which often occurs when lying down).
3. **Hardware:** A heart rate chest strap (e.g., Polar H10) or a high-quality optical camera reading (e.g., HRV4Training app).
4. **Duration:** Exactly 3 minutes of quiet, natural breathing.

## **7. SYSTEM PROFILE CONFIGURATION (JSON Block)**

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
