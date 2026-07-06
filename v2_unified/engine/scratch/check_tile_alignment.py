import xml.etree.ElementTree as ET
import math

def lat_lon_to_tile(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return x, y

# Parse first point in GPX
tree = ET.parse("wyrypa75km.gpx")
root = tree.getroot()
ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}
points = []
for trkpt in root.findall('.//gpx:trkpt', ns):
    lat = float(trkpt.attrib['lat'])
    lon = float(trkpt.attrib['lon'])
    points.append((lat, lon))
    break
    
if not points:
    for trkpt in root.findall('.//trkpt'):
        lat = float(trkpt.attrib['lat'])
        lon = float(trkpt.attrib['lon'])
        points.append((lat, lon))
        break

lat, lon = points[0]
print(f"First point coordinate: Lat={lat}, Lon={lon}")

# Calculate tile for zoom 17
zoom = 17
x, y = lat_lon_to_tile(lat, lon, zoom)
print(f"Calculated Tile Zoom {zoom}: X={x}, Y={y}")
print(f"Tile URL: https://a.tile.opentopomap.org/{zoom}/{x}/{y}.png")
