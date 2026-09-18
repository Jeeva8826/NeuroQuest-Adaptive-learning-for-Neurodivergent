import React, { useState, useEffect } from 'react';
import { 
  Sparkles, Palette, Volume2, BookOpen, Gift, ShieldCheck,
  ArrowRight, ArrowLeft, Check, HelpCircle, Eye, Clock, Layers,
  Compass, Heart, Zap, Sliders, AlertCircle, Save, Edit3
} from 'lucide-react';
import AudioButton from '../common/AudioButton';
import { getQuestionnaireDraft, saveQuestionnaireDraft } from '../../services/api';

export const STEPS_CONFIG = [
  {
    step: 1,
    title: 'Learner & Education',
    category: 'Category A — Pedagogical Foundation',
    icon: Compass,
    color: 'text-blue-600',
    bg: 'bg-blue-50',
    description: "Tell us about your learner and their favorite subjects and passion topics."
  },
  {
    step: 2,
    title: 'Known Support Information',
    category: 'Category C — Educational Accommodations (Optional)',
    icon: ShieldCheck,
    color: 'text-indigo-600',
    bg: 'bg-indigo-50',
    description: "Optional section to pre-configure existing formal school supports. Strictly non-diagnostic.",
    isOptional: true
  },
  {
    step: 3,
    title: 'Learning Strengths & Representation',
    category: 'Category A — Modality & Representation',
    icon: Sparkles,
    color: 'text-amber-600',
    bg: 'bg-amber-50',
    description: "How your learner naturally grasps concepts and stays engaged."
  },
  {
    step: 4,
    title: 'Learning Difficulties & Processing',
    category: 'Category A & B — Cognitive Chunking',
    icon: Layers,
    color: 'text-rose-600',
    bg: 'bg-rose-50',
    description: "Identifying cognitive roadblocks so NeuroQuest can chunk information appropriately."
  },
  {
    step: 5,
    title: 'Attention & Task Management',
    category: 'Category B — Executive Function Support',
    icon: Zap,
    color: 'text-purple-600',
    bg: 'bg-purple-50',
    description: "Supporting task initiation, focus maintenance, and calm recovery from frustration."
  },
  {
    step: 6,
    title: 'Accessibility & Sensory Preferences',
    category: 'Category B & C — Sensory Regulation',
    icon: Palette,
    color: 'text-teal-600',
    bg: 'bg-teal-50',
    description: "Tailoring fonts, visual density, animations, and sound effects to prevent overload."
  },
  {
    step: 7,
    title: 'Communication & Instruction',
    category: 'Category A — Instructional Design',
    icon: BookOpen,
    color: 'text-emerald-600',
    bg: 'bg-emerald-50',
    description: "Configuring how our AI mentor speaks, guides, and paces learning activities."
  },
  {
    step: 8,
    title: 'Existing Accommodations',
    category: 'Category C — School Support Bridge',
    icon: Sliders,
    color: 'text-cyan-600',
    bg: 'bg-cyan-50',
    description: "Bringing proven home and classroom accommodations into the digital interface."
  },
  {
    step: 9,
    title: 'Learning Environment & Motivation',
    category: 'Category B — Motivation Architecture',
    icon: Gift,
    color: 'text-orange-600',
    bg: 'bg-orange-50',
    description: "Surroundings, break rhythms, and non-competitive celebration dynamics."
  },
  {
    step: 10,
    title: 'Review & Profile Generation',
    category: 'Privacy, Consent & Calibration',
    icon: Heart,
    color: 'text-pink-600',
    bg: 'bg-pink-50',
    description: "Review responses, confirm educational consent, and generate the initial support profile."
  }
];

export default function QuestionnaireWizard({ onSubmit, loading }) {
  const [currentStep, setCurrentStep] = useState(1);
  const [savedNotice, setSavedNotice] = useState(false);

  const [formData, setFormData] = useState({
    // Step 1: Learner & Education
    learner_name: 'Explorer',
    grade_level: 'Class 6 (NCERT)',
    primary_subjects: ['Science', 'Mathematics'],
    interest_anchors: ['Space & Astronomy', 'Animals & Nature'],

    // Step 2: Known Support Info
    has_identified_support: 'No',
    support_categories: [],

    // Step 3: Learning Strengths
    representation_mode: ['Visual diagrams, charts & infographics', 'Step-by-step worked examples'],
    engagement_anchors: ['Exploration quests & territory unlocks', 'Visual logic puzzles'],
    interest_boost: 'Greatly helps (doubles engagement)',

    // Step 4: Learning Difficulties
    reading_text_volume: 'Bite-sized sentences (1 to 2 lines per card)',
    academic_triggers: ['Dense continuous reading passages'],
    difficulty_response: 'Break into smaller steps',

    // Step 5: Attention & Task Management
    task_management_friction: ['Starting a task (initiation friction)', 'Staying focused on single screen'],
    frustration_behavior: 'Offer a 1-minute calming sensory break',
    session_fatigue_pattern: 'Prefers short micro-sessions (5 to 8 mins)',

    // Step 6: Accessibility & Sensory
    visual_accessibility: ['Dyslexic-friendly font (OpenDyslexic)', 'Reduced motion (disable auto-sliding & animations)'],
    audio_preferences: 'On-demand audio button (listen when helpful)',
    color_palette: 'Soft calming pastels (low sensory glare)',

    // Step 7: Communication & Instruction
    instruction_granularity: 'Single-clause direct instructions (one action per card)',
    feedback_style: 'Show the first step gently',
    pacing_control: 'Completely untimed, relaxed exploration (zero clocks)',

    // Step 8: Existing Accommodations
    accommodations_used: ['Additional time for tasks', 'Visual step instructions', 'Audio read-aloud / Text-to-speech'],
    effective_accommodations: ['Visual instructions', 'Additional time'],

    // Step 9: Environment & Motivation
    study_environment: 'Quiet, distraction-minimized space',
    break_rhythm: 'Every 5 to 7 minutes with calm sensory animations',
    celebration_style: 'Visual unlocks (opening new planets, sanctuaries, or cyber parts)',

    // Step 10: Consent & Goals
    learner_goals: ['Build confidence in STEM concepts', 'Enjoy stress-free learning exploration'],
    consent_acknowledged: true
  });

  // Resume saved draft from server or localStorage
  useEffect(() => {
    const loadDraft = async () => {
      try {
        const local = localStorage.getItem('neuroquest_questionnaire_draft');
        if (local) {
          const parsed = JSON.parse(local);
          if (parsed.form_data) setFormData(prev => ({ ...prev, ...parsed.form_data }));
          if (parsed.step) setCurrentStep(parsed.step);
        }

        const res = await getQuestionnaireDraft();
        if (res.data && res.data.exists && res.data.form_data) {
          setFormData(prev => ({ ...prev, ...res.data.form_data }));
          if (res.data.step) setCurrentStep(res.data.step);
        }
      } catch (err) {
        // Fallback silently if offline or unauthenticated draft
      }
    };
    loadDraft();
  }, []);

  const handleSelect = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleToggleMulti = (field, item) => {
    setFormData(prev => {
      const current = prev[field] || [];
      const updated = current.includes(item) ? current.filter(x => x !== item) : [...current, item];
      return { ...prev, [field]: updated };
    });
  };

  const handleSaveDraft = async () => {
    try {
      localStorage.setItem('neuroquest_questionnaire_draft', JSON.stringify({
        step: currentStep,
        form_data: formData,
        saved_at: new Date().toISOString()
      }));
      await saveQuestionnaireDraft({ step: currentStep, form_data: formData });
      setSavedNotice(true);
      setTimeout(() => setSavedNotice(false), 3000);
    } catch (e) {
      setSavedNotice(true);
      setTimeout(() => setSavedNotice(false), 3000);
    }
  };

  const handleNext = () => {
    if (currentStep < 10) {
      setCurrentStep(s => s + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      // Package submission payload
      const submission = {
        ...formData,
        // Ensure legacy fields match for 100% backward compatibility
        q1_learning_environment: formData.study_environment,
        q2_content_format: formData.representation_mode[0] || 'Visual diagrams',
        q3_text_tolerance: formData.reading_text_volume,
        q4_visual_support: 'High visual support',
        q5_audio_support: formData.audio_preferences,
        q6_pace_preference: formData.pacing_control,
        q7_response_time: 'Needs extended time to think',
        q8_distraction_sensitivity: 'High — visual motion breaks focus',
        q9_content_density: 'Single-concept focus',
        q10_task_chunking: 'Micro-challenges',
        q11_repetition_preference: 'Spiral review',
        q12_instruction_complexity: formData.instruction_granularity,
        q13_difficulty_tolerance: 'Prefers high early success',
        q14_frustration_recovery: formData.frustration_behavior,
        q15_example_preference: 'Real-world analogy',
        q16_step_guidance: 'Always scaffolded',
        q17_break_frequency: formData.break_rhythm,
        q18_reinforcement_style: formData.celebration_style,
        q19_support_communication: 'Warm, patient mentor persona',
        q20_accommodations: formData.visual_accessibility,
        q3_themes: formData.interest_anchors
      };
      onSubmit(submission);
    }
  };

  const handlePrev = () => {
    if (currentStep > 1) {
      setCurrentStep(s => s - 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const stepMeta = STEPS_CONFIG[currentStep - 1];
  const StepIcon = stepMeta.icon;

  return (
    <div className="bg-white rounded-3xl border border-slate-200 shadow-sm overflow-hidden transition-all">
      {/* Top Banner & Progress Bar */}
      <div className="p-6 sm:p-8 bg-gradient-to-r from-slate-50 via-white to-blue-50/40 border-b border-slate-100">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className={`p-3 rounded-2xl ${stepMeta.bg} ${stepMeta.color} shadow-sm`}>
              <StepIcon className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-bold px-2.5 py-0.5 rounded-full bg-slate-200/80 text-slate-700">
                  Step {currentStep} of 10
                </span>
                <span className="text-xs font-semibold text-emerald-700 bg-emerald-50 px-2.5 py-0.5 rounded-full border border-emerald-200">
                  Dataset-Informed Non-Diagnostic
                </span>
                {stepMeta.isOptional && (
                  <span className="text-xs font-medium text-amber-700 bg-amber-50 px-2 py-0.5 rounded-full border border-amber-200">
                    Optional Section
                  </span>
                )}
              </div>
              <h2 className="text-xl sm:text-2xl font-black text-slate-900 mt-1">
                {stepMeta.title}
              </h2>
              <p className="text-sm text-slate-500 mt-0.5">
                {stepMeta.description}
              </p>
            </div>
          </div>

          {/* Action Tools */}
          <div className="flex items-center gap-2 self-start sm:self-auto">
            <button
              type="button"
              onClick={handleSaveDraft}
              className="flex items-center gap-1.5 px-3 py-1.5 text-xs font-bold text-slate-600 bg-slate-100 hover:bg-slate-200 rounded-xl transition-all"
              title="Save progress and resume later"
            >
              <Save className="w-3.5 h-3.5" />
              <span>Save Draft</span>
            </button>

            <AudioButton 
              text={`Step ${currentStep}: ${stepMeta.title}. ${stepMeta.description}`} 
              className="bg-white shadow-xs border border-slate-200 text-slate-600 hover:text-slate-900"
            />
          </div>
        </div>

        {/* Saved Draft Toast Notification */}
        {savedNotice && (
          <div className="mt-4 p-2.5 bg-emerald-50 text-emerald-800 text-xs font-bold rounded-xl border border-emerald-200 flex items-center gap-2">
            <Check className="w-4 h-4 text-emerald-600" />
            <span>Progress saved! You can close or resume this questionnaire at any time.</span>
          </div>
        )}

        {/* 10-Step Visual Segmented Progress */}
        <div className="grid grid-cols-10 gap-1.5 mt-6">
          {STEPS_CONFIG.map((s) => (
            <button
              key={s.step}
              type="button"
              onClick={() => setCurrentStep(s.step)}
              className={`h-2.5 rounded-full transition-all duration-300 ${
                s.step === currentStep
                  ? 'bg-blue-600 ring-2 ring-blue-200 scale-105'
                  : s.step < currentStep
                    ? 'bg-emerald-500'
                    : 'bg-slate-200 hover:bg-slate-300'
              }`}
              title={`Jump to Step ${s.step}: ${s.title}`}
            />
          ))}
        </div>
      </div>

      {/* Step Form Body */}
      <div className="p-6 sm:p-8 space-y-8">
        {/* STEP 1: LEARNER & EDUCATION */}
        {currentStep === 1 && (
          <div className="space-y-6">
            <div className="space-y-2">
              <label className="text-sm font-bold text-slate-800 block">
                Learner Preferred Name
              </label>
              <input
                type="text"
                value={formData.learner_name}
                onChange={(e) => handleSelect('learner_name', e.target.value)}
                placeholder="e.g., Leo, Maya, Kai"
                className="w-full px-4 py-3 bg-slate-50 border border-slate-200 rounded-2xl font-medium text-slate-900 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>

            <div className="space-y-2">
              <label className="text-sm font-bold text-slate-800 block">
                NCERT Curriculum Grade Band
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                {['Class 6 (NCERT)', 'Class 7 (NCERT)', 'Class 8 (NCERT)', 'Flexible Explorer'].map((grade) => (
                  <button
                    key={grade}
                    type="button"
                    onClick={() => handleSelect('grade_level', grade)}
                    className={`p-3.5 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.grade_level === grade
                        ? 'bg-blue-50 border-blue-500 text-blue-700 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {grade}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-sm font-bold text-slate-800 block">
                Primary Subjects for Learning Support
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {['Science', 'Mathematics', 'Social Science', 'Logic & Puzzles', 'English & Vocabulary'].map((subj) => {
                  const active = formData.primary_subjects.includes(subj);
                  return (
                    <button
                      key={subj}
                      type="button"
                      onClick={() => handleToggleMulti('primary_subjects', subj)}
                      className={`p-3.5 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between ${
                        active
                          ? 'bg-blue-50 border-blue-500 text-blue-700 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{subj}</span>
                      {active && <Check className="w-4 h-4 text-blue-600" />}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-sm font-bold text-slate-800 block">
                Passion Topics & Special Interests (Drives Mission Themes)
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
                {['Space & Astronomy', 'Animals & Nature', 'Coding & Robotics', 'Fantasy & Mythology', 'Art & Drawing', 'Vehicles & Transport', 'Music & Rhythm'].map((interest) => {
                  const active = formData.interest_anchors.includes(interest);
                  return (
                    <button
                      key={interest}
                      type="button"
                      onClick={() => handleToggleMulti('interest_anchors', interest)}
                      className={`p-3.5 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between ${
                        active
                          ? 'bg-indigo-50 border-indigo-500 text-indigo-700 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{interest}</span>
                      {active && <Check className="w-4 h-4 text-indigo-600" />}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* STEP 2: KNOWN SUPPORT INFORMATION (OPTIONAL) */}
        {currentStep === 2 && (
          <div className="space-y-6">
            <div className="p-4 bg-amber-50/80 border border-amber-200 rounded-2xl text-xs text-amber-900 leading-relaxed">
              <strong className="block font-bold mb-1">Non-Diagnostic Privacy Declaration</strong>
              This section is optional. NeuroQuest does not diagnose or screen for medical conditions. Information here is strictly used to pre-configure appropriate educational accommodations (such as visual step checklists or audio readers).
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Has the learner been identified by a qualified educator or specialist as having an educational support need?
              </label>
              <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
                {['Yes', 'No', 'Unsure', 'Prefer not to say'].map((opt) => (
                  <button
                    key={opt}
                    type="button"
                    onClick={() => handleSelect('has_identified_support', opt)}
                    className={`p-3.5 rounded-2xl text-xs font-bold border transition-all ${
                      formData.has_identified_support === opt
                        ? 'bg-indigo-50 border-indigo-500 text-indigo-700'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {opt}
                  </button>
                ))}
              </div>
            </div>

            {formData.has_identified_support === 'Yes' && (
              <div className="space-y-3 pt-2 animate-fadeIn">
                <label className="text-sm font-bold text-slate-800 block">
                  Which general educational support domains are relevant?
                </label>
                <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                  {[
                    'Attention & Focus Support',
                    'Reading & Dyslexia Support',
                    'Writing & Fine Motor Support',
                    'Mathematics & Processing Support',
                    'Social & Communication Support',
                    'Sensory Regulation Support'
                  ].map((cat) => {
                    const active = formData.support_categories.includes(cat);
                    return (
                      <button
                        key={cat}
                        type="button"
                        onClick={() => handleToggleMulti('support_categories', cat)}
                        className={`p-3.5 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between ${
                          active
                            ? 'bg-indigo-50 border-indigo-500 text-indigo-700'
                            : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                        }`}
                      >
                        <span>{cat}</span>
                        {active && <Check className="w-4 h-4 text-indigo-600" />}
                      </button>
                    );
                  })}
                </div>
              </div>
            )}
          </div>
        )}

        {/* STEP 3: LEARNING STRENGTHS & REPRESENTATION */}
        {currentStep === 3 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                What type of material usually helps the learner understand a new topic best?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Visual diagrams, charts & infographics',
                  'Step-by-step worked examples',
                  'Short bite-sized text',
                  'Interactive animations & simulations',
                  'Audio narration & speech',
                  'Hands-on puzzle exploration'
                ].map((rep) => {
                  const active = formData.representation_mode.includes(rep);
                  return (
                    <button
                      key={rep}
                      type="button"
                      onClick={() => handleToggleMulti('representation_mode', rep)}
                      className={`p-4 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between text-left ${
                        active
                          ? 'bg-amber-50 border-amber-500 text-amber-900 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{rep}</span>
                      {active && <Check className="w-4 h-4 text-amber-600" />}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Which learning activities consistently keep the learner engaged?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Exploration quests & territory unlocks',
                  'Visual logic puzzles',
                  'Step-by-step mystery solving',
                  'Card collecting & badges',
                  'Story-driven missions with characters'
                ].map((act) => {
                  const active = formData.engagement_anchors.includes(act);
                  return (
                    <button
                      key={act}
                      type="button"
                      onClick={() => handleToggleMulti('engagement_anchors', act)}
                      className={`p-4 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between text-left ${
                        active
                          ? 'bg-amber-50 border-amber-500 text-amber-900 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{act}</span>
                      {active && <Check className="w-4 h-4 text-amber-600" />}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* STEP 4: LEARNING DIFFICULTIES & PROCESSING */}
        {currentStep === 4 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Comfortable amount of continuous reading text per screen
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Bite-sized sentences (1 to 2 lines per card)',
                  'Short paragraphs (3 to 4 lines)',
                  'Bullet points with icons',
                  'Standard story passages'
                ].map((vol) => (
                  <button
                    key={vol}
                    type="button"
                    onClick={() => handleSelect('reading_text_volume', vol)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.reading_text_volume === vol
                        ? 'bg-rose-50 border-rose-500 text-rose-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {vol}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Which academic tasks usually trigger struggle or avoidance?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Dense continuous reading passages',
                  'Multi-step word problems',
                  'Abstract definitions without examples',
                  'Rapid mental calculation',
                  'Open-ended ambiguous questions'
                ].map((trig) => {
                  const active = formData.academic_triggers.includes(trig);
                  return (
                    <button
                      key={trig}
                      type="button"
                      onClick={() => handleToggleMulti('academic_triggers', trig)}
                      className={`p-4 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between text-left ${
                        active
                          ? 'bg-rose-50 border-rose-500 text-rose-900 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{trig}</span>
                      {active && <Check className="w-4 h-4 text-rose-600" />}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* STEP 5: ATTENTION & TASK MANAGEMENT */}
        {currentStep === 5 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Which parts of independent learning are usually difficult?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Starting a task (initiation friction)',
                  'Staying focused on single screen',
                  'Remembering multi-step instructions',
                  'Switching between tasks / topics',
                  'Completing tasks without checking out'
                ].map((fric) => {
                  const active = formData.task_management_friction.includes(fric);
                  return (
                    <button
                      key={fric}
                      type="button"
                      onClick={() => handleToggleMulti('task_management_friction', fric)}
                      className={`p-4 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between text-left ${
                        active
                          ? 'bg-purple-50 border-purple-500 text-purple-900 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{fric}</span>
                      {active && <Check className="w-4 h-4 text-purple-600" />}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                What usually happens when a task becomes frustrating?
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Offer a 1-minute calming sensory break',
                  'Requests a gentle hint immediately',
                  'Wants to see the solution step-by-step',
                  'Leaves task temporarily to reset'
                ].map((frust) => (
                  <button
                    key={frust}
                    type="button"
                    onClick={() => handleSelect('frustration_behavior', frust)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.frustration_behavior === frust
                        ? 'bg-purple-50 border-purple-500 text-purple-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {frust}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* STEP 6: ACCESSIBILITY & SENSORY PREFERENCES */}
        {currentStep === 6 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Visual Accessibility Supports
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Dyslexic-friendly font (OpenDyslexic)',
                  'Larger text and generous line spacing',
                  'Reduced motion (disable auto-sliding & animations)',
                  'High contrast mode',
                  'Fewer elements on screen (spacious layout)',
                  'Clear visual breadcrumbs'
                ].map((acc) => {
                  const active = formData.visual_accessibility.includes(acc);
                  return (
                    <button
                      key={acc}
                      type="button"
                      onClick={() => handleToggleMulti('visual_accessibility', acc)}
                      className={`p-4 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between text-left ${
                        active
                          ? 'bg-teal-50 border-teal-500 text-teal-900 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{acc}</span>
                      {active && <Check className="w-4 h-4 text-teal-600" />}
                    </button>
                  );
                })}
              </div>
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Color Palette Theme
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {[
                  'Soft calming pastels (low sensory glare)',
                  'High contrast dark mode',
                  'Minimalist monochrome'
                ].map((pal) => (
                  <button
                    key={pal}
                    type="button"
                    onClick={() => handleSelect('color_palette', pal)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.color_palette === pal
                        ? 'bg-teal-50 border-teal-500 text-teal-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {pal}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* STEP 7: COMMUNICATION & INSTRUCTION */}
        {currentStep === 7 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Instruction Delivery Style
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Single-clause direct instructions (one action per card)',
                  'Short bullet points with icons',
                  'Concrete example shown first',
                  'Visual diagram / flowchart'
                ].map((inst) => (
                  <button
                    key={inst}
                    type="button"
                    onClick={() => handleSelect('instruction_granularity', inst)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.instruction_granularity === inst
                        ? 'bg-emerald-50 border-emerald-500 text-emerald-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {inst}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Feedback Style on Learning Mistakes
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Show the first step gently',
                  'Provide a small clue without revealing answer',
                  'Show a parallel worked example',
                  'Let them retry with 2 options eliminated'
                ].map((feed) => (
                  <button
                    key={feed}
                    type="button"
                    onClick={() => handleSelect('feedback_style', feed)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.feedback_style === feed
                        ? 'bg-emerald-50 border-emerald-500 text-emerald-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {feed}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* STEP 8: EXISTING ACCOMMODATIONS */}
        {currentStep === 8 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Supports currently found helpful at school or home
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Additional time for tasks',
                  'Shorter chunked assignments',
                  'Scheduled visual breaks',
                  'Visual step instructions',
                  'Audio read-aloud / Text-to-speech',
                  'Reduced visual clutter on paper/screen'
                ].map((acc) => {
                  const active = formData.accommodations_used.includes(acc);
                  return (
                    <button
                      key={acc}
                      type="button"
                      onClick={() => handleToggleMulti('accommodations_used', acc)}
                      className={`p-4 rounded-2xl text-xs font-bold border transition-all flex items-center justify-between text-left ${
                        active
                          ? 'bg-cyan-50 border-cyan-500 text-cyan-900 shadow-sm'
                          : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                      }`}
                    >
                      <span>{acc}</span>
                      {active && <Check className="w-4 h-4 text-cyan-600" />}
                    </button>
                  );
                })}
              </div>
            </div>
          </div>
        )}

        {/* STEP 9: ENVIRONMENT & MOTIVATION */}
        {currentStep === 9 && (
          <div className="space-y-6">
            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Sensory Break Rhythm
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {[
                  'Every 5 to 7 minutes with calm sensory animations',
                  'Every 10 to 12 minutes',
                  'Only when learner requests a pause'
                ].map((brk) => (
                  <button
                    key={brk}
                    type="button"
                    onClick={() => handleSelect('break_rhythm', brk)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.break_rhythm === brk
                        ? 'bg-orange-50 border-orange-500 text-orange-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {brk}
                  </button>
                ))}
              </div>
            </div>

            <div className="space-y-3">
              <label className="text-sm font-bold text-slate-800 block">
                Achievement & Celebration Style
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3">
                {[
                  'Visual unlocks (opening new planets, sanctuaries, or cyber parts)',
                  'Quiet star count updates (minimal fanfare)',
                  'Gentle celebratory animations',
                  'Collection vault badges'
                ].map((cel) => (
                  <button
                    key={cel}
                    type="button"
                    onClick={() => handleSelect('celebration_style', cel)}
                    className={`p-4 rounded-2xl text-xs font-bold border transition-all text-left ${
                      formData.celebration_style === cel
                        ? 'bg-orange-50 border-orange-500 text-orange-900 shadow-sm'
                        : 'bg-slate-50/70 border-slate-200 text-slate-700 hover:bg-white'
                    }`}
                  >
                    {cel}
                  </button>
                ))}
              </div>
            </div>
          </div>
        )}

        {/* STEP 10: REVIEW & CONSENT */}
        {currentStep === 10 && (
          <div className="space-y-6">
            <div className="p-4 bg-slate-50 border border-slate-200 rounded-2xl space-y-3">
              <div className="flex items-center justify-between">
                <h3 className="text-sm font-bold text-slate-900 flex items-center gap-2">
                  <Edit3 className="w-4 h-4 text-blue-600" />
                  <span>Summary of Learning Support Profile</span>
                </h3>
                <span className="text-xs text-slate-500 font-medium">Click any item to edit</span>
              </div>

              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs">
                <div 
                  onClick={() => setCurrentStep(1)}
                  className="p-3 bg-white rounded-xl border border-slate-200 cursor-pointer hover:border-blue-300"
                >
                  <span className="text-slate-400 block mb-0.5">Learner & Grade</span>
                  <span className="font-bold text-slate-800">{formData.learner_name} — {formData.grade_level}</span>
                </div>
                <div 
                  onClick={() => setCurrentStep(1)}
                  className="p-3 bg-white rounded-xl border border-slate-200 cursor-pointer hover:border-blue-300"
                >
                  <span className="text-slate-400 block mb-0.5">Special Interests</span>
                  <span className="font-bold text-slate-800">{formData.interest_anchors.join(', ')}</span>
                </div>
                <div 
                  onClick={() => setCurrentStep(4)}
                  className="p-3 bg-white rounded-xl border border-slate-200 cursor-pointer hover:border-blue-300"
                >
                  <span className="text-slate-400 block mb-0.5">Reading Volume</span>
                  <span className="font-bold text-slate-800">{formData.reading_text_volume}</span>
                </div>
                <div 
                  onClick={() => setCurrentStep(6)}
                  className="p-3 bg-white rounded-xl border border-slate-200 cursor-pointer hover:border-blue-300"
                >
                  <span className="text-slate-400 block mb-0.5">Sensory & Palette</span>
                  <span className="font-bold text-slate-800">{formData.color_palette}</span>
                </div>
              </div>
            </div>

            <div className="p-4 bg-emerald-50/90 border border-emerald-200 rounded-2xl flex items-start gap-3">
              <ShieldCheck className="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" />
              <div className="text-xs text-emerald-900 leading-relaxed space-y-1">
                <strong className="block font-bold">Data Sovereignty & Continuous Adaptation</strong>
                This profile serves as your learner's initial support baseline. As they complete activities, NeuroQuest dynamically adapts pacing and scaffolding while respecting these boundaries. Zero clinical or diagnostic labels are ever assigned.
              </div>
            </div>
          </div>
        )}

        {/* Navigation Control Buttons */}
        <div className="pt-6 border-t border-slate-100 flex items-center justify-between gap-4">
          <button
            type="button"
            onClick={handlePrev}
            disabled={currentStep === 1 || loading}
            className={`flex items-center gap-2 px-5 py-3 rounded-2xl text-xs font-bold transition-all ${
              currentStep === 1
                ? 'opacity-40 cursor-not-allowed text-slate-400'
                : 'bg-slate-100 hover:bg-slate-200 text-slate-700'
            }`}
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Previous</span>
          </button>

          <div className="flex items-center gap-3">
            {stepMeta.isOptional && currentStep === 2 && (
              <button
                type="button"
                onClick={() => setCurrentStep(3)}
                className="px-4 py-3 rounded-2xl text-xs font-bold text-slate-500 hover:text-slate-800 transition-all"
              >
                Skip Optional Step
              </button>
            )}

            <button
              type="button"
              onClick={handleNext}
              disabled={loading}
              className="flex items-center gap-2 px-6 py-3.5 rounded-2xl text-xs font-bold bg-blue-600 hover:bg-blue-700 text-white shadow-md shadow-blue-500/20 transition-all disabled:opacity-50"
            >
              {loading ? (
                <span>Generating Support Profile...</span>
              ) : currentStep === 10 ? (
                <>
                  <span>Create Learning Support Profile</span>
                  <Check className="w-4 h-4" />
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
    </div>
  );
}
