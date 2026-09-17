import React, { useState } from 'react';
import { Info, Check, Sparkles, ChevronDown, ChevronUp } from 'lucide-react';

const AdaptationExplainer = ({ explainerData }) => {
  const [expanded, setExpanded] = useState(true);

  if (!explainerData) return null;

  const { title, current_state, ui_mode, theme_applied, adaptation_reasons, non_medical_disclaimer } = explainerData;

  return (
    <div className="bg-indigo-950 text-white rounded-3xl p-5 border border-indigo-400/40 shadow-xl space-y-3 animate-fadeIn">
      <div className="flex items-center justify-between cursor-pointer" onClick={() => setExpanded(!expanded)}>
        <div className="flex items-center gap-2">
          <div className="w-8 h-8 rounded-xl bg-indigo-500/30 text-indigo-300 flex items-center justify-center font-bold border border-indigo-400/30">
            <Sparkles className="w-4 h-4" />
          </div>
          <div>
            <span className="text-[10px] uppercase font-extrabold text-indigo-300 tracking-wider">Judge Adaptation Explainer</span>
            <h4 className="text-sm font-black text-white">{title}</h4>
          </div>
        </div>

        <button className="text-indigo-300 hover:text-white">
          {expanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
        </button>
      </div>

      {expanded && (
        <div className="space-y-3 pt-2 border-t border-indigo-900/80">
          <div className="flex flex-wrap gap-2 text-xs font-extrabold">
            <span className="px-2.5 py-1 rounded-lg bg-indigo-800/80 text-indigo-200 border border-indigo-700">
              State: {current_state}
            </span>
            <span className="px-2.5 py-1 rounded-lg bg-indigo-800/80 text-indigo-200 border border-indigo-700">
              UI Mode: {ui_mode}
            </span>
            <span className="px-2.5 py-1 rounded-lg bg-indigo-800/80 text-indigo-200 border border-indigo-700">
              Theme: {theme_applied}
            </span>
          </div>

          <div className="space-y-1.5 bg-indigo-900/40 p-3 rounded-2xl border border-indigo-800/60">
            {adaptation_reasons?.map((reason, idx) => (
              <div key={idx} className="flex items-start gap-2 text-xs text-indigo-100 font-medium">
                <Check className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span>{reason}</span>
              </div>
            ))}
          </div>

          <div className="text-[10px] text-indigo-400 font-semibold italic">
            {non_medical_disclaimer}
          </div>
        </div>
      )}
    </div>
  );
};

export default AdaptationExplainer;
