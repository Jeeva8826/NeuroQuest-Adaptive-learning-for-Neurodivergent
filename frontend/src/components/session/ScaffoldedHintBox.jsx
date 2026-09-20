import React from 'react';
import { Lightbulb, Layers, Sparkles, ChevronRight, HelpCircle, CheckCircle2, XCircle, Compass, BookOpen } from 'lucide-react';
import AudioButton from '../common/AudioButton';

const LEVEL_LABELS = [
  "1. Restate Goal",
  "2. Concept Clue",
  "3. Guiding Q",
  "4. Worked Example",
  "5. Partial Steps",
  "6. Reasoning",
  "7. Full Solution"
];

const SIX_LEVEL_LABELS = [
  "0. Clarify Q",
  "1. Hint",
  "2. Concept Clue",
  "3. Example",
  "4. Step Guide",
  "5. Full Solution"
];

const ScaffoldedHintBox = ({ scaffoldData, onSelectRepresentation, onRequestNextLevel, onDismiss }) => {
  if (!scaffoldData) return null;

  const {
    feedback_message,
    hint,
    next_representation,
    scaffold_step,
    scaffold_level,
    level_name,
    ladder_progress,
    eliminated_options = [],
    clarifying_question,
    concept_explanation,
    guiding_question,
    worked_example,
    partial_step,
    reasoning_walkthrough,
    full_solution,
    learner_agency_choices = []
  } = scaffoldData;

  const is6Level = ladder_progress && ladder_progress.max_levels === 6;
  const currentLevel = (scaffold_level !== undefined && scaffold_level !== null)
    ? scaffold_level
    : ((ladder_progress && ladder_progress.current_level !== undefined) ? ladder_progress.current_level : 1);
  const maxLevels = is6Level ? 6 : 7;
  const canAdvance = ladder_progress && ladder_progress.can_advance !== undefined
    ? ladder_progress.can_advance
    : (currentLevel < (is6Level ? 5 : 7));

  const activeLabels = is6Level ? SIX_LEVEL_LABELS : LEVEL_LABELS;

  return (
    <div className="bg-amber-50/95 border border-amber-200 rounded-3xl p-6 space-y-4 animate-fadeIn shadow-sm text-slate-800">
      {/* Graduated Ladder Stepper Header */}
      <div className="bg-white/80 p-3 rounded-2xl border border-amber-200/80">
        <div className="flex items-center justify-between mb-2">
          <div className="flex items-center gap-1.5 text-xs font-black text-amber-900 uppercase tracking-wider">
            <Sparkles className="w-3.5 h-3.5 text-amber-600" />
            <span>{is6Level ? '6-Level NCERT Scaffolding Ladder' : '7-Level Scaffolding Ladder'} (Never Leaks Solution Early)</span>
          </div>
          <span className="text-[11px] font-bold text-amber-800 bg-amber-100 px-2 py-0.5 rounded-full">
            Level {currentLevel} of {is6Level ? 5 : 7}
          </span>
        </div>

        {/* Level Stepper Bar */}
        <div className={`grid ${is6Level ? 'grid-cols-6' : 'grid-cols-7'} gap-1`}>
          {activeLabels.map((label, idx) => {
            const lvlNum = is6Level ? idx : idx + 1;
            const isCompleted = lvlNum < currentLevel;
            const isCurrent = lvlNum === currentLevel;
            return (
              <div
                key={idx}
                title={label}
                className={`py-1 px-0.5 text-center rounded-lg text-[10px] font-bold transition-all ${
                  isCurrent
                    ? 'bg-amber-500 text-amber-950 shadow-sm ring-2 ring-amber-400'
                    : isCompleted
                    ? 'bg-amber-200 text-amber-900'
                    : 'bg-amber-100/60 text-amber-400 opacity-60'
                }`}
              >
                {lvlNum}
              </div>
            );
          })}
        </div>
      </div>

      {/* Encouraging Feedback Header */}
      <div className="flex items-center justify-between gap-3">
        <div className="flex items-center gap-3">
          <div className="w-10 h-10 rounded-2xl bg-amber-400 text-amber-950 flex items-center justify-center font-bold shadow-sm shrink-0">
            <Lightbulb className="w-5 h-5" />
          </div>
          <div>
            <h4 className="font-extrabold text-amber-950 text-sm leading-snug">{feedback_message}</h4>
            <span className="text-[11px] font-bold text-amber-700">{level_name || `Scaffold Ladder Level ${currentLevel}`}</span>
          </div>
        </div>

        <AudioButton
          text={`${feedback_message}. ${hint}`}
          label="Listen Clue"
          className="bg-amber-200/80 text-amber-900 border-amber-300 hover:bg-amber-300 shrink-0"
        />
      </div>

      {/* Main Hint / Narrative */}
      <div className="text-xs text-amber-900 font-medium bg-white/80 p-3.5 rounded-2xl border border-amber-200/70 leading-relaxed shadow-inner">
        {hint}
      </div>

      {/* Level 0: Clarifying Orienting Question Card */}
      {clarifying_question && (
        <div className="bg-sky-50 border border-sky-200 rounded-2xl p-3.5 flex items-start gap-2.5">
          <Compass className="w-4 h-4 text-sky-700 shrink-0 mt-0.5" />
          <div className="text-xs">
            <span className="font-bold text-sky-900 block mb-1">Level 0: Clarifying Question</span>
            <p className="text-sky-800 italic font-medium">{clarifying_question}</p>
          </div>
        </div>
      )}

      {/* Level 2: Concept Explanation Card */}
      {concept_explanation && (
        <div className="bg-blue-50 border border-blue-200 rounded-2xl p-3.5 space-y-1.5">
          <div className="text-xs font-bold text-blue-900 flex items-center gap-1.5">
            <BookOpen className="w-3.5 h-3.5 text-blue-700" />
            <span>Level 2: Concept Explanation</span>
          </div>
          <p className="text-xs text-blue-800 font-medium leading-relaxed">{concept_explanation}</p>
        </div>
      )}

      {/* Level 2: Eliminated Distractor Card */}
      {eliminated_options && eliminated_options.length > 0 && (
        <div className="bg-rose-50 border border-rose-200 rounded-2xl p-3 flex items-center gap-2.5">
          <XCircle className="w-4 h-4 text-rose-600 shrink-0" />
          <div className="text-xs">
            <span className="font-bold text-rose-900">Cognitive Load Reduction: </span>
            <span className="line-through text-rose-700 font-semibold">{eliminated_options[0]}</span>
            <span className="text-rose-800"> is ruled out! Focus on the remaining choices.</span>
          </div>
        </div>
      )}

      {/* Level 3: Guiding Socratic Question Card */}
      {guiding_question && (
        <div className="bg-sky-50 border border-sky-200 rounded-2xl p-3.5 flex items-start gap-2.5">
          <Compass className="w-4 h-4 text-sky-700 shrink-0 mt-0.5" />
          <div className="text-xs">
            <span className="font-bold text-sky-900 block mb-1">Guiding Socratic Question:</span>
            <p className="text-sky-800 italic font-medium">{guiding_question}</p>
          </div>
        </div>
      )}

      {/* Level 4: Worked Example Card */}
      {worked_example && (
        <div className="bg-emerald-50 border border-emerald-200 rounded-2xl p-3.5 space-y-1.5">
          <div className="text-xs font-bold text-emerald-900 flex items-center gap-1.5">
            <BookOpen className="w-3.5 h-3.5 text-emerald-700" />
            <span>Parallel Worked Example</span>
          </div>
          <p className="text-xs text-emerald-800 font-medium">{worked_example.scenario}</p>
          <div className="text-xs font-bold text-emerald-900 bg-white/80 px-2.5 py-1 rounded-xl border border-emerald-200 inline-block">
            Takeaway: {worked_example.solution}
          </div>
        </div>
      )}

      {/* Level 5: Partial Step Card */}
      {partial_step && (
        <div className="bg-purple-50 border border-purple-200 rounded-2xl p-3.5 space-y-1.5">
          <div className="text-xs font-bold text-purple-900 flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-purple-700" />
            <span>Partial Step (Fill in the Blank)</span>
          </div>
          <p className="text-xs text-purple-800 font-medium">{partial_step.prompt}</p>
          {partial_step.clue && (
            <div className="text-[11px] text-purple-700 italic bg-purple-100/70 px-2 py-0.5 rounded-lg inline-block">
              Clue: {partial_step.clue}
            </div>
          )}
        </div>
      )}

      {/* Level 6: Step-by-Step Reasoning Walkthrough */}
      {reasoning_walkthrough && reasoning_walkthrough.length > 0 && (
        <div className="bg-indigo-50 border border-indigo-200 rounded-2xl p-3.5 space-y-2">
          <div className="text-xs font-bold text-indigo-900 flex items-center gap-1.5">
            <HelpCircle className="w-3.5 h-3.5 text-indigo-700" />
            <span>Step-by-Step Reasoning Walkthrough</span>
          </div>
          <ul className="space-y-1 text-xs text-indigo-800 font-medium">
            {reasoning_walkthrough.map((step, idx) => (
              <li key={idx} className="flex items-start gap-1.5">
                <span className="font-bold text-indigo-600 shrink-0">•</span>
                <span>{step}</span>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Level 7: Complete Worked Solution */}
      {full_solution && (
        <div className="bg-teal-50 border border-teal-200 rounded-2xl p-4 space-y-2">
          <div className="text-xs font-extrabold text-teal-900 flex items-center gap-1.5">
            <CheckCircle2 className="w-4 h-4 text-teal-700" />
            <span>Complete Solution & Concept Mastery</span>
          </div>
          <div className="text-xs font-bold text-teal-900 bg-teal-100/70 px-3 py-1.5 rounded-xl">
            Answer: {full_solution.final_answer}
          </div>
          <p className="text-xs text-teal-800 font-medium leading-relaxed">{full_solution.explanation}</p>
          {full_solution.celebration && (
            <p className="text-[11px] text-teal-700 font-semibold italic">{full_solution.celebration}</p>
          )}
        </div>
      )}

      {/* Generic Bite-sized Step from backend */}
      {scaffold_step && !full_solution && !reasoning_walkthrough && !partial_step && !worked_example && (
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

      {/* Learner Agency Controls Bar */}
      <div className="pt-2 border-t border-amber-200/80 flex flex-wrap items-center justify-between gap-2">
        <div className="flex flex-wrap items-center gap-2">
          {/* Request Next Level Button */}
          {canAdvance && (
            <button
              onClick={() => onRequestNextLevel && onRequestNextLevel(currentLevel + 1)}
              className="px-3.5 py-1.5 rounded-xl bg-amber-500 text-amber-950 text-xs font-extrabold hover:bg-amber-400 transition-all flex items-center gap-1.5 shadow-sm"
            >
              <span>Next Hint Level ({currentLevel + 1}/{is6Level ? 5 : 7})</span>
              <ChevronRight className="w-3.5 h-3.5" />
            </button>
          )}

          {/* Dismiss / Try on My Own */}
          <button
            onClick={() => onDismiss && onDismiss()}
            className="px-3 py-1.5 rounded-xl bg-white text-slate-700 border border-slate-200 text-xs font-bold hover:bg-slate-50 transition-all"
          >
            I'm Ready to Try!
          </button>
        </div>

        {/* Representation Switching */}
        {next_representation && next_representation !== 'standard' && (
          <div className="flex items-center gap-1.5">
            <button
              onClick={() => onSelectRepresentation && onSelectRepresentation(next_representation)}
              className="px-3 py-1.5 rounded-xl bg-amber-200 text-amber-950 text-xs font-bold hover:bg-amber-300 transition-all flex items-center gap-1.5"
            >
              <Layers className="w-3.5 h-3.5" />
              <span>Switch to {next_representation === 'visual_block' ? 'Visual Diagrams' : 'Simplified Version'}</span>
            </button>
          </div>
        )}
      </div>
    </div>
  );
};

export default ScaffoldedHintBox;
