import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { ShieldCheck, Eye, EyeOff, AlertCircle, ArrowRight, UserCheck } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

export default function RegisterPage() {
  const navigate = useNavigate();
  const { refreshUser } = useAuth();
  const [formData, setFormData] = useState({
    full_name: '',
    username: '',
    email: '',
    password: ''
  });
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  // Smart input syncing: if user enters an email in the username field, auto-populate email
  const handleUsernameChange = (val) => {
    const trimmed = val.trim();
    setFormData(prev => {
      const updated = { ...prev, username: val };
      if (trimmed.includes('@') && !prev.email) {
        updated.email = trimmed;
      }
      return updated;
    });
  };

  const handleEmailChange = (val) => {
    const trimmed = val.trim();
    setFormData(prev => {
      const updated = { ...prev, email: val };
      if (!prev.username && trimmed.includes('@')) {
        updated.username = trimmed.split('@')[0];
      }
      return updated;
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    // Normalize inputs
    let normalizedUsername = formData.username.trim();
    let normalizedEmail = formData.email.trim();

    if (!normalizedEmail && normalizedUsername.includes('@')) {
      normalizedEmail = normalizedUsername;
      normalizedUsername = normalizedUsername.split('@')[0];
    } else if (!normalizedUsername && normalizedEmail) {
      normalizedUsername = normalizedEmail.split('@')[0];
    } else if (!normalizedEmail) {
      normalizedEmail = `${normalizedUsername.toLowerCase()}@neuroquest.local`;
    }

    const payload = {
      username: normalizedUsername,
      email: normalizedEmail,
      password: formData.password,
      full_name: formData.full_name.trim() || normalizedUsername,
      role: 'CAREGIVER'
    };

    try {
      let res;
      try {
        res = await fetch('/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      } catch (err) {
        res = await fetch('http://localhost:8000/auth/register', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(payload)
        });
      }
      
      const data = await res.json();
      
      if (!res.ok) {
        const errorMsg = data.detail || 'Registration failed';
        throw new Error(errorMsg);
      }

      // Store token under both keys for cross-compatibility
      localStorage.setItem('neuroquest_token', data.access_token);
      localStorage.setItem('token', data.access_token);
      
      if (refreshUser) {
        await refreshUser();
      }

      // Navigate directly to student registration to set up learner!
      navigate('/student-registration');
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  const isAlreadyRegistered = error && (error.toLowerCase().includes('already registered') || error.toLowerCase().includes('already exists'));

  return (
    <div className="min-h-screen bg-slate-50 flex flex-col justify-center py-12 sm:px-6 lg:px-8 font-sans">
      <div className="sm:mx-auto sm:w-full sm:max-w-md">
        <div className="flex justify-center mb-4">
          <div className="w-14 h-14 rounded-2xl bg-emerald-100 flex items-center justify-center border border-emerald-200">
            <ShieldCheck className="w-8 h-8 text-emerald-700" />
          </div>
        </div>
        <h2 className="text-center text-3xl font-extrabold text-slate-900 tracking-tight">
          Join NeuroQuest
        </h2>
        <p className="mt-2 text-center text-sm text-slate-600 font-medium">
          The adaptive learning environment designed for how you learn.
        </p>
      </div>

      <div className="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
        <div className="bg-white py-8 px-4 shadow sm:rounded-xl sm:px-10 border border-slate-200">
          {error && (
            <div className="mb-5 bg-rose-50 border border-rose-200 text-rose-700 px-4 py-3 rounded-lg flex flex-col gap-2">
              <div className="flex items-start gap-2.5">
                <AlertCircle className="w-5 h-5 shrink-0 mt-0.5 text-rose-600" />
                <p className="text-sm font-medium">{error}</p>
              </div>
              {isAlreadyRegistered && (
                <Link
                  to="/login"
                  className="mt-1 inline-flex items-center gap-1.5 text-xs font-bold text-emerald-800 bg-emerald-100 hover:bg-emerald-200 px-3 py-1.5 rounded-md transition-colors self-start"
                >
                  <UserCheck className="w-4 h-4" />
                  <span>Sign In to Existing Account &rarr;</span>
                </Link>
              )}
            </div>
          )}
          
          <form className="space-y-5" onSubmit={handleSubmit}>
            <div>
              <label className="block text-sm font-bold text-slate-700 mb-1">
                Full Name <span className="text-xs font-normal text-slate-500">(Caregiver / Parent)</span>
              </label>
              <input
                type="text"
                value={formData.full_name}
                placeholder="e.g. Jeevananth"
                className="appearance-none block w-full px-3.5 py-2.5 border border-slate-300 rounded-lg shadow-sm placeholder-slate-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm font-medium transition-colors"
                onChange={e => setFormData({...formData, full_name: e.target.value})}
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-700 mb-1">
                Username or Email
              </label>
              <input
                type="text"
                required
                value={formData.username}
                placeholder="e.g. jeevananth or user@example.com"
                className="appearance-none block w-full px-3.5 py-2.5 border border-slate-300 rounded-lg shadow-sm placeholder-slate-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm font-medium transition-colors"
                onChange={e => handleUsernameChange(e.target.value)}
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-700 mb-1">
                Email Address <span className="text-xs font-normal text-slate-500">(Optional if username is an email)</span>
              </label>
              <input
                type="email"
                value={formData.email}
                placeholder="your.email@example.com"
                className="appearance-none block w-full px-3.5 py-2.5 border border-slate-300 rounded-lg shadow-sm placeholder-slate-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm font-medium transition-colors"
                onChange={e => handleEmailChange(e.target.value)}
              />
            </div>

            <div>
              <label className="block text-sm font-bold text-slate-700 mb-1">Password</label>
              <div className="relative">
                <input
                  type={showPassword ? 'text' : 'password'}
                  required
                  value={formData.password}
                  placeholder="Enter a secure password"
                  className="appearance-none block w-full px-3.5 py-2.5 pr-11 border border-slate-300 rounded-lg shadow-sm placeholder-slate-400 focus:outline-none focus:ring-emerald-500 focus:border-emerald-500 sm:text-sm font-medium transition-colors"
                  onChange={e => setFormData({...formData, password: e.target.value})}
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

            <div className="pt-2">
              <button
                type="submit"
                disabled={loading}
                className="w-full flex justify-center items-center gap-2 py-3 px-4 border border-transparent rounded-lg shadow-sm text-sm font-bold text-white bg-slate-800 hover:bg-slate-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-slate-800 disabled:opacity-50 transition-colors"
              >
                {loading ? 'Creating Caregiver Account...' : (
                  <>
                    <span>Continue to Student Registration</span>
                    <ArrowRight className="w-4 h-4" />
                  </>
                )}
              </button>
            </div>
          </form>
          
          <div className="mt-8 pt-6 border-t border-slate-100 text-center text-sm">
            <span className="text-slate-500 font-medium">Already have an account? </span>
            <Link to="/login" className="font-bold text-emerald-700 hover:text-emerald-600 transition-colors">
              Sign In
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
}
