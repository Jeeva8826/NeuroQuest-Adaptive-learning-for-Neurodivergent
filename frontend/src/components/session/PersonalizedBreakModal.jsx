import React, { useState } from 'react';
import { Coffee, Wind, Activity, Eye, Volume2, X } from 'lucide-react';
import AudioButton from '../common/AudioButton';

const PersonalizedBreakModal = ({ onClose, breakPreference = 'breathing' }) => {
  const [activeMode, setActiveMode] = useState(breakPreference); // 'breathing', 'rhythm', 'calm_space', 'audio'
  const [fidgetCount, setFidgetCount] = useState(0);

  return (
    <div className="fixed inset-0 z-50 bg-slate-900/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-white rounded-3xl p-6 sm:p-8 max-w-lg w-full shadow-2xl space-y-6 animate-fadeIn relative">
        <button
          onClick={onClose}
          className="absolute top-4 right-4 p-2 text-slate-400 hover:text-slate-700 rounded-full hover:bg-slate-100 transition-all"
        >
          <X className="w-5 h-5" />
        </button>

        {/* Modal Header */}
        <div className="text-center space-y-2">
          <div className="w-14 h-14 rounded-3xl bg-indigo-100 text-indigo-600 mx-auto flex items-center justify-center font-bold">
            <Coffee className="w-7 h-7" />
          </div>
          <h3 className="text-2xl font-black text-slate-900">Personalized Rest & Refresh</h3>
          <p className="text-xs text-slate-600 font-medium max-w-sm mx-auto">
            Take a short, low-stress breather tailored to your sensory comfort.
          </p>
        </div>

        {/* Sensory Break Selector */}
        <div className="grid grid-cols-4 gap-2 bg-slate-100 p-1.5 rounded-2xl text-xs font-bold">
          <button
            onClick={() => setActiveMode('breathing')}
            className={`py-2 rounded-xl transition-all flex flex-col items-center gap-1 ${
              activeMode === 'breathing' ? 'bg-white text-indigo-600 shadow-sm' : 'text-slate-500'
            }`}
          >
            <Wind className="w-4 h-4" />
            <span className="text-[10px]">Breathing</span>
          </button>

          <button
            onClick={() => setActiveMode('rhythm')}
            className={`py-2 rounded-xl transition-all flex flex-col items-center gap-1 ${
              activeMode === 'rhythm' ? 'bg-white text-indigo-600 shadow-sm' : 'text-slate-500'
            }`}
          >
            <Activity className="w-4 h-4" />
            <span className="text-[10px]">Fidget</span>
          </button>

          <button
            onClick={() => setActiveMode('calm_space')}
            className={`py-2 rounded-xl transition-all flex flex-col items-center gap-1 ${
              activeMode === 'calm_space' ? 'bg-white text-indigo-600 shadow-sm' : 'text-slate-500'
            }`}
          >
            <Eye className="w-4 h-4" />
            <span className="text-[10px]">Calm View</span>
          </button>

          <button
            onClick={() => setActiveMode('audio')}
            className={`py-2 rounded-xl transition-all flex flex-col items-center gap-1 ${
              activeMode === 'audio' ? 'bg-white text-indigo-600 shadow-sm' : 'text-slate-500'
            }`}
          >
            <Volume2 className="w-4 h-4" />
            <span className="text-[10px]">Audio</span>
          </button>
        </div>

        {/* Sensory Interactive Area */}
        <div className="bg-slate-50 border border-slate-200/90 rounded-2xl p-6 min-h-[160px] flex items-center justify-center text-center">

          {/* 1. Breathing Circle */}
          {activeMode === 'breathing' && (
            <div className="space-y-4">
              <div className="w-24 h-24 rounded-full bg-indigo-500/20 border-4 border-indigo-500 mx-auto flex items-center justify-center shadow-inner">
                <span className="text-xs font-black text-indigo-700">Inhale... Exhale...</span>
              </div>
              <p className="text-xs text-slate-500 font-medium">Breathe softly and relax.</p>
            </div>
          )}

          {/* 2. Rhythm Fidget Clicker */}
          {activeMode === 'rhythm' && (
            <div className="space-y-3">
              <button
                onClick={() => setFidgetCount(c => c + 1)}
                className="w-20 h-20 rounded-2xl bg-indigo-600 text-white font-black text-xl shadow-lg active:scale-95 transition-all mx-auto flex items-center justify-center"
              >
                {fidgetCount}
              </button>
              <p className="text-xs text-slate-500 font-medium">Tap the fidget pad to clear your mind.</p>
            </div>
          )}

          {/* 3. Visual Calm Space */}
          {activeMode === 'calm_space' && (
            <div className="space-y-3">
              <div className="w-full h-24 rounded-xl bg-gradient-to-r from-sky-900 via-indigo-950 to-slate-900 flex items-center justify-center text-indigo-200 text-xs font-bold shadow-inner">
                ✨ Soft Starlight Drift
              </div>
              <p className="text-xs text-slate-500 font-medium">Rest your eyes on the calm horizon.</p>
            </div>
          )}

          {/* 4. Audio Chime Reset */}
          {activeMode === 'audio' && (
            <div className="space-y-3">
              <AudioButton
                text="Take a moment to rest. When you are ready, resume your quest with fresh energy."
                label="Play Calming Chime"
                className="bg-indigo-600 text-white px-6 py-3"
              />
              <p className="text-xs text-slate-500 font-medium">Listen to a gentle calming chime.</p>
            </div>
          )}

        </div>

        <button
          onClick={onClose}
          className="w-full py-3.5 rounded-2xl text-xs font-extrabold text-white bg-indigo-600 hover:bg-indigo-700 shadow-md transition-all"
        >
          Resume Learning Quest
        </button>
      </div>
    </div>
  );
};

export default PersonalizedBreakModal;
