import re
import subprocess

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Fix the regex for elevation
    content = content.replace(r'cp.ele.match(/\\+?(\\d+)m/);', r'cp.ele.match(/\\+?\\s*(\\d+)\\s*m/);')

    # 2. Remove all bad injected footers
    bad_logic_pattern = r'[ \t]*if \(checkpoints\.length > 0\) \{[^{}]*?tableBody\.appendChild\(summaryTr\);\s*\}\s*'
    content = re.sub(bad_logic_pattern, '', content, flags=re.DOTALL)

    # 3. Inject footer ONLY before renderMiniCharts()
    logic_to_insert = """
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
"""
    target = r'([ \t]*if \(gpxElevationData && gpxElevationData\.length > 0\) \{\s*renderMiniCharts\(\);\s*\})'
    
    # Check if target exists
    if re.search(target, content):
        content = re.sub(target, lambda m: logic_to_insert + m.group(1), content, count=1)
    else:
        print(f"Warning: target not found in {filename}")

    # 4. Remove index.html writing logic ONLY in 75km build
    if "75km" in filename:
        index_write_pattern = r'with open\(\'index\.html\', \'w\', encoding=\'utf-8\'\) as f:\s*f\.write\(.*?print\(\'Writing Ultra75'
        content = re.sub(r'print\(\'Writing index\.html\.\.\.\'\)\s*with open\(\'index\.html\', \'w\', encoding=\'utf-8\'\) as f:\s*f\.write\(.*?\)[\s\r\n]*print\(\'Writing Ultra75', "print('Writing Ultra75", content, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully processed {filename}")

fix_file('build_standalone.py')
fix_file('build_standalone_75km.py')

# 5. Restore the portal index.html from HEAD~1
try:
    portal_html = subprocess.check_output(['git', 'show', 'HEAD~1:index.html']).decode('utf-8')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(portal_html)
    print("Restored portal index.html")
except Exception as e:
    print(f"Failed to restore index.html: {e}")
