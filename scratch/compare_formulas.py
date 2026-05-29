import math

def osm_deg2num(lat_deg, lon_deg, zoom):
    lat_rad = math.radians(lat_deg)
    n = 2.0 ** zoom
    xtile = int((lon_deg + 180.0) / 360.0 * n)
    ytile = int((1.0 - math.asinh(math.tan(lat_rad)) / math.pi) / 2.0 * n)
    return (xtile, ytile)

def our_lat_lon_to_tile(lat, lon, zoom):
    lat_rad = lat * math.pi / 180
    xtile = math.floor((lon + 180) / 360 * math.pow(2, zoom))
    ytile = math.floor((1 - math.log(math.tan(lat_rad) + 1 / math.cos(lat_rad)) / math.pi) / 2 * math.pow(2, zoom))
    return (xtile, ytile)

lat, lon, zoom = 49.795845, 19.096194, 17
print("OSM Wiki formula:", osm_deg2num(lat, lon, zoom))
print("Our formula:     ", our_lat_lon_to_tile(lat, lon, zoom))
