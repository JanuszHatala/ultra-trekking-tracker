import re
import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0 # Earth radius in kilometers
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return R * c

def get_track_length(filename):
    data = open(filename, 'r', encoding='utf-8').read()
    pts = re.findall(r'<trkpt lat="(.*?)" lon="(.*?)"', data)
    dist = 0.0
    for i in range(1, len(pts)):
        dist += haversine(float(pts[i-1][0]), float(pts[i-1][1]), float(pts[i][0]), float(pts[i][1]))
    print(f'{filename} length: {dist:.2f} km')

get_track_length('wyrypa75km.gpx')
get_track_length('wyrypa-100km.gpx')
