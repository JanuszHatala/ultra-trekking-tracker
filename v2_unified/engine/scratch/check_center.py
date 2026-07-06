import json
import math
import xml.etree.ElementTree as ET

def lat_lon_to_tile(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad)))) / 2.0 * n)
    return (x, y)

def distance(lat1, lon1, lat2, lon2):
    R = 6371000 # meters
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

# parse GPX
tree = ET.parse('wyrypa75km.gpx')
root = tree.getroot()
ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}

pts = []
for trkpt in root.findall('.//gpx:trkpt', ns):
    lat = float(trkpt.attrib['lat'])
    lon = float(trkpt.attrib['lon'])
    pts.append((lat, lon))

# Section 1 is from start (0km) to CP1 (approx 16km)
# Let's just take the first 1/5th of points
section_pts = pts[:len(pts)//5]

min_lat = min(p[0] for p in section_pts)
max_lat = max(p[0] for p in section_pts)
min_lon = min(p[1] for p in section_pts)
max_lon = max(p[1] for p in section_pts)

center_lat = (min_lat + max_lat) / 2
center_lon = (min_lon + max_lon) / 2

# find nearest track point to center
min_dist = min(distance(center_lat, center_lon, p[0], p[1]) for p in pts)
print(f"Center: {center_lat}, {center_lon}")
print(f"Distance from bounding box center to nearest track point: {min_dist:.2f} meters")

# How many tiles is that at zoom 17?
center_tile = lat_lon_to_tile(center_lat, center_lon, 17)
nearest_pt = min(pts, key=lambda p: distance(center_lat, center_lon, p[0], p[1]))
nearest_tile = lat_lon_to_tile(nearest_pt[0], nearest_pt[1], 17)

dx = abs(center_tile[0] - nearest_tile[0])
dy = abs(center_tile[1] - nearest_tile[1])
print(f"Tile difference at zoom 17: dx={dx}, dy={dy}")
