import React, { createContext, useContext, useState, useEffect } from 'react';

const AuthContext = createContext();

const API = 'http://localhost:8000';

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    checkAuthStatus();
  }, []);

  const getToken = () => localStorage.getItem('neuroquest_token') || localStorage.getItem('token');

  const checkAuthStatus = async () => {
    const token = getToken();
    if (!token) {
      setLoading(false);
      return;
    }
    try {
      const res = await fetch(`${API}/auth/whoami`, {
        headers: { Authorization: `Bearer ${token}` }
      });
      if (res.ok) {
        const data = await res.json();
        setUser(data);
      } else {
        // Token invalid, clear it
        localStorage.removeItem('neuroquest_token');
        localStorage.removeItem('token');
        setUser(null);
      }
    } catch (err) {
      console.error('Auth check failed:', err);
      setUser(null);
    } finally {
      setLoading(false);
    }
  };

  const login = async (username, password) => {
    const res = await fetch(`${API}/auth/token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username, password })
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || 'Login failed');
    }
    const data = await res.json();
    localStorage.setItem('neuroquest_token', data.access_token);
    await checkAuthStatus();
    return data;
  };

  const register = async (userData) => {
    const res = await fetch(`${API}/auth/register`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(userData)
    });
    if (!res.ok) {
      const err = await res.json();
      throw new Error(err.detail || 'Registration failed');
    }
    const data = await res.json();
    localStorage.setItem('neuroquest_token', data.access_token);
    await checkAuthStatus();
    return data;
  };

  const logout = () => {
    localStorage.removeItem('neuroquest_token');
    localStorage.removeItem('token');
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        loading,
        hasCompletedOnboarding: true, // Skip onboarding gate for prototype
        hasCompletedMedical: true,
        login,
        register,
        logout,
        completeOnboarding: () => {},
        completeMedicalOnboarding: () => {},
        refreshUser: checkAuthStatus
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => useContext(AuthContext);
