import xml.etree.ElementTree as ET
import math

def haversine(lat1, lon1, lat2, lon2):
    # Distance in meters
    R = 6371000
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = math.sin(delta_phi/2)**2 + math.cos(phi1)*math.cos(phi2)*math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def analyze_gpx(gpx_path):
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
            
    print(f"GPX: {gpx_path}")
    print(f"Total points: {len(points)}")
    
    distances = []
    large_gaps = []
    for i in range(1, len(points)):
        dist = haversine(points[i-1][0], points[i-1][1], points[i][0], points[i][1])
        distances.append(dist)
        if dist > 100: # gap larger than 100m
            large_gaps.append((i-1, i, dist, points[i-1], points[i]))
            
    if distances:
        print(f"Average distance: {sum(distances)/len(distances):.2f}m")
        print(f"Max distance: {max(distances):.2f}m")
        print(f"Number of gaps > 100m: {len(large_gaps)}")
        for idx, (p1, p2, dist, c1, c2) in enumerate(large_gaps[:5]):
            print(f"  Gap {idx}: {dist:.2f}m between point {p1} ({c1}) and {p2} ({c2})")
    print("-" * 40)

analyze_gpx("wyrypa75km.gpx")
analyze_gpx("wyrypa-100km.gpx")
