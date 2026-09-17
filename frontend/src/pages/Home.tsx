import React from 'react';
import { useAppStore } from '../store/useAppStore';
import { Star, Target, Compass, Zap } from 'lucide-react';
import { motion } from 'framer-motion';

export const Home: React.FC = () => {
  const { currentMission, masteryPoints, focusQuestActive, setFocusQuest } = useAppStore();

  return (
    <div className="max-w-4xl mx-auto p-6 space-y-8">
      <header className="flex justify-between items-center pb-4 border-b border-gray-200">
        <div>
          <h1 className="text-3xl font-bold text-slate-800 tracking-tight">Your Learning Journey</h1>
          <p className="text-slate-600 mt-2 text-lg">Continue where you left off and discover new concepts.</p>
        </div>
        <div className="flex items-center gap-3 bg-indigo-50 px-5 py-3 rounded-2xl border border-indigo-100">
          <Star className="w-6 h-6 text-indigo-500 fill-current" />
          <div>
            <div className="text-sm font-medium text-indigo-900">Mastery</div>
            <div className="text-xl font-bold text-indigo-700">{masteryPoints} XP</div>
          </div>
        </div>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Current Mission */}
        <section className="bg-white p-6 rounded-3xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow focus-within:ring-2 focus-within:ring-indigo-500">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 bg-blue-50 text-blue-600 rounded-xl">
              <Compass className="w-6 h-6" />
            </div>
            <h2 className="text-xl font-semibold text-slate-800">Current Mission</h2>
          </div>
          <p className="text-slate-600 mb-6 text-lg">{currentMission}</p>
          <div className="w-full bg-slate-100 rounded-full h-3 mb-6 overflow-hidden">
            <div className="bg-blue-500 h-3 rounded-full w-2/3" role="progressbar" aria-valuenow={66} aria-valuemin={0} aria-valuemax={100}></div>
          </div>
          <button className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 px-4 rounded-xl transition-colors focus:ring-4 focus:ring-blue-200">
            Continue Mission
          </button>
        </section>

        {/* Focus Quest */}
        <section className="bg-white p-6 rounded-3xl shadow-sm border border-slate-200 hover:shadow-md transition-shadow focus-within:ring-2 focus-within:ring-amber-500">
          <div className="flex items-center gap-3 mb-4">
            <div className="p-3 bg-amber-50 text-amber-600 rounded-xl">
              <Target className="w-6 h-6" />
            </div>
            <h2 className="text-xl font-semibold text-slate-800">Focus Quest</h2>
          </div>
          <p className="text-slate-600 mb-6 text-lg">Short, high-intensity sessions to build specific skills without overwhelm.</p>
          <button 
            onClick={() => setFocusQuest(!focusQuestActive)}
            className={`w-full font-medium py-3 px-4 rounded-xl transition-colors focus:ring-4 flex items-center justify-center gap-2 ${
              focusQuestActive 
                ? 'bg-amber-100 text-amber-800 hover:bg-amber-200 focus:ring-amber-200' 
                : 'bg-amber-500 hover:bg-amber-600 text-white focus:ring-amber-200'
            }`}
          >
            <Zap className="w-5 h-5" />
            {focusQuestActive ? 'Quest Active!' : 'Start Focus Quest'}
          </button>
        </section>
      </div>

      {/* Suggested Paths */}
      <section className="pt-4">
        <h3 className="text-xl font-semibold text-slate-800 mb-4">Recommended for You</h3>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          {['Visual Patterns', 'Logic Puzzles', 'Reading Comprehension'].map((topic, i) => (
            <div key={i} tabIndex={0} className="p-5 bg-slate-50 rounded-2xl border border-slate-200 hover:bg-slate-100 transition-colors cursor-pointer focus:outline-none focus:ring-2 focus:ring-indigo-500">
              <div className="font-medium text-slate-700">{topic}</div>
              <div className="text-sm text-slate-500 mt-1">10-15 mins</div>
            </div>
          ))}
        </div>
      </section>
    </div>
  );
};
