import math
import xml.etree.ElementTree as ET

def distance(lat1, lon1, lat2, lon2):
    R = 6371000 # meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

tree = ET.parse('wyrypa75km.gpx')
root = tree.getroot()
ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}

pts = []
for trkpt in root.findall('.//gpx:trkpt', ns):
    lat = float(trkpt.attrib['lat'])
    lon = float(trkpt.attrib['lon'])
    pts.append((lat, lon))

max_dist = 0
max_pair = None
for i in range(len(pts)-1):
    dist = distance(pts[i][0], pts[i][1], pts[i+1][0], pts[i+1][1])
    if dist > max_dist:
        max_dist = dist
        max_pair = (i, i+1)

print(f"Total points: {len(pts)}")
print(f"Maximum distance between consecutive points: {max_dist:.2f} meters (between points {max_pair[0]} and {max_pair[1]})")
