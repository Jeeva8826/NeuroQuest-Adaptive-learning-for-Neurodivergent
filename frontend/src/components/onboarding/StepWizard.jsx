import React, { useState } from 'react';
import { 
  Sparkles, Palette, Volume2, BookOpen, Gift, ShieldAlert,
  ArrowRight, ArrowLeft, Check, HelpCircle, Eye, Clock, Layers,
  Compass, Heart, Zap, Sliders
} from 'lucide-react';
import AudioButton from '../common/AudioButton';

export const CAREGIVER_20_QUESTIONS = [
  // SECTION 1: LEARNING ENVIRONMENT & MODALITIES (Q1 - Q5)
  {
    id: 'q1_learning_environment',
    section: 0,
    number: 1,
    title: 'Preferred Learning Environment',
    subtitle: 'Where does the learner feel most comfortable and attentive during learning activities?',
    options: [
      'Quiet, distraction-minimized space with soft ambient lighting',
      'Gentle background music or calming white noise',
      'Interactive room with freedom for physical movement',
      'Co-learning space alongside a supporting parent or educator'
    ]
  },
  {
    id: 'q2_content_format',
    section: 0,
    number: 2,
    title: 'Preferred Content Format',
    subtitle: 'Which format helps the learner grasp new educational ideas most naturally?',
    options: [
      'Visual diagrams, infographics & structured charts',
      'Spoken audio explanations & read-aloud storytelling',
      'Hands-on interactive simulations & manipulative widgets',
      'Bite-sized concise text cards with bullet points'
    ]
  },
  {
    id: 'q3_text_tolerance',
    section: 0,
    number: 3,
    title: 'Text Tolerance',
    subtitle: 'What amount of continuous reading text is most comfortable per screen?',
    options: [
      'Bite-sized sentences (1 to 2 short lines per card)',
      'Short paragraphs (3 to 4 lines with generous line spacing)',
      'Bullet-point summaries & visual cue cards',
      'Standard multi-paragraph descriptive passages'
    ]
  },
  {
    id: 'q4_visual_support',
    section: 0,
    number: 4,
    title: 'Visual Support Preference',
    subtitle: 'How much visual framing assists the learner in retaining concepts?',
    options: [
      'High visual support (icons, color-coded clues, diagrams on every concept)',
      'Moderate visual support (supporting illustrations for key anchor ideas)',
      'Clean minimal visual layout (plain text to prevent visual clutter)',
      'Custom thematic artwork based on learner special interests (e.g. Space, Animals)'
    ]
  },
  {
    id: 'q5_audio_support',
    section: 0,
    number: 5,
    title: 'Audio Support Preference',
    subtitle: 'How should spoken speech and auditory cues be used during lessons?',
    options: [
      'Automatic read-aloud narration for all lesson prompts',
      'On-demand audio button (learner taps to listen when helpful)',
      'Subtle pleasant chime cues for milestone completions',
      'Quiet mode only (no automatic audio or sound effects)'
    ]
  },

  // SECTION 2: PACING, DISTRACTION & CONTENT DENSITY (Q6 - Q10)
  {
    id: 'q6_pace_preference',
    section: 1,
    number: 6,
    title: 'Pace Preference',
    subtitle: 'What rhythm of pacing best supports the learner without causing anxiety?',
    options: [
      'Completely untimed, relaxed exploration with zero clock pressure',
      'Structured, steady step-by-step tempo',
      'Brisk pace with short rapid check-ins',
      'Learner-driven pace with pause-and-resume anytime'
    ]
  },
  {
    id: 'q7_response_time',
    section: 1,
    number: 7,
    title: 'Response Time & Processing',
    subtitle: 'How does the learner typically approach thinking through a question?',
    options: [
      'Needs extended time to reflect before selecting an answer',
      'Standard response duration',
      'Tends to answer very quickly; benefits from a gentle "double check" pause',
      'Variable response time depending on energy and interest level'
    ]
  },
  {
    id: 'q8_distraction_sensitivity',
    section: 1,
    number: 8,
    title: 'Distraction Sensitivity',
    subtitle: 'How do visual motions or background elements affect concentration?',
    options: [
      'High sensitivity — moving elements, flashing or sliding animations break focus',
      'Moderate sensitivity — unexpected popups or side banners cause distraction',
      'Low sensitivity — comfortably filters out secondary interface elements',
      'Benefits from dedicated Focus Mode hiding headers and navigation bars'
    ]
  },
  {
    id: 'q9_content_density',
    section: 1,
    number: 9,
    title: 'Content Density on Screen',
    subtitle: 'How much information should be displayed simultaneously?',
    options: [
      'Single-concept focus (exactly one idea and one action per screen)',
      'Dual-card view (concept explanation alongside one example)',
      'Balanced lesson view with gradual progressive disclosure',
      'Comprehensive layout with side-by-side reference notes'
    ]
  },
  {
    id: 'q10_task_chunking',
    section: 1,
    number: 10,
    title: 'Task Chunking & Milestone Size',
    subtitle: 'What challenge size creates the most satisfying sense of completion?',
    options: [
      'Micro-challenges (1 to 2 minutes each)',
      'Short missions (3 to 5 minutes each)',
      'Standard learning blocks (8 to 12 minutes each)',
      'Modular checkpoints with learner-controlled progress'
    ]
  },

  // SECTION 3: INSTRUCTION, REPETITION & FRUSTRATION RECOVERY (Q11 - Q15)
  {
    id: 'q11_repetition_preference',
    section: 2,
    number: 11,
    title: 'Repetition & Spiral Review',
    subtitle: 'How should learned concepts be revisited over time for solid retention?',
    options: [
      'Spiral review (concept revisited with new fresh analogies and themes)',
      'Direct immediate reinforcement with similar practice questions',
      'Gentle reminder cards only after a break or new session',
      'No repetition needed if the concept was solved correctly on first try'
    ]
  },
  {
    id: 'q12_instruction_complexity',
    section: 2,
    number: 12,
    title: 'Instruction Complexity',
    subtitle: 'What style of instruction prompt is easiest to follow?',
    options: [
      'Single-clause direct action ("Select the plant organ that absorbs sunlight")',
      'Numbered 2-step checklists ("1. Observe the chart, 2. Pick the matching answer")',
      'Visual flowcards or picture-supported instruction cards',
      'Conversational guided dialogue from the AI mentor companion'
    ]
  },
  {
    id: 'q13_difficulty_tolerance',
    section: 2,
    number: 13,
    title: 'Difficulty Progression & Challenge Ramp',
    subtitle: 'How does the learner respond as questions become more challenging?',
    options: [
      'Prefers high early success with very gradual challenge ramps',
      'Comfortable with gentle challenge provided hints are free and non-penalized',
      'Enjoys tricky puzzle challenges with no penalty for retrying',
      'Sensitive to sudden difficulty spikes; needs a reliable safety net'
    ]
  },
  {
    id: 'q14_frustration_recovery',
    section: 2,
    number: 14,
    title: 'Frustration Recovery During Repeated Errors',
    subtitle: 'When an answer is missed multiple times, what intervention helps most?',
    options: [
      'Offer a 1-minute calming sensory break or breathing visual exercise',
      'Provide an immediate step-by-step worked example demonstrating the concept',
      'Pivot gently to a simpler related concept to rebuild confidence',
      'Present a gentle guiding clue without displaying red error banners'
    ]
  },
  {
    id: 'q15_example_preference',
    section: 2,
    number: 15,
    title: 'Preference for Examples & Analogies',
    subtitle: 'What types of examples make abstract academic principles click?',
    options: [
      'Concrete step-by-step worked example shown before attempting questions',
      'Real-world analogy tied to child\'s special interest (e.g. Space, Animals, Coding)',
      'Interactive sandbox where child can manipulate inputs and observe results',
      'Side-by-side comparison contrasting the correct approach with a common misconception'
    ]
  },

  // SECTION 4: GUIDANCE, BREAKS, REINFORCEMENT & ACCOMMODATIONS (Q16 - Q20)
  {
    id: 'q16_step_guidance',
    section: 3,
    number: 16,
    title: 'Step-by-Step Scaffolding Guidance',
    subtitle: 'How proactive should the AI learning scaffold be during problem solving?',
    options: [
      'Always scaffolded (automatically break complex questions into smaller mini-steps)',
      'Guided upon request (learner taps for step-by-step assistance when needed)',
      'Try independently first, offer graduated scaffolding after hesitation',
      'Summary steps provided at the conclusion of each lesson'
    ]
  },
  {
    id: 'q17_break_frequency',
    section: 3,
    number: 17,
    title: 'Breaks Between Learning Activities',
    subtitle: 'How often should gentle cognitive breaks and breathing pauses be offered?',
    options: [
      'Every 5 to 7 minutes with calm sensory animations',
      'After every 3 completed task milestones',
      'Learner-initiated whenever the "Take a Break" button is clicked',
      'Triggered automatically when cognitive fatigue or rapid clicking is detected'
    ]
  },
  {
    id: 'q18_reinforcement_style',
    section: 3,
    number: 18,
    title: 'Preferred Reinforcement & Reward Style',
    subtitle: 'What positive reinforcement motivates the learner without causing competitive stress?',
    options: [
      'Visual unlocks (opening new planets, sanctuaries, or cyber lab components)',
      'Non-competitive mastery progress tree (watching conceptual branches blossom)',
      'Warm encouraging verbal praise from friendly AI mentor',
      'Collecting interest-themed badges and milestone stars'
    ]
  },
  {
    id: 'q19_support_communication',
    section: 3,
    number: 19,
    title: 'Mentor Communication & Persona',
    subtitle: 'What tone of interaction creates a welcoming, supportive atmosphere?',
    options: [
      'Warm, encouraging and patient mentor companion persona',
      'Calm, neutral, concise and matter-of-fact educational guide',
      'Audio voice companion with gentle spoken prompts',
      'Visual mascot providing non-verbal supportive cues'
    ]
  },
  {
    id: 'q20_accommodations',
    section: 3,
    number: 20,
    isMultiSelect: true,
    title: 'Classroom & Digital Accommodations',
    subtitle: 'Select any accessibility features currently found helpful (choose all that apply):',
    options: [
      'OpenDyslexic font with increased character & line spacing',
      'Calm color palette (soft pastels or high-contrast dark theme)',
      'Text-to-speech read aloud with synchronized word highlighting',
      'Reduced motion (disable auto-sliding and flashing animations)',
      'Thematic skin matching child\'s special interest (Space, Animals, Coding)'
    ]
  }
];

export const SECTION_METADATA = [
  {
    title: 'Environment & Modalities',
    icon: Compass,
    color: 'text-blue-600',
    bg: 'bg-blue-50',
    description: 'Setting up the physical learning space, preferred media formats, and visual/audio tolerances.'
  },
  {
    title: 'Pacing & Density',
    icon: Clock,
    color: 'text-amber-600',
    bg: 'bg-amber-50',
    description: 'Calibrating comfortable speed, processing response time, and screen clutter sensitivity.'
  },
  {
    title: 'Guidance & Recovery',
    icon: Heart,
    color: 'text-emerald-600',
    bg: 'bg-emerald-50',
    description: 'Configuring instruction style, examples, and gentle recovery from learning mistakes.'
  },
  {
    title: 'Reinforcement & Accommodations',
    icon: Gift,
    color: 'text-purple-600',
    bg: 'bg-purple-50',
    description: 'Personalizing rewards, break intervals, mentor communication, and accessibility tools.'
  }
];

export default function StepWizard({ onSubmit, loading }) {
  const [currentSection, setCurrentSection] = useState(0);

  const [formData, setFormData] = useState({
    // 20 Core Non-Diagnostic Fields
    q1_learning_environment: CAREGIVER_20_QUESTIONS[0].options[0],
    q2_content_format: CAREGIVER_20_QUESTIONS[1].options[0],
    q3_text_tolerance: CAREGIVER_20_QUESTIONS[2].options[0],
    q4_visual_support: CAREGIVER_20_QUESTIONS[3].options[0],
    q5_audio_support: CAREGIVER_20_QUESTIONS[4].options[1],
    q6_pace_preference: CAREGIVER_20_QUESTIONS[5].options[0],
    q7_response_time: CAREGIVER_20_QUESTIONS[6].options[0],
    q8_distraction_sensitivity: CAREGIVER_20_QUESTIONS[7].options[0],
    q9_content_density: CAREGIVER_20_QUESTIONS[8].options[0],
    q10_task_chunking: CAREGIVER_20_QUESTIONS[9].options[0],
    q11_repetition_preference: CAREGIVER_20_QUESTIONS[10].options[0],
    q12_instruction_complexity: CAREGIVER_20_QUESTIONS[11].options[0],
    q13_difficulty_tolerance: CAREGIVER_20_QUESTIONS[12].options[0],
    q14_frustration_recovery: CAREGIVER_20_QUESTIONS[13].options[0],
    q15_example_preference: CAREGIVER_20_QUESTIONS[14].options[1],
    q16_step_guidance: CAREGIVER_20_QUESTIONS[15].options[0],
    q17_break_frequency: CAREGIVER_20_QUESTIONS[16].options[0],
    q18_reinforcement_style: CAREGIVER_20_QUESTIONS[17].options[0],
    q19_support_communication: CAREGIVER_20_QUESTIONS[18].options[0],
    q20_accommodations: [
      'OpenDyslexic font with increased character & line spacing',
      'Calm color palette (soft pastels or high-contrast dark theme)'
    ],

    // Special interest tag
    special_interest: 'Space',
    
    // Legacy helper fields for backward compatibility
    q1_enjoyed_topics: 'Space Exploration, Astronomy',
    q2_engaging_activities: 'Building Lego models and observing planets',
    q3_themes: ['Space', 'Animals'],
    q6_favorite_color: 'blue',
    q8_color_palette_preference: 'soft',
    q9_visual_style_preference: 'mixture',
    q10_animation_effect: 'distract',
    q11_sound_effect: 'help',
    q12_prefer_calm_screen: true,
    q15_learning_modality: ['Seeing', 'Doing'],
    q16_task_structure: 'step_by_step',
    q17_difficulty_reaction: 'needs_break',
    q19_feedback_style: 'immediate',
    q21_reward_types: ['Unlocking something', 'Collecting objects']
  });

  const handleSelectOption = (field, option) => {
    setFormData(prev => ({ ...prev, [field]: option }));
  };

  const handleToggleMulti = (field, option) => {
    setFormData(prev => {
      const current = prev[field] || [];
      const exists = current.includes(option);
      const updated = exists ? current.filter(x => x !== option) : [...current, option];
      return { ...prev, [field]: updated };
    });
  };

  const currentQuestions = CAREGIVER_20_QUESTIONS.filter(q => q.section === currentSection);
  const totalSections = SECTION_METADATA.length;
  const currentMeta = SECTION_METADATA[currentSection];
  const IconComponent = currentMeta.icon;

  const handleNext = () => {
    if (currentSection < totalSections - 1) {
      setCurrentSection(s => s + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } else {
      onSubmit(formData);
    }
  };

  const handlePrev = () => {
    if (currentSection > 0) {
      setCurrentSection(s => s - 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  return (
    <div className="bg-white rounded-3xl border border-slate-200/80 shadow-sm overflow-hidden transition-all">
      {/* Header Banner */}
      <div className="p-6 sm:p-8 bg-gradient-to-r from-slate-50 via-white to-indigo-50/40 border-b border-slate-100">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
          <div className="flex items-center gap-3">
            <div className={`p-3 rounded-2xl ${currentMeta.bg} ${currentMeta.color} shadow-sm`}>
              <IconComponent className="w-6 h-6" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-semibold px-2.5 py-0.5 rounded-full bg-slate-200/70 text-slate-700">
                  Section {currentSection + 1} of {totalSections}
                </span>
                <span className="text-xs font-medium text-emerald-700 bg-emerald-50 px-2 py-0.5 rounded-full border border-emerald-200">
                  Strictly Non-Diagnostic
                </span>
              </div>
              <h2 className="text-xl sm:text-2xl font-bold text-slate-900 mt-1">
                {currentMeta.title}
              </h2>
              <p className="text-sm text-slate-500 mt-0.5">
                {currentMeta.description}
              </p>
            </div>
          </div>

          <div className="flex items-center gap-2 self-start sm:self-auto">
            <AudioButton 
              text={`Section ${currentSection + 1}: ${currentMeta.title}. ${currentMeta.description}`} 
              className="bg-white shadow-xs border border-slate-200 text-slate-600 hover:text-slate-900"
            />
          </div>
        </div>

        {/* Progress Dots */}
        <div className="grid grid-cols-4 gap-2 mt-6">
          {SECTION_METADATA.map((meta, idx) => (
            <div 
              key={meta.title}
              className={`h-2 rounded-full transition-all duration-300 ${
                idx === currentSection 
                  ? 'bg-indigo-600 ring-2 ring-indigo-200' 
                  : idx < currentSection 
                    ? 'bg-emerald-500' 
                    : 'bg-slate-200'
              }`}
            />
          ))}
        </div>
      </div>

      {/* Questions Form Area */}
      <div className="p-6 sm:p-8 space-y-8">
        {currentQuestions.map((q) => {
          const isMulti = q.isMultiSelect;
          const selectedValue = formData[q.id];

          return (
            <div 
              key={q.id}
              className="p-5 sm:p-6 rounded-2xl bg-slate-50/70 border border-slate-200/70 hover:border-slate-300 transition-all space-y-4"
            >
              <div className="flex items-start justify-between gap-3">
                <div>
                  <div className="flex items-center gap-2">
                    <span className="text-xs font-extrabold px-2 py-0.5 rounded-md bg-white border border-slate-200 text-slate-700 shadow-xs">
                      Q{q.number}
                    </span>
                    <h3 className="text-base sm:text-lg font-bold text-slate-900">
                      {q.title}
                    </h3>
                  </div>
                  <p className="text-sm text-slate-600 mt-1">
                    {q.subtitle}
                  </p>
                </div>
                <AudioButton text={`${q.title}. ${q.subtitle}`} />
              </div>

              {/* Options Grid */}
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-2">
                {q.options.map((opt) => {
                  const isSelected = isMulti 
                    ? Array.isArray(selectedValue) && selectedValue.includes(opt)
                    : selectedValue === opt;

                  return (
                    <button
                      key={opt}
                      type="button"
                      onClick={() => isMulti ? handleToggleMulti(q.id, opt) : handleSelectOption(q.id, opt)}
                      className={`text-left p-3.5 sm:p-4 rounded-xl text-sm font-medium transition-all duration-200 border flex items-start gap-3 ${
                        isSelected
                          ? 'bg-indigo-50 border-indigo-500 text-indigo-900 shadow-xs ring-1 ring-indigo-400'
                          : 'bg-white border-slate-200 text-slate-700 hover:bg-slate-100/70 hover:border-slate-300'
                      }`}
                    >
                      <div className={`w-5 h-5 rounded-${isMulti ? 'md' : 'full'} mt-0.5 flex-shrink-0 flex items-center justify-center border transition-all ${
                        isSelected 
                          ? 'bg-indigo-600 border-indigo-600 text-white' 
                          : 'border-slate-300 bg-white'
                      }`}>
                        {isSelected && <Check className="w-3.5 h-3.5 stroke-[3]" />}
                      </div>
                      <span className="flex-1 leading-snug">{opt}</span>
                    </button>
                  );
                })}
              </div>
            </div>
          );
        })}

        {/* Special Interest Selector in Section 4 */}
        {currentSection === 3 && (
          <div className="p-6 rounded-2xl bg-indigo-50/50 border border-indigo-200/80 space-y-4">
            <div className="flex items-center gap-2">
              <Sparkles className="w-5 h-5 text-indigo-600" />
              <h3 className="text-base font-bold text-indigo-950">
                Primary Motivation Theme
              </h3>
            </div>
            <p className="text-sm text-indigo-800">
              Choose the learner's favorite topic to theme lessons, game worlds, and achievement missions:
            </p>
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-3">
              {[
                { id: 'Space', label: '🚀 Space & Planets' },
                { id: 'Animals', label: '🐾 Animals & Wildlife' },
                { id: 'Coding', label: '🤖 Coding & Robotics' },
                { id: 'Nature', label: '🌿 Nature & Plants' }
              ].map(th => (
                <button
                  key={th.id}
                  type="button"
                  onClick={() => {
                    handleSelectOption('special_interest', th.id);
                    handleSelectOption('q3_themes', [th.id]);
                  }}
                  className={`p-3 rounded-xl border text-sm font-semibold transition-all ${
                    formData.special_interest === th.id
                      ? 'bg-indigo-600 border-indigo-600 text-white shadow-xs'
                      : 'bg-white border-indigo-200 text-slate-800 hover:bg-white/80'
                  }`}
                >
                  {th.label}
                </button>
              ))}
            </div>
          </div>
        )}
      </div>

      {/* Navigation Footer */}
      <div className="p-6 sm:p-8 bg-slate-50/90 border-t border-slate-200/80 flex items-center justify-between gap-4">
        <button
          type="button"
          onClick={handlePrev}
          disabled={currentSection === 0 || loading}
          className={`flex items-center gap-2 px-5 py-2.5 rounded-xl font-semibold text-sm border transition-all ${
            currentSection === 0 || loading
              ? 'opacity-40 cursor-not-allowed bg-slate-100 border-slate-200 text-slate-400'
              : 'bg-white border-slate-300 text-slate-700 hover:bg-slate-100'
          }`}
        >
          <ArrowLeft className="w-4 h-4" />
          Previous Section
        </button>

        <button
          type="button"
          onClick={handleNext}
          disabled={loading}
          className="flex items-center gap-2 px-6 py-2.5 rounded-xl font-bold text-sm bg-indigo-600 text-white hover:bg-indigo-700 shadow-sm hover:shadow transition-all"
        >
          {loading ? (
            <span>Saving Profile...</span>
          ) : currentSection === totalSections - 1 ? (
            <>
              <span>Complete Assessment</span>
              <Check className="w-4 h-4" />
            </>
          ) : (
            <>
              <span>Continue to Section {currentSection + 2}</span>
              <ArrowRight className="w-4 h-4" />
            </>
          )}
        </button>
      </div>
    </div>
  );
}
