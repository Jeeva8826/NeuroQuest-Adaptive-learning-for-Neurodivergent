import React from 'react';
import { Sparkles, Rocket, Heart, Cpu, Globe, Palette, Compass } from 'lucide-react';
import { useTheme } from '../../context/ThemeContext';
import AudioButton from '../common/AudioButton';

const THEME_ICONS = {
  space: Rocket,
  animals: Heart,
  coding: Cpu,
  nature: Globe,
  art: Palette,
  default: Compass
};

const ThemeBanner = ({ learnerName = 'Learner', totalStars = 10 }) => {
  const { primaryColor, secondaryColor, backgroundTheme, profile } = useTheme();

  const IconComp = THEME_ICONS[backgroundTheme] || THEME_ICONS.default;
  const topInterest = profile?.interests?.[0] || backgroundTheme || 'Exploration';

  const welcomeMessage = `Welcome back to your personalized world, ${learnerName}! Your current active motif is ${backgroundTheme.toUpperCase()}, tailored to your interests in ${topInterest}.`;

  return (
    <div
      className={`relative rounded-3xl p-6 sm:p-8 text-white shadow-xl overflow-hidden transition-all duration-500 theme-motif-${backgroundTheme}`}
      style={{
        background: `linear-gradient(135deg, ${primaryColor}, ${secondaryColor})`
      }}
    >
      {/* Background Decorative Element */}
      <div className="absolute -right-6 -bottom-6 w-48 h-48 bg-white/10 rounded-full blur-2xl pointer-events-none" />
      
      <div className="relative z-10 flex flex-col sm:flex-row sm:items-center sm:justify-between gap-6">
        
        <div className="space-y-2 max-w-xl">
          <div className="flex items-center gap-2">
            <span className="inline-flex items-center gap-1 px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-widest bg-white/20 backdrop-blur-md text-white border border-white/30">
              <IconComp className="w-3.5 h-3.5" />
              {backgroundTheme} World
            </span>
            <AudioButton text={welcomeMessage} label="Listen Welcome" className="bg-white/20 text-white border-white/30 hover:bg-white/30" />
          </div>

          <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight drop-shadow-sm">
            Welcome back, {learnerName}!
          </h1>

          <p className="text-white/90 text-sm font-medium leading-relaxed">
            Your learning environment is custom tailored with gentle pacing, soft visual styling, and topics in <strong className="text-white font-bold underline capitalize">{topInterest}</strong>.
          </p>
        </div>

        {/* Stars / Reward Stats Widget */}
        <div className="bg-white/15 backdrop-blur-md border border-white/30 p-4 rounded-2xl flex items-center gap-4 self-start sm:self-auto shadow-inner">
          <div className="w-12 h-12 rounded-2xl bg-amber-400 text-amber-950 flex items-center justify-center font-extrabold text-xl shadow-md">
            <Sparkles className="w-6 h-6 fill-current animate-pulse" />
          </div>
          <div>
            <div className="text-xs uppercase tracking-wider font-bold text-white/80">Quest Stars</div>
            <div className="text-2xl font-black text-white tracking-tight">{totalStars} Stars</div>
          </div>
        </div>

      </div>
    </div>
  );
};

export default ThemeBanner;
