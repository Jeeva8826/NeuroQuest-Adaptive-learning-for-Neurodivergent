import React, { useState } from 'react';
import { Palette, Volume2, Type, Eye, Sparkles, Check } from 'lucide-react';
import { useTheme } from '../../context/ThemeContext';

const PRESET_COLORS = [
  { label: 'Space Blue', hex: '#3b82f6' },
  { label: 'Cosmic Purple', hex: '#8b5cf6' },
  { label: 'Emerald Nature', hex: '#10b981' },
  { label: 'Ocean Teal', hex: '#14b8a6' },
  { label: 'Sunset Amber', hex: '#f59e0b' },
  { label: 'Soft Pink', hex: '#ec4899' },
  { label: 'Deep Indigo', hex: '#6366f1' }
];

const PRESET_THEMES = [
  { id: 'space', label: '🚀 Space Exploration' },
  { id: 'animals', label: '🐾 Animal Kingdom' },
  { id: 'coding', label: '💻 Coding & Tech' },
  { id: 'nature', label: '🌿 Nature Sanctuary' },
  { id: 'fantasy', label: '🧙 Magic & Fantasy' },
  { id: 'art', label: '🎨 Creative Art Studio' }
];

const PreferenceCustomizer = () => {
  const {
    primaryColor,
    paletteType,
    backgroundTheme,
    fontFamily,
    fontScale,
    animationIntensity,
    soundEnabled,
    visualDensity,
    updatePreferences
  } = useTheme();

  const [saving, setSaving] = useState(false);
  const [successMsg, setSuccessMsg] = useState('');

  const handleColorChange = async (hex) => {
    setSaving(true);
    try {
      await updatePreferences({ primary_color: hex });
      setSuccessMsg('Color updated!');
      setTimeout(() => setSuccessMsg(''), 2000);
    } catch (e) {
      console.error(e);
    } finally {
      setSaving(false);
    }
  };

  const handleThemeChange = async (themeId) => {
    setSaving(true);
    try {
      await updatePreferences({ background_theme: themeId });
      setSuccessMsg('World motif updated!');
      setTimeout(() => setSuccessMsg(''), 2000);
    } catch (e) {
      console.error(e);
    } finally {
      setSaving(false);
    }
  };

  const handleFontChange = async (font) => {
    setSaving(true);
    try {
      await updatePreferences({ font_family: font });
    } catch (e) {
      console.error(e);
    } finally {
      setSaving(false);
    }
  };

  const handlePaletteChange = async (pal) => {
    setSaving(true);
    try {
      await updatePreferences({ palette_type: pal });
    } catch (e) {
      console.error(e);
    } finally {
      setSaving(false);
    }
  };

  const handleAnimChange = async (anim) => {
    setSaving(true);
    try {
      await updatePreferences({ animation_intensity: anim });
    } catch (e) {
      console.error(e);
    } finally {
      setSaving(false);
    }
  };

  return (
    <div className="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/80 shadow-xl space-y-8">
      
      <div className="flex items-center justify-between border-b border-slate-100 pb-4">
        <div>
          <h2 className="text-2xl font-extrabold text-slate-900 flex items-center gap-2">
            <Palette className="w-6 h-6 text-indigo-600" />
            Live Personalized Theme Engine
          </h2>
          <p className="text-slate-500 text-sm mt-0.5">
            Adjust visual contrast, colors, font legibility, motion, and audio preferences anytime.
          </p>
        </div>
        {successMsg && (
          <span className="px-3 py-1 bg-emerald-100 text-emerald-800 text-xs font-bold rounded-full animate-bounce">
            {successMsg}
          </span>
        )}
      </div>

      {/* 1. Primary Accent Color */}
      <div className="space-y-3">
        <label className="block text-sm font-bold text-slate-800">
          Primary Accent Color
        </label>
        <div className="flex flex-wrap gap-3">
          {PRESET_COLORS.map(c => (
            <button
              key={c.hex}
              type="button"
              onClick={() => handleColorChange(c.hex)}
              className={`w-10 h-10 rounded-2xl flex items-center justify-center transition-transform ${
                primaryColor === c.hex ? 'ring-4 ring-slate-900 scale-110 shadow-md' : 'hover:scale-105'
              }`}
              style={{ backgroundColor: c.hex }}
              title={c.label}
            >
              {primaryColor === c.hex && <Check className="w-5 h-5 text-white" />}
            </button>
          ))}
        </div>
      </div>

      {/* 2. World Theme Motif */}
      <div className="space-y-3">
        <label className="block text-sm font-bold text-slate-800">
          World Background Theme Motif
        </label>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
          {PRESET_THEMES.map(th => (
            <button
              key={th.id}
              type="button"
              onClick={() => handleThemeChange(th.id)}
              className={`p-3 rounded-2xl text-xs font-bold text-left border transition-all ${
                backgroundTheme === th.id
                  ? 'border-indigo-600 bg-indigo-50 text-indigo-900 ring-2 ring-indigo-500'
                  : 'border-slate-200 bg-white hover:bg-slate-50 text-slate-700'
              }`}
            >
              {th.label}
            </button>
          ))}
        </div>
      </div>

      {/* 3. Color Palette Style */}
      <div className="space-y-3">
        <label className="block text-sm font-bold text-slate-800">
          Color Palette Mode
        </label>
        <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
          {[
            { id: 'soft', label: 'Soft Pastels' },
            { id: 'dark', label: 'Dark Mode' },
            { id: 'high_contrast', label: 'High Contrast' },
            { id: 'bright', label: 'Bright & Vibrant' },
            { id: 'minimal', label: 'Minimal Neutral' }
          ].map(pal => (
            <button
              key={pal.id}
              type="button"
              onClick={() => handlePaletteChange(pal.id)}
              className={`p-3 rounded-2xl text-xs font-bold border transition-all ${
                paletteType === pal.id
                  ? 'bg-slate-900 text-white border-slate-900 shadow-md'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              {pal.label}
            </button>
          ))}
        </div>
      </div>

      {/* 4. Font Style */}
      <div className="space-y-3">
        <label className="block text-sm font-bold text-slate-800 flex items-center gap-1.5">
          <Type className="w-4 h-4 text-slate-600" /> Font Typography
        </label>
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-2.5">
          {[
            { id: 'rounded', label: 'Friendly Rounded', fontClass: 'font-rounded' },
            { id: 'sans', label: 'Clean Sans-Serif', fontClass: 'font-sans' },
            { id: 'dyslexic', label: 'Dyslexia-Friendly', fontClass: 'font-dyslexic' }
          ].map(f => (
            <button
              key={f.id}
              type="button"
              onClick={() => handleFontChange(f.id)}
              className={`p-3 rounded-2xl text-xs font-bold border transition-all ${f.fontClass} ${
                fontFamily === f.id
                  ? 'border-indigo-600 bg-indigo-50 text-indigo-900 ring-2 ring-indigo-500'
                  : 'border-slate-200 bg-white text-slate-700 hover:bg-slate-50'
              }`}
            >
              {f.label}
            </button>
          ))}
        </div>
      </div>

      {/* 5. Motion & Animation */}
      <div className="space-y-3">
        <label className="block text-sm font-bold text-slate-800 flex items-center gap-1.5">
          <Eye className="w-4 h-4 text-slate-600" /> Motion & Animation Speed
        </label>
        <div className="grid grid-cols-3 gap-2.5">
          {[
            { id: 'none', label: 'No Motion (0x)' },
            { id: 'low', label: 'Gentle (Low)' },
            { id: 'normal', label: 'Standard (Normal)' }
          ].map(a => (
            <button
              key={a.id}
              type="button"
              onClick={() => handleAnimChange(a.id)}
              className={`p-3 rounded-2xl text-xs font-bold border transition-all ${
                animationIntensity === a.id
                  ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                  : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
              }`}
            >
              {a.label}
            </button>
          ))}
        </div>
      </div>

    </div>
  );
};

export default PreferenceCustomizer;
