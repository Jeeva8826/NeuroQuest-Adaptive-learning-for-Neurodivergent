import React from 'react';
import { Settings, RefreshCw } from 'lucide-react';
import { useNavigate } from 'react-router-dom';
import PreferenceCustomizer from '../components/profile/PreferenceCustomizer';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';

const SettingsPage = () => {
  const navigate = useNavigate();

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />

      <main className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">
        
        <div className="flex items-center justify-between border-b border-slate-200/80 pb-4">
          <div>
            <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
              <Settings className="w-8 h-8 text-indigo-600" />
              Settings & Preferences
            </h1>
            <p className="text-slate-500 text-sm mt-1">
              Customize UI appearance, contrast, dyslexic font options, and audio narration.
            </p>
          </div>

          <button
            onClick={() => navigate('/onboarding')}
            className="px-4 py-2 bg-indigo-50 border border-indigo-200 text-indigo-700 hover:bg-indigo-100 text-xs font-bold rounded-2xl transition-all flex items-center gap-1.5"
          >
            <RefreshCw className="w-4 h-4" />
            <span>Retake Caregiver Questionnaire</span>
          </button>
        </div>

        {/* Live Theme Customizer */}
        <PreferenceCustomizer />

      </main>

      <Footer />
    </div>
  );
};

export default SettingsPage;
