const APP_CACHE = 'ultra-trekking-app-v2';
const TILE_CACHE = 'ultra-tiles-v2';

self.addEventListener('install', event => {
    self.skipWaiting();
});

self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;
    
    // Offline map tile interceptor
    if (event.request.url.includes('tile.opentopomap.org')) {
        const normalizedUrl = event.request.url.replace(/https?:\/\/[abc]\.tile\.opentopomap\.org/, 'https://a.tile.opentopomap.org');
        event.respondWith(
            caches.open(TILE_CACHE).then(cache => {
                return cache.match(normalizedUrl, { ignoreVary: true, ignoreSearch: true }).then(response => {
                    return response || fetch(event.request).then(fetchResponse => {
                        if (fetchResponse.ok) {
                            const responseClone = fetchResponse.clone();
                            cache.put(normalizedUrl, responseClone);
                        }
                        return fetchResponse;
                    }).catch(() => {
                        // Offline fallback: return a diagnostic SVG tile
                        const urlObj = new URL(normalizedUrl);
                        const parts = urlObj.pathname.split('/');
                        const zxy = parts.slice(1).join('/'); // 'z/x/y.png'
                        const svg = `<svg xmlns="http://www.w3.org/2000/svg" width="256" height="256" style="background:rgba(239, 68, 68, 0.5); border: 1px solid red;">
                            <text x="10" y="128" fill="black" font-family="sans-serif" font-size="16" font-weight="bold">${zxy}</text>
                        </svg>`;
                        return new Response(svg, {
                            headers: { 'Content-Type': 'image/svg+xml', 'Access-Control-Allow-Origin': '*' }
                        });
                    });
                });
            })
        );
        return;
    }

    // Default fetch for other assets (network first, fallback to cache if available, but for now we rely on Vite's caching mostly)
    // We can add PWA offline support for the app itself later if needed, but for now, focus on maps.
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(keys
                .filter(key => key !== APP_CACHE && key !== TILE_CACHE)
                .map(key => caches.delete(key))
            );
        }).then(() => self.clients.claim())
    );
});
