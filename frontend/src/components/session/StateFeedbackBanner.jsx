import React, { useState } from 'react';
import { Sparkles, Heart, Coffee, X } from 'lucide-react';
import { useSensory } from '../../context/SensoryContext';
import AudioButton from '../common/AudioButton';

const StateFeedbackBanner = ({ onRequestBreak }) => {
  const { currentLearnerState, encouragementMessage } = useSensory();
  const [dismissed, setDismissed] = useState(false);

  if (dismissed || !encouragementMessage) return null;

  const isFatigueOrDisengaged = currentLearnerState === 'POSSIBLE_FATIGUE' || currentLearnerState === 'DISENGAGED';

  return (
    <div className={`p-4 rounded-2xl border-2 transition-all flex flex-wrap items-center justify-between gap-3 ${
      isFatigueOrDisengaged
        ? 'bg-amber-50/90 border-amber-300 text-amber-950'
        : 'bg-indigo-50/90 border-indigo-200 text-indigo-950'
    }`}>
      
      <div className="flex items-center gap-3">
        <div className={`w-9 h-9 rounded-xl flex items-center justify-center shrink-0 ${
          isFatigueOrDisengaged ? 'bg-amber-400 text-amber-950' : 'bg-indigo-600 text-white'
        }`}>
          {isFatigueOrDisengaged ? <Heart className="w-5 h-5 fill-current" /> : <Sparkles className="w-5 h-5 fill-current" />}
        </div>
        <div>
          <span className="text-xs uppercase tracking-wider font-extrabold text-indigo-700 block">
            Your Learning Companion
          </span>
          <p className="text-sm font-bold leading-tight">{encouragementMessage}</p>
        </div>
      </div>

      <div className="flex items-center gap-2">
        {isFatigueOrDisengaged && onRequestBreak && (
          <button
            type="button"
            onClick={onRequestBreak}
            className="px-3.5 py-1.5 rounded-xl bg-amber-400 text-amber-950 text-xs font-black shadow-sm hover:bg-amber-500 transition-colors flex items-center gap-1.5"
          >
            <Coffee className="w-4 h-4" />
            <span>Take 1-Min Breather</span>
          </button>
        )}

        <AudioButton text={encouragementMessage} label="Listen" className="bg-white/80" />

        <button
          type="button"
          onClick={() => setDismissed(true)}
          className="p-1.5 text-slate-400 hover:text-slate-700 rounded-lg"
          title="Dismiss banner"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

    </div>
  );
};

export default StateFeedbackBanner;
