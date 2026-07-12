import React from 'react';

export function Training({ data, lang }) {
  if (!data || data.length === 0) return null;

  return (
    <div className="space-y-4">
      {data.map((item, idx) => (
        <div key={idx} className="flex gap-4 p-4 rounded-lg bg-slate-800/50 border border-slate-700 shadow-sm">
          <div className="text-3xl flex-shrink-0 mt-1">
            {item.icon || '🏃'}
          </div>
          <div>
            <h3 className="text-sm md:text-base font-bold text-lime-400 mb-1">
              {item[`title_${lang}`]}
            </h3>
            <p className="text-xs md:text-sm text-slate-300">
              {item[`description_${lang}`]}
            </p>
          </div>
        </div>
      ))}
    </div>
  );
}
