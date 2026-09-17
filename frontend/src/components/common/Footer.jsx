import React from 'react';
import { Heart, Sparkles, ShieldCheck } from 'lucide-react';

const Footer = () => {
  return (
    <footer className="mt-auto border-t border-slate-200/60 bg-white/50 backdrop-blur-sm py-6 transition-colors">
      <div className="max-w-7xl mx-auto px-4 text-center sm:flex sm:items-center sm:justify-between">
        <div className="flex items-center justify-center gap-2 text-sm text-slate-600">
          <Sparkles className="w-4 h-4 text-indigo-500" />
          <span className="font-semibold text-slate-800">NeuroQuest</span>
          <span>— Personalizing learning for every neurodivergent mind.</span>
        </div>
        <div className="mt-3 sm:mt-0 flex items-center justify-center gap-4 text-xs text-slate-500">
          <span className="inline-flex items-center gap-1">
            <ShieldCheck className="w-3.5 h-3.5 text-emerald-500" />
            Caregiver First & Safe
          </span>
          <span>•</span>
          <span>Phase 1 Discovery Engine</span>
        </div>
      </div>
    </footer>
  );
};

export default Footer;
