import React, { useState, useEffect } from 'react';

const ConceptMatch = ({ difficulty = 'easy', conceptPairs = [] }) => {
  const [selectedTerm, setSelectedTerm] = useState(null);
  const [matchedPairs, setMatchedPairs] = useState([]);
  const [message, setMessage] = useState('');

  // Adapt based on difficulty
  const pairsToShow = difficulty === 'easy' ? conceptPairs.slice(0, 3) :
                      difficulty === 'medium' ? conceptPairs.slice(0, 5) :
                      conceptPairs;

  const [terms, setTerms] = useState([]);
  const [definitions, setDefinitions] = useState([]);

  useEffect(() => {
    // Shuffle separately
    setTerms([...pairsToShow].map(p => ({ id: p.id, text: p.term })).sort(() => Math.random() - 0.5));
    setDefinitions([...pairsToShow].map(p => ({ id: p.id, text: p.definition })).sort(() => Math.random() - 0.5));
  }, [difficulty, conceptPairs]);

  const handleTermClick = (id) => {
    if (matchedPairs.includes(id)) return;
    setSelectedTerm(id);
    setMessage('');
  };

  const handleDefinitionClick = (id) => {
    if (matchedPairs.includes(id)) return;
    
    if (selectedTerm === id) {
      setMatchedPairs([...matchedPairs, id]);
      setSelectedTerm(null);
      setMessage('Great match!');
    } else {
      setSelectedTerm(null);
      setMessage('Not quite, try again. Take your time.');
    }
  };

  const isComplete = matchedPairs.length === pairsToShow.length && pairsToShow.length > 0;

  return (
    <div className="p-4 bg-gray-50 rounded-xl max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center text-gray-800">Concept Match</h2>
      <p className="text-center text-gray-600 mb-6">Match the terms to their definitions. There's no rush.</p>
      
      {message && <p className="text-center mb-4 font-semibold text-indigo-600" aria-live="polite">{message}</p>}
      
      <div className="flex flex-col md:flex-row gap-8 justify-center">
        <div className="flex flex-col gap-3 w-full md:w-1/2">
          <h3 className="font-semibold text-lg text-gray-700">Terms</h3>
          {terms.map(term => {
            const isMatched = matchedPairs.includes(term.id);
            const isSelected = selectedTerm === term.id;
            return (
              <button
                key={term.id}
                onClick={() => handleTermClick(term.id)}
                disabled={isMatched}
                className={`p-3 rounded border text-left transition-colors ${
                  isMatched ? 'bg-green-100 border-green-300 text-gray-500 opacity-60' :
                  isSelected ? 'bg-indigo-100 border-indigo-500 shadow' :
                  'bg-white border-gray-200 hover:bg-gray-100'
                }`}
                aria-pressed={isSelected}
              >
                {term.text}
              </button>
            );
          })}
        </div>

        <div className="flex flex-col gap-3 w-full md:w-1/2">
          <h3 className="font-semibold text-lg text-gray-700">Definitions</h3>
          {definitions.map(def => {
            const isMatched = matchedPairs.includes(def.id);
            return (
              <button
                key={def.id}
                onClick={() => handleDefinitionClick(def.id)}
                disabled={isMatched || !selectedTerm}
                className={`p-3 rounded border text-left transition-colors ${
                  isMatched ? 'bg-green-100 border-green-300 text-gray-500 opacity-60' :
                  'bg-white border-gray-200 hover:bg-gray-100'
                }`}
              >
                {def.text}
              </button>
            );
          })}
        </div>
      </div>
      
      {isComplete && (
        <div className="mt-8 p-4 bg-green-50 border border-green-200 rounded-lg text-center">
          <h3 className="text-xl font-bold text-green-800">Wonderful!</h3>
          <p className="text-green-700">You've successfully matched all the concepts.</p>
        </div>
      )}
    </div>
  );
};

export default ConceptMatch;
