import urllib.request
import json
import time

app_version = f"ultra-trekking-v{int(time.time())}"

def fetch(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    return urllib.request.urlopen(req).read().decode('utf-8')

print('Fetching Tailwind...')
tailwind_js = fetch('https://cdn.tailwindcss.com')

print('Fetching Leaflet CSS...')
leaflet_css = fetch('https://unpkg.com/leaflet@1.9.4/dist/leaflet.css')

print('Fetching Leaflet JS...')
leaflet_js = fetch('https://unpkg.com/leaflet@1.9.4/dist/leaflet.js')

print('Fetching Leaflet GPX...')
leaflet_gpx_js = fetch('https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.7.0/gpx.min.js')

print('Reading GPX file...')
with open('wyrypa-100km.gpx', 'r', encoding='utf-8') as f:
    gpx_content = f.read()

# Escape backticks, dollars, slashes, and closing scripts
gpx_content_escaped = gpx_content.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$').replace('</script>', '<\\/script>')

checkpoints_json = '''[
    {
        "km": 5,
        "lat": 49.77298,
        "lon": 19.135408,
        "time": "20:20",
        "pace": "16:00",
        "ele": "+542m",
        "action": "Opróżnij 1. bidon Hyper-Mix.",
        "bounds": [
            [
                49.761016,
                19.086507
            ],
            [
                49.776999,
                19.135408
            ]
        ],
        "action_en": "Empty 1st Hyper-Mix flask."
    },
    {
        "km": 10,
        "lat": 49.756147,
        "lon": 19.192668,
        "time": "21:18",
        "pace": "13:48",
        "ele": "+99m",
        "action": "Weź 2 kaps. SaltStick.",
        "bounds": [
            [
                49.756147,
                19.135492
            ],
            [
                49.772917,
                19.192668
            ]
        ],
        "action_en": "Take 2 SaltStick caps."
    },
    {
        "km": 15,
        "lat": 49.752494,
        "lon": 19.234045,
        "time": "22:35",
        "pace": "14:20",
        "ele": "+475m",
        "action": "Zjedz 1 kanapkę.",
        "bounds": [
            [
                49.745768,
                19.193001
            ],
            [
                49.755981,
                19.234045
            ]
        ],
        "action_en": "Eat 1 sandwich."
    },
    {
        "km": 20,
        "lat": 49.777629,
        "lon": 19.279882,
        "time": "23:41",
        "pace": "14:03",
        "ele": "+269m",
        "action": "1 kostka Dextro Energy.",
        "bounds": [
            [
                49.752507,
                19.234175
            ],
            [
                49.777629,
                19.279882
            ]
        ],
        "action_en": "1 cube of Dextro Energy."
    },
    {
        "km": 25,
        "lat": 49.792141,
        "lon": 19.304483,
        "time": "00:44",
        "pace": "13:45",
        "ele": "+108m",
        "action": "PRZERWA 5 MIN. Zmiana skarpet! SaltStick + Baton.",
        "bounds": [
            [
                49.776679,
                19.280574
            ],
            [
                49.792207,
                19.316707
            ]
        ],
        "action_en": "5 MIN BREAK. Change socks! SaltStick + Bar."
    },
    {
        "km": 30,
        "lat": 49.819205,
        "lon": 19.263115,
        "time": "01:53",
        "pace": "13:46",
        "ele": "+285m",
        "action": "Opróżnij 3. bidon Hyper-Mix.",
        "bounds": [
            [
                49.792138,
                19.263115
            ],
            [
                49.819807,
                19.304321
            ]
        ],
        "action_en": "Empty 3rd Hyper-Mix flask."
    },
    {
        "km": 35,
        "lat": 49.823822,
        "lon": 19.213726,
        "time": "02:50",
        "pace": "13:25",
        "ele": "+34m",
        "action": "1 kanapka + Banan.",
        "bounds": [
            [
                49.817347,
                19.21359
            ],
            [
                49.823822,
                19.262697
            ]
        ],
        "action_en": "1 sandwich + Banana."
    },
    {
        "km": 40,
        "lat": 49.828276,
        "lon": 19.176234,
        "time": "04:14",
        "pace": "13:51",
        "ele": "+577m",
        "action": "Weź 2 kaps. SaltStick.",
        "bounds": [
            [
                49.82388,
                19.176234
            ],
            [
                49.831375,
                19.213817
            ]
        ],
        "action_en": "Take 2 SaltStick caps."
    },
    {
        "km": 45,
        "lat": 49.805408,
        "lon": 19.129303,
        "time": "05:20",
        "pace": "13:46",
        "ele": "+213m",
        "action": "KRYZYS NOCNY. Wypij Red Bull #1 + Glukoza 1WW.",
        "bounds": [
            [
                49.805408,
                19.127867
            ],
            [
                49.828247,
                19.17591
            ]
        ],
        "action_en": "NIGHT CRISIS. Drink Red Bull #1 + Glucose 1WW."
    },
    {
        "km": 50,
        "lat": 49.775288,
        "lon": 19.108276,
        "time": "06:33",
        "pace": "13:51",
        "ele": "+267m",
        "action": "Opróżnij 5. bidon Hyper-Mix.",
        "bounds": [
            [
                49.774857,
                19.108276
            ],
            [
                49.805167,
                19.131963
            ]
        ],
        "action_en": "Empty 5th Hyper-Mix flask."
    },
    {
        "km": 55,
        "lat": 49.759398,
        "lon": 19.057464,
        "time": "07:31",
        "pace": "13:39",
        "ele": "+66m",
        "action": "Weź 2 kaps. SaltStick.",
        "bounds": [
            [
                49.759398,
                19.057464
            ],
            [
                49.776556,
                19.108131
            ]
        ],
        "action_en": "Take 2 SaltStick caps."
    },
    {
        "km": 60,
        "lat": 49.738409,
        "lon": 19.00473,
        "time": "09:28",
        "pace": "14:28",
        "ele": "+640m",
        "action": "PRZEPAK (30 min). Zmiana butów, zupa, depozyt.",
        "bounds": [
            [
                49.738308,
                19.00473
            ],
            [
                49.759361,
                19.057283
            ]
        ],
        "action_en": "DROP BAG (30 min). Change shoes, soup, drop bag."
    },
    {
        "km": 65,
        "lat": 49.706954,
        "lon": 18.988097,
        "time": "10:34",
        "pace": "14:22",
        "ele": "+174m",
        "action": "Start na świeżym Hyper-Mixie.",
        "bounds": [
            [
                49.706954,
                18.988073
            ],
            [
                49.738971,
                19.00443
            ]
        ],
        "action_en": "Start with fresh Hyper-Mix."
    },
    {
        "km": 70,
        "lat": 49.676524,
        "lon": 18.94969,
        "time": "11:44",
        "pace": "14:20",
        "ele": "+251m",
        "action": "Żel + Banan + SaltStick.",
        "bounds": [
            [
                49.674825,
                18.94969
            ],
            [
                49.706801,
                18.987932
            ]
        ],
        "action_en": "Gel + Banana + SaltStick."
    },
    {
        "km": 75,
        "lat": 49.711845,
        "lon": 18.91931,
        "time": "12:51",
        "pace": "14:16",
        "ele": "+100m",
        "action": "1 kostka Dextro Energy.",
        "bounds": [
            [
                49.676575,
                18.915831
            ],
            [
                49.711845,
                18.949433
            ]
        ],
        "action_en": "1 cube of Dextro Energy."
    },
    {
        "km": 80,
        "lat": 49.746019,
        "lon": 18.935688,
        "time": "14:11",
        "pace": "14:23",
        "ele": "+466m",
        "action": "UPAŁ. Red Bull #2 + Max Sól.",
        "bounds": [
            [
                49.712155,
                18.916604
            ],
            [
                49.746019,
                18.935688
            ]
        ],
        "action_en": "HEAT. Red Bull #2 + Max Salt."
    },
    {
        "km": 85,
        "lat": 49.739677,
        "lon": 18.994522,
        "time": "15:26",
        "pace": "14:25",
        "ele": "+360m",
        "action": "Żel, koniec jedzenia stałego.",
        "bounds": [
            [
                49.736711,
                18.935909
            ],
            [
                49.748139,
                18.994522
            ]
        ],
        "action_en": "Gel, end of solid food."
    },
    {
        "km": 90,
        "lat": 49.767413,
        "lon": 19.029714,
        "time": "16:26",
        "pace": "14:17",
        "ele": "+58m",
        "action": "Opróżnij ostatni Hyper-Mix.",
        "bounds": [
            [
                49.739824,
                18.993553
            ],
            [
                49.767413,
                19.029714
            ]
        ],
        "action_en": "Empty last Hyper-Mix."
    },
    {
        "km": 95,
        "lat": 49.792751,
        "lon": 19.066255,
        "time": "17:27",
        "pace": "14:10",
        "ele": "+77m",
        "action": "FINISZ. Red Bull #3 + Glukoza 1WW.",
        "bounds": [
            [
                49.767443,
                19.029864
            ],
            [
                49.792751,
                19.066255
            ]
        ],
        "action_en": "FINISH. Red Bull #3 + Glucose 1WW."
    },
    {
        "km": 100,
        "lat": 49.776164,
        "lon": 19.105477,
        "time": "18:46",
        "pace": "14:15",
        "ele": "+432m",
        "action": "META.",
        "bounds": [
            [
                49.776164,
                19.06693
            ],
            [
                49.795029,
                19.106579
            ]
        ],
        "action_en": "META."
    }
]'''

html_template = f'''<!DOCTYPE html>
<html lang="en" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="theme-color" content="#0f172a">
    <link rel="manifest" href="manifest.json">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🥾</text></svg>">
    <link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🥾</text></svg>">
    <title>100km Ultra-Trekking Tracker (Offline)</title>
    
    <style>
        {leaflet_css}

    </style>
    
    <script>
        {tailwind_js}
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    colors: {{
                        slate: tailwind.colors.slate,
                        lime: tailwind.colors.lime,
                        cyan: tailwind.colors.cyan,
                        emerald: tailwind.colors.emerald
                    }}
                }}
            }}
        }}
    </script>
    
    <style>
        html {{ scroll-behavior: smooth; }}
        body {{ overscroll-behavior-y: none; }}
        .table-row-highlight {{
            background-color: #334155; 
            transition: background-color 0.3s ease-in-out;
            outline: 2px solid #84cc16; 
        }}
        .table-row-transition {{ transition: background-color 0.3s ease-in-out, outline 0.3s ease-in-out; }}
        
        .custom-div-icon {{
            background: #84cc16;
            border: 2px solid #0f172a;
            color: #0f172a;
            font-weight: bold;
            text-align: center;
            border-radius: 50%;
            line-height: 24px;
            box-shadow: 0 0 10px rgba(132, 204, 22, 0.5);
        }}
        
        .leaflet-layer,
        .leaflet-control-zoom-in,
        .leaflet-control-zoom-out,
        .leaflet-control-attribution {{
            filter: none;
        }}
        
        dialog::backdrop {{
            background-color: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(2px);
        }}
        
        /* Prevent selection during drag */
        .no-select {{
            user-select: none;
            -webkit-user-select: none;
        }}
        
        /* Custom scrollbar for table */
        ::-webkit-scrollbar {{ width: 8px; height: 8px; }}
        ::-webkit-scrollbar-track {{ background: #0f172a; }}
        ::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #475569; }}

        /* Language toggling CSS */
        html[lang="pl"] .lang-en {{ display: none !important; }}
        html[lang="en"] .lang-pl {{ display: none !important; }}

        /* Custom scrollbar for table container */
        .custom-table-scroll::-webkit-scrollbar {{ 
            width: 8px; 
            height: 8px; 
            background: #1e293b; /* Fills the top right corner gap matching header bg-slate-800 */
            border-top-right-radius: 8px;
        }}
        .custom-table-scroll::-webkit-scrollbar-track {{ 
            background: #0f172a; 
            margin-top: 65px; /* Exact height of the sticky table header */
            border-bottom-right-radius: 8px;
        }}
        .custom-table-scroll::-webkit-scrollbar-thumb {{ background: #334155; border-radius: 4px; }}
        .custom-table-scroll::-webkit-scrollbar-thumb:hover {{ background: #475569; }}

        /* Time Input Dark Mode Icon Fix */
        input[type="time"]::-webkit-calendar-picker-indicator {{
            filter: invert(0.8) sepia(1) saturate(5) hue-rotate(45deg);
            cursor: pointer;
            opacity: 0.8;
        }}
        input[type="time"]::-webkit-calendar-picker-indicator:hover {{
            opacity: 1;
            filter: invert(0.9) sepia(1) saturate(5) hue-rotate(45deg);
        }}

        /* Mobile Map Controls Scaling */
        @media (max-width: 767px) {{
            .leaflet-control-zoom a, .leaflet-control-custom a {{
                width: 26px !important;
                height: 26px !important;
                font-size: 12px !important;
            }}
        }}

        /* Ensure popups render above map controls (+/- and eye button) */
        .leaflet-map-pane {{
            z-index: auto !important;
        }}
        .leaflet-popup-pane {{
            z-index: 1005 !important;
        }}

        /* Smooth transitions for map controls */
        .leaflet-control-zoom, .leaflet-control-custom {{
            transition: opacity 0.2s ease-in-out !important;
        }}

        /* Fade out controls when a popup is open to prevent overlapping */
        .leaflet-container:has(.leaflet-popup) .leaflet-control-zoom,
        .leaflet-container:has(.leaflet-popup) .leaflet-control-custom {{
            opacity: 0 !important;
            pointer-events: none !important;
        }}
    </style>
</head>
<body class="bg-slate-900 text-slate-200 font-sans antialiased h-[100dvh] w-full overflow-hidden flex flex-col md:flex-row">

    <!-- Map Section -->
    <div id="map-container" class="w-full h-[33vh] md:h-screen md:w-[45%] flex-shrink-0 z-0 relative transition-all duration-300">
        <div id="map" class="w-full h-full bg-[#f8f9fa]"></div>

    </div>

    <!-- Resizer -->
    <div id="resizer" class="bg-slate-700 hover:bg-lime-500 flex items-center justify-center cursor-row-resize md:cursor-col-resize h-3 w-full md:h-full md:w-3 z-50 transition-colors flex-shrink-0 border-y border-slate-800 md:border-y-0 md:border-x">
       <div class="bg-slate-400 w-8 h-1 rounded md:h-8 md:w-1 pointer-events-none"></div>
    </div>

    <!-- Right Panel (Tabs + Content) -->
    <div id="content-container" class="flex-1 flex flex-col min-w-0 bg-slate-900 z-10 shadow-[-10px_0_15px_-3px_rgba(0,0,0,0.5)] h-[60vh] md:h-screen overflow-hidden">
        
        <!-- Header & Tabs -->
        <div class="p-3 md:p-6 pb-0 flex-shrink-0 bg-slate-900 z-20">
            <div class="flex justify-between items-center w-full">
                <div>
                    <h1 class="text-xl sm:text-2xl md:text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-lime-400 to-cyan-400 mb-0.5">Wyrypa 100km Ultra-Trekking</h1>
                    <p class="text-[10px] md:text-xs text-slate-400 italic mb-0"><span class="lang-pl">Prawdziwe chodzenie zaczyna się po setce...</span><span class="lang-en">Real walking begins after a hundred...</span></p>
                </div>
                <!-- Show Map Button -->
                <button id="show-map-btn" class="hidden h-[28px] leading-[26px] bg-lime-600 hover:bg-lime-500 text-slate-900 px-2 sm:px-3 rounded shadow border border-lime-500 font-bold text-[10px] sm:text-xs transition-colors whitespace-nowrap cursor-pointer ml-2 flex-shrink-0"><span class="lang-pl">Pokaż mapę</span><span class="lang-en">Show Map</span></button>
            </div>
             
            <!-- Tab Bar -->
            <div class="flex border-b border-slate-700 mt-2 md:mt-4 mb-2 overflow-x-auto hide-scrollbar text-sm md:text-base" id="tab-bar">
                <button class="tab-btn active px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-lime-400 text-lime-400 font-bold focus:outline-none transition-colors whitespace-nowrap" data-target="tab-overview"><span class="lang-pl">Przegląd</span><span class="lang-en">Overview</span></button>
                <button class="tab-btn px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-transparent text-slate-500 hover:text-slate-300 font-medium focus:outline-none transition-colors whitespace-nowrap" data-target="tab-table"><span class="lang-pl">Tabela</span><span class="lang-en">Data Table</span></button>
                <button class="tab-btn px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-transparent text-slate-500 hover:text-slate-300 font-medium focus:outline-none transition-colors whitespace-nowrap" data-target="tab-taktyka"><span class="lang-pl">Taktyka</span><span class="lang-en">Tactics</span></button>
                <button class="tab-btn px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-transparent text-slate-500 hover:text-slate-300 font-medium focus:outline-none transition-colors whitespace-nowrap" data-target="tab-inwentarz"><span class="lang-pl">Inwentarz</span><span class="lang-en">Inventory</span></button>
                <button class="tab-btn px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-transparent text-slate-500 hover:text-slate-300 font-medium focus:outline-none transition-colors whitespace-nowrap" data-target="tab-harmonogram"><span class="lang-pl">Harmonogram</span><span class="lang-en">Schedule</span></button>
                <button class="tab-btn px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-transparent text-slate-500 hover:text-slate-300 font-medium focus:outline-none transition-colors whitespace-nowrap" data-target="tab-testy"><span class="lang-pl">Testy</span><span class="lang-en">Tests</span></button>
                <button class="tab-btn px-3 md:px-4 py-1.5 md:py-2 border-b-2 border-transparent text-slate-500 hover:text-slate-300 font-medium focus:outline-none transition-colors whitespace-nowrap" data-target="tab-trening"><span class="lang-pl">Trening</span><span class="lang-en">Training</span></button>
            </div>
             

        </div>


        <!-- Tab Content: Overview -->
        <div id="tab-overview" class="tab-content p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-slate-300">
            <div class="bg-slate-800/50 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl mb-3 md:mb-4">
                
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">Ustawienia</span><span class="lang-en">Settings</span></h2>
                <div class="flex flex-row flex-wrap gap-2 md:gap-3 items-center mb-4 md:mb-6">
                    <!-- Start Time Input -->
                    <div class="flex items-center space-x-2 bg-slate-800 p-1.5 md:p-2 px-2 md:px-3 rounded border border-slate-600 shadow-sm">
                        <label for="start-time-input" class="text-xs md:text-sm font-bold text-slate-300 whitespace-nowrap"><span class="lang-pl">Godzina Startu:</span><span class="lang-en">Start Time:</span></label>
                        <input type="time" id="start-time-input" class="bg-slate-900 border border-slate-600 text-lime-400 font-bold rounded px-1.5 md:px-2 py-0.5 md:py-1 text-xs md:text-sm text-center outline-none focus:border-lime-400 cursor-pointer">
                    </div>

                    <!-- Language Toggle -->
                    <div class="flex bg-slate-800 rounded border border-slate-600 overflow-hidden shadow-sm h-[28px] md:h-[38px]">
                        <button id="btn-lang-pl" class="px-3 md:px-4 text-xs md:text-sm font-bold bg-lime-500 text-slate-900 transition-colors">PL</button>
                        <button id="btn-lang-en" class="px-3 md:px-4 text-xs md:text-sm font-bold bg-slate-700 text-slate-400 hover:text-white transition-colors">EN</button>
                    </div>
                </div>

                <h2 class="text-base md:text-lg font-bold text-cyan-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">Parametry Wyzwania</span><span class="lang-en">Challenge Parameters</span></h2>
                
                <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 md:gap-4">
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
                </div>

            </div>

            <!-- Elevation Profile Card -->
            <div class="bg-slate-800/50 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl mt-3 md:mt-4">
                <h2 class="text-base md:text-lg font-bold text-cyan-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2">
                    <span class="lang-pl">Profil Wysokości Trasy</span>
                    <span class="lang-en">Route Elevation Profile</span>
                </h2>
                <div class="w-full relative mb-4">
                    <canvas id="overview-elevation-canvas" class="w-full bg-[#0f172a] border border-slate-700/50 rounded shadow-inner h-48 md:h-64 cursor-crosshair"></canvas>
                </div>
                
                <!-- Legend for slope colors -->
                <div class="flex flex-wrap gap-2 md:gap-4 text-[10px] md:text-xs font-semibold justify-center bg-slate-900/60 p-2 md:p-3 rounded border border-slate-800">
                    <div class="flex items-center"><span class="w-2.5 h-2.5 bg-red-600 inline-block mr-1.5 rounded-full"></span><span class="lang-pl">Stromo w górę (&gt;15%)</span><span class="lang-en">Steep Up (&gt;15%)</span></div>
                    <div class="flex items-center"><span class="w-2.5 h-2.5 bg-orange-500 inline-block mr-1.5 rounded-full"></span><span class="lang-pl">W górę (5-15%)</span><span class="lang-en">Up (5-15%)</span></div>
                    <div class="flex items-center"><span class="w-2.5 h-2.5 bg-blue-500 inline-block mr-1.5 rounded-full"></span><span class="lang-pl">Płasko (-5 do 5%)</span><span class="lang-en">Flat (-5 to 5%)</span></div>
                    <div class="flex items-center"><span class="w-2.5 h-2.5 bg-lime-500 inline-block mr-1.5 rounded-full"></span><span class="lang-pl">W dół (-15 do -5%)</span><span class="lang-en">Down (-15 to -5%)</span></div>
                    <div class="flex items-center"><span class="w-2.5 h-2.5 bg-green-600 inline-block mr-1.5 rounded-full"></span><span class="lang-pl">Stromo w dół (&lt;-15%)</span><span class="lang-en">Steep Down (&lt;-15%)</span></div>
                </div>
            </div>
        </div>

        <!-- Tab Content: Data Table -->
        <div id="tab-table" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 flex flex-col overflow-hidden">
            <div class="rounded-lg border border-slate-700 shadow-xl bg-slate-800/50 flex-1 overflow-y-auto custom-table-scroll">
                <table class="w-full text-left border-collapse whitespace-nowrap md:whitespace-normal min-w-[600px]">
                    <thead class="sticky top-0 z-30">
                        <tr class="bg-slate-800 border-b border-slate-700 text-slate-300 text-[10px] md:text-sm uppercase tracking-wider">
                            <th class="p-2 md:p-3 font-semibold bg-slate-800">KM</th>
                            <th class="p-2 md:p-3 font-semibold bg-slate-800"><span class="lang-pl">Czas</span><span class="lang-en">Time</span></th>
                            <th class="p-2 md:p-3 font-semibold bg-slate-800"><span class="lang-pl">Śr. Całość</span><span class="lang-en">Avg Total</span></th>
                            <th class="p-2 md:p-3 font-semibold border-r border-slate-700/50 bg-slate-800"><span class="lang-pl">Śr. Odcinek</span><span class="lang-en">Section Avg</span></th>
                            <th class="p-2 md:p-3 font-semibold bg-slate-800"><span class="lang-pl">Wzn.</span><span class="lang-en">Ele</span></th>
                            <th class="p-2 md:p-3 font-semibold min-w-[200px] bg-slate-800"><span class="lang-pl">Akcja</span><span class="lang-en">Action</span></th>
                            <th class="p-2 md:p-3 font-semibold text-center bg-slate-800"><span class="lang-pl">Profil</span><span class="lang-en">Profile</span></th>
                        </tr>
                    </thead>
                    <tbody id="data-table" class="divide-y divide-slate-800/50">
                    </tbody>
                </table>
            </div>
        </div>
        <!-- Tab: Taktyka -->
        <div id="tab-taktyka" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
            <div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl mb-4">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">ZASADY RUCHU I TAKTYKA 12 KG</span><span class="lang-en">MOVEMENT RULES & 12KG TACTICS</span></h2>
                <ul class="space-y-4">
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Płasko (&lt; 8%):</strong> Tempo 12:30 - 13:30 min/km.</span><span class="lang-en">Flat (&lt; 8%):</strong> Pace 12:30 - 13:30 min/km.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Podejścia (8-15%):</strong> Tempo 15:00 - 18:00 min/km. Krótki krok, aktywna praca kijami.</span><span class="lang-en">Uphills (8-15%):</strong> Pace 15:00 - 18:00 min/km. Short steps, active poles.</span></div></li>
                    <li class="flex items-start"><span class="text-amber-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Ściany (&gt; 15%):</strong> Tempo 22:00+ min/km. Przekroczenie HR 155 = natychmiastowe zwolnienie kroku.</span><span class="lang-en">Walls (&gt; 15%):</strong> Pace 22:00+ min/km. Exceeding HR 155 = slow down immediately.</span></div></li>
                    <li class="flex items-start"><span class="text-red-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Zbiegi:</strong> Kategoryczny zakaz uderzeń piętą. Lądowanie na śródstopiu, amortyzacja kijkami przed sobą.</span><span class="lang-en">Downhills:</strong> Strict ban on heel strikes. Midfoot landing, pole absorption in front.</span></div></li>
                </ul>
            </div>
        </div>

        <!-- Tab: Inwentarz -->
        <div id="tab-inwentarz" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                <div class="bg-slate-800/50 p-5 rounded-lg border border-slate-700 shadow-xl">
                    <h3 class="text-lg font-bold text-cyan-400 mb-3 border-b border-slate-700 pb-2"><span class="lang-pl">Baza Płynna (Hyper-Mix 2:1)</span><span class="lang-en">Liquid Base (Hyper-Mix 2:1)</span></h3>
                    <p class="text-sm text-slate-400 italic mb-3"><span class="lang-pl">Przygotuj 10 strunowych woreczków. 1 woreczek = 1 bidon 500-700ml.</span><span class="lang-en">Prepare 10 ziplock bags. 1 bag = 1 flask 500-700ml.</span></p>
                    <ul class="space-y-2 text-sm">
                        <li class="flex items-center"><span class="w-2 h-2 bg-cyan-500 rounded-full mr-2 flex-shrink-0"></span><span><span class="lang-pl">40g Maltodekstryny + 20g Fruktozy + 1 saszetka Izotonika + ~500mg Cytrynianu Potasu.</span><span class="lang-en">40g Maltodextrin + 20g Fructose + 1 Isotonic sachet + ~500mg Potassium Citrate.</span></span></li>
                        <li class="flex items-center text-amber-300 font-semibold mt-2"><span class="w-2 h-2 bg-amber-500 rounded-full mr-2 flex-shrink-0"></span><span><span class="lang-pl">Zasada: Wypijasz 1 bidon w ciągu godziny. Nie popijasz tego dodatkową wodą.</span><span class="lang-en">Rule: Drink 1 flask per hour. Do not chase with extra water.</span></span></li>
                    </ul>
                </div>
                
                <div class="bg-slate-800/50 p-5 rounded-lg border border-slate-700 shadow-xl">
                    <h3 class="text-lg font-bold text-red-400 mb-3 border-b border-slate-700 pb-2"><span class="lang-pl">Suplementacja i Rescue</span><span class="lang-en">Supplementation & Rescue</span></h3>
                    <ul class="space-y-3 text-sm">
                        <li><strong class="text-white">SaltStick Caps:</strong> <span class="lang-pl">30 kaps. (2 co 1.5h - 2h)</span><span class="lang-en">30 caps. (2 every 1.5h - 2h)</span></li>
                        <li><strong class="text-white">Dextro Energy:</strong> <span class="lang-pl">24 kostki. (Ssane w marszu co 2h)</span><span class="lang-en">24 cubes. (Suck while walking every 2h)</span></li>
                        <li><strong class="text-white">Red Bull 250ml:</strong> <span class="lang-pl">3 puszki (Na wskazane kryzysy)</span><span class="lang-en">3 cans (For indicated crises)</span></li>
                        <li class="bg-red-900/30 p-2 rounded border border-red-800"><strong class="text-red-400"><span class="lang-pl">Rescue Protocol (Odcięcie):</span><span class="lang-en">Rescue Protocol (Bonking):</span></strong> <span class="lang-pl">1 saszetka Płynnej Glukozy 1WW pod język + popić min. 150ml wody.</span><span class="lang-en">1 sachet Liquid Glucose under tongue + drink min. 150ml water.</span></li>
                    </ul>
                </div>
                
                <div class="bg-slate-800/50 p-5 rounded-lg border border-slate-700 shadow-xl md:col-span-2">
                    <h3 class="text-lg font-bold text-orange-400 mb-3 border-b border-slate-700 pb-2"><span class="lang-pl">Jedzenie Stałe</span><span class="lang-en">Solid Food</span></h3>
                    <p class="text-sm text-slate-400 italic mb-3"><span class="lang-pl">Ciała stałe jesz i popijasz czystą wodą</span><span class="lang-en">Eat solids and chase with clean water</span> (Target: 60g Carbs/h).</p>
                    <div class="flex flex-wrap gap-3">
                        <span class="bg-slate-700 px-3 py-1 rounded-full text-sm shadow">🥪 <span class="lang-pl">6-8 Kanapek (szynka/ser/masło orzechowe)</span><span class="lang-en">6-8 Sandwiches (ham/cheese/pb)</span></span>
                        <span class="bg-slate-700 px-3 py-1 rounded-full text-sm shadow">🍫 <span class="lang-pl">8-10 Batonów owsianych</span><span class="lang-en">8-10 Oat bars</span></span>
                        <span class="bg-slate-700 px-3 py-1 rounded-full text-sm shadow">🍯 <span class="lang-pl">10 Żeli energetycznych</span><span class="lang-en">10 Energy gels</span></span>
                        <span class="bg-slate-700 px-3 py-1 rounded-full text-sm shadow">🍌 <span class="lang-pl">5 Bananów</span><span class="lang-en">5 Bananas</span></span>
                        <span class="bg-slate-700 px-3 py-1 rounded-full text-sm shadow">🍎 <span class="lang-pl">2 Jabłka</span><span class="lang-en">2 Apples</span></span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Harmonogram -->
        <div id="tab-harmonogram" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
            <div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">HARMONOGRAM OGÓLNY I POSTOJE</span><span class="lang-en">GENERAL SCHEDULE & STOPS</span></h2>
                <p class="text-sm text-slate-400 italic mb-6"><span class="lang-pl">Wszystkie dłuższe postoje zaplanowane są na wypłaszczeniach/przełęczach po zakończeniu zejść, aby uniknąć wychłodzenia szczytowego i blokady mięśni na zbiegu.</span><span class="lang-en">All longer stops are planned on flats/passes after descents, to avoid peak chilling and muscle blockages on downhills.</span></p>
                
                <div class="relative border-l-2 border-slate-600 ml-3 pl-6 space-y-6">
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-slate-500 w-4 h-4 rounded-full mt-1.5"></span>
                        <h4 class="font-bold text-white text-lg">0 - 25 km</h4>
                        <p class="text-sm"><span class="lang-pl">Marsz ciągły.</span><span class="lang-en">Continuous march.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">25 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 5 min</span><span class="lang-en">5 min break</span></span></h4>
                        <p class="text-sm"><span class="lang-pl">Przełęcz. Zmiana skarpet na suche (kluczowe dla ochrony stopy przed 12kg naciskiem).</span><span class="lang-en">Mountain pass. Change socks to dry ones (crucial to protect feet against 12kg pressure).</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-slate-500 w-4 h-4 rounded-full mt-1.5"></span>
                        <h4 class="font-bold text-white text-lg">25 - 50 km</h4>
                        <p class="text-sm"><span class="lang-pl">Nocny marsz, chłodno.</span><span class="lang-en">Night march, chilly.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">50 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 5 min</span><span class="lang-en">5 min break</span></span></h4>
                        <p class="text-sm"><span class="lang-pl">Przygotowanie mentalne i sprzętowe sprzętu pod przepak.</span><span class="lang-en">Mental and gear prep for the drop bag point.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-[34px] bg-slate-900 border-2 border-lime-500 w-5 h-5 rounded-full mt-1 flex items-center justify-center shadow-[0_0_12px_rgba(132,204,22,0.6)]"><span class="bg-lime-500 w-2 h-2 rounded-full"></span></span>
                        <h4 class="font-bold text-lime-400 text-xl">60 km - <span class="lang-pl">PRZEPAK</span><span class="lang-en">DROP BAG</span> <span class="text-sm text-lime-400 font-normal ml-2 bg-lime-900/30 px-2 py-0.5 rounded border border-lime-700"><span class="lang-pl">Przerwa 30 min</span><span class="lang-en">30 min break</span></span></h4>
                        <p class="text-sm"><span class="lang-pl">Obowiązkowa zmiana butów, zjedzenie ciepłego posiłku (zupa), pobranie 50% depozytu (Hyper-mix, suple, batony).</span><span class="lang-en">Mandatory shoe change, eat warm meal (soup), take 50% of deposit (Hyper-mix, supplements, bars).</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">75 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 5 min</span><span class="lang-en">5 min break</span></span></h4>
                        <p class="text-sm"><span class="lang-pl">Dolina. Kontrola otarć, chłodzenie karku wodą przed najgorszym upałem.</span><span class="lang-en">Valley. Chafing check, cool neck with water before the worst heat.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-red-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(239,68,68,0.5)]"></span>
                        <h4 class="font-bold text-red-400 text-lg">75 - 100 km</h4>
                        <p class="text-sm"><span class="lang-pl">Marsz na czas. Zatrzymanie tylko w przypadku odcięcia.</span><span class="lang-en">Time trial march. Stop only in case of a complete bonk.</span></p>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Testy -->
        <div id="tab-testy" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div class="bg-slate-800/50 p-5 rounded-lg border border-slate-700 shadow-xl">
                    <h3 class="text-lg font-bold text-blue-400 mb-2 border-b border-slate-700 pb-2">Test A: 70 km (Balast 12 kg)</h3>
                    <p class="text-sm text-slate-400 italic mb-4"><span class="lang-pl">Test sprzętowy i trawienny na długim dystansie.</span><span class="lang-en">Gear and digestion test over long distance.</span></p>
                    <ol class="list-decimal pl-5 space-y-2 text-sm marker:text-blue-500 font-medium">
                        <li><strong class="text-white">0 - 30 km:</strong> <span class="lang-pl">Test pełnego reżimu suplementacji (Sól co 1.5h, Hyper-Mix co 1h).</span><span class="lang-en">Full supplementation regime test (Salt every 1.5h, Hyper-Mix every 1h).</span></li>
                        <li><strong class="text-white">30 km:</strong> <span class="lang-pl">Ściągasz buty i sprawdzasz stopy. Jeśli są odciski lub ostre pieczenie, konfiguracja sprzętowa do zmiany.</span><span class="lang-en">Take off shoes and check feet. If blisters or burning, change gear setup.</span></li>
                        <li><strong class="text-white">50 km:</strong> <span class="lang-pl">Test wymuszonego zjedzenia kanapki popitej Red Bullem. Sprawdzasz, czy żołądek nie buntuje się po 12h.</span><span class="lang-en">Forced eating of a sandwich washed down with Red Bull. Check if stomach rebels after 12h.</span></li>
                        <li class="text-lime-400 mt-3 p-2 bg-slate-900 border border-slate-700 rounded"><strong class="text-lime-400"><span class="lang-pl">Cel:</span><span class="lang-en">Goal:</span></strong> <span class="lang-pl">Ukończenie w granicach 16.5 - 17.5h.</span><span class="lang-en">Finish around 16.5 - 17.5h.</span></li>
                    </ol>
                </div>
                
                <div class="bg-slate-800/50 p-5 rounded-lg border border-slate-700 shadow-xl">
                    <h3 class="text-lg font-bold text-purple-400 mb-2 border-b border-slate-700 pb-2">Test B: 42 km (Balast 10-12 kg)</h3>
                    <p class="text-sm text-slate-400 italic mb-4"><span class="lang-pl">Test dynamiki zbiegów i procedur w ruchu.</span><span class="lang-en">Downhill dynamics and moving procedures test.</span></p>
                    <ol class="list-decimal pl-5 space-y-2 text-sm marker:text-purple-500 font-medium">
                        <li><strong class="text-white">0 - 20 km:</strong> <span class="lang-pl">Skupienie na brutalnie mocnej pracy ramion na podejściach. Kije mają przejmować 20% masy.</span><span class="lang-en">Focus on brutally strong arm work on uphills. Poles should take 20% of the mass.</span></li>
                        <li><strong class="text-white">20 - 30 km:</strong> <span class="lang-pl">Procedury w ruchu. Wyciąganie batona, jedzenie i chowanie śmieci bez zatrzymywania marszu.</span><span class="lang-en">Procedures on the move. Pulling out a bar, eating and stowing trash without stopping.</span></li>
                        <li><strong class="text-white">30 km:</strong> <span class="lang-pl">Uruchomienie procedury Rescue (Red Bull + Glukoza) i narzucenie ostrego tempa, aby sprawdzić obciążenie prawego kolana na zmęczeniu.</span><span class="lang-en">Activate Rescue protocol (Red Bull + Glucose) and push a hard pace to check right knee stress under fatigue.</span></li>
                        <li class="text-lime-400 mt-3 p-2 bg-slate-900 border border-slate-700 rounded"><strong class="text-lime-400"><span class="lang-pl">Cel:</span><span class="lang-en">Goal:</span></strong> <span class="lang-pl">Ukończenie &lt; 9.5h.</span><span class="lang-en">Finish &lt; 9.5h.</span></li>
                    </ol>
                </div>
            </div>
        </div>

        <!-- Tab: Trening -->
        <div id="tab-trening" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
            <div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">PROGRAM CORE &amp; MTB (W Tygodniu)</span><span class="lang-en">CORE &amp; MTB PROGRAM (Weekly)</span></h2>
                <p class="text-sm text-slate-400 italic mb-6"><span class="lang-pl">12kg plecak wymaga wzmocnienia gorsetu i ścięgien, rower nie załatwi tu wszystkiego.</span><span class="lang-en">12kg backpack requires core and tendon strengthening, bike won't fix everything.</span></p>
                
                <div class="space-y-4">
                    <div class="bg-slate-900 p-4 rounded border border-slate-700 flex items-start shadow">
                        <div class="text-3xl mr-4">🚵‍♂️</div>
                        <div>
                            <h4 class="font-bold text-white text-lg"><span class="lang-pl">Rower MTB (1x tydz. 45-60 min)</span><span class="lang-en">MTB Bike (1x week 45-60 min)</span></h4>
                            <p class="text-sm text-slate-400 mt-1"><span class="lang-pl">Trening "siłowy". Sztywne podjazdy, niskie RPM (50-60), żeby wzmocnić czworogłowe pod ciężar na zbiegach.</span><span class="lang-en">"Strength" training. Steep climbs, low RPM (50-60), to strengthen quads for downhill weight bearing.</span></p>
                        </div>
                    </div>
                    
                    <div class="bg-slate-900 p-4 rounded border border-slate-700 flex items-start shadow">
                        <div class="text-3xl mr-4">🚴‍♀️</div>
                        <div>
                            <h4 class="font-bold text-white text-lg"><span class="lang-pl">Rowerek domowy (1x tydz. 60 min)</span><span class="lang-en">Stationary bike (1x week 60 min)</span></h4>
                            <p class="text-sm text-slate-400 mt-1"><span class="lang-pl">Regeneracja tlenowa, HR 120-130.</span><span class="lang-en">Aerobic recovery, HR 120-130.</span></p>
                        </div>
                    </div>
                    
                    <div class="bg-slate-900 p-4 rounded border border-slate-700 flex items-start shadow">
                        <div class="text-3xl mr-4">🧘‍♂️</div>
                        <div class="w-full">
                            <h4 class="font-bold text-white text-lg mb-3"><span class="lang-pl">Core w domu (3x tydz. po 10 min)</span><span class="lang-en">Core at home (3x week 10 min)</span></h4>
                            <ul class="space-y-2 text-sm bg-slate-800 p-3 rounded">
                                <li class="flex justify-between items-center"><span class="font-semibold text-slate-300"><span class="lang-pl">Plank (Deska)</span><span class="lang-en">Plank</span></span><span class="text-cyan-400 font-mono bg-slate-900 px-2 py-1 rounded"><span class="lang-pl">3 x 60s (plecy)</span><span class="lang-en">3 x 60s (back)</span></span></li>
                                <li class="flex justify-between items-center border-t border-slate-700 pt-2"><span class="font-semibold text-slate-300"><span class="lang-pl">Wspięcia na palce boso</span><span class="lang-en">Barefoot calf raises</span></span><span class="text-cyan-400 font-mono bg-slate-900 px-2 py-1 rounded"><span class="lang-pl">3 x 20 (lewe śródstopie)</span><span class="lang-en">3 x 20 (left midfoot)</span></span></li>
                                <li class="flex justify-between items-center border-t border-slate-700 pt-2"><span class="font-semibold text-slate-300"><span class="lang-pl">Przysiady na jednej nodze (bułgarskie)</span><span class="lang-en">Single-leg squats (Bulgarian)</span></span><span class="text-cyan-400 font-mono bg-slate-900 px-2 py-1 rounded"><span class="lang-pl">3 x 10 / nogę (prawe kolano)</span><span class="lang-en">3 x 10 / leg (right knee)</span></span></li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </div>

    </div>

    <!-- Profile Modal -->
    <dialog id="chart-modal" class="bg-slate-800 text-slate-200 p-6 rounded-lg border border-slate-600 shadow-2xl w-11/12 md:w-3/4 max-w-4xl max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
            <h2 id="chart-modal-title" class="text-base md:text-lg font-bold text-lime-400"><span class="lang-pl">Profil Odcinka</span><span class="lang-en">Section Profile</span></h2>
            <button onclick="document.getElementById('chart-modal').close()" class="text-slate-400 hover:text-white text-3xl leading-none cursor-pointer">&times;</button>
        </div>
        <div class="w-full relative mb-4">
            <canvas id="detailed-canvas" width="800" height="300" class="w-full bg-[#f8f9fa] border border-slate-500 rounded"></canvas>
        </div>
        <div class="flex flex-wrap gap-4 text-xs font-semibold justify-center bg-slate-900 p-3 rounded border border-slate-700">
            <div class="flex items-center"><span class="w-3 h-3 bg-red-600 inline-block mr-2 rounded-full"></span><span class="lang-pl">Stromo w górę (&gt;15%)</span><span class="lang-en">Steep Up (&gt;15%)</span></div>
            <div class="flex items-center"><span class="w-3 h-3 bg-orange-500 inline-block mr-2 rounded-full"></span><span class="lang-pl">W górę (5-15%)</span><span class="lang-en">Up (5-15%)</span></div>
            <div class="flex items-center"><span class="w-3 h-3 bg-blue-500 inline-block mr-2 rounded-full"></span><span class="lang-pl">Płasko (-5 do 5%)</span><span class="lang-en">Flat (-5 to 5%)</span></div>
            <div class="flex items-center"><span class="w-3 h-3 bg-lime-500 inline-block mr-2 rounded-full"></span><span class="lang-pl">W dół (-15 do -5%)</span><span class="lang-en">Down (-15 to -5%)</span></div>
            <div class="flex items-center"><span class="w-3 h-3 bg-green-600 inline-block mr-2 rounded-full"></span><span class="lang-pl">Stromo w dół (&lt;-15%)</span><span class="lang-en">Steep Down (&lt;-15%)</span></div>
        </div>
    </dialog>

    <script>
        {leaflet_js}
    </script>
    <script>
        {leaflet_gpx_js}
    </script>

    <script>
        const checkpoints = {checkpoints_json};
        const rawGpxData = `{gpx_content_escaped}`;
        let gpxElevationData = [];
        let overviewHoveredPoint = null;
        let highlightedSectionIndex = null;
        let gpxTrackPoints = [];
        let mapHoverMarker = null;

        const map = L.map('map').setView([49.762544, 19.086507], 11);

        function getLayerLatLngs(layer) {{
            let pts = [];
            function extract(l) {{
                if (typeof l.getLatLngs === 'function') {{
                    const latlngs = l.getLatLngs();
                    if (latlngs.length > 0) {{
                        if (Array.isArray(latlngs[0])) {{
                            latlngs.forEach(arr => {{
                                if (Array.isArray(arr)) {{
                                    pts.push(...arr);
                                }} else {{
                                    pts.push(arr);
                                }}
                            }});
                        }} else {{
                            pts.push(...latlngs);
                        }}
                    }}
                }} else if (typeof l.eachLayer === 'function') {{
                    l.eachLayer(extract);
                }}
            }}
            extract(layer);
            return pts;
        }}

        function updateMapHoverPointer(hoverKm) {{
            const mapContainer = document.getElementById('map-container');
            const isMapVisible = mapContainer && !mapContainer.classList.contains('hidden') && mapContainer.style.display !== 'none';
            if (!isMapVisible || !gpxTrackPoints || gpxTrackPoints.length === 0) return;
            
            // Find closest point in gpxTrackPoints
            let closestTrackPt = gpxTrackPoints[0];
            let minDist = Math.abs(closestTrackPt.km - hoverKm);
            for (let i = 1; i < gpxTrackPoints.length; i++) {{
                const d = Math.abs(gpxTrackPoints[i].km - hoverKm);
                if (d < minDist) {{
                    minDist = d;
                    closestTrackPt = gpxTrackPoints[i];
                }}
            }}
            
            // Update or create the marker
            if (!mapHoverMarker) {{
                mapHoverMarker = L.circleMarker(closestTrackPt.latlng, {{
                    radius: 7,
                    fillColor: '#22d3ee', // Cyan-400
                    fillOpacity: 1,
                    color: '#ffffff', // White border
                    weight: 2,
                    className: 'map-hover-pointer'
                }}).addTo(map);
            }} else {{
                mapHoverMarker.setLatLng(closestTrackPt.latlng);
            }}
            
            // Recenter only if the pointer gets close to the edge of the viewport
            const containerPoint = map.latLngToContainerPoint(closestTrackPt.latlng);
            const mapSize = map.getSize();
            const marginX = mapSize.x * 0.05; // 5% margin from left/right edges
            const marginY = mapSize.y * 0.05; // 5% margin from top/bottom edges
            
            if (containerPoint.x < marginX || 
                containerPoint.x > mapSize.x - marginX || 
                containerPoint.y < marginY || 
                containerPoint.y > mapSize.y - marginY) {{
                map.panTo(closestTrackPt.latlng, {{ animate: true, duration: 0.4 }});
            }}
        }}

        function clearMapHoverPointer() {{
            if (mapHoverMarker) {{
                map.removeLayer(mapHoverMarker);
                mapHoverMarker = null;
            }}
        }}

        L.tileLayer('https://{{s}}.tile.opentopomap.org/{{z}}/{{x}}/{{y}}.png', {{
            maxZoom: 17,
            attribution: 'Map data: &copy; OSM | Style: &copy; OpenTopoMap'
        }}).addTo(map);

        // Custom Hide Map Control (Eye Icon)
        var HideMapControl = L.Control.extend({{
            options: {{ position: 'topleft' }},
            onAdd: function (map) {{
                var container = L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');
                container.innerHTML = `<a href="#" title="Hide Map" style="display: flex; align-items: center; justify-content: center;" class="hover:bg-slate-50 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="#475569" stroke-width="2.5" style="width: 16px; height: 16px;">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" />
                        <path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                    </svg>
                </a>`;
                container.onclick = function(e){{
                    e.preventDefault();
                    e.stopPropagation();
                    
                    const mapContainer = document.getElementById('map-container');
                    const resizer = document.getElementById('resizer');
                    const contentContainer = document.getElementById('content-container');
                    const showMapBtn = document.getElementById('show-map-btn');
                    
                    mapContainer.classList.add('hidden');
                    mapContainer.style.display = 'none';
                    resizer.style.display = 'none';
                    contentContainer.style.height = '100dvh';
                    
                    showMapBtn.classList.remove('hidden');
                }}
                return container;
            }}
        }});
        map.addControl(new HideMapControl());

        // Custom Fit Track Control (Fit to view / zoom out)
        var FitTrackControl = L.Control.extend({{
            options: {{ position: 'topright' }},
            onAdd: function (map) {{
                var container = L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');
                container.innerHTML = `<a href="#" title="Fit Entire Track to View" style="display: flex; align-items: center; justify-content: center;" class="hover:bg-slate-50 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="#475569" stroke-width="2.5" style="width: 16px; height: 16px;">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M3.75 3.75v4.5m0-4.5h4.5m-4.5 0L9 9M3.75 20.25v-4.5m0 4.5h4.5m-4.5 0L9 15M20.25 3.75v4.5m0-4.5h-4.5m4.5 0L15 9m5.25 11.25v-4.5m0 4.5h-4.5m4.5 0l-5.25-5.25" />
                    </svg>
                </a>`;
                container.onclick = function(e){{
                    e.preventDefault();
                    e.stopPropagation();
                    if (gpxLayer) {{
                        map.invalidateSize();
                        const mapContainer = document.getElementById('map-container');
                        const paddingVal = (mapContainer && mapContainer.offsetHeight < 400) ? [10, 10] : [30, 30];
                        map.fitBounds(gpxLayer.getBounds(), {{ padding: paddingVal, animate: true, duration: 1 }});
                    }}
                }}
                return container;
            }}
        }});
        map.addControl(new FitTrackControl());

        const gpxLayer = new L.GPX(rawGpxData, {{
            async: true,
            marker_options: {{ startIconUrl: '', endIconUrl: '', shadowUrl: '' }},
            polyline_options: {{
                color: '#ef4444',
                opacity: 0.9,
                weight: 5,
                lineCap: 'round'
            }}
        }}).on('loaded', function(e) {{
            map.invalidateSize();
            const mapContainer = document.getElementById('map-container');
            const paddingVal = (mapContainer && mapContainer.offsetHeight < 400) ? [10, 10] : [20, 20];
            map.fitBounds(e.target.getBounds(), {{ padding: paddingVal }});
            gpxElevationData = e.target.get_elevation_data();
            
            // Build gpxTrackPoints
            const allLatLngs = getLayerLatLngs(e.target);
            let currentDist = 0;
            gpxTrackPoints = [];
            for (let i = 0; i < allLatLngs.length; i++) {{
                if (i > 0) {{
                    currentDist += allLatLngs[i-1].distanceTo(allLatLngs[i]) / 1000.0;
                }}
                gpxTrackPoints.push({{
                    latlng: allLatLngs[i],
                    km: currentDist
                }});
            }}

            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderMiniCharts();
                renderOverviewElevationChart();
            }}
        }}).addTo(map);

        map.on('click', () => {{
            if (highlightedPolyline) {{
                map.removeLayer(highlightedPolyline);
                highlightedPolyline = null;
            }}
            highlightedSectionIndex = null;
            document.querySelectorAll('tbody tr').forEach(row => row.classList.remove('table-row-highlight'));
            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderOverviewElevationChart();
            }}
        }});
        
        // --- LANGUAGE LOGIC ---
        const btnPl = document.getElementById('btn-lang-pl');
        const btnEn = document.getElementById('btn-lang-en');
        const htmlTag = document.documentElement;
        
        let savedLang = 'pl';
        try {{ savedLang = localStorage.getItem('ultra_lang') || 'pl'; }} catch(e) {{}}
        setLanguage(savedLang);

        btnPl.addEventListener('click', () => setLanguage('pl'));
        btnEn.addEventListener('click', () => setLanguage('en'));

        function setLanguage(lang) {{
            htmlTag.setAttribute('lang', lang);
            try {{ localStorage.setItem('ultra_lang', lang); }} catch(e) {{}}
            
            if (lang === 'pl') {{
                btnPl.className = 'px-2 py-1 text-xs font-bold bg-lime-500 text-slate-900 transition-colors';
                btnEn.className = 'px-2 py-1 text-xs font-bold bg-slate-700 text-slate-400 hover:text-white transition-colors';
            }} else {{
                btnEn.className = 'px-2 py-1 text-xs font-bold bg-lime-500 text-slate-900 transition-colors';
                btnPl.className = 'px-2 py-1 text-xs font-bold bg-slate-700 text-slate-400 hover:text-white transition-colors';
            }}
        }}
        // ----------------------

        // --- TABS LOGIC ---
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {{
            btn.addEventListener('click', () => {{
                tabBtns.forEach(b => {{
                    b.classList.remove('border-lime-400', 'text-lime-400', 'font-bold');
                    b.classList.add('border-transparent', 'text-slate-500', 'font-medium');
                }});
                
                tabContents.forEach(c => c.classList.add('hidden'));
                
                btn.classList.remove('border-transparent', 'text-slate-500', 'font-medium');
                btn.classList.add('border-lime-400', 'text-lime-400', 'font-bold');
                
                const targetId = btn.getAttribute('data-target');
                document.getElementById(targetId).classList.remove('hidden');
                
                // Important: If we switch back to the map/table, we might want to invalidate size
                if (targetId === 'tab-table') {{
                    setTimeout(() => map.invalidateSize(), 100);
                }} else if (targetId === 'tab-overview') {{
                    setTimeout(() => {{
                        if (gpxElevationData && gpxElevationData.length > 0) {{
                            renderOverviewElevationChart();
                        }}
                    }}, 50);
                }}
            }});
        }});
        // ------------------

        // --- MAP RESIZING & TOGGLING LOGIC ---
        const mapContainer = document.getElementById('map-container');
        const resizer = document.getElementById('resizer');
                const showMapBtn = document.getElementById('show-map-btn');
        const contentContainer = document.getElementById('content-container');
        let isResizing = false;



        showMapBtn.addEventListener('click', () => {{
            mapContainer.classList.remove('hidden');
            mapContainer.style.display = 'block';
            resizer.style.display = 'flex';
            
            // Restore default sizes or previously resized sizes
            if (window.innerWidth >= 768) {{
                mapContainer.style.width = mapContainer.dataset.lastWidth || '45%';
                mapContainer.style.height = '100dvh';
                contentContainer.style.height = '100dvh';
            }} else {{
                mapContainer.style.height = mapContainer.dataset.lastHeight || '40vh';
                mapContainer.style.width = '100%';
                contentContainer.style.height = `calc(100dvh - ${{mapContainer.style.height}} - 12px)`;
            }}
            
            showMapBtn.classList.add('hidden');
            setTimeout(() => map.invalidateSize(), 100);
        }});

        // Resizer event listeners
        resizer.addEventListener('mousedown', startResize);
        resizer.addEventListener('touchstart', startResize, {{passive: true}});
        
        document.addEventListener('mousemove', handleResize);
        document.addEventListener('touchmove', handleResize, {{passive: false}});
        
        document.addEventListener('mouseup', stopResize);
        document.addEventListener('touchend', stopResize);

        function startResize(e) {{
            isResizing = true;
            document.body.classList.add('no-select');
            const isDesktop = window.innerWidth >= 768;
            document.body.style.cursor = isDesktop ? 'col-resize' : 'row-resize';
        }}

        function stopResize() {{
            if (!isResizing) return;
            isResizing = false;
            document.body.classList.remove('no-select');
            document.body.style.cursor = '';
            map.invalidateSize();
            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderOverviewElevationChart();
            }}
        }}

        function handleResize(e) {{
            if (!isResizing) return;
            if (e.type === 'touchmove') e.preventDefault(); // prevent scrolling while resizing

            const isDesktop = window.innerWidth >= 768;
            
            if (isDesktop) {{
                const clientX = e.clientX || (e.touches && e.touches[0].clientX);
                if (clientX) {{
                    const newWidth = (clientX / window.innerWidth) * 100;
                    if (newWidth > 10 && newWidth < 90) {{
                        mapContainer.style.width = `${{newWidth}}%`;
                        mapContainer.dataset.lastWidth = `${{newWidth}}%`;
                    }}
                }}
            }} else {{
                const clientY = e.clientY || (e.touches && e.touches[0].clientY);
                if (clientY) {{
                    const newHeight = (clientY / window.innerHeight) * 100;
                    if (newHeight > 10 && newHeight < 85) {{
                        mapContainer.style.height = `${{newHeight}}vh`;
                        mapContainer.dataset.lastHeight = `${{newHeight}}vh`;
                        contentContainer.style.height = `calc(100dvh - ${{newHeight}}vh - 12px)`;
                    }}
                }}
            }}
            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderOverviewElevationChart();
            }}
        }}
        // -------------------------------------

        // --- DATA & TABLE LOGIC ---
        const BASE_START = 19 * 60;
        let prevKm = 0;
        let prevElapsed = 0;
        let cumulativeEle = 0;
        
        checkpoints.forEach(cp => {{
            const eleMatch = cp.ele.match(/\\+?(\\d+)m/);
            const eleValue = eleMatch ? parseInt(eleMatch[1]) : 0;
            cumulativeEle += eleValue;
            cp.cumulative_ele = `+${{cumulativeEle}}m`;
            
            const parts = cp.time.split(':');
            let cpMins = parseInt(parts[0]) * 60 + parseInt(parts[1]);
            let elapsed = cpMins - BASE_START;
            if (elapsed < 0) elapsed += 24 * 60;
            cp.elapsed_minutes = elapsed;
            
            const paceDecimal = cp.elapsed_minutes / cp.km;
            const paceMin = Math.floor(paceDecimal);
            const paceSec = Math.round((paceDecimal - paceMin) * 60);
            cp.overall_pace = `${{paceMin}}:${{paceSec.toString().padStart(2, '0')}}/km`;
            
            const speed = cp.km / (cp.elapsed_minutes / 60);
            cp.overall_speed = `${{speed.toFixed(1)}} km/h`;
            
            const sectionKm = cp.km - prevKm;
            const sectionElapsed = cp.elapsed_minutes - prevElapsed;
            
            if (sectionKm > 0 && sectionElapsed > 0) {{
                const sPaceDec = sectionElapsed / sectionKm;
                const sPaceMin = Math.floor(sPaceDec);
                const sPaceSec = Math.round((sPaceDec - sPaceMin) * 60);
                cp.section_pace = `${{sPaceMin}}:${{sPaceSec.toString().padStart(2, '0')}}/km`;
                
                const sSpeed = sectionKm / (sectionElapsed / 60);
                cp.section_speed = `${{sSpeed.toFixed(1)}} km/h`;
            }} else {{
                cp.section_pace = "N/A";
                cp.section_speed = "N/A";
            }}
            
            prevKm = cp.km;
            prevElapsed = cp.elapsed_minutes;
        }});

        let markers = [];
        const tableBody = document.getElementById('data-table');
        const timeInput = document.getElementById('start-time-input');
        
        try {{ timeInput.value = localStorage.getItem('ultra_start_time') || "19:00"; }} catch(e) {{ timeInput.value = "19:00"; }}
        
        timeInput.addEventListener('change', () => {{
            try {{ localStorage.setItem('ultra_start_time', timeInput.value); }} catch(e) {{}}
            renderApp();
        }});

        let highlightedPolyline = null;

        function highlightSection(index) {{
            if (!gpxLayer) return;
            
            highlightedSectionIndex = index;
            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderOverviewElevationChart();
            }}
            
            const cp = checkpoints[index];
            const startKm = index === 0 ? 0 : checkpoints[index-1].km;
            const endKm = cp.km;
            
            const allLatLngs = getLayerLatLngs(gpxLayer);
            
            let segmentLatLngs = [];
            let currentDist = 0;
            for(let i=0; i<allLatLngs.length; i++) {{
                if(i > 0) {{
                    currentDist += allLatLngs[i-1].distanceTo(allLatLngs[i]) / 1000.0;
                }}
                if(currentDist >= startKm && currentDist <= endKm) {{
                    segmentLatLngs.push(allLatLngs[i]);
                }}
                if(currentDist > endKm) {{
                    segmentLatLngs.push(allLatLngs[i]);
                    break;
                }}
            }}
            
            if (highlightedPolyline) {{
                map.removeLayer(highlightedPolyline);
            }}
            
            if (segmentLatLngs.length > 0) {{
                highlightedPolyline = L.polyline(segmentLatLngs, {{
                    color: '#3b82f6', // blue-500 (elevation profile blue)
                    weight: 8,
                    opacity: 0.95,
                    lineCap: 'round'
                }}).addTo(map);
                
                const mapContainer = document.getElementById('map-container');
                const isMapVisible = mapContainer && !mapContainer.classList.contains('hidden') && mapContainer.style.display !== 'none';
                if (isMapVisible) {{
                    map.invalidateSize();
                    const paddingVal = (mapContainer && mapContainer.offsetHeight < 400) ? [15, 15] : [40, 40];
                    map.fitBounds(highlightedPolyline.getBounds(), {{ padding: paddingVal, animate: true, duration: 1 }});
                    const marker = markers[index];
                    if (marker) {{
                        setTimeout(() => marker.openPopup(), 600);
                    }}
                }}
            }}
        }}

        function renderApp() {{
            markers.forEach(m => map.removeLayer(m));
            markers = [];
            tableBody.innerHTML = '';
            
            const startParts = timeInput.value.split(':');
            const startMins = parseInt(startParts[0] || 19) * 60 + parseInt(startParts[1] || 0);

            checkpoints.forEach((cp, index) => {{
                const currentMins = startMins + cp.elapsed_minutes;
                const outHour = Math.floor((currentMins % (24 * 60)) / 60);
                const outMin = currentMins % 60;
                const dynamicTime = `${{outHour.toString().padStart(2, '0')}}:${{outMin.toString().padStart(2, '0')}}`;
                
                const tr = document.createElement('tr');
                tr.id = `row-${{index}}`;
                tr.className = 'table-row-transition cursor-pointer hover:bg-slate-700/50 text-[11px] md:text-base';
                
                let actionClass = 'text-slate-300';
                if (cp.action.includes('<span class="lang-pl">PRZEPAK</span><span class="lang-en">DROP BAG</span>') || cp.action.includes('META') || cp.action.includes('FINISZ')) {{
                    actionClass = 'text-lime-400 font-bold';
                }} else if (cp.action.includes('KRYZYS') || cp.action.includes('UPAŁ')) {{
                    actionClass = 'text-amber-400 font-bold';
                }}

                tr.innerHTML = `
                    <td class="p-2 md:p-3 text-cyan-400 font-bold">${{cp.km}}</td>
                    <td class="p-2 md:p-3 text-slate-200 font-bold">${{dynamicTime}}</td>
                    <td class="p-2 md:p-3 text-slate-400 leading-tight">
                        <div class="font-semibold text-slate-300">${{cp.overall_pace}}</div>
                        <div class="text-xs">${{cp.overall_speed}}</div>
                    </td>
                    <td class="p-2 md:p-3 text-slate-400 leading-tight border-r border-slate-700/50">
                        <div class="font-semibold text-emerald-400">${{cp.section_pace}}</div>
                        <div class="text-xs text-emerald-500/70">${{cp.section_speed}}</div>
                    </td>
                    <td class="p-2 md:p-3 leading-tight font-mono border-r border-slate-700/50">
                        <div class="text-sm text-slate-300 font-semibold">${{cp.ele}}</div>
                        <div class="text-[10px] text-slate-500 font-bold">Σ ${{cp.cumulative_ele}}</div>
                    </td>
                    <td class="p-3 ${{actionClass}} whitespace-normal leading-snug min-w-[200px]"><span class="lang-pl">${{cp.action}}</span><span class="lang-en">${{cp.action_en}}</span></td>
                    <td class="p-2 text-center" id="chart-td-${{index}}">
                        <span class="text-xs text-slate-500">${{gpxElevationData && gpxElevationData.length > 0 ? '' : '<span class="lang-pl">Ładowanie...</span><span class="lang-en">Loading...</span>'}}</span>
                    </td>
                `;

                tableBody.appendChild(tr);

                const iconHtml = `<div class="w-6 h-6 bg-slate-900 rounded-full border-2 border-lime-500 text-lime-400 flex items-center justify-center font-bold text-[10px] shadow-lg">${{cp.km}}</div>`;
                const customIcon = L.divIcon({{
                    html: iconHtml,
                    className: '',
                    iconSize: [24, 24],
                    iconAnchor: [12, 12],
                    popupAnchor: [0, -12]
                }});

                const marker = L.marker([cp.lat, cp.lon], {{ icon: customIcon }}).addTo(map);
                
                const popupContent = `
                    <div class="text-[10px] md:text-xs text-slate-800 p-0.5" style="min-width: 120px;">
                        <strong class="text-emerald-700 text-[11px] md:text-sm block mb-1 border-b border-slate-200 pb-0.5">KM ${{cp.km}}</strong>
                        <div class="text-slate-600 mb-1 font-medium">${{dynamicTime}} | Avg: ${{cp.overall_pace}}</div>
                        <div class="text-slate-600 mb-1 font-medium">Sect: ${{cp.section_pace}} | ${{cp.ele}}</div>
                        <div class="bg-slate-100 p-1 md:p-2 rounded text-slate-800 border border-slate-300 font-medium leading-tight"><span class="lang-pl">${{cp.action}}</span><span class="lang-en">${{cp.action_en}}</span></div>
                    </div>
                `;
                marker.bindPopup(popupContent);
                markers.push(marker);

                tr.addEventListener('click', () => {{
                    highlightSection(index);
                    highlightRow(index);
                    const isMapVisible = !mapContainer.classList.contains('hidden') && mapContainer.style.display !== 'none';
                    if (window.innerWidth < 768 && isMapVisible) {{
                        document.getElementById('map-container').scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }});

                marker.on('click', () => {{
                    highlightRow(index);
                    tr.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                    highlightSection(index);
                }});
            }});
            
            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderMiniCharts();
            }}
        }}

        function highlightRow(index) {{
            document.querySelectorAll('tbody tr').forEach(row => row.classList.remove('table-row-highlight'));
            const targetRow = document.getElementById(`row-${{index}}`);
            if (targetRow) targetRow.classList.add('table-row-highlight');
        }}

        function renderMiniCharts() {{
            checkpoints.forEach((cp, index) => {{
                const startKm = index === 0 ? 0 : checkpoints[index-1].km;
                const endKm = cp.km;
                
                const segmentPts = gpxElevationData.filter(pt => pt[0] >= startKm && pt[0] <= endKm);
                const td = document.getElementById(`chart-td-${{index}}`);
                
                if (segmentPts.length < 2) {{
                    td.innerHTML = '<span class="text-xs text-slate-500">N/A</span>';
                    return;
                }}
                
                const minEle = Math.min(...segmentPts.map(pt => pt[1]));
                const maxEle = Math.max(...segmentPts.map(pt => pt[1]));
                const eleRange = Math.max(maxEle - minEle, 1);
                
                const svgW = 80;
                const svgH = 30;
                
                let ptsStr = "";
                segmentPts.forEach(pt => {{
                    const x = ((pt[0] - startKm) / (endKm - startKm)) * svgW;
                    const y = svgH - ((pt[1] - minEle) / eleRange) * svgH;
                    ptsStr += `${{x}},${{y}} `;
                }});
                
                const svgHtml = `
                    <svg width="${{svgW}}" height="${{svgH}}" viewBox="0 0 ${{svgW}} ${{svgH}}" class="cursor-pointer hover:opacity-80 border border-slate-700 bg-slate-800 rounded inline-block" onclick="openDetailedChart(${{index}}, event)">
                        <polyline points="${{ptsStr}}" fill="none" stroke="#22d3ee" stroke-width="1.5" vector-effect="non-scaling-stroke"/>
                        <polygon points="0,${{svgH}} ${{ptsStr}} ${{svgW}},${{svgH}}" fill="rgba(34, 211, 238, 0.2)" />
                    </svg>
                `;
                td.innerHTML = svgHtml;
            }});
        }}

        function openDetailedChart(index, event) {{
            event.stopPropagation();
            
            const cp = checkpoints[index];
            const startKm = index === 0 ? 0 : checkpoints[index-1].km;
            const endKm = cp.km;
            
            const segmentPts = gpxElevationData.filter(pt => pt[0] >= startKm && pt[0] <= endKm);
            
            document.getElementById('chart-modal-title').innerHTML = `<span class="lang-pl">Profil wysokości: KM ${{startKm}} do ${{endKm}}</span><span class="lang-en">Elevation Profile: KM ${{startKm}} to ${{endKm}}</span>`;
            
            const canvas = document.getElementById('detailed-canvas');
            const ctx = canvas.getContext('2d');
            const w = canvas.width;
            const h = canvas.height;
            
            ctx.clearRect(0, 0, w, h);
            ctx.fillStyle = '#f8f9fa';
            ctx.fillRect(0, 0, w, h);
            
            if(segmentPts.length < 2) return;
            
            const minEle = Math.min(...segmentPts.map(pt => pt[1]));
            const maxEle = Math.max(...segmentPts.map(pt => pt[1]));
            const elePad = Math.max((maxEle - minEle) * 0.1, 10);
            const plotMin = Math.max(0, minEle - elePad);
            const plotMax = maxEle + elePad;
            const eleRange = plotMax - plotMin;
            
            ctx.strokeStyle = '#cbd5e1';
            ctx.fillStyle = '#475569';
            ctx.font = '12px sans-serif';
            ctx.lineWidth = 1;
            
            ctx.beginPath();
            for(let i=1; i<5; i++) {{
                let y = h - (h/5)*i;
                ctx.moveTo(40, y);
                ctx.lineTo(w, y);
                ctx.fillText(Math.round(plotMin + (eleRange/5)*i) + 'm', 5, y + 4);
            }}
            ctx.stroke();

            const mappedPts = segmentPts.map(pt => {{
                const x = 40 + ((pt[0] - startKm) / (endKm - startKm)) * (w - 40);
                const y = h - ((pt[1] - plotMin) / eleRange) * h;
                return {{x, y, dist: pt[0], ele: pt[1]}};
            }});

            ctx.lineWidth = 3;
            for(let i = 0; i < mappedPts.length - 1; i++) {{
                const p1 = mappedPts[i];
                const p2 = mappedPts[i+1];
                
                const dDist = (p2.dist - p1.dist) * 1000; 
                const dEle = p2.ele - p1.ele;
                let slope = 0;
                if(dDist > 0) slope = (dEle / dDist) * 100;
                
                if (slope > 15) ctx.strokeStyle = '#dc2626';
                else if (slope > 5) ctx.strokeStyle = '#f97316';
                else if (slope < -15) ctx.strokeStyle = '#16a34a';
                else if (slope < -5) ctx.strokeStyle = '#84cc16';
                else ctx.strokeStyle = '#3b82f6';

                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }}
            
            ctx.globalCompositeOperation = 'destination-over';
            ctx.beginPath();
            ctx.moveTo(mappedPts[0].x, h);
            for(let i = 0; i < mappedPts.length; i++) {{
                ctx.lineTo(mappedPts[i].x, mappedPts[i].y);
            }}
            ctx.lineTo(mappedPts[mappedPts.length-1].x, h);
            ctx.closePath();
            ctx.fillStyle = '#f1f5f9';
            ctx.fill();
            ctx.globalCompositeOperation = 'source-over';
            
            ctx.font = 'bold 13px sans-serif';
            ctx.fillStyle = '#0f172a';
            
            const numChunks = 6;
            for(let c = 0; c < numChunks; c++) {{
                const i1 = Math.floor(mappedPts.length * (c / numChunks));
                const i2 = Math.floor(mappedPts.length * ((c+1) / numChunks)) - 1;
                
                if(i1 >= 0 && i2 > i1 && i2 < mappedPts.length) {{
                    const p1 = mappedPts[i1];
                    const p2 = mappedPts[i2];
                    const dDist = (p2.dist - p1.dist) * 1000;
                    const dEle = p2.ele - p1.ele;
                    
                    if(dDist > 100) {{ 
                        const slope = (dEle / dDist) * 100;
                        if(Math.abs(slope) > 4) {{
                            const midX = (p1.x + p2.x) / 2;
                            const midY = (p1.y + p2.y) / 2 - 20;
                            const txt = slope > 0 ? `+${{slope.toFixed(1)}}%` : `${{slope.toFixed(1)}}%`;
                            
                            ctx.strokeStyle = 'white';
                            ctx.lineWidth = 3;
                            ctx.strokeText(txt, midX - 15, midY);
                            ctx.fillText(txt, midX - 15, midY);
                        }}
                    }}
                }}
            }}
            
            document.getElementById('chart-modal').showModal();
        }}

        function renderOverviewElevationChart() {{
            const canvas = document.getElementById('overview-elevation-canvas');
            if (!canvas) return;
            const ctx = canvas.getContext('2d');
            const rect = canvas.getBoundingClientRect();
            
            // Handle high DPI screens
            const dpr = window.devicePixelRatio || 1;
            canvas.width = rect.width * dpr;
            canvas.height = rect.height * dpr;
            ctx.scale(dpr, dpr);
            
            const w = rect.width;
            const h = rect.height;
            
            ctx.clearRect(0, 0, w, h);
            
            if (!gpxElevationData || gpxElevationData.length < 2) {{
                ctx.fillStyle = '#94a3b8';
                ctx.font = '13px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText(
                    document.documentElement.getAttribute('lang') === 'pl' 
                        ? 'Ładowanie profilu wysokości...' 
                        : 'Loading elevation profile...', 
                    w / 2, 
                    h / 2
                );
                return;
            }}
            
            const paddingLeft = 45;
            const paddingTop = 25;
            const paddingRight = 15;
            const paddingBottom = 25;
            const plotW = w - paddingLeft - paddingRight;
            const plotH = h - paddingTop - paddingBottom;
            
            const minEle = Math.min(...gpxElevationData.map(pt => pt[1]));
            const maxEle = Math.max(...gpxElevationData.map(pt => pt[1]));
            const elePad = Math.max((maxEle - minEle) * 0.1, 10);
            const plotMin = Math.max(0, minEle - elePad);
            const plotMax = maxEle + elePad;
            const eleRange = plotMax - plotMin;
            const maxDist = gpxElevationData[gpxElevationData.length - 1][0];
            
            // 0. Draw Highlighted Section Background Band (if selected)
            if (highlightedSectionIndex !== null) {{
                const cp = checkpoints[highlightedSectionIndex];
                const startKm = highlightedSectionIndex === 0 ? 0 : checkpoints[highlightedSectionIndex - 1].km;
                const endKm = cp.km;
                
                const hsXStart = paddingLeft + (startKm / maxDist) * plotW;
                const hsXEnd = paddingLeft + (endKm / maxDist) * plotW;
                
                // Draw a soft translucent highlight background band
                ctx.fillStyle = 'rgba(34, 211, 238, 0.08)'; // cyan-400 translucent
                ctx.fillRect(hsXStart, paddingTop, hsXEnd - hsXStart, plotH);
                
                // Draw vertical dashed bounds for the highlighted section
                ctx.strokeStyle = 'rgba(34, 211, 238, 0.4)'; // cyan border
                ctx.lineWidth = 1.5;
                ctx.setLineDash([4, 4]);
                ctx.beginPath();
                ctx.moveTo(hsXStart, paddingTop);
                ctx.lineTo(hsXStart, h - paddingBottom);
                ctx.moveTo(hsXEnd, paddingTop);
                ctx.lineTo(hsXEnd, h - paddingBottom);
                ctx.stroke();
                ctx.setLineDash([]);
            }}

            // 1. Draw Grid Lines (Horizontal for elevation)
            ctx.strokeStyle = '#1e293b'; // slate-800
            ctx.fillStyle = '#64748b'; // slate-500
            ctx.font = '10px sans-serif';
            ctx.textAlign = 'right';
            ctx.lineWidth = 1;
            
            const gridLines = 4;
            for (let i = 0; i <= gridLines; i++) {{
                const eleVal = plotMin + (eleRange / gridLines) * i;
                const y = paddingTop + (1 - (eleVal - plotMin) / eleRange) * plotH;
                
                ctx.beginPath();
                ctx.moveTo(paddingLeft, y);
                ctx.lineTo(w - paddingRight, y);
                ctx.stroke();
                
                ctx.fillText(Math.round(eleVal) + 'm', paddingLeft - 8, y + 3);
            }}
            
            // 2. Draw Checkpoint lines and labels
            ctx.textAlign = 'center';
            checkpoints.forEach(cp => {{
                const cpX = paddingLeft + (cp.km / maxDist) * plotW;
                
                // Dotted vertical line
                ctx.strokeStyle = 'rgba(148, 163, 184, 0.15)'; // very light gray
                ctx.beginPath();
                ctx.setLineDash([2, 4]);
                ctx.moveTo(cpX, paddingTop);
                ctx.lineTo(cpX, h - paddingBottom);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // Label at bottom
                ctx.fillStyle = '#64748b';
                ctx.font = '9px sans-serif';
                ctx.fillText(cp.km.toString(), cpX, h - paddingBottom + 12);
            }});
            
            // 3. Map elevation data points
            const mappedPts = gpxElevationData.map(pt => {{
                const x = paddingLeft + (pt[0] / maxDist) * plotW;
                const y = paddingTop + (1 - (pt[1] - plotMin) / eleRange) * plotH;
                return {{ x, y, dist: pt[0], ele: pt[1] }};
            }});
            
            // 4. Fill area under the curve with a gradient
            const grad = ctx.createLinearGradient(0, paddingTop, 0, h - paddingBottom);
            grad.addColorStop(0, 'rgba(59, 130, 246, 0.15)'); // blue gradient
            grad.addColorStop(1, 'rgba(59, 130, 246, 0.0)');
            ctx.fillStyle = grad;
            
            ctx.beginPath();
            ctx.moveTo(paddingLeft, h - paddingBottom);
            mappedPts.forEach(pt => {{
                ctx.lineTo(pt.x, pt.y);
            }});
            ctx.lineTo(paddingLeft + plotW, h - paddingBottom);
            ctx.closePath();
            ctx.fill();
            
            // 4.5. Draw a thick glowing cyan guide line for the highlighted section
            if (highlightedSectionIndex !== null) {{
                const startKm = highlightedSectionIndex === 0 ? 0 : checkpoints[highlightedSectionIndex - 1].km;
                const endKm = checkpoints[highlightedSectionIndex].km;
                
                ctx.strokeStyle = 'rgba(34, 211, 238, 0.35)'; // semi-translucent cyan
                ctx.lineWidth = 7;
                ctx.lineCap = 'round';
                ctx.beginPath();
                
                let first = true;
                for (let i = 0; i < mappedPts.length; i++) {{
                    const pt = mappedPts[i];
                    if (pt.dist >= startKm && pt.dist <= endKm) {{
                        if (first) {{
                            if (i > 0) ctx.moveTo(mappedPts[i-1].x, mappedPts[i-1].y);
                            else ctx.moveTo(pt.x, pt.y);
                            first = false;
                        }}
                        ctx.lineTo(pt.x, pt.y);
                    }}
                }}
                ctx.stroke();
            }}

            // 5. Draw the colored slope segments
            for (let i = 0; i < mappedPts.length - 1; i++) {{
                const p1 = mappedPts[i];
                const p2 = mappedPts[i+1];
                
                const dDist = (p2.dist - p1.dist) * 1000;
                const dEle = p2.ele - p1.ele;
                let slope = 0;
                if (dDist > 0) slope = (dEle / dDist) * 100;
                
                if (slope > 15) ctx.strokeStyle = '#dc2626';      // steep up (red)
                else if (slope > 5) ctx.strokeStyle = '#f97316';   // up (orange)
                else if (slope < -15) ctx.strokeStyle = '#16a34a'; // steep down (green)
                else if (slope < -5) ctx.strokeStyle = '#84cc16';  // down (lime)
                else ctx.strokeStyle = '#3b82f6';                 // flat (blue)
                
                // Determine line width: make highlighted section thicker
                let isHighlighted = false;
                if (highlightedSectionIndex !== null) {{
                    const startKm = highlightedSectionIndex === 0 ? 0 : checkpoints[highlightedSectionIndex - 1].km;
                    const endKm = checkpoints[highlightedSectionIndex].km;
                    if (p1.dist >= startKm && p2.dist <= endKm) {{
                        isHighlighted = true;
                    }}
                }}
                ctx.lineWidth = isHighlighted ? 3.5 : 2;
                
                ctx.beginPath();
                ctx.moveTo(p1.x, p1.y);
                ctx.lineTo(p2.x, p2.y);
                ctx.stroke();
            }}
            
            // 6. Draw dots on the elevation curve for checkpoints
            checkpoints.forEach((cp, idx) => {{
                const closestPt = gpxElevationData.reduce((prev, curr) => {{
                    return Math.abs(curr[0] - cp.km) < Math.abs(prev[0] - cp.km) ? curr : prev;
                }});
                const cpX = paddingLeft + (cp.km / maxDist) * plotW;
                const cpY = paddingTop + (1 - (closestPt[1] - plotMin) / eleRange) * plotH;
                
                ctx.beginPath();
                let isBound = false;
                if (highlightedSectionIndex !== null) {{
                    if (idx === highlightedSectionIndex || idx === highlightedSectionIndex - 1) {{
                        isBound = true;
                    }}
                }}
                
                ctx.arc(cpX, cpY, isBound ? 5.5 : 3.5, 0, 2 * Math.PI);
                ctx.fillStyle = isBound ? '#22d3ee' : '#a3e635'; // cyan-400 or lime-400
                ctx.fill();
                ctx.strokeStyle = '#0f172a'; // slate-900 outline
                ctx.lineWidth = isBound ? 1.5 : 1;
                ctx.stroke();
            }});
            
            // 7. Draw hover effects (tooltip & cursor)
            if (overviewHoveredPoint) {{
                const hoverX = paddingLeft + (overviewHoveredPoint[0] / maxDist) * plotW;
                const hoverY = paddingTop + (1 - (overviewHoveredPoint[1] - plotMin) / eleRange) * plotH;
                
                // Draw vertical line
                ctx.strokeStyle = 'rgba(255, 255, 255, 0.25)';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.setLineDash([3, 3]);
                ctx.moveTo(hoverX, paddingTop);
                ctx.lineTo(hoverX, h - paddingBottom);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // Draw highlight circle
                ctx.beginPath();
                ctx.arc(hoverX, hoverY, 5.5, 0, 2 * Math.PI);
                ctx.fillStyle = '#22d3ee'; // cyan-400
                ctx.fill();
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 1.5;
                ctx.stroke();
                
                // Draw floating tooltip
                const tooltipText = `${{overviewHoveredPoint[0].toFixed(1)}} km | ${{Math.round(overviewHoveredPoint[1])}} m`;
                ctx.font = 'bold 10px sans-serif';
                const textWidth = ctx.measureText(tooltipText).width;
                const boxW = textWidth + 12;
                const boxH = 20;
                let boxX = hoverX - boxW / 2;
                let boxY = hoverY - boxH - 8;
                
                if (boxX < paddingLeft) boxX = paddingLeft;
                if (boxX + boxW > w - paddingRight) boxX = w - paddingRight - boxW;
                if (boxY < paddingTop) boxY = hoverY + 8;
                
                ctx.fillStyle = 'rgba(15, 23, 42, 0.9)';
                ctx.strokeStyle = '#334155';
                ctx.lineWidth = 1;
                ctx.beginPath();
                ctx.rect(boxX, boxY, boxW, boxH);
                ctx.fill();
                ctx.stroke();
                
                ctx.fillStyle = '#ffffff';
                ctx.textAlign = 'center';
                ctx.fillText(tooltipText, boxX + boxW / 2, boxY + 13);
            }}
        }}

        // Register hover listeners for Overview Elevation Chart
        const overviewCanvas = document.getElementById('overview-elevation-canvas');
        if (overviewCanvas) {{
            const handleHover = (e) => {{
                if (!gpxElevationData || gpxElevationData.length < 2) return;
                const rect = overviewCanvas.getBoundingClientRect();
                const clientX = (e.touches && e.touches.length > 0) ? e.touches[0].clientX : e.clientX;
                const x = clientX - rect.left;
                
                const paddingLeft = 45;
                const paddingRight = 15;
                
                if (x >= paddingLeft && x <= rect.width - paddingRight) {{
                    const pct = (x - paddingLeft) / (rect.width - paddingLeft - paddingRight);
                    const maxDist = gpxElevationData[gpxElevationData.length - 1][0];
                    const hoverKm = pct * maxDist;
                    
                    // Find closest point in gpxElevationData
                    let closest = gpxElevationData[0];
                    let minDist = Math.abs(closest[0] - hoverKm);
                    for (let i = 1; i < gpxElevationData.length; i++) {{
                        const d = Math.abs(gpxElevationData[i][0] - hoverKm);
                        if (d < minDist) {{
                            minDist = d;
                            closest = gpxElevationData[i];
                        }}
                    }}
                    overviewHoveredPoint = closest;
                    updateMapHoverPointer(closest[0]);
                }} else {{
                    overviewHoveredPoint = null;
                    clearMapHoverPointer();
                }}
                renderOverviewElevationChart();
            }};
            
            overviewCanvas.addEventListener('mousemove', handleHover);
            overviewCanvas.addEventListener('mouseleave', () => {{
                overviewHoveredPoint = null;
                clearMapHoverPointer();
                renderOverviewElevationChart();
            }});
            
            overviewCanvas.addEventListener('touchstart', handleHover, {{ passive: true }});
            overviewCanvas.addEventListener('touchmove', handleHover, {{ passive: true }});
            overviewCanvas.addEventListener('touchend', () => {{
                overviewHoveredPoint = null;
                clearMapHoverPointer();
                renderOverviewElevationChart();
            }});
        }}

        window.addEventListener('resize', () => {{
            if (gpxElevationData && gpxElevationData.length > 0) {{
                renderOverviewElevationChart();
            }}
        }});
        
        renderApp();

        // Service Worker registration for PWA installation
        if ('serviceWorker' in navigator) {{
            window.addEventListener('load', () => {{
                navigator.serviceWorker.register('./sw.js').then(registration => {{
                    console.log('SW registered: ', registration);
                }}).catch(registrationError => {{
                    console.log('SW registration failed: ', registrationError);
                }});
            }});

            // Force refresh when new service worker takes control
            let refreshing = false;
            navigator.serviceWorker.addEventListener('controllerchange', () => {{
                if (!refreshing) {{
                    refreshing = true;
                    window.location.reload();
                }}
            }});
        }}
    </script>
</body>
</html>'''

print('Writing index.html...')
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

print('Writing Ultra100_standalone.html...')
with open('Ultra100_standalone.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

manifest_data = {
    "name": "Wyrypa 100km",
    "short_name": "Wyrypa 100k",
    "start_url": "./index.html",
    "display": "standalone",
    "background_color": "#0f172a",
    "theme_color": "#0f172a",
    "description": "Offline tracker for 100km Ultra-Trekking",
    "icons": [
        {
            "src": "./icon-192.svg",
            "sizes": "192x192",
            "type": "image/svg+xml",
            "purpose": "any maskable"
        },
        {
            "src": "./icon-512.svg",
            "sizes": "512x512",
            "type": "image/svg+xml",
            "purpose": "any maskable"
        }
    ]
}

with open('manifest.json', 'w', encoding='utf-8') as f:
    json.dump(manifest_data, f, indent=4)

sw_content = f'''const CACHE_NAME = '{app_version}';
const ASSETS = [
    './',
    './index.html',
    './manifest.json',
    './icon-192.svg',
    './icon-512.svg',
    './wyrypa-100km.gpx',
    'https://cdn.tailwindcss.com',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.7.0/gpx.min.js'
];

self.addEventListener('install', event => {{
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {{
            return cache.addAll(ASSETS);
        }})
    );
}});

self.addEventListener('fetch', event => {{
    if (event.request.method !== 'GET') return;
    
    if (event.request.url.includes('cartocdn.com')) {{
        event.respondWith(
            caches.match(event.request).then(response => {{
                return response || fetch(event.request).then(fetchResponse => {{
                    return caches.open('ultra-tiles-v1').then(cache => {{
                        cache.put(event.request, fetchResponse.clone());
                        return fetchResponse;
                    }});
                }});
            }})
        );
        return;
    }}

    event.respondWith(
        caches.match(event.request).then(response => {{
            return response || fetch(event.request);
        }})
    );
}});

self.addEventListener('activate', event => {{
    event.waitUntil(
        caches.keys().then(keys => {{
            return Promise.all(keys
                .filter(key => key !== CACHE_NAME && key !== 'ultra-tiles-v1')
                .map(key => caches.delete(key))
            );
        }}).then(() => self.clients.claim())
    );
}});
'''

print('Writing sw.js...')
with open('sw.js', 'w', encoding='utf-8') as f:
    f.write(sw_content)

print('Successfully generated index.html, Ultra100_standalone.html, manifest.json, and sw.js.')
