import React, { useState } from 'react';
import { 
  Heart, Sparkles, Palette, Volume2, BookOpen, Gift, ShieldAlert,
  ArrowRight, ArrowLeft, Check, HelpCircle
} from 'lucide-react';
import AudioButton from '../common/AudioButton';

const THEME_OPTIONS = [
  { id: 'Space', label: '🚀 Space', color: 'bg-indigo-50 border-indigo-200 text-indigo-800' },
  { id: 'Animals', label: '🐾 Animals', color: 'bg-emerald-50 border-emerald-200 text-emerald-800' },
  { id: 'Cars', label: '🏎️ Cars & Vehicles', color: 'bg-amber-50 border-amber-200 text-amber-800' },
  { id: 'Sports', label: '⚽ Sports', color: 'bg-blue-50 border-blue-200 text-blue-800' },
  { id: 'Art', label: '🎨 Art & Drawing', color: 'bg-pink-50 border-pink-200 text-pink-800' },
  { id: 'Music', label: '🎵 Music & Sound', color: 'bg-purple-50 border-purple-200 text-purple-800' },
  { id: 'Coding/Technology', label: '💻 Coding & Tech', color: 'bg-sky-50 border-sky-200 text-sky-800' },
  { id: 'Nature', label: '🌿 Nature & Plants', color: 'bg-green-50 border-green-200 text-green-800' },
  { id: 'Fantasy', label: '🧙 Magic & Fantasy', color: 'bg-rose-50 border-rose-200 text-rose-800' },
  { id: 'Games', label: '🎮 Video Games', color: 'bg-teal-50 border-teal-200 text-teal-800' },
  { id: 'Stories', label: '📚 Stories', color: 'bg-violet-50 border-violet-200 text-violet-800' },
  { id: 'Other', label: '✨ Other Topics', color: 'bg-slate-50 border-slate-200 text-slate-800' }
];

const REWARD_OPTIONS = [
  'Unlocking something', 'Collecting objects', 'Exploring', 'Building',
  'Stories', 'Characters', 'Music/sounds', 'Visual effects',
  'Choice/control', 'Praise/encouragement'
];

const StepWizard = ({ onSubmit, loading }) => {
  const [currentStep, setCurrentStep] = useState(0);

  const [formData, setFormData] = useState({
    // Section 1: Interests
    q1_enjoyed_topics: '',
    q2_engaging_activities: '',
    q3_themes: ['Space', 'Animals'],
    q4_hobbies: '',
    q5_voluntary_subjects: '',

    // Section 2: Visual Preferences
    q6_favorite_color: 'blue',
    q7_disliked_colors: [],
    q8_color_palette_preference: 'Soft/muted colors',
    q9_visual_style_preference: 'A mixture',

    // Section 3: Sensory Preferences
    q10_animation_effect: 'distract',
    q11_sound_effect: 'distract',
    q12_prefer_calm_screen: true,
    q13_prefer_movement: false,
    q14_avoided_patterns: '',

    // Section 4: Learning Style
    q15_learning_modality: ['Seeing', 'Doing'],
    q16_task_structure: 'Step-by-step guidance',
    q17_difficulty_reaction: 'needs_break',
    q18_reengagement_helper: 'visual_reward',
    q19_feedback_style: 'immediate',

    // Section 5: Motivation
    q20_excitement_triggers: '',
    q21_reward_types: ['Unlocking something', 'Collecting objects'],

    // Section 6: Comfort
    q22_frustration_triggers: '',
    q23_calming_methods: '',
    q24_platform_avoidances: ''
  });

  const steps = [
    { title: 'Learner Interests', icon: Sparkles, color: 'text-amber-500' },
    { title: 'Visual World', icon: Palette, color: 'text-indigo-500' },
    { title: 'Sensory Comfort', icon: Volume2, color: 'text-emerald-500' },
    { title: 'Learning Style', icon: BookOpen, color: 'text-blue-500' },
    { title: 'Motivation & Rewards', icon: Gift, color: 'text-purple-500' },
    { title: 'Comfort & Safety', icon: ShieldAlert, color: 'text-rose-500' }
  ];

  const handleTextChange = (field, val) => {
    setFormData(prev => ({ ...prev, [field]: val }));
  };

  const toggleArrayItem = (field, item) => {
    setFormData(prev => {
      const arr = [...prev[field]];
      const index = arr.indexOf(item);
      if (index > -1) {
        arr.splice(index, 1);
      } else {
        arr.push(item);
      }
      return { ...prev, [field]: arr };
    });
  };

  const handleNext = () => {
    if (currentStep < steps.length - 1) {
      setCurrentStep(s => s + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      onSubmit(formData);
    }
  };

  const handlePrev = () => {
    if (currentStep > 0) {
      setCurrentStep(s => s - 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  // Section Audio Narration Prompts
  const getStepNarrationText = () => {
    switch (currentStep) {
      case 0:
        return "Section 1: Learner Interests. What topics does the learner naturally enjoy talking about, and what themes attract them most?";
      case 1:
        return "Section 2: Visual Preferences. What are their favorite colors, avoided colors, and preferred visual presentation style?";
      case 2:
        return "Section 3: Sensory Preferences. Do animations or sounds help or distract them? Do they prefer a calm screen?";
      case 3:
        return "Section 4: Learning Preferences. How do they learn best, and do they prefer step-by-step guidance or exploration?";
      case 4:
        return "Section 5: Motivation and Rewards. What kinds of rewards excite them to complete an activity?";
      case 5:
        return "Section 6: Comfort and Safety. What usually causes frustration, and what should the platform avoid?";
      default:
        return "";
    }
  };

  return (
    <div className="max-w-3xl mx-auto bg-white rounded-3xl shadow-xl border border-slate-200/80 overflow-hidden">
      
      {/* Header Banner */}
      <div className="bg-slate-900 text-white p-6 sm:p-8 relative overflow-hidden">
        <div className="absolute -right-8 -bottom-8 w-40 h-40 bg-indigo-500/20 rounded-full blur-2xl pointer-events-none" />
        
        <div className="flex items-center justify-between gap-4 mb-3">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-extrabold uppercase tracking-wider bg-indigo-500/30 text-indigo-300 border border-indigo-400/30">
            Personalization Questionnaire
          </span>
          <AudioButton text={getStepNarrationText()} label="Read Section" className="bg-slate-800 text-slate-200 border-slate-700" />
        </div>

        <h2 className="text-2xl sm:text-3xl font-extrabold tracking-tight">
          Help Us Build Their Learning World
        </h2>
        <p className="text-slate-300 text-sm mt-1 max-w-xl">
          This is a low-stress preference questionnaire (not a diagnostic medical form). Every answer tailors their UI, colors, pacing, and feedback style.
        </p>

        {/* Step Progress Bar */}
        <div className="mt-6">
          <div className="flex items-center justify-between text-xs font-semibold text-slate-400 mb-2">
            <span>Step {currentStep + 1} of {steps.length}: {steps[currentStep].title}</span>
            <span>{Math.round(((currentStep + 1) / steps.length) * 100)}% Complete</span>
          </div>
          <div className="w-full h-2.5 bg-slate-800 rounded-full overflow-hidden">
            <div
              className="h-full bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-500"
              style={{ width: `${((currentStep + 1) / steps.length) * 100}%` }}
            />
          </div>
        </div>
      </div>

      {/* Questionnaire Body */}
      <div className="p-6 sm:p-8 space-y-6">

        {/* STEP 1: INTERESTS */}
        {currentStep === 0 && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                1. What topics does the learner naturally enjoy talking about?
              </label>
              <input
                type="text"
                value={formData.q1_enjoyed_topics}
                onChange={e => handleTextChange('q1_enjoyed_topics', e.target.value)}
                placeholder="e.g. Black holes, Dinosaurs, Minecraft, Drawing cats, Piano..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 outline-none text-slate-800 text-sm"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                2. What activities can they spend a long time doing willingly?
              </label>
              <input
                type="text"
                value={formData.q2_engaging_activities}
                onChange={e => handleTextChange('q2_engaging_activities', e.target.value)}
                placeholder="e.g. Building Lego sets, sorting cards, watching space launches..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 focus:ring-2 focus:ring-indigo-500 outline-none text-sm"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                3. Which themes attract them most? (Select all that apply)
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                {THEME_OPTIONS.map(theme => {
                  const isSelected = formData.q3_themes.includes(theme.id);
                  return (
                    <button
                      key={theme.id}
                      type="button"
                      onClick={() => toggleArrayItem('q3_themes', theme.id)}
                      className={`px-3 py-2.5 rounded-2xl text-xs font-bold text-left border transition-all flex items-center justify-between ${
                        isSelected
                          ? `${theme.color} ring-2 ring-indigo-500 shadow-sm`
                          : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                      }`}
                    >
                      <span>{theme.label}</span>
                      {isSelected && <Check className="w-4 h-4 text-indigo-600" />}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-bold text-slate-800 mb-1">
                  4. Current favorite hobbies?
                </label>
                <input
                  type="text"
                  value={formData.q4_hobbies}
                  onChange={e => handleTextChange('q4_hobbies', e.target.value)}
                  placeholder="e.g. Origami, Swimming, Coding..."
                  className="w-full px-4 py-2.5 rounded-2xl border border-slate-300 focus:ring-2 focus:ring-indigo-500 text-sm outline-none"
                />
              </div>
              <div>
                <label className="block text-sm font-bold text-slate-800 mb-1">
                  5. Voluntarily explored subjects?
                </label>
                <input
                  type="text"
                  value={formData.q5_voluntary_subjects}
                  onChange={e => handleTextChange('q5_voluntary_subjects', e.target.value)}
                  placeholder="e.g. Astronomy, Robots, World History..."
                  className="w-full px-4 py-2.5 rounded-2xl border border-slate-300 focus:ring-2 focus:ring-indigo-500 text-sm outline-none"
                />
              </div>
            </div>
          </div>
        )}

        {/* STEP 2: VISUAL PREFERENCES */}
        {currentStep === 1 && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                6. Favorite color (Accent Theme)?
              </label>
              <div className="flex flex-wrap gap-2.5">
                {['blue', 'purple', 'teal', 'green', 'pink', 'amber', 'sky', 'indigo'].map(color => {
                  const isSel = formData.q6_favorite_color === color;
                  return (
                    <button
                      key={color}
                      type="button"
                      onClick={() => handleTextChange('q6_favorite_color', color)}
                      className={`px-4 py-2 rounded-2xl text-xs font-bold capitalize transition-all border ${
                        isSel
                          ? 'bg-slate-900 text-white shadow-md ring-2 ring-indigo-500'
                          : 'bg-slate-100 text-slate-700 hover:bg-slate-200 border-slate-200'
                      }`}
                    >
                      {color}
                    </button>
                  );
                })}
              </div>
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                7. Colors usually disliked or avoided? (e.g. Avoid aggressive red error popups)
              </label>
              <div className="flex flex-wrap gap-2">
                {['bright red', 'neon yellow', 'harsh orange', 'dark grey', 'bright white'].map(c => {
                  const isSel = formData.q7_disliked_colors.includes(c);
                  return (
                    <button
                      key={c}
                      type="button"
                      onClick={() => toggleArrayItem('q7_disliked_colors', c)}
                      className={`px-3 py-1.5 rounded-xl text-xs font-semibold border ${
                        isSel
                          ? 'bg-rose-100 border-rose-300 text-rose-800 font-bold'
                          : 'bg-white border-slate-200 text-slate-600'
                      }`}
                    >
                      {isSel ? `✓ Avoid ${c}` : `Avoid ${c}`}
                    </button>
                  );
                })}
              </div>
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                8. Preferred Color Palette?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  { id: 'Soft/muted colors', desc: 'Calm, gentle pastels (Low strain)' },
                  { id: 'Dark themes', desc: 'Relaxing dark background (Reduced glare)' },
                  { id: 'High contrast', desc: 'Maximum legibility and crisp outlines' },
                  { id: 'Bright colors', desc: 'Vibrant, high-energy visuals' },
                  { id: 'Minimal colors', desc: 'Clean, distraction-free neutral tones' }
                ].map(opt => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => handleTextChange('q8_color_palette_preference', opt.id)}
                    className={`p-3.5 rounded-2xl border text-left transition-all ${
                      formData.q8_color_palette_preference === opt.id
                        ? 'border-indigo-600 bg-indigo-50/50 ring-2 ring-indigo-500'
                        : 'border-slate-200 bg-white hover:bg-slate-50'
                    }`}
                  >
                    <div className="text-sm font-bold text-slate-900">{opt.id}</div>
                    <div className="text-xs text-slate-500 mt-0.5">{opt.desc}</div>
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                9. Preferred Visual Presentation Format?
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                {['Pictures', 'Icons', 'Diagrams', 'Text', 'A mixture'].map(style => (
                  <button
                    key={style}
                    type="button"
                    onClick={() => handleTextChange('q9_visual_style_preference', style)}
                    className={`p-2.5 rounded-2xl text-xs font-bold border transition-all ${
                      formData.q9_visual_style_preference === style
                        ? 'bg-indigo-600 text-white border-indigo-600 shadow-sm'
                        : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                    }`}
                  >
                    {style}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* STEP 3: SENSORY PREFERENCES */}
        {currentStep === 2 && (
          <div className="space-y-6 animate-fadeIn">
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div className="p-4 rounded-2xl border border-slate-200 bg-slate-50/50">
                <label className="block text-sm font-bold text-slate-800 mb-1">
                  10. Do animations help or distract?
                </label>
                <select
                  value={formData.q10_animation_effect}
                  onChange={e => handleTextChange('q10_animation_effect', e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm outline-none bg-white font-medium"
                >
                  <option value="distract">Animations distract (Reduce motion)</option>
                  <option value="help">Animations help focus</option>
                  <option value="neutral">Neutral</option>
                </select>
              </div>

              <div className="p-4 rounded-2xl border border-slate-200 bg-slate-50/50">
                <label className="block text-sm font-bold text-slate-800 mb-1">
                  11. Do sound effects help or distract?
                </label>
                <select
                  value={formData.q11_sound_effect}
                  onChange={e => handleTextChange('q11_sound_effect', e.target.value)}
                  className="w-full px-3 py-2 rounded-xl border border-slate-300 text-sm outline-none bg-white font-medium"
                >
                  <option value="distract">Sounds distract (Mute by default)</option>
                  <option value="help">Sounds help focus (Calm chimes)</option>
                  <option value="neutral">Neutral</option>
                </select>
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <label className={`p-4 rounded-2xl border cursor-pointer transition-all flex items-start gap-3 ${
                formData.q12_prefer_calm_screen ? 'bg-indigo-50/70 border-indigo-300' : 'bg-white border-slate-200'
              }`}>
                <input
                  type="checkbox"
                  checked={formData.q12_prefer_calm_screen}
                  onChange={e => handleTextChange('q12_prefer_calm_screen', e.target.checked)}
                  className="mt-1 w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500"
                />
                <div>
                  <div className="text-sm font-bold text-slate-900">12. Visually Calm Screen</div>
                  <div className="text-xs text-slate-500 mt-0.5">Spacious paddings, minimal clutter</div>
                </div>
              </label>

              <label className={`p-4 rounded-2xl border cursor-pointer transition-all flex items-start gap-3 ${
                formData.q13_prefer_movement ? 'bg-indigo-50/70 border-indigo-300' : 'bg-white border-slate-200'
              }`}>
                <input
                  type="checkbox"
                  checked={formData.q13_prefer_movement}
                  onChange={e => handleTextChange('q13_prefer_movement', e.target.checked)}
                  className="mt-1 w-4 h-4 rounded text-indigo-600 focus:ring-indigo-500"
                />
                <div>
                  <div className="text-sm font-bold text-slate-900">13. Movement & Interactive Dragging</div>
                  <div className="text-xs text-slate-500 mt-0.5">Enjoys tactile drag & drop controls</div>
                </div>
              </label>
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                14. Visual patterns or triggers to avoid?
              </label>
              <input
                type="text"
                value={formData.q14_avoided_patterns}
                onChange={e => handleTextChange('q14_avoided_patterns', e.target.value)}
                placeholder="e.g. Flashing lights, dense wall of text, ticking timers..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 text-sm outline-none"
              />
            </div>
          </div>
        )}

        {/* STEP 4: LEARNING PREFERENCES */}
        {currentStep === 3 && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                15. How do they learn best? (Select all that apply)
              </label>
              <div className="flex flex-wrap gap-2.5">
                {['Seeing (Visual)', 'Listening (Auditory)', 'Doing (Hands-on)', 'Reading (Text)', 'Combination'].map(mode => {
                  const cleanMode = mode.split(' ')[0];
                  const isSel = formData.q15_learning_modality.includes(cleanMode);
                  return (
                    <button
                      key={mode}
                      type="button"
                      onClick={() => toggleArrayItem('q15_learning_modality', cleanMode)}
                      className={`px-4 py-2.5 rounded-2xl text-xs font-bold border transition-all ${
                        isSel
                          ? 'bg-blue-600 text-white border-blue-600 shadow-sm'
                          : 'bg-slate-50 text-slate-700 border-slate-200 hover:bg-slate-100'
                      }`}
                    >
                      {isSel ? `✓ ${mode}` : mode}
                    </button>
                  );
                })}
              </div>
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                16. Preferred Task Structure?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  { id: 'Step-by-step guidance', desc: 'Guided micro-steps with instant hints' },
                  { id: 'Small tasks', desc: 'Single bite-sized questions (Low cognitive load)' },
                  { id: 'Exploration', desc: 'Open-ended problem solving and freedom' },
                  { id: 'Longer challenges', desc: 'Multi-part quest adventures' }
                ].map(opt => (
                  <button
                    key={opt.id}
                    type="button"
                    onClick={() => handleTextChange('q16_task_structure', opt.id)}
                    className={`p-3.5 rounded-2xl border text-left transition-all ${
                      formData.q16_task_structure === opt.id
                        ? 'border-blue-600 bg-blue-50/60 ring-2 ring-blue-500'
                        : 'border-slate-200 bg-white hover:bg-slate-50'
                    }`}
                  >
                    <div className="text-sm font-bold text-slate-900">{opt.id}</div>
                    <div className="text-xs text-slate-500 mt-0.5">{opt.desc}</div>
                  </button>
                ))}
              </div>
            </div>

            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div>
                <label className="block text-sm font-bold text-slate-800 mb-1">
                  17. Reaction when task becomes difficult?
                </label>
                <select
                  value={formData.q17_difficulty_reaction}
                  onChange={e => handleTextChange('q17_difficulty_reaction', e.target.value)}
                  className="w-full px-3 py-2.5 rounded-xl border border-slate-300 text-sm outline-none bg-white font-medium"
                >
                  <option value="needs_break">Needs a quick micro-break</option>
                  <option value="wants_hint">Wants an immediate step-by-step hint</option>
                  <option value="gets_frustrated">Expresses frustration (Needs gentle encouragement)</option>
                  <option value="tries_again">Enjoys retrying independently</option>
                </select>
              </div>

              <div>
                <label className="block text-sm font-bold text-slate-800 mb-1">
                  19. Feedback Preference?
                </label>
                <select
                  value={formData.q19_feedback_style}
                  onChange={e => handleTextChange('q19_feedback_style', e.target.value)}
                  className="w-full px-3 py-2.5 rounded-xl border border-slate-300 text-sm outline-none bg-white font-medium"
                >
                  <option value="immediate">Immediate feedback (Instant encouragement)</option>
                  <option value="summary">Summary feedback after completing task</option>
                </select>
              </div>
            </div>
          </div>
        )}

        {/* STEP 5: MOTIVATION */}
        {currentStep === 4 && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                20. What makes them excited to complete an activity?
              </label>
              <input
                type="text"
                value={formData.q20_excitement_triggers}
                onChange={e => handleTextChange('q20_excitement_triggers', e.target.value)}
                placeholder="e.g. Earning new space badges, unlocking story chapters, hearing gentle chimes..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 text-sm outline-none"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-2">
                21. What kinds of rewards do they naturally value? (Select all that apply)
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-2.5">
                {REWARD_OPTIONS.map(rw => {
                  const isSel = formData.q21_reward_types.includes(rw);
                  return (
                    <button
                      key={rw}
                      type="button"
                      onClick={() => toggleArrayItem('q21_reward_types', rw)}
                      className={`p-3 rounded-2xl text-xs font-bold border transition-all text-left flex items-center justify-between ${
                        isSel
                          ? 'bg-purple-50 border-purple-300 text-purple-900 ring-2 ring-purple-500'
                          : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-50'
                      }`}
                    >
                      <span>{rw}</span>
                      {isSel && <Check className="w-4 h-4 text-purple-600" />}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* STEP 6: COMFORT & SAFETY */}
        {currentStep === 5 && (
          <div className="space-y-6 animate-fadeIn">
            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                22. What usually makes learning frustrating for them?
              </label>
              <input
                type="text"
                value={formData.q22_frustration_triggers}
                onChange={e => handleTextChange('q22_frustration_triggers', e.target.value)}
                placeholder="e.g. Strict time limits, harsh wrong red X markers, complex language..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 text-sm outline-none"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                23. What usually helps calm them?
              </label>
              <input
                type="text"
                value={formData.q23_calming_methods}
                onChange={e => handleTextChange('q23_calming_methods', e.target.value)}
                placeholder="e.g. Taking a 1-minute breathing break, switching to soft colors, listening to calm music..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 text-sm outline-none"
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-800 mb-1">
                24. What should the platform avoid at all costs?
              </label>
              <input
                type="text"
                value={formData.q24_platform_avoidances}
                onChange={e => handleTextChange('q24_platform_avoidances', e.target.value)}
                placeholder="e.g. Unexpected loud popups, punitive negative scoring..."
                className="w-full px-4 py-3 rounded-2xl border border-slate-300 text-sm outline-none"
              />
            </div>
          </div>
        )}

        {/* Footer Wizard Controls */}
        <div className="pt-6 border-t border-slate-200/80 flex items-center justify-between">
          <button
            type="button"
            onClick={handlePrev}
            disabled={currentStep === 0 || loading}
            className={`inline-flex items-center gap-2 px-5 py-2.5 rounded-2xl text-sm font-bold transition-all ${
              currentStep === 0
                ? 'opacity-0 pointer-events-none'
                : 'bg-slate-100 text-slate-700 hover:bg-slate-200'
            }`}
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Previous</span>
          </button>

          <button
            type="button"
            onClick={handleNext}
            disabled={loading}
            className="inline-flex items-center gap-2 px-7 py-3 rounded-2xl text-sm font-extrabold text-white bg-indigo-600 hover:bg-indigo-700 shadow-lg shadow-indigo-500/25 transition-all transform active:scale-95"
          >
            {loading ? (
              <span>Building Learner World...</span>
            ) : currentStep === steps.length - 1 ? (
              <>
                <Sparkles className="w-4 h-4 fill-current" />
                <span>Create Personalized World</span>
              </>
            ) : (
              <>
                <span>Next Step</span>
                <ArrowRight className="w-4 h-4" />
              </>
            )}
          </button>
        </div>

      </div>
    </div>
  );
};

export default StepWizard;
