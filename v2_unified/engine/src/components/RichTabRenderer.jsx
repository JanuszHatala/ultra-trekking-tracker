import React, { useState, useEffect } from 'react';

const THEME_MAP = {
  cyan: 'text-cyan-400 border-cyan-500/30 bg-cyan-500/10 hover:bg-cyan-500/20',
  emerald: 'text-emerald-400 border-emerald-500/30 bg-emerald-500/10 hover:bg-emerald-500/20',
  red: 'text-red-400 border-red-500/30 bg-red-500/10 hover:bg-red-500/20',
  orange: 'text-orange-400 border-orange-500/30 bg-orange-500/10 hover:bg-orange-500/20',
  lime: 'text-lime-400 border-lime-500/30 bg-lime-500/10 hover:bg-lime-500/20',
  blue: 'text-blue-400 border-blue-500/30 bg-blue-500/10 hover:bg-blue-500/20',
  gray: 'text-slate-400 border-slate-500/30 bg-slate-500/10 hover:bg-slate-500/20',
  amber: 'text-amber-400 border-amber-500/30 bg-amber-500/10 hover:bg-amber-500/20',
};

const PILL_MAP = {
  cyan: 'bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 hover:bg-cyan-500/30',
  emerald: 'bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 hover:bg-emerald-500/30',
  red: 'bg-red-500/20 text-red-300 border border-red-500/30 hover:bg-red-500/30',
  orange: 'bg-orange-500/20 text-orange-300 border border-orange-500/30 hover:bg-orange-500/30',
  lime: 'bg-lime-500/20 text-lime-300 border border-lime-500/30 hover:bg-lime-500/30',
  blue: 'bg-blue-500/20 text-blue-300 border border-blue-500/30 hover:bg-blue-500/30',
  gray: 'bg-slate-500/20 text-slate-300 border border-slate-500/30 hover:bg-slate-500/30',
  amber: 'bg-amber-500/20 text-amber-300 border border-amber-500/30 hover:bg-amber-500/30',
};

export function RichTabRenderer({ data, type, lang = 'en', routeId }) {
  const [checkedItems, setCheckedItems] = useState({});
  const [customInventoryItems, setCustomInventoryItems] = useState([]);
  const [newCustomItemName, setNewCustomItemName] = useState('');
  const [editingCustomItem, setEditingCustomItem] = useState(null);
  const [editingCustomItemName, setEditingCustomItemName] = useState('');

  useEffect(() => {
    if (type === 'inventory' && routeId) {
      try {
        const saved = localStorage.getItem(`ultra_inventory_${routeId}`);
        if (saved) setCheckedItems(JSON.parse(saved));
        else setCheckedItems({});
        
        const savedCustom = localStorage.getItem(`ultra_inventory_custom_${routeId}`);
        if (savedCustom) setCustomInventoryItems(JSON.parse(savedCustom));
        else setCustomInventoryItems([]);
      } catch (e) {
        setCheckedItems({});
        setCustomInventoryItems([]);
      }
    }
  }, [type, routeId]);

  const toggleCheck = (itemId) => {
    const nextState = { ...checkedItems, [itemId]: !checkedItems[itemId] };
    setCheckedItems(nextState);
    if (routeId) {
      try {
        localStorage.setItem(`ultra_inventory_${routeId}`, JSON.stringify(nextState));
      } catch (e) {}
    }
  };

  const addCustomItem = (e) => {
    e.preventDefault();
    if (!newCustomItemName.trim()) return;
    
    const nextItems = [...customInventoryItems, newCustomItemName.trim()];
    setCustomInventoryItems(nextItems);
    setNewCustomItemName('');
    if (routeId) {
      try {
        localStorage.setItem(`ultra_inventory_custom_${routeId}`, JSON.stringify(nextItems));
      } catch (e) {}
    }
  };

  const removeCustomItem = (itemName) => {
    const nextItems = customInventoryItems.filter(i => i !== itemName);
    setCustomInventoryItems(nextItems);
    if (routeId) {
      try {
        localStorage.setItem(`ultra_inventory_custom_${routeId}`, JSON.stringify(nextItems));
      } catch (e) {}
    }
    const itemId = `Custom Items-${itemName}`;
    if (checkedItems[itemId]) {
      const nextState = { ...checkedItems };
      delete nextState[itemId];
      setCheckedItems(nextState);
      if (routeId) {
        localStorage.setItem(`ultra_inventory_${routeId}`, JSON.stringify(nextState));
      }
    }
  };

  const startEditingCustomItem = (itemName) => {
    setEditingCustomItem(itemName);
    setEditingCustomItemName(itemName);
  };

  const saveEditedCustomItem = (oldName) => {
    if (!editingCustomItemName.trim() || editingCustomItemName.trim() === oldName) {
      setEditingCustomItem(null);
      return;
    }
    const newName = editingCustomItemName.trim();
    const nextItems = customInventoryItems.map(i => i === oldName ? newName : i);
    setCustomInventoryItems(nextItems);
    if (routeId) {
      try {
        localStorage.setItem(`ultra_inventory_custom_${routeId}`, JSON.stringify(nextItems));
      } catch (e) {}
    }
    
    const oldId = `Custom Items-${oldName}`;
    const newId = `Custom Items-${newName}`;
    if (checkedItems[oldId]) {
      const nextState = { ...checkedItems, [newId]: true };
      delete nextState[oldId];
      setCheckedItems(nextState);
      if (routeId) {
        localStorage.setItem(`ultra_inventory_${routeId}`, JSON.stringify(nextState));
      }
    }
    setEditingCustomItem(null);
  };

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
    let displayData = [...data];
    if (customInventoryItems.length > 0) {
      displayData.push({
        category_en: "Custom Items",
        category_pl: "Własne Rzeczy",
        displayMode: "list",
        themeColor: "amber",
        items: customInventoryItems.map(name => ({
          icon: "📌",
          text_en: name,
          text_pl: name
        }))
      });
    }

    return (
      <div className="space-y-6 pb-8">
        <div className="flex justify-between items-center mb-6 border-b border-slate-700 pb-2">
          <h2 className="text-xl font-bold text-slate-100">{lang === 'en' ? 'Inventory' : 'Sprzęt'}</h2>
          <button 
            onClick={() => {
              if(window.confirm(lang === 'en' ? 'Clear all checked items?' : 'Wyczyścić zaznaczenia?')) {
                setCheckedItems({});
                if(routeId) localStorage.removeItem(`ultra_inventory_${routeId}`);
              }
            }}
            className="text-xs bg-slate-800 text-slate-400 hover:text-slate-200 px-3 py-1.5 rounded border border-slate-700 transition-colors cursor-pointer"
          >
            {lang === 'en' ? 'Reset' : 'Resetuj'}
          </button>
        </div>
        
        {displayData.map((cat, idx) => {
          const checkedCount = cat.items.filter(item => checkedItems[`${cat.category_en}-${item.text_en}`]).length;
          const isAllChecked = checkedCount === cat.items.length && cat.items.length > 0;
          
          return (
          <div key={idx} className="space-y-3">
            <div className="flex justify-between items-center border-b border-slate-700/50 pb-1">
              <h3 className={`font-bold transition-colors ${isAllChecked ? 'text-lime-500' : 'text-slate-200'}`}>
                {t(cat, 'category')}
              </h3>
              <span className="text-xs font-mono text-slate-500">{checkedCount}/{cat.items.length}</span>
            </div>
            
            {cat.displayMode === 'pills' ? (
              <div className="flex flex-wrap gap-2">
                {cat.items.map((item, i) => {
                  const itemId = `${cat.category_en}-${item.text_en}`;
                  const isChecked = checkedItems[itemId] || false;
                  return (
                  <button 
                    key={i} 
                    onClick={() => toggleCheck(itemId)}
                    className={`px-3 py-1.5 rounded-full text-sm flex items-center gap-2 cursor-pointer transition-colors ${isChecked ? 'bg-slate-800/80 text-slate-500 border-slate-700/50 opacity-60 line-through' : (PILL_MAP[cat.themeColor] || PILL_MAP.gray)}`}
                  >
                    <span className={isChecked ? 'grayscale' : ''}>{item.icon}</span> {t(item, 'text')}
                  </button>
                )})}
              </div>
            ) : (
              <ul className="space-y-2">
                {cat.items.map((item, i) => {
                  const itemId = `${cat.category_en}-${item.text_en}`;
                  const isChecked = checkedItems[itemId] || false;
                  return (
                  <li 
                    key={i} 
                    onClick={() => { if(editingCustomItem !== item.text_en) toggleCheck(itemId); }}
                    className={`group relative flex items-start gap-3 p-3 rounded-lg border cursor-pointer transition-all ${isChecked ? 'bg-slate-800/40 border-slate-700/50 opacity-50' : (item.isCritical ? THEME_MAP.red : (THEME_MAP[cat.themeColor] || THEME_MAP.gray))}`}
                  >
                    <div className="mt-0.5 flex-shrink-0 flex items-center justify-center">
                       {isChecked ? (
                          <div className="w-5 h-5 rounded bg-lime-500 flex items-center justify-center text-slate-900">
                             <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                          </div>
                       ) : (
                          <div className={`w-5 h-5 rounded border-2 ${item.isCritical ? 'border-red-500/50' : 'border-slate-500/60'}`}></div>
                       )}
                    </div>
                    <span className={`mt-0.5 text-lg transition-all ${isChecked ? 'grayscale scale-90' : 'scale-100'}`}>{item.icon}</span>
                    
                    {editingCustomItem === item.text_en ? (
                      <div className="flex-1 flex gap-2" onClick={e => e.stopPropagation()}>
                        <input
                          type="text"
                          value={editingCustomItemName}
                          onChange={e => setEditingCustomItemName(e.target.value)}
                          onKeyDown={e => {
                            if(e.key === 'Enter') saveEditedCustomItem(item.text_en);
                            if(e.key === 'Escape') setEditingCustomItem(null);
                          }}
                          autoFocus
                          className="flex-1 bg-slate-950 border border-slate-700 rounded px-2 py-1 text-sm text-slate-200 focus:outline-none focus:border-cyan-500"
                        />
                        <button onClick={() => saveEditedCustomItem(item.text_en)} className="text-lime-500 hover:text-lime-400 p-1">
                          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>
                        </button>
                      </div>
                    ) : (
                      <span className={`text-sm transition-all flex-1 ${isChecked ? 'line-through text-slate-400' : ''}`}>{t(item, 'text')}</span>
                    )}
                    
                    {cat.category_en === 'Custom Items' && editingCustomItem !== item.text_en && (
                       <div className="absolute right-3 top-1/2 -translate-y-1/2 flex items-center gap-1 opacity-0 group-hover:opacity-100 transition-opacity">
                         <button
                           onClick={(e) => { e.stopPropagation(); startEditingCustomItem(item.text_en); }}
                           className="p-2 text-slate-500 hover:text-cyan-400"
                           title={lang === 'en' ? 'Edit' : 'Edytuj'}
                         >
                           <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><path d="M12 20h9"></path><path d="M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"></path></svg>
                         </button>
                         <button
                           onClick={(e) => { e.stopPropagation(); removeCustomItem(item.text_en); }}
                           className="p-2 text-slate-500 hover:text-red-400"
                           title={lang === 'en' ? 'Delete' : 'Usuń'}
                         >
                           <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><line x1="18" y1="6" x2="6" y2="18"></line><line x1="6" y1="6" x2="18" y2="18"></line></svg>
                         </button>
                       </div>
                    )}
                  </li>
                )})}
              </ul>
            )}
          </div>
        )})}
        
        <form onSubmit={addCustomItem} className="mt-6 flex gap-2">
           <input 
             type="text" 
             value={newCustomItemName}
             onChange={e => setNewCustomItemName(e.target.value)}
             placeholder={lang === 'en' ? 'Add custom item...' : 'Dodaj własną rzecz...'}
             className="flex-1 bg-slate-800 border border-slate-700 rounded px-3 py-2 text-sm text-slate-200 placeholder:text-slate-500 focus:outline-none focus:border-cyan-500"
           />
           <button type="submit" className="bg-slate-700 hover:bg-slate-600 text-slate-200 px-4 py-2 rounded text-sm transition-colors border border-slate-600">
             {lang === 'en' ? 'Add' : 'Dodaj'}
           </button>
        </form>
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
