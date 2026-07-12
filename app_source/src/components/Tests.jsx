import React from 'react';

export function Tests({ data, lang }) {
  if (!data || data.length === 0) return null;

  return (
    <div className="space-y-4">
      {data.map((test, idx) => (
        <div key={idx} className={`p-4 md:p-6 rounded-lg border border-${test.themeColor || 'cyan'}-500/30 bg-${test.themeColor || 'cyan'}-900/10 shadow-lg`}>
          <h3 className={`text-lg font-bold text-${test.themeColor || 'cyan'}-400 mb-2 border-b border-${test.themeColor || 'cyan'}-500/30 pb-2`}>
            {test[`title_${lang}`]}
          </h3>
          <p className="text-slate-300 mb-4">{test[`description_${lang}`]}</p>
          
          {test.steps && test.steps.length > 0 && (
            <div className="mb-4">
              <h4 className="text-xs font-bold text-slate-500 uppercase tracking-wider mb-2">
                {lang === 'en' ? 'Protocol' : 'Protokół'}
              </h4>
              <ul className="space-y-2">
                {test.steps.map((step, sIdx) => (
                  <li key={sIdx} className="flex items-start text-sm text-slate-300">
                    <span className="text-emerald-500 mr-2">▶</span>
                    {step[`text_${lang}`]}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {test[`goal_${lang}`] && (
            <div className={`mt-4 p-2 bg-${test.themeColor || 'cyan'}-500/20 rounded text-sm font-semibold text-${test.themeColor || 'cyan'}-300 flex items-center gap-2`}>
              <span>🎯</span> {test[`goal_${lang}`]}
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
