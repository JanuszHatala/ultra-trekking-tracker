import re

def print_last_pt(filename):
    data = open(filename, 'r', encoding='utf-8').read()
    pts = re.findall(r'<trkpt lat="(.*?)" lon="(.*?)"', data)
    print(f'{filename} last point: {pts[-1]}')

print_last_pt('wyrypa75km.gpx')
print_last_pt('wyrypa-100km.gpx')
