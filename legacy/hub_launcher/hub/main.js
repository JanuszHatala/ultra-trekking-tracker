import { Filesystem, Directory, Encoding } from '@capacitor/filesystem';
import { Capacitor } from '@capacitor/core';

const REPO_URL = 'https://januszhatala.github.io/ultra-trekking-tracker';
let onlineRoutes = [];
let localRoutes = {};

async function log(msg) {
    document.getElementById('status').innerText = msg;
}

async function init() {
    log('Checking local routes...');
    // Load local routes metadata
    try {
        const res = await Filesystem.readFile({
            path: 'routes_meta.json',
            directory: Directory.Data,
            encoding: Encoding.UTF8
        });
        localRoutes = JSON.parse(res.data);
    } catch (e) {
        localRoutes = {};
    }

    log('Fetching online routes...');
    try {
        const res = await fetch(`${REPO_URL}/routes.json?t=${Date.now()}`);
        const data = await res.json();
        onlineRoutes = data.routes;
        log('Online routes fetched successfully.');
    } catch (e) {
        log('Offline mode. Showing installed routes only.');
    }

    renderUI();
}

function renderUI() {
    const container = document.getElementById('routes-container');
    container.innerHTML = '';

    const lastUrl = localStorage.getItem('wyrypa_last_route_url');
    if (lastUrl && Capacitor.isNativePlatform()) {
        const resumeCard = document.createElement('div');
        resumeCard.className = 'route-card';
        resumeCard.style.borderColor = '#a3e635';
        resumeCard.innerHTML = `
            <div class="route-title" style="color: #a3e635;">Active Route Found</div>
            <div class="route-meta">You were previously navigating a route.</div>
            <div class="btn-group">
                <button class="btn-launch" onclick="window.location.href='${lastUrl}'">Resume Navigation</button>
                <button class="btn-disabled" style="cursor:pointer;" onclick="localStorage.removeItem('wyrypa_last_route_url'); renderUI();">Clear</button>
            </div>
        `;
        container.appendChild(resumeCard);
    }

    // Merge online and local to show everything available
    const allRouteIds = new Set([...onlineRoutes.map(r => r.id), ...Object.keys(localRoutes)]);

    allRouteIds.forEach(id => {
        const onlineData = onlineRoutes.find(r => r.id === id);
        const localData = localRoutes[id];
        
        const card = document.createElement('div');
        card.className = 'route-card';

        const name = onlineData ? onlineData.name : localData.name;
        const onlineVer = onlineData ? onlineData.version : null;
        const localVer = localData ? localData.version : null;

        let statusText = '';
        if (localVer && onlineVer && localVer !== onlineVer) statusText = `(Update available: v${onlineVer})`;
        else if (localVer) statusText = `(Installed v${localVer})`;
        else statusText = `(Not installed - v${onlineVer})`;

        let html = `
            <div class="route-title">${name}</div>
            <div class="route-meta">Status: ${statusText}</div>
            <div class="btn-group">
        `;

        if (localVer) {
            html += `<button class="btn-launch" onclick="launchRoute('${id}')">Launch</button>`;
        }

        if (onlineData) {
            if (!localVer) {
                html += `<button class="btn-download" onclick="downloadRoute('${id}')">Download</button>`;
            } else if (localVer !== onlineVer) {
                html += `<button class="btn-update" onclick="downloadRoute('${id}')">Update</button>`;
            }
        }

        html += `</div>`;
        card.innerHTML = html;
        container.appendChild(card);
    });
}

window.downloadRoute = async function(id) {
    const route = onlineRoutes.find(r => r.id === id);
    if (!route) return;

    log(`Downloading ${route.name}...`);
    try {
        // Fetch all files
        for (let i = 0; i < route.files.length; i++) {
            const filePath = route.files[i];
            log(`Downloading (${i+1}/${route.files.length}): ${filePath}`);
            
            const res = await fetch(`${REPO_URL}/${filePath}?t=${Date.now()}`);
            const text = await res.text();

            // Ensure directories exist (simple hack for 1-level deep)
            const dirParts = filePath.split('/');
            if (dirParts.length > 1) {
                const dir = dirParts[0];
                try {
                    await Filesystem.mkdir({
                        path: `routes/${dir}`,
                        directory: Directory.Data,
                        recursive: true
                    });
                } catch (e) {} // ignore if exists
            }

            // Save to device
            await Filesystem.writeFile({
                path: `routes/${filePath}`,
                data: text,
                directory: Directory.Data,
                encoding: Encoding.UTF8
            });
        }

        // Update local metadata
        localRoutes[id] = { name: route.name, version: route.version, entryFile: `routes/${route.files[0]}` };
        await Filesystem.writeFile({
            path: 'routes_meta.json',
            data: JSON.stringify(localRoutes),
            directory: Directory.Data,
            encoding: Encoding.UTF8
        });

        log('Download complete!');
        renderUI();
    } catch (e) {
        log(`Download failed: ${e.message}`);
    }
};

window.launchRoute = async function(id) {
    const localData = localRoutes[id];
    if (!localData) return;

    if (Capacitor.isNativePlatform()) {
        try {
            const uriResult = await Filesystem.getUri({
                path: localData.entryFile,
                directory: Directory.Data
            });
            const url = Capacitor.convertFileSrc(uriResult.uri);
            localStorage.setItem('wyrypa_last_route_url', url);
            window.location.href = url;
        } catch (e) {
            log('Failed to launch route.');
        }
    } else {
        log('Cannot launch local file in web browser. Compile to Android to test.');
    }
};

init();
