import React from 'react';
import { CheckCircle, Circle, Flag } from 'lucide-react';

const MicroMilestoneProgress = ({ currentStep = 1, totalSteps = 3, milestoneTitle = "Personal Mission Milestone" }) => {
  return (
    <div className="bg-white/90 backdrop-blur-sm rounded-2xl p-4 border border-slate-200/80 shadow-sm space-y-2">
      <div className="flex items-center justify-between text-xs font-bold text-slate-700">
        <span className="flex items-center gap-1.5 text-indigo-600">
          <Flag className="w-4 h-4" />
          {milestoneTitle}
        </span>
        <span className="text-slate-400">Step {currentStep} of {totalSteps}</span>
      </div>

      {/* Milestone Dots */}
      <div className="flex items-center gap-2 pt-1">
        {Array.from({ length: totalSteps }).map((_, idx) => {
          const stepNum = idx + 1;
          const isDone = stepNum < currentStep;
          const isCurrent = stepNum === currentStep;

          return (
            <div key={idx} className="flex-1 flex items-center gap-2">
              <div className={`h-2.5 rounded-full flex-1 transition-all ${
                isDone ? 'bg-emerald-500' : isCurrent ? 'bg-indigo-600 animate-pulse' : 'bg-slate-200'
              }`} />
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default MicroMilestoneProgress;
