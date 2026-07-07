import { KeepAwake } from '@capacitor-community/keep-awake';

export class MapOfflineService {
  static CACHE_NAME = 'ultra-tiles-v2';
  static DOWNLOADED_FLAG = 'ultra_map_downloaded_v2';

  static isDownloading = false;
  static currentProgress = 0;
  static shouldCancel = false;
  static listeners = new Set();

  static subscribe(listener) {
    this.listeners.add(listener);
    listener({ isDownloading: this.isDownloading, progress: this.currentProgress });
    return () => this.listeners.delete(listener);
  }

  static notify() {
    this.listeners.forEach(l => l({ isDownloading: this.isDownloading, progress: this.currentProgress }));
  }

  static cancelDownload() {
    this.shouldCancel = true;
  }

  static latLonToTile(lat, lon, zoom) {
    const latRad = lat * Math.PI / 180;
    let xtile = Math.floor((lon + 180) / 360 * Math.pow(2, zoom));
    let ytile = Math.floor((1 - Math.log(Math.tan(latRad) + 1 / Math.cos(latRad)) / Math.PI) / 2 * Math.pow(2, zoom));
    return { x: xtile, y: ytile };
  }

  static async isDownloaded(routeId = null) {
    if (routeId) {
      return localStorage.getItem(`${this.DOWNLOADED_FLAG}_${routeId}`) === '1';
    }
    // Fallback if no route specified (legacy)
    return localStorage.getItem(this.DOWNLOADED_FLAG) === '1';
  }

  static async getCacheStats() {
    try {
      const cache = await caches.open(this.CACHE_NAME);
      const keys = await cache.keys();
      const stats = { total: keys.length, zooms: {} };
      keys.forEach(req => {
        // Expected URL: https://a.tile.opentopomap.org/11/1143/698.png
        const match = req.url.match(/\/(\d+)\/\d+\/\d+\.png$/);
        if (match) {
          const z = match[1];
          stats.zooms[`z${z}`] = (stats.zooms[`z${z}`] || 0) + 1;
        }
      });
      return stats;
    } catch (e) {
      return { total: 0, zooms: {} };
    }
  }

  static async deleteMap() {
    try {
      await caches.delete(this.CACHE_NAME);
      // Remove all download flags from localStorage
      for (let i = 0; i < localStorage.length; i++) {
        const key = localStorage.key(i);
        if (key && key.startsWith(this.DOWNLOADED_FLAG)) {
          localStorage.removeItem(key);
        }
      }
      return true;
    } catch (e) {
      console.error('Failed to delete map cache', e);
      return false;
    }
  }

  static async downloadOfflineTiles(gpxPoints, onProgress) {
    if (this.isDownloading) return { success: false, message: 'Already downloading' };
    
    if (!gpxPoints || gpxPoints.length === 0) {
      throw new Error("No GPX points provided");
    }

    try {
      await KeepAwake.keepAwake();
    } catch (e) { console.warn('KeepAwake error', e); }

    try {
      this.isDownloading = true;
      this.shouldCancel = false;
      this.currentProgress = 0;
      this.notify();

      const urls = [];
      const tileSet = new Set();
      const zooms = [11, 12, 13, 14, 15, 16, 17];

      zooms.forEach(zoom => {
        gpxPoints.forEach(pt => {
          const centerTile = this.latLonToTile(pt.lat, pt.lon, zoom);
          
          // Dynamic buffer to ensure offline availability
          let buf = 1;
          if (zoom === 14 || zoom === 15) {
            buf = 2;
          } else if (zoom === 16) {
            buf = 3;
          } else if (zoom === 17) {
            buf = 4;
          }

          for (let dx = -buf; dx <= buf; dx++) {
            for (let dy = -buf; dy <= buf; dy++) {
              const x = centerTile.x + dx;
              const y = centerTile.y + dy;
              const tileKey = `${zoom}_${x}_${y}`;
              if (!tileSet.has(tileKey)) {
                tileSet.add(tileKey);
                // We cache OpenTopoMap specifically (only 'a' to save space, SW will route b/c to a's cache)
                urls.push(`https://a.tile.opentopomap.org/${zoom}/${x}/${y}.png`);
              }
            }
          }
        });
      });

      const total = urls.length;
      const cache = await caches.open(this.CACHE_NAME);
      
      // Pre-check what is already cached to show correct resume progress
      const keys = await cache.keys();
      const cachedUrls = new Set(keys.map(k => k.url));
      
      let alreadyCached = 0;
      urls.forEach(url => {
        if (cachedUrls.has(url)) alreadyCached++;
      });

      let succeeded = alreadyCached;
      let failed = 0;

      // Trigger initial progress if resuming
      if (total > 0) {
        this.currentProgress = Math.round((succeeded / total) * 100);
        if (onProgress) onProgress(this.currentProgress);
        this.notify();
      }

      for (let i = 0; i < total; i++) {
        if (this.shouldCancel) {
          this.isDownloading = false;
          this.notify();
          return { success: false, message: 'Download cancelled' };
        }

        const url = urls[i];
        if (cachedUrls.has(url)) {
           continue; // Skip already cached from pre-check
        }
        try {
          const cachedRes = await cache.match(new Request(url), { ignoreVary: true, ignoreSearch: true });
          if (!cachedRes) {
            let attempts = 0;
            let resOk = false;
            let res = null;
            while (attempts < 3 && !resOk) {
              try {
                res = await fetch(url, { mode: 'cors', cache: 'reload' });
                if (res.ok) {
                  resOk = true;
                } else if (res.status === 429) {
                  attempts++;
                  await new Promise(resolve => setTimeout(resolve, 1000 * attempts));
                } else {
                  attempts++;
                  await new Promise(resolve => setTimeout(resolve, 300));
                }
              } catch (err) {
                attempts++;
                await new Promise(resolve => setTimeout(resolve, 300));
              }
            }
            if (resOk && res) {
              await cache.put(url, res.clone());
              succeeded++;
            } else {
              failed++;
              console.warn(`Failed to fetch tile after 3 attempts: ${url}`);
            }
            // Slight delay to be gentle on OpenTopoMap
            await new Promise(resolve => setTimeout(resolve, 50));
          } else {
            succeeded++; // in case it was cached while running
          }
        } catch (e) {
          failed++;
          console.warn("Failed to fetch tile: " + url, e);
        }
        
        
        this.currentProgress = Math.round(((succeeded + failed) / total) * 100);
        if (onProgress) onProgress(this.currentProgress);
        this.notify();
      }

      this.isDownloading = false;
      this.notify();

      if (failed === 0) {
        localStorage.setItem(this.DOWNLOADED_FLAG, '1');
        return { success: true, message: 'All tiles downloaded' };
      } else {
        return { success: false, message: `Failed to download ${failed} tiles`, succeeded, failed, total };
      }
    } finally {
      try {
        await KeepAwake.allowSleep();
      } catch (e) { console.warn('KeepAwake error', e); }
    }
  }
}
