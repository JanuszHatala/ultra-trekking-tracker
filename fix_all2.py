import re
import subprocess

def fix_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Clean up ALL occurrences of the bad logic
    bad_pattern = r'[ \t]*if \(checkpoints\.length > 0\) \{\{[\s\S]*?tableBody\.appendChild\(summaryTr\);\s*\}\}\n?'
    content = re.sub(bad_pattern, '', content)

    # 2. Fix elevation regex
    content = content.replace(r'cp.ele.match(/\\+?(\\d+)m/);', r'cp.ele.match(/\\+?\\s*(\\d+)\\s*m/);')

    # 3. Inject footer ONLY inside renderApp (right before renderMiniCharts)
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
    # Find the renderApp definition block and inject inside it
    # We look for "function renderApp() {{" and then the end of it where renderMiniCharts is called.
    render_app_pattern = r'(function renderApp\(\) \{\{[\s\S]*?)(            if \(gpxElevationData && gpxElevationData\.length > 0\) \{\{\s*renderMiniCharts\(\);\s*\}\}\s*\})'
    
    # Wait, in the Python string, it's `if (gpxElevationData && gpxElevationData.length > 0) {{`
    render_app_pattern = r'(function renderApp\(\) \{\{[\s\S]*?)([ \t]*if \(gpxElevationData && gpxElevationData\.length > 0\) \{\{\s*renderMiniCharts\(\);\s*\}\}\s*\})'
    
    content, count = re.subn(render_app_pattern, lambda m: m.group(1) + logic_to_insert + m.group(2), content, count=1)
    if count == 0:
        print(f"Warning: Failed to inject footer in {filename}")

    # 4. Remove index.html overwrite in 75km app
    if '75km' in filename:
        index_write = r"print\('Writing index\.html\.\.\.'\)\nwith open\('index\.html', 'w', encoding='utf-8'\) as f:\n    f\.write\(index_html\)\n\n"
        content = content.replace(index_write, "")
        
        # In case the regex didn't match the exact spacing
        content = re.sub(r"print\('Writing index\.html\.\.\.'\)\s*with open\('index\.html', 'w', encoding='utf-8'\) as f:\s*f\.write\(index_html\)\s*", "", content)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Cleaned and fixed {filename}")

fix_file('build_standalone.py')
fix_file('build_standalone_75km.py')
