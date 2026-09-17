import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { Stethoscope, ArrowRight, ArrowLeft, CheckCircle } from 'lucide-react';
import { getMedicalQuestions, submitMedicalProfile, getCurrentUser } from '../services/api';
import { useAuth } from '../context/AuthContext';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';

const MedicalOnboardingPage = () => {
  const { user, completeMedicalOnboarding } = useAuth();
  const navigate = useNavigate();
  
  const [questions, setQuestions] = useState([]);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState('');
  
  const [currentPage, setCurrentPage] = useState(0);
  const questionsPerPage = 5;

  useEffect(() => {
    const fetchQuestions = async () => {
      try {
        if (!user || !user.learner_id) {
            // Need user object to be fully loaded
            const meRes = await getCurrentUser();
            if(!meRes.data.learner_id) {
                setError("Learner profile not found. Please contact support.");
                setLoading(false);
                return;
            }
            const res = await getMedicalQuestions(meRes.data.learner_id);
            setQuestions(res.data);
        } else {
            const res = await getMedicalQuestions(user.learner_id);
            setQuestions(res.data);
        }
      } catch (err) {
        console.error("Failed to load medical questions:", err);
        setError("Failed to load medical questions. Please ensure the backend is running.");
      } finally {
        setLoading(false);
      }
    };
    
    fetchQuestions();
  }, [user]);

  const handleAnswer = (qId, qText, val) => {
    setAnswers(prev => ({
      ...prev,
      [qId]: {
        question_id: qId,
        question_text: qText,
        answer: val
      }
    }));
  };

  const totalPages = Math.ceil(questions.length / questionsPerPage);
  
  const canGoNext = () => {
    const currentQStartIndex = currentPage * questionsPerPage;
    const currentQEndIndex = Math.min(currentQStartIndex + questionsPerPage, questions.length);
    for (let i = currentQStartIndex; i < currentQEndIndex; i++) {
      if (!answers[questions[i].id]) return false;
    }
    return true;
  };

  const handleNext = () => {
    if (currentPage < totalPages - 1) {
      setCurrentPage(prev => prev + 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const handlePrev = () => {
    if (currentPage > 0) {
      setCurrentPage(prev => prev - 1);
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }
  };

  const handleSubmit = async () => {
    if (!canGoNext()) return;
    setSubmitting(true);
    setError('');

    try {
      const payload = {
        learner_id: user?.learner_id || '',
        condition: 'Medical Assessment', // Real condition is fetched on backend or stored previously
        answers: Object.values(answers)
      };
      await submitMedicalProfile(payload);
      completeMedicalOnboarding();
      navigate('/onboarding');
    } catch (err) {
      console.error(err);
      setError('Failed to submit medical profile.');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }

  const currentQuestions = questions.slice(
    currentPage * questionsPerPage,
    (currentPage + 1) * questionsPerPage
  );

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />

      <main className="flex-1 py-8 px-4 sm:px-6 max-w-4xl mx-auto w-full space-y-6">
        
        <div className="bg-white rounded-3xl p-8 border border-slate-200/80 shadow-sm text-center">
          <div className="w-16 h-16 rounded-2xl bg-indigo-100 text-indigo-600 mx-auto flex items-center justify-center mb-4">
            <Stethoscope className="w-8 h-8" />
          </div>
          <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight">Clinical Medical Assessment</h1>
          <p className="mt-2 text-slate-500 max-w-2xl mx-auto text-sm leading-relaxed">
            Please answer the following {questions.length} questions based on the child's medical records and your observations. 
            This highly specific medical data allows NeuroQuest to adapt its Cognitive Scaffold ML models accurately. 
            Your responses are stored securely.
          </p>
        </div>

        {error && (
          <div className="bg-rose-50 text-rose-700 p-4 rounded-2xl text-sm font-bold border border-rose-200 text-center">
            {error}
          </div>
        )}

        <div className="bg-white rounded-3xl p-6 sm:p-10 border border-slate-200/80 shadow-xl space-y-8 relative overflow-hidden">
          
          {/* Progress Bar */}
          <div className="w-full bg-slate-100 rounded-full h-2.5 mb-8 overflow-hidden">
            <div 
              className="bg-indigo-600 h-2.5 rounded-full transition-all duration-500 ease-out"
              style={{ width: `${((currentPage + 1) / totalPages) * 100}%` }}
            ></div>
          </div>

          <div className="space-y-8">
            {currentQuestions.map((q, idx) => (
              <div key={q.id} className="space-y-4">
                <p className="font-bold text-slate-800 text-lg">
                  {currentPage * questionsPerPage + idx + 1}. {q.text}
                </p>
                <div className="flex flex-wrap gap-2">
                  {q.options.map(opt => (
                    <button
                      key={opt}
                      onClick={() => handleAnswer(q.id, q.text, opt)}
                      className={`px-4 py-2 rounded-xl text-sm font-bold border transition-all
                        ${answers[q.id]?.answer === opt 
                          ? 'bg-indigo-600 border-indigo-600 text-white shadow-md' 
                          : 'bg-white border-slate-200 text-slate-600 hover:border-indigo-300 hover:bg-indigo-50'
                        }`}
                    >
                      {opt}
                    </button>
                  ))}
                </div>
              </div>
            ))}
          </div>

          <div className="flex items-center justify-between pt-8 mt-8 border-t border-slate-100">
            <button
              onClick={handlePrev}
              disabled={currentPage === 0}
              className={`flex items-center gap-2 px-6 py-3 rounded-2xl text-sm font-bold transition-all
                ${currentPage === 0 ? 'opacity-50 cursor-not-allowed text-slate-400 bg-slate-50' : 'text-slate-700 bg-slate-100 hover:bg-slate-200'}`}
            >
              <ArrowLeft className="w-4 h-4" /> Back
            </button>
            
            {currentPage < totalPages - 1 ? (
              <button
                onClick={handleNext}
                disabled={!canGoNext()}
                className={`flex items-center gap-2 px-8 py-3 rounded-2xl text-sm font-bold transition-all
                  ${!canGoNext() ? 'opacity-50 cursor-not-allowed bg-indigo-300 text-white' : 'bg-indigo-600 text-white hover:bg-indigo-700 shadow-md hover:shadow-lg'}`}
              >
                Next <ArrowRight className="w-4 h-4" />
              </button>
            ) : (
              <button
                onClick={handleSubmit}
                disabled={!canGoNext() || submitting}
                className={`flex items-center gap-2 px-8 py-3 rounded-2xl text-sm font-bold transition-all
                  ${(!canGoNext() || submitting) ? 'opacity-50 cursor-not-allowed bg-green-400 text-white' : 'bg-emerald-500 text-white hover:bg-emerald-600 shadow-md hover:shadow-lg'}`}
              >
                {submitting ? 'Submitting...' : 'Complete Assessment'} <CheckCircle className="w-4 h-4" />
              </button>
            )}
          </div>

        </div>
      </main>

      <Footer />
    </div>
  );
};

export default MedicalOnboardingPage;
