import re

with open('build_standalone_75km.py', 'r', encoding='utf-8') as f:
    content = f.read()

placeholder_start = '<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl border-dashed border-slate-600 opacity-80">'
placeholder_end = '<!-- ZAKŁADKA: TRENING (jeśli występuje) -->' # Wait, I don't know the exact string after.
# I'll just use regex to replace that div
# The div has class starting with bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl border-dashed

new_schedule_html = '''<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl">
                <h2 class="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2"><span class="lang-pl">2. HARMONOGRAM OGÓLNY I POSTOJE</span><span class="lang-en">2. GENERAL SCHEDULE & STOPS</span></h2>
                <p class="text-sm text-slate-400 italic mb-6"><span class="lang-pl">Wyrypa w pełnej autonomii. Brak przepaku i ciepłych posiłków. Przerwy zredukowane do absolutnego minimum wymaganego do utrzymania stóp w sprawności pod obciążeniem 12 kg.</span><span class="lang-en">Full autonomy. No drop bags or warm meals. Breaks reduced to the absolute minimum required to keep feet functional under a 12kg load.</span></p>
                
                <div class="relative border-l-2 border-slate-600 ml-3 pl-6 space-y-6">
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-slate-500 w-4 h-4 rounded-full mt-1.5"></span>
                        <h4 class="font-bold text-white text-lg">0 - 25 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Marsz ciągły</span><span class="lang-en">Continuous march</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Wejście w noc. Adaptacja do ciężaru. Skupienie na miarowym tętnie i rygorystycznym opróżnianiu bidonów (1/h).</span><span class="lang-en">Entering the night. Adapting to the load. Focus on steady heart rate and strict flask emptying (1/h).</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">25 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 5 min</span><span class="lang-en">5 min break</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl"><strong>Krytyczna konserwacja stóp.</strong> Ściągnięcie butów, osuszenie, nałożenie wazeliny, zmiana skarpet na suche. Zjedzenie stałego pokarmu (baton/kabanos).</span><span class="lang-en"><strong>Critical foot maintenance.</strong> Take off shoes, dry feet, apply vaseline, change to dry socks. Eat solid food (energy bar/salty snack).</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-slate-500 w-4 h-4 rounded-full mt-1.5"></span>
                        <h4 class="font-bold text-white text-lg">25 - 50 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Nocny marsz</span><span class="lang-en">Night march</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Faza największego kryzysu senności ("Godzina Wilka"). Konieczność przyjęcia kofeiny (ok. 30-35 km). Na koniec tego etapu następuje wschód słońca.</span><span class="lang-en">The deepest sleep crisis phase ("Witching Hour"). Caffeine intake required (around 30-35 km). Sunrise occurs at the end of this stage.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-amber-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(245,158,11,0.5)]"></span>
                        <h4 class="font-bold text-amber-400 text-lg">50 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Przerwa 5 min</span><span class="lang-en">5 min break</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl"><strong>Druga konserwacja stóp.</strong> Przewietrzenie stóp, inspekcja otarć, ponowna aplikacja wazeliny (ew. zmiana na 2. parę zapasowych skarpet). Zjedzenie kanapki.</span><span class="lang-en"><strong>Second foot maintenance.</strong> Air out feet, inspect for chafing, reapply vaseline (change to 2nd spare pair of socks if carried). Eat a sandwich.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-8 bg-slate-800 border-2 border-red-500 w-4 h-4 rounded-full mt-1.5 shadow-[0_0_8px_rgba(239,68,68,0.5)]"></span>
                        <h4 class="font-bold text-red-400 text-lg">50 - 74 km <span class="text-sm text-slate-400 font-normal ml-2 bg-slate-800 px-2 py-0.5 rounded border border-slate-600"><span class="lang-pl">Faza końcowa</span><span class="lang-en">Final phase</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Marsz w świetle dnia na narastającym długu mięśniowym. Żołądek może odrzucać ciała stałe – przejście całkowicie na żele i Hyper-Mix. Kofeina w razie potrzeby.</span><span class="lang-en">Daylight march on accumulating muscle fatigue. Stomach may reject solid food – transition entirely to gels and Hyper-Mix. Caffeine as needed.</span></p>
                    </div>
                    
                    <div class="relative">
                        <span class="absolute -left-[34px] bg-slate-900 border-2 border-lime-500 w-5 h-5 rounded-full mt-1 flex items-center justify-center shadow-[0_0_12px_rgba(132,204,22,0.6)]"><span class="bg-lime-500 w-2 h-2 rounded-full"></span></span>
                        <h4 class="font-bold text-lime-400 text-xl">74 km <span class="text-sm text-lime-400 font-normal ml-2 bg-lime-900/30 px-2 py-0.5 rounded border border-lime-700"><span class="lang-pl">META</span><span class="lang-en">FINISH</span></span></h4>
                        <p class="text-sm text-slate-300 mt-1"><span class="lang-pl">Zatrzymanie stopera. Koniec testu autonomii. Nawodnienie i odpoczynek.</span><span class="lang-en">Stop the timer. End of the autonomy test. Hydrate and rest.</span></p>
                    </div>
                </div>
            </div>'''

content = re.sub(r'<div class="bg-slate-800/50 p-6 rounded-lg border border-slate-700 shadow-xl border-dashed border-slate-600 opacity-80">.*?</div>', new_schedule_html, content, flags=re.DOTALL)

with open('build_standalone_75km.py', 'w', encoding='utf-8') as f:
    f.write(content)
