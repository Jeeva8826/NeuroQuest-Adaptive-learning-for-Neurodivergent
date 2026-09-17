import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext';
import { ThemeProvider } from './context/ThemeContext';
import { SensoryProvider } from './context/SensoryContext';

import LandingPage from './pages/LandingPage';
import LoginPage from './pages/LoginPage';
import RegisterPage from './pages/RegisterPage';
import MedicalOnboardingPage from './pages/MedicalOnboardingPage';
import OnboardingPage from './pages/OnboardingPage';
import LearnerHomePage from './pages/LearnerHomePage';
import SessionPage from './pages/SessionPage';
import ProgressPage from './pages/ProgressPage';
import SettingsPage from './pages/SettingsPage';
import CaregiverDashboardPage from './pages/CaregiverDashboardPage';

// Agent E Imports
import { Home } from './pages/Home';
import { CaregiverProfile } from './components/profile/CaregiverProfile';
import { AdaptiveLesson } from './components/lesson/AdaptiveLesson';

// Dashboards and Games
import GamesContainer from './games/Games';
import { LearnerDashboard, CaregiverDashboard, EducatorDashboard } from './components/dashboards/Dashboards';

const ProtectedRoute = ({ children }) => {
  const { user, loading } = useAuth();
  if (loading) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-slate-50">
        <div className="w-10 h-10 border-4 border-indigo-600 border-t-transparent rounded-full animate-spin" />
      </div>
    );
  }
  if (!user) return <Navigate to="/login" replace />;
  return children;
};

const OnboardingCheckRoute = ({ children }) => {
  const { user, hasCompletedOnboarding, loading } = useAuth();
  if (loading) return null;
  if (!user) return <Navigate to="/login" replace />;
  if (!hasCompletedOnboarding) return <Navigate to="/onboarding" replace />;
  return children;
};

function AppRoutes() {
  return (
    <Routes>
      <Route path="/" element={<LandingPage />} />
      <Route path="/login" element={<LoginPage />} />
      <Route path="/register" element={<RegisterPage />} />
      
      {/* Registration / Medical / Caregiver Profile & Settings */}
      <Route path="/medical-onboarding" element={
        <ProtectedRoute>
          <MedicalOnboardingPage />
        </ProtectedRoute>
      } />
      
      <Route
        path="/onboarding"
        element={
          <ProtectedRoute>
            <OnboardingPage />
          </ProtectedRoute>
        }
      />

      {/* Learner Pages */}
      <Route
        path="/home"
        element={
          <OnboardingCheckRoute>
            <LearnerHomePage />
          </OnboardingCheckRoute>
        }
      />

      <Route
        path="/session"
        element={
          <OnboardingCheckRoute>
            <SessionPage />
          </OnboardingCheckRoute>
        }
      />

      <Route
        path="/progress"
        element={
          <OnboardingCheckRoute>
            <ProgressPage />
          </OnboardingCheckRoute>
        }
      />

      {/* Phase 2 Caregiver Insights Dashboard */}
      <Route
        path="/caregiver"
        element={
          <ProtectedRoute>
            <CaregiverDashboardPage />
          </ProtectedRoute>
        }
      />

      <Route
        path="/settings"
        element={
          <ProtectedRoute>
            <SettingsPage />
          </ProtectedRoute>
        }
      />

      {/* New Components from Agent E */}
      <Route path="/home-new" element={<Home />} />
      <Route path="/caregiver-profile" element={<CaregiverProfile />} />
      <Route path="/lesson" element={<AdaptiveLesson />} />

      {/* Gamification & Dashboards */}
      <Route path="/games" element={<GamesContainer />} />
      <Route path="/dashboard/learner" element={<LearnerDashboard />} />
      <Route path="/dashboard/caregiver" element={<CaregiverDashboard />} />
      <Route path="/dashboard/educator" element={<EducatorDashboard />} />

      <Route path="*" element={<Navigate to="/" replace />} />
    </Routes>
  );
}

function App() {
  return (
    <Router>
      <AuthProvider>
        <ThemeProvider>
          <SensoryProvider>
            <AppRoutes />
          </SensoryProvider>
        </ThemeProvider>
      </AuthProvider>
    </Router>
  );
}

export default App;
