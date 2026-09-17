import React, { useState } from 'react';

const BossQuestion = ({ 
  difficulty = 'easy', 
  question = "What is the core concept we learned today?", 
  options = [], 
  hints = [] 
}) => {
  const [selectedOption, setSelectedOption] = useState(null);
  const [showHint, setShowHint] = useState(difficulty === 'easy');
  const [hintIndex, setHintIndex] = useState(0);
  const [isCorrect, setIsCorrect] = useState(null);

  const handleSelect = (option) => {
    setSelectedOption(option.id);
    if (option.isCorrect) {
      setIsCorrect(true);
    } else {
      setIsCorrect(false);
    }
  };

  const handleNextHint = () => {
    if (hintIndex < hints.length - 1) {
      setHintIndex(hintIndex + 1);
    }
  };

  const revealHintManual = () => {
    setShowHint(true);
  };

  return (
    <div className="p-6 bg-orange-50 rounded-xl max-w-3xl mx-auto shadow-sm">
      <h2 className="text-2xl font-bold mb-2 text-center text-orange-900">Final Challenge</h2>
      <p className="text-center text-orange-700 mb-8 opacity-80">Take your time. You know this.</p>

      <div className="bg-white p-6 rounded-lg shadow-inner mb-6 border border-orange-100">
        <h3 className="text-xl font-medium text-gray-800 text-center">{question}</h3>
      </div>

      {hints.length > 0 && (
        <div className="mb-6 flex flex-col items-center">
          {!showHint ? (
            <button 
              onClick={revealHintManual}
              className="text-orange-600 hover:text-orange-800 underline text-sm transition-colors"
            >
              Need a hint?
            </button>
          ) : (
            <div className="bg-yellow-50 border border-yellow-200 p-4 rounded-lg w-full max-w-md">
              <p className="text-yellow-800 text-sm mb-2 font-medium">Hint {hintIndex + 1}:</p>
              <p className="text-yellow-900 italic">{hints[hintIndex]}</p>
              {hintIndex < hints.length - 1 && (
                <button 
                  onClick={handleNextHint}
                  className="mt-2 text-xs bg-yellow-200 text-yellow-800 px-3 py-1 rounded hover:bg-yellow-300 transition-colors"
                >
                  Show another hint
                </button>
              )}
            </div>
          )}
        </div>
      )}

      <div className="space-y-3">
        {options.map((option) => {
          let btnClass = "w-full p-4 text-left rounded-lg border-2 transition-all ";
          
          if (selectedOption === option.id) {
            btnClass += option.isCorrect 
              ? "bg-green-100 border-green-500 text-green-900" 
              : "bg-red-50 border-red-300 text-red-900";
          } else {
            btnClass += "bg-white border-orange-200 hover:border-orange-400 hover:bg-orange-100/50 text-gray-700";
          }

          return (
            <button
              key={option.id}
              onClick={() => handleSelect(option)}
              disabled={isCorrect}
              className={btnClass}
            >
              {option.text}
            </button>
          );
        })}
      </div>

      {isCorrect === true && (
        <div className="mt-8 p-4 bg-green-50 rounded-lg text-center animate-fade-in">
          <p className="text-xl font-bold text-green-800 mb-2">Incredible!</p>
          <p className="text-green-700">You've mastered this concept.</p>
        </div>
      )}

      {isCorrect === false && (
        <div className="mt-4 text-center">
          <p className="text-red-500 font-medium">Not quite right. Take a deep breath and try another option.</p>
        </div>
      )}
    </div>
  );
};

export default BossQuestion;
