import React, { useEffect, useState } from 'react';
import { 
  ShieldCheck, Heart, Clock, Award, CheckCircle, Sparkles, TrendingUp, BookOpen, User, RefreshCw
} from 'lucide-react';
import { getCaregiverInsights } from '../services/api';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';
import AudioButton from '../components/common/AudioButton';

const CaregiverDashboardPage = () => {
  const [insights, setInsights] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchInsights();
  }, []);

  const fetchInsights = async () => {
    try {
      const res = await getCaregiverInsights();
      setInsights(res.data);
    } catch (err) {
      console.error('Failed to fetch caregiver insights:', err);
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex flex-col bg-slate-50">
        <Navbar />
        <div className="flex-1 flex items-center justify-center">
          <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin" />
        </div>
        <Footer />
      </div>
    );
  }

  const learnerName = insights?.learner_name || 'Learner';
  const engagement = insights?.engagement_distribution || {};

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      <Navbar />

      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-slate-200/80 pb-4">
          <div>
            <div className="flex items-center gap-2">
              <span className="px-3 py-1 bg-emerald-100 text-emerald-800 rounded-full text-xs font-extrabold uppercase tracking-wider flex items-center gap-1">
                <ShieldCheck className="w-4 h-4 text-emerald-600" /> Non-Medical Privacy Safe
              </span>
            </div>
            <h1 className="text-3xl font-extrabold text-slate-900 tracking-tight mt-2">
              Caregiver Insights Dashboard
            </h1>
            <p className="text-slate-500 text-sm mt-0.5">
              Broad engagement trends, effective adaptations, and session history for {learnerName}.
            </p>
          </div>
          <AudioButton
            text={`Caregiver Insights summary for ${learnerName}. Total sessions completed: ${insights?.total_sessions || 0}.`}
            label="Listen Summary"
          />
        </div>

        {/* Top Summary Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <div className="bg-white p-6 rounded-3xl border border-slate-200/80 shadow-md space-y-2">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-400">Total Sessions</div>
            <div className="text-3xl font-black text-slate-900">{insights?.total_sessions || 0} Sessions</div>
            <div className="text-xs text-slate-500 font-medium">Completed learning quests</div>
          </div>

          <div className="bg-white p-6 rounded-3xl border border-slate-200/80 shadow-md space-y-2">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-400">Tasks Completed</div>
            <div className="text-3xl font-black text-indigo-600">{insights?.total_tasks_completed || 0} Quests</div>
            <div className="text-xs text-slate-500 font-medium">Across all subjects</div>
          </div>

          <div className="bg-white p-6 rounded-3xl border border-slate-200/80 shadow-md space-y-2">
            <div className="text-xs font-bold uppercase tracking-wider text-slate-400">Quest Stars</div>
            <div className="text-3xl font-black text-amber-500">{insights?.total_stars || 0} Stars</div>
            <div className="text-xs text-slate-500 font-medium">Earned reward points</div>
          </div>
        </div>

        {/* Broad Engagement Trend */}
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/80 shadow-md space-y-6">
          <div className="flex items-center justify-between">
            <h2 className="text-xl font-extrabold text-slate-900 flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-indigo-600" />
              Session Interaction State Distribution
            </h2>
            <span className="text-xs text-slate-400 font-semibold">Broad non-medical signals</span>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <div className="p-4 rounded-2xl bg-indigo-50/70 border border-indigo-100 text-center space-y-1">
              <div className="text-2xl font-black text-indigo-700">{engagement.focused_percentage || 70}%</div>
              <div className="text-xs font-bold text-slate-700">Focused & High Engagement</div>
              <div className="text-[10px] text-slate-500">Active problem solving</div>
            </div>

            <div className="p-4 rounded-2xl bg-amber-50/70 border border-amber-100 text-center space-y-1">
              <div className="text-2xl font-black text-amber-700">{engagement.attention_drift_percentage || 15}%</div>
              <div className="text-xs font-bold text-slate-700">Attention Drift</div>
              <div className="text-[10px] text-slate-500">Re-engaged with interest theme</div>
            </div>

            <div className="p-4 rounded-2xl bg-rose-50/70 border border-rose-100 text-center space-y-1">
              <div className="text-2xl font-black text-rose-700">{engagement.fatigue_percentage || 15}%</div>
              <div className="text-xs font-bold text-slate-700">Possible Fatigue</div>
              <div className="text-[10px] text-slate-500">Supported by Calm Mode breaks</div>
            </div>
          </div>
        </div>

        {/* Effective Adaptations */}
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/80 shadow-md space-y-6">
          <h2 className="text-xl font-extrabold text-slate-900 flex items-center gap-2">
            <Sparkles className="w-5 h-5 text-purple-600" />
            Commonly Effective UI & Learning Adaptations
          </h2>

          <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
            {(insights?.effective_adaptations || []).map((adapt, idx) => (
              <div key={idx} className="p-4 rounded-2xl border border-slate-200 bg-slate-50/50 space-y-1">
                <div className="text-sm font-bold text-slate-900">{adapt.adaptation}</div>
                <div className="text-xs text-slate-600">{adapt.impact}</div>
              </div>
            ))}
          </div>
        </div>

        {/* Recent Session History */}
        <div className="bg-white p-6 sm:p-8 rounded-3xl border border-slate-200/80 shadow-md space-y-4">
          <h2 className="text-xl font-extrabold text-slate-900 flex items-center gap-2">
            <Clock className="w-5 h-5 text-slate-600" />
            Recent Session History
          </h2>

          <div className="divide-y divide-slate-100">
            {(insights?.recent_sessions || []).map(sess => (
              <div key={sess.id} className="py-3 flex items-center justify-between">
                <div>
                  <div className="text-sm font-bold text-slate-800">{sess.date}</div>
                  <div className="text-xs text-slate-500">{sess.tasks_completed} activities completed</div>
                </div>
                <span className="px-3 py-1 bg-indigo-50 text-indigo-700 font-extrabold text-xs rounded-full">
                  +{sess.points_earned} Stars
                </span>
              </div>
            ))}
          </div>
        </div>

      </main>

      <Footer />
    </div>
  );
};

export default CaregiverDashboardPage;
