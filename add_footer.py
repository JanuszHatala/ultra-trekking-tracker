import re

logic_to_insert = """
            if (checkpoints.length > 0) {
                const lastCp = checkpoints[checkpoints.length - 1];
                const currentMins = startMins + lastCp.elapsed_minutes;
                const outHour = Math.floor((currentMins % (24 * 60)) / 60);
                const outMin = currentMins % 60;
                const arrivalTime = `${outHour.toString().padStart(2, '0')}:${outMin.toString().padStart(2, '0')}`;
                
                const totalHours = Math.floor(lastCp.elapsed_minutes / 60);
                const totalMins = lastCp.elapsed_minutes % 60;
                const totalElapsed = `${totalHours}h ${totalMins}m`;

                const summaryTr = document.createElement('tr');
                summaryTr.className = 'bg-slate-900/80 font-bold text-lime-400 text-[11px] md:text-base border-t-2 border-lime-500/50';
                summaryTr.innerHTML = `
                    <td colspan="4" class="p-2 md:p-3 text-right">
                        <span class="lang-pl">SZACOWANY CZAS PRZEJŚCIA:</span><span class="lang-en">EST. TOTAL TIME:</span> <span class="text-white">${totalElapsed}</span>
                    </td>
                    <td colspan="3" class="p-2 md:p-3 text-left border-l border-slate-700/50">
                        <span class="lang-pl">CZAS NA MECIE:</span><span class="lang-en">ARRIVAL TIME:</span> <span class="text-white">${arrivalTime}</span>
                    </td>
                `;
                tableBody.appendChild(summaryTr);
            }
"""

for filename in ['build_standalone.py', 'build_standalone_75km.py']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target_str = "            if (gpxElevationData && gpxElevationData.length > 0) {"
    
    if target_str in content:
        content = content.replace(target_str, logic_to_insert + "\n" + target_str)
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Injected into {filename}")
