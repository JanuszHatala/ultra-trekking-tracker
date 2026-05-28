const CACHE_NAME = 'ultra-trekking-v1779985392';
const ASSETS = [
    './',
    './index.html',
    './Ultra100_standalone.html',
    './manifest.json',
    './icon-192.svg',
    './icon-512.svg',
    './wyrypa-100km.gpx',
    'https://cdn.tailwindcss.com',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.css',
    'https://unpkg.com/leaflet@1.9.4/dist/leaflet.js',
    'https://cdnjs.cloudflare.com/ajax/libs/leaflet-gpx/1.7.0/gpx.min.js'
];

self.addEventListener('install', event => {
    self.skipWaiting();
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            return cache.addAll(ASSETS);
        })
    );
});

self.addEventListener('fetch', event => {
    if (event.request.method !== 'GET') return;
    
    if (event.request.url.includes('tile.opentopomap.org')) {
        const normalizedUrl = event.request.url.replace(/https:\/\/[abc]\.tile\.opentopomap\.org/, 'https://a.tile.opentopomap.org');
        event.respondWith(
            caches.match(normalizedUrl).then(response => {
                return response || fetch(event.request).then(fetchResponse => {
                    if (fetchResponse.ok) {
                        const responseClone = fetchResponse.clone();
                        caches.open('ultra-tiles-v1').then(cache => {
                            cache.put(normalizedUrl, responseClone);
                        });
                    }
                    return fetchResponse;
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
