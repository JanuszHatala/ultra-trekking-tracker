import os

for filename in ['build_standalone.py', 'build_standalone_75km.py']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove CDN URLs from ASSETS
    content = content.replace("    'https://cdn.tailwindcss.com',\n", '')
    content = content.replace("    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',\n", '')
    content = content.replace("    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',\n", '')
    content = content.replace("    'https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.7.0/gpx.min.js'\n", '')
    
    # Fix the trailing comma in ASSETS array for wyrypa100km.gpx / wyrypa75km.gpx
    content = content.replace("    './wyrypa75km.gpx',\n];", "    './wyrypa75km.gpx'\n];")
    content = content.replace("    './wyrypa100km.gpx',\n];", "    './wyrypa100km.gpx'\n];")
    
    # Increment version
    content = content.replace('v1.4</span></h1>', 'v1.5</span></h1>')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
