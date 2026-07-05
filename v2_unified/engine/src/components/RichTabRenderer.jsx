import React from 'react';

const THEME_MAP = {
  cyan: 'text-cyan-400 border-cyan-500/30 bg-cyan-500/10',
  emerald: 'text-emerald-400 border-emerald-500/30 bg-emerald-500/10',
  red: 'text-red-400 border-red-500/30 bg-red-500/10',
  orange: 'text-orange-400 border-orange-500/30 bg-orange-500/10',
  lime: 'text-lime-400 border-lime-500/30 bg-lime-500/10',
  blue: 'text-blue-400 border-blue-500/30 bg-blue-500/10',
  gray: 'text-slate-400 border-slate-500/30 bg-slate-500/10',
  amber: 'text-amber-400 border-amber-500/30 bg-amber-500/10',
};

const PILL_MAP = {
  cyan: 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30',
  emerald: 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30',
  red: 'bg-red-500/20 text-red-300 border border-red-500/30',
  orange: 'bg-orange-500/20 text-orange-300 border border-orange-500/30',
  lime: 'bg-lime-500/20 text-lime-300 border border-lime-500/30',
  blue: 'bg-blue-500/20 text-blue-300 border border-blue-500/30',
  gray: 'bg-slate-500/20 text-slate-300 border border-slate-500/30',
  amber: 'bg-amber-500/20 text-amber-300 border border-amber-500/30',
};

export function RichTabRenderer({ data, type, lang = 'en' }) {
  if (!data) return <div className="text-slate-500 text-center p-8">{lang === 'en' ? 'No data available' : 'Brak danych'}</div>;

  const t = (item, key) => item[`${key}_${lang}`] || item[`${key}_en`];

  if (type === 'tactics') {
    return (
      <div className="space-y-4">
        <h2 className="text-xl font-bold text-slate-100 mb-6">{lang === 'en' ? 'Tactics' : 'Taktyka'}</h2>
        {data.map((item, idx) => (
          <div key={idx} className={`p-4 rounded-xl border ${THEME_MAP[item.themeColor] || THEME_MAP.gray}`}>
            <div className="flex items-center gap-3 mb-2">
              <span className="text-2xl">{item.icon}</span>
              <h3 className="font-bold text-lg">{t(item, 'title')}</h3>
            </div>
            <p className="text-sm opacity-90">{t(item, 'description')}</p>
          </div>
        ))}
      </div>
    );
  }

  if (type === 'inventory') {
    return (
      <div className="space-y-6">
        <h2 className="text-xl font-bold text-slate-100 mb-6">{lang === 'en' ? 'Inventory' : 'Sprzęt'}</h2>
        {data.map((cat, idx) => (
          <div key={idx} className="space-y-3">
            <h3 className="font-bold text-slate-200 border-b border-slate-700 pb-2">{t(cat, 'category')}</h3>
            
            {cat.displayMode === 'pills' ? (
              <div className="flex flex-wrap gap-2">
                {cat.items.map((item, i) => (
                  <span key={i} className={`px-3 py-1.5 rounded-full text-sm flex items-center gap-2 ${PILL_MAP[cat.themeColor] || PILL_MAP.gray}`}>
                    {item.icon} {t(item, 'text')}
                  </span>
                ))}
              </div>
            ) : (
              <ul className="space-y-2">
                {cat.items.map((item, i) => (
                  <li key={i} className={`flex items-start gap-3 p-3 rounded-lg border ${item.isCritical ? THEME_MAP.red : (THEME_MAP[cat.themeColor] || THEME_MAP.gray)}`}>
                    <span className="mt-0.5">{item.icon}</span>
                    <span className="text-sm">{t(item, 'text')}</span>
                  </li>
                ))}
              </ul>
            )}
          </div>
        ))}
      </div>
    );
  }

  if (type === 'schedule') {
    return (
      <div className="space-y-4">
        <h2 className="text-xl font-bold text-slate-100 mb-6">{lang === 'en' ? 'Timeline Events' : 'Oś Czasu'}</h2>
        <div className="relative border-l-2 border-slate-700 ml-4 space-y-8 pb-8">
          {data.map((event, idx) => {
            const badges = event[`badges_${lang}`] || event.badges_en;
            const kmTitle = event.startKm === event.endKm ? `${event.startKm} km` : `${event.startKm} - ${event.endKm} km`;
            // If the dotColor is red/green/yellow, use it, else default
            const colorClass = PILL_MAP[event.dotColor] || PILL_MAP.gray;
            const textThemeMap = {
              green: 'text-lime-400',
              red: 'text-red-400',
              blue: 'text-cyan-400',
              orange: 'text-orange-400',
              yellow: 'text-amber-400',
              cyan: 'text-cyan-400',
              emerald: 'text-emerald-400',
            };
            const titleColor = textThemeMap[event.dotColor] || 'text-slate-200';
            
            return (
              <div key={idx} className="relative pl-6">
                <div className={`absolute -left-[9px] top-1.5 w-4 h-4 rounded-full border-2 border-slate-900 ${colorClass}`}></div>
                <div className="flex flex-wrap items-center gap-3 mb-1">
                  <h3 className={`font-bold text-xl ${titleColor}`}>{kmTitle} {event.dotColor === 'green' || event.title_en?.includes('DROP BAG') ? '- DROP BAG' : ''}</h3>
                  {badges && (
                    <div className="flex gap-2">
                      {badges.map((b, i) => (
                        <span key={i} className="text-xs bg-slate-800/80 text-slate-300 px-2 py-1 rounded border border-slate-700">
                          {b}
                        </span>
                      ))}
                    </div>
                  )}
                </div>
                <p className="text-sm text-slate-300">{t(event, 'description')}</p>
              </div>
            );
          })}
        </div>
      </div>
    );
  }

  return null;
}
