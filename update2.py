import re

with open('build_standalone_75km.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix Title
content = content.replace('<title>100km Ultra-Trekking Tracker (Offline)</title>', '<title>75km Ultra-Trekking Tracker (Offline)</title>')

# Fix Challenge parameters: Date removal and Goal update
# Remove Date
content = re.sub(r'<div class="flex items-center space-x-2">\s*<span class="bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1\.5 rounded border border-slate-700 shadow-sm w-full font-semibold text-xs md:text-sm">🗓️ <span class="lang-pl">10 lipca 2026</span><span class="lang-en">July 10, 2026</span></span>\s*</div>\s*', '', content, flags=re.DOTALL)

# Update Goal
content = content.replace('⏱️ <span class="lang-pl">Cel: &lt; 24h</span><span class="lang-en">Goal: &lt; 24h</span>', '⏱️ <span class="lang-pl">Cel: ~16-17h</span><span class="lang-en">Goal: ~16-17h</span>')


# Checkpoints JSON update (Updating only time, pace, and actions based on the new table)
# (Coordinates and bounds stay the same from previous generation)
new_checkpoints_json = '''[
  {
    "km": 5,
    "lat": 49.777544,
    "lon": 19.113625,
    "time": "20:03",
    "pace": "12:39",
    "ele": "+500 m",
    "action": "Wypij 1. bidon izotoniku, baton.",
    "action_en": "Drink 1st isotonic flask, energy bar.",
    "bounds": [[49.776947, 19.096194], [49.795845, 19.128895]]
  },
  {
    "km": 10,
    "lat": 49.784075,
    "lon": 19.104631,
    "time": "21:02",
    "pace": "11:48",
    "ele": "+176 m",
    "action": "Weź kapsułki z solą / słone jedzenie.",
    "action_en": "Take salt capsules / salty food.",
    "bounds": [[49.777253, 19.095909], [49.795845, 19.113625]]
  },
  {
    "km": 15,
    "lat": 49.775386,
    "lon": 19.105436,
    "time": "22:05",
    "pace": "12:40",
    "ele": "+405 m",
    "action": "Zjedz kanapkę.",
    "action_en": "Eat a sandwich.",
    "bounds": [[49.774707, 19.10206], [49.784075, 19.128324]]
  },
  {
    "km": 20,
    "lat": 49.77777,
    "lon": 19.122489,
    "time": "23:11",
    "pace": "13:04",
    "ele": "+482 m",
    "action": "Opróżnij bidon.",
    "action_en": "Empty flask.",
    "bounds": [[49.77403, 19.086939], [49.77777, 19.122489]]
  },
  {
    "km": 25,
    "lat": 49.76596,
    "lon": 19.108642,
    "time": "00:12",
    "pace": "12:11",
    "ele": "+159 m",
    "action": "Kontrola stóp. Zmiana skarpet. Baton.",
    "action_en": "Check feet. Change socks. Energy bar.",
    "bounds": [[49.760112, 19.102835], [49.780002, 19.129878]]
  },
  {
    "km": 30,
    "lat": 49.765973,
    "lon": 19.13909,
    "time": "01:18",
    "pace": "13:21",
    "ele": "+475 m",
    "action": "Napój z kofeiną (kryzys nocny).",
    "action_en": "Caffeinated beverage (night crisis).",
    "bounds": [[49.76596, 19.108642], [49.780002, 19.140513]]
  },
  {
    "km": 35,
    "lat": 49.756541,
    "lon": 19.12972,
    "time": "02:21",
    "pace": "12:24",
    "ele": "+137 m",
    "action": "Kapsułki z solą, żel.",
    "action_en": "Salt capsules, energy gel.",
    "bounds": [[49.753813, 19.118867], [49.765973, 19.143013]]
  },
  {
    "km": 40,
    "lat": 49.769759,
    "lon": 19.142486,
    "time": "03:28",
    "pace": "13:30",
    "ele": "+427 m",
    "action": "Zjedz kanapkę.",
    "action_en": "Eat a sandwich.",
    "bounds": [[49.756541, 19.12972], [49.776784, 19.143013]]
  },
  {
    "km": 45,
    "lat": 49.767715,
    "lon": 19.160125,
    "time": "04:33",
    "pace": "13:03",
    "ele": "+247 m",
    "action": "Opróżnij bidon.",
    "action_en": "Empty flask.",
    "bounds": [[49.763475, 19.142486], [49.769759, 19.182465]]
  },
  {
    "km": 50,
    "lat": 49.77438,
    "lon": 19.139428,
    "time": "05:37",
    "pace": "12:42",
    "ele": "+98 m",
    "action": "Zmiana skarpet. Baton.",
    "action_en": "Change socks. Energy bar.",
    "bounds": [[49.766767, 19.127321], [49.783785, 19.160125]]
  },
  {
    "km": 55,
    "lat": 49.775302,
    "lon": 19.140957,
    "time": "06:44",
    "pace": "13:30",
    "ele": "+292 m",
    "action": "Kofeina (zmęczenie poranne).",
    "action_en": "Caffeine (morning fatigue).",
    "bounds": [[49.77438, 19.138081], [49.785056, 19.161343]]
  },
  {
    "km": 60,
    "lat": 49.79874,
    "lon": 19.131337,
    "time": "07:52",
    "pace": "13:31",
    "ele": "+253 m",
    "action": "Kapsułki z solą.",
    "action_en": "Salt capsules.",
    "bounds": [[49.773642, 19.127321], [49.79874, 19.140957]]
  },
  {
    "km": 65,
    "lat": 49.814493,
    "lon": 19.113824,
    "time": "09:00",
    "pace": "13:30",
    "ele": "+207 m",
    "action": "Żel energetyczny.",
    "action_en": "Energy gel.",
    "bounds": [[49.79874, 19.113362], [49.821366, 19.131963]]
  },
  {
    "km": 70,
    "lat": 49.782609,
    "lon": 19.12814,
    "time": "10:13",
    "pace": "14:43",
    "ele": "+510 m",
    "action": "Opróżnij bidon. Ostatnie podejście.",
    "action_en": "Empty flask. Last ascent.",
    "bounds": [[49.782609, 19.11375], [49.814493, 19.131963]]
  },
  {
    "km": 74,
    "lat": 49.795845,
    "lon": 19.096194,
    "time": "11:05",
    "pace": "13:10",
    "ele": "+49 m",
    "action": "META TESTU.",
    "action_en": "TEST FINISH.",
    "bounds": [[49.782609, 19.096194], [49.795845, 19.12814]]
  }
]'''

content = re.sub(r'checkpoints_json = \'\'\'\[.*?\]\'\'\'', f"checkpoints_json = '''{new_checkpoints_json}'''", content, flags=re.DOTALL)

# Update Schedule to match new ~11:10 finish time
content = content.replace('~17:30 META', '~11:10 META')
content = content.replace('17:30 (Dzień 2)', '11:10 (Dzień 2)')

with open('build_standalone_75km.py', 'w', encoding='utf-8') as f:
    f.write(content)
