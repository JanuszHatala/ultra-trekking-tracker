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
with open('wyrypa75km.gpx', 'r', encoding='utf-8') as f:
    gpx_content = f.read()

# Escape backticks, dollars, slashes, and closing scripts
gpx_content_escaped = gpx_content.replace('\\', '\\\\').replace('`', '\\`').replace('$', '\\$').replace('</script>', '<\\/script>')

checkpoints_json = '''[
  {
    "km": 5,
    "lat": 49.777544,
    "lon": 19.113625,
    "time": "20:20",
    "pace": "16:00",
    "ele": "+500 m",
    "action": "Wypij 1. bidon izotoniku, baton.",
    "action_en": "Drink 1st isotonic flask, energy bar.",
    "bounds": [[49.776947, 19.096194], [49.795845, 19.128895]]
  },
  {
    "km": 10,
    "lat": 49.784075,
    "lon": 19.104631,
    "time": "21:28",
    "pace": "13:36",
    "ele": "+176 m",
    "action": "Kapsułki z solą / słone jedzenie.",
    "action_en": "Take salt capsules / salty food.",
    "bounds": [[49.777253, 19.095909], [49.795845, 19.113625]]
  },
  {
    "km": 15,
    "lat": 49.775386,
    "lon": 19.105436,
    "time": "22:43",
    "pace": "15:00",
    "ele": "+405 m",
    "action": "Zjedz kanapkę.",
    "action_en": "Eat a sandwich.",
    "bounds": [[49.774707, 19.10206], [49.784075, 19.128324]]
  },
  {
    "km": 20,
    "lat": 49.77777,
    "lon": 19.122489,
    "time": "00:01",
    "pace": "15:36",
    "ele": "+482 m",
    "action": "Opróżnij bidon.",
    "action_en": "Empty flask.",
    "bounds": [[49.77403, 19.086939], [49.77777, 19.122489]]
  },
  {
    "km": 25,
    "lat": 49.76596,
    "lon": 19.108642,
    "time": "01:13",
    "pace": "14:24",
    "ele": "+159 m",
    "action": "POSTÓJ 5 MIN (Stopy). Zmiana skarpet.",
    "action_en": "BREAK 5 MIN (Feet). Change socks.",
    "bounds": [[49.760112, 19.102835], [49.780002, 19.129878]]
  },
  {
    "km": 30,
    "lat": 49.765973,
    "lon": 19.13909,
    "time": "02:33",
    "pace": "16:00",
    "ele": "+475 m",
    "action": "Opróżnij bidon, baton.",
    "action_en": "Empty flask, energy bar.",
    "bounds": [[49.76596, 19.108642], [49.780002, 19.140513]]
  },
  {
    "km": 35,
    "lat": 49.756541,
    "lon": 19.12972,
    "time": "03:41",
    "pace": "13:36",
    "ele": "+137 m",
    "action": "Kapsułki z solą, żel.",
    "action_en": "Salt capsules, energy gel.",
    "bounds": [[49.753813, 19.118867], [49.765973, 19.143013]]
  },
  {
    "km": 40,
    "lat": 49.769759,
    "lon": 19.142486,
    "time": "05:03",
    "pace": "16:24",
    "ele": "+427 m",
    "action": "Napój z kofeiną (kryzys nocny).",
    "action_en": "Caffeinated beverage (night crisis).",
    "bounds": [[49.756541, 19.12972], [49.776784, 19.143013]]
  },
  {
    "km": 45,
    "lat": 49.767715,
    "lon": 19.160125,
    "time": "06:15",
    "pace": "14:24",
    "ele": "+247 m",
    "action": "Zjedz kanapkę. Opróżnij bidon.",
    "action_en": "Eat sandwich. Empty flask.",
    "bounds": [[49.763475, 19.142486], [49.769759, 19.182465]]
  },
  {
    "km": 50,
    "lat": 49.77438,
    "lon": 19.139428,
    "time": "07:33",
    "pace": "15:36",
    "ele": "+98 m",
    "action": "POSTÓJ 10 MIN. Zmiana skarpet.",
    "action_en": "BREAK 10 MIN. Change socks.",
    "bounds": [[49.766767, 19.127321], [49.783785, 19.160125]]
  },
  {
    "km": 55,
    "lat": 49.775302,
    "lon": 19.140957,
    "time": "08:48",
    "pace": "15:00",
    "ele": "+292 m",
    "action": "Kofeina (zmęczenie poranne).",
    "action_en": "Caffeine (morning fatigue).",
    "bounds": [[49.77438, 19.138081], [49.785056, 19.161343]]
  },
  {
    "km": 60,
    "lat": 49.79874,
    "lon": 19.131337,
    "time": "10:02",
    "pace": "14:48",
    "ele": "+253 m",
    "action": "Kapsułki z solą.",
    "action_en": "Salt capsules.",
    "bounds": [[49.773642, 19.127321], [49.79874, 19.140957]]
  },
  {
    "km": 65,
    "lat": 49.814493,
    "lon": 19.113824,
    "time": "11:13",
    "pace": "14:12",
    "ele": "+207 m",
    "action": "Żel energetyczny. Koniec jedzenia stałego.",
    "action_en": "Energy gel. End of solid food.",
    "bounds": [[49.79874, 19.113362], [49.821366, 19.131963]]
  },
  {
    "km": 70,
    "lat": 49.782609,
    "lon": 19.12814,
    "time": "12:38",
    "pace": "17:00",
    "ele": "+510 m",
    "action": "Opróżnij bidon. Ostatnie strome podejście.",
    "action_en": "Empty flask. Last steep ascent.",
    "bounds": [[49.782609, 19.11375], [49.814493, 19.131963]]
  },
  {
    "km": 74,
    "lat": 49.795845,
    "lon": 19.096194,
    "time": "13:30",
    "pace": "13:00",
    "ele": "+49 m",
    "action": "META TESTU.",
    "action_en": "TEST FINISH.",
    "bounds": [[49.782609, 19.096194], [49.795845, 19.12814]]
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
    <link rel="manifest" href="manifest_75.json">
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🥾</text></svg>">
    <link rel="apple-touch-icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🥾</text></svg>">
    <title>75km Ultra-Trekking Tracker (Offline)</title>
    
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

        /* GPS Ring Pulse animation */
        @keyframes gps-ring-pulse {{
            0% {{
                fill-opacity: 0.12;
                stroke-opacity: 0.45;
            }}
            50% {{
                fill-opacity: 0.25;
                stroke-opacity: 0.75;
            }}
            100% {{
                fill-opacity: 0.12;
                stroke-opacity: 0.45;
            }}
        }}
        .gps-ring-pulse {{
            animation: gps-ring-pulse 2s infinite ease-in-out;
        }}

        /* GPS Toast Notification */
        .gps-toast {{
            position: absolute;
            bottom: 16px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 2000;
            background-color: rgba(15, 23, 42, 0.95);
            border: 1px solid #334155;
            color: #cbd5e1;
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 500;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.5);
            display: flex;
            align-items: center;
            gap: 8px;
            pointer-events: none;
            transition: opacity 0.3s ease-in-out;
            white-space: nowrap;
        }}

        /* Leaflet GPS Custom Buttons */
        .leaflet-control-gps-active {{
            background-color: #ef4444 !important; /* red-500 */
            border-color: #fca5a5 !important;
            box-shadow: 0 0 12px #ef4444 !important;
            animation: gps-btn-glow 1.5s infinite alternate ease-in-out !important;
        }}
        .leaflet-control-gps-active svg {{
            stroke: #ffffff !important;
        }}
        .leaflet-control-gps-active svg circle {{
            fill: #ffffff !important;
        }}
        @keyframes gps-btn-glow {{
            0% {{
                box-shadow: 0 0 4px #ef4444;
            }}
            100% {{
                box-shadow: 0 0 16px #ef4444, 0 0 4px #ef4444 inset;
            }}
        }}
    </style>
</head>
<body class="bg-slate-900 text-slate-200 font-sans antialiased h-[100dvh] w-full overflow-hidden flex flex-col md:flex-row">

    <!-- Map Section -->
    <div id="map-container" class="w-full h-[33vh] md:h-screen md:w-[45%] flex-shrink-0 z-0 relative transition-all duration-300">
        <div id="map" class="w-full h-full bg-[#f8f9fa]"></div>
        <div id="gps-toast" class="gps-toast opacity-0"></div>
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
                    <h1 class="text-xl sm:text-2xl md:text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-lime-400 to-cyan-400 mb-0.5">Wyrypa 75km Ultra-Trekking</h1>
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
                
                
            </div>
             

        </div>


        <!-- Tab Content: Overview -->
        <div id="tab-overview" class="tab-content p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-slate-300">
            <div class="bg-slate-800/50 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl mb-3 md:mb-4">
                
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">Ustawienia</span><span class="lang-en">Settings</span></h2>
                <div class="flex flex-row flex-wrap gap-2 md:gap-3 items-center mb-4 md:mb-6">
                    <!-- Start Time Input -->
                    <div class="flex items-center space-x-2 bg-slate-800 p-1.5 md:p-2 px-2 md:px-3 rounded border border-slate-600 shadow-sm h-[28px] md:h-[38px]">
                        <label for="start-time-input" class="text-xs md:text-sm font-bold text-slate-300 whitespace-nowrap"><span class="lang-pl">Godzina Startu:</span><span class="lang-en">Start Time:</span></label>
                        <input type="time" id="start-time-input" class="bg-slate-900 border border-slate-600 text-lime-400 font-bold rounded px-1.5 md:px-2 py-0.5 text-xs md:text-sm text-center outline-none focus:border-lime-400 cursor-pointer h-full">
                    </div>

                    <!-- GPS Polling Interval -->
                    <div class="flex items-center space-x-2 bg-slate-800 p-1.5 md:p-2 px-2 md:px-3 rounded border border-slate-600 shadow-sm h-[28px] md:h-[38px]">
                        <label for="gps-poll-interval" class="text-xs md:text-sm font-bold text-slate-300 whitespace-nowrap">
                            <span class="lang-pl">Interwał GPS:</span>
                            <span class="lang-en">GPS Interval:</span>
                        </label>
                        <select id="gps-poll-interval" class="bg-slate-900 border border-slate-600 text-lime-400 font-bold rounded px-1 md:px-2 py-0 text-xs md:text-sm outline-none focus:border-lime-400 cursor-pointer h-[20px] md:h-[26px] align-middle">
                            <option value="0">Wyłączone</option>
                            <option value="15000">15 s</option>
                            <option value="30000" selected>30 s</option>
                            <option value="60000">1 min</option>
                            <option value="120000">2 min</option>
                        </select>
                    </div>

                    <!-- Map Pre-Cache Button -->
                    <div class="flex bg-slate-800 rounded border border-slate-600 overflow-hidden shadow-sm h-[28px] md:h-[38px] items-center">
                        <button id="btn-download-map" class="px-3 md:px-4 text-xs md:text-sm font-bold bg-slate-700 text-slate-300 hover:text-white transition-colors h-full cursor-pointer">
                            <span class="lang-pl">📥 Pobierz mapę offline</span>
                            <span class="lang-en">📥 Download offline map</span>
                        </button>
                        <div id="download-progress-bar" class="hidden h-full bg-slate-900 border-l border-slate-600 px-3 flex items-center text-[10px] md:text-xs font-mono text-lime-400">
                            0%
                        </div>
                    </div>

                    <!-- Language Toggle -->
                    <div class="flex bg-slate-800 rounded border border-slate-600 overflow-hidden shadow-sm h-[28px] md:h-[38px]">
                        <button id="btn-lang-pl" class="px-3 md:px-4 text-xs md:text-sm font-bold bg-lime-500 text-slate-900 transition-colors">PL</button>
                        <button id="btn-lang-en" class="px-3 md:px-4 text-xs md:text-sm font-bold bg-slate-700 text-slate-400 hover:text-white transition-colors">EN</button>
                    </div>
                </div>

                <h2 class="text-base md:text-lg font-bold text-cyan-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">Parametry Wyzwania</span><span class="lang-en">Challenge Parameters</span></h2>
                
                <div class="flex flex-col sm:flex-row gap-2 md:gap-4 flex-wrap">
                    <span class="bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1.5 rounded border border-slate-700 shadow-sm flex-1 text-center font-semibold text-xs md:text-sm whitespace-nowrap">🏃‍♂️ 87 kg (75+12)</span>
                    <span class="bg-slate-800 text-red-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-red-900/50 shadow-sm flex-1 text-center font-semibold text-xs md:text-sm whitespace-nowrap">❤️ Target: 125-140 bpm</span>
                    <span class="bg-lime-900/30 text-lime-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-lime-700/50 shadow-sm flex-1 text-center font-semibold text-xs md:text-sm whitespace-nowrap">⏱️ <span class="lang-pl">Cel: ~18h 30m</span><span class="lang-en">Goal: ~18h 30m</span></span>
                </div>

            </div>

            <!-- GPS Status Card -->
            <div id="gps-status-card" class="hidden bg-slate-800/50 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl mb-3 md:mb-4">
                <div class="flex justify-between items-center mb-2 border-b border-slate-700 pb-1 md:pb-2">
                    <h2 class="text-base md:text-lg font-bold text-cyan-400 flex items-center gap-1.5">
                        <span>📍</span>
                        <span class="lang-pl">Moja Pozycja</span>
                        <span class="lang-en">My Position</span>
                    </h2>
                    <div class="flex items-center gap-2">
                        <span id="gps-accuracy-badge" class="text-[10px] md:text-xs font-bold px-2 py-0.5 rounded bg-slate-900 text-slate-400">
                            GPS: --
                        </span>
                        <button id="btn-reset-gps" class="text-[10px] md:text-xs font-bold px-2 py-0.5 rounded bg-slate-900/80 hover:bg-slate-900 border border-slate-700 hover:border-cyan-500/50 text-slate-400 hover:text-cyan-400 transition-all cursor-pointer">
                            <span class="lang-pl">Resetuj</span>
                            <span class="lang-en">Reset</span>
                        </button>
                    </div>
                </div>
                
                <!-- Active Content -->
                <div id="gps-card-active" class="space-y-3">
                    <!-- Progress Bar -->
                    <div>
                        <div class="flex justify-between text-xs md:text-sm font-semibold mb-1">
                            <span class="text-slate-300">
                                <span class="lang-pl">Dystans:</span>
                                <span class="lang-en">Distance:</span>
                                <span id="gps-progress-km" class="text-lime-400 font-bold ml-1">-- / 100 km</span>
                            </span>
                            <span id="gps-progress-pct" class="text-lime-400 font-bold">--%</span>
                        </div>
                        <div class="w-full bg-slate-950 rounded-full h-2 overflow-hidden border border-slate-800">
                            <div id="gps-progress-fill" class="bg-gradient-to-r from-lime-500 to-cyan-500 h-full transition-all duration-500" style="width: 0%"></div>
                        </div>
                    </div>
                    
                    <!-- Section Info and Schedule -->
                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 text-xs md:text-sm">
                        <div class="bg-slate-900/60 p-2 rounded border border-slate-800/50">
                            <div class="text-slate-500 font-semibold uppercase tracking-wider text-[9px] md:text-[10px]"><span class="lang-pl">Aktualny Odcinek</span><span class="lang-en">Current Section</span></div>
                            <div id="gps-section-name" class="font-bold text-slate-200 mt-0.5">--</div>
                        </div>
                        <div class="bg-slate-900/60 p-2 rounded border border-slate-800/50">
                            <div class="text-slate-500 font-semibold uppercase tracking-wider text-[9px] md:text-[10px]"><span class="lang-pl">Tempo vs Plan</span><span class="lang-en">Pace vs Plan</span></div>
                            <div class="flex items-center gap-1.5 mt-0.5">
                                <span id="gps-schedule-delta" class="font-bold text-slate-300">--</span>
                            </div>
                        </div>
                    </div>

                    <!-- Finish ETA -->
                    <div class="bg-slate-900/60 p-2.5 rounded border border-slate-800/50 flex justify-between items-center text-xs md:text-sm font-semibold">
                        <span class="text-slate-300">
                            <span class="lang-pl">Szacowana meta (ETA):</span>
                            <span class="lang-en">Estimated Finish (ETA):</span>
                        </span>
                        <span id="gps-finish-eta" class="font-mono font-bold text-cyan-400 text-sm md:text-base">--:--</span>
                    </div>

                    <!-- Warnings zone -->
                    <div id="gps-card-warnings" class="space-y-1.5">
                        <!-- Off Route -->
                        <div id="warn-off-route" class="hidden bg-yellow-500/10 border border-yellow-500/30 text-yellow-500 px-2 py-1.5 rounded text-xs flex items-center gap-1.5">
                            <span>⚠️</span>
                            <span>
                                <span class="lang-pl">Poza trasą (>200m) - wskazania mogą być niedokładne.</span>
                                <span class="lang-en">Off route (>200m) - values may be approximate.</span>
                            </span>
                        </div>
                        <!-- Poor Signal -->
                        <div id="warn-poor-signal" class="hidden bg-red-500/10 border border-red-500/30 text-red-400 px-2 py-1.5 rounded text-xs flex items-center gap-1.5">
                            <span>⚠️</span>
                            <span>
                                <span class="lang-pl">Słaby sygnał GPS - pozycja jest przybliżona.</span>
                                <span class="lang-en">Poor GPS signal - position is approximate.</span>
                            </span>
                        </div>
                    </div>
                </div>
                
                <!-- Status / Error Text -->
                <div id="gps-card-message" class="hidden text-xs md:text-sm text-slate-400 py-1 italic text-center">
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
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">3. TAKTYKA I ZASADY RUCHU</span><span class="lang-en">3. TACTICS & MOVEMENT</span></h2>
                <ul class="space-y-4">
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Płaskie i łagodne podejścia:</strong> Miarowy, stabilny marsz. Unikaj biegu.</span><span class="lang-en">Flat and gentle ascents:</strong> Maintain a steady, rhythmic walk. Avoid running.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Strome podejścia:</strong> Krótki krok, mocne wsparcie kijami. Tętno do 140 bpm.</span><span class="lang-en">Steep ascents:</strong> Shorter steps, lean heavily on poles. HR limit: 140 bpm.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Zbiegi:</strong> Szybki marsz, ale bez uderzeń piętą. Ląduj na śródstopiu. Kije absorbują impakt.</span><span class="lang-en">Downhills:</strong> Fast walk, no heel strikes. Land on midfoot. Poles absorb impact.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><span class="lang-pl"><strong class="text-white">Nawadnianie i Żywienie:</strong> 1 bidon (500ml) na godzinę marszu. Cel: 60-80g węgli na godzinę.</span><span class="lang-en">Hydration and Nutrition:</strong> 1 flask (500ml) per hour. Target: 60-80g carbs/hour.</span></div></li>
                </ul>
            </div>
        </div>

        <!-- Tab: Inwentarz -->
        <div id="tab-inwentarz" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl mb-4">
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
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Napoje z kofeiną</span><span class="lang-en">Caffeinated drinks</span></div></li>
                            <li class="flex items-start"><span class="text-emerald-500 mr-2 mt-0.5">▶</span><div><span class="lang-pl">Filtr do wody / Tabletki uzdatniające</span><span class="lang-en">Water filtration system / Purification tablets</span></div></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>

        <!-- Tab: Harmonogram -->
        <div id="tab-harmonogram" class="tab-content hidden p-3 md:p-6 pt-2 flex-1 overflow-y-auto text-xs md:text-sm text-slate-300">
            <div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl mb-4">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">1. HARMONOGRAM LOGISTYCZNY DNIA</span><span class="lang-en">1. LOGISTICS SCHEDULE</span></h2>
                <ul class="space-y-4">
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">06:00</strong> - <span class="lang-pl">Pobudka, nawodnienie i lekkie śniadanie.</span><span class="lang-en">Wake up, hydration, and light breakfast.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">07:00 - 15:00</strong> - <span class="lang-pl">Dzień pracy. Ciągłe nawadnianie organizmu.</span><span class="lang-en">Work day. Continuous hydration.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">15:00 - 16:30</strong> - <span class="lang-pl">Drzemka / odpoczynek.</span><span class="lang-en">Short nap / rest.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">17:00</strong> - <span class="lang-pl">Obiad (węglowodany, mało błonnika).</span><span class="lang-en">Dinner - high carb, low fiber.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">18:00</strong> - <span class="lang-pl">Kontrola ekwipunku, dojazd na start.</span><span class="lang-en">Gear audit and travel.</span></div></li>
                    <li class="flex items-start"><span class="text-amber-500 mr-3 mt-1">▶</span><div><strong class="text-amber-400">19:00 START TESTU</strong> - <span class="lang-pl">Wejście w tryb marszu.</span><span class="lang-en">Enter walking mode.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">~03:45 (Dzień 2)</strong> - <span class="lang-pl">Kryzys nocny ("Godzina wilka") w okolicach 35. kilometra. Czas na kofeinę.</span><span class="lang-en">Night crisis around 35th km. Caffeine shot.</span></div></li>
                    <li class="flex items-start"><span class="text-emerald-500 mr-3 mt-1">▶</span><div><strong class="text-white">~05:00 (Dzień 2)</strong> - <span class="lang-pl">Wschód słońca. Ocieplenie.</span><span class="lang-en">Sunrise.</span></div></li>
                    <li class="flex items-start"><span class="text-amber-500 mr-3 mt-1">▶</span><div><strong class="text-amber-400">~13:30 (Dzień 2) META TESTU</strong> - <span class="lang-pl">Czas łączny ~18h 30m.</span><span class="lang-en">Expected Finish (~18h 30m).</span></div></li>
                </ul>
            </div>
            
            <div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">2. HARMONOGRAM OGÓLNY I POSTOJE</span><span class="lang-en">2. GENERAL SCHEDULE & STOPS</span></h2>
                <p class="text-sm text-slate-400 italic mb-6"><span class="lang-pl">Wyrypa w pełnej autonomii. Brak przepaku i ciepłych posiłków. Przerwy zredukowane do minimum potrzebnego na regenerację stóp z 12 kg balastem.</span><span class="lang-en">Full autonomy. No drop bags or warm meals. Breaks reduced to the minimum needed for foot recovery under a 12kg load.</span></p>
                
                <div class="relative border-l-2 border-slate-600 ml-3 pl-6 space-y-6">
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-slate-500 w-4 h-4 rounded-full mt-1.5"></span>
                        <h4 class="font-bold text-white text-lg">0 - 25 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Marsz ciągły</span><span class="lang-en">Continuous march</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Wejście w noc. Rygorystyczne nawadnianie (1 bidon/h). Zbiegi z prędkością 4.3 - 4.4 km/h, bez forsowania kolan.</span><span class="lang-en">Entering the night. Strict hydration (1 flask/h). Downhills at 4.3 - 4.4 km/h, without forcing knees.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">25 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 5 min (Zegarek ok. 01:13)</span><span class="lang-en">5 min break (Watch approx. 01:13)</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl"><strong>Konserwacja stóp.</strong> Ściągnięcie butów, osuszenie, nałożenie wazeliny, zmiana skarpet na suche. Zjedzenie stałego pokarmu.</span><span class="lang-en"><strong>Foot maintenance.</strong> Take off shoes, dry feet, apply vaseline, change to dry socks. Eat solid food.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-slate-500 w-4 h-4 rounded-full mt-1.5"></span>
                        <h4 class="font-bold text-white text-lg">25 - 50 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Nocny marsz</span><span class="lang-en">Night march</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Obejmuje najtrudniejszą fazę senności w okolicach 35-40 km. Wymagany strzał z kofeiny i utrzymanie tempa na zbiegach.</span><span class="lang-en">Includes the toughest sleep phase around 35-40 km. Caffeine shot required and maintaining pace on downhills.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">50 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 10 min (Zegarek ok. 07:33)</span><span class="lang-en">10 min break (Watch approx. 07:33)</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl"><strong>Druga konserwacja stóp.</strong> Przewietrzenie, inspekcja otarć, ponowna wazelina. Zjedzenie solidnego posiłku po wschodzie słońca.</span><span class="lang-en"><strong>Second foot maintenance.</strong> Air out, inspect for chafing, reapply vaseline. Eat a solid meal after sunrise.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-red-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(239,68,68,0.5)]"></span>
                        <h4 class="font-bold text-red-400 text-lg">50 - 74 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Faza końcowa</span><span class="lang-en">Final phase</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Dług mięśniowy przekracza 3000m UP. Przejście z pokarmów stałych na żele i Hyper-Mix w celu odciążenia żołądka.</span><span class="lang-en">Muscle debt exceeds 3000m UP. Transition from solid foods to gels and Hyper-Mix to relieve the stomach.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-[34px] bg-slate-900 border-2 border-lime-500 w-5 h-5 rounded-full mt-1 flex items-center justify-center shadow-[0_0_12px_rgba(132,204,22,0.6)]"><span class="bg-lime-500 w-2 h-2 rounded-full"></span></span>
                        <h4 class="font-bold text-lime-400 text-xl">74 km <span class="text-sm text-lime-400 font-normal ml-2 bg-lime-900/30 px-2 py-0.5 rounded border border-lime-700"><span class="lang-pl">META</span><span class="lang-en">FINISH</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Zatrzymanie stopera. Odpoczynek.</span><span class="lang-en">Stop the timer. Rest.</span></p>
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

        // GPS State globals
        let gpsMarker = null;
        let gpsAccuracyCircle = null;
        let gpsTrackingInterval = null;
        let isTracking = false;
        let gpsHintShown = false;
        let gpsCurrentKm = null;
        let gpsCurrentAccuracy = null;
        let gpsLastMatchedIndex = null;
        try {{
            const savedIdx = localStorage.getItem('gps_last_matched_index');
            if (savedIdx !== null) {{
                gpsLastMatchedIndex = parseInt(savedIdx, 10);
            }}
        }} catch (e) {{}}

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

        // --- GPS AND OFFLINE CACHING FUNCTIONS ---
        function showToast(msgHtml) {{
            const toast = document.getElementById('gps-toast');
            if (!toast) return;
            toast.innerHTML = msgHtml;
            toast.style.opacity = '1';
            setTimeout(() => {{
                toast.style.opacity = '0';
            }}, 5000);
        }}

        function checkAndShowIosHint() {{
            try {{
                const shown = localStorage.getItem('ultra_gps_hint_shown');
                if (!shown) {{
                    const isIos = /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
                    if (isIos) {{
                        showToast('<span class="lang-pl">Przeglądarka zapyta o zgodę na lokalizację. Kliknij <strong>Zezwól</strong>.</span><span class="lang-en">Your browser will ask for location permission. Tap <strong>Allow</strong>.</span>');
                    }} else {{
                        showToast('<span class="lang-pl">Przeglądarka zapyta o zgodę na lokalizację.</span><span class="lang-en">Your browser will ask for location permission.</span>');
                    }}
                    localStorage.setItem('ultra_gps_hint_shown', '1');
                }}
            }} catch (e) {{}}
        }}

        function updateGpsStatusPanel(lat, lon, accuracy, minDistanceMetres) {{
            const card = document.getElementById('gps-status-card');
            const activeZone = document.getElementById('gps-card-active');
            const msgZone = document.getElementById('gps-card-message');
            
            card.classList.remove('hidden');
            activeZone.classList.remove('hidden');
            msgZone.classList.add('hidden');
            
            const accuracyBadge = document.getElementById('gps-accuracy-badge');
            accuracyBadge.innerHTML = `GPS: ±${{Math.round(accuracy)}} m`;
            
            accuracyBadge.className = "text-[10px] md:text-xs font-bold px-2 py-0.5 rounded ";
            if (accuracy <= 50) {{
                accuracyBadge.className += "bg-blue-500/20 text-blue-400 border border-blue-500/30";
            }} else if (accuracy <= 100) {{
                accuracyBadge.className += "bg-orange-500/20 text-orange-400 border border-orange-500/30";
            }} else {{
                accuracyBadge.className += "bg-red-500/20 text-red-400 border border-red-500/30";
            }}
            
            const warnOffRoute = document.getElementById('warn-off-route');
            const isOffRoute = minDistanceMetres > 200;
            if (isOffRoute) {{
                warnOffRoute.classList.remove('hidden');
            }} else {{
                warnOffRoute.classList.add('hidden');
            }}
            
            const warnPoorSignal = document.getElementById('warn-poor-signal');
            if (accuracy > 100) {{
                warnPoorSignal.classList.remove('hidden');
            }} else {{
                warnPoorSignal.classList.add('hidden');
            }}
            
            let currentKm = 0;
            const gpsLatLng = L.latLng(lat, lon);
            if (gpxTrackPoints && gpxTrackPoints.length > 0) {{
                let closestPt = gpxTrackPoints[0];
                let minDist = gpsLatLng.distanceTo(closestPt.latlng);
                for (let i = 1; i < gpxTrackPoints.length; i++) {{
                    const d = gpsLatLng.distanceTo(gpxTrackPoints[i].latlng);
                    if (d < minDist) {{
                        minDist = d;
                        closestPt = gpxTrackPoints[i];
                    }}
                }}
                currentKm = closestPt.km;
            }}
            
            const kmText = document.getElementById('gps-progress-km');
            kmText.innerHTML = `${{currentKm.toFixed(1)}} / 100 km`;
            
            const pct = Math.min(Math.max((currentKm / 100) * 100, 0), 100);
            document.getElementById('gps-progress-pct').innerHTML = `${{Math.round(pct)}}%`;
            document.getElementById('gps-progress-fill').style.width = `${{pct}}%`;
            
            let sectionName = "";
            let prevCpKm = 0;
            for (let i = 0; i < checkpoints.length; i++) {{
                if (currentKm <= checkpoints[i].km) {{
                    const secNum = i + 1;
                    const lang = document.documentElement.getAttribute('lang') || 'pl';
                    if (lang === 'pl') {{
                        sectionName = `Odcinek ${{secNum}} · KM ${{prevCpKm}} → KM ${{checkpoints[i].km}}`;
                    }} else {{
                        sectionName = `Section ${{secNum}} · KM ${{prevCpKm}} → KM ${{checkpoints[i].km}}`;
                    }}
                    break;
                }}
                prevCpKm = checkpoints[i].km;
            }}
            if (!sectionName) {{
                const lang = document.documentElement.getAttribute('lang') || 'pl';
                sectionName = lang === 'pl' ? "META" : "FINISH";
            }}
            document.getElementById('gps-section-name').innerHTML = sectionName;
            
            const timeInput = document.getElementById('start-time-input');
            const startParts = timeInput.value.split(':');
            const now = new Date();
            let startDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), parseInt(startParts[0] || 19), parseInt(startParts[1] || 0), 0);
            let diffMs = now.getTime() - startDate.getTime();
            if (diffMs < -12 * 60 * 60 * 1000) {{
                startDate.setDate(startDate.getDate() - 1);
                diffMs = now.getTime() - startDate.getTime();
            }}
            const actualElapsedMinutes = diffMs / 60000;
            
            let expectedElapsed = 0;
            if (currentKm <= 0) {{
                expectedElapsed = 0;
            }} else if (currentKm >= checkpoints[checkpoints.length - 1].km) {{
                expectedElapsed = checkpoints[checkpoints.length - 1].elapsed_minutes;
            }} else {{
                let prevCp = {{ km: 0, elapsed_minutes: 0 }};
                let nextCp = checkpoints[0];
                for (let i = 0; i < checkpoints.length; i++) {{
                    if (checkpoints[i].km >= currentKm) {{
                        nextCp = checkpoints[i];
                        if (i > 0) {{
                            prevCp = checkpoints[i - 1];
                        }}
                        break;
                    }}
                }}
                const kmRatio = (currentKm - prevCp.km) / (nextCp.km - prevCp.km);
                expectedElapsed = prevCp.elapsed_minutes + kmRatio * (nextCp.elapsed_minutes - prevCp.elapsed_minutes);
            }}
            
            const delta = actualElapsedMinutes - expectedElapsed;
            const absDelta = Math.round(Math.abs(delta));
            const deltaSpan = document.getElementById('gps-schedule-delta');
            
            const lang = document.documentElement.getAttribute('lang') || 'pl';
            if (Math.abs(delta) <= 5) {{
                deltaSpan.className = "font-bold text-slate-300";
                deltaSpan.innerHTML = lang === 'pl' ? `● W harmonogramie` : `● On schedule`;
            }} else if (delta < -5) {{
                deltaSpan.className = "font-bold text-lime-400";
                deltaSpan.innerHTML = lang === 'pl' ? `▲ ${{absDelta}} min przed planem` : `▲ ${{absDelta}} min ahead of plan`;
            }} else if (delta <= 20) {{
                deltaSpan.className = "font-bold text-orange-400";
                deltaSpan.innerHTML = lang === 'pl' ? `▼ ${{absDelta}} min za planem` : `▼ ${{absDelta}} min behind plan`;
            }} else {{
                deltaSpan.className = "font-bold text-red-500";
                deltaSpan.innerHTML = lang === 'pl' ? `▼ ${{absDelta}} min za planem` : `▼ ${{absDelta}} min behind plan`;
            }}
            
            const lastCp = checkpoints[checkpoints.length - 1];
            const remainingPlanMins = lastCp.elapsed_minutes - expectedElapsed;
            const etaMs = now.getTime() + remainingPlanMins * 60000;
            const etaDate = new Date(etaMs);
            const etaStr = `${{etaDate.getHours().toString().padStart(2, '0')}}:${{etaDate.getMinutes().toString().padStart(2, '0')}}`;
            document.getElementById('gps-finish-eta').innerHTML = etaStr;
        }}

        function showGpsErrorCard(msg) {{
            const card = document.getElementById('gps-status-card');
            const activeZone = document.getElementById('gps-card-active');
            const msgZone = document.getElementById('gps-card-message');
            
            card.classList.remove('hidden');
            activeZone.classList.add('hidden');
            msgZone.classList.remove('hidden');
            msgZone.innerHTML = msg;
        }}

        function locateMe(onSuccess = null) {{
            checkAndShowIosHint();
            
            if (!navigator.geolocation) {{
                showGpsErrorCard(document.documentElement.getAttribute('lang') === 'pl' ? "Brak wsparcia dla GPS w tej przeglądarce." : "GPS is not supported by this browser.");
                return;
            }}
            
            navigator.geolocation.getCurrentPosition(
                function(pos) {{
                    const lat = pos.coords.latitude;
                    const lon = pos.coords.longitude;
                    const accuracy = pos.coords.accuracy;
                    
                    let dotColor = '#3b82f6';
                    if (accuracy > 100) {{
                        dotColor = '#ef4444';
                    }} else if (accuracy > 50) {{
                        dotColor = '#f97316';
                    }}
                    
                    let minDistanceMetres = Infinity;
                    let closestTrackPt = null;
                    let closestIdx = -1;
                    const gpsLatLng = L.latLng(lat, lon);
                    
                    if (gpxTrackPoints && gpxTrackPoints.length > 0) {{
                        let searchStart = 0;
                        let searchEnd = gpxTrackPoints.length - 1;
                        
                        if (gpsLastMatchedIndex !== null) {{
                            searchStart = Math.max(0, gpsLastMatchedIndex - 150);
                            searchEnd = Math.min(gpxTrackPoints.length - 1, gpsLastMatchedIndex + 600);
                        }}
                        
                        for (let i = searchStart; i <= searchEnd; i++) {{
                            const d = gpsLatLng.distanceTo(gpxTrackPoints[i].latlng);
                            if (d < minDistanceMetres) {{
                                minDistanceMetres = d;
                                closestTrackPt = gpxTrackPoints[i];
                                closestIdx = i;
                            }}
                        }}
                        
                        if (closestIdx !== -1) {{
                            gpsLastMatchedIndex = closestIdx;
                            try {{
                                localStorage.setItem('gps_last_matched_index', gpsLastMatchedIndex);
                            }} catch(e) {{}}
                        }}
                    }}
                    
                    const isOffRoute = minDistanceMetres > 200;
                    const borderCol = isOffRoute ? '#fbbf24' : '#ffffff';
                    
                    if (!gpsMarker) {{
                        gpsMarker = L.circleMarker(gpsLatLng, {{
                            radius: 8,
                            fillColor: dotColor,
                            fillOpacity: 1,
                            color: borderCol,
                            weight: 2,
                            zIndexOffset: 1000
                        }}).addTo(map);
                    }} else {{
                        gpsMarker.setLatLng(gpsLatLng);
                        gpsMarker.setStyle({{
                            fillColor: dotColor,
                            color: borderCol
                        }});
                    }}
                    
                    if (!gpsAccuracyCircle) {{
                        gpsAccuracyCircle = L.circle(gpsLatLng, {{
                            radius: accuracy,
                            fillColor: dotColor,
                            fillOpacity: 0.12,
                            color: dotColor,
                            opacity: 0.45,
                            weight: 1.5,
                            className: isTracking ? 'gps-ring-pulse' : ''
                        }}).addTo(map);
                    }} else {{
                        gpsAccuracyCircle.setLatLng(gpsLatLng);
                        gpsAccuracyCircle.setRadius(accuracy);
                        gpsAccuracyCircle.setStyle({{
                            fillColor: dotColor,
                            color: dotColor,
                            className: isTracking ? 'gps-ring-pulse' : ''
                        }});
                        const path = gpsAccuracyCircle._path;
                        if (path) {{
                            if (isTracking) {{
                                path.classList.add('gps-ring-pulse');
                            }} else {{
                                path.classList.remove('gps-ring-pulse');
                            }}
                        }}
                    }}
                    
                    if (gpsMarker) {{
                        gpsMarker.bringToFront();
                    }}
                    if (gpsAccuracyCircle) {{
                        gpsAccuracyCircle.bringToBack();
                    }}
                    
                    const containerPoint = map.latLngToContainerPoint(gpsLatLng);
                    const mapSize = map.getSize();
                    const marginX = mapSize.x * 0.05;
                    const marginY = mapSize.y * 0.05;
                    
                    if (containerPoint.x < marginX || 
                        containerPoint.x > mapSize.x - marginX || 
                        containerPoint.y < marginY || 
                        containerPoint.y > mapSize.y - marginY) {{
                        map.panTo(gpsLatLng, {{ animate: true, duration: 0.4 }});
                    }}
                    
                    gpsCurrentKm = closestTrackPt ? closestTrackPt.km : 0;
                    gpsCurrentAccuracy = accuracy;
                    renderOverviewElevationChart();
                    
                    updateGpsStatusPanel(lat, lon, accuracy, minDistanceMetres);
                    
                    if (onSuccess) onSuccess();
                }},
                function(err) {{
                    console.warn("GPS Error code: " + err.code + " message: " + err.message);
                    let errStr = "";
                    const lang = document.documentElement.getAttribute('lang') || 'pl';
                    
                    if (err.code === 1) {{
                        errStr = lang === 'pl' ? "⚠️ Odmowa dostępu do lokalizacji. Włącz GPS w ustawieniach przeglądarki." : "⚠️ Location permission denied. Enable GPS in browser settings.";
                        if (isTracking) toggleTracking();
                    }} else if (err.code === 2) {{
                        errStr = lang === 'pl' ? "⚠️ Pozycja GPS niedostępna na tym urządzeniu." : "⚠️ GPS position unavailable on this device.";
                    }} else if (err.code === 3) {{
                        errStr = lang === 'pl' ? "⚠️ Przekroczono limit czasu oczekiwania. Spróbuj na zewnątrz." : "⚠️ GPS request timed out. Try again outdoors.";
                    }} else {{
                        errStr = lang === 'pl' ? "⚠️ Błąd lokalizacji: " + err.message : "⚠️ Geolocation error: " + err.message;
                    }}
                    showGpsErrorCard(errStr);
                }},
                {{ enableHighAccuracy: true, timeout: 10000, maximumAge: 5000 }}
            );
        }}

        function snapGpsToCheckpoint(cpKm) {{
            if (!gpxTrackPoints || gpxTrackPoints.length === 0) return;
            
            let closestIdx = 0;
            let minDiff = Math.abs(gpxTrackPoints[0].km - cpKm);
            for (let i = 1; i < gpxTrackPoints.length; i++) {{
                const diff = Math.abs(gpxTrackPoints[i].km - cpKm);
                if (diff < minDiff) {{
                    minDiff = diff;
                    closestIdx = i;
                }}
            }}
            
            gpsLastMatchedIndex = closestIdx;
            try {{
                localStorage.setItem('gps_last_matched_index', gpsLastMatchedIndex);
            }} catch (e) {{}}
            
            const isPl = document.documentElement.getAttribute('lang') === 'pl';
            showToast(isPl 
                ? `GPS zsynchronizowany z punktem KM ${{cpKm.toFixed(1)}}` 
                : `GPS snapped to checkpoint KM ${{cpKm.toFixed(1)}}`);
            
            if (gpsMarker) {{
                const currentLatLng = gpsMarker.getLatLng();
                let searchStart = Math.max(0, gpsLastMatchedIndex - 150);
                let searchEnd = Math.min(gpxTrackPoints.length - 1, gpsLastMatchedIndex + 600);
                
                let minDistanceMetres = Infinity;
                let closestTrackPt = gpxTrackPoints[searchStart];
                for (let i = searchStart; i <= searchEnd; i++) {{
                    const d = currentLatLng.distanceTo(gpxTrackPoints[i].latlng);
                    if (d < minDistanceMetres) {{
                        minDistanceMetres = d;
                        closestTrackPt = gpxTrackPoints[i];
                    }}
                }}
                
                gpsCurrentKm = closestTrackPt.km;
                renderOverviewElevationChart();
                updateGpsStatusPanel(currentLatLng.lat, currentLatLng.lng, gpsCurrentAccuracy || 10, minDistanceMetres);
            }}
        }}

        function toggleTracking() {{
            const btn = document.getElementById('btn-track-me');
            const isPl = document.documentElement.getAttribute('lang') === 'pl';
            
            if (!isTracking) {{
                const intervalVal = parseInt(document.getElementById('gps-poll-interval').value);
                if (intervalVal === 0) {{
                    showToast(isPl 
                        ? "Śledzenie automatyczne jest wyłączone w ustawieniach." 
                        : "Auto-positioning is disabled in settings.");
                    return;
                }}
                
                isTracking = true;
                if (btn) {{
                    btn.classList.add('leaflet-control-gps-active');
                    btn.querySelector('a').title = isPl ? "Wyłącz śledzenie GPS" : "Disable GPS tracking";
                }}
                
                showToast(isPl ? "Uruchamianie śledzenia GPS..." : "Starting GPS tracking...");
                locateMe(function() {{
                    gpsTrackingInterval = setInterval(locateMe, intervalVal);
                }});
                
            }} else {{
                isTracking = false;
                if (btn) {{
                    btn.classList.remove('leaflet-control-gps-active');
                    btn.querySelector('a').title = isPl ? "Śledź moją pozycję (GPS)" : "Track my position (GPS)";
                }}
                
                if (gpsTrackingInterval) {{
                    clearInterval(gpsTrackingInterval);
                    gpsTrackingInterval = null;
                }}
                
                if (gpsMarker) {{
                    map.removeLayer(gpsMarker);
                    gpsMarker = null;
                }}
                if (gpsAccuracyCircle) {{
                    map.removeLayer(gpsAccuracyCircle);
                    gpsAccuracyCircle = null;
                }}
                
                gpsCurrentKm = null;
                gpsCurrentAccuracy = null;
                renderOverviewElevationChart();
                
                const card = document.getElementById('gps-status-card');
                card.classList.add('hidden');
                
                showToast(isPl ? "Śledzenie GPS wyłączone" : "GPS tracking disabled");
            }}
        }}

        async function downloadOfflineTiles() {{
            const btn = document.getElementById('btn-download-map');
            const progress = document.getElementById('download-progress-bar');
            const isPl = document.documentElement.getAttribute('lang') === 'pl';
            
            if (!btn || btn.disabled) return;
            
            btn.disabled = true;
            btn.classList.add('bg-slate-800', 'text-slate-500', 'cursor-not-allowed');
            btn.classList.remove('bg-slate-700', 'text-slate-300', 'hover:text-white');
            progress.classList.remove('hidden');
            
            showToast(isPl ? "Rozpoczynanie pobierania mapy..." : "Starting map download...");
            
            try {{
                const urls = [];
                const bounds = {{
                    south: 49.30,
                    north: 49.95,
                    west: 18.40,
                    east: 19.60
                }};
                const zooms = [11, 12, 13, 14];
                
                zooms.forEach(zoom => {{
                    const startTile = latLonToTile(bounds.north, bounds.west, zoom);
                    const endTile = latLonToTile(bounds.south, bounds.east, zoom);
                    
                    const minX = Math.min(startTile.x, endTile.x);
                    const maxX = Math.max(startTile.x, endTile.x);
                    const minY = Math.min(startTile.y, endTile.y);
                    const maxY = Math.max(startTile.y, endTile.y);
                    
                    for (let x = minX; x <= maxX; x++) {{
                        for (let y = minY; y <= maxY; y++) {{
                            urls.push(`https://a.tile.opentopomap.org/${{zoom}}/${{x}}/${{y}}.png`);
                        }}
                    }}
                }});
                
                const total = urls.length;
                const cache = await caches.open('ultra-tiles-v1');
                
                for (let i = 0; i < total; i++) {{
                    const url = urls[i];
                    try {{
                        const res = await fetch(url, {{ mode: 'cors' }});
                        if (res.ok) {{
                            await cache.put(url, res);
                        }}
                    }} catch (e) {{
                        console.warn("Failed to fetch tile: " + url, e);
                    }}
                    
                    await new Promise(resolve => setTimeout(resolve, 150));
                    
                    const pct = Math.round(((i + 1) / total) * 100);
                    progress.innerHTML = `${{pct}}%`;
                }}
                
                localStorage.setItem('ultra_map_downloaded', '1');
                btn.innerHTML = `<span class="lang-pl">✓ Mapa offline gotowa</span><span class="lang-en">✓ Offline map ready</span>`;
                progress.classList.add('hidden');
                showToast(isPl ? "Pobieranie mapy zakończone sukcesem!" : "Map download completed successfully!");
                
            }} catch (err) {{
                console.error("Offline map cache download failed", err);
                btn.disabled = false;
                btn.classList.remove('bg-slate-800', 'text-slate-500', 'cursor-not-allowed');
                btn.classList.add('bg-slate-700', 'text-slate-300', 'hover:text-white');
                progress.classList.add('hidden');
                showToast(isPl ? "Błąd pobierania mapy. Spróbuj ponownie." : "Map download failed. Try again.");
            }}
        }}

        function latLonToTile(lat, lon, zoom) {{
            const latRad = lat * Math.PI / 180;
            let xtile = Math.floor((lon + 180) / 360 * Math.pow(2, zoom));
            let ytile = Math.floor((1 - Math.log(Math.tan(latRad) + 1 / Math.cos(latRad)) / Math.PI) / 2 * Math.pow(2, zoom));
            return {{ x: xtile, y: ytile }};
        }}

        // Initialize GPS polling and map pre-caching elements on load
        document.addEventListener('DOMContentLoaded', () => {{
            const intervalSelect = document.getElementById('gps-poll-interval');
            if (intervalSelect) {{
                try {{
                    const savedInterval = localStorage.getItem('ultra_gps_interval');
                    if (savedInterval) {{
                        intervalSelect.value = savedInterval;
                    }}
                }} catch(e) {{}}
                intervalSelect.addEventListener('change', () => {{
                    try {{
                        localStorage.setItem('ultra_gps_interval', intervalSelect.value);
                    }} catch(e) {{}}
                    
                    const isPl = document.documentElement.getAttribute('lang') === 'pl';
                    const intervalVal = parseInt(intervalSelect.value);
                    
                    if (isTracking) {{
                        if (intervalVal === 0) {{
                            toggleTracking();
                        }} else {{
                            if (gpsTrackingInterval) {{
                                clearInterval(gpsTrackingInterval);
                            }}
                            gpsTrackingInterval = setInterval(locateMe, intervalVal);
                            showToast(isPl ? "Zaktualizowano interwał GPS" : "GPS interval updated");
                        }}
                    }}
                }});
            }}

            const btnDownload = document.getElementById('btn-download-map');
            if (btnDownload) {{
                try {{
                    const downloaded = localStorage.getItem('ultra_map_downloaded');
                    if (downloaded === '1') {{
                        btnDownload.innerHTML = `<span class="lang-pl">✓ Mapa offline gotowa</span><span class="lang-en">✓ Offline map ready</span>`;
                    }}
                }} catch(e) {{}}
                btnDownload.addEventListener('click', downloadOfflineTiles);
            }}

            const btnResetGps = document.getElementById('btn-reset-gps');
            if (btnResetGps) {{
                btnResetGps.addEventListener('click', () => {{
                    gpsLastMatchedIndex = null;
                    try {{
                        localStorage.removeItem('gps_last_matched_index');
                    }} catch(e) {{}}
                    
                    if (isTracking) {{
                        toggleTracking();
                    }} else {{
                        if (gpsMarker) {{
                            map.removeLayer(gpsMarker);
                            gpsMarker = null;
                        }}
                        if (gpsAccuracyCircle) {{
                            map.removeLayer(gpsAccuracyCircle);
                            gpsAccuracyCircle = null;
                        }}
                        gpsCurrentKm = null;
                        gpsCurrentAccuracy = null;
                        renderOverviewElevationChart();
                        const card = document.getElementById('gps-status-card');
                        if (card) card.classList.add('hidden');
                        
                        const isPl = document.documentElement.getAttribute('lang') === 'pl';
                        showToast(isPl ? "Lokalizacja została zresetowana" : "Location tracking has been reset");
                    }}
                }});
            }}
        }});
        // ---------------------------------------------


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

        // Custom Locate Me Control (Crosshair target SVG)
        var LocateMeControl = L.Control.extend({{
            options: {{ position: 'topleft' }},
            onAdd: function (map) {{
                var container = L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');
                const isPl = document.documentElement.getAttribute('lang') === 'pl';
                container.innerHTML = `<a href="#" title="${{isPl ? 'Pokaż moją pozycję' : 'Show my current position'}}" style="display: flex; align-items: center; justify-content: center;" class="hover:bg-slate-50 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="#475569" stroke-width="2.5" style="width: 16px; height: 16px;">
                        <circle cx="12" cy="12" r="9" />
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 2v4M12 18v4M2 12h4M18 12h4" />
                        <circle cx="12" cy="12" r="2.5" fill="#475569" />
                    </svg>
                </a>`;
                container.onclick = function(e){{
                    e.preventDefault();
                    e.stopPropagation();
                    locateMe();
                }};
                return container;
            }}
        }});
        map.addControl(new LocateMeControl());

        // Custom Track Me Control (GPS signal SVG)
        var TrackMeControl = L.Control.extend({{
            options: {{ position: 'topleft' }},
            onAdd: function (map) {{
                var container = L.DomUtil.create('div', 'leaflet-bar leaflet-control leaflet-control-custom');
                container.id = 'btn-track-me';
                const isPl = document.documentElement.getAttribute('lang') === 'pl';
                container.innerHTML = `<a href="#" title="${{isPl ? 'Śledź moją pozycję (GPS)' : 'Track my position (GPS)'}}" style="display: flex; align-items: center; justify-content: center;" class="hover:bg-slate-50 transition-colors">
                    <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="#475569" stroke-width="2.5" style="width: 16px; height: 16px;">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M12 12L8 21M12 12L16 21M9.5 16h5M12 12V7" />
                        <path stroke-linecap="round" stroke-linejoin="round" d="M9 5a4.5 4.5 0 016 0" />
                        <path stroke-linecap="round" stroke-linejoin="round" d="M6 3a8.5 8.5 0 0112 0" />
                        <circle cx="12" cy="7" r="1.5" fill="#475569" />
                    </svg>
                </a>`;
                container.onclick = function(e){{
                    e.preventDefault();
                    e.stopPropagation();
                    toggleTracking();
                }};
                return container;
            }}
        }});
        map.addControl(new TrackMeControl());

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
            
            const disabledOpt = document.querySelector('#gps-poll-interval option[value="0"]');
            if (disabledOpt) {{
                disabledOpt.textContent = lang === 'pl' ? "Wyłączone" : "Disabled";
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
            const eleMatch = cp.ele.match(/\\+?\\s*(\\d+)\\s*m/);
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
            
            const sectHours = Math.floor(sectionElapsed / 60);
            const sectMins = sectionElapsed % 60;
            cp.section_duration = sectHours > 0 ? '+' + sectHours + 'h ' + sectMins + 'm' : '+' + sectMins + 'm';
            
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
                    color: '#c084fc', // purple-400 (distinct selection highlight)
                    weight: 8,
                    opacity: 0.95,
                    lineCap: 'round'
                }}).addTo(map);
                
                if (gpsMarker) {{
                    gpsMarker.bringToFront();
                }}
                
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
                    <td class="p-2 md:p-3 text-cyan-400 font-bold">
                        <div class="flex items-center gap-1.5">
                            <span>${{cp.km}}</span>
                            <button class="btn-snap-gps p-1 hover:bg-slate-700/80 rounded text-slate-500 hover:text-cyan-400 transition-colors text-[10px] md:text-xs cursor-pointer" title="Snap GPS search here" data-km="${{cp.km}}">📍</button>
                        </div>
                    </td>
                    <td class="p-2 md:p-3 leading-tight">
                        <div class="text-slate-200 font-bold">${{dynamicTime}}</div>
                        <div class="text-[10px] text-slate-500 font-bold">${{cp.section_duration}}</div>
                    </td>
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

                const snapBtn = tr.querySelector('.btn-snap-gps');
                if (snapBtn) {{
                    snapBtn.addEventListener('click', (e) => {{
                        e.stopPropagation();
                        snapGpsToCheckpoint(cp.km);
                    }});
                }}

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
            



            if (checkpoints.length > 0) {{
                const lastCp = checkpoints[checkpoints.length - 1];
                const currentMins = startMins + lastCp.elapsed_minutes;
                const outHour = Math.floor((currentMins % (24 * 60)) / 60);
                const outMin = currentMins % 60;
                const arrivalTime = `${{outHour.toString().padStart(2, '0')}}:${{outMin.toString().padStart(2, '0')}}`;
                
                const totalHours = Math.floor(lastCp.elapsed_minutes / 60);
                const totalMins = lastCp.elapsed_minutes % 60;
                const totalElapsed = `${{totalHours}}h ${{totalMins}}m`;

                const summaryTr = document.createElement('tr');
                summaryTr.className = 'bg-slate-900 font-bold text-lime-400 text-[11px] md:text-base border-t-2 border-lime-500/50';
                summaryTr.innerHTML = `
                    <td colspan="4" class="p-2 md:p-3 text-right">
                        <span class="lang-pl">SZACOWANY CZAS PRZEJŚCIA:</span><span class="lang-en">EST. TOTAL TIME:</span> <span class="text-white">${{totalElapsed}}</span>
                    </td>
                    <td colspan="3" class="p-2 md:p-3 text-left border-l border-slate-700/50">
                        <span class="lang-pl">CZAS NA MECIE:</span><span class="lang-en">ARRIVAL TIME:</span> <span class="text-white">${{arrivalTime}}</span>
                    </td>
                `;
                tableBody.appendChild(summaryTr);
            }}
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
                ctx.fillStyle = 'rgba(168, 85, 247, 0.08)'; // purple-500 translucent
                ctx.fillRect(hsXStart, paddingTop, hsXEnd - hsXStart, plotH);
                
                // Draw vertical dashed bounds for the highlighted section
                ctx.strokeStyle = 'rgba(168, 85, 247, 0.45)'; // purple border
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
                
                ctx.strokeStyle = 'rgba(168, 85, 247, 0.35)'; // semi-translucent purple
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
                ctx.fillStyle = isBound ? '#c084fc' : '#a3e635'; // purple-400 or lime-400
                ctx.fill();
                ctx.strokeStyle = '#0f172a'; // slate-900 outline
                ctx.lineWidth = isBound ? 1.5 : 1;
                ctx.stroke();
            }});
            
            // 6.5. Draw GPS user position (if available)
            if (gpsCurrentKm !== null) {{
                const gpsX = paddingLeft + (gpsCurrentKm / maxDist) * plotW;
                
                // Interpolate Y elevation at gpsCurrentKm
                let gpsEle = minEle;
    

            if (gpxElevationData && gpxElevationData.length > 0) {{
                    let closestPrev = gpxElevationData[0];
                    let closestNext = gpxElevationData[gpxElevationData.length - 1];
                    for (let i = 0; i < gpxElevationData.length; i++) {{
                        const pt = gpxElevationData[i];
                        if (pt[0] <= gpsCurrentKm && pt[0] > closestPrev[0]) {{
                            closestPrev = pt;
                        }}
                        if (pt[0] >= gpsCurrentKm && pt[0] < closestNext[0]) {{
                            closestNext = pt;
                        }}
                    }}
                    if (closestNext[0] === closestPrev[0]) {{
                        gpsEle = closestPrev[1];
                    }} else {{
                        const ratio = (gpsCurrentKm - closestPrev[0]) / (closestNext[0] - closestPrev[0]);
                        gpsEle = closestPrev[1] + ratio * (closestNext[1] - closestPrev[1]);
                    }}
                }}
                
                const gpsY = paddingTop + (1 - (gpsEle - plotMin) / eleRange) * plotH;
                
                // Determine signal quality color
                let gpsColor = '#3b82f6'; // Good (<=50m)
                if (gpsCurrentAccuracy > 100) {{
                    gpsColor = '#ef4444'; // Poor
                }} else if (gpsCurrentAccuracy > 50) {{
                    gpsColor = '#f97316'; // Moderate
                }}
                
                // Draw vertical indicator line
                ctx.strokeStyle = gpsColor;
                ctx.lineWidth = 1.5;
                ctx.setLineDash([3, 3]);
                ctx.beginPath();
                ctx.moveTo(gpsX, gpsY);
                ctx.lineTo(gpsX, h - paddingBottom);
                ctx.stroke();
                ctx.setLineDash([]);
                
                // Draw white glowing underlay for the dot
                ctx.beginPath();
                ctx.arc(gpsX, gpsY, 8.5, 0, 2 * Math.PI);
                ctx.fillStyle = 'rgba(255, 255, 255, 0.4)';
                ctx.fill();
                
                // Draw position dot
                ctx.beginPath();
                ctx.arc(gpsX, gpsY, 6, 0, 2 * Math.PI);
                ctx.fillStyle = gpsColor;
                ctx.fill();
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 2;
                ctx.stroke();
            }}
            
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
                navigator.serviceWorker.register('./sw_75.js', {{ scope: './Ultra75_standalone.html' }}).then(registration => {{
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



print('Writing Ultra75_standalone.html...')
with open('Ultra75_standalone.html', 'w', encoding='utf-8') as f:
    f.write(html_template)

manifest_data = {
    "id": "./Ultra75_standalone.html",
    "scope": "./Ultra75_standalone.html",
    "name": "Wyrypa 75km",
    "short_name": "Wyrypa 75k",
    "start_url": "./Ultra75_standalone.html",
    "display": "standalone",
    "background_color": "#0f172a",
    "theme_color": "#0f172a",
    "description": "Offline tracker for 75km Ultra-Trekking",
    "icons": [
        {
            "src": "./icon-192_75.svg",
            "sizes": "192x192",
            "type": "image/svg+xml",
            "purpose": "any maskable"
        },
        {
            "src": "./icon-512_75.svg",
            "sizes": "512x512",
            "type": "image/svg+xml",
            "purpose": "any maskable"
        }
    ]
}

with open('manifest_75.json', 'w', encoding='utf-8') as f:
    json.dump(manifest_data, f, indent=4)

sw_content = f'''const CACHE_NAME = '{app_version}';
const ASSETS = [
    './',
    './index.html',
    './Ultra75_standalone.html',
    './manifest_75.json',
    './icon-192_75.svg',
    './icon-512_75.svg',
    './wyrypa75km.gpx',
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
    
    if (event.request.url.includes('tile.opentopomap.org')) {{
        const normalizedUrl = event.request.url.replace(/https:\/\/[abc]\.tile\.opentopomap\.org/, 'https://a.tile.opentopomap.org');
        event.respondWith(
            caches.match(normalizedUrl).then(response => {{
                return response || fetch(event.request).then(fetchResponse => {{
                    if (fetchResponse.ok) {{
                        const responseClone = fetchResponse.clone();
                        caches.open('ultra-tiles-v1').then(cache => {{
                            cache.put(normalizedUrl, responseClone);
                        }});
                    }}
                    return fetchResponse;
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

print('Writing sw_75.js...')
with open('sw_75.js', 'w', encoding='utf-8') as f:
    f.write(sw_content)

icon_192_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="192" height="192">
  <rect width="192" height="192" fill="#0f172a"/>
  <circle cx="96" cy="96" r="48" fill="#06b6d4"/>
  <text x="96" y="104" font-family="sans-serif" font-size="24" font-weight="bold" fill="#0f172a" text-anchor="middle">75k</text>
</svg>
'''

icon_512_content = '''<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512">
  <rect width="512" height="512" fill="#0f172a"/>
  <circle cx="256" cy="256" r="128" fill="#06b6d4"/>
  <text x="256" y="278" font-family="sans-serif" font-size="64" font-weight="bold" fill="#0f172a" text-anchor="middle">75k</text>
</svg>
'''

print('Writing icon-192_75.svg...')
with open('icon-192_75.svg', 'w', encoding='utf-8') as f:
    f.write(icon_192_content)

print('Writing icon-512_75.svg...')
with open('icon-512_75.svg', 'w', encoding='utf-8') as f:
    f.write(icon_512_content)

print('Successfully generated Ultra75_standalone.html, manifest_75.json, sw_75.js, and 75k icons.')
