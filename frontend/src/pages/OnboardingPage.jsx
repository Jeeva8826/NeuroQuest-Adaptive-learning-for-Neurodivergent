import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import QuestionnaireWizard from '../components/onboarding/QuestionnaireWizard';
import { submitQuestionnaire } from '../services/api';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';

const OnboardingPage = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  
  const { completeOnboarding } = useAuth();
  const { reloadTheme } = useTheme();
  const navigate = useNavigate();

  const handleQuestionnaireSubmit = async (formData) => {
    setLoading(true);
    setError('');

    try {
      await submitQuestionnaire(formData);
      completeOnboarding();
      await reloadTheme();
      // Instantly navigate to personalized Learner Home
      navigate('/home');
    } catch (err) {
      console.error(err);
      setError('Failed to save profile. Please ensure backend is running.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />

      <main className="flex-1 py-8 px-4 sm:px-6 max-w-7xl mx-auto w-full space-y-6">
        {error && (
          <div className="max-w-3xl mx-auto bg-rose-50 text-rose-800 p-4 rounded-2xl border border-rose-300 text-sm font-bold text-center">
            {error}
          </div>
        )}

        <QuestionnaireWizard onSubmit={handleQuestionnaireSubmit} loading={loading} />
      </main>

      <Footer />
    </div>
  );
};

export default OnboardingPage;
