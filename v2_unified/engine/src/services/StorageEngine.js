import localforage from 'localforage';

localforage.config({
  name: 'WyrypaV2',
  storeName: 'route_cache'
});

export const StorageEngine = {
  /**
   * Generates a cache key based on route ID and parameters
   */
  getCacheKey: (routeId, minWindow, maxWindow) => {
    return `v5_${routeId}_${minWindow}_${maxWindow}`;
  },

  /**
   * Saves calculated checkpoints to IndexedDB
   */
  cacheCheckpoints: async (cacheKey, checkpoints) => {
    try {
      await localforage.clear(); // Clear old cached routes
      await localforage.setItem(cacheKey, checkpoints);
      console.log(`[StorageEngine] Cleared old caches and cached checkpoints under ${cacheKey}`);
    } catch (err) {
      console.error('[StorageEngine] Error caching checkpoints:', err);
    }
  },

  /**
   * Retrieves cached checkpoints if they exist
   */
  getCheckpoints: async (cacheKey) => {
    try {
      const checkpoints = await localforage.getItem(cacheKey);
      if (checkpoints) {
        console.log(`[StorageEngine] Loaded checkpoints from cache ${cacheKey}`);
        return checkpoints;
      }
    } catch (err) {
      console.error('[StorageEngine] Error reading cache:', err);
    }
    return null;
  }
};
