import re
import shutil

# Copy the original 100km as a fresh start
shutil.copy('build_standalone.py', 'build_standalone_75km.py')

with open('build_standalone_75km.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Output file names and titles
content = content.replace('Ultra100_standalone.html', 'Ultra75_standalone.html')
content = content.replace('wyrypa-100km.gpx', 'wyrypa75km.gpx')
content = content.replace('Wyrypa 100km', 'Wyrypa 75km')
content = content.replace('"name": "Ultra 100km Tracker"', '"name": "Ultra 75km Tracker"')
content = content.replace('"short_name": "Ultra 100"', '"short_name": "Ultra 75"')
content = content.replace('sw.js', 'sw_75.js')
content = content.replace('manifest.json', 'manifest_75.json')
content = content.replace('ultra-100-tracker-v1', 'ultra-75-tracker-v1')
content = content.replace('<title>100km Ultra-Trekking Tracker (Offline)</title>', '<title>75km Ultra-Trekking Tracker (Offline)</title>')

# 2. Challenge Parameters Layout Fix
old_params = '''<div class="grid grid-cols-1 sm:grid-cols-2 gap-2 md:gap-4">
                    <div class="flex flex-col space-y-2 md:space-y-3">
                        <div class="flex items-center space-x-2">
                            <span class="bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1.5 rounded border border-slate-700 shadow-sm w-full font-semibold text-xs md:text-sm">🗓️ <span class="lang-pl">10 lipca 2026</span><span class="lang-en">July 10, 2026</span></span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1.5 rounded border border-slate-700 shadow-sm w-full font-semibold text-xs md:text-sm">🏃‍♂️ 87 kg (75+12)</span>
                        </div>
                    </div>
                    <div class="flex flex-col space-y-2 md:space-y-3">
                        <div class="flex items-center space-x-2">
                            <span class="bg-slate-800 text-red-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-red-900/50 shadow-sm w-full font-semibold text-xs md:text-sm">❤️ Target: 125-140 bpm</span>
                        </div>
                        <div class="flex items-center space-x-2">
                            <span class="bg-lime-900/30 text-lime-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-lime-700/50 shadow-sm w-full font-semibold text-xs md:text-sm">⏱️ <span class="lang-pl">Cel: &lt; 24h</span><span class="lang-en">Goal: &lt; 24h</span></span>
                        </div>
                    </div>
                </div>'''

new_params = '''<div class="flex flex-col sm:flex-row gap-2 md:gap-4 flex-wrap">
                    <span class="bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1.5 rounded border border-slate-700 shadow-sm flex-1 text-center font-semibold text-xs md:text-sm whitespace-nowrap">🏃‍♂️ 87 kg (75+12)</span>
                    <span class="bg-slate-800 text-red-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-red-900/50 shadow-sm flex-1 text-center font-semibold text-xs md:text-sm whitespace-nowrap">❤️ Target: 125-140 bpm</span>
                    <span class="bg-lime-900/30 text-lime-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-lime-700/50 shadow-sm flex-1 text-center font-semibold text-xs md:text-sm whitespace-nowrap">⏱️ <span class="lang-pl">Cel: ~16-17h</span><span class="lang-en">Goal: ~16-17h</span></span>
                </div>'''

content = content.replace(old_params, new_params)

# 3. Checkpoints JSON
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

# 4. Remove Testy & Trening Tabs from HTML Header
content = re.sub(r'<button class="tab-btn[^"]*" data-target="tab-testy">.*?</button>', '', content, flags=re.DOTALL)
content = re.sub(r'<button class="tab-btn[^"]*" data-target="tab-trening">.*?</button>', '', content, flags=re.DOTALL)

# 5. Remove Testy & Trening Tab Content Blocks
# Find start of tab-testy and remove to end of tab-trening block
start_testy = content.find('<div id="tab-testy"')
end_trening = content.find('<!-- JavaScript -->')
if start_testy != -1 and end_trening != -1:
    # Look back to find the start of the previous tab to ensure we don't break HTML structure, actually just remove these divs
    # We will slice out the content
    content = content[:start_testy] + '</div>\n    </div>\n\n    <!-- JavaScript -->' + content[end_trening + len('<!-- JavaScript -->'):]


# 6. Update INWENTARZ 
inwentarz_content = '''<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl mb-4">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">2. INWENTARZ - EKWIPUNEK (Limit 12kg z wodą)</span><span class="lang-en">2. GEAR INVENTORY (12kg limit with water)</span></h2>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                    <div>
                        <h3 class="text-sm font-bold text-cyan-400 mb-2"><span class="lang-pl">Ubiór</span><span class="lang-en">Clothing</span></h3>
                        <ul class="space-y-1">
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Kurtka wiatrówka/przeciwdeszczowa</span><span class="lang-en">Windproof/waterproof jacket</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Lekka warstwa termiczna (np. cienki polar na noc)</span><span class="lang-en">Lightweight thermal layer</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Zapasowe skarpetki - 2 pary w worku</span><span class="lang-en">Spare socks - 2 pairs in a ziplock bag</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Chusta wielofunkcyjna / Buff</span><span class="lang-en">Multifunctional headwear / Buff</span></div></li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-cyan-400 mb-2"><span class="lang-pl">Apteczka Minimalistyczna</span><span class="lang-en">Minimalist First Aid Kit</span></h3>
                        <ul class="space-y-1">
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Folia NRC / Koc ratunkowy</span><span class="lang-en">Emergency blanket</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Wazelina do stóp</span><span class="lang-en">Petroleum jelly for feet</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Tabletki przeciwbólowe (luzem)</span><span class="lang-en">Painkillers</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Plastry z opatrunkiem i na pęcherze</span><span class="lang-en">Band-aids and blister plasters</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Opaska elastyczna</span><span class="lang-en">Elastic bandage</span></div></li>
                        </ul>
                    </div>
                </div>
                <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mt-4">
                    <div>
                        <h3 class="text-sm font-bold text-cyan-400 mb-2"><span class="lang-pl">Sprzęt i Elektronika</span><span class="lang-en">Gear & Electronics</span></h3>
                        <ul class="space-y-1">
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Kije trekkingowe</span><span class="lang-en">Trekking poles</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Czołówka główna + zapasowa (lub baterie)</span><span class="lang-en">Main headlamp + spare/batteries</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Powerbank 10000mAh + kabel</span><span class="lang-en">Powerbank 10000mAh + short cable</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Smartfon</span><span class="lang-en">Smartphone</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Zegarek GPS (Garmin)</span><span class="lang-en">GPS Watch</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Softflaski / Bukłak na max 2 litry</span><span class="lang-en">Hydration bladder or soft flasks for max 2 liters</span></div></li>
                        </ul>
                    </div>
                    <div>
                        <h3 class="text-sm font-bold text-cyan-400 mb-2"><span class="lang-pl">Jedzenie i Picie</span><span class="lang-en">Food & Hydration</span></h3>
                        <ul class="space-y-1">
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Hyper-Mix: ok. 14 porcji w woreczkach</span><span class="lang-en">Carb powder mix - approx. 14 servings</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Żele energetyczne i batony</span><span class="lang-en">Energy gels and bars</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">4-5 spłaszczonych kanapek w folii</span><span class="lang-en">4-5 flattened sandwiches in foil</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Kapsułki z solą (SaltStick) lub słone przekąski</span><span class="lang-en">Salt capsules or salty snacks</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Napoje z kofeiną w puszkach (np. Red Bull)</span><span class="lang-en">Caffeinated drinks</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Filtr do wody / Tabletki uzdatniające</span><span class="lang-en">Water filtration system / Purification tablets</span></div></li>
                        </ul>
                    </div>
                </div>
            </div>'''
start_inwentarz = content.find('<div id="tab-inwentarz"')
end_inwentarz = content.find('<div id="tab-harmonogram"')
if start_inwentarz != -1 and end_inwentarz != -1:
    content = content[:start_inwentarz] + '<div id="tab-inwentarz" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">\n' + inwentarz_content + '\n        </div>\n\n        <!-- Tab: Harmonogram -->\n        ' + content[end_inwentarz:]


# 7. Update TAKTYKA
taktyka_content = '''<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl mb-4">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">3. TAKTYKA I ZASADY RUCHU</span><span class="lang-en">3. TACTICS & MOVEMENT</span></h2>
                <ul class="space-y-4">
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Płaskie i łagodne podejścia:</strong> Miarowy, stabilny marsz. Unikaj biegu.</span><span class="lang-en">Flat and gentle ascents:</strong> Maintain a steady, rhythmic walk. Avoid running.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Strome podejścia:</strong> Krótki krok, mocne wsparcie kijami. Tętno do 140 bpm. Zwalniasz, gdy rośnie.</span><span class="lang-en">Steep ascents:</strong> Take shorter steps, lean heavily on poles. HR limit: 140 bpm. Slow down if higher.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Zbiegi:</strong> Ląduj na śródstopiu/całej stopie. Kije absorbują 10-15% impaktu.</span><span class="lang-en">Downhills:</strong> Land on midfoot. Poles absorb 10-15% impact.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Nawadnianie i Żywienie:</strong> 1 bidon (500ml) na godzinę marszu. Cel: 60g węglowodanów na godzinę.</span><span class="lang-en">Hydration and Nutrition:</strong> 1 flask (500ml) per hour. Target: 60g carbs/hour.</span></div></li>
                </ul>
            </div>'''
start_taktyka = content.find('<div id="tab-taktyka"')
end_taktyka = content.find('<div id="tab-inwentarz"')
if start_taktyka != -1 and end_taktyka != -1:
    content = content[:start_taktyka] + '<div id="tab-taktyka" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">\n' + taktyka_content + '\n        </div>\n\n        <!-- Tab: Inwentarz -->\n        ' + content[end_taktyka:]

# 8. Update HARMONOGRAM
harmonogram_content = '''<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl mb-4">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">1. HARMONOGRAM LOGISTYCZNY DNIA</span><span class="lang-en">1. LOGISTICS SCHEDULE</span></h2>
                <ul class="space-y-4">
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">06:00</strong> - <span class="lang-pl">Pobudka, nawodnienie i lekkie śniadanie.</span><span class="lang-en">Wake up, hydration, and light breakfast.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">07:00 - 15:00</strong> - <span class="lang-pl">Praca. Skupienie na ciągłym nawadnianiu.</span><span class="lang-en">Work day. Focus on continuous hydration.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">15:00 - 16:30</strong> - <span class="lang-pl">Drzemka / odpoczynek.</span><span class="lang-en">Short nap / rest.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">17:00</strong> - <span class="lang-pl">Obiad (węglowodany, mało błonnika).</span><span class="lang-en">Dinner - high carb, low fiber.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">18:00</strong> - <span class="lang-pl">Kontrola ekwipunku i dojazd na start.</span><span class="lang-en">Final gear audit and travel.</span></div></li>
                    <li class="flex items-start"><span class="text-amber-500 mr-3 mt-1">▶</span><div><strong class="text-amber-400">19:00 START TESTU</strong> - <span class="lang-pl">Wejście w tryb marszu.</span><span class="lang-en">Enter walking mode.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">~03:30 (Dzień 2)</strong> - <span class="lang-pl">Kryzys nocny ("Godzina wilka"). Użycie kofeiny.</span><span class="lang-en">Night crisis / "The Witching Hour". Caffeine shot.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">~05:00 (Dzień 2)</strong> - <span class="lang-pl">Wschód słońca.</span><span class="lang-en">Sunrise.</span></div></li>
                    <li class="flex items-start"><span class="text-amber-500 mr-3 mt-1">▶</span><div><strong class="text-amber-400">~11:10 (Dzień 2) META TESTU</strong> - <span class="lang-pl">Czas łączny ~16h 10m.</span><span class="lang-en">Expected Finish (~16h 10m).</span></div></li>
                </ul>
            </div>
            
            <div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl border-dashed border-slate-600 opacity-80">
                <h2 class="text-base md:text-lg font-bold text-slate-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">HARMONOGRAM OGÓLNY I POSTOJE (Wymaga wygenerowania)</span><span class="lang-en">GENERAL SCHEDULE & STOPS (Needs to be generated)</span></h2>
                <p class="text-sm italic text-slate-500"><span class="lang-pl">Brak szczegółowego rozpisania etapów (np. 0-25km, 25-50km) i długości postojów na zmienianie skarpet / przepak dla 75km. Wygeneruj ten fragment u AI i dostarcz w kolejnej iteracji!</span><span class="lang-en">Missing detailed staging (e.g., 0-25km) and stop lengths for 75km. Generate this chunk with AI and provide it in the next iteration!</span></p>
            </div>'''
start_harmonogram = content.find('<div id="tab-harmonogram"')
end_harmonogram = content.find('</div>\n    </div>\n\n    <!-- JavaScript -->')
if start_harmonogram != -1 and end_harmonogram != -1:
    content = content[:start_harmonogram] + '<div id="tab-harmonogram" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">\n' + harmonogram_content + '\n        </div>\n' + content[end_harmonogram:]

# 9. Stop overwriting index.html in the builder script
content = content.replace("with open('index.html', 'w', encoding='utf-8') as f:\n        f.write(html_content)", "")
content = content.replace("print('Writing index.html...')", "")
content = content.replace("Successfully generated index.html, Ultra75_standalone.html", "Successfully generated Ultra75_standalone.html")

with open('build_standalone_75km.py', 'w', encoding='utf-8') as f:
    f.write(content)
