import xml.etree.ElementTree as ET
import math

def lat_lon_to_tile(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return x, y

def analyze_buffers(gpx_path):
    tree = ET.parse(gpx_path)
    root = tree.getroot()
    ns = {'gpx': 'http://www.topografix.com/GPX/1/1'}
    points = []
    for trkpt in root.findall('.//gpx:trkpt', ns):
        lat = float(trkpt.attrib['lat'])
        lon = float(trkpt.attrib['lon'])
        points.append((lat, lon))
        
    if not points:
        for trkpt in root.findall('.//trkpt'):
            lat = float(trkpt.attrib['lat'])
            lon = float(trkpt.attrib['lon'])
            points.append((lat, lon))
            
    print(f"\nLoaded {len(points)} points from {gpx_path}")
    
    zooms = [11, 12, 13, 14, 15, 16, 17]
    
    tile_set = set()
    for zoom in zooms:
        if zoom <= 13:
            buf = 1  # 3x3
        elif zoom <= 15:
            buf = 2  # 5x5
        elif zoom == 16:
            buf = 3  # 7x7
        else:
            buf = 4  # 9x9
            
        for lat, lon in points:
            cx, cy = lat_lon_to_tile(lat, lon, zoom)
            for dx in range(-buf, buf + 1):
                for dy in range(-buf, buf + 1):
                    tile_set.add((zoom, cx + dx, cy + dy))
                    
    print(f"Total unique tiles (zooms 11-13: 3x3, 14-15: 5x5, 16: 7x7, 17: 9x9): {len(tile_set)}")
    
    # Let's count by zoom level
    for zoom in zooms:
        z_set = {t for t in tile_set if t[0] == zoom}
        print(f"Zoom {zoom} (buf={1 if zoom<=13 else (2 if zoom<=15 else (3 if zoom==16 else 4))}): {len(z_set)} tiles")

print("--- 75km App ---")
analyze_buffers("wyrypa75km.gpx")
print("\n--- 100km App ---")
analyze_buffers("wyrypa-100km.gpx")
