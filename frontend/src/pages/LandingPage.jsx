import React from 'react';
import { Link } from 'react-router-dom';
import { ShieldCheck, ArrowRight, Layout, Volume2, Cpu, UserCheck } from 'lucide-react';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';

const LandingPage = () => {
  return (
    <div className="min-h-screen flex flex-col bg-slate-50 font-sans text-slate-800">
      <Navbar />

      {/* Hero Section */}
      <section className="py-20 px-4 sm:px-6 lg:px-8 max-w-6xl mx-auto w-full">
        <div className="text-center max-w-3xl mx-auto space-y-8">
          
          <div className="inline-flex items-center gap-2 px-3 py-1 rounded-sm text-xs font-bold uppercase tracking-widest bg-emerald-100 text-emerald-900 border border-emerald-200">
            <ShieldCheck className="w-4 h-4 text-emerald-700" />
            Adaptive Education Platform
          </div>

          <h1 className="text-4xl sm:text-5xl font-extrabold text-slate-900 leading-tight">
            Education structured for the way you actually learn.
          </h1>

          <p className="text-slate-600 text-lg sm:text-xl font-normal leading-relaxed max-w-2xl mx-auto">
            NeuroQuest provides a calm, sensory-friendly, and highly structured learning environment that adapts to your pacing, density needs, and visual preferences.
          </p>

          <div className="pt-6 flex flex-col sm:flex-row items-center justify-center gap-4">
            <Link
              to="/register"
              className="w-full sm:w-auto px-8 py-3 rounded-md text-base font-bold text-white bg-slate-800 hover:bg-slate-700 transition-colors flex items-center justify-center gap-2 shadow-sm"
            >
              <span>Get Started</span>
              <ArrowRight className="w-4 h-4" />
            </Link>
            <Link
              to="/login"
              className="w-full sm:w-auto px-8 py-3 rounded-md text-base font-medium text-slate-700 bg-white border border-slate-300 hover:bg-slate-100 transition-colors flex items-center justify-center"
            >
              Sign In
            </Link>
          </div>

          {/* Core Principle Box */}
          <div className="mt-16 bg-white p-6 rounded-lg border border-slate-200 shadow-sm text-left max-w-2xl mx-auto flex items-start gap-4">
            <div className="w-10 h-10 rounded bg-slate-100 text-slate-600 flex items-center justify-center shrink-0">
              <UserCheck className="w-5 h-5" />
            </div>
            <div>
              <div className="text-xs uppercase tracking-wider font-bold text-slate-500 mb-1">
                Core Philosophy
              </div>
              <p className="text-sm font-medium text-slate-700 leading-relaxed">
                "No medical labels. No assumptions. We build the interface around the learner's current needs, recognizing that those needs may change day to day."
              </p>
            </div>
          </div>

        </div>
      </section>

      {/* Feature Grid */}
      <section className="py-16 bg-white border-t border-slate-200">
        <div className="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="mb-12">
            <h2 className="text-2xl font-bold text-slate-900">
              Platform Capabilities
            </h2>
            <div className="w-12 h-1 bg-emerald-500 mt-4"></div>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div className="p-6 rounded-lg bg-slate-50 border border-slate-100 space-y-4">
              <Layout className="w-6 h-6 text-slate-700" />
              <h3 className="text-lg font-bold text-slate-900">Structural Adaptation</h3>
              <p className="text-sm text-slate-600 leading-relaxed">
                Automatically chunks large paragraphs, adjusts text density, and alters pacing based on real-time cognitive load indicators.
              </p>
            </div>

            <div className="p-6 rounded-lg bg-slate-50 border border-slate-100 space-y-4">
              <Volume2 className="w-6 h-6 text-slate-700" />
              <h3 className="text-lg font-bold text-slate-900">Sensory Controls</h3>
              <p className="text-sm text-slate-600 leading-relaxed">
                Full control over visual themes, contrast ratios, and optional text-to-speech narration to minimize sensory overload.
              </p>
            </div>

            <div className="p-6 rounded-lg bg-slate-50 border border-slate-100 space-y-4">
              <Cpu className="w-6 h-6 text-slate-700" />
              <h3 className="text-lg font-bold text-slate-900">Scaffolded Support</h3>
              <p className="text-sm text-slate-600 leading-relaxed">
                Provides progressive hints, visual examples, and foundational reviews rather than simply grading answers right or wrong.
              </p>
            </div>
          </div>
        </div>
      </section>

      <Footer />
    </div>
  );
};

export default LandingPage;
