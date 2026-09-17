import React, { useState } from 'react';
import { Sparkles, ChevronDown, ChevronUp, RotateCcw, Check, Sliders, ShieldCheck } from 'lucide-react';

const AdaptationExplainer = ({ explainerData, onKeep, onChangeMode, onUndo }) => {
  const [expanded, setExpanded] = useState(true);
  const [userChoice, setUserChoice] = useState(null); // 'kept' | 'undone' | 'changed'

  if (!explainerData) return null;

  const {
    title = 'Why Did This Change?',
    current_state = 'ATTENTION_DRIFT',
    ui_mode = 'focus',
    theme_applied = 'Space',
    adaptation_reasons = [],
    what_changed = 'Simplified single-question view with dimmed background elements and increased line spacing.',
    why_it_changed = 'To reduce competing visual stimuli and help you focus comfortably on one step at a time.',
    what_signal_used = 'Interaction pacing: consecutive hesitation and rapid clicks detected in telemetry stream.',
    non_medical_disclaimer = 'Adaptations are non-diagnostic educational adjustments designed for learner comfort and agency.'
  } = explainerData;

  const handleKeep = () => {
    setUserChoice('kept');
    if (onKeep) onKeep();
  };

  const handleUndo = () => {
    setUserChoice('undone');
    if (onUndo) onUndo();
  };

  return (
    <aside 
      aria-label="Adaptation Explanation and Controls" 
      className="bg-white/95 text-slate-900 rounded-3xl p-5 sm:p-6 border border-indigo-200/80 shadow-md space-y-4 transition-all"
    >
      {/* Header bar */}
      <div 
        className="flex items-center justify-between cursor-pointer select-none" 
        onClick={() => setExpanded(!expanded)}
      >
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-2xl bg-indigo-100 text-indigo-700 flex items-center justify-center font-bold border border-indigo-200 shadow-xs">
            <Sparkles className="w-4 h-4" />
          </div>
          <div>
            <div className="flex items-center gap-2">
              <span className="text-[10px] uppercase font-bold text-indigo-600 tracking-wider bg-indigo-50 px-2 py-0.5 rounded-md border border-indigo-100">
                Transparent AI Explanation
              </span>
              <span className="text-[10px] font-semibold text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-md border border-emerald-200 flex items-center gap-1">
                <ShieldCheck className="w-3 h-3" /> Learner in Control
              </span>
            </div>
            <h4 className="text-base font-bold text-slate-900 mt-0.5">
              Why Did This Change?
            </h4>
          </div>
        </div>

        <button 
          type="button" 
          aria-expanded={expanded}
          aria-label={expanded ? "Collapse explanation" : "Expand explanation"}
          className="text-slate-400 hover:text-slate-700 p-1.5 rounded-xl hover:bg-slate-100 transition-all"
        >
          {expanded ? <ChevronUp className="w-5 h-5" /> : <ChevronDown className="w-5 h-5" />}
        </button>
      </div>

      {expanded && (
        <div className="space-y-4 pt-2 border-t border-slate-100">
          {/* 3 Core Transparent Dimensions: What Changed, Why, What Signal */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
            {/* 1. What Changed */}
            <div className="p-3.5 rounded-2xl bg-indigo-50/70 border border-indigo-100 space-y-1">
              <span className="text-[11px] font-bold uppercase tracking-wider text-indigo-800">
                1. What Changed
              </span>
              <p className="text-xs text-slate-700 font-medium leading-relaxed">
                {what_changed}
              </p>
              <div className="pt-1 flex flex-wrap gap-1">
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-white text-indigo-900 border border-indigo-200">
                  Mode: {ui_mode}
                </span>
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-white text-indigo-900 border border-indigo-200">
                  Theme: {theme_applied}
                </span>
              </div>
            </div>

            {/* 2. Why It Changed */}
            <div className="p-3.5 rounded-2xl bg-emerald-50/70 border border-emerald-100 space-y-1">
              <span className="text-[11px] font-bold uppercase tracking-wider text-emerald-800">
                2. Why It Changed
              </span>
              <p className="text-xs text-slate-700 font-medium leading-relaxed">
                {why_it_changed}
              </p>
              <div className="pt-1">
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-white text-emerald-900 border border-emerald-200">
                  Goal: Cognitive Comfort
                </span>
              </div>
            </div>

            {/* 3. What Signal Was Used */}
            <div className="p-3.5 rounded-2xl bg-amber-50/70 border border-amber-100 space-y-1">
              <span className="text-[11px] font-bold uppercase tracking-wider text-amber-800">
                3. Signal Used
              </span>
              <p className="text-xs text-slate-700 font-medium leading-relaxed">
                {what_signal_used}
              </p>
              <div className="pt-1">
                <span className="text-[10px] font-bold px-2 py-0.5 rounded-md bg-white text-amber-900 border border-amber-200">
                  State: {current_state}
                </span>
              </div>
            </div>
          </div>

          {/* Adaptation Reasons list */}
          {adaptation_reasons.length > 0 && (
            <div className="p-3 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
              <span className="text-[11px] font-bold text-slate-700 block">
                Educational Rationale:
              </span>
              {adaptation_reasons.map((reason, idx) => (
                <div key={idx} className="flex items-start gap-2 text-xs text-slate-600 font-medium">
                  <Check className="w-3.5 h-3.5 text-emerald-600 shrink-0 mt-0.5" />
                  <span>{reason}</span>
                </div>
              ))}
            </div>
          )}

          {/* Learner Control Actions: KEEP / CHANGE / UNDO */}
          <div className="pt-1 flex flex-wrap items-center justify-between gap-3 border-t border-slate-100">
            <span className="text-xs text-slate-500 font-medium">
              You always have full control over your learning view:
            </span>

            <div className="flex items-center gap-2">
              <button
                type="button"
                onClick={handleKeep}
                className={`px-3.5 py-1.5 rounded-xl text-xs font-bold border transition-all flex items-center gap-1.5 ${
                  userChoice === 'kept'
                    ? 'bg-emerald-600 text-white border-emerald-600 shadow-xs'
                    : 'bg-white text-slate-700 border-slate-200 hover:bg-slate-50'
                }`}
              >
                <Check className="w-3.5 h-3.5" />
                <span>Keep This</span>
              </button>

              {onChangeMode && (
                <button
                  type="button"
                  onClick={onChangeMode}
                  className="px-3.5 py-1.5 rounded-xl text-xs font-bold bg-white text-slate-700 border border-slate-200 hover:bg-slate-50 transition-all flex items-center gap-1.5"
                >
                  <Sliders className="w-3.5 h-3.5 text-indigo-600" />
                  <span>Customize</span>
                </button>
              )}

              <button
                type="button"
                onClick={handleUndo}
                className={`px-3.5 py-1.5 rounded-xl text-xs font-bold border transition-all flex items-center gap-1.5 ${
                  userChoice === 'undone'
                    ? 'bg-rose-600 text-white border-rose-600 shadow-xs'
                    : 'bg-white text-slate-700 border-slate-200 hover:bg-rose-50 hover:text-rose-700 hover:border-rose-200'
                }`}
              >
                <RotateCcw className="w-3.5 h-3.5" />
                <span>Undo Change</span>
              </button>
            </div>
          </div>

          {/* Non-diagnostic disclaimer */}
          <p className="text-[11px] text-slate-400 font-medium italic text-center">
            {non_medical_disclaimer}
          </p>
        </div>
      )}
    </aside>
  );
};

export default AdaptationExplainer;
