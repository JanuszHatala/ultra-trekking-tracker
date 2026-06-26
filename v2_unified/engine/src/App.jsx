import { useState } from 'react';
import { Map, List, BookOpen, User } from 'lucide-react';

function App() {
  const [activeTab, setActiveTab] = useState('map');

  return (
    <div className="flex flex-col h-screen bg-slate-900 text-slate-100">
      {/* Header */}
      <header className="flex-none p-4 bg-slate-800 border-b border-slate-700 shadow-md z-10 flex justify-between items-center">
        <div>
          <h1 className="text-xl font-bold text-lime-400">Wyrypa Engine</h1>
          <p className="text-xs text-slate-400">Awaiting Dataset...</p>
        </div>
      </header>

      {/* Main Content Area */}
      <main className="flex-grow overflow-hidden relative">
        {activeTab === 'map' && (
          <div className="absolute inset-0 flex items-center justify-center text-slate-500">
            [Map Renderer Placeholder]
          </div>
        )}
        {activeTab === 'table' && (
          <div className="h-full overflow-y-auto p-4 flex items-center justify-center text-slate-500">
            [Dynamic Table Placeholder]
          </div>
        )}
        {activeTab === 'tactics' && (
          <div className="h-full overflow-y-auto p-4 flex items-center justify-center text-slate-500">
            [Tactics & Inventory Placeholder]
          </div>
        )}
        {activeTab === 'profile' && (
          <div className="h-full overflow-y-auto p-4 flex items-center justify-center text-slate-500">
            [User Profile Settings Placeholder]
          </div>
        )}
      </main>

      {/* Bottom Navigation */}
      <nav className="flex-none bg-slate-800 border-t border-slate-700 flex justify-around p-2 pb-safe">
        <button 
          onClick={() => setActiveTab('map')}
          className={`flex flex-col items-center p-2 rounded-lg transition-colors ${activeTab === 'map' ? 'text-lime-400' : 'text-slate-400 hover:text-slate-200'}`}
        >
          <Map size={24} />
          <span className="text-xs mt-1 font-medium">Map</span>
        </button>
        <button 
          onClick={() => setActiveTab('table')}
          className={`flex flex-col items-center p-2 rounded-lg transition-colors ${activeTab === 'table' ? 'text-lime-400' : 'text-slate-400 hover:text-slate-200'}`}
        >
          <List size={24} />
          <span className="text-xs mt-1 font-medium">Table</span>
        </button>
        <button 
          onClick={() => setActiveTab('tactics')}
          className={`flex flex-col items-center p-2 rounded-lg transition-colors ${activeTab === 'tactics' ? 'text-lime-400' : 'text-slate-400 hover:text-slate-200'}`}
        >
          <BookOpen size={24} />
          <span className="text-xs mt-1 font-medium">Tactics</span>
        </button>
        <button 
          onClick={() => setActiveTab('profile')}
          className={`flex flex-col items-center p-2 rounded-lg transition-colors ${activeTab === 'profile' ? 'text-lime-400' : 'text-slate-400 hover:text-slate-200'}`}
        >
          <User size={24} />
          <span className="text-xs mt-1 font-medium">Profile</span>
        </button>
      </nav>
    </div>
  );
}

export default App;
