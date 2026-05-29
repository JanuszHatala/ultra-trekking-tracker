import xml.etree.ElementTree as ET
import math

def lat_lon_to_tile(lat, lon, zoom):
    lat_rad = lat * math.pi / 180.0
    xtile = int((lon + 180.0) / 360.0 * (2.0 ** zoom))
    ytile = int((1.0 - math.log(math.tan(lat_rad) + 1.0 / math.cos(lat_rad)) / math.pi) / 2.0 * (2.0 ** zoom))
    return xtile, ytile

# Parse GPX
tree = ET.parse('wyrypa75km.gpx')
root = tree.getroot()

# Namespaces in GPX
ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}

trackpoints = []
for trkpt in root.findall('.//gpx:trkpt', ns):
    lat = float(trkpt.attrib['lat'])
    lon = float(trkpt.attrib['lon'])
    trackpoints.append((lat, lon))

print(f"Total trackpoints: {len(trackpoints)}")

zooms = [11, 12, 13, 14, 15, 16, 17]
for zoom in zooms:
    tiles = set()
    for lat, lon in trackpoints:
        cx, cy = lat_lon_to_tile(lat, lon, zoom)
        # 3x3 block
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                tiles.add((cx + dx, cy + dy))
    print(f"Zoom {zoom}: {len(tiles)} unique tiles")
