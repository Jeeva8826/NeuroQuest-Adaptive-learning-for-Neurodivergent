import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { ShieldCheck, LogIn, AlertCircle, Eye, EyeOff, KeyRound, CheckCircle2, Sparkles, X } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function LoginPage() {
  const navigate = useNavigate();
  const { refreshUser } = useAuth();
  const [formData, setFormData] = useState({
    username: '',
    password: ''
  });
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [successMsg, setSuccessMsg] = useState('');
  const [loading, setLoading] = useState(false);

  // Password reset modal state
  const [showResetModal, setShowResetModal] = useState(false);
  const [resetIdentifier, setResetIdentifier] = useState('');
  const [resetNewPassword, setResetNewPassword] = useState('');
  const [resetLoading, setResetLoading] = useState(false);
  const [resetMsg, setResetMsg] = useState({ type: '', text: '' });

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setSuccessMsg('');
    setLoading(true);

    const identifier = formData.username.trim();
    const payload = {
      username: identifier,
      email: identifier,
      password: formData.password.trim()
    };

    try {
      // Use relative proxy first, fallback to direct port 8000
      let res;
      try {
        res = await fetch('/auth/token', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } catch (networkErr) {
        res = await fetch('http://localhost:8000/auth/token', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }
      
      const data = await res.json();
      
      if (!res.ok) {
        throw new Error(data.detail || 'Invalid username or password');
      }

      // Store token in both keys for compatibility
      localStorage.setItem('neuroquest_token', data.access_token);
      localStorage.setItem('token', data.access_token);

      if (refreshUser) {
        await refreshUser();
      }

      // Check registered students to guide caretaker directly into the student setup flow
      try {
        let studentRes;
        try {
          studentRes = await fetch('/api/students', {
            headers: { 'Authorization': `Bearer ${data.access_token}` }
          });
        } catch (netErr) {
          studentRes = await fetch('http://localhost:8000/api/students', {
            headers: { 'Authorization': `Bearer ${data.access_token}` }
          });
        }

        if (studentRes && studentRes.ok) {
          const students = await studentRes.json();
          // If no student registered yet, guide caretaker directly to Student Registration!
          if (!students || students.length === 0) {
            navigate('/student-registration');
            return;
          }

          // If a student is registered but baseline assessment is pending, take them directly to the 20-Q wizard!
          const pending = students.find(s => !s.has_completed_screening);
          if (pending) {
            navigate(`/student-screening/${pending.id}`);
            return;
          }

          // If screening is complete, go to Caregiver Hub
          navigate('/caregiver');
          return;
        }
      } catch (checkErr) {
        console.warn('Student onboarding check notice:', checkErr);
      }

      navigate('/student-registration');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const handlePasswordReset = async (e) => {
    e.preventDefault();
    setResetLoading(true);
    setResetMsg({ type: '', text: '' });

    const id = resetIdentifier.trim() || formData.username.trim();
    if (!id) {
      setResetMsg({ type: 'error', text: 'Please enter your username or email.' });
      setResetLoading(false);
      return;
    }

    try {
      let res;
      try {
        res = await fetch('/auth/reset-password', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            identifier: id,
            new_password: resetNewPassword.trim()
          })
        });
      } catch (err) {
        res = await fetch('http://localhost:8000/auth/reset-password', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            identifier: id,
            new_password: resetNewPassword.trim()
          })
        });
      }

      const data = await res.json();
      if (!res.ok) {
        throw new Error(data.detail || 'Password reset failed');
      }

      setResetMsg({ type: 'success', text: 'Password reset successfully!' });
      setFormData({
        username: id,
        password: resetNewPassword.trim()
      });
      setSuccessMsg('Password updated! You can now sign in immediately.');
      setTimeout(() => setShowResetModal(false), 1200);
    } catch (err) {
      setResetMsg({ type: 'error', text: err.message });
    } finally {
      setResetLoading(false);
    }
  };

  const fillQuickLogin = (user, pass) => {
    setFormData({ username: user, password: pass });
    setError('');
  };

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8 font-sans">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="flex justify-center mb-6">
          <div className="w-16 h-16 rounded-2xl bg-emerald-100 flex items-center justify-center border border-emerald-200 shadow-sm">
            <ShieldCheck className="w-8 h-8 text-emerald-700" />
          </div>
        </div>
        <h2 className="text-center text-3xl font-extrabold text-slate-900 tracking-tight">
          Welcome to NeuroQuest
        </h2>
        <p className="mt-2 text-center text-sm text-slate-500 font-medium">
          Access your secure Caregiver and Learner dashboards.
        </p>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 sm:rounded-xl sm:px-10 border border-slate-200 shadow-sm">
          {error && (
            <div className="mb-6 bg-rose-50 border border-rose-200 text-rose-700 px-4 py-3 rounded-lg flex items-start gap-3">
              <AlertCircle className="w-5 h-5 shrink-0 mt-0.5 text-rose-600" />
              <div className="text-sm font-medium">
                <p>{error}</p>
                <button
                  type="button"
                  onClick={() => {
                    setResetIdentifier(formData.username);
                    setShowResetModal(true);
                  }}
                  className="mt-1 text-xs font-bold text-emerald-700 hover:text-emerald-800 underline"
                >
                  Forgot your password? Reset it here &rarr;
                </button>
              </div>
            </div>
          )}

          {successMsg && (
            <div className="mb-6 bg-emerald-50 border border-emerald-200 text-emerald-800 px-4 py-3 rounded-lg flex items-center gap-3 text-sm font-medium">
              <CheckCircle2 className="w-5 h-5 text-emerald-600 shrink-0" />
              <span>{successMsg}</span>
            </div>
          )}
          
          <form className="space-y-6" onSubmit={handleSubmit}>
            <div>
              <label className="block text-sm font-bold text-slate-700 mb-1">Username or Email</label>
              <input
                type="text"
                required
                value={formData.username}
                className="appearance-none block w-full px-4 py-3 border border-slate-300 rounded-lg shadow-sm placeholder-slate-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm font-medium transition-colors"
                onChange={e => setFormData({...formData, username: e.target.value})}
                placeholder="Enter your username or email"
              />
            </div>

            <div>
              <div className="flex items-center justify-between mb-1">
                <label className="block text-sm font-bold text-slate-700">Password</label>
                <button
                  type="button"
                  onClick={() => {
                    setResetIdentifier(formData.username);
                    setShowResetModal(true);
                  }}
                  className="text-xs font-semibold text-emerald-700 hover:text-emerald-800"
                >
                  Forgot password?
                </button>
              </div>
              <div className="relative">
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  value={formData.password}
                  className="appearance-none block w-full px-4 py-3 pr-11 border border-slate-300 rounded-lg shadow-sm placeholder-slate-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm font-medium transition-colors"
                  onChange={e => setFormData({...formData, password: e.target.value})}
                  placeholder="••••••••"
                />
                <button
                  type="button"
                  onClick={() => setShowPassword(!showPassword)}
                  className="absolute inset-y-0 right-0 pr-3 flex items-center text-slate-400 hover:text-slate-600"
                  tabIndex={-1}
                >
                  {showPassword ? <EyeOff className="w-5 h-5" /> : <Eye className="w-5 h-5" />}
                </button>
              </div>
            </div>

            <div className="pt-1">
              <button
                type="submit"
                disabled={loading}
                className="w-full flex justify-center items-center gap-2 py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-bold text-white bg-slate-800 hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-800 disabled:opacity-50 transition-colors"
              >
                {loading ? 'Authenticating...' : (
                  <>
                    <span>Sign In Securely</span>
                    <LogIn className="w-4 h-4" />
                  </>
                )}
              </button>
            </div>
          </form>

          {/* Quick Demo Credentials for Testing & Evaluation */}
          <div className="mt-6 pt-5 border-t border-slate-100">
            <div className="flex items-center gap-1.5 text-xs font-bold text-slate-500 mb-2.5">
              <Sparkles className="w-3.5 h-3.5 text-amber-500" />
              <span>Quick Demo Logins (Click to Autofill):</span>
            </div>
            <div className="flex flex-wrap gap-2">
              <button
                type="button"
                onClick={() => fillQuickLogin('jeevananth1234@gmail.com', '123')}
                className="text-xs bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold px-2.5 py-1.5 rounded border border-slate-200 transition-colors"
              >
                jeevananth (Pass: 123)
              </button>
              <button
                type="button"
                onClick={() => fillQuickLogin('testparent@example.com', 'Password123!')}
                className="text-xs bg-slate-100 hover:bg-slate-200 text-slate-800 font-semibold px-2.5 py-1.5 rounded border border-slate-200 transition-colors"
              >
                testparent (Pass: Password123!)
              </button>
            </div>
          </div>
          
          <div className="mt-6 pt-5 border-t border-slate-100 text-center text-sm">
            <span className="text-slate-500 font-medium">Don't have an account yet? </span>
            <Link to="/register" className="font-bold text-emerald-700 hover:text-emerald-600 transition-colors">
              Create an Account
            </Link>
          </div>
        </div>
      </div>

      {/* Instant Password Reset Modal */}
      {showResetModal && (
        <div className="fixed inset-0 z-50 flex items-center justify-center bg-slate-900/50 backdrop-blur-sm p-4">
          <div className="bg-white rounded-2xl p-6 max-w-sm w-full shadow-xl border border-slate-200">
            <div className="flex items-center justify-between mb-4">
              <div className="flex items-center gap-2">
                <div className="w-8 h-8 rounded-lg bg-emerald-100 flex items-center justify-center text-emerald-700">
                  <KeyRound className="w-4 h-4" />
                </div>
                <h3 className="font-bold text-slate-800 text-base">Reset Password</h3>
              </div>
              <button
                onClick={() => setShowResetModal(false)}
                className="text-slate-400 hover:text-slate-600 p-1 rounded-lg"
              >
                <X className="w-5 h-5" />
              </button>
            </div>

            {resetMsg.text && (
              <div className={`mb-4 p-3 rounded-lg text-xs font-semibold flex items-center gap-2 ${
                resetMsg.type === 'success' ? 'bg-emerald-50 text-emerald-700 border border-emerald-200' : 'bg-rose-50 text-rose-700 border border-rose-200'
              }`}>
                {resetMsg.type === 'success' ? <CheckCircle2 className="w-4 h-4 shrink-0" /> : <AlertCircle className="w-4 h-4 shrink-0" />}
                <span>{resetMsg.text}</span>
              </div>
            )}

            <form onSubmit={handlePasswordReset} className="space-y-4">
              <div>
                <label className="block text-xs font-bold text-slate-600 mb-1">Username or Email</label>
                <input
                  type="text"
                  required
                  value={resetIdentifier}
                  onChange={e => setResetIdentifier(e.target.value)}
                  placeholder="Enter your username or email"
                  className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
                />
              </div>

              <div>
                <label className="block text-xs font-bold text-slate-600 mb-1">New Password</label>
                <input
                  type="text"
                  required
                  value={resetNewPassword}
                  onChange={e => setResetNewPassword(e.target.value)}
                  placeholder="e.g. 123 or new password"
                  className="w-full px-3 py-2 border border-slate-300 rounded-lg text-sm focus:outline-none focus:ring-2 focus:ring-emerald-500"
                />
              </div>

              <div className="flex gap-2 pt-2">
                <button
                  type="button"
                  onClick={() => setShowResetModal(false)}
                  className="flex-1 py-2 px-3 border border-slate-300 text-slate-700 rounded-lg text-xs font-bold hover:bg-slate-50"
                >
                  Cancel
                </button>
                <button
                  type="submit"
                  disabled={resetLoading}
                  className="flex-1 py-2 px-3 bg-emerald-700 text-white rounded-lg text-xs font-bold hover:bg-emerald-800 disabled:opacity-50"
                >
                  {resetLoading ? 'Updating...' : 'Set Password'}
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
