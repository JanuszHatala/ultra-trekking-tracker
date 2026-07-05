// GpsTrackingService.js
// Handles geolocation watch, throttling, and GPX snapping

import { Geolocation } from '@capacitor/geolocation';

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

  static async startTracking(gpxPoints, intervalMs, onUpdate, onError) {
    if (this.watcherId !== null) {
      await this.stopTracking();
    }
    
    try {
      const permStatus = await Geolocation.checkPermissions();
      if (permStatus.location !== 'granted') {
        const req = await Geolocation.requestPermissions();
        if (req.location !== 'granted') {
          throw new Error("Location permission not granted");
        }
      }
    } catch (e) {
      console.warn("Could not check/request permissions. Proceeding anyway.", e);
    }

    try {
      this.watcherId = await Geolocation.watchPosition(
        { enableHighAccuracy: true, timeout: 10000, maximumAge: 5000 },
        (pos, err) => {
          if (err) {
            if (onError) onError(err);
            return;
          }
          if (!pos) return;
          
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
        }
      );
    } catch (err) {
      if (onError) onError(err);
    }
  }

  static async stopTracking() {
    if (this.watcherId !== null) {
      try {
        await Geolocation.clearWatch({ id: this.watcherId });
      } catch (e) {
        console.warn("Error clearing watch", e);
      }
      this.watcherId = null;
      this.lastUpdateTime = 0;
    }
  }
}
