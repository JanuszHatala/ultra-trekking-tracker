import sys
import math
import xml.etree.ElementTree as ET

def get_distance(lat1, lon1, lat2, lon2):
    R = 6371
    dLat = math.radians(lat2 - lat1)
    dLon = math.radians(lon2 - lon1)
    a = math.sin(dLat/2) * math.sin(dLat/2) + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dLon/2) * math.sin(dLon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

def analyze_gpx(filepath):
    tree = ET.parse(filepath)
    root = tree.getroot()
    # Handle namespaces
    ns = {'gpx': root.tag.split('}')[0].strip('{') if '}' in root.tag else ''}
    ns_prefix = f"{{{ns['gpx']}}}" if ns['gpx'] else ""
    
    points = []
    for trkpt in root.iter(f'{ns_prefix}trkpt'):
        lat = float(trkpt.attrib['lat'])
        lon = float(trkpt.attrib['lon'])
        ele = float(trkpt.find(f'{ns_prefix}ele').text)
        points.append({'lat': lat, 'lon': lon, 'ele': ele})
    
    if not points:
        print("No track points found in GPX.")
        return
        
    total_dist = 0
    elapsed_minutes = 0
    
    # Store data point for each hour
    hourly_stats = []
    current_hour = 0
    
    hour_start_km = 0
    hour_ascent = 0
    hour_descent = 0
    
    for i in range(1, len(points)):
        p1 = points[i-1]
        p2 = points[i]
        
        dist = get_distance(p1['lat'], p1['lon'], p2['lat'], p2['lon'])
        total_dist += dist
        
        ele_diff = p2['ele'] - p1['ele']
        ascent = max(0, ele_diff)
        descent = max(0, -ele_diff)
        
        hour_ascent += ascent
        hour_descent += descent
        
        base_time = dist * 10
        ascent_time = (ascent / 100) * 10
        descent_time = (descent / 100) * -2
        
        section_time = max(base_time + ascent_time + descent_time, dist * 5)
        elapsed_minutes += section_time
        
        while elapsed_minutes >= (current_hour + 1) * 60:
            terrain = "Flat/Rolling"
            if hour_ascent > 150 and hour_ascent > hour_descent * 2:
                terrain = "Steep Climb"
            elif hour_ascent > 50 and hour_ascent > hour_descent:
                terrain = "Climb"
            elif hour_descent > 150 and hour_descent > hour_ascent * 2:
                terrain = "Steep Descent"
            elif hour_descent > 50 and hour_descent > hour_ascent:
                terrain = "Descent"
            elif hour_ascent > 100 and hour_descent > 100:
                terrain = "Hilly/Mixed"
                
            hourly_stats.append({
                "hour": current_hour,
                "start_km": hour_start_km,
                "end_km": total_dist,
                "ascent": hour_ascent,
                "descent": hour_descent,
                "terrain": terrain
            })
            current_hour += 1
            hour_start_km = total_dist
            hour_ascent = 0
            hour_descent = 0
            
    # Remaining time
    if hour_start_km < total_dist:
        terrain = "Flat/Rolling"
        if hour_ascent > hour_descent + 50: terrain = "Climb"
        elif hour_descent > hour_ascent + 50: terrain = "Descent"
        hourly_stats.append({
            "hour": current_hour,
            "start_km": hour_start_km,
            "end_km": total_dist,
            "ascent": hour_ascent,
            "descent": hour_descent,
            "terrain": terrain
        })
    
    print(f"--- Topography Analysis for {filepath} ---")
    print("Copy this table into the LLM prompt to provide exact topographical context for the actionTimeline.\n")
    print(f"{'Hour':<10} | {'KM Range':<15} | {'Ascent':<10} | {'Descent':<10} | {'Terrain Type'}")
    print("-" * 65)
    for stat in hourly_stats:
        hour_label = f"{stat['hour']}.0 - {stat['hour']+1}.0"
        km_label = f"{stat['start_km']:.1f} - {stat['end_km']:.1f}"
        asc_label = f"+{int(stat['ascent'])}m"
        desc_label = f"-{int(stat['descent'])}m"
        print(f"{hour_label:<10} | {km_label:<15} | {asc_label:<10} | {desc_label:<10} | {stat['terrain']}")
    print("-" * 65)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python analyze_gpx_topography.py <path_to_gpx>")
        sys.exit(1)
    analyze_gpx(sys.argv[1])
