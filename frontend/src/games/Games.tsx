import React from 'react';
import { motion } from 'framer-motion';
import { useAppStore } from '../store/useAppStore';

// Simple Gamification Component for NeuroQuest
// Implements Concept Match and Mission Map without forced timers or punishment

export const ConceptMatch = ({ conceptData, difficulty }) => {
  return (
    <div className="p-6 bg-white rounded-xl shadow-sm border border-slate-200">
      <h3 className="text-xl font-bold text-slate-800 mb-4">Concept Match</h3>
      <p className="text-slate-600 mb-6">Match the concept to its meaning. Take your time!</p>
      
      <div className="grid grid-cols-2 gap-4">
        {/* Left Side: Concepts */}
        <div className="flex flex-col gap-3">
          <motion.div whileHover={{ scale: 1.02 }} className="p-3 bg-blue-50 border border-blue-200 rounded cursor-pointer text-center">
            Photosynthesis
          </motion.div>
          <motion.div whileHover={{ scale: 1.02 }} className="p-3 bg-blue-50 border border-blue-200 rounded cursor-pointer text-center">
            Chlorophyll
          </motion.div>
        </div>
        
        {/* Right Side: Meanings */}
        <div className="flex flex-col gap-3">
          {difficulty > 1 ? (
            <motion.div whileHover={{ scale: 1.02 }} className="p-3 bg-green-50 border border-green-200 rounded cursor-pointer text-center">
              The process by which plants make food using sunlight.
            </motion.div>
          ) : (
            <motion.div whileHover={{ scale: 1.02 }} className="p-3 bg-green-50 border border-green-200 rounded cursor-pointer text-center">
              Plants making food.
            </motion.div>
          )}
          <motion.div whileHover={{ scale: 1.02 }} className="p-3 bg-green-50 border border-green-200 rounded cursor-pointer text-center">
            Green pigment in leaves.
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export const MissionMap = () => {
  return (
    <div className="p-6 bg-slate-50 rounded-xl border border-slate-200 mt-6">
      <h3 className="text-lg font-bold text-slate-800 mb-4">Mission Map</h3>
      <div className="flex items-center justify-between">
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-green-500 text-white flex items-center justify-center font-bold">1</div>
          <span className="text-sm mt-2 text-slate-600">Water</span>
        </div>
        <div className="h-1 flex-1 bg-green-500 mx-2"></div>
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-blue-500 text-white flex items-center justify-center font-bold">2</div>
          <span className="text-sm mt-2 text-slate-600">Sunlight</span>
        </div>
        <div className="h-1 flex-1 bg-slate-300 mx-2"></div>
        <div className="flex flex-col items-center">
          <div className="w-12 h-12 rounded-full bg-slate-200 text-slate-400 flex items-center justify-center font-bold">3</div>
          <span className="text-sm mt-2 text-slate-400">Food</span>
        </div>
      </div>
    </div>
  );
};

export default function GamesContainer() {
  const { masteryPoints } = useAppStore();
  const difficulty = masteryPoints > 60 ? 2 : 1;

  
  return (
    <div className="max-w-3xl mx-auto py-8">
      <h2 className="text-2xl font-bold text-slate-800 mb-6">Focus Quest 🎮</h2>
      <ConceptMatch conceptData={{}} difficulty={difficulty} />
      <MissionMap />
    </div>
  );
}
