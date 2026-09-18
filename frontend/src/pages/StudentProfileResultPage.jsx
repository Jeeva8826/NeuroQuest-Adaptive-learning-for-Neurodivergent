import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { 
  ShieldCheck, Sparkles, CheckCircle2, Rocket, ArrowRight, 
  Settings, Eye, Sliders, Volume2, BookOpen, Clock, Heart, 
  RefreshCw, CheckCircle, Compass, Layers, Zap, AlertCircle
} from 'lucide-react';
import { getStudentBaselineProfile, getStudent } from '../services/api';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';
import AudioButton from '../components/common/AudioButton';

const StudentProfileResultPage = () => {
  const { studentId } = useParams();
  const navigate = useNavigate();

  const [loading, setLoading] = useState(true);
  const [profile, setProfile] = useState(null);
  const [student, setStudent] = useState(null);
  const [error, setError] = useState('');

  useEffect(() => {
    fetchProfileData();
  }, [studentId]);

  const fetchProfileData = async () => {
    try {
      setLoading(true);
      const [profRes, studRes] = await Promise.all([
        getStudentBaselineProfile(studentId),
        getStudent(studentId).catch(() => null)
      ]);

      setProfile(profRes.data);
      if (studRes?.data) {
        setStudent(studRes.data);
      }
    } catch (err) {
      console.error('Failed to fetch baseline profile:', err);
      setError('Could not load student baseline profile. Please complete the assessment.');
    } finally {
      setLoading(false);
    }
  };

  const handleLaunchStudentExperience = () => {
    // Persist active student ID in localStorage so the learner experience loads this student's profile
    localStorage.setItem('neuroquest_active_student_id', studentId);
    if (student?.name || profile?.student_name) {
      localStorage.setItem('neuroquest_active_student_name', student?.name || profile?.student_name);
    }
    
    // Launch directly into the student experience
    navigate('/home');
  };

  if (loading) {
    return (
      <div className="min-h-screen flex flex-col bg-slate-50">
        <Navbar />
        <div className="flex-1 flex flex-col items-center justify-center gap-4">
          <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin" />
          <p className="text-slate-600 font-semibold text-sm">Building Baseline Support Profile...</p>
        </div>
        <Footer />
      </div>
    );
  }

  if (error || !profile) {
    return (
      <div className="min-h-screen flex flex-col bg-slate-50">
        <Navbar />
        <main className="flex-1 max-w-2xl mx-auto px-4 py-16 text-center space-y-6">
          <div className="w-16 h-16 bg-rose-100 text-rose-600 rounded-3xl flex items-center justify-center mx-auto">
            <AlertCircle className="w-8 h-8" />
          </div>
          <h2 className="text-2xl font-black text-slate-900">Baseline Assessment Required</h2>
          <p className="text-slate-600 text-sm">
            {error || 'No completed baseline profile found for this student.'}
          </p>
          <div className="flex justify-center gap-3">
            <button
              onClick={() => navigate(`/student-screening/${studentId}`)}
              className="px-6 py-3 bg-indigo-600 text-white font-bold rounded-2xl shadow-md text-sm"
            >
              Start 20-Q Assessment
            </button>
            <button
              onClick={() => navigate('/caregiver')}
              className="px-6 py-3 bg-slate-200 text-slate-700 font-bold rounded-2xl text-sm"
            >
              Return to Dashboard
            </button>
          </div>
        </main>
        <Footer />
      </div>
    );
  }

  const studentName = student?.name || profile?.student_name || 'Student';
  const dimensions = profile?.dimensions || [];
  const accommodations = profile?.recommended_accommodations || [];
  const uiConfig = profile?.initial_ui_configuration || {};

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 text-slate-900 font-sans">
      <Navbar />

      <main className="flex-1 max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-10 w-full space-y-8">
        
        {/* Header Hero Banner */}
        <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 rounded-3xl p-6 sm:p-10 text-white shadow-xl relative overflow-hidden">
          <div className="absolute top-0 right-0 w-96 h-96 bg-indigo-500/10 rounded-full blur-3xl pointer-events-none" />
          <div className="absolute bottom-0 left-1/3 w-64 h-64 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none" />

          <div className="relative z-10 flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div className="space-y-3">
              <div className="flex flex-wrap items-center gap-2">
                <span className="px-3 py-1 bg-emerald-500/20 text-emerald-300 rounded-full text-xs font-bold uppercase tracking-wider flex items-center gap-1.5 border border-emerald-400/30">
                  <ShieldCheck className="w-3.5 h-3.5" />
                  Product Baseline v1 • Strictly Non-Diagnostic
                </span>
                <span className="px-3 py-1 bg-indigo-500/20 text-indigo-300 rounded-full text-xs font-semibold">
                  Personalized Profile Active
                </span>
              </div>

              <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight">
                {studentName}'s Learning Support Profile
              </h1>
              <p className="text-slate-300 text-sm sm:text-base max-w-2xl leading-relaxed">
                Initial baseline configurations synthesized from the 20-question caregiver assessment. 
                Ready to power personalized quests, pacing, and sensory adaptations.
              </p>
            </div>

            {/* Launch Experience CTA */}
            <div className="flex flex-col sm:flex-row md:flex-col gap-3 shrink-0">
              <button
                onClick={handleLaunchStudentExperience}
                className="px-8 py-4 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-600 hover:to-teal-600 text-slate-950 font-black rounded-2xl shadow-xl shadow-emerald-500/25 transition-all transform hover:-translate-y-0.5 flex items-center justify-center gap-2 text-base"
              >
                <Rocket className="w-5 h-5 text-slate-950" />
                <span>Launch Student Experience</span>
                <ArrowRight className="w-4 h-4 text-slate-950" />
              </button>

              <AudioButton
                text={`Learning support profile for ${studentName}. 10 educational dimensions configured. Visual density is set to ${uiConfig.visual_density}. Ready to launch student experience.`}
                label="Listen Summary"
                className="bg-white/10 hover:bg-white/20 text-white border-white/20 justify-center"
              />
            </div>
          </div>
        </div>

        {/* UI Configuration Chips */}
        <div className="bg-white p-6 sm:p-7 rounded-3xl border border-slate-200 shadow-sm space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-lg font-bold text-slate-900 flex items-center gap-2">
              <Sliders className="w-5 h-5 text-indigo-600" />
              Pre-Configured Educational Accommodations
            </h2>
            <span className="text-xs text-slate-400 font-semibold">Automatically applied to student sessions</span>
          </div>

          <div className="grid grid-cols-2 sm:grid-cols-4 gap-3.5">
            <div className="p-4 bg-slate-50 rounded-2xl border border-slate-200/80 space-y-1">
              <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">Visual Density</div>
              <div className="text-base font-extrabold text-slate-900 capitalize">{uiConfig.visual_density || 'Spacious'}</div>
              <p className="text-xs text-slate-500">Whitespace & low visual noise</p>
            </div>

            <div className="p-4 bg-slate-50 rounded-2xl border border-slate-200/80 space-y-1">
              <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">Guidance Level</div>
              <div className="text-base font-extrabold text-slate-900 capitalize">{uiConfig.guidance_level || 'High'}</div>
              <p className="text-xs text-slate-500">Step-by-step sequential hints</p>
            </div>

            <div className="p-4 bg-slate-50 rounded-2xl border border-slate-200/80 space-y-1">
              <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">Pacing Pressure</div>
              <div className="text-base font-extrabold text-emerald-600 capitalize">
                {uiConfig.calm_mode ? 'Untimed (Calm)' : 'Self-Paced Soft Timer'}
              </div>
              <p className="text-xs text-slate-500">Zero countdown anxiety</p>
            </div>

            <div className="p-4 bg-slate-50 rounded-2xl border border-slate-200/80 space-y-1">
              <div className="text-xs font-bold text-slate-400 uppercase tracking-wider">Typography</div>
              <div className="text-base font-extrabold text-indigo-600">{uiConfig.font_family || 'OpenDyslexic'}</div>
              <p className="text-xs text-slate-500">High legibility typeface</p>
            </div>
          </div>

          {/* Accommodation Badges */}
          <div className="pt-2 flex flex-wrap gap-2">
            {accommodations.map((acc, idx) => (
              <span
                key={idx}
                className="px-3 py-1.5 bg-indigo-50 text-indigo-800 text-xs font-semibold rounded-xl border border-indigo-100 flex items-center gap-1.5"
              >
                <CheckCircle2 className="w-3.5 h-3.5 text-indigo-600 shrink-0" />
                {acc}
              </span>
            ))}
          </div>
        </div>

        {/* 10 Educational Dimensions Grid */}
        <div className="space-y-4">
          <div>
            <h2 className="text-xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
              <Layers className="w-5 h-5 text-indigo-600" />
              10 Educational Support Dimensions
            </h2>
            <p className="text-slate-500 text-xs sm:text-sm mt-0.5">
              Strictly non-diagnostic learning strategies computed from caregiver observations.
            </p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            {dimensions.map((dim, idx) => {
              const isHigh = (dim.support_level || '').toLowerCase().includes('high') || 
                             (dim.support_level || '').toLowerCase().includes('sequential') ||
                             (dim.support_level || '').toLowerCase().includes('spacious');

              return (
                <div 
                  key={idx}
                  className="bg-white p-6 rounded-3xl border border-slate-200/90 shadow-sm space-y-3 hover:shadow-md transition-shadow"
                >
                  <div className="flex items-start justify-between gap-3">
                    <h3 className="text-base font-bold text-slate-900">
                      {dim.title}
                    </h3>
                    <span className={`px-2.5 py-1 rounded-xl text-xs font-extrabold shrink-0 ${
                      isHigh
                        ? 'bg-amber-50 text-amber-800 border border-amber-200'
                        : 'bg-emerald-50 text-emerald-800 border border-emerald-200'
                    }`}>
                      {dim.support_level}
                    </span>
                  </div>

                  <div className="space-y-1.5 text-xs sm:text-sm">
                    <p className="text-slate-700 leading-relaxed">
                      <span className="font-bold text-slate-900">Strategy: </span>
                      {dim.recommended_strategy}
                    </p>
                    <p className="text-slate-400 text-xs italic">
                      <span className="font-semibold">Observation Rationale: </span>
                      {dim.rationale}
                    </p>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Non-Diagnostic Disclaimer Card */}
        <div className="bg-slate-100 rounded-3xl p-6 border border-slate-200 text-xs text-slate-500 leading-relaxed space-y-2">
          <p className="font-bold text-slate-800 flex items-center gap-1.5 text-sm">
            <ShieldCheck className="w-4 h-4 text-emerald-600" />
            Medical & Clinical Disclaimer (Product Baseline v1)
          </p>
          <p>
            {profile?.disclaimer || 
              "This profile is based on reported observations to personalize the educational experience. It is strictly non-diagnostic and does not constitute or substitute for an assessment by a qualified healthcare or education professional."}
          </p>
        </div>

        {/* Bottom Actions Bar */}
        <div className="flex flex-col sm:flex-row items-center justify-between gap-4 pt-4 border-t border-slate-200">
          <button
            onClick={() => navigate('/caregiver')}
            className="text-slate-500 hover:text-slate-800 text-sm font-semibold transition-colors"
          >
            ← Return to Caregiver Dashboard
          </button>

          <button
            onClick={handleLaunchStudentExperience}
            className="w-full sm:w-auto px-8 py-3.5 bg-indigo-600 hover:bg-indigo-700 text-white font-bold rounded-2xl shadow-lg shadow-indigo-600/20 transition-all flex items-center justify-center gap-2 text-sm"
          >
            <Rocket className="w-4 h-4" />
            <span>Launch Student Experience Now</span>
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </main>

      <Footer />
    </div>
  );
};

export default StudentProfileResultPage;
