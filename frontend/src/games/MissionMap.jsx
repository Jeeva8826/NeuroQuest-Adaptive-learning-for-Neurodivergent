import React from 'react';

const MissionMap = ({ difficulty = 'easy', currentNodeId, nodes = [] }) => {
  // Difficulty adaptation could involve hiding future node details if 'hard'
  // Or showing a simplified straight line for 'easy'

  const getStatusColor = (status) => {
    switch (status) {
      case 'completed': return 'bg-green-500 border-green-600';
      case 'current': return 'bg-yellow-400 border-yellow-500 ring-4 ring-yellow-200 shadow-sm';
      case 'locked': return 'bg-gray-300 border-gray-400';
      default: return 'bg-gray-300 border-gray-400';
    }
  };

  return (
    <div className="p-6 bg-slate-50 rounded-xl max-w-4xl mx-auto overflow-hidden">
      <h2 className="text-2xl font-bold mb-8 text-center text-slate-800">Mission Map</h2>
      
      <div className="relative flex flex-col md:flex-row items-center justify-between min-h-[200px] px-8">
        {/* Connecting Line */}
        <div className="absolute top-1/2 left-8 right-8 h-2 bg-gray-200 -z-10 -translate-y-1/2 hidden md:block rounded-full"></div>
        <div className="absolute left-1/2 top-8 bottom-8 w-2 bg-gray-200 -z-10 -translate-x-1/2 md:hidden rounded-full"></div>

        {nodes.map((node, index) => {
          const isHard = difficulty === 'hard';
          const isLocked = node.status === 'locked';
          const hideDetails = isHard && isLocked;

          return (
            <div key={node.id} className="relative flex flex-col items-center group my-4 md:my-0">
              <div className={`w-16 h-16 rounded-full border-4 flex items-center justify-center text-xl font-bold shadow-md transition-transform transform group-hover:scale-105 z-10 ${getStatusColor(node.status)}`}>
                {node.status === 'completed' ? '✓' : (index + 1)}
              </div>
              
              <div className="mt-4 text-center bg-white p-2 rounded shadow-sm border border-slate-100 min-w-[120px]">
                <h4 className="font-semibold text-slate-700">
                  {hideDetails ? '???' : node.title}
                </h4>
                {!hideDetails && node.description && (
                  <p className="text-xs text-slate-500 mt-1">{node.description}</p>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default MissionMap;
