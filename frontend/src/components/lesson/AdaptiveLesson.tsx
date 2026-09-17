import React, { useState } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { CheckCircle2, ChevronRight, Activity } from 'lucide-react';
import { useAppStore } from '../../store/useAppStore';

const CONCEPTS = [
  { id: 1, title: 'What is a Planet?', content: 'A planet is a large round object in space that travels around a star.' },
  { id: 2, title: 'Our Star: The Sun', content: 'The Sun is a star at the center of our solar system. All planets travel around it.' },
  { id: 3, title: 'Rocky vs Gas Planets', content: 'Some planets are made of rock (like Earth), and others are made of gas (like Jupiter).' },
];

export const AdaptiveLesson: React.FC = () => {
  const [currentIndex, setCurrentIndex] = useState(0);
  const [showLoadCheck, setShowLoadCheck] = useState(false);
  const { addMasteryPoints } = useAppStore();

  const handleNext = () => {
    if (showLoadCheck) return;
    
    // Every concept triggers a load check
    setShowLoadCheck(true);
  };

  const handleLoadFeedback = (feedback: string) => {
    setShowLoadCheck(false);
    
    // Add points for engagement
    addMasteryPoints(10);
    
    if (currentIndex < CONCEPTS.length - 1) {
      setCurrentIndex(prev => prev + 1);
    } else {
      // Finished lesson
      alert('Lesson Complete! Great job!');
    }
    
    // In a real app, 'feedback' would adjust the difficulty or volume of the next concept
  };

  const progress = Math.round((currentIndex / CONCEPTS.length) * 100);
  const currentConcept = CONCEPTS[currentIndex];

  return (
    <div className="max-w-2xl mx-auto p-6 min-h-[80vh] flex flex-col">
      <header className="mb-8">
        <div className="flex justify-between items-center mb-4">
          <h1 className="text-xl font-bold text-slate-500 uppercase tracking-wider text-sm">Solar System Basics</h1>
          <div className="text-slate-500 font-medium text-sm">Concept {currentIndex + 1} of {CONCEPTS.length}</div>
        </div>
        <div className="w-full bg-slate-200 rounded-full h-2">
          <div 
            className="bg-green-500 h-2 rounded-full transition-all duration-500" 
            style={{ width: `${progress}%` }}
            role="progressbar" 
          />
        </div>
      </header>

      <main className="flex-1 flex flex-col justify-center relative">
        <AnimatePresence mode="wait">
          {!showLoadCheck ? (
            <motion.div
              key={`concept-${currentConcept.id}`}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
              className="bg-white rounded-3xl p-8 sm:p-12 shadow-sm border border-slate-200 text-center"
            >
              <h2 className="text-3xl font-bold text-slate-800 mb-6">{currentConcept.title}</h2>
              <p className="text-xl text-slate-600 leading-relaxed max-w-lg mx-auto">
                {currentConcept.content}
              </p>
              
              <div className="mt-12">
                <button
                  onClick={handleNext}
                  className="bg-indigo-600 hover:bg-indigo-700 text-white font-medium py-4 px-8 rounded-2xl transition-colors focus:ring-4 focus:ring-indigo-200 flex items-center justify-center gap-2 w-full sm:w-auto mx-auto text-lg shadow-sm"
                >
                  I Understand <ChevronRight className="w-5 h-5" />
                </button>
              </div>
            </motion.div>
          ) : (
            <motion.div
              key="load-check"
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.95 }}
              transition={{ duration: 0.3 }}
              className="bg-indigo-50 rounded-3xl p-8 sm:p-12 shadow-sm border border-indigo-100 text-center"
            >
              <div className="flex justify-center mb-6">
                <div className="p-4 bg-indigo-100 text-indigo-600 rounded-full">
                  <Activity className="w-8 h-8" />
                </div>
              </div>
              <h2 className="text-2xl font-bold text-indigo-900 mb-2">Cognitive Load Check</h2>
              <p className="text-indigo-700 mb-8 text-lg">How did that last concept feel?</p>
              
              <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 max-w-lg mx-auto">
                {[
                  { label: 'Too Easy', color: 'bg-emerald-100 text-emerald-800 hover:bg-emerald-200 ring-emerald-300' },
                  { label: 'Just Right', color: 'bg-blue-100 text-blue-800 hover:bg-blue-200 ring-blue-300' },
                  { label: 'A Little Much', color: 'bg-amber-100 text-amber-800 hover:bg-amber-200 ring-amber-300' },
                  { label: 'Too Much', color: 'bg-rose-100 text-rose-800 hover:bg-rose-200 ring-rose-300' },
                ].map((option) => (
                  <button
                    key={option.label}
                    onClick={() => handleLoadFeedback(option.label)}
                    className={`py-4 px-6 rounded-2xl font-medium text-lg transition-colors focus:outline-none focus:ring-4 ${option.color}`}
                  >
                    {option.label}
                  </button>
                ))}
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </main>
    </div>
  );
};
