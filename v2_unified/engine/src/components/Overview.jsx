import React, { useState, useEffect } from 'react';
import { createPortal } from 'react-dom';
import { ElevationProfile } from './ElevationProfile';
import { MapOfflineService } from '../services/MapOfflineService';

export function Overview({ dataset, gpxPoints, checkpoints, lang, hoverPoint, selectedSection, onHoverPoint, autoOpenDetails, setAutoOpenDetails, gpsState, gpsInterval, setGpsInterval }) {
  const [downloadProgress, setDownloadProgress] = useState(0);
  const [isDownloaded, setIsDownloaded] = useState(false);
  const [isDownloading, setIsDownloading] = useState(false);
  const [cacheStats, setCacheStats] = useState({ total: 0, zooms: {} });
  const [startTime, setStartTime] = useState(localStorage.getItem('ultra_start_time_v2') || "05:00");
  const [challengeDate, setChallengeDate] = useState('2026-07-10');
  const [showResetModal, setShowResetModal] = useState(false);

  useEffect(() => {
    if (dataset?.route_id) {
      const key = `ultra_challenge_date_${dataset.route_id}`;
      const savedDate = localStorage.getItem(key);
      setChallengeDate(savedDate || dataset.challengeParameters?.date || '2026-07-10');
    }
  }, [dataset]);

  useEffect(() => {
    if (dataset?.route_id && challengeDate) {
      localStorage.setItem(`ultra_challenge_date_${dataset.route_id}`, challengeDate);
    }
  }, [challengeDate, dataset?.route_id]);

  const fetchStats = async () => {
    const stats = await MapOfflineService.getCacheStats();
    setCacheStats(stats);
  };

  useEffect(() => {
    // live update for clock in GPS card
    const timer = setInterval(() => {
      if (selectedSection) setStartTime(prev => prev); // force re-render
    }, 60000);
    return () => clearInterval(timer);
  }, [selectedSection]);

  useEffect(() => {
    MapOfflineService.isDownloaded().then(setIsDownloaded);
    fetchStats();
    
    const unsubscribe = MapOfflineService.subscribe((state) => {
      setIsDownloading(state.isDownloading);
      setDownloadProgress(state.progress);
      if (!state.isDownloading) {
         fetchStats();
         MapOfflineService.isDownloaded().then(setIsDownloaded);
      }
    });
    
    return unsubscribe;
  }, []);

  useEffect(() => {
    let intervalId;
    if (isDownloading) {
      intervalId = setInterval(() => {
        fetchStats();
      }, 1500);
    }
    return () => {
      if (intervalId) clearInterval(intervalId);
    };
  }, [isDownloading]);

  const handleDownloadMap = async () => {
    if (isDownloaded || isDownloading) return;
    setIsDownloading(true);
    setDownloadProgress(0);
    try {
      const result = await MapOfflineService.downloadOfflineTiles(gpxPoints);
      if (result.success) {
        setIsDownloaded(true);
      } else {
        alert(lang === 'en' ? result.message : `Błąd: ${result.message}`);
      }
      fetchStats();
    } catch (e) {
      console.error(e);
      alert(lang === 'en' ? 'Download failed' : 'Pobieranie nie powiodło się');
    }
  };

  const handleDeleteMap = async () => {
    if (window.confirm(lang === 'en' ? 'Delete offline map data?' : 'Usunąć dane mapy offline?')) {
      await MapOfflineService.deleteMap();
      setIsDownloaded(false);
      setDownloadProgress(0);
      fetchStats();
    }
  };

  return (
    <div className="space-y-4">
      {/* Settings & Challenge Parameters */}
      <div className="bg-slate-800/50 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl">
        <h2 className="text-base md:text-lg font-bold text-lime-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2">
          {lang === 'en' ? 'Settings' : 'Ustawienia'}
        </h2>
        
        <div className="flex flex-wrap gap-2 md:gap-3 items-center mb-4 md:mb-6">
          <div className="flex items-center space-x-2 bg-slate-800 p-1.5 md:p-2 px-2 md:px-3 rounded border border-slate-600 shadow-sm h-[28px] md:h-[38px]">
            <label className="text-xs md:text-sm font-bold text-slate-300 whitespace-nowrap">
              {lang === 'en' ? 'Start Time:' : 'Godzina Startu:'}
            </label>
            <input 
              type="time" 
              value={startTime} 
              onChange={(e) => {
                setStartTime(e.target.value);
                localStorage.setItem('ultra_start_time_v2', e.target.value);
              }}
              style={{ colorScheme: 'dark' }} 
              className="bg-slate-900 border border-slate-600 text-lime-400 font-bold rounded px-1.5 md:px-2 py-0.5 text-xs md:text-sm outline-none" 
            />
          </div>

          <div className="flex items-center space-x-2 bg-slate-800 p-1.5 md:p-2 px-2 md:px-3 rounded border border-slate-600 shadow-sm h-[28px] md:h-[38px]">
            <label className="text-xs md:text-sm font-bold text-slate-300 whitespace-nowrap">
              {lang === 'en' ? 'GPS Interval:' : 'Interwał GPS:'}
            </label>
            <select 
              value={gpsInterval}
              onChange={(e) => {
                const val = parseInt(e.target.value);
                setGpsInterval(val);
                try { localStorage.setItem('ultra_gps_interval', val); } catch(err) {}
              }}
              className="bg-slate-900 border border-slate-600 text-lime-400 font-bold rounded px-1 md:px-2 text-xs md:text-sm outline-none h-[20px] md:h-[26px]"
            >
              <option value="15000">15 s</option>
              <option value="30000">30 s</option>
              <option value="60000">1 min</option>
            </select>
          </div>

          <div className="flex bg-slate-800 rounded border border-slate-600 overflow-hidden shadow-sm h-[28px] md:h-[38px] items-center">
             {isDownloaded ? (
               <>
                 <div className="px-3 md:px-4 text-xs md:text-sm font-bold bg-slate-800 text-slate-400 h-full flex items-center cursor-default border-r border-slate-700">
                    {lang === 'en' ? '✓ Offline map ready' : '✓ Mapa offline gotowa'}
                 </div>
                 <button onClick={handleDeleteMap} className="px-2 md:px-3 text-xs md:text-sm font-bold bg-red-950/40 text-red-400 hover:bg-red-900/60 hover:text-red-200 transition-colors h-full cursor-pointer" title={lang === 'en' ? 'Delete offline map' : 'Usuń mapę offline'}>
                    ✕
                 </button>
               </>
             ) : (
               <button 
                 className="bg-slate-700 hover:bg-slate-600 text-slate-200 px-3 md:px-4 font-bold text-xs md:text-sm transition-colors h-full whitespace-nowrap cursor-pointer disabled:opacity-50"
                 onClick={handleDownloadMap}
                 disabled={isDownloaded || isDownloading}
               >
                 {isDownloading 
                    ? (lang === 'en' ? 'Downloading...' : 'Pobieranie...') 
                    : (lang === 'en' ? '📥 Download offline map' : '📥 Pobierz mapę offline')}
               </button>
             )}
             {isDownloading && (
               <>
                 <div className="h-full bg-slate-900 border-l border-slate-600 px-3 flex items-center text-[10px] md:text-xs font-mono text-lime-400">
                    {downloadProgress}%
                 </div>
                 <button 
                   onClick={() => MapOfflineService.cancelDownload()}
                   className="bg-red-900/50 hover:bg-red-800 text-red-400 px-3 border-l border-slate-600 text-xs font-bold transition-colors cursor-pointer"
                 >
                   {lang === 'en' ? 'Stop' : 'Stop'}
                 </button>
               </>
             )}
          </div>
          {cacheStats.total > 0 && (
            <div className="text-[10px] md:text-xs text-slate-500 font-mono flex items-center ml-1">
               {lang === 'en' ? 'Tile cache:' : 'Pamięć map:'} {cacheStats.total} tiles 
               ({Object.entries(cacheStats.zooms).map(([k,v]) => `${k}:${v}`).join(', ')})
            </div>
          )}
        </div>

        <div className="flex flex-wrap gap-2 md:gap-3 items-center mb-4 md:mb-6">
          <label className="flex items-center space-x-2 bg-slate-800 p-1.5 md:p-2 px-2 md:px-3 rounded border border-slate-600 shadow-sm cursor-pointer hover:bg-slate-700 transition-colors">
            <input 
              type="checkbox" 
              checked={autoOpenDetails} 
              onChange={e => setAutoOpenDetails(e.target.checked)} 
              className="w-4 h-4 rounded accent-lime-500" 
            />
            <span className="text-xs md:text-sm font-bold text-slate-300">
              {lang === 'en' ? 'Auto-open section info on map' : 'Auto-otwieranie panelu sekcji na mapie'}
            </span>
          </label>
          
          <button
            onClick={() => setShowResetModal(true)}
            className="px-3 py-1.5 md:py-2 bg-red-900/40 text-red-400 hover:bg-red-800 border border-red-700 rounded text-xs md:text-sm font-bold shadow-sm transition-colors"
          >
            {lang === 'en' ? 'Reset Settings' : 'Resetuj Ustawienia'}
          </button>
        </div>

        {dataset?.challengeParameters && (
          <>
            <h2 className="text-base md:text-lg font-bold text-cyan-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2">
              {lang === 'en' ? 'Challenge Parameters' : 'Parametry Wyzwania'}
            </h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-2 md:gap-4">
               <div className="flex flex-col space-y-2 md:space-y-3">
                  <div className="flex items-center bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1.5 rounded border border-slate-700 shadow-sm w-full font-semibold text-xs md:text-sm">
                    <span className="mr-2">🗓️</span>
                    <input 
                      type="date"
                      value={challengeDate}
                      onChange={(e) => setChallengeDate(e.target.value)}
                      className="bg-transparent border-none outline-none text-slate-300 w-full"
                      style={{ colorScheme: 'dark' }}
                    />
                  </div>
                  <div className="bg-slate-800 text-slate-300 px-2 py-1 md:px-3 md:py-1.5 rounded border border-slate-700 shadow-sm w-full font-semibold text-xs md:text-sm">
                    🏃‍♂️ {dataset.challengeParameters.weightKg} kg
                  </div>
               </div>
               <div className="flex flex-col space-y-2 md:space-y-3">
                  <div className="bg-slate-800 text-red-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-red-900/50 shadow-sm w-full font-semibold text-xs md:text-sm">
                    ❤️ Target: {dataset.challengeParameters.targetBpm} bpm
                  </div>
                  <div className="bg-lime-900/30 text-lime-400 px-2 py-1 md:px-3 md:py-1.5 rounded border border-lime-700/50 shadow-sm w-full font-semibold text-xs md:text-sm">
                    ⏱️ {lang === 'en' ? 'Goal:' : 'Cel:'} {dataset.challengeParameters.goalTime}
                  </div>
               </div>
            </div>
          </>
        )}
      </div>

      {/* GPS Status Card (Pinned Section or Live Tracking) */}
      {((gpsState && gpsState.active && gpsState.lat !== null) || selectedSection) && (() => {
        let activeKm = 0;
        let expectedElapsed = 0;
        let sectionName = "";
        let gpsAccuracy = null;
        let isOffRoute = false;
        const lastCp = checkpoints[checkpoints.length - 1];
        
        if (selectedSection) {
            activeKm = selectedSection.km;
            expectedElapsed = (selectedSection.etaHrs || 0) * 60;
            sectionName = selectedSection.name;
        } else if (gpsState && gpsState.active && gpsState.lat !== null) {
            activeKm = gpsState.km;
            gpsAccuracy = gpsState.accuracy;
            isOffRoute = gpsState.offRoute;
            
            let prevCp = checkpoints[0];
            let nextCp = lastCp;
            for (let i = 0; i < checkpoints.length - 1; i++) {
               if (activeKm >= checkpoints[i].km && activeKm <= checkpoints[i+1].km) {
                   prevCp = checkpoints[i];
                   nextCp = checkpoints[i+1];
                   break;
               }
            }
            if (!prevCp || !nextCp) {
                expectedElapsed = 0;
            } else if (nextCp.km === prevCp.km) {
                expectedElapsed = (prevCp.etaHrs || 0) * 60;
            } else {
                const ratio = ((activeKm || 0) - (prevCp.km || 0)) / ((nextCp.km || 1) - (prevCp.km || 0));
                expectedElapsed = ((prevCp.etaHrs || 0) + ((nextCp.etaHrs || 0) - (prevCp.etaHrs || 0)) * ratio) * 60;
            }
            
            sectionName = nextCp?.name || (lang === 'en' ? 'Live Position' : 'Pozycja na żywo');
            if (isOffRoute) {
                sectionName = `⚠️ ${sectionName} (${lang === 'en' ? 'Off Route' : 'Poza trasą'})`;
            }
        }

        const now = new Date();
        const startParts = startTime.split(':');
        let startDate = new Date(now.getFullYear(), now.getMonth(), now.getDate(), parseInt(startParts[0] || 5), parseInt(startParts[1] || 0), 0);
        let diffMs = now.getTime() - startDate.getTime();
        if (diffMs < -12 * 60 * 60 * 1000) {
            startDate.setDate(startDate.getDate() - 1);
            diffMs = now.getTime() - startDate.getTime();
        }
        const actualElapsedMinutes = diffMs / 60000;
        const delta = actualElapsedMinutes - (expectedElapsed || 0);
        const absDelta = isNaN(delta) ? 0 : Math.round(Math.abs(delta));
        
        let deltaText = "";
        let deltaColor = "";
        if (Math.abs(delta) <= 5) {
            deltaColor = "text-slate-300";
            deltaText = lang === 'en' ? '● On schedule' : '● Zgodnie z planem';
        } else if (delta < -5) {
            deltaColor = "text-lime-400";
            deltaText = lang === 'en' ? `▲ ${absDelta} min ahead of plan` : `▲ ${absDelta} min przed planem`;
        } else if (delta <= 20) {
            deltaColor = "text-orange-400";
            deltaText = lang === 'en' ? `▼ ${absDelta} min behind plan` : `▼ ${absDelta} min za planem`;
        } else {
            deltaColor = "text-red-500";
            deltaColor = "text-red-500";
            deltaText = lang === 'en' ? `▼ ${absDelta} min behind plan` : `▼ ${absDelta} min za planem`;
        }

        const remainingPlanMins = (lastCp?.etaHrs || 0) * 60 - expectedElapsed;
        const etaMs = now.getTime() + remainingPlanMins * 60000;
        const etaDate = new Date(etaMs);
        const nowDay = new Date(now.getFullYear(), now.getMonth(), now.getDate());
        const etaDay = new Date(etaDate.getFullYear(), etaDate.getMonth(), etaDate.getDate());
        const diffDays = Math.round((etaDay.getTime() - nowDay.getTime()) / (1000 * 60 * 60 * 24));
        
        let dayPrefix = "";
        if (diffDays === 1) {
            dayPrefix = lang === 'en' ? 'Tomorrow, ' : 'Jutro, ';
        } else if (diffDays === 2) {
            dayPrefix = lang === 'en' ? 'Day after tomorrow, ' : 'Pojutrze, ';
        } else if (diffDays > 2) {
            dayPrefix = lang === 'en' ? `In ${diffDays} days, ` : `Za ${diffDays} dni, `;
        }
        
        const timeStr = `${etaDate.getHours().toString().padStart(2, '0')}:${etaDate.getMinutes().toString().padStart(2, '0')}`;
        const etaStr = dayPrefix + timeStr;

        return (
          <div className="bg-slate-900 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl relative overflow-hidden">
            <div className="absolute top-0 left-0 w-full h-1 bg-gradient-to-r from-lime-400 to-cyan-400"></div>
            
            <div className="flex justify-between items-center mb-4">
              <h2 className="text-sm md:text-base font-bold text-lime-400 flex items-center gap-2">
                 📍 {lang === 'en' ? 'My Position' : 'Moja Pozycja'}
              </h2>
              <div className="flex gap-2">
                 {gpsAccuracy !== null && (
                   <div className="bg-slate-800 border border-slate-700 px-2 py-0.5 rounded text-[10px] text-cyan-400 font-bold">
                     GPS: ±{Math.round(gpsAccuracy)}m
                   </div>
                 )}
              </div>
            </div>
            
            <div className="mb-4">
              <div className="flex justify-between text-[10px] md:text-xs font-bold text-slate-300 mb-1">
                <span>{lang === 'en' ? 'Distance:' : 'Dystans:'} <span className="text-lime-400">{Number(activeKm || 0).toFixed(1)} / {Number(lastCp?.km || 0).toFixed(1)} km</span></span>
                <span className="text-lime-400">{Math.round(((activeKm || 0) / (lastCp?.km || 1)) * 100)}%</span>
              </div>
              <div className="w-full bg-slate-800 h-2 md:h-2.5 rounded-full overflow-hidden">
                 <div 
                   className="h-full bg-gradient-to-r from-lime-400 to-cyan-400 transition-all duration-300" 
                   style={{ width: `${(activeKm / (lastCp?.km || 1)) * 100}%` }}
                 ></div>
              </div>
            </div>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 mb-4">
              <div className="bg-slate-800/50 p-2 md:p-3 rounded border border-slate-700">
                 <div className="text-[9px] md:text-[10px] text-slate-500 font-bold uppercase mb-1">
                   {lang === 'en' ? 'Current Section' : 'Obecny Odcinek'}
                 </div>
                 <div className="text-xs md:text-sm font-bold text-slate-200 truncate" title={sectionName}>
                   {sectionName}
                 </div>
              </div>
              <div className="bg-slate-800/50 p-2 md:p-3 rounded border border-slate-700">
                 <div className="text-[9px] md:text-[10px] text-slate-500 font-bold uppercase mb-1">
                   {lang === 'en' ? 'Pace vs Plan' : 'Tempo vs Plan'}
                 </div>
                 <div className={`text-xs md:text-sm font-bold ${deltaColor}`}>
                   {deltaText}
                 </div>
              </div>
            </div>
            
            <div className="bg-slate-800/80 p-2 md:p-3 rounded border border-slate-700 flex flex-wrap gap-2 justify-between items-center">
               <div className="text-xs font-bold text-slate-400">
                 {lang === 'en' ? 'Estimated Finish (ETA):' : 'Szacowany Koniec (ETA):'}
               </div>
               <div className="text-lg md:text-xl font-bold text-cyan-400 text-right">
                 {etaStr}
               </div>
            </div>
          </div>
        );
      })()}

      {/* Elevation Profile Card */}
      <div className="bg-slate-800/50 p-3 md:p-5 rounded-lg border border-slate-700 shadow-xl">
        <h2 className="text-base md:text-lg font-bold text-cyan-400 mb-2 md:mb-3 border-b border-slate-700 pb-1 md:pb-2">
          {lang === 'en' ? 'Route Elevation Profile' : 'Profil Wysokości Trasy'}
        </h2>
        <div className="w-full relative mb-4">
           <ElevationProfile points={gpxPoints} checkpoints={checkpoints} height={256} hoverPoint={hoverPoint} onHoverPoint={onHoverPoint} />
        </div>
        
        {/* Legend */}
        <div className="flex flex-wrap gap-2 md:gap-4 text-[10px] md:text-xs font-semibold justify-center bg-slate-900/60 p-2 md:p-3 rounded border border-slate-800">
           <div className="flex items-center"><span className="w-2.5 h-2.5 bg-red-600 inline-block mr-1.5 rounded-full"></span>{lang === 'en' ? 'Steep Up (>15%)' : 'Stromo w górę (>15%)'}</div>
           <div className="flex items-center"><span className="w-2.5 h-2.5 bg-orange-500 inline-block mr-1.5 rounded-full"></span>{lang === 'en' ? 'Up (5-15%)' : 'W górę (5-15%)'}</div>
           <div className="flex items-center"><span className="w-2.5 h-2.5 bg-lime-500 inline-block mr-1.5 rounded-full"></span>{lang === 'en' ? 'Flat (-5 to 5%)' : 'Płasko (-5 do 5%)'}</div>
           <div className="flex items-center"><span className="w-2.5 h-2.5 bg-green-700 inline-block mr-1.5 rounded-full"></span>{lang === 'en' ? 'Down (-15 to -5%)' : 'W dół (-15 do -5%)'}</div>
           <div className="flex items-center"><span className="w-2.5 h-2.5 bg-blue-500 inline-block mr-1.5 rounded-full"></span>{lang === 'en' ? 'Steep Down (<-15%)' : 'Stromo w dół (<-15%)'}</div>
        </div>
      </div>
      
      {/* Reset Confirmation Modal */}
      {showResetModal && createPortal(
        <div className="fixed inset-0 z-[9999] flex items-center justify-center bg-black/60 backdrop-blur-sm p-4">
          <div className="bg-slate-800 border border-slate-700 rounded-xl shadow-2xl p-6 max-w-sm w-full animate-in zoom-in-95 duration-200">
            <h3 className="text-lg font-bold text-slate-200 mb-2">
              {lang === 'en' ? 'Reset all settings?' : 'Zresetować ustawienia?'}
            </h3>
            <p className="text-sm text-slate-400 mb-6">
              {lang === 'en' 
                ? 'Are you sure you want to reset all settings to default? Offline maps will not be deleted.' 
                : 'Czy na pewno chcesz zresetować wszystkie ustawienia do domyślnych? Pobrane mapy offline zostaną zachowane.'}
            </p>
            <div className="flex justify-end gap-3">
              <button 
                onClick={() => setShowResetModal(false)}
                className="px-4 py-2 bg-slate-700 hover:bg-slate-600 text-slate-300 rounded font-medium transition-colors"
              >
                {lang === 'en' ? 'Cancel' : 'Anuluj'}
              </button>
              <button 
                onClick={() => {
                  localStorage.removeItem('ultra_start_time_v2');
                  localStorage.removeItem('ultra_gps_interval');
                  localStorage.removeItem('ultra_lang');
                  localStorage.removeItem('ultra_challenge_date');
                  window.location.reload();
                }}
                className="px-4 py-2 bg-red-600 hover:bg-red-500 text-white rounded font-medium transition-colors shadow-lg shadow-red-900/20"
              >
                {lang === 'en' ? 'Reset' : 'Resetuj'}
              </button>
            </div>
          </div>
        </div>,
        document.body
      )}
    </div>
  );
}
