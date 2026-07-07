import json
import re
import subprocess

def get_topography(gpx_file):
    # Run the script and parse stdout
    result = subprocess.run(['python', 'analyze_gpx_topography.py', gpx_file], capture_output=True, text=True)
    lines = result.stdout.split('\n')
    
    topo_dict = {}
    for line in lines:
        if ' - ' in line and '|' in line and not 'Hour' in line:
            parts = line.split('|')
            if len(parts) >= 5:
                hour_range = parts[0].strip()
                km_range = parts[1].strip()
                ascent = parts[2].strip()
                descent = parts[3].strip()
                terrain = parts[4].strip()
                
                try:
                    start_hr = float(hour_range.split('-')[0].strip())
                    topo_dict[start_hr] = {
                        'km_range': km_range,
                        'ascent': ascent,
                        'descent': descent,
                        'terrain': terrain
                    }
                except:
                    pass
    return topo_dict

TERRAIN_PL = {
    "Steep Climb": "Strome Podejście",
    "Climb": "Podejście",
    "Steep Descent": "Stromy Zbieg",
    "Descent": "Zbieg",
    "Hilly/Mixed": "Teren Mieszany",
    "Flat/Rolling": "Płasko/Lekko falisto"
}

def clean_action(text_pl, text_en, start_hr, topo):
    # Remove hallucinatory KM references
    text_pl = re.sub(r'(?i)KM \d+\.?\d*\.?\s*', '', text_pl)
    text_en = re.sub(r'(?i)KM \d+\.?\d*\.?\s*', '', text_en)
    
    # Remove hallucinatory topography words that might contradict
    bad_pl = [r'(?i)ostatnie strome podejście', r'(?i)ostatni zbieg', r'(?i)podejście', r'(?i)zbieg', r'(?i)szczyt']
    bad_en = [r'(?i)last steep climb', r'(?i)last downhill', r'(?i)climb', r'(?i)descent', r'(?i)downhill', r'(?i)peak']
    for b in bad_pl: text_pl = re.sub(b, '', text_pl)
    for b in bad_en: text_en = re.sub(b, '', text_en)
    
    # Clean up double spaces or floating punctuation
    text_pl = re.sub(r'\s+', ' ', text_pl).replace(' .', '.').strip()
    text_en = re.sub(r'\s+', ' ', text_en).replace(' .', '.').strip()
    
    # Prepend the true topography!
    if start_hr in topo:
        t = topo[start_hr]
        pl_prefix = f"[{t['km_range']}km | {TERRAIN_PL.get(t['terrain'], t['terrain'])}] "
        en_prefix = f"[{t['km_range']}km | {t['terrain']}] "
        
        text_pl = pl_prefix + text_pl
        text_en = en_prefix + text_en
        
    return text_pl, text_en

def process_dataset(json_path, gpx_path):
    print(f"Processing {json_path}...")
    topo = get_topography(gpx_path)
    
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data.get('actionTimeline', []):
        start = item['startElapsedHours']
        pl, en = clean_action(item['action_pl'], item['action_en'], start, topo)
        item['action_pl'] = pl
        item['action_en'] = en
        
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    process_dataset('v2/data/routes/wyrypa-100k/dataset.json', 'wyrypa-100km.gpx')
    process_dataset('v2/data/routes/wyrypa-75k/dataset.json', 'wyrypa75km.gpx')
    process_dataset('v2/data/routes/msb-134k/dataset.json', 'v2/data/routes/msb-134k/route.gpx')
    print("All datasets accurately updated with GPX topography!")
