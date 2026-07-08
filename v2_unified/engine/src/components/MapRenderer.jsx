import React, { useEffect, useState, useRef } from 'react';
import { MapContainer, TileLayer, Polyline, Marker, Popup, useMap, useMapEvents, ZoomControl, Circle, CircleMarker } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import L from 'leaflet';
import { Crosshair, EyeOff, Maximize, Navigation, ZoomIn, X, Expand } from 'lucide-react';
import { GpsTrackingService } from '../services/GpsTrackingService';
import { Geolocation } from '@capacitor/geolocation';

// Create the custom circle marker icon with green border and number
const createNumberedIcon = (number) => {
  return L.divIcon({
    className: 'custom-div-icon',
    html: `
      <div style="
        background-color: #0f172a; 
        border: 2px solid #84cc16; 
        color: #f8fafc; 
        border-radius: 50%; 
        width: 24px; 
        height: 24px; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        font-weight: bold; 
        font-size: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.5);
      ">
        ${number}
      </div>`,
    iconSize: [24, 24],
    iconAnchor: [12, 12],
  });
};

const createHoverIcon = () => {
  return L.divIcon({
    className: 'hover-div-icon',
    html: `
      <div style="
        background-color: rgba(239, 68, 68, 0.2); 
        border: 3px solid #ef4444; 
        border-radius: 50%; 
        width: 36px; 
        height: 36px; 
        box-shadow: 0 0 15px rgba(239, 68, 68, 0.8);
        display: flex;
        align-items: center;
        justify-content: center;
        animation: pulse 2s infinite;
      ">
        <div style="width: 8px; height: 8px; background: #ef4444; border-radius: 50%;"></div>
      </div>
      <style>
        @keyframes pulse {
          0% { transform: scale(0.9); opacity: 1; }
          50% { transform: scale(1.1); opacity: 0.8; }
          100% { transform: scale(0.9); opacity: 1; }
        }
      </style>`,
    iconSize: [36, 36],
    iconAnchor: [18, 18]
  });
};

const profileHoverIcon = L.divIcon({
  className: 'profile-hover-icon',
  html: '<div style="background-color: #ec4899; border: 2px solid white; border-radius: 50%; width: 12px; height: 12px; box-shadow: 0 0 8px rgba(236, 72, 153, 0.8);"></div>',
  iconSize: [12, 12],
  iconAnchor: [6, 6]
});

// Component to handle dynamic map centering on hover/select
function MapHoverSync({ activeSection }) {
  const map = useMap();
  useEffect(() => {
    if (activeSection && activeSection.lat) {
      if (activeSection.sectionPoints && activeSection.sectionPoints.length > 0) {
        const bounds = L.latLngBounds(activeSection.sectionPoints.map(p => [p.lat, p.lon]));
        const mapBounds = map.getBounds();
        
        // Only adjust if the section is not fully visible
        if (!mapBounds.contains(bounds)) {
          const targetZoom = map.getBoundsZoom(bounds, false, [40, 40]);
          const currentZoom = map.getZoom();
          
          if (currentZoom <= targetZoom) {
            // It fits at current zoom, just pan to center
            map.panTo(bounds.getCenter(), { animate: true, duration: 0.3 });
          } else {
            // Too large for current zoom, fit bounds
            map.fitBounds(bounds, { padding: [40, 40], maxZoom: 15, animate: true });
          }
        }
      } else {
        const latlng = L.latLng(activeSection.lat, activeSection.lon);
        if (!map.getBounds().contains(latlng)) {
          map.setView(latlng, Math.max(map.getZoom(), 14), {
            animate: true,
            duration: 0.2
          });
        }
      }
    }
  }, [activeSection, map]);
  return null;
}

// Component to handle dynamic map centering for profile hovering
function ProfileHoverSync({ profileHoverPoint }) {
  const map = useMap();
  useEffect(() => {
    if (profileHoverPoint && profileHoverPoint.lat) {
      const latlng = L.latLng(profileHoverPoint.lat, profileHoverPoint.lon);
      if (!map.getBounds().contains(latlng)) {
        map.panTo(latlng, { animate: true, duration: 0.25 });
      }
    }
  }, [profileHoverPoint, map]);
  return null;
}


// Component to dynamically fit bounds of the polyline
function MapBounds({ bounds }) {
  const map = useMap();
  useEffect(() => {
    if (bounds) {
      map.fitBounds(bounds, { padding: [20, 20] });
    }
  }, [bounds, map]);
  return null;
}

// Component to handle map container size invalidation
function MapResizeObserver() {
  const map = useMap();
  useEffect(() => {
    const resizeObserver = new ResizeObserver(() => {
      map.invalidateSize();
    });
    resizeObserver.observe(map.getContainer());
    return () => resizeObserver.disconnect();
  }, [map]);
  return null;
}

// Component to handle the reset button
function MapResetButton({ bounds }) {
  const map = useMap();
  return (
    <div className="absolute bottom-6 right-4 z-[650] leaflet-control">
      <button 
        onClick={(e) => {
          e.preventDefault();
          e.stopPropagation();
          if (bounds) map.fitBounds(bounds, { padding: [20, 20] });
        }}
        className="w-10 h-10 rounded-full bg-slate-800 border-slate-600 border-2 text-slate-300 flex items-center justify-center shadow-lg hover:text-lime-400 hover:border-lime-500 transition-colors"
        title="Fit track to view"
      >
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="m15 15 6 6m-6-6v4.8m0-4.8h4.8M9 15l-6 6m6-6v4.8m0-4.8H4.2M9 9 3 3m6 6V4.2M9 9H4.2m5.8-6 6 6m-6-6v4.8m0-4.8h4.8"/></svg>
      </button>
    </div>
  );
}

// Component to handle overlay buttons (must be inside MapContainer for useMap context)
function MapOverlayControls({ mapVisible, setMapVisible, isTracking, setIsTracking, bounds, gpsState, setGpsState, activeSection }) {
  const map = useMap();
  
  if (!mapVisible) return null;
  
  return (
    <>
      <div className="absolute top-[80px] left-[10px] z-[650] flex flex-col gap-2">
        <button 
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            setMapVisible(false);
          }}
          className="w-[34px] h-[34px] bg-slate-800 border-2 border-slate-600 text-slate-300 hover:text-lime-400 rounded flex items-center justify-center shadow-lg transition-colors leaflet-control"
          title="Hide Map"
        >
          <EyeOff size={18} />
        </button>
        <button 
          onClick={async (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (gpsState && gpsState.active && gpsState.lat !== null && gpsState.lon !== null) {
              // If tracking is ON and we have coordinates, just pan to current pos without requesting again
              map.setView([gpsState.lat, gpsState.lon], map.getZoom(), { animate: true });
              return;
            }
            try {
              const permStatus = await Geolocation.checkPermissions();
              if (permStatus.location !== 'granted') {
                const req = await Geolocation.requestPermissions();
                if (req.location !== 'granted') {
                  throw new Error("Location permission not granted");
                }
              }
              const pos = await Geolocation.getCurrentPosition({ enableHighAccuracy: true, timeout: 10000 });
              map.setView([pos.coords.latitude, pos.coords.longitude], 15, { animate: true });
              setGpsState(prev => ({ ...prev, lat: pos.coords.latitude, lon: pos.coords.longitude, accuracy: pos.coords.accuracy }));
            } catch (err) {
              console.warn("Could not get current position", err);
              alert("GPS Error: " + err.message + "\nCheck if location permissions are granted for this site or app.");
            }
          }}
          className="w-[34px] h-[34px] bg-slate-800 border-2 border-slate-600 text-slate-300 hover:text-lime-400 rounded flex items-center justify-center shadow-lg transition-colors leaflet-control"
          title="Show current position"
        >
          <Crosshair size={18} />
        </button>
        <button 
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            if (bounds) map.fitBounds(bounds, { padding: [5, 5] });
          }}
          className="w-[34px] h-[34px] bg-slate-800 border-2 border-slate-600 text-slate-300 hover:text-lime-400 rounded flex items-center justify-center shadow-lg transition-colors leaflet-control"
          title="Fit track to view"
        >
          <Maximize size={18} />
        </button>
        {activeSection && activeSection.sectionPoints && activeSection.sectionPoints.length > 0 && (
          <button 
            onClick={(e) => {
              e.preventDefault();
              e.stopPropagation();
              const sectionBounds = L.latLngBounds(activeSection.sectionPoints.map(p => [p.lat, p.lon]));
              map.fitBounds(sectionBounds, { padding: [20, 20], maxZoom: 15, animate: true });
            }}
            className="w-[34px] h-[34px] bg-slate-800 border-2 border-cyan-500 text-cyan-400 hover:text-cyan-300 rounded flex items-center justify-center shadow-lg transition-colors leaflet-control"
            title="Fit selected section to view"
          >
            <ZoomIn size={18} />
          </button>
        )}
        <button 
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            setIsTracking(!isTracking);
          }}
          className={`w-[34px] h-[34px] rounded flex items-center justify-center shadow-lg border-2 transition-colors leaflet-control ${isTracking ? 'bg-lime-500 border-lime-400 text-slate-900' : 'bg-slate-800 border-slate-600 text-slate-300 hover:text-lime-400'}`}
          title="Toggle GPS Tracking"
        >
          <Navigation size={18} />
        </button>
        <button 
          onClick={(e) => {
            e.preventDefault();
            e.stopPropagation();
            const container = map.getContainer();
            if (!document.fullscreenElement) {
              container.requestFullscreen().catch(err => console.warn(err));
            } else {
              document.exitFullscreen();
            }
          }}
          className="w-[34px] h-[34px] bg-slate-800 border-2 border-slate-600 text-slate-300 hover:text-lime-400 rounded flex items-center justify-center shadow-lg transition-colors leaflet-control mt-4"
          title="Fullscreen Map"
        >
          <Expand size={18} />
        </button>
      </div>
    </>
  );
}

export function MapRenderer({ gpxPoints, checkpoints, actionTimeline, activeSection, setSelectedSection, profileHoverPoint, mapVisible, setMapVisible, autoOpenDetails, gpsState, setGpsState, gpsInterval, lang = 'en' }) {
  const [positions, setPositions] = useState([]);
  const [bounds, setBounds] = useState(null);
  const [isTracking, setIsTracking] = useState(() => {
    try {
      return localStorage.getItem('ultra_is_tracking') === '1';
    } catch(e) {
      return false;
    }
  });

  const [showOverlay, setShowOverlay] = useState(false);

  useEffect(() => {
    if (!activeSection) {
      setShowOverlay(false);
    } else if (autoOpenDetails) {
      setShowOverlay(true);
    }
  }, [activeSection, autoOpenDetails]);

  useEffect(() => {
    try {
      if (isTracking) {
        localStorage.setItem('ultra_is_tracking', '1');
      } else {
        localStorage.removeItem('ultra_is_tracking');
      }
    } catch(e) {}
  }, [isTracking]);

  useEffect(() => {
    if (gpxPoints && gpxPoints.length > 0) {
      const posArray = gpxPoints.map(pt => [pt.lat, pt.lon]);
      setPositions(posArray);
      setBounds(L.latLngBounds(posArray));
    }
  }, [gpxPoints]);

  useEffect(() => {
    if (isTracking) {
      GpsTrackingService.startTracking(gpxPoints, gpsInterval, (update) => {
        setGpsState(prev => ({ ...prev, active: true, ...update }));
      }, (err) => {
        console.warn("GPS Tracking Error:", err);
        alert("GPS Tracking Error: " + err.message + "\nPlease enable location services and grant permission.");
        setIsTracking(false);
      });
    } else {
      GpsTrackingService.stopTracking();
      if (setGpsState) {
        setGpsState(prev => ({ ...prev, active: false, lat: null, lon: null }));
      }
    }
    
    return () => GpsTrackingService.stopTracking();
  }, [isTracking, gpxPoints, gpsInterval, setGpsState]);

  if (!gpxPoints || gpxPoints.length === 0) {
    return <div className="h-full bg-slate-800 flex items-center justify-center text-slate-500">Loading Map...</div>;
  }

  return (
    <div className={`w-full h-full relative z-0 transition-all duration-300 ${!mapVisible ? 'h-0 hidden md:block md:w-0' : ''}`}>
      
      {/* Map Actions Overlay (desktop) -> moved inside MapContainer */}
      
      {/* Section Information Overlay Card */}
      {activeSection && mapVisible && activeSection.sectionPoints && showOverlay && (
        <div className="absolute bottom-10 left-1/2 -translate-x-1/2 w-[90%] max-w-[340px] md:max-w-[500px] z-[2000] bg-slate-800/95 backdrop-blur-md border border-cyan-500/50 p-4 rounded-xl shadow-[0_0_20px_rgba(0,0,0,0.5)] pointer-events-auto">
          <button 
            onClick={() => setShowOverlay(false)}
            className="absolute top-3 right-3 text-slate-400 hover:text-white bg-slate-700/50 hover:bg-slate-600 rounded-full p-1 transition-colors"
          >
            <X size={16} />
          </button>
          <div className="font-bold text-cyan-400 text-sm mb-2 pb-2 border-b border-slate-700 pr-6 flex items-center gap-2">
            <span>{activeSection.name}</span>
            {activeSection.type && (
              <span className={`text-[8px] font-bold px-1.5 py-0.5 rounded select-none ${
                activeSection.type === 'Peak' ? 'bg-red-950/60 text-red-400 border border-red-800/40' :
                activeSection.type === 'Valley' ? 'bg-blue-950/60 text-blue-400 border border-blue-800/40' :
                activeSection.type === 'Start' ? 'bg-lime-950/60 text-lime-400 border border-lime-800/40' :
                activeSection.type === 'Finish' ? 'bg-pink-950/60 text-pink-400 border border-pink-800/40' :
                'bg-slate-800 text-slate-400 border border-slate-700'
              }`}>
                {activeSection.type === 'Peak' ? (lang === 'en' ? 'PEAK' : 'SZCZYT') :
                 activeSection.type === 'Valley' ? (lang === 'en' ? 'VALLEY' : 'DOLINA') :
                 activeSection.type === 'Start' ? 'START' :
                 activeSection.type === 'Finish' ? (lang === 'en' ? 'FINISH' : 'META') :
                 (lang === 'en' ? 'FLAT' : 'PŁASKO')}
              </span>
            )}
          </div>
          <div className="flex justify-between items-center mb-2">
            <div className="text-xs text-slate-300">
              <span className="text-slate-500">Dist: </span>
              {activeSection.km.toFixed(1)} km {activeSection.sectionDist && <span className="text-cyan-400">(+{activeSection.sectionDist.toFixed(1)} km)</span>}
            </div>
            <div className="flex gap-2 text-xs">
              <span className="text-lime-400">+{Math.round(activeSection.sectionAscent)}m</span>
              <span className="text-red-400">-{Math.round(activeSection.sectionDescent)}m</span>
            </div>
          </div>
          <div className="flex justify-between items-center mb-2 bg-slate-900/50 p-1.5 rounded border border-slate-700/50 text-xs">
             <div><span className="text-slate-500">Total ETA:</span> <span className="text-orange-400 font-bold">{Math.floor(activeSection.etaHrs)}h {Math.round((activeSection.etaHrs % 1) * 60).toString().padStart(2, '0')}m</span></div>
             <div className="text-slate-400 font-semibold">{(activeSection.etaHrs / activeSection.km * 60).toFixed(0)} min/km</div>
          </div>
          {activeSection.actionText && (
            <div className="text-[10px] md:text-[11px] leading-tight text-slate-400 mt-2 bg-slate-900/50 p-2 rounded border border-slate-700/50 max-h-[35vh] md:max-h-[60vh] overflow-y-auto custom-scrollbar">
              {activeSection.actionText}
            </div>
          )}
        </div>
      )}

      <div className={`w-full h-full ${!mapVisible ? 'hidden md:block' : ''}`}>
        <MapContainer 
          center={positions[0]} 
          zoom={13} 
          style={{ height: '100%', width: '100%', background: '#0f172a' }}
          zoomControl={false}
        >
          <TileLayer
            url="https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png"
            attribution='&copy; OpenTopoMap'
            maxZoom={17}
          />
          
          <ZoomControl position="topleft" />
          
          {/* GPX Track (RED as requested) */}
          <Polyline positions={positions} color="#ef4444" weight={4} opacity={0.8} />
          
          {/* Checkpoints */}
          {checkpoints && checkpoints.map((cp, i) => {
            let actionText = null;
            let sectionDist = 0;
            if (i > 0 && actionTimeline) {
                const prevCp = checkpoints[i-1];
                sectionDist = cp.km - prevCp.km;
                const actions = actionTimeline.filter(a => a.startElapsedHours >= prevCp.etaHrs && a.startElapsedHours < cp.etaHrs);
                if (actions.length === 0) {
                    const fallback = actionTimeline.find(a => cp.etaHrs > a.startElapsedHours && cp.etaHrs <= a.endElapsedHours);
                    if (fallback) actionText = fallback[`action_${lang}`] || fallback.action_en;
                } else {
                    actionText = actions.map(a => `- ${a[`action_${lang}`] || a.action_en}`).join('\n');
                }
            }
            const isActive = activeSection && (activeSection.id === cp.id || activeSection.name === cp.name);
            return (
              <Marker 
                key={i} 
                position={[cp.lat, cp.lon]} 
                icon={createNumberedIcon(i === 0 ? 'S' : i)}
                zIndexOffset={isActive ? 1000 : 0}
                eventHandlers={{ 
                  click: () => { 
                    if (setSelectedSection) setSelectedSection({ ...cp, actionText, sectionDist }); 
                    setShowOverlay(true);
                  } 
                }}
              />
            );
          })}

          {/* Hover Marker and Section */}
          {activeSection && activeSection.sectionPoints && activeSection.sectionPoints.length > 0 && (
             <Polyline 
               positions={activeSection.sectionPoints.map(p => [p.lat, p.lon])} 
               color="#06b6d4" 
               weight={8} 
               opacity={0.9} 
             />
          )}
          {activeSection && activeSection.lat && (
             <Marker position={[activeSection.lat, activeSection.lon]} icon={createHoverIcon()} zIndexOffset={-100} />
          )}
          
          {profileHoverPoint && (
             <Marker 
               position={[profileHoverPoint.lat, profileHoverPoint.lon]}
               icon={profileHoverIcon}
               zIndexOffset={2000}
             />
          )}
          
          <MapHoverSync activeSection={activeSection} />
          <ProfileHoverSync profileHoverPoint={profileHoverPoint} />

          {bounds && <MapBounds bounds={bounds} />}
          <MapResizeObserver />
          <MapOverlayControls 
             mapVisible={mapVisible} 
             setMapVisible={setMapVisible} 
             isTracking={isTracking} 
             setIsTracking={setIsTracking} 
             bounds={bounds} 
             gpsState={gpsState}
             setGpsState={setGpsState} 
             activeSection={activeSection}
          />
          {/* Live GPS Markers */}
          {gpsState?.lat !== null && (
            <>
              <Circle 
                center={[gpsState.lat, gpsState.lon]} 
                radius={gpsState.accuracy || 10} 
                pathOptions={{ 
                  fillColor: !gpsState.active ? '#3b82f6' : (gpsState.accuracy > 100 ? '#ef4444' : (gpsState.accuracy > 50 ? '#f97316' : '#84cc16')), 
                  color: !gpsState.active ? '#3b82f6' : (gpsState.accuracy > 100 ? '#ef4444' : (gpsState.accuracy > 50 ? '#f97316' : '#84cc16')), 
                  fillOpacity: 0.12, 
                  opacity: 0.45, 
                  weight: 1.5, 
                  className: 'gps-ring-pulse' 
                }}
              />
              <CircleMarker
                center={[gpsState.lat, gpsState.lon]}
                radius={8}
                pathOptions={{
                   fillColor: !gpsState.active ? '#3b82f6' : (gpsState.accuracy > 100 ? '#ef4444' : (gpsState.accuracy > 50 ? '#f97316' : '#84cc16')),
                   fillOpacity: 1,
                   color: gpsState.offRoute ? '#fbbf24' : '#ffffff',
                   weight: 2
                }}
                zIndexOffset={1000}
              />
            </>
          )}
        </MapContainer>
      </div>
    </div>
  );
}
