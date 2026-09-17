import React, { useEffect, useState } from 'react';
import { motion } from 'framer-motion';

export const LearnerDashboard = () => {
  return (
    <div className="max-w-4xl mx-auto p-6 space-y-8">
      <header className="border-b border-slate-200 pb-6">
        <h1 className="text-3xl font-bold text-slate-800">Your Learning Hub</h1>
        <p className="text-slate-500 mt-2">Welcome back! Choose a subject to continue.</p>
      </header>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Course Card 1 */}
        <motion.div whileHover={{ y: -4 }} className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
          <div className="flex justify-between items-start mb-4">
            <div>
              <span className="text-xs font-semibold uppercase tracking-wider text-emerald-600 bg-emerald-50 px-2 py-1 rounded">Science</span>
              <h3 className="text-xl font-bold text-slate-800 mt-2">Nutrition in Plants</h3>
            </div>
            <div className="text-right">
              <span className="block text-2xl font-bold text-slate-800">61%</span>
              <span className="text-xs text-slate-500">Mastery</span>
            </div>
          </div>
          
          <div className="w-full bg-slate-100 rounded-full h-2 mb-4">
            <div className="bg-emerald-500 h-2 rounded-full" style={{ width: '61%' }}></div>
          </div>
          
          <button className="w-full py-2 bg-slate-800 text-white rounded-lg font-medium hover:bg-slate-700 transition-colors">
            Continue Lesson
          </button>
        </motion.div>

        {/* Course Card 2 */}
        <motion.div whileHover={{ y: -4 }} className="bg-white p-6 rounded-xl border border-slate-200 shadow-sm hover:shadow-md transition-shadow">
          <div className="flex justify-between items-start mb-4">
            <div>
              <span className="text-xs font-semibold uppercase tracking-wider text-blue-600 bg-blue-50 px-2 py-1 rounded">Mathematics</span>
              <h3 className="text-xl font-bold text-slate-800 mt-2">Integers</h3>
            </div>
            <div className="text-right">
              <span className="block text-2xl font-bold text-slate-800">42%</span>
              <span className="text-xs text-slate-500">Mastery</span>
            </div>
          </div>
          
          <div className="w-full bg-slate-100 rounded-full h-2 mb-4">
            <div className="bg-blue-500 h-2 rounded-full" style={{ width: '42%' }}></div>
          </div>
          
          <button className="w-full py-2 bg-slate-100 text-slate-700 rounded-lg font-medium hover:bg-slate-200 transition-colors">
            Start Lesson
          </button>
        </motion.div>
      </div>
    </div>
  );
};

export const CaregiverDashboard = () => {
  return (
    <div className="max-w-5xl mx-auto p-6 space-y-8">
      <header className="border-b border-slate-200 pb-6">
        <h1 className="text-3xl font-bold text-slate-800">Learner Support Overview</h1>
        <p className="text-slate-500 mt-2">Insights into how the learning environment is adapting today.</p>
      </header>

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        
        {/* Support Preferences Panel */}
        <div className="lg:col-span-1 bg-slate-50 p-6 rounded-xl border border-slate-200">
          <h3 className="font-bold text-slate-800 mb-4">Current Settings</h3>
          <ul className="space-y-4">
            <li className="flex justify-between items-center border-b border-slate-200 pb-2">
              <span className="text-slate-600 text-sm">Visuals</span>
              <span className="font-medium text-slate-800 text-sm bg-white px-2 py-1 rounded border border-slate-200">High</span>
            </li>
            <li className="flex justify-between items-center border-b border-slate-200 pb-2">
              <span className="text-slate-600 text-sm">Pacing</span>
              <span className="font-medium text-slate-800 text-sm bg-white px-2 py-1 rounded border border-slate-200">Slowed</span>
            </li>
            <li className="flex justify-between items-center border-b border-slate-200 pb-2">
              <span className="text-slate-600 text-sm">Density</span>
              <span className="font-medium text-slate-800 text-sm bg-white px-2 py-1 rounded border border-slate-200">Chunked</span>
            </li>
          </ul>
          
          <button className="mt-6 w-full py-2 text-sm text-indigo-600 font-medium hover:bg-indigo-50 rounded-lg transition-colors border border-indigo-200">
            Edit Preferences
          </button>
        </div>

        {/* Efficacy Analytics */}
        <div className="lg:col-span-2 bg-white p-6 rounded-xl border border-slate-200 shadow-sm">
          <h3 className="font-bold text-slate-800 mb-4">Adaptation Efficacy</h3>
          
          <div className="grid grid-cols-2 gap-4 mb-6">
            <div className="p-4 bg-slate-50 rounded-lg border border-slate-100">
              <span className="block text-sm text-slate-500 mb-1">Load Reports (Today)</span>
              <span className="text-2xl font-bold text-slate-800">2</span>
              <span className="ml-2 text-xs text-emerald-600 font-medium">Both successfully resolved</span>
            </div>
            
            <div className="p-4 bg-slate-50 rounded-lg border border-slate-100">
              <span className="block text-sm text-slate-500 mb-1">Most Effective Scaffold</span>
              <span className="text-lg font-bold text-slate-800">Visual Chunking</span>
            </div>
          </div>
          
          <div className="space-y-3">
            <h4 className="text-sm font-semibold text-slate-700 uppercase tracking-wide">Recent Adjustments</h4>
            <div className="flex items-start gap-3 p-3 bg-white border border-slate-100 rounded-lg shadow-sm">
              <div className="w-2 h-2 mt-2 rounded-full bg-emerald-500"></div>
              <div>
                <p className="text-sm font-medium text-slate-800">Text density reduced</p>
                <p className="text-xs text-slate-500">Triggered during Science module at 10:42 AM.</p>
              </div>
            </div>
            <div className="flex items-start gap-3 p-3 bg-white border border-slate-100 rounded-lg shadow-sm">
              <div className="w-2 h-2 mt-2 rounded-full bg-emerald-500"></div>
              <div>
                <p className="text-sm font-medium text-slate-800">Visual hint provided</p>
                <p className="text-xs text-slate-500">Triggered during Math module at 09:15 AM.</p>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>
  );
};

export const EducatorDashboard = () => {
  return (
    <div className="max-w-6xl mx-auto p-6 space-y-8">
      <header className="border-b border-slate-200 pb-6 flex justify-between items-end">
        <div>
          <h1 className="text-3xl font-bold text-slate-800">Class Learning Map</h1>
          <p className="text-slate-500 mt-2">Aggregate view of class mastery and adaptation trends.</p>
        </div>
        <button className="px-4 py-2 bg-slate-800 text-white rounded-lg text-sm font-medium hover:bg-slate-700">
          Export Report
        </button>
      </header>
      
      <div className="bg-white border border-slate-200 rounded-xl overflow-hidden shadow-sm">
        <table className="w-full text-left border-collapse">
          <thead>
            <tr className="bg-slate-50 border-b border-slate-200">
              <th className="p-4 text-sm font-semibold text-slate-600">Concept</th>
              <th className="p-4 text-sm font-semibold text-slate-600">Avg Mastery</th>
              <th className="p-4 text-sm font-semibold text-slate-600">Common Difficulty</th>
              <th className="p-4 text-sm font-semibold text-slate-600">Effective Scaffold</th>
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            <tr className="hover:bg-slate-50 transition-colors">
              <td className="p-4 text-sm font-medium text-slate-800">Nutrition in Plants</td>
              <td className="p-4 text-sm"><span className="text-emerald-600 font-bold">82%</span></td>
              <td className="p-4 text-sm text-slate-600">Multi-step sequences</td>
              <td className="p-4 text-sm text-slate-600">Visual workflows</td>
            </tr>
            <tr className="hover:bg-slate-50 transition-colors">
              <td className="p-4 text-sm font-medium text-slate-800">Heat</td>
              <td className="p-4 text-sm"><span className="text-amber-600 font-bold">71%</span></td>
              <td className="p-4 text-sm text-slate-600">Abstract definitions</td>
              <td className="p-4 text-sm text-slate-600">Real-world examples</td>
            </tr>
            <tr className="hover:bg-slate-50 transition-colors">
              <td className="p-4 text-sm font-medium text-slate-800">Acids & Bases</td>
              <td className="p-4 text-sm"><span className="text-rose-600 font-bold">63%</span></td>
              <td className="p-4 text-sm text-slate-600">Categorization rules</td>
              <td className="p-4 text-sm text-slate-600">Concept sorting games</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};
