import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { 
  Compass, Gamepad2, Sparkles, Sliders, ShieldCheck, 
  ArrowRight, Award, BookOpen, CheckCircle2, HeartHandshake 
} from 'lucide-react';
import Navbar from '../common/Navbar';
import Footer from '../common/Footer';

export const LearnerDashboard = () => {
  const navigate = useNavigate();
  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />
      <main className="flex-1 max-w-5xl mx-auto p-6 space-y-8 w-full">
        <header className="border-b border-slate-200 pb-6 flex flex-col sm:flex-row justify-between sm:items-center gap-4">
          <div>
            <h1 className="text-3xl font-extrabold text-slate-800 tracking-tight">Your Learning Hub</h1>
            <p className="text-slate-500 mt-1">Welcome back! Choose a subject or launch your daily mission.</p>
          </div>
          <button 
            onClick={() => navigate('/home')}
            className="px-4 py-2.5 bg-indigo-600 hover:bg-indigo-700 text-white rounded-xl font-bold shadow-sm flex items-center gap-2 text-sm transition-all"
          >
            <Compass className="w-4 h-4" />
            <span>Open Mission World</span>
          </button>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Course Card 1 */}
          <motion.div whileHover={{ y: -4 }} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
            <div className="flex justify-between items-start mb-4">
              <div>
                <span className="text-xs font-semibold uppercase tracking-wider text-emerald-600 bg-emerald-50 px-2.5 py-1 rounded-full">Science</span>
                <h3 className="text-xl font-bold text-slate-800 mt-2">Nutrition in Plants</h3>
              </div>
              <div className="text-right">
                <span className="block text-2xl font-bold text-slate-800">61%</span>
                <span className="text-xs text-slate-500">Mastery</span>
              </div>
            </div>
            
            <div className="w-full bg-slate-100 rounded-full h-2.5 mb-5">
              <div className="bg-emerald-500 h-2.5 rounded-full" style={{ width: '61%' }}></div>
            </div>
            
            <button 
              onClick={() => navigate('/session')}
              className="w-full py-2.5 bg-indigo-600 text-white rounded-xl font-bold hover:bg-indigo-700 transition-colors flex items-center justify-center gap-2 text-sm shadow-sm"
            >
              <span>Continue Lesson</span>
              <ArrowRight className="w-4 h-4" />
            </button>
          </motion.div>

          {/* Course Card 2 */}
          <motion.div whileHover={{ y: -4 }} className="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
            <div className="flex justify-between items-start mb-4">
              <div>
                <span className="text-xs font-semibold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full">Mathematics</span>
                <h3 className="text-xl font-bold text-slate-800 mt-2">Integers</h3>
              </div>
              <div className="text-right">
                <span className="block text-2xl font-bold text-slate-800">42%</span>
                <span className="text-xs text-slate-500">Mastery</span>
              </div>
            </div>
            
            <div className="w-full bg-slate-100 rounded-full h-2.5 mb-5">
              <div className="bg-blue-500 h-2.5 rounded-full" style={{ width: '42%' }}></div>
            </div>
            
            <button 
              onClick={() => navigate('/games')}
              className="w-full py-2.5 bg-slate-100 text-slate-700 rounded-xl font-bold hover:bg-slate-200 transition-colors flex items-center justify-center gap-2 text-sm"
            >
              <Gamepad2 className="w-4 h-4 text-indigo-600" />
              <span>Practice in Game Arena</span>
            </button>
          </motion.div>
        </div>
      </main>
      <Footer />
    </div>
  );
};

export const CaregiverDashboard = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />

      <main className="flex-1 max-w-6xl mx-auto p-4 sm:p-6 lg:p-8 space-y-8 w-full">
        {/* Top Welcome / Orientation Banner */}
        <div className="bg-gradient-to-r from-indigo-900 via-indigo-800 to-purple-900 text-white p-6 sm:p-8 rounded-3xl shadow-xl relative overflow-hidden">
          <div className="absolute right-0 top-0 translate-x-10 -translate-y-10 w-64 h-64 bg-white/5 rounded-full blur-2xl pointer-events-none" />
          <div className="relative z-10 max-w-3xl space-y-3">
            <div className="inline-flex items-center gap-2 px-3 py-1 bg-white/10 backdrop-blur-md rounded-full text-xs font-bold text-indigo-200 tracking-wide border border-white/10">
              <ShieldCheck className="w-4 h-4 text-emerald-400" />
              <span>Non-Diagnostic Educational Accommodations Active</span>
            </div>
            <h1 className="text-3xl sm:text-4xl font-extrabold tracking-tight">
              Learner Support & Overview Hub
            </h1>
            <p className="text-indigo-100 text-sm sm:text-base leading-relaxed">
              Your account is all set up! NeuroQuest dynamically adapts visual contrast, cognitive pacing, and failure scaffolding to help your learner build mastery without cognitive overload.
            </p>
          </div>
        </div>

        {/* Quick Launch Action Cards (What to do next) */}
        <div>
          <div className="flex items-center justify-between mb-4">
            <div>
              <h2 className="text-xl font-bold text-slate-900">What would you like to explore next?</h2>
              <p className="text-sm text-slate-500">Pick any gateway below to enter lessons, games, or customize preferences.</p>
            </div>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            {/* Gateway 1: Learner Hub */}
            <motion.div 
              whileHover={{ y: -4 }} 
              onClick={() => navigate('/home')}
              className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md hover:border-indigo-200 transition-all cursor-pointer flex flex-col justify-between group"
            >
              <div>
                <div className="w-12 h-12 rounded-xl bg-indigo-50 flex items-center justify-center text-indigo-600 mb-4 group-hover:scale-110 transition-transform">
                  <Compass className="w-6 h-6" />
                </div>
                <h3 className="font-bold text-slate-900 text-base mb-1">Learner Home Hub</h3>
                <p className="text-xs text-slate-500 leading-relaxed">
                  Interactive NCERT subjects (Science, Math, Social Science) with gentle pacing & read-aloud.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-indigo-600 group-hover:text-indigo-700">
                <span>Enter Learner Portal</span>
                <ArrowRight className="w-3.5 h-3.5 ml-1 transition-transform group-hover:translate-x-1" />
              </div>
            </motion.div>

            {/* Gateway 2: Games Arena */}
            <motion.div 
              whileHover={{ y: -4 }} 
              onClick={() => navigate('/games')}
              className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md hover:border-emerald-200 transition-all cursor-pointer flex flex-col justify-between group"
            >
              <div>
                <div className="w-12 h-12 rounded-xl bg-emerald-50 flex items-center justify-center text-emerald-600 mb-4 group-hover:scale-110 transition-transform">
                  <Gamepad2 className="w-6 h-6" />
                </div>
                <h3 className="font-bold text-slate-900 text-base mb-1">NCERT Focus Quests</h3>
                <p className="text-xs text-slate-500 leading-relaxed">
                  4 gamified modules: Concept Match, Build Sequence, Find Signal, and Boss Arena.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-emerald-600 group-hover:text-emerald-700">
                <span>Play Focus Quests</span>
                <ArrowRight className="w-3.5 h-3.5 ml-1 transition-transform group-hover:translate-x-1" />
              </div>
            </motion.div>

            {/* Gateway 3: Interactive Lesson */}
            <motion.div 
              whileHover={{ y: -4 }} 
              onClick={() => navigate('/session')}
              className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md hover:border-purple-200 transition-all cursor-pointer flex flex-col justify-between group"
            >
              <div>
                <div className="w-12 h-12 rounded-xl bg-purple-50 flex items-center justify-center text-purple-600 mb-4 group-hover:scale-110 transition-transform">
                  <Sparkles className="w-6 h-6" />
                </div>
                <h3 className="font-bold text-slate-900 text-base mb-1">Live Adaptive Quest</h3>
                <p className="text-xs text-slate-500 leading-relaxed">
                  Experience the 7-level scaffolding ladder with real-time AI adaptation explainers.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-purple-600 group-hover:text-purple-700">
                <span>Start Live Session</span>
                <ArrowRight className="w-3.5 h-3.5 ml-1 transition-transform group-hover:translate-x-1" />
              </div>
            </motion.div>

            {/* Gateway 4: Student Baseline Screening */}
            <motion.div 
              whileHover={{ y: -4 }} 
              onClick={() => navigate('/student-registration')}
              className="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md hover:border-amber-200 transition-all cursor-pointer flex flex-col justify-between group"
            >
              <div>
                <div className="w-12 h-12 rounded-xl bg-amber-50 flex items-center justify-center text-amber-600 mb-4 group-hover:scale-110 transition-transform">
                  <Sliders className="w-6 h-6" />
                </div>
                <h3 className="font-bold text-slate-900 text-base mb-1">Student Baseline Screening</h3>
                <p className="text-xs text-slate-500 leading-relaxed">
                  Register a learner and complete the 20-question profile to tailor contrast, chunking, and sound.
                </p>
              </div>
              <div className="mt-4 pt-3 border-t border-slate-100 flex items-center text-xs font-bold text-amber-600 group-hover:text-amber-700">
                <span>Register & Screen Student</span>
                <ArrowRight className="w-3.5 h-3.5 ml-1 transition-transform group-hover:translate-x-1" />
              </div>
            </motion.div>
          </div>
        </div>

        {/* Support Settings & Adaptation Efficacy Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
          
          {/* Support Preferences Panel */}
          <div className="lg:col-span-1 bg-white p-6 rounded-2xl border border-slate-200 shadow-sm flex flex-col justify-between">
            <div>
              <div className="flex items-center gap-2 mb-4">
                <Sliders className="w-5 h-5 text-indigo-600" />
                <h3 className="font-bold text-slate-800">Current Accommodations</h3>
              </div>
              <ul className="space-y-3">
                <li className="flex justify-between items-center border-b border-slate-100 pb-2.5">
                  <span className="text-slate-600 text-sm font-medium">Visual Intensity</span>
                  <span className="font-bold text-indigo-700 text-xs bg-indigo-50 px-2.5 py-1 rounded-md border border-indigo-100">High Contrast</span>
                </li>
                <li className="flex justify-between items-center border-b border-slate-100 pb-2.5">
                  <span className="text-slate-600 text-sm font-medium">Pacing Rate</span>
                  <span className="font-bold text-emerald-700 text-xs bg-emerald-50 px-2.5 py-1 rounded-md border border-emerald-100">Slowed & Calm</span>
                </li>
                <li className="flex justify-between items-center border-b border-slate-100 pb-2.5">
                  <span className="text-slate-600 text-sm font-medium">Content Density</span>
                  <span className="font-bold text-blue-700 text-xs bg-blue-50 px-2.5 py-1 rounded-md border border-blue-100">Chunked Concepts</span>
                </li>
                <li className="flex justify-between items-center pb-1">
                  <span className="text-slate-600 text-sm font-medium">Scaffold Assist</span>
                  <span className="font-bold text-purple-700 text-xs bg-purple-50 px-2.5 py-1 rounded-md border border-purple-100">Level 2 (Visual Clues)</span>
                </li>
              </ul>
            </div>
            
            <button 
              onClick={() => navigate('/onboarding')}
              className="mt-6 w-full py-2.5 text-sm text-indigo-700 font-bold bg-indigo-50 hover:bg-indigo-100 rounded-xl transition-colors border border-indigo-200 flex items-center justify-center gap-2"
            >
              <Sliders className="w-4 h-4" />
              <span>Edit Support Preferences</span>
            </button>
          </div>

          {/* Efficacy Analytics */}
          <div className="lg:col-span-2 bg-white p-6 rounded-2xl border border-slate-200 shadow-sm">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <CheckCircle2 className="w-5 h-5 text-emerald-600" />
                <h3 className="font-bold text-slate-800">Adaptation Efficacy & Safety</h3>
              </div>
              <button 
                onClick={() => navigate('/caregiver')}
                className="text-xs font-bold text-indigo-600 hover:text-indigo-800 flex items-center gap-1"
              >
                <span>View Full Caregiver Dashboard</span>
                <ArrowRight className="w-3 h-3" />
              </button>
            </div>
            
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-6">
              <div className="p-4 bg-emerald-50/70 rounded-xl border border-emerald-100">
                <span className="block text-xs text-emerald-800 font-bold mb-1 uppercase tracking-wider">Cognitive Load Resolved</span>
                <span className="text-3xl font-extrabold text-emerald-900">2 / 2</span>
                <span className="block text-xs text-emerald-700 font-medium mt-1">Both de-escalated via gentle breaks</span>
              </div>
              
              <div className="p-4 bg-indigo-50/70 rounded-xl border border-indigo-100">
                <span className="block text-xs text-indigo-800 font-bold mb-1 uppercase tracking-wider">Most Effective Support</span>
                <span className="text-xl font-extrabold text-indigo-900 mt-1 block">Visual Chunking</span>
                <span className="block text-xs text-indigo-700 font-medium mt-1">Boosted completion by +35%</span>
              </div>
            </div>
            
            <div className="space-y-3">
              <h4 className="text-xs font-bold text-slate-500 uppercase tracking-wider">Recent AI Adjustments</h4>
              <div className="flex items-start gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
                <div className="w-2.5 h-2.5 mt-1.5 rounded-full bg-emerald-500 flex-shrink-0"></div>
                <div>
                  <p className="text-sm font-bold text-slate-800">Text density chunked automatically</p>
                  <p className="text-xs text-slate-500">Triggered during Science: Nutrition in Plants at 10:42 AM.</p>
                </div>
              </div>
              <div className="flex items-start gap-3 p-3 bg-slate-50 border border-slate-100 rounded-xl">
                <div className="w-2.5 h-2.5 mt-1.5 rounded-full bg-indigo-500 flex-shrink-0"></div>
                <div>
                  <p className="text-sm font-bold text-slate-800">Visual hint ladder stepped to Level 2</p>
                  <p className="text-xs text-slate-500">Provided interactive visual diagram during Math integers module at 09:15 AM.</p>
                </div>
              </div>
            </div>
          </div>

        </div>
      </main>

      <Footer />
    </div>
  );
};

export const EducatorDashboard = () => {
  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />
      <main className="flex-1 max-w-6xl mx-auto p-6 space-y-8 w-full">
        <header className="border-b border-slate-200 pb-6 flex justify-between items-end">
          <div>
            <h1 className="text-3xl font-bold text-slate-800">Class Learning Map</h1>
            <p className="text-slate-500 mt-2">Aggregate view of class mastery and adaptation trends.</p>
          </div>
          <button className="px-4 py-2 bg-slate-800 text-white rounded-lg text-sm font-medium hover:bg-slate-700">
            Export Report
          </button>
        </header>
        
        <div className="bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-slate-50 border-b border-slate-200">
                <th className="p-4 text-sm font-semibold text-slate-600">Concept</th>
                <th className="p-4 text-sm font-semibold text-slate-600">Avg Mastery</th>
                <th className="p-4 text-sm font-semibold text-slate-600">Common Difficulty</th>
                <th className="p-4 text-sm font-semibold text-slate-600">Effective Scaffold</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-100">
              <tr className="hover:bg-slate-50 transition-colors">
                <td className="p-4 text-sm font-medium text-slate-800">Nutrition in Plants</td>
                <td className="p-4 text-sm"><span className="text-emerald-600 font-bold">82%</span></td>
                <td className="p-4 text-sm text-slate-600">Multi-step sequences</td>
                <td className="p-4 text-sm text-slate-600">Visual workflows</td>
              </tr>
              <tr className="hover:bg-slate-50 transition-colors">
                <td className="p-4 text-sm font-medium text-slate-800">Heat</td>
                <td className="p-4 text-sm"><span className="text-amber-600 font-bold">71%</span></td>
                <td className="p-4 text-sm text-slate-600">Abstract definitions</td>
                <td className="p-4 text-sm text-slate-600">Real-world examples</td>
              </tr>
              <tr className="hover:bg-slate-50 transition-colors">
                <td className="p-4 text-sm font-medium text-slate-800">Acids & Bases</td>
                <td className="p-4 text-sm"><span className="text-rose-600 font-bold">63%</span></td>
                <td className="p-4 text-sm text-slate-600">Categorization rules</td>
                <td className="p-4 text-sm text-slate-600">Concept sorting games</td>
              </tr>
            </tbody>
          </table>
        </div>
      </main>
      <Footer />
    </div>
  );
};
