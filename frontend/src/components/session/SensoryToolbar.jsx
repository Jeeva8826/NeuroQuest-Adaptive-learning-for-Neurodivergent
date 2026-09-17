import React from 'react';
import { useSensory } from '../../context/SensoryContext';
import { Sliders, RotateCcw } from 'lucide-react';

const SensoryToolbar = () => {
  const {
    activeSensoryMode,
    isManualOverride,
    setManualSensoryMode,
    resetManualOverride,
    SENSORY_MODES
  } = useSensory();

  return (
    <div className="bg-white/90 backdrop-blur-md rounded-2xl p-2.5 border border-slate-200/80 shadow-sm flex flex-wrap items-center justify-between gap-2">
      
      <div className="flex items-center gap-1.5 text-xs font-extrabold text-slate-700">
        <Sliders className="w-3.5 h-3.5 text-indigo-600" />
        <span>Sensory Mode:</span>
      </div>

      <div className="flex flex-wrap items-center gap-1.5">
        {Object.values(SENSORY_MODES).map(mode => {
          const isSelected = activeSensoryMode === mode.id;
          return (
            <button
              key={mode.id}
              type="button"
              onClick={() => setManualSensoryMode(mode.id)}
              title={mode.desc}
              className={`px-3 py-1.5 rounded-xl text-xs font-bold transition-all flex items-center gap-1 border ${
                isSelected
                  ? 'bg-slate-900 text-white border-slate-900 shadow-sm'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              <span>{mode.icon}</span>
              <span>{mode.name}</span>
            </button>
          );
        })}

        {isManualOverride && (
          <button
            type="button"
            onClick={resetManualOverride}
            title="Reset to AI Recommended Mode"
            className="px-2.5 py-1.5 rounded-xl text-xs font-semibold bg-indigo-50 text-indigo-700 border border-indigo-200 hover:bg-indigo-100 transition-colors flex items-center gap-1"
          >
            <RotateCcw className="w-3 h-3" />
            <span>AI Auto</span>
          </button>
        )}
      </div>

    </div>
  );
};

export default SensoryToolbar;
