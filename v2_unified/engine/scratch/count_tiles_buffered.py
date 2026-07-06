import xml.etree.ElementTree as ET
import math

def lat_lon_to_tile(lat, lon, zoom):
    lat_rad = math.radians(lat)
    n = 2.0 ** zoom
    x = int((lon + 180.0) / 360.0 * n)
    y = int((1.0 - math.log(math.tan(lat_rad) + (1 / math.cos(lat_rad))) / math.pi) / 2.0 * n)
    return x, y

def count_tiles_buffered(gpx_path):
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
            
    print(f"Loaded {len(points)} points from {gpx_path}")
    
    zooms = [11, 12, 13, 14, 15, 16, 17]
    total_unique_tiles = 0
    
    for zoom in zooms:
        tile_set = set()
        
        # Buffer mapping
        if zoom in [11, 12, 13]:
            buf = 1
        elif zoom in [14, 15]:
            buf = 2
        elif zoom == 16:
            buf = 3
        elif zoom == 17:
            buf = 4
        else:
            buf = 1
            
        for lat, lon in points:
            cx, cy = lat_lon_to_tile(lat, lon, zoom)
            for dx in range(-buf, buf + 1):
                for dy in range(-buf, buf + 1):
                    tile_set.add((cx + dx, cy + dy))
        print(f"Zoom {zoom} (buf={buf}): {len(tile_set)} unique tiles")
        total_unique_tiles += len(tile_set)
        
    print(f"Total unique tiles for all zooms: {total_unique_tiles}")
    return total_unique_tiles

print("--- 75km Track (Buffered) ---")
count_tiles_buffered("wyrypa75km.gpx")
print("\n--- 100km Track (Buffered) ---")
count_tiles_buffered("wyrypa-100km.gpx")
