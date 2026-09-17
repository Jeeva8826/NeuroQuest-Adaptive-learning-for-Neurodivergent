import React from 'react';
import { Lightbulb, Layers, Volume2, Sparkles } from 'lucide-react';
import AudioButton from '../common/AudioButton';

const ScaffoldedHintBox = ({ scaffoldData, onSelectRepresentation }) => {
  if (!scaffoldData) return null;

  const { feedback_message, hint, next_representation, scaffold_step } = scaffoldData;

  return (
    <div className="bg-amber-50/90 border border-amber-200 rounded-3xl p-6 space-y-4 animate-fadeIn shadow-sm">
      <div className="flex items-center justify-between">
        <div className="flex items-center gap-2">
          <div className="w-10 h-10 rounded-2xl bg-amber-400 text-amber-950 flex items-center justify-center font-bold shadow-sm">
            <Lightbulb className="w-5 h-5" />
          </div>
          <div>
            <h4 className="font-extrabold text-amber-950 text-sm">{feedback_message}</h4>
            <span className="text-[11px] font-bold text-amber-700">AI Mentor Gentle Scaffold</span>
          </div>
        </div>

        <AudioButton
          text={`${feedback_message}. ${hint}`}
          label="Listen Hint"
          className="bg-amber-200/80 text-amber-900 border-amber-300 hover:bg-amber-300"
        />
      </div>

      {/* Hint Body */}
      <p className="text-xs text-amber-900 font-medium bg-white/70 p-3.5 rounded-2xl border border-amber-200/60 leading-relaxed">
        {hint}
      </p>

      {/* Scaffold Step Example if present */}
      {scaffold_step && (
        <div className="bg-white rounded-2xl p-4 border border-amber-200 space-y-2">
          <div className="text-xs font-extrabold text-indigo-700 flex items-center gap-1.5">
            <Sparkles className="w-4 h-4" />
            {scaffold_step.step_title}: {scaffold_step.simplified_prompt}
          </div>
          <div className="text-xs font-bold text-emerald-700 bg-emerald-50 px-3 py-1.5 rounded-xl border border-emerald-200">
            Suggested Clue: {scaffold_step.suggested_answer}
          </div>
        </div>
      )}

      {/* Representation Action Buttons */}
      {next_representation && next_representation !== 'standard' && (
        <div className="pt-2 flex flex-wrap items-center gap-2">
          <span className="text-[11px] font-bold text-amber-800">Alternative View Options:</span>
          <button
            onClick={() => onSelectRepresentation && onSelectRepresentation(next_representation)}
            className="px-3.5 py-1.5 rounded-xl bg-amber-200 text-amber-950 text-xs font-bold hover:bg-amber-300 transition-all flex items-center gap-1.5 shadow-sm"
          >
            <Layers className="w-3.5 h-3.5" />
            <span>Switch to {next_representation === 'visual_block' ? 'Visual Diagrams' : 'Simplified Version'}</span>
          </button>
        </div>
      )}
    </div>
  );
};

export default ScaffoldedHintBox;
