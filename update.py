import re
import json

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

# 2. Checkpoints JSON
new_checkpoints_json = '''[
  {
    "km": 5,
    "lat": 49.777544,
    "lon": 19.113625,
    "time": "20:25",
    "pace": "17:00",
    "ele": "+500 m",
    "action": "Wypij 1. bidon izotoniku i zjedz baton.",
    "action_en": "Drink the 1st flask of isotonic and eat an energy bar.",
    "bounds": [[49.776947, 19.096194], [49.795845, 19.128895]]
  },
  {
    "km": 10,
    "lat": 49.784075,
    "lon": 19.104631,
    "time": "21:44",
    "pace": "15:47",
    "ele": "+176 m",
    "action": "Weź kapsułki z solą.",
    "action_en": "Take salt capsules.",
    "bounds": [[49.777253, 19.095909], [49.795845, 19.113625]]
  },
  {
    "km": 15,
    "lat": 49.775386,
    "lon": 19.105436,
    "time": "23:10",
    "pace": "17:12",
    "ele": "+405 m",
    "action": "Zjedz kanapkę.",
    "action_en": "Eat a sandwich.",
    "bounds": [[49.774707, 19.10206], [49.784075, 19.128324]]
  },
  {
    "km": 20,
    "lat": 49.77777,
    "lon": 19.122489,
    "time": "00:39",
    "pace": "17:55",
    "ele": "+482 m",
    "action": "Opróżnij bidon z izotonikiem.",
    "action_en": "Empty the isotonic flask.",
    "bounds": [[49.77403, 19.086939], [49.77777, 19.122489]]
  },
  {
    "km": 25,
    "lat": 49.76596,
    "lon": 19.108642,
    "time": "02:02",
    "pace": "16:37",
    "ele": "+159 m",
    "action": "Zmień skarpetki i zjedz baton.",
    "action_en": "Change socks and eat an energy bar.",
    "bounds": [[49.760112, 19.102835], [49.780002, 19.129878]]
  },
  {
    "km": 30,
    "lat": 49.765973,
    "lon": 19.13909,
    "time": "03:35",
    "pace": "18:32",
    "ele": "+475 m",
    "action": "Wypij napój z kofeiną (kryzys nocny).",
    "action_en": "Drink caffeinated beverage (night crisis).",
    "bounds": [[49.76596, 19.108642], [49.780002, 19.140513]]
  },
  {
    "km": 35,
    "lat": 49.756541,
    "lon": 19.12972,
    "time": "05:01",
    "pace": "17:06",
    "ele": "+137 m",
    "action": "Weź kapsułki z solą i zjedz żel.",
    "action_en": "Take salt capsules and eat an energy gel.",
    "bounds": [[49.753813, 19.118867], [49.765973, 19.143013]]
  },
  {
    "km": 40,
    "lat": 49.769759,
    "lon": 19.142486,
    "time": "06:35",
    "pace": "18:57",
    "ele": "+427 m",
    "action": "Zjedz kanapkę.",
    "action_en": "Eat a sandwich.",
    "bounds": [[49.756541, 19.12972], [49.776784, 19.143013]]
  },
  {
    "km": 45,
    "lat": 49.767715,
    "lon": 19.160125,
    "time": "08:07",
    "pace": "18:18",
    "ele": "+247 m",
    "action": "Opróżnij bidon z izotonikiem.",
    "action_en": "Empty the isotonic flask.",
    "bounds": [[49.763475, 19.142486], [49.769759, 19.182465]]
  },
  {
    "km": 50,
    "lat": 49.77438,
    "lon": 19.139428,
    "time": "09:36",
    "pace": "17:47",
    "ele": "+98 m",
    "action": "Zmień skarpetki. Zjedz baton.",
    "action_en": "Change socks. Eat an energy bar.",
    "bounds": [[49.766767, 19.127321], [49.783785, 19.160125]]
  },
  {
    "km": 55,
    "lat": 49.775302,
    "lon": 19.140957,
    "time": "11:12",
    "pace": "19:10",
    "ele": "+292 m",
    "action": "Wypij napój z kofeiną (kryzys poranny).",
    "action_en": "Drink a caffeinated beverage (morning crisis).",
    "bounds": [[49.77438, 19.138081], [49.785056, 19.161343]]
  },
  {
    "km": 60,
    "lat": 49.79874,
    "lon": 19.131337,
    "time": "12:48",
    "pace": "19:16",
    "ele": "+253 m",
    "action": "Weź kapsułki z solą.",
    "action_en": "Take salt capsules.",
    "bounds": [[49.773642, 19.127321], [49.79874, 19.140957]]
  },
  {
    "km": 65,
    "lat": 49.814493,
    "lon": 19.113824,
    "time": "14:25",
    "pace": "19:18",
    "ele": "+207 m",
    "action": "Zjedz żel energetyczny.",
    "action_en": "Eat an energy gel.",
    "bounds": [[49.79874, 19.113362], [49.821366, 19.131963]]
  },
  {
    "km": 70,
    "lat": 49.782609,
    "lon": 19.12814,
    "time": "16:12",
    "pace": "21:24",
    "ele": "+510 m",
    "action": "Opróżnij bidon. Ostatnie strome podejście.",
    "action_en": "Empty the flask. Last steep ascent.",
    "bounds": [[49.782609, 19.11375], [49.814493, 19.131963]]
  },
  {
    "km": 74,
    "lat": 49.795845,
    "lon": 19.096194,
    "time": "17:27",
    "pace": "18:51",
    "ele": "+49 m",
    "action": "META! Odpocznij i nawodnij się.",
    "action_en": "FINISH! Rest and hydrate.",
    "bounds": [[49.782609, 19.096194], [49.795845, 19.12814]]
  }
]'''
content = re.sub(r'checkpoints_json = \'\'\'\[.*?\]\'\'\'', f"checkpoints_json = '''{new_checkpoints_json}'''", content, flags=re.DOTALL)

# 3. Remove Tests tab from html
content = re.sub(r'<button class=\"tab-btn[^\"]*\" data-target=\"tab-testy\">.*?</button>', '', content, flags=re.DOTALL)
content = re.sub(r'<div id=\"tab-testy\".*?</div>\n*        <!-- ZAKŁADKA: MAPA', '<!-- ZAKŁADKA: MAPA', content, flags=re.DOTALL)

# 4. Inventory HTML
inventory_content = '''
        <!-- Ubiór -->
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Ubiór</span>
                <span class="lang-en">Clothing</span>
            </h3>
            <ul class="space-y-1">
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-shirt text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Kurtka wiatrówka/przeciwdeszczowa</span>
                        <span class="lang-en">Windproof/waterproof jacket</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-vest text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Lekka warstwa termiczna np. cienki polar na noc</span>
                        <span class="lang-en">Lightweight thermal layer for the night</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-socks text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Zapasowe skarpetki - 2 pary szczelnie zapakowane</span>
                        <span class="lang-en">Spare socks - 2 pairs in a ziplock bag</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-mask text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Chusta wielofunkcyjna / Buff</span>
                        <span class="lang-en">Multifunctional headwear / Buff</span>
                    </span>
                </li>
            </ul>
        </div>
        <!-- Sprzęt -->
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Sprzęt i Elektronika</span>
                <span class="lang-en">Gear &amp; Electronics</span>
            </h3>
            <ul class="space-y-1">
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-person-hiking text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Kije trekkingowe - absolutny wymóg przy 12kg</span>
                        <span class="lang-en">Trekking poles</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-headlamp text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Czołówka główna + zapasowa czołówka lub baterie</span>
                        <span class="lang-en">Main headlamp + spare headlamp or batteries</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-battery-full text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Powerbank 10000mAh + krótki kabel</span>
                        <span class="lang-en">Powerbank 10000mAh + short cable</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-mobile-screen text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Smartfon</span>
                        <span class="lang-en">Smartphone</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-watch text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Zegarek GPS (Garmin)</span>
                        <span class="lang-en">GPS Watch</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-bottle-water text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Softflaski lub bukłak na max 2 litry</span>
                        <span class="lang-en">Hydration bladder or soft flasks for max 2 liters</span>
                    </span>
                </li>
            </ul>
        </div>
        <!-- Apteczka -->
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Apteczka Minimalistyczna</span>
                <span class="lang-en">Minimalist First Aid Kit</span>
            </h3>
            <ul class="space-y-1">
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-kit-medical text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Folia NRC / Koc ratunkowy</span>
                        <span class="lang-en">Emergency blanket</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-pump-medical text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Wazelina do smarowania stóp przeciw otarciom</span>
                        <span class="lang-en">Petroleum jelly for feet chafing prevention</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-pills text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Tabletki przeciwbólowe - wyjęte z blistra</span>
                        <span class="lang-en">Painkillers - out of blister pack</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-band-aid text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Kilka plastrów z opatrunkiem i plastry na pęcherze</span>
                        <span class="lang-en">Band-aids and blister plasters</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-bandage text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Opaska elastyczna</span>
                        <span class="lang-en">Elastic bandage</span>
                    </span>
                </li>
            </ul>
        </div>
        <!-- Jedzenie i Picie -->
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Jedzenie i Picie</span>
                <span class="lang-en">Food &amp; Hydration</span>
            </h3>
            <ul class="space-y-1">
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-jar text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Proszek węglowodanowy/Hyper-Mix na ok. 14 porcji w woreczkach</span>
                        <span class="lang-en">Carbohydrate powder mix for approx. 14 servings</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-candy-cane text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Żele energetyczne i batony w łatwo dostępnych kieszeniach</span>
                        <span class="lang-en">Energy gels and bars in quick-access pockets</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-hotdog text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">4-5 spłaszczonych kanapek w folii aluminiowej</span>
                        <span class="lang-en">4-5 flattened sandwiches in aluminum foil</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-capsules text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Kapsułki z solą (SaltStick) lub słone przekąski</span>
                        <span class="lang-en">Salt capsules or salty snacks</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-mug-hot text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Napoje z kofeiną w puszkach np. Red Bull</span>
                        <span class="lang-en">Caffeinated drinks in cans</span>
                    </span>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-glass-water text-slate-500 mt-0.5 w-4"></i>
                    <span>
                        <span class="lang-pl">Filtr do wody / Tabletki uzdatniające</span>
                        <span class="lang-en">Water filtration system / Purification tablets</span>
                    </span>
                </li>
            </ul>
        </div>
'''
content = re.sub(r'<div id=\"tab-inventory\".*?</div>\n*        <!-- ZAKŁADKA: HARMONOGRAM', '<div id="tab-inventory" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">\n' + inventory_content + '        </div>\n        <!-- ZAKŁADKA: HARMONOGRAM', content, flags=re.DOTALL)

# 5. Schedule HTML
schedule_content = '''
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Dzień 1</span>
                <span class="lang-en">Day 1</span>
            </h3>
            <ul class="space-y-2">
                <li class="flex items-start gap-2">
                    <i class="fa-regular fa-clock text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">06:00</div>
                        <div>
                            <span class="lang-pl">Pobudka, nawodnienie i lekkie śniadanie.</span>
                            <span class="lang-en">Wake up, hydration, and light breakfast.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-regular fa-clock text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">07:00 - 15:00</div>
                        <div>
                            <span class="lang-pl">Dzień pracy. Skupienie na ciągłym nawadnianiu.</span>
                            <span class="lang-en">Work day. Focus on continuous hydration.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-regular fa-clock text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">15:00 - 16:30</div>
                        <div>
                            <span class="lang-pl">Krótka drzemka / odpoczynek z zamkniętymi oczami.</span>
                            <span class="lang-en">Short nap / rest with eyes closed.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-regular fa-clock text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">17:00</div>
                        <div>
                            <span class="lang-pl">Obiad (bogaty w węglowodany, ubogi w błonnik).</span>
                            <span class="lang-en">Dinner - rich in carbohydrates, low in fiber.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-regular fa-clock text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">18:00</div>
                        <div>
                            <span class="lang-pl">Ostatni audyt ekwipunku i dojazd na start.</span>
                            <span class="lang-en">Final gear audit and travel to the starting point.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-play text-amber-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-amber-500">19:00 START</div>
                        <div class="text-amber-400/90">
                            <span class="lang-pl">Wejście w tryb marszu tlenowego.</span>
                            <span class="lang-en">Enter aerobic walking mode.</span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Dzień 2</span>
                <span class="lang-en">Day 2</span>
            </h3>
            <ul class="space-y-2">
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-moon text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">~03:30</div>
                        <div>
                            <span class="lang-pl">Kryzys nocny ("Godzina wilka"). Czas na uderzeniową dawkę kofeiny.</span>
                            <span class="lang-en">Night crisis / "The Witching Hour". Caffeine shot.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-sun text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">~05:00</div>
                        <div>
                            <span class="lang-pl">Wschód słońca. Psychologiczny reset i ocieplenie.</span>
                            <span class="lang-en">Sunrise. Psychological reset and warming up.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-flag-checkered text-amber-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-amber-500">~17:30 META</div>
                        <div class="text-amber-400/90">
                            <span class="lang-pl">Planowana Meta.</span>
                            <span class="lang-en">Expected Finish.</span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
'''
content = re.sub(r'<div id=\"tab-schedule\".*?</div>\n*        <!-- ZAKŁADKA: TAKTYKA', '<div id="tab-schedule" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">\n' + schedule_content + '        </div>\n        <!-- ZAKŁADKA: TAKTYKA', content, flags=re.DOTALL)

# 6. Tactics HTML
tactics_content = '''
        <div class="mb-4">
            <h3 class="text-sm font-bold text-amber-500 mb-2 border-b border-slate-700 pb-1">
                <span class="lang-pl">Zasady Ruchu (Plecaka 12kg)</span>
                <span class="lang-en">Movement Rules (12kg pack)</span>
            </h3>
            <ul class="space-y-2">
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-arrow-right text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">
                            <span class="lang-pl">Płaskie i łagodne podejścia</span>
                            <span class="lang-en">Flat and gentle ascents</span>
                        </div>
                        <div class="text-slate-400">
                            <span class="lang-pl">Utrzymuj miarowy, stabilny marsz. Ręce luźno, kije służą tylko do utrzymania rytmu. Unikaj zrywającego biegu.</span>
                            <span class="lang-en">Maintain a steady, rhythmic walk. Arms relaxed, poles used only for rhythm. Avoid sudden running.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-arrow-trend-up text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">
                            <span class="lang-pl">Strome podejścia</span>
                            <span class="lang-en">Steep ascents</span>
                        </div>
                        <div class="text-slate-400">
                            <span class="lang-pl">Zrób mniejszy krok, opieraj mocno ciężar na kijach, by odciążyć kolana. Tętno nie powinno przekraczać 140 bpm. Jeśli serce bije szybciej, bezwzględnie zwolnij.</span>
                            <span class="lang-en">Take shorter steps, lean heavily on poles to relieve knees. HR limit: 140 bpm. If heart beats faster, absolutely slow down.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-arrow-trend-down text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">
                            <span class="lang-pl">Zbiegi</span>
                            <span class="lang-en">Downhills</span>
                        </div>
                        <div class="text-slate-400">
                            <span class="lang-pl">Absolutny zakaz uderzania piętą o podłoże! Ląduj miękko na śródstopiu/całej stopie. Kije stawiaj przed sobą, by absorbowały impakt (10-15% obciążenia w ręce).</span>
                            <span class="lang-en">Absolute ban on heel striking! Land softly on the midfoot. Plant poles in front to absorb impact - 10-15% of the load into arms.</span>
                        </div>
                    </div>
                </li>
                <li class="flex items-start gap-2">
                    <i class="fa-solid fa-bottle-droplet text-slate-500 mt-0.5 w-4"></i>
                    <div>
                        <div class="font-bold text-slate-200">
                            <span class="lang-pl">Nawadnianie i Żywienie</span>
                            <span class="lang-en">Hydration and Nutrition</span>
                        </div>
                        <div class="text-slate-400">
                            <span class="lang-pl">1 bidon (500ml) płynów na każdą godzinę marszu. Cel to stała podaż 60g węglowodanów na godzinę. Przeplataj płyny izotoniczne z jedzeniem.</span>
                            <span class="lang-en">1 flask (500ml) of fluids per hour. Target: 60g carbs/hour. Alternate isotonic fluids with solid food.</span>
                        </div>
                    </div>
                </li>
            </ul>
        </div>
'''
content = re.sub(r'<div id=\"tab-tactics\".*?</div>\n*        <!-- ZAKŁADKA: TESTY', '<div id="tab-tactics" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">\n' + tactics_content + '        </div>\n        <!-- ZAKŁADKA: TESTY', content, flags=re.DOTALL)

with open('build_standalone_75km.py', 'w', encoding='utf-8') as f:
    f.write(content)

