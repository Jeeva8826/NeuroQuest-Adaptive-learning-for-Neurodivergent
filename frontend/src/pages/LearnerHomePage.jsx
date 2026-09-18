import React, { useEffect, useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { 
  Sparkles, BookOpen, Calculator, Globe, Music, Cpu, Palette,
  Award, Play, ArrowRight, Star, Flame, CheckCircle, Rocket
} from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import { useTheme } from '../context/ThemeContext';
import { useSensory } from '../context/SensoryContext';
import { 
  getProgressSummary, getTasks, getDailyWelcomeMission, 
  getPersonalGameWorld, getPersonalMasteryTree 
} from '../services/api';
import ThemeBanner from '../components/dashboard/ThemeBanner';
import PersonalWorldMap from '../components/dashboard/PersonalWorldMap';
import HackathonDemoBar from '../components/common/HackathonDemoBar';
import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';
import AudioButton from '../components/common/AudioButton';

const SUBJECT_CARDS = [
  { id: 'Mathematics', label: 'Mathematics', desc: 'Space counting, pattern jumps & numbers', icon: Calculator, color: 'from-blue-500 to-indigo-600' },
  { id: 'Science', label: 'Science', desc: 'Ocean habitats, planets & solar system', icon: Globe, color: 'from-emerald-500 to-teal-600' },
  { id: 'English', label: 'English', desc: 'Rhyming words, playful stories & vocab', icon: BookOpen, color: 'from-purple-500 to-pink-600' },
  { id: 'Coding/Logic', label: 'Coding & Logic', desc: 'Robot maze navigation & sequencing', icon: Cpu, color: 'from-sky-500 to-blue-700' },
  { id: 'General Knowledge', label: 'General Knowledge', desc: 'Rainbows, nature & world facts', icon: Palette, color: 'from-amber-500 to-orange-600' }
];

const LearnerHomePage = () => {
  const { user } = useAuth();
  const { primaryColor, profile } = useTheme();
  const { applyStateAdaptation } = useSensory();
  const navigate = useNavigate();

  const [progress, setProgress] = useState(null);
  const [recommendedTask, setRecommendedTask] = useState(null);
  const [dailyWelcome, setDailyWelcome] = useState(null);
  const [gameWorld, setGameWorld] = useState(null);
  const [masteryTree, setMasteryTree] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchDashboardData();
  }, []);

  const fetchDashboardData = async () => {
    try {
      const [progRes, tasksRes, welcomeRes, worldRes, treeRes] = await Promise.all([
        getProgressSummary(),
        getTasks(null, null),
        getDailyWelcomeMission().catch(() => ({ data: null })),
        getPersonalGameWorld().catch(() => ({ data: null })),
        getPersonalMasteryTree().catch(() => ({ data: null }))
      ]);
      
      setProgress(progRes.data);
      if (tasksRes.data && tasksRes.data.length > 0) {
        setRecommendedTask(tasksRes.data[0]);
      }
      if (welcomeRes.data) setDailyWelcome(welcomeRes.data);
      if (worldRes.data) setGameWorld(worldRes.data);
      if (treeRes.data) setMasteryTree(treeRes.data);
    } catch (err) {
      console.error('Error fetching dashboard data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleDemoProfileActivated = () => {
    fetchDashboardData();
  };

  const learnerName = localStorage.getItem('neuroquest_active_student_name') || profile?.learner_name || user?.full_name || 'Learner';
  const totalStars = progress?.total_stars || 10;
  const streakDays = progress?.streak_days || 1;
  const completedCount = progress?.total_tasks_completed || 0;

  return (
    <div className="min-h-screen flex flex-col bg-slate-50 relative overflow-x-hidden">
      {/* Ambient background soft glow */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full max-w-7xl h-96 bg-gradient-to-b from-indigo-50/60 via-purple-50/30 to-transparent pointer-events-none" />

      {/* Hackathon Presenter Demo Bar */}
      <HackathonDemoBar 
        onProfileActivated={handleDemoProfileActivated} 
        onStateSimulated={(data) => applyStateAdaptation(data?.adaptation, data?.state)}
      />

      <Navbar />

      <main className="flex-1 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 w-full space-y-8 relative z-10">
        
        {/* Hero Personalized Banner */}
        <ThemeBanner learnerName={learnerName} totalStars={totalStars} />

        {/* Phase 3 Personalized Daily Return Experience Mission */}
        {dailyWelcome && (
          <div className="bg-gradient-to-br from-indigo-900 via-purple-950 to-slate-900 text-white rounded-3xl p-6 sm:p-8 shadow-xl border border-indigo-500/30 space-y-4">
            <div className="flex items-center justify-between">
              <div className="flex items-center gap-2">
                <div className="w-10 h-10 rounded-2xl bg-indigo-500 text-white flex items-center justify-center font-bold shadow-md">
                  <Rocket className="w-5 h-5" />
                </div>
                <div>
                  <span className="text-[10px] font-extrabold uppercase text-indigo-300 tracking-wider">Daily Return Mission</span>
                  <h3 className="text-xl font-black text-white">{dailyWelcome.mission_title}</h3>
                </div>
              </div>
              <AudioButton
                text={`${dailyWelcome.greeting}`}
                label="Listen Welcome"
                className="bg-indigo-800 text-indigo-100 border-indigo-700"
              />
            </div>
            <p className="text-sm text-indigo-100 leading-relaxed font-medium bg-indigo-950/60 p-4 rounded-2xl border border-indigo-800/60">
              {dailyWelcome.greeting}
            </p>
            <div className="pt-2 flex justify-end">
              <button
                onClick={() => navigate('/session')}
                className="px-6 py-3 rounded-2xl text-xs font-black text-white bg-indigo-600 hover:bg-indigo-500 shadow-lg shadow-indigo-500/30 transition-all flex items-center gap-2 hover:scale-[1.02] active:scale-98"
              >
                <Play className="w-4 h-4 fill-current" />
                <span>Launch Today's Mission</span>
              </button>
            </div>
          </div>
        )}

        {/* Phase 3 Personal Game World Map & Mastery Tree */}
        <PersonalWorldMap gameWorld={gameWorld} masteryTree={masteryTree} />

        {/* Quick Stats Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-3 gap-4">
          <div 
            onClick={() => navigate('/progress')}
            className="bg-white p-5 rounded-3xl border border-slate-200/80 shadow-sm hover:shadow-md hover:border-amber-300 transition-all cursor-pointer flex items-center gap-4 group"
            title="View Badges & Stars"
          >
            <div className="w-12 h-12 rounded-2xl bg-amber-100 text-amber-600 flex items-center justify-center font-bold group-hover:scale-105 transition-transform">
              <Star className="w-6 h-6 fill-current" />
            </div>
            <div className="flex-1">
              <div className="text-2xl font-black text-slate-900">{totalStars}</div>
              <div className="text-xs font-semibold text-slate-500 flex items-center justify-between">
                <span>Stars Earned</span>
                <ArrowRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-1 transition-all" />
              </div>
            </div>
          </div>

          <div 
            onClick={() => navigate('/progress')}
            className="bg-white p-5 rounded-3xl border border-slate-200/80 shadow-sm hover:shadow-md hover:border-rose-300 transition-all cursor-pointer flex items-center gap-4 group"
            title="View Streak Progress"
          >
            <div className="w-12 h-12 rounded-2xl bg-rose-100 text-rose-600 flex items-center justify-center font-bold group-hover:scale-105 transition-transform">
              <Flame className="w-6 h-6 fill-current" />
            </div>
            <div className="flex-1">
              <div className="text-2xl font-black text-slate-900">{streakDays} Day Streak</div>
              <div className="text-xs font-semibold text-slate-500 flex items-center justify-between">
                <span>Daily Quest Streak</span>
                <ArrowRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-1 transition-all" />
              </div>
            </div>
          </div>

          <div 
            onClick={() => navigate('/session')}
            className="bg-white p-5 rounded-3xl border border-slate-200/80 shadow-sm hover:shadow-md hover:border-emerald-300 transition-all cursor-pointer flex items-center gap-4 group"
            title="Go to Quest Room"
          >
            <div className="w-12 h-12 rounded-2xl bg-emerald-100 text-emerald-600 flex items-center justify-center font-bold group-hover:scale-105 transition-transform">
              <CheckCircle className="w-6 h-6" />
            </div>
            <div className="flex-1">
              <div className="text-2xl font-black text-slate-900">{completedCount} Quests</div>
              <div className="text-xs font-semibold text-slate-500 flex items-center justify-between">
                <span>Completed Activities</span>
                <ArrowRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-indigo-600 group-hover:translate-x-1 transition-all" />
              </div>
            </div>
          </div>
        </div>

        {/* Featured Quest Start Banner */}
        {recommendedTask && (
          <div className="bg-gradient-to-r from-slate-900 via-indigo-950 to-slate-900 text-white rounded-3xl p-6 sm:p-8 shadow-xl flex flex-col sm:flex-row items-center justify-between gap-6 border border-slate-800">
            <div className="space-y-2 max-w-xl">
              <div className="flex items-center gap-2">
                <span className="px-3 py-1 bg-indigo-500/30 text-indigo-300 rounded-full text-xs font-extrabold uppercase tracking-wider border border-indigo-400/30">
                  Recommended Quest
                </span>
                <AudioButton
                  text={`Recommended Quest: ${recommendedTask.title}. ${recommendedTask.question}`}
                  label="Listen Quest"
                  className="bg-slate-800 text-slate-200 border-slate-700"
                />
              </div>
              <h3 className="text-2xl font-extrabold">{recommendedTask.title}</h3>
              <p className="text-slate-300 text-sm">{recommendedTask.question}</p>
            </div>

            <button
              onClick={() => navigate('/session', { state: { taskId: recommendedTask.id } })}
              className="px-7 py-3.5 rounded-2xl font-extrabold text-white bg-indigo-600 hover:bg-indigo-500 shadow-lg shadow-indigo-500/30 transition-all flex items-center gap-2 shrink-0 transform active:scale-95"
            >
              <Play className="w-5 h-5 fill-current" />
              <span>Start Activity</span>
            </button>
          </div>
        )}

        {/* Subject Exploration Cards */}
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h2 className="text-2xl font-extrabold text-slate-900 tracking-tight">
              Learning Quests by Subject
            </h2>
            <Link to="/session" className="text-xs font-bold text-indigo-600 hover:underline flex items-center gap-1">
              View All Quests <ArrowRight className="w-3.5 h-3.5" />
            </Link>
          </div>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
            {SUBJECT_CARDS.map(sub => {
              const IconComponent = sub.icon;
              return (
                <div
                  key={sub.id}
                  onClick={() => navigate('/session', { state: { subject: sub.id } })}
                  className="bg-white rounded-3xl p-6 border border-slate-200/80 shadow-md hover:shadow-xl transition-all cursor-pointer group flex flex-col justify-between"
                >
                  <div className="space-y-4">
                    <div className={`w-12 h-12 rounded-2xl bg-gradient-to-br ${sub.color} text-white flex items-center justify-center shadow-md group-hover:scale-110 transition-transform`}>
                      <IconComponent className="w-6 h-6" />
                    </div>
                    <div>
                      <h3 className="text-lg font-extrabold text-slate-900 group-hover:text-indigo-600 transition-colors">
                        {sub.label}
                      </h3>
                      <p className="text-xs font-medium text-slate-500 mt-1">
                        {sub.desc}
                      </p>
                    </div>
                  </div>

                  <div className="pt-6 flex items-center justify-between border-t border-slate-100 mt-4">
                    <span className="text-xs font-bold text-slate-400">Adaptive Tasks</span>
                    <span className="text-xs font-extrabold text-indigo-600 group-hover:translate-x-1 transition-transform flex items-center gap-1">
                      Enter Subject <ArrowRight className="w-3.5 h-3.5" />
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Earned Rewards Preview */}
        {progress?.earned_badges && progress.earned_badges.length > 0 && (
          <div className="bg-white rounded-3xl p-6 sm:p-8 border border-slate-200/80 shadow-md space-y-4">
            <div className="flex items-center justify-between">
              <h2 className="text-xl font-extrabold text-slate-900 flex items-center gap-2">
                <Award className="w-5 h-5 text-amber-500" />
                Unlocked Trophies & Badges
              </h2>
              <Link to="/progress" className="text-xs font-bold text-indigo-600 hover:underline">
                View Collection
              </Link>
            </div>

            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
              {progress.earned_badges.slice(0, 4).map(badge => (
                <div
                  key={badge.id}
                  onClick={() => navigate('/progress')}
                  className={`p-4 rounded-2xl border text-center space-y-2 cursor-pointer hover:shadow-md hover:scale-[1.02] transition-all ${
                    badge.is_unlocked
                      ? 'bg-amber-50/70 border-amber-200 text-amber-950'
                      : 'bg-slate-50 border-slate-200 text-slate-400 opacity-60'
                  }`}
                  title="View Badge in Progress Hub"
                >
                  <div className="w-10 h-10 rounded-2xl bg-amber-400 text-amber-950 mx-auto flex items-center justify-center font-bold shadow-sm">
                    <Award className="w-5 h-5" />
                  </div>
                  <div className="text-xs font-extrabold">{badge.title}</div>
                  <div className="text-[10px] text-slate-500">{badge.description}</div>
                </div>
              ))}
            </div>
          </div>
        )}

      </main>

      <Footer />
    </div>
  );
};

export default LearnerHomePage;
