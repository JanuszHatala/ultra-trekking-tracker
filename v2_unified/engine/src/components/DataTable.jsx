import React, { useState, useRef, useEffect } from 'react';
import { createPortal } from 'react-dom';
import { Settings2, MapPin, X } from 'lucide-react';

// Tiny inline canvas for section profile
function SparklineProfile({ points, minEle, maxEle, width = 100, height = 40 }) {
  const canvasRef = useRef(null);

  useEffect(() => {
    if (!points || points.length === 0 || !canvasRef.current) return;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    
    ctx.clearRect(0, 0, width, height);
    
    const range = maxEle - minEle || 1;
    const maxDist = points[points.length - 1].dist - points[0].dist;
    
    // Fill
    ctx.beginPath();
    ctx.moveTo(0, height);
    points.forEach((p, i) => {
      const x = ((p.dist - points[0].dist) / maxDist) * width;
      const y = height - ((p.ele - minEle) / range) * height;
      ctx.lineTo(x, y);
    });
    ctx.lineTo(width, height);
    ctx.closePath();
    ctx.fillStyle = 'rgba(6, 182, 212, 0.2)'; // cyan-500/20
    ctx.fill();

    // Stroke
    for (let i = 1; i < points.length; i++) {
      const p1 = points[i - 1];
      const p2 = points[i];
      
      const x1 = ((p1.dist - points[0].dist) / maxDist) * width;
      const y1 = height - ((p1.ele - minEle) / range) * height;
      const x2 = ((p2.dist - points[0].dist) / maxDist) * width;
      const y2 = height - ((p2.ele - minEle) / range) * height;
      
      const distDiff = (p2.dist - p1.dist) * 1000;
      const eleDiff = p2.ele - p1.ele;
      const slope = distDiff > 0 ? (eleDiff / distDiff) * 100 : 0;
      
      ctx.beginPath();
      ctx.moveTo(x1, y1);
      ctx.lineTo(x2, y2);
      
      if (slope > 15) ctx.strokeStyle = '#dc2626'; // red-600
      else if (slope > 5) ctx.strokeStyle = '#f97316'; // orange-500
      else if (slope > -5) ctx.strokeStyle = '#84cc16'; // lime-500
      else if (slope > -15) ctx.strokeStyle = '#15803d'; // green-700
      else ctx.strokeStyle = '#3b82f6'; // blue-500
      
      ctx.lineWidth = 2;
      ctx.stroke();
    }

    // Start/End dots
    const firstY = height - ((points[0].ele - minEle) / range) * height;
    const lastY = height - ((points[points.length - 1].ele - minEle) / range) * height;
    
    ctx.beginPath();
    ctx.arc(0, firstY, 2.5, 0, Math.PI * 2);
    ctx.fillStyle = '#84cc16';
    ctx.fill();

    ctx.beginPath();
    ctx.arc(width, lastY, 2.5, 0, Math.PI * 2);
    ctx.fillStyle = '#ec4899';
    ctx.fill();

  }, [points, minEle, maxEle, width, height]);

  return <canvas ref={canvasRef} width={width} height={height} className="bg-slate-900/50 rounded shadow-inner max-w-full" />;
}

export function DataTable({ checkpoints, actionTimeline, minWindow, maxWindow, setMinWindow, setMaxWindow, lang = 'en', activeSection, selectedSection, setSelectedSection, setHoveredSection, mapVisible, setMapVisible }) {
  const [showSettings, setShowSettings] = useState(false);
  const [profileModal, setProfileModal] = useState(null);

  const getActionForETA = (startHrs, endHrs) => {
    if (!actionTimeline) return null;
    const actions = actionTimeline.filter(a => a.startElapsedHours >= startHrs && a.startElapsedHours < endHrs);
    if (actions.length === 0) {
      // If no actions exactly match, grab the one covering the end point
      const fallback = actionTimeline.find(a => endHrs > a.startElapsedHours && endHrs <= a.endElapsedHours);
      if (fallback) return fallback[`action_${lang}`] || fallback.action_en;
      return null;
    }
    return actions.map(a => `- ${a[`action_${lang}`] || a.action_en}`).join('\n');
  };

  const formatTime = (hrs) => {
    const h = Math.floor(hrs);
    const m = Math.round((hrs % 1) * 60).toString().padStart(2, '0');
    return `${h}h ${m}m`;
  };

  const formatPace = (hrsPerKm) => {
    const minsPerKm = hrsPerKm * 60;
    const m = Math.floor(minsPerKm);
    const s = Math.round((minsPerKm % 1) * 60).toString().padStart(2, '0');
    return `${m}:${s}/km`;
  };

  // Find global min/max elevation for consistent sparkline scaling
  const globalMinEle = checkpoints.length > 0 ? Math.min(...checkpoints.map(c => c.ele)) : 0;
  const globalMaxEle = checkpoints.length > 0 ? Math.max(...checkpoints.map(c => c.ele)) : 1000;

  // Pre-calculate cumulative ascent
  const enrichedCheckpoints = checkpoints.map((cp, idx) => {
    let cumulativeAscent = 0;
    for (let i = 1; i <= idx; i++) {
      cumulativeAscent += checkpoints[i].sectionAscent;
    }
    return { ...cp, cumulativeAscent };
  });

  return (
    <div className="flex flex-col h-full">
      <div className="flex flex-col gap-3 mb-4 flex-shrink-0 bg-slate-800 p-3 rounded-xl border border-slate-700">
        <div className="flex justify-between items-center">
          <h2 className="text-xl font-bold text-slate-100">{lang === 'en' ? 'Data Table' : 'Tabela Danych'}</h2>
          <button
            onClick={() => setShowSettings(!showSettings)}
            className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg border text-xs font-bold transition-all cursor-pointer ${
              showSettings 
                ? 'bg-lime-950/40 text-lime-400 border-lime-800 shadow-[0_0_8px_rgba(132,204,22,0.15)]' 
                : 'bg-slate-700 hover:bg-slate-600 text-slate-200 border-slate-600'
            }`}
          >
            ⚙️ {lang === 'en' ? 'Window Settings' : 'Ustawienia okna'}
          </button>
        </div>

        {showSettings && (
          <div className="flex flex-col pt-2 border-t border-slate-700">
            <div className="flex justify-between items-center mb-2">
              <span className="text-xs font-bold text-slate-300">
                {lang === 'en' ? 'Settings' : 'Ustawienia'}
              </span>
              <button
                onClick={() => {
                  setMinWindow(5);
                  setMaxWindow(10);
                }}
                className="px-2 py-1 bg-red-950/40 hover:bg-red-900 text-red-400 border border-red-800 rounded text-[10px] md:text-xs font-bold transition-colors cursor-pointer"
              >
                {lang === 'en' ? 'Reset Settings' : 'Resetuj Ustawienia'}
              </button>
            </div>
            
            <div className="flex flex-wrap gap-4">
              <div className="flex flex-col gap-1 select-none">
                <span className="text-[10px] md:text-xs text-slate-400 font-medium">
                  {lang === 'en' ? 'Min Window (km)' : 'Minimalne okno (km)'}
                </span>
                <div className="flex items-center bg-slate-900 border border-slate-700 rounded overflow-hidden h-[32px] w-28">
                  <button
                    type="button"
                    onClick={() => setMinWindow(Math.max(1, minWindow - 1))}
                    className="w-8 h-full bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold flex items-center justify-center border-r border-slate-700 transition-colors cursor-pointer"
                  >
                    -
                  </button>
                  <input
                    type="number"
                    value={minWindow}
                    onChange={e => setMinWindow(Math.max(1, Number(e.target.value)))}
                    className="w-12 text-center bg-transparent text-white font-mono text-xs md:text-sm focus:outline-none [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                  />
                  <button
                    type="button"
                    onClick={() => setMinWindow(Math.min(50, minWindow + 1))}
                    className="w-8 h-full bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold flex items-center justify-center border-l border-slate-700 transition-colors cursor-pointer"
                  >
                    +
                  </button>
                </div>
              </div>

              <div className="flex flex-col gap-1 select-none">
                <span className="text-[10px] md:text-xs text-slate-400 font-medium">
                  {lang === 'en' ? 'Max Window (km)' : 'Maksymalne okno (km)'}
                </span>
                <div className="flex items-center bg-slate-900 border border-slate-700 rounded overflow-hidden h-[32px] w-28">
                  <button
                    type="button"
                    onClick={() => setMaxWindow(Math.max(1, maxWindow - 1))}
                    className="w-8 h-full bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold flex items-center justify-center border-r border-slate-700 transition-colors cursor-pointer"
                  >
                    -
                  </button>
                  <input
                    type="number"
                    value={maxWindow}
                    onChange={e => setMaxWindow(Math.max(1, Number(e.target.value)))}
                    className="w-12 text-center bg-transparent text-white font-mono text-xs md:text-sm focus:outline-none [appearance:textfield] [&::-webkit-outer-spin-button]:appearance-none [&::-webkit-inner-spin-button]:appearance-none"
                  />
                  <button
                    type="button"
                    onClick={() => setMaxWindow(Math.min(50, maxWindow + 1))}
                    className="w-8 h-full bg-slate-800 hover:bg-slate-700 text-slate-300 font-bold flex items-center justify-center border-l border-slate-700 transition-colors cursor-pointer"
                  >
                    +
                  </button>
                </div>
              </div>
            </div>
          </div>
        )}
      </div>

      <div className="rounded-lg border border-slate-700 shadow-xl bg-slate-800/50 flex-1 overflow-y-auto">
        <table className="w-full text-left border-collapse whitespace-nowrap min-w-[600px]">
          <thead className="sticky top-0 z-30">
            <tr className="bg-slate-800 border-b border-slate-700 text-slate-300 text-[10px] md:text-xs uppercase tracking-wider">
              <th className="p-2 md:p-3 font-semibold bg-slate-800 w-[40px]">Nr</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800">KM</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800">{lang === 'en' ? 'Time' : 'Czas'}</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800">{lang === 'en' ? 'Avg Total' : 'Śr. Całość'}</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800 border-r border-slate-700/50">{lang === 'en' ? 'Section Avg' : 'Śr. Odcinek'}</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800">GAIN / LOSS</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800 min-w-[200px]">{lang === 'en' ? 'Action' : 'Akcja'}</th>
              <th className="p-2 md:p-3 font-semibold bg-slate-800 text-center">{lang === 'en' ? 'Profile' : 'Profil'}</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-800/50">
            {enrichedCheckpoints.slice(1).map((cp, idx) => {
              const realIdx = idx + 1;
              const prevCp = enrichedCheckpoints[realIdx - 1];
              const sectionDist = cp.km - prevCp.km;
              const sectionTime = cp.etaHrs - prevCp.etaHrs;
              const actionText = getActionForETA(prevCp.etaHrs, cp.etaHrs);
              
              // Averages
              const avgPaceTotal = cp.km > 0 ? (cp.etaHrs / cp.km) : 0;
              const avgSpeedTotal = cp.etaHrs > 0 ? (cp.km / cp.etaHrs) : 0;
              const sectionPace = sectionDist > 0 ? (sectionTime / sectionDist) : 0;
              const sectionSpeed = sectionTime > 0 ? (sectionDist / sectionTime) : 0;
              
              const isSelected = activeSection?.id === cp.id;

              return (
                <tr 
                  key={cp.id} 
                  className={`transition-colors cursor-pointer group ${isSelected ? 'bg-cyan-900/30 ring-1 ring-cyan-500/50 z-10 relative' : 'hover:bg-slate-700/50'}`}
                  onMouseEnter={() => setHoveredSection({...cp, actionText, sectionDist})}
                  onMouseLeave={() => setHoveredSection(null)}
                  onClick={() => {
                    if (selectedSection?.id === cp.id) setSelectedSection(null);
                    else setSelectedSection({...cp, actionText, sectionDist});
                  }}
                >
                  <td className="p-2 md:p-3 border-r border-slate-700/30 align-middle">
                    <div className="w-6 h-6 rounded-full bg-slate-800 border border-slate-600 flex items-center justify-center text-[10px] font-bold text-lime-400">
                      {realIdx}
                    </div>
                  </td>
                  
                  <td className="p-2 md:p-3 border-r border-slate-700/30">
                    <div className="flex items-center gap-1.5 font-bold text-slate-200">
                      <MapPin size={14} className={`${isSelected ? 'text-cyan-400 opacity-100' : 'text-slate-500 opacity-50 group-hover:opacity-100'}`} />
                      {cp.km.toFixed(1)}
                    </div>
                    <div className="text-[10px] text-cyan-500 ml-5">+{sectionDist.toFixed(1)} km section</div>
                    <div className="text-[10px] text-slate-500 ml-5 truncate max-w-[180px]" title={cp.name}>{cp.name}</div>
                    {cp.type && (
                      <div className="ml-5 mt-1 select-none">
                        <span className={`inline-block text-[8px] font-bold px-1.5 py-0.5 rounded ${
                          cp.type === 'Peak' ? 'bg-red-950/60 text-red-400 border border-red-800/40' :
                          cp.type === 'Valley' ? 'bg-blue-950/60 text-blue-400 border border-blue-800/40' :
                          cp.type === 'Start' ? 'bg-lime-950/60 text-lime-400 border border-lime-800/40' :
                          cp.type === 'Finish' ? 'bg-pink-950/60 text-pink-400 border border-pink-800/40' :
                          'bg-slate-800 text-slate-400 border border-slate-700'
                        }`}>
                          {cp.type === 'Peak' ? (lang === 'en' ? '▲ PEAK' : '▲ SZCZYT') :
                           cp.type === 'Valley' ? (lang === 'en' ? '▼ VALLEY' : '▼ DOLINA') :
                           cp.type === 'Start' ? 'START' :
                           cp.type === 'Finish' ? (lang === 'en' ? 'FINISH' : 'META') :
                           (lang === 'en' ? '▶ FLAT' : '▶ PŁASKO')}
                        </span>
                      </div>
                    )}
                  </td>
                  
                  <td className="p-2 md:p-3 border-r border-slate-700/30">
                    <div className="font-bold text-orange-400">{formatTime(cp.etaHrs)}</div>
                    <div className="text-[10px] text-slate-500">+{formatTime(sectionTime)}</div>
                  </td>
                  
                  <td className="p-2 md:p-3 border-r border-slate-700/30">
                    <div className="font-semibold text-slate-300">{formatPace(avgPaceTotal)}</div>
                    <div className="text-[10px] text-slate-500">{avgSpeedTotal.toFixed(1)} km/h</div>
                  </td>
                  
                  <td className="p-2 md:p-3 border-r border-slate-700/50 bg-slate-900/20">
                    <div className="font-semibold text-cyan-400">{formatPace(sectionPace)}</div>
                    <div className="text-[10px] text-cyan-500/70">{sectionSpeed.toFixed(1)} km/h</div>
                  </td>
                  
                  <td className="p-2 md:p-3 border-r border-slate-700/30">
                    <div className="font-bold text-slate-200">{Math.round(cp.cumulativeAscent)} m <span className="text-[10px] text-slate-500 font-normal ml-1">total gain</span></div>
                    <div className="text-[10px] flex gap-2">
                      <span className="text-lime-500">+{Math.round(cp.sectionAscent)} m</span>
                      <span className="text-red-400">-{Math.round(cp.sectionDescent)} m</span>
                    </div>
                  </td>
                  
                  <td className="p-2 md:p-3 border-r border-slate-700/30">
                    <div className="text-[10px] md:text-xs text-slate-400 whitespace-pre-wrap break-words max-w-[250px] leading-tight">
                      {actionText || '-'}
                    </div>
                  </td>
                  
                  <td className="p-1 text-center align-middle" onClick={(e) => { e.stopPropagation(); setProfileModal(cp); }}>
                    <div className="flex justify-center cursor-zoom-in hover:opacity-80 transition-opacity" title="Click to expand profile">
                       <SparklineProfile points={cp.sectionPoints} minEle={globalMinEle} maxEle={globalMaxEle} />
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
          <tfoot className="sticky bottom-0 z-20">
            {(() => {
               const finalCp = enrichedCheckpoints[enrichedCheckpoints.length - 1];
               if (!finalCp) return null;
               const totalKm = finalCp.km;
               const totalTime = finalCp.etaHrs;
               const avgPace = totalKm > 0 ? (totalTime / totalKm) : 0;
               const avgSpeed = totalTime > 0 ? (totalKm / totalTime) : 0;
               const totalAscent = finalCp.cumulativeAscent;
               // approximate total descent from sections
               const totalDescent = enrichedCheckpoints.reduce((sum, cp) => sum + (cp.sectionDescent || 0), 0);
               
               return (
                 <tr className="bg-slate-900 border-t-2 border-slate-700 text-slate-300 font-bold shadow-[0_-5px_15px_rgba(0,0,0,0.3)]">
                   <td className="p-2 md:p-3 text-center border-r border-slate-700/50">
                     <span className="text-lime-400">Σ</span>
                   </td>
                   <td className="p-2 md:p-3 border-r border-slate-700/50">
                     <div className="text-lime-400">{totalKm.toFixed(1)} km</div>
                     <div className="text-[10px] text-slate-500 font-normal">{lang === 'en' ? 'Total Distance' : 'Całkowity Dystans'}</div>
                   </td>
                   <td className="p-2 md:p-3 border-r border-slate-700/50">
                     <div className="text-orange-400">{formatTime(totalTime)}</div>
                     <div className="text-[10px] text-slate-500 font-normal">{lang === 'en' ? 'Total ETA' : 'Całkowity ETA'}</div>
                   </td>
                   <td className="p-2 md:p-3 border-r border-slate-700/50">
                     <div className="text-slate-200">{formatPace(avgPace)}</div>
                     <div className="text-[10px] text-slate-500 font-normal">{avgSpeed.toFixed(1)} km/h</div>
                   </td>
                   <td className="p-2 md:p-3 border-r border-slate-700/50 bg-slate-900">
                     {/* empty */}
                   </td>
                   <td className="p-2 md:p-3 border-r border-slate-700/50">
                     <div className="text-slate-200">{Math.round(totalAscent)} m</div>
                     <div className="text-[10px] flex gap-2 font-normal">
                       <span className="text-lime-500">+{Math.round(totalAscent)}</span>
                       <span className="text-red-400">-{Math.round(totalDescent)}</span>
                     </div>
                   </td>
                   <td colSpan="2" className="p-2 md:p-3 text-[10px] md:text-xs text-slate-400 text-right align-middle">
                     {lang === 'en' ? 'EST. TOTAL TIME:' : 'SZAC. CZAS CAŁK.:'} <span className="text-lime-400 ml-1 text-sm">{formatTime(totalTime)}</span>
                   </td>
                 </tr>
               );
            })()}
          </tfoot>
        </table>
      </div>

      {/* Profile Modal */}
      {profileModal && createPortal(
        <div className="fixed inset-0 z-[9999] flex items-center justify-center p-4 sm:p-8 bg-slate-950/80 backdrop-blur-sm pointer-events-auto">
          <div className="bg-slate-900 border border-slate-700 shadow-2xl rounded-xl overflow-hidden w-full max-w-4xl max-h-full flex flex-col pointer-events-auto">
            <div className="bg-slate-800 p-4 border-b border-slate-700 flex justify-between items-center">
              <h3 className="text-xl font-bold text-slate-100">Section Profile: {profileModal.name}</h3>
              <button onClick={() => setProfileModal(null)} className="text-slate-400 hover:text-white bg-slate-800 p-2 rounded-lg"><X size={20} /></button>
            </div>
            <div className="p-6 flex flex-col items-center">
              <div className="w-full flex justify-center mb-4 overflow-hidden">
                <SparklineProfile points={profileModal.sectionPoints} minEle={globalMinEle} maxEle={globalMaxEle} width={800} height={300} />
              </div>
              <div className="flex justify-between w-full text-slate-400 text-sm">
                <div>Start: <span className="text-lime-400">{Math.round(profileModal.sectionPoints[0].ele)}m</span></div>
                <div>Gain: <span className="text-lime-400">+{Math.round(profileModal.sectionAscent)}m</span> / <span className="text-red-400">-{Math.round(profileModal.sectionDescent)}m</span></div>
                <div>End: <span className="text-pink-400">{Math.round(profileModal.sectionPoints[profileModal.sectionPoints.length - 1].ele)}m</span></div>
              </div>
            </div>
          </div>
        </div>,
        document.body
      )}
    </div>
  );
}
