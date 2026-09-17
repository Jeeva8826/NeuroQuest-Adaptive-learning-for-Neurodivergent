import React, { useState } from 'react';
import { Sliders, Rocket, Heart, Cpu, Activity, Sparkles, AlertCircle } from 'lucide-react';
import { activateDemoProfile, simulateState } from '../../services/api';

const HackathonDemoBar = ({ onProfileActivated, onStateSimulated }) => {
  const [activeProfile, setActiveProfile] = useState('demo_learner_a');
  const [activeState, setActiveState] = useState('FOCUSED');
  const [collapsed, setCollapsed] = useState(false);

  const handleProfileSelect = async (learnerId) => {
    setActiveProfile(learnerId);
    try {
      const res = await activateDemoProfile(learnerId);
      if (onProfileActivated) onProfileActivated(res.data);
    } catch (err) {
      console.error('Failed to activate demo profile:', err);
    }
  };

  const handleStateSimulate = async (stateName) => {
    setActiveState(stateName);
    try {
      const res = await simulateState(stateName);
      if (onStateSimulated) onStateSimulated(res.data);
    } catch (err) {
      console.error('Failed to simulate state:', err);
    }
  };

  if (collapsed) {
    return (
      <button
        onClick={() => setCollapsed(false)}
        className="fixed bottom-4 right-4 z-40 bg-slate-900 text-amber-400 border border-amber-400/40 px-4 py-2.5 rounded-full text-xs font-black shadow-2xl flex items-center gap-2 hover:scale-105 transition-all"
      >
        <Sliders className="w-4 h-4" />
        <span>Open Hackathon Demo Bar</span>
      </button>
    );
  }

  return (
    <div className="bg-slate-900 text-white border-b border-amber-400/40 px-4 py-2.5 shadow-xl text-xs sticky top-0 z-40">
      <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-3">
        
        {/* Title */}
        <div className="flex items-center gap-2">
          <span className="bg-amber-400 text-amber-950 px-2.5 py-0.5 rounded-md font-black uppercase text-[10px] tracking-wider">
            Demo Simulation Mode
          </span>
          <span className="font-extrabold text-slate-200">Hackathon Judge Controls</span>
        </div>

        {/* 1-Click Demo Profiles */}
        <div className="flex items-center gap-1 bg-slate-800 p-1 rounded-xl border border-slate-700">
          <span className="text-[10px] text-slate-400 font-bold px-2">Learner:</span>
          
          <button
            onClick={() => handleProfileSelect('demo_learner_a')}
            className={`px-3 py-1 rounded-lg font-extrabold transition-all flex items-center gap-1 ${
              activeProfile === 'demo_learner_a' ? 'bg-indigo-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
            }`}
          >
            <Rocket className="w-3.5 h-3.5" />
            <span>Learner A (Space)</span>
          </button>

          <button
            onClick={() => handleProfileSelect('demo_learner_b')}
            className={`px-3 py-1 rounded-lg font-extrabold transition-all flex items-center gap-1 ${
              activeProfile === 'demo_learner_b' ? 'bg-emerald-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
            }`}
          >
            <Heart className="w-3.5 h-3.5" />
            <span>Learner B (Animals)</span>
          </button>

          <button
            onClick={() => handleProfileSelect('demo_learner_c')}
            className={`px-3 py-1 rounded-lg font-extrabold transition-all flex items-center gap-1 ${
              activeProfile === 'demo_learner_c' ? 'bg-sky-600 text-white shadow-sm' : 'text-slate-400 hover:text-white'
            }`}
          >
            <Cpu className="w-3.5 h-3.5" />
            <span>Learner C (Coding)</span>
          </button>
        </div>

        {/* Live Simulated Learner States */}
        <div className="flex items-center gap-1 bg-slate-800 p-1 rounded-xl border border-slate-700">
          <span className="text-[10px] text-slate-400 font-bold px-2">State:</span>

          <button
            onClick={() => handleStateSimulate('FOCUSED')}
            className={`px-2.5 py-1 rounded-lg font-bold transition-all ${
              activeState === 'FOCUSED' ? 'bg-emerald-500 text-slate-950 font-black' : 'text-slate-400 hover:text-white'
            }`}
          >
            Focused
          </button>

          <button
            onClick={() => handleStateSimulate('ATTENTION_DRIFT')}
            className={`px-2.5 py-1 rounded-lg font-bold transition-all ${
              activeState === 'ATTENTION_DRIFT' ? 'bg-amber-400 text-slate-950 font-black' : 'text-slate-400 hover:text-white'
            }`}
          >
            Drift
          </button>

          <button
            onClick={() => handleStateSimulate('POSSIBLE_FATIGUE')}
            className={`px-2.5 py-1 rounded-lg font-bold transition-all ${
              activeState === 'POSSIBLE_FATIGUE' ? 'bg-rose-500 text-white font-black' : 'text-slate-400 hover:text-white'
            }`}
          >
            Fatigue
          </button>
        </div>

        <button
          onClick={() => setCollapsed(true)}
          className="text-[10px] text-slate-400 hover:text-white underline font-medium"
        >
          Hide Bar
        </button>

      </div>
    </div>
  );
};

export default HackathonDemoBar;
