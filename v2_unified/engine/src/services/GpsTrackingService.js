// GpsTrackingService.js
// Handles geolocation watch, throttling, and GPX snapping

export class GpsTrackingService {
  static watcherId = null;
  static lastUpdateTime = 0;
  static lastMatchedIndex = null;
  
  // Calculate distance between two lat/lon points using Haversine
  static distanceTo(lat1, lon1, lat2, lon2) {
    const R = 6371e3; // metres
    const p1 = lat1 * Math.PI / 180;
    const p2 = lat2 * Math.PI / 180;
    const dp = (lat2 - lat1) * Math.PI / 180;
    const dl = (lon2 - lon1) * Math.PI / 180;

    const a = Math.sin(dp/2) * Math.sin(dp/2) +
              Math.cos(p1) * Math.cos(p2) *
              Math.sin(dl/2) * Math.sin(dl/2);
    const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
    return R * c;
  }

  static startTracking(gpxPoints, intervalMs, onUpdate, onError) {
    if (this.watcherId !== null) {
      this.stopTracking();
    }
    
    if (!navigator.geolocation) {
      if (onError) onError(new Error("Geolocation is not supported by your browser"));
      return;
    }

    this.watcherId = navigator.geolocation.watchPosition(
      (pos) => {
        const now = Date.now();
        if (this.lastUpdateTime !== 0 && (now - this.lastUpdateTime < intervalMs)) {
          return; // Throttled
        }
        this.lastUpdateTime = now;
        
        const lat = pos.coords.latitude;
        const lon = pos.coords.longitude;
        const accuracy = pos.coords.accuracy;
        
        let minDistanceMetres = Infinity;
        let closestTrackPt = null;
        let closestIdx = -1;
        
        if (gpxPoints && gpxPoints.length > 0) {
          let searchStart = 0;
          let searchEnd = gpxPoints.length - 1;
          let usingRestricted = false;
          
          if (this.lastMatchedIndex !== null) {
              searchStart = Math.max(0, this.lastMatchedIndex - 150);
              searchEnd = Math.min(gpxPoints.length - 1, this.lastMatchedIndex + 600);
              usingRestricted = true;
          }
          
          for (let i = searchStart; i <= searchEnd; i++) {
              const d = this.distanceTo(lat, lon, gpxPoints[i].lat, gpxPoints[i].lon);
              if (d < minDistanceMetres) {
                  minDistanceMetres = d;
                  closestTrackPt = gpxPoints[i];
                  closestIdx = i;
              }
          }
          
          // Fallback to global search if restricted search fails (distance > 200m)
          if (usingRestricted && minDistanceMetres > 200) {
              let globalMinDistance = Infinity;
              let globalClosestPt = null;
              let globalClosestIdx = -1;
              for (let i = 0; i < gpxPoints.length; i++) {
                  const d = this.distanceTo(lat, lon, gpxPoints[i].lat, gpxPoints[i].lon);
                  if (d < globalMinDistance) {
                      globalMinDistance = d;
                      globalClosestPt = gpxPoints[i];
                      globalClosestIdx = i;
                  }
              }
              minDistanceMetres = globalMinDistance;
              closestTrackPt = globalClosestPt;
              closestIdx = globalClosestIdx;
          }
          
          if (closestIdx !== -1) {
              this.lastMatchedIndex = closestIdx;
          }
        }
        
        const isOffRoute = minDistanceMetres > 200;
        const currentKm = closestTrackPt ? closestTrackPt.dist : 0;
        
        if (onUpdate) {
          onUpdate({
            lat,
            lon,
            accuracy,
            km: currentKm,
            offRoute: isOffRoute,
            timestamp: now
          });
        }
      },
      (err) => {
        if (onError) onError(err);
      },
      { enableHighAccuracy: true, timeout: 10000, maximumAge: 5000 }
    );
  }

  static stopTracking() {
    if (this.watcherId !== null) {
      if (navigator.geolocation) {
        navigator.geolocation.clearWatch(this.watcherId);
      }
      this.watcherId = null;
      this.lastUpdateTime = 0;
    }
  }
}
