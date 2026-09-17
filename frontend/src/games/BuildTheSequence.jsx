import React, { useState } from 'react';

const BuildTheSequence = ({ difficulty = 'easy', sequenceSteps = [] }) => {
  // sequenceSteps: [{ id: 1, text: 'First step', order: 1 }]
  const [currentSequence, setCurrentSequence] = useState([]);
  const [availableSteps, setAvailableSteps] = useState([]);
  const [message, setMessage] = useState('');

  // Initialize randomly
  React.useEffect(() => {
    // Difficulty adaptation: easy = fewer steps or visual cues. We'll just limit or simplify.
    let stepsToUse = [...sequenceSteps];
    if (difficulty === 'easy') {
      stepsToUse = stepsToUse.slice(0, Math.min(3, stepsToUse.length));
    }
    setAvailableSteps(stepsToUse.sort(() => Math.random() - 0.5));
    setCurrentSequence([]);
    setMessage('');
  }, [difficulty, sequenceSteps]);

  const handleSelectStep = (step) => {
    // If the step is the correct next step in the sequence
    const expectedOrder = currentSequence.length + 1;
    
    if (step.order === expectedOrder) {
      setCurrentSequence([...currentSequence, step]);
      setAvailableSteps(availableSteps.filter(s => s.id !== step.id));
      setMessage('Good job, that is the next step.');
    } else {
      // Gentle feedback
      setMessage('That step might belong somewhere else. Take a breath and try another one.');
    }
  };

  const handleRemoveStep = (step) => {
    // Allow undo without penalty
    const index = currentSequence.findIndex(s => s.id === step.id);
    if (index === currentSequence.length - 1) { // only remove the last one added
      const newSequence = currentSequence.slice(0, -1);
      setCurrentSequence(newSequence);
      setAvailableSteps([...availableSteps, step]);
      setMessage('');
    }
  };

  const isComplete = availableSteps.length === 0 && currentSequence.length > 0;

  return (
    <div className="p-4 bg-blue-50 rounded-xl max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center text-blue-900">Build the Sequence</h2>
      <p className="text-center text-blue-700 mb-6">Select the steps in the correct order. You can undo if you change your mind.</p>
      
      {message && <p className="text-center mb-4 font-medium text-blue-800" aria-live="polite">{message}</p>}
      
      <div className="mb-8">
        <h3 className="font-semibold text-lg text-blue-800 mb-3">Your Sequence</h3>
        <div className="flex flex-col gap-2 min-h-[100px] p-4 bg-white rounded-lg border-2 border-dashed border-blue-200">
          {currentSequence.length === 0 && <span className="text-gray-400 italic">Select a step below to start...</span>}
          {currentSequence.map((step, index) => (
            <div 
              key={step.id} 
              onClick={() => handleRemoveStep(step)}
              className="p-3 bg-blue-100 border border-blue-300 rounded cursor-pointer hover:bg-blue-200 transition-colors flex gap-3"
            >
              <span className="font-bold text-blue-800">{index + 1}.</span>
              <span>{step.text}</span>
            </div>
          ))}
        </div>
      </div>

      {!isComplete && (
        <div>
          <h3 className="font-semibold text-lg text-blue-800 mb-3">Available Steps</h3>
          <div className="flex flex-wrap gap-3">
            {availableSteps.map(step => (
              <button
                key={step.id}
                onClick={() => handleSelectStep(step)}
                className="p-3 bg-white border border-gray-300 rounded shadow-sm hover:bg-gray-50 transition-colors text-left flex-1 min-w-[200px]"
              >
                {step.text}
              </button>
            ))}
          </div>
        </div>
      )}

      {isComplete && (
        <div className="mt-8 p-4 bg-green-50 border border-green-200 rounded-lg text-center">
          <h3 className="text-xl font-bold text-green-800">Excellent!</h3>
          <p className="text-green-700">You've built the sequence perfectly.</p>
        </div>
      )}
    </div>
  );
};

export default BuildTheSequence;
