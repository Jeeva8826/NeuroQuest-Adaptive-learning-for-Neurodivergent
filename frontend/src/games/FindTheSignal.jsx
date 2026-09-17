import React, { useState, useEffect } from 'react';

const FindTheSignal = ({ difficulty = 'easy', target = { id: 'target', label: 'Signal' }, noise = [] }) => {
  const [items, setItems] = useState([]);
  const [found, setFound] = useState(false);
  const [message, setMessage] = useState('');

  useEffect(() => {
    // Difficulty adaptation: grid size
    const noiseCount = difficulty === 'easy' ? 3 :
                       difficulty === 'medium' ? 8 :
                       15;
    
    // Pick distractors
    const selectedNoise = noise.slice(0, noiseCount);
    
    const allItems = [target, ...selectedNoise].sort(() => Math.random() - 0.5);
    setItems(allItems);
    setFound(false);
    setMessage('');
  }, [difficulty, target, noise]);

  const handleItemClick = (item) => {
    if (item.id === target.id) {
      setFound(true);
      setMessage('You found it! Great focus.');
    } else {
      setMessage('Not quite. Keep looking, you can do it.');
    }
  };

  return (
    <div className="p-4 bg-purple-50 rounded-xl max-w-4xl mx-auto">
      <h2 className="text-2xl font-bold mb-4 text-center text-purple-900">Find the Signal</h2>
      <p className="text-center text-purple-700 mb-6">Can you find: <strong>{target.label}</strong>?</p>
      
      {message && <p className="text-center mb-4 font-medium text-purple-800" aria-live="polite">{message}</p>}
      
      {!found ? (
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {items.map((item, i) => (
            <button
              key={`${item.id}-${i}`}
              onClick={() => handleItemClick(item)}
              className="aspect-square p-4 bg-white border-2 border-purple-200 rounded-lg shadow-sm hover:border-purple-400 hover:bg-purple-50 transition-all flex items-center justify-center text-center font-medium text-gray-700"
            >
              {/* If items have icons or images, they'd go here. Using labels for now. */}
              {item.label || 'Noise'}
            </button>
          ))}
        </div>
      ) : (
        <div className="mt-8 p-8 bg-purple-100 border border-purple-300 rounded-lg text-center">
          <div className="w-24 h-24 bg-white rounded-full mx-auto flex items-center justify-center text-4xl mb-4 border-4 border-purple-400">
            ⭐
          </div>
          <h3 className="text-2xl font-bold text-purple-900 mb-2">Signal Detected</h3>
          <p className="text-purple-800">You successfully tuned out the noise.</p>
        </div>
      )}
    </div>
  );
};

export default FindTheSignal;
