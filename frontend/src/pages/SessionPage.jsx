import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import { ArrowLeft, Award, Coffee, RefreshCw, ShieldCheck, Camera, CameraOff } from 'lucide-react';
import { 
  getTasks, startSession, submitAnswer, endSession, 
  generatePersonalizedTask, getAIScaffold, getAdaptationExplanation 
} from '../services/api';
import { telemetryCollector } from '../services/telemetryService';
import { stopWebGazer } from '../services/webgazerService';
import { useSensory } from '../context/SensoryContext';
import { useTheme } from '../context/ThemeContext';

import TaskCard from '../components/session/TaskCard';
import SessionCalibration from '../components/session/SessionCalibration';
import SensoryToolbar from '../components/session/SensoryToolbar';
import StateFeedbackBanner from '../components/session/StateFeedbackBanner';
import MicroMilestoneProgress from '../components/session/MicroMilestoneProgress';
import ScaffoldedHintBox from '../components/session/ScaffoldedHintBox';
import PersonalizedBreakModal from '../components/session/PersonalizedBreakModal';
import HackathonDemoBar from '../components/common/HackathonDemoBar';
import AdaptationExplainer from '../components/session/AdaptationExplainer';
import PrivacyConsentModal from '../components/common/PrivacyConsentModal';

import Navbar from '../components/common/Navbar';
import Footer from '../components/common/Footer';

const SessionPage = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { primaryColor } = useTheme();
  const { applyStateAdaptation, setManualSensoryMode, resetManualOverride } = useSensory();

  const [showCalibration, setShowCalibration] = useState(true);
  const [tasks, setTasks] = useState([]);
  const [currentTaskIndex, setCurrentTaskIndex] = useState(0);
  const [sessionId, setSessionId] = useState(null);
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [sessionSummary, setSessionSummary] = useState(null);
  const [showBreakModal, setShowBreakModal] = useState(false);
  const [showPrivacyModal, setShowPrivacyModal] = useState(false);
  const [scaffoldData, setScaffoldData] = useState(null);
  const [explainerData, setExplainerData] = useState(null);
  const [attemptCount, setAttemptCount] = useState(0);
  const [isCameraActive, setIsCameraActive] = useState(false);

  const filterSubject = location.state?.subject || null;
  const filterGrade = location.state?.grade || parseInt(localStorage.getItem('neuroquest_active_student_grade'), 10) || 6;
  const filterChapter = location.state?.chapter || null;
  const initialTaskId = location.state?.taskId || null;

  useEffect(() => {
    initSessionData();
    return () => {
      telemetryCollector.stopTracking();
      stopWebGazer();
    };
  }, []);

  const initSessionData = async () => {
    setLoading(true);
    try {
      // 1. Start backend session
      const sRes = await startSession();
      const sId = sRes.data.id;
      setSessionId(sId);

      // 2. Fetch NCERT tasks for this subject and grade
      let taskList = [];
      const tRes = await getTasks(filterSubject, null, filterGrade);
      taskList = tRes.data || [];

      // If chapter filter specified, prioritize matching chapter tasks
      if (filterChapter && taskList.length > 0) {
        const matchingChapterTasks = taskList.filter(t => 
          (t.chapter && t.chapter.toLowerCase() === filterChapter.toLowerCase()) ||
          (t.title && t.title.toLowerCase().includes(filterChapter.toLowerCase())) ||
          (t.chapter && filterChapter.toLowerCase().includes(t.chapter.toLowerCase()))
        );
        if (matchingChapterTasks.length > 0) {
          taskList = [...matchingChapterTasks, ...taskList.filter(t => !matchingChapterTasks.includes(t))];
        }
      }

      // If subject query yielded 0, load all available authentic NCERT tasks for this grade
      if (taskList.length === 0) {
        const gradeFallbackRes = await getTasks(null, null, filterGrade);
        taskList = gradeFallbackRes.data || [];
      }

      if (initialTaskId) {
        const foundIdx = taskList.findIndex(t => t.id === initialTaskId);
        if (foundIdx > -1) {
          setCurrentTaskIndex(foundIdx);
        }
      }

      setTasks(taskList);
    } catch (err) {
      console.error('Failed to initialize session:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleCalibrationComplete = ({ useCamera }) => {
    setShowCalibration(false);
    setIsCameraActive(Boolean(useCamera));
    
    // Start real-time browser telemetry evaluation loop
    if (sessionId) {
      telemetryCollector.startTracking(sessionId, (telemetryResult) => {
        if (telemetryResult?.adaptation) {
          applyStateAdaptation(telemetryResult.adaptation, telemetryResult.state);
        }
      });
    }
  };

  const handleAnswerSubmit = async (selectedOption) => {
    if (!sessionId || !tasks[currentTaskIndex]) return;

    setSubmitting(true);
    const newAttempt = attemptCount + 1;
    setAttemptCount(newAttempt);

    try {
      const currentTask = tasks[currentTaskIndex];
      const res = await submitAnswer(sessionId, {
        task_id: currentTask.id,
        selected_answer: selectedOption,
        time_taken_seconds: 15,
        hints_used: 0
      });

      if (!res.data.is_correct) {
        telemetryCollector.recordIncorrectAttempt();
        // Fetch gentle failure scaffolding
        try {
          const scRes = await getAIScaffold({ task: currentTask, attempt_count: newAttempt });
          if (scRes.data) setScaffoldData(scRes.data);
        } catch (scErr) {
          console.log("Scaffold error:", scErr);
        }
      } else {
        setScaffoldData(null);
      }

      return res.data;
    } catch (err) {
      console.error('Answer submission error:', err);
      return {
        is_correct: false,
        points_earned: 2,
        correct_answer: tasks[currentTaskIndex].correct_answer,
        explanation: tasks[currentTaskIndex].explanation,
        feedback_message: "Let's try another route together! Taking it step by step makes learning easy."
      };
    } finally {
      setSubmitting(false);
    }
  };

  const handleRequestNextScaffoldLevel = async (nextLvl) => {
    if (!tasks[currentTaskIndex]) return;
    try {
      const scRes = await getAIScaffold({
        task: tasks[currentTaskIndex],
        attempt_count: attemptCount,
        requested_level: nextLvl
      });
      if (scRes.data) setScaffoldData(scRes.data);
    } catch (err) {
      console.error("Next scaffold level error:", err);
    }
  };

  const handleNextTask = () => {
    setScaffoldData(null);
    setAttemptCount(0);
    if (currentTaskIndex < tasks.length - 1) {
      const nextIdx = currentTaskIndex + 1;
      setCurrentTaskIndex(nextIdx);
      telemetryCollector.resetTaskTimer(tasks[nextIdx].difficulty);
    } else {
      finishSession();
    }
  };

  const finishSession = async () => {
    telemetryCollector.stopTracking();
    stopWebGazer();

    if (sessionId) {
      try {
        const res = await endSession(sessionId);
        setSessionSummary(res.data);
      } catch (err) {
        console.error(err);
      }
    }
  };

  if (loading) {
    return (
      <div className="min-h-screen flex flex-col bg-slate-50">
        <Navbar />
        <div className="flex-1 flex items-center justify-center">
          <div className="text-center space-y-3">
            <div className="w-12 h-12 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin mx-auto" />
            <p className="text-sm font-bold text-slate-700">Loading your Quest Room...</p>
          </div>
        </div>
        <Footer />
      </div>
    );
  }

  const handleDemoProfileActivated = async (resData) => {
    initSessionData();
  };

  const handleStateSimulated = async (resData) => {
    if (resData?.adaptation) {
      applyStateAdaptation(resData.adaptation, resData.state);
    }
    if (resData?.explainer) {
      setExplainerData(resData.explainer);
    }
  };

  return (
    <div className="min-h-screen flex flex-col bg-slate-50">
      {/* Hackathon Presenter Demo Simulation Bar */}
      <HackathonDemoBar
        onProfileActivated={handleDemoProfileActivated}
        onStateSimulated={handleStateSimulated}
      />

      <Navbar />

      {/* 1. Session Calibration Wizard */}
      {showCalibration && (
        <SessionCalibration onCalibrationComplete={handleCalibrationComplete} />
      )}

      {/* 2. Personalized Break Modal */}
      {showBreakModal && (
        <PersonalizedBreakModal onClose={() => setShowBreakModal(false)} />
      )}

      {/* 3. Data Privacy & Sensing Consent Modal */}
      <PrivacyConsentModal
        isOpen={showPrivacyModal}
        onClose={() => setShowPrivacyModal(false)}
      />

      <main className="flex-1 max-w-4xl mx-auto px-4 sm:px-6 py-8 w-full space-y-6">
        
        {/* Top Header & Navigation */}
        <div className="flex items-center justify-between">
          <button
            onClick={() => navigate('/home')}
            className="inline-flex items-center gap-2 px-4 py-2 rounded-2xl bg-white border border-slate-200 text-xs font-bold text-slate-700 hover:bg-slate-50 transition-all shadow-sm"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Return Home</span>
          </button>

          <div className="flex items-center gap-2.5">
            {isCameraActive ? (
              <div className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-2xl bg-emerald-50 border border-emerald-300 text-xs font-bold text-emerald-800 shadow-sm">
                <span className="w-2 h-2 rounded-full bg-emerald-500 animate-pulse" />
                <Camera className="w-3.5 h-3.5 text-emerald-600" />
                <span>Gaze Assist Active</span>
              </div>
            ) : (
              <div className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-2xl bg-slate-100 border border-slate-200 text-xs font-semibold text-slate-600">
                <CameraOff className="w-3.5 h-3.5 text-slate-400" />
                <span>Non-Camera Telemetry</span>
              </div>
            )}

            <button
              onClick={() => setShowPrivacyModal(true)}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-2xl bg-emerald-50 border border-emerald-200 text-xs font-extrabold text-emerald-800 hover:bg-emerald-100 transition-all"
            >
              <ShieldCheck className="w-4 h-4 text-emerald-600" />
              <span>Privacy & Sensing</span>
            </button>

            {tasks.length > 0 && !sessionSummary && (
              <div className="text-xs font-bold text-slate-500 bg-slate-200/60 px-3.5 py-1.5 rounded-full">
                Task {currentTaskIndex + 1} of {tasks.length}
              </div>
            )}
          </div>
        </div>

        {/* Micro-Milestone Progress */}
        {tasks.length > 0 && !sessionSummary && (
          <MicroMilestoneProgress
            currentStep={currentTaskIndex + 1}
            totalSteps={tasks.length}
            milestoneTitle={tasks[currentTaskIndex]?.title || "Personal Mission Milestone"}
          />
        )}

        {/* Live Sensory Override Toolbar */}
        {!sessionSummary && <SensoryToolbar />}

        {/* Learner Encouragement State Feedback Banner */}
        {!sessionSummary && (
          <StateFeedbackBanner onRequestBreak={() => setShowBreakModal(true)} />
        )}

        {/* Hackathon Judge Adaptation Visualization Explainer */}
        {explainerData && !sessionSummary && (
          <AdaptationExplainer 
            explainerData={explainerData} 
            onKeep={() => {
              if (explainerData.ui_mode) setManualSensoryMode(explainerData.ui_mode);
            }}
            onUndo={() => {
              setManualSensoryMode('normal');
              setExplainerData(prev => prev ? {
                ...prev,
                what_changed: "Layout reverted back to standard balanced mode upon learner request.",
                why_it_changed: "Learner autonomy respected & reversible adaptation applied.",
                what_signal_used: "Direct learner Undo button click.",
                ui_mode: "normal"
              } : null);
            }}
            onChangeMode={() => {
              setManualSensoryMode('calm');
            }}
          />
        )}

        {/* Phase 3 Failure Scaffolding Box */}
        {scaffoldData && !sessionSummary && (
          <ScaffoldedHintBox
            scaffoldData={scaffoldData}
            onRequestNextLevel={handleRequestNextScaffoldLevel}
            onDismiss={() => setScaffoldData(null)}
            onSelectRepresentation={(rep) => {
              if (rep === 'visual_block' || rep === 'simplified') {
                setManualSensoryMode('focus');
              }
            }}
          />
        )}

        {/* Session Summary Modal */}
        {sessionSummary ? (
          <div className="bg-white rounded-3xl p-8 border border-slate-200/80 shadow-xl text-center space-y-6 animate-fadeIn">
            <div className="w-16 h-16 rounded-3xl bg-amber-400 text-amber-950 mx-auto flex items-center justify-center font-extrabold shadow-lg">
              <Award className="w-8 h-8" />
            </div>

            <div className="space-y-2">
              <h2 className="text-3xl font-black text-slate-900">Quest Adventure Completed!</h2>
              <p className="text-sm text-slate-600 max-w-md mx-auto">
                You completed {sessionSummary.tasks_completed} activities and earned {sessionSummary.points_earned} stars in this session!
              </p>
            </div>

            <div className="pt-4 flex justify-center gap-4">
              <button
                onClick={() => navigate('/home')}
                className="px-8 py-3.5 rounded-2xl text-sm font-extrabold text-white bg-indigo-600 hover:bg-indigo-700 shadow-lg shadow-indigo-500/25 transition-all"
              >
                Back to Dashboard
              </button>
            </div>
          </div>
        ) : tasks.length === 0 ? (
          <div className="bg-white rounded-3xl p-8 text-center space-y-4 border border-slate-200">
            <h3 className="text-lg font-bold text-slate-800">No tasks found for this selection.</h3>
            <button
              onClick={() => navigate('/home')}
              className="px-6 py-2.5 bg-indigo-600 text-white font-bold rounded-2xl text-xs"
            >
              Explore All Subjects
            </button>
          </div>
        ) : (
          <div className="space-y-6">
            <TaskCard
              key={tasks[currentTaskIndex].id}
              task={tasks[currentTaskIndex]}
              onAnswerSubmit={handleAnswerSubmit}
              loading={submitting}
            />

            <div className="flex justify-end">
              <button
                onClick={handleNextTask}
                className="px-8 py-3.5 rounded-2xl text-sm font-extrabold text-white shadow-lg transition-all flex items-center gap-2 active:scale-95"
                style={{ backgroundColor: primaryColor }}
              >
                <span>{currentTaskIndex < tasks.length - 1 ? 'Next Activity' : 'Complete Quest Session'}</span>
              </button>
            </div>
          </div>
        )}

      </main>

      <Footer />
    </div>
  );
};

export default SessionPage;
