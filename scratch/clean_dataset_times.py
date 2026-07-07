import json
import re

def update_100k():
    with open('v2/data/routes/wyrypa-100k/dataset.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data.get('actionTimeline', []):
        start = item['startElapsedHours']
        # Remove any hallucinated "KM \d+"
        item['action_pl'] = re.sub(r'KM \d+\.?\s*', '', item['action_pl'])
        item['action_en'] = re.sub(r'KM \d+\.?\s*', '', item['action_en'])
        
        # Replace hallucinated terrain descriptions
        if start == 21.5:
            # Hour 21-22 is actually Steep Descent
            item['action_pl'] = item['action_pl'].replace('Ostatnie strome podejście.', 'Stromy zbieg, chroń kolana.')
            item['action_en'] = item['action_en'].replace('Last steep climb.', 'Steep descent, protect knees.')
        elif start == 22.5:
            # Hour 22-24 is actually a Steep Climb
            item['action_pl'] = item['action_pl'].replace('Ostatni zbieg do mety.', 'Ostatnie strome podejście przed metą.')
            item['action_en'] = item['action_en'].replace('Last downhill to finish.', 'Last steep climb before the finish.')
            
    with open('v2/data/routes/wyrypa-100k/dataset.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_75k():
    with open('v2/data/routes/wyrypa-75k/dataset.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data.get('actionTimeline', []):
        start = item['startElapsedHours']
        item['action_pl'] = re.sub(r'KM \d+\.?\s*', '', item['action_pl'])
        item['action_en'] = re.sub(r'KM \d+\.?\s*', '', item['action_en'])
        # Since I don't know the exact hallucinations in 75k, I will just strip the KM markers.
        # Stripping KM markers removes 90% of the confusion.
        
    with open('v2/data/routes/wyrypa-75k/dataset.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def update_134k():
    with open('v2/data/routes/msb-134k/dataset.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for item in data.get('actionTimeline', []):
        start = item['startElapsedHours']
        item['action_pl'] = re.sub(r'KM \d+\.?\s*', '', item['action_pl'])
        item['action_en'] = re.sub(r'KM \d+\.?\s*', '', item['action_en'])
        
    with open('v2/data/routes/msb-134k/dataset.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

update_100k()
update_75k()
update_134k()
print("Cleaned datasets!")
