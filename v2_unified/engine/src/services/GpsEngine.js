import gpxParser from 'gpxparser';

// Helper to calculate distance between two lat/lon points using Haversine formula
function getDistance(lat1, lon1, lat2, lon2) {
  const R = 6371; // km
  const dLat = ((lat2 - lat1) * Math.PI) / 180;
  const dLon = ((lon2 - lon1) * Math.PI) / 180;
  const a =
    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
    Math.cos((lat1 * Math.PI) / 180) *
      Math.cos((lat2 * Math.PI) / 180) *
      Math.sin(dLon / 2) *
      Math.sin(dLon / 2);
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
  return R * c;
}

export const GpsEngine = {
  /**
   * Parse raw GPX text and return an array of enriched track points
   */
  parseGpx: (gpxText) => {
    const gpx = new gpxParser();
    gpx.parse(gpxText);
    
    if (!gpx.tracks || gpx.tracks.length === 0) return [];
    
    let totalDist = 0;
    const points = gpx.tracks[0].points;
    const enrichedPoints = [];

    for (let i = 0; i < points.length; i++) {
      const p = points[i];
      if (i > 0) {
        const prev = points[i - 1];
        totalDist += getDistance(prev.lat, prev.lon, p.lat, p.lon);
      }
      enrichedPoints.push({
        lat: p.lat,
        lon: p.lon,
        ele: p.ele,
        dist: totalDist // distance from start in km
      });
    }
    return enrichedPoints;
  },

  /**
   * Applies the Topological Checkpoint Algorithm (Anchored Sliding Window)
   * to chunk the track into logical sections based on peaks/valleys.
   */
  generateTopologicalCheckpoints: (points, minWindowKm = 5, maxWindowKm = 10) => {
    if (!points || points.length === 0) return [];

    const checkpoints = [];
    let lastCpIndex = 0;
    let lastCpDist = 0;
    
    // Add start point
    checkpoints.push({
      id: 0,
      name: 'Start',
      type: 'Start',
      km: 0,
      ele: points[0].ele,
      lat: points[0].lat,
      lon: points[0].lon,
      pointIndex: 0,
      sectionAscent: 0,
      sectionDescent: 0,
      sectionPoints: [points[0]]
    });

    const totalDistance = points[points.length - 1].dist;
    let cpId = 1;

    while (lastCpDist + minWindowKm < totalDistance) {
      const windowStartDist = lastCpDist + minWindowKm;
      const windowEndDist = Math.min(lastCpDist + maxWindowKm, totalDistance);
      
      // Find points in this window
      let windowPoints = [];
      let windowStartIndex = lastCpIndex;
      let windowEndIndex = lastCpIndex;
      
      for (let i = lastCpIndex; i < points.length; i++) {
        if (points[i].dist >= windowStartDist && points[i].dist <= windowEndDist) {
          if (windowPoints.length === 0) windowStartIndex = i;
          windowPoints.push({ ...points[i], index: i });
          windowEndIndex = i;
        } else if (points[i].dist > windowEndDist) {
          break;
        }
      }

      if (windowPoints.length === 0) {
        // Should only happen near the very end
        break;
      }

      // Topological analysis in this window
      let maxElePt = windowPoints[0];
      let minElePt = windowPoints[0];
      const startEle = points[lastCpIndex].ele;

      windowPoints.forEach(pt => {
        if (pt.ele > maxElePt.ele) maxElePt = pt;
        if (pt.ele < minElePt.ele) minElePt = pt;
      });

      const eleVariance = maxElePt.ele - minElePt.ele;
      const deltaUp = maxElePt.ele - startEle;
      const deltaDown = startEle - minElePt.ele;
      
      let selectedPt;
      let cpName = '';

      let cpType = 'Flat';
      if (eleVariance > 40) { // If there is significant topology (>40m variance)
        if (deltaUp > deltaDown) {
          selectedPt = maxElePt;
          cpName = `Section ${cpId} (KM ${lastCpDist.toFixed(1)} - ${selectedPt.dist.toFixed(1)}) (Peak)`;
          cpType = 'Peak';
        } else {
          selectedPt = minElePt;
          cpName = `Section ${cpId} (KM ${lastCpDist.toFixed(1)} - ${selectedPt.dist.toFixed(1)}) (Valley)`;
          cpType = 'Valley';
        }
      } else {
        // Flat terrain fallback -> just take the furthest point in the window
        selectedPt = windowPoints[windowPoints.length - 1];
        cpName = `Section ${cpId} (KM ${lastCpDist.toFixed(1)} - ${selectedPt.dist.toFixed(1)})`;
        cpType = 'Flat';
      }

      // Calculate ascent/descent for this section (from lastCp to selectedPt)
      let sectionAscent = 0;
      let sectionDescent = 0;
      for (let i = lastCpIndex + 1; i <= selectedPt.index; i++) {
        const diff = points[i].ele - points[i-1].ele;
        if (diff > 0) sectionAscent += diff;
        else sectionDescent -= diff;
      }

      checkpoints.push({
        id: cpId++,
        name: cpName,
        type: cpType,
        km: selectedPt.dist,
        ele: selectedPt.ele,
        lat: selectedPt.lat,
        lon: selectedPt.lon,
        pointIndex: selectedPt.index,
        sectionAscent: Math.round(sectionAscent),
        sectionDescent: Math.round(sectionDescent),
        sectionPoints: points.slice(lastCpIndex, selectedPt.index + 1)
      });

      lastCpIndex = selectedPt.index;
      lastCpDist = selectedPt.dist;
    }

    // Add Finish if not exactly at the end
    if (lastCpDist < totalDistance - 0.5) { // If more than 500m to finish
      const endPt = points[points.length - 1];
      let sectionAscent = 0;
      let sectionDescent = 0;
      for (let i = lastCpIndex + 1; i < points.length; i++) {
        const diff = points[i].ele - points[i-1].ele;
        if (diff > 0) sectionAscent += diff;
        else sectionDescent -= diff;
      }
      checkpoints.push({
        id: cpId,
        name: `Finish (KM ${lastCpDist.toFixed(1)} - ${totalDistance.toFixed(1)})`,
        type: 'Finish',
        km: totalDistance,
        ele: endPt.ele,
        lat: endPt.lat,
        lon: endPt.lon,
        pointIndex: points.length - 1,
        sectionAscent: Math.round(sectionAscent),
        sectionDescent: Math.round(sectionDescent),
        sectionPoints: points.slice(lastCpIndex, points.length)
      });
    }

    // Now enrich with ETA math
    return GpsEngine.calculateETAs(checkpoints);
  },

  /**
   * Calculates ETA based on a very basic pace formula (to be refined by user profile later)
   * Base pace: 10 min/km
   * Ascent penalty: +10 min per 100m climb
   * Descent bonus: -2 min per 100m descent
   */
  calculateETAs: (checkpoints) => {
    let elapsedMinutes = 0;
    
    return checkpoints.map((cp, idx) => {
      if (idx === 0) {
        return { ...cp, etaHrs: 0, paceMinKm: 0 };
      }
      const prevCp = checkpoints[idx - 1];
      const dist = cp.km - prevCp.km;
      const ascent = cp.sectionAscent;
      const descent = cp.sectionDescent;
      
      const baseTime = dist * 10; 
      const ascentTime = (ascent / 100) * 10;
      const descentTime = (descent / 100) * -2;
      
      const sectionTime = Math.max(baseTime + ascentTime + descentTime, dist * 5); // cap speed at 5min/km
      elapsedMinutes += sectionTime;
      
      return {
        ...cp,
        etaHrs: elapsedMinutes / 60,
        paceMinKm: sectionTime / dist
      };
    });
  }
};
