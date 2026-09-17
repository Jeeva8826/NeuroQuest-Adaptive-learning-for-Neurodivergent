import React, { useEffect, useState } from 'react';
import { Award, Star, Flame, CheckCircle, Sparkles, BookOpen } from 'lucide-react';
import { getProgressSummary } from '../services/api';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';
import AudioButton from '../components/common/AudioButton';

const ProgressPage = () => {
  const [progress, setProgress] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchProgress();
  }, []);

  const fetchProgress = async () => {
    try {
      const res = await getProgressSummary();
      setProgress(res.data);
    } catch (err) {
      console.error('Failed to load progress:', err);
    } finally {
      setLoading(false);
    }
  };

  const totalStars = progress?.total_stars || 10;
  const streakDays = progress?.streak_days || 1;
  const totalTasks = progress?.total_tasks_completed || 0;
  const mastery = progress?.subject_mastery || {};

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />

      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-200/80 pb-4">
          <div>
            <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight flex items-center gap-2">
              <Award className="w-8 h-8 text-amber-500" />
              Badges & Progress Mastery
            </h1>
            <p className="text-slate-500 text-sm mt-1">
              Celebrate every milestone, star earned, and subject mastered!
            </p>
          </div>
          <AudioButton
            text={`You have earned ${totalStars} stars and completed ${totalTasks} quest activities so far.`}
            label="Listen Stats"
          />
        </div>

        {/* Stats Row */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <div className="bg-white p-6 rounded-3xl border border-slate-200/80 shadow-md flex items-center gap-4">
            <div className="w-14 h-14 rounded-2xl bg-amber-400 text-amber-950 flex items-center justify-center font-extrabold shadow-md">
              <Star className="w-7 h-7 fill-current" />
            </div>
            <div>
              <div className="text-3xl font-black text-slate-900">{totalStars}</div>
              <div className="text-xs font-bold text-slate-500 uppercase tracking-wider">Total Quest Stars</div>
            </div>
          </div>

          <div className="bg-white p-6 rounded-3xl border border-slate-200/80 shadow-md flex items-center gap-4">
            <div className="w-14 h-14 rounded-2xl bg-rose-500 text-white flex items-center justify-center font-extrabold shadow-md">
              <Flame className="w-7 h-7 fill-current" />
            </div>
            <div>
              <div className="text-3xl font-black text-slate-900">{streakDays} Days</div>
              <div className="text-xs font-bold text-slate-500 uppercase tracking-wider">Daily Streak</div>
            </div>
          </div>

          <div className="bg-white p-6 rounded-3xl border border-slate-200/80 shadow-md flex items-center gap-4">
            <div className="w-14 h-14 rounded-2xl bg-emerald-500 text-white flex items-center justify-center font-extrabold shadow-md">
              <CheckCircle className="w-7 h-7" />
            </div>
            <div>
              <div className="text-3xl font-black text-slate-900">{totalTasks}</div>
              <div className="text-xs font-bold text-slate-500 uppercase tracking-wider">Activities Done</div>
            </div>
          </div>
        </div>

        {/* Subject Mastery Progress Bars */}
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/80 shadow-md space-y-6">
          <h2 className="text-xl font-extrabold text-slate-900">Subject Mastery Tracker</h2>
          <div className="space-y-4">
            {Object.entries(mastery).map(([sub, count]) => (
              <div key={sub} className="space-y-1.5">
                <div className="flex justify-between text-xs font-bold text-slate-700">
                  <span>{sub}</span>
                  <span>{count} Quests Solved</span>
                </div>
                <div className="w-full h-3 bg-slate-100 rounded-full overflow-hidden">
                  <div
                    className="h-full bg-indigo-600 rounded-full transition-all duration-500"
                    style={{ width: `${Math.min(count * 20, 100)}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Earned Badges Grid */}
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/80 shadow-md space-y-6">
          <h2 className="text-xl font-extrabold text-slate-900 flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-purple-600" />
            Learner Badge Collection
          </h2>

          <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
            {(progress?.earned_badges || []).map(badge => (
              <div
                key={badge.id}
                className={`p-5 rounded-3xl border text-center space-y-3 transition-all ${
                  badge.is_unlocked
                    ? 'bg-amber-50/80 border-amber-300 text-amber-950 shadow-md'
                    : 'bg-slate-50 border-slate-200 text-slate-400 opacity-60'
                }`}
              >
                <div className={`w-14 h-14 rounded-2xl mx-auto flex items-center justify-center font-extrabold shadow-md ${
                  badge.is_unlocked ? 'bg-amber-400 text-amber-950' : 'bg-slate-200 text-slate-400'
                }`}>
                  <Award className="w-7 h-7" />
                </div>
                <div>
                  <div className="text-sm font-black">{badge.title}</div>
                  <div className="text-xs text-slate-600 mt-1">{badge.description}</div>
                </div>
                <div className="pt-2">
                  <span className={`px-3 py-1 rounded-full text-[10px] font-extrabold uppercase tracking-wider ${
                    badge.is_unlocked ? 'bg-amber-200 text-amber-900' : 'bg-slate-200 text-slate-600'
                  }`}>
                    {badge.is_unlocked ? 'Unlocked' : 'Locked'}
                  </span>
                </div>
              </div>
            ))}
          </div>
        </div>

      </main>

      <Footer />
    </div>
  );
};

export default ProgressPage;
