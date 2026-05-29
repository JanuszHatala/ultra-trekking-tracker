const CACHE_NAME = 'ultra-trekking-v1780052403';
const ASSETS = [
    './',
    './index.html',
    './manifest.json',
    './icon-192.svg',
    './icon-512.svg',
    './wyrypa75km.gpx',
    'https://cdn.tailwindcss.com',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.7.0/gpx.min.js'
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
