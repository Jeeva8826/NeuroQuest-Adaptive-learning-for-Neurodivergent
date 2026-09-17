import React, { useState } from 'react';
import { Check, Info } from 'lucide-react';

const QUESTIONS = [
  "How easily does the learner get distracted by background noises?",
  "How well does the learner respond to changes in routine?",
  "How often does the learner need breaks during a 30-minute task?",
  "How effective are visual schedules for the learner?",
  "How does the learner respond to bright lights or high-contrast screens?",
  "How well does the learner follow multi-step verbal instructions?",
  "How often does the learner engage in repetitive motions when concentrating?",
  "How clearly does the learner communicate frustration?",
  "How effective are reward systems (e.g., tokens, points)?",
  "How does the learner respond to timed tasks?",
  "How well does the learner retain information from one day to the next?",
  "How often does the learner hyper-focus on a specific interest?",
  "How comfortable is the learner with open-ended questions?",
  "How much prompting does the learner need to start a new task?",
  "How well does the learner transition away from a preferred activity?",
  "How does the learner respond to corrective feedback?",
  "How often does the learner seek sensory input (e.g., deep pressure)?",
  "How effective is written text compared to audio instructions?",
  "How well does the learner work independently for 15 minutes?",
  "How often does the learner seem overwhelmed by complex visuals?"
];

export const CaregiverProfile: React.FC = () => {
  const [answers, setAnswers] = useState<Record<number, number>>({});

  const handleSelect = (qIndex: number, value: number) => {
    setAnswers(prev => ({ ...prev, [qIndex]: value }));
  };

  const progress = Math.round((Object.keys(answers).length / QUESTIONS.length) * 100);

  return (
    <div className="max-w-3xl mx-auto p-6 space-y-8">
      <header className="bg-white p-6 rounded-3xl shadow-sm border border-slate-200">
        <h1 className="text-2xl font-bold text-slate-800">Support Profile Questionnaire</h1>
        <p className="text-slate-600 mt-2 text-lg">
          Help us personalize the learning environment by answering these questions. 
          Your insights shape a supportive and effective experience.
        </p>
        
        <div className="mt-6">
          <div className="flex justify-between text-sm font-medium text-slate-600 mb-2">
            <span>Progress</span>
            <span>{progress}%</span>
          </div>
          <div className="w-full bg-slate-100 rounded-full h-2">
            <div 
              className="bg-indigo-600 h-2 rounded-full transition-all duration-500 ease-out" 
              style={{ width: `${progress}%` }}
              role="progressbar" 
              aria-valuenow={progress} 
              aria-valuemin={0} 
              aria-valuemax={100}
            />
          </div>
        </div>
      </header>

      <div className="space-y-6">
        {QUESTIONS.map((question, index) => (
          <div key={index} className="bg-white p-6 rounded-2xl shadow-sm border border-slate-100 focus-within:ring-2 focus-within:ring-indigo-500 transition-shadow hover:shadow-md">
            <div className="flex gap-4">
              <div className="flex-shrink-0 w-8 h-8 bg-slate-100 text-slate-500 rounded-full flex items-center justify-center font-medium">
                {index + 1}
              </div>
              <div className="flex-1 space-y-4">
                <h3 className="text-lg font-medium text-slate-800">{question}</h3>
                
                <div className="flex justify-between items-center gap-2">
                  <span className="text-sm text-slate-500 w-24 text-right">Rarely / Poorly</span>
                  <div className="flex-1 flex justify-between px-2">
                    {[1, 2, 3, 4, 5].map((val) => (
                      <button
                        key={val}
                        onClick={() => handleSelect(index, val)}
                        className={`w-12 h-12 rounded-full flex items-center justify-center text-lg font-medium transition-all focus:outline-none focus:ring-4 focus:ring-indigo-200 ${
                          answers[index] === val 
                            ? 'bg-indigo-600 text-white shadow-md transform scale-110' 
                            : 'bg-slate-50 text-slate-600 hover:bg-slate-100 border border-slate-200'
                        }`}
                        aria-label={`Rate ${val} out of 5`}
                        aria-pressed={answers[index] === val}
                      >
                        {val}
                      </button>
                    ))}
                  </div>
                  <span className="text-sm text-slate-500 w-24">Highly / Very Well</span>
                </div>
              </div>
            </div>
          </div>
        ))}
      </div>

      <div className="flex justify-end pt-4 pb-12">
        <button 
          disabled={progress < 100}
          className="bg-indigo-600 disabled:bg-slate-300 disabled:cursor-not-allowed hover:bg-indigo-700 text-white font-medium py-3 px-8 rounded-xl transition-colors focus:ring-4 focus:ring-indigo-200 flex items-center gap-2 text-lg"
        >
          <Check className="w-5 h-5" />
          Save Profile
        </button>
      </div>
    </div>
  );
};
