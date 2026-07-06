import packageJson from '../package.json';
import React, { useState, useEffect, useRef } from 'react';
import { GpsEngine } from './services/GpsEngine';
import { StorageEngine } from './services/StorageEngine';
import { DataTable } from './components/DataTable';
import { RichTabRenderer } from './components/RichTabRenderer';
import { MapRenderer } from './components/MapRenderer';
import { Overview } from './components/Overview';
import { Tests } from './components/Tests';
import { Training } from './components/Training';

function App() {
  const [routesList, setRoutesList] = useState([]);
  const [routeId, setRouteId] = useState(null);
  const [dataset, setDataset] = useState(null);
  const [gpxPoints, setGpxPoints] = useState([]);
  const [checkpoints, setCheckpoints] = useState([]);
  const [activeTab, setActiveTab] = useState('overview');
  const [loading, setLoading] = useState(true);
  const [lang, setLang] = useState(() => localStorage.getItem('ultra_lang') || 'pl');
  useEffect(() => {
    localStorage.setItem('ultra_lang', lang);
  }, [lang]);
  const [hoveredSection, setHoveredSection] = useState(null);
  const [selectedSection, setSelectedSection] = useState(null);
  const [profileHoverPoint, setProfileHoverPoint] = useState(null);
  const [mapVisible, setMapVisible] = useState(true);
  const [autoOpenDetails, setAutoOpenDetails] = useState(window.innerWidth >= 768);

  const [gpsState, setGpsState] = useState({ active: false, lat: null, lon: null, accuracy: null, km: 0, offRoute: false, timestamp: 0 });
  const [gpsInterval, setGpsInterval] = useState(() => parseInt(localStorage.getItem('ultra_gps_interval')) || 15000);

  let currentGpsSection = null;
  if (gpsState && gpsState.active && gpsState.lat !== null && checkpoints.length > 0) {
      let activeKm = gpsState.km || 0;
      for (let i = 0; i < checkpoints.length - 1; i++) {
         if (activeKm >= checkpoints[i].km && activeKm <= checkpoints[i+1].km) {
             currentGpsSection = checkpoints[i+1];
             break;
         }
      }
      if (!currentGpsSection) currentGpsSection = checkpoints[checkpoints.length - 1];
  }

  const activeSection = selectedSection || hoveredSection || currentGpsSection;

  // Resizer state
  const [leftWidth, setLeftWidth] = useState(45); // percentage
  const resizerRef = useRef(null);

  // Default window settings
  const [minWindow, setMinWindow] = useState(5);
  const [maxWindow, setMaxWindow] = useState(10);

  // Load route catalog once on mount
  useEffect(() => {
    fetch(`${import.meta.env.BASE_URL}routes.json`)
      .then(r => r.json())
      .then(catalog => {
        setRoutesList(catalog.routes);
        
        // Determine initial route: query parameter -> localStorage -> default 'msb-134k'
        const searchParams = new URLSearchParams(window.location.search);
        const initialId = searchParams.get('route') || localStorage.getItem('ultra_last_route_id') || 'msb-134k';
        
        // If query param is missing, set it so the address bar reflects the actual route loaded
        if (!searchParams.has('route')) {
          const url = new URL(window.location.href);
          url.searchParams.set('route', initialId);
          window.history.replaceState({}, '', url.toString());
        }

        setRouteId(initialId);
      })
      .catch(err => {
        console.error('Failed to load routes catalog:', err);
        setLoading(false);
      });
  }, []);

  // Fetch dataset and GPX track when routeId changes
  useEffect(() => {
    if (routesList.length === 0 || !routeId) return;

    const routeConfig = routesList.find(r => r.id === routeId);
    if (!routeConfig) {
      console.error('Route not found in catalog:', routeId);
      setLoading(false);
      return;
    }

    setLoading(true);
    const [datasetPath, gpxPath] = routeConfig.files;

    Promise.all([
      fetch(`${import.meta.env.BASE_URL}${datasetPath}`).then(r => r.json()),
      fetch(`${import.meta.env.BASE_URL}${gpxPath}`).then(r => r.text())
    ])
      .then(([ds, gpxText]) => {
        setDataset(ds);
        const points = GpsEngine.parseGpx(gpxText);
        setGpxPoints(points);
        
        // Reset navigation / hover states on route change to prevent visual mismatch
        setSelectedSection(null);
        setHoveredSection(null);
        setProfileHoverPoint(null);
      })
      .catch(err => {
        console.error('Error loading route data:', err);
      })
      .finally(() => {
        setLoading(false);
      });
  }, [routeId, routesList]);

  const handleRouteChange = (newRouteId) => {
    setRouteId(newRouteId);
    localStorage.setItem('ultra_last_route_id', newRouteId);
    
    // Update address bar dynamically
    const url = new URL(window.location.href);
    url.searchParams.set('route', newRouteId);
    window.history.pushState({}, '', url.toString());
  };

  useEffect(() => {
    if (gpxPoints.length === 0 || !routeId) return;

    const processCheckpoints = async () => {
      setLoading(true);
      const cacheKey = StorageEngine.getCacheKey(routeId, minWindow, maxWindow);
      
      let cached = await StorageEngine.getCheckpoints(cacheKey);
      if (cached) {
        setCheckpoints(cached);
      } else {
        const newCheckpoints = GpsEngine.generateTopologicalCheckpoints(gpxPoints, minWindow, maxWindow);
        setCheckpoints(newCheckpoints);
        await StorageEngine.cacheCheckpoints(cacheKey, newCheckpoints);
      }
      setLoading(false);
    };

    processCheckpoints();
  }, [gpxPoints, routeId, minWindow, maxWindow]);

  const toggleLanguage = () => {
    setLang(prev => prev === 'en' ? 'pl' : 'en');
  };

  // Resizer logic
  const handleDragStart = (e) => {
    if (e.type === 'mousedown') {
      e.preventDefault();
      document.addEventListener('mousemove', handleDragMove);
      document.addEventListener('mouseup', handleDragEnd);
    } else if (e.type === 'touchstart') {
      document.addEventListener('touchmove', handleDragMove, { passive: false });
      document.addEventListener('touchend', handleDragEnd);
    }
  };

  const handleDragMove = (e) => {
    if (e.type === 'touchmove') e.preventDefault();
    const clientX = e.type.includes('touch') ? e.touches[0].clientX : e.clientX;
    const clientY = e.type.includes('touch') ? e.touches[0].clientY : e.clientY;
    
    if (window.innerWidth >= 768) {
      const newWidth = (clientX / window.innerWidth) * 100;
      if (newWidth > 20 && newWidth < 80) setLeftWidth(newWidth);
    } else {
      const newHeight = (clientY / window.innerHeight) * 100;
      if (newHeight > 20 && newHeight < 80) setLeftWidth(newHeight);
    }
  };

  const handleDragEnd = () => {
    document.removeEventListener('mousemove', handleDragMove);
    document.removeEventListener('mouseup', handleDragEnd);
    document.removeEventListener('touchmove', handleDragMove);
    document.removeEventListener('touchend', handleDragEnd);
  };

  if (loading && !dataset) {
    return <div className="min-h-screen flex items-center justify-center text-lime-400 bg-slate-900">Loading Wyrypa Engine...</div>;
  }

  const title = dataset ? dataset[`title_${lang}`] || dataset.title_en : 'Wyrypa V2';
  const subtitle = dataset ? dataset[`subtitle_${lang}`] || dataset.subtitle_en : '';
  const version = `v${packageJson.version}`;

  return (
    <div className="bg-slate-900 text-slate-200 font-sans antialiased h-[100dvh] w-full overflow-hidden flex flex-col md:flex-row">
      
      {/* Map Section */}
      <div 
        id="map-container" 
        className={`md:h-screen flex-shrink-0 z-0 relative transition-none md:transition-all duration-300 ${!mapVisible ? 'h-0 w-0 hidden md:block md:w-0' : 'w-full md:w-auto'}`}
        style={{ 
          width: mapVisible && window.innerWidth >= 768 ? `${leftWidth}%` : '100%',
          height: mapVisible && window.innerWidth < 768 ? `${leftWidth}vh` : undefined
        }}
      >
        <MapRenderer 
           gpxPoints={gpxPoints} 
           checkpoints={checkpoints} 
           actionTimeline={dataset?.actionTimeline}
           activeSection={activeSection}
           setSelectedSection={setSelectedSection}
           profileHoverPoint={profileHoverPoint}
           mapVisible={mapVisible}
           setMapVisible={setMapVisible}
           autoOpenDetails={autoOpenDetails}
           gpsState={gpsState}
           setGpsState={setGpsState}
           gpsInterval={gpsInterval}
           lang={lang} 
        />
      </div>

      {/* Resizer */}
      {mapVisible && (
        <div 
          id="resizer" 
          ref={resizerRef}
          onMouseDown={handleDragStart}
          onTouchStart={handleDragStart}
          className="bg-slate-700 hover:bg-lime-500 flex items-center justify-center cursor-row-resize md:cursor-col-resize h-4 w-full md:h-full md:w-3 z-50 transition-colors flex-shrink-0 border-y border-slate-800 md:border-y-0 md:border-x flex"
        >
          <div className="bg-slate-400 w-8 h-1 rounded md:h-8 md:w-1 pointer-events-none"></div>
        </div>
      )}

      {/* Right Panel */}
      <div 
        id="content-container" 
        className="flex-1 flex flex-col min-w-0 bg-slate-900 z-10 shadow-[-10px_0_15px_-3px_rgba(0,0,0,0.5)] md:h-screen overflow-hidden transition-none md:transition-all duration-300"
        style={{ width: mapVisible ? (window.innerWidth >= 768 ? `${100 - leftWidth}%` : '100%') : '100%' }}
      >
        
        {/* Header & Tabs */}
        <div className="p-3 md:p-6 pb-0 flex-shrink-0 bg-slate-900 z-20 border-b border-slate-700">
          <div className="flex flex-col sm:flex-row sm:justify-between sm:items-center gap-3 w-full pb-3 sm:pb-0">
            <div className="flex items-center gap-3">
              <div>
                <h1 className="text-xl sm:text-2xl md:text-3xl font-bold text-transparent bg-clip-text bg-gradient-to-r from-lime-400 to-cyan-400 mb-0.5">
                  Wyrypa Tracker <span style={{ fontSize: '0.5em', color: 'white' }}>{version}</span>
                </h1>
                <p className="text-[10px] md:text-xs text-slate-400 italic mb-0">
                  {title} - {subtitle}
                </p>
              </div>
              {!mapVisible && (
                <button 
                  onClick={() => setMapVisible(true)}
                  className="bg-slate-800 text-lime-400 border border-lime-500/30 px-3 py-1 rounded shadow text-xs font-bold hover:bg-slate-700 transition-colors"
                >
                  {lang === 'en' ? 'Show Map' : 'Pokaż Mapę'}
                </button>
              )}
            </div>
            
            <div className="flex items-center justify-between sm:justify-end gap-2">
              {/* Route Selector Dropdown */}
              {routesList.length > 0 && (
                <select
                  value={routeId || 'msb-134k'}
                  onChange={(e) => handleRouteChange(e.target.value)}
                  className="bg-slate-800 text-slate-200 border border-slate-700 rounded px-2.5 py-1 text-xs md:text-sm font-semibold focus:outline-none focus:border-lime-400 cursor-pointer"
                >
                  {routesList.map(r => (
                    <option key={r.id} value={r.id}>
                      {r.name}
                    </option>
                  ))}
                </select>
              )}

              <button onClick={toggleLanguage} className="h-[28px] flex items-center bg-slate-800 rounded shadow border border-slate-600 font-bold text-[10px] sm:text-xs overflow-hidden cursor-pointer">
                <span className={`px-2 md:px-3 h-full flex items-center justify-center transition-colors ${lang === 'en' ? 'bg-lime-500 text-slate-900' : 'text-slate-400 hover:text-slate-200'}`}>EN</span>
                <span className={`px-2 md:px-3 h-full flex items-center justify-center transition-colors ${lang === 'pl' ? 'bg-lime-500 text-slate-900' : 'text-slate-400 hover:text-slate-200'}`}>PL</span>
              </button>
            </div>
          </div>
            
          {/* Tab Bar */}
          <div className="flex border-b border-slate-700 mt-2 md:mt-4 mb-0 overflow-x-auto hide-scrollbar text-sm md:text-base">
            <button onClick={() => setActiveTab('overview')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'overview' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Overview' : 'Przegląd'}
            </button>
            <button onClick={() => setActiveTab('table')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'table' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Data Table' : 'Tabela'}
            </button>
            <button onClick={() => setActiveTab('tactics')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'tactics' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Tactics' : 'Taktyka'}
            </button>
            <button onClick={() => setActiveTab('inventory')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'inventory' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Inventory' : 'Inwentarz'}
            </button>
            <button onClick={() => setActiveTab('schedule')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'schedule' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Schedule' : 'Harmonogram'}
            </button>
            <button onClick={() => setActiveTab('tests')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'tests' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Tests' : 'Testy'}
            </button>
            <button onClick={() => setActiveTab('training')} className={`px-3 md:px-4 py-1.5 md:py-2 border-b-2 transition-colors whitespace-nowrap ${activeTab === 'training' ? 'border-lime-400 text-lime-400 font-bold' : 'border-transparent text-slate-500 hover:text-slate-300 font-medium'}`}>
              {lang === 'en' ? 'Training' : 'Trening'}
            </button>
          </div>
        </div>

        <div className="flex-1 overflow-y-auto p-3 md:p-6 bg-slate-900">
          {activeTab === 'overview' && (
            <Overview 
              dataset={dataset} 
              gpxPoints={gpxPoints} 
              checkpoints={checkpoints} 
              lang={lang} 
              hoverPoint={activeSection} 
              selectedSection={selectedSection}
              onHoverPoint={setProfileHoverPoint}
              autoOpenDetails={autoOpenDetails}
              setAutoOpenDetails={setAutoOpenDetails}
              gpsState={gpsState}
              gpsInterval={gpsInterval}
              setGpsInterval={setGpsInterval}
            />
          )}

          {activeTab === 'table' && (
             <DataTable 
               checkpoints={checkpoints} 
               actionTimeline={dataset?.actionTimeline} 
               minWindow={minWindow} 
               maxWindow={maxWindow}
               setMinWindow={setMinWindow}
               lang={lang}
               activeSection={activeSection}
               selectedSection={selectedSection}
               setSelectedSection={setSelectedSection}
               setHoveredSection={setHoveredSection}
               mapVisible={mapVisible}
               setMapVisible={setMapVisible}
             />
          )}

          {activeTab === 'tactics' && (
             <RichTabRenderer data={dataset?.tactics} type="tactics" lang={lang} />
          )}

          {activeTab === 'inventory' && (
            <RichTabRenderer data={dataset?.inventory} type="inventory" lang={lang} />
          )}

          {activeTab === 'schedule' && (
            <RichTabRenderer data={dataset?.schedule} type="schedule" lang={lang} />
          )}

          {activeTab === 'tests' && (
             <Tests data={dataset?.tests} lang={lang} />
          )}

          {activeTab === 'training' && (
             <Training data={dataset?.training} lang={lang} />
          )}
        </div>
      </div>
    </div>
  );
}

export default App;
