const CACHE_NAME = 'ultra-trekking-v1780059392';
const ASSETS = [
    './',
    './index.html',
    './manifest.json',
    './icon-192.svg',
    './icon-512.svg',
    './wyrypa75km.gpx'
];

self.addEventListener('install', event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            const requests = ASSETS.map(url => new Request(url, { cache: 'reload' }));
            return cache.addAll(requests);
        })
    );
});

self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;
    
    if (event.request.url.includes('tile.opentopomap.org')) {
        const normalizedUrl = event.request.url.replace(/https?:\/\/[abc]\.tile\.opentopomap\.org/, 'https://a.tile.opentopomap.org');
        event.respondWith(
            caches.open('ultra-tiles-v1').then(cache => {
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
                        const zxy = parts.slice(1).join('/');
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

    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});

self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(keys => {
            return Promise.all(keys
                .filter(key => key !== CACHE_NAME && key !== 'ultra-tiles-v1')
                .map(key => caches.delete(key))
            );
        }).then(() => self.clients.claim())
    );
});
