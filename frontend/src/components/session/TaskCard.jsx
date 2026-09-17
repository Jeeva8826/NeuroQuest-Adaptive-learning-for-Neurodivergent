import React, { useState } from 'react';
import { Sparkles, HelpCircle, CheckCircle2, RefreshCw, ArrowRight, Lightbulb, Volume2 } from 'lucide-react';
import AudioButton from '../common/AudioButton';
import { useTheme } from '../../context/ThemeContext';
import { getAIExplanation } from '../../services/api';

const TaskCard = ({ task, onAnswerSubmit, loading }) => {
  const { primaryColor, profile } = useTheme();
  
  const [selectedOption, setSelectedOption] = useState('');
  const [activeHintIndex, setActiveHintIndex] = useState(null);
  const [aiHint, setAiHint] = useState('');
  const [loadingAi, setLoadingAi] = useState(false);
  const [feedback, setFeedback] = useState(null);

  if (!task) return null;

  const handleOptionSelect = (opt) => {
    if (feedback) return; // locked after submission until next
    setSelectedOption(opt);
  };

  const handleSubmit = async () => {
    if (!selectedOption) return;
    const res = await onAnswerSubmit(selectedOption);
    setFeedback(res);
  };

  const handleFetchAiHint = async () => {
    setLoadingAi(true);
    try {
      const interests = profile?.interests || ['Space', 'Animals'];
      const res = await getAIExplanation({
        question: task.question,
        correct_answer: task.correct_answer,
        learner_interests: interests,
        guidance_level: profile?.interaction_preferences?.guidance_level || 'high'
      });
      setAiHint(res.data.explanation);
    } catch (err) {
      console.error('Failed to get AI explanation:', err);
      setAiHint('Focus on the main clue in the question! You can do this!');
    } finally {
      setLoadingAi(false);
    }
  };

  return (
    <div className="bg-white rounded-3xl p-6 sm:p-8 shadow-xl border border-slate-200/80 space-y-6 transition-all">
      
      {/* Task Header */}
      <div className="flex flex-wrap items-center justify-between gap-3 border-b border-slate-100 pb-4">
        <div className="flex items-center gap-2">
          <span
            className="px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider text-white shadow-sm"
            style={{ backgroundColor: primaryColor }}
          >
            {task.subject}
          </span>
          <span className="text-xs font-semibold text-slate-500">
            Difficulty {task.difficulty}/5 • ~{task.estimated_duration} mins
          </span>
        </div>

        <AudioButton text={`${task.title}. Question: ${task.question}`} label="Read Question" />
      </div>

      {/* Question Title & Prompt */}
      <div className="space-y-3">
        <h2 className="text-xl sm:text-2xl font-extrabold text-slate-900 tracking-tight">
          {task.title}
        </h2>
        <p className="text-slate-800 text-base sm:text-lg font-medium leading-relaxed bg-slate-50 p-4 rounded-2xl border border-slate-200/60">
          {task.question}
        </p>
      </div>

      {/* Step-by-Step Guide if present */}
      {task.steps && task.steps.length > 0 && (
        <div className="bg-indigo-50/50 p-4 rounded-2xl border border-indigo-100 space-y-2">
          <div className="text-xs font-bold text-indigo-900 uppercase tracking-wider flex items-center gap-1.5">
            <Sparkles className="w-3.5 h-3.5 text-indigo-600" />
            Step-by-Step Helper
          </div>
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
            {task.steps.map(step => (
              <div key={step.step_number} className="bg-white p-3 rounded-xl border border-indigo-100/80 text-xs">
                <span className="font-bold text-indigo-600">Step {step.step_number}:</span> {step.title}
                <div className="text-slate-500 mt-0.5">{step.description}</div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Options Selection Grid */}
      <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
        {task.options.map((opt, idx) => {
          const isSelected = selectedOption === opt;
          return (
            <button
              key={idx}
              type="button"
              onClick={() => handleOptionSelect(opt)}
              disabled={!!feedback}
              className={`p-4 rounded-2xl text-left font-bold text-sm sm:text-base border-2 transition-all flex items-center justify-between ${
                isSelected
                  ? 'border-indigo-600 bg-indigo-50/70 text-indigo-950 shadow-md ring-2 ring-indigo-400'
                  : 'border-slate-200 bg-white hover:bg-slate-50 text-slate-800'
              }`}
            >
              <span>{opt}</span>
              {isSelected && <CheckCircle2 className="w-5 h-5 text-indigo-600 fill-indigo-100" />}
            </button>
          );
        })}
      </div>

      {/* Hints & AI Guide Section */}
      <div className="flex flex-wrap items-center justify-between gap-3 pt-2">
        <div className="flex items-center gap-2">
          {task.hints && task.hints.length > 0 && (
            <button
              type="button"
              onClick={() => setActiveHintIndex(activeHintIndex === null ? 0 : (activeHintIndex + 1) % task.hints.length)}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold text-amber-800 bg-amber-50 border border-amber-200 hover:bg-amber-100 transition-colors"
            >
              <Lightbulb className="w-4 h-4 text-amber-500" />
              <span>Hint {activeHintIndex !== null ? `#${activeHintIndex + 1}` : ''}</span>
            </button>
          )}

          <button
            type="button"
            onClick={handleFetchAiHint}
            disabled={loadingAi}
            className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-xl text-xs font-bold text-purple-800 bg-purple-50 border border-purple-200 hover:bg-purple-100 transition-colors"
          >
            <Sparkles className="w-4 h-4 text-purple-600" />
            <span>{loadingAi ? 'AI Thinking...' : 'AI Micro-Explanation'}</span>
          </button>
        </div>

        {/* Submit Button */}
        {!feedback && (
          <button
            type="button"
            onClick={handleSubmit}
            disabled={!selectedOption || loading}
            className="px-6 py-3 rounded-2xl text-sm font-extrabold text-white shadow-lg transition-all active:scale-95 disabled:opacity-50"
            style={{ backgroundColor: primaryColor }}
          >
            Check Answer
          </button>
        )}
      </div>

      {/* Active Static Hint Display */}
      {activeHintIndex !== null && task.hints[activeHintIndex] && (
        <div className="bg-amber-50 border border-amber-200 text-amber-900 p-4 rounded-2xl text-xs sm:text-sm font-medium flex items-start gap-2.5">
          <Lightbulb className="w-5 h-5 text-amber-500 shrink-0 mt-0.5" />
          <div>
            <span className="font-bold">Hint #{activeHintIndex + 1}: </span>
            {task.hints[activeHintIndex]}
          </div>
        </div>
      )}

      {/* AI Explanation Display */}
      {aiHint && (
        <div className="bg-purple-50 border border-purple-200 text-purple-950 p-4 rounded-2xl text-xs sm:text-sm font-medium space-y-1">
          <div className="font-bold flex items-center justify-between text-purple-800">
            <span className="flex items-center gap-1.5">
              <Sparkles className="w-4 h-4 text-purple-600" /> AI Adaptive Guide
            </span>
            <AudioButton text={aiHint} label="Listen Hint" />
          </div>
          <p className="text-slate-800">{aiHint}</p>
        </div>
      )}

      {/* Non-punitive Feedback Banner */}
      {feedback && (
        <div
          className={`p-5 rounded-2xl border-2 space-y-3 transition-all ${
            feedback.is_correct
              ? 'bg-emerald-50 border-emerald-300 text-emerald-950'
              : 'bg-indigo-50 border-indigo-300 text-indigo-950'
          }`}
        >
          <div className="flex items-center justify-between">
            <span className="font-extrabold text-base flex items-center gap-2">
              {feedback.is_correct ? '🎉 Splendid Work!' : '🌟 Wonderful Exploration!'}
            </span>
            <AudioButton text={feedback.feedback_message + ' ' + feedback.explanation} label="Read Feedback" />
          </div>

          <p className="text-sm font-medium">{feedback.feedback_message}</p>
          <p className="text-xs text-slate-700 bg-white/70 p-3 rounded-xl border border-slate-200/60 font-semibold">
            {feedback.explanation}
          </p>
        </div>
      )}

    </div>
  );
};

export default TaskCard;
