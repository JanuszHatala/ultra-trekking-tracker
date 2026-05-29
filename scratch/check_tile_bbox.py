import math

def num2deg(xtile, ytile, zoom):
  n = 2.0 ** zoom
  lon_deg = xtile / n * 360.0 - 180.0
  lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
  lat_deg = math.degrees(lat_rad)
  return (lat_deg, lon_deg)

zoom = 17
x = 72488
y = 44567

# Bounding box of tile is from (x, y) to (x+1, y+1)
lat_top, lon_left = num2deg(x, y, zoom)
lat_bottom, lon_right = num2deg(x + 1, y + 1, zoom)

print(f"Tile 17/{x}/{y} bounding box:")
print(f"Top-Left:     Lat={lat_top}, Lon={lon_left}")
print(f"Bottom-Right: Lat={lat_bottom}, Lon={lon_right}")

target_lat, target_lon = 49.795845, 19.096194
print(f"\nTarget point: Lat={target_lat}, Lon={target_lon}")

lat_inside = lat_bottom <= target_lat <= lat_top
lon_inside = lon_left <= target_lon <= lon_right

print(f"Lat inside? {lat_inside}")
print(f"Lon inside? {lon_inside}")
