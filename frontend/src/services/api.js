import axios from 'axios';

const API_BASE_URL = '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Interceptor to add JWT Auth token - checks both key names for compatibility
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('neuroquest_token') || localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => Promise.reject(error)
);

// Auth Endpoints - backend routes are /auth/register and /auth/token and /auth/me
export const registerUser = (userData) => api.post('/auth/register', userData);
export const loginUser = (credentials) => api.post('/auth/token', { username: credentials.email || credentials.username, password: credentials.password });
export const getCurrentUser = () => api.get('/auth/me');

// Medical Onboarding & Data Collection (ICMR Questions)
export const getMedicalQuestions = (learnerId) => api.get(`/medical/questions/${learnerId}`);
export const submitMedicalProfile = (data) => api.post('/medical/submit', data);

// Onboarding Questionnaire & Profile Engine
export const getQuestionnaireSchema = () => api.get('/onboarding/schema');
export const getQuestionnaireDraft = () => api.get('/onboarding/draft');
export const saveQuestionnaireDraft = (draftData) => api.post('/onboarding/draft', draftData);
export const getInitialSupportProfile = () => api.get('/onboarding/profile');
export const submitQuestionnaire = (answers) => api.post('/onboarding/questionnaire', answers);

// Learner Preferences & Theme Engine
export const getLearnerProfile = () => api.get('/learner/profile');
export const updateLearnerPreferences = (prefs) => api.put('/learner/preferences', prefs);

// Tasks & Sessions
export const getTasks = (subject, difficulty, grade) => {
  const params = {};
  if (subject) params.subject = subject;
  if (difficulty) params.difficulty = difficulty;
  if (grade) params.grade = grade;
  return api.get('/tasks', { params });
};
export const getTaskById = (taskId) => api.get(`/tasks/${taskId}`);
export const getNCERTSyllabus = (grade, subject) => {
  const params = {};
  if (grade) params.grade = grade;
  if (subject) params.subject = subject;
  return api.get('/tasks/syllabus', { params });
};
export const getNCERTStandards = () => api.get('/tasks/standards');

export const startSession = () => api.post('/session/start');
export const submitAnswer = (sessionId, data) => api.post(`/session/${sessionId}/answer`, data);
export const endSession = (sessionId) => api.post(`/session/${sessionId}/end`);

// Phase 2 Telemetry ML & Session Adaptation
export const evaluateTelemetry = (payload) => api.post('/telemetry/evaluate', payload);

// Phase 2 Caregiver Insights Dashboard
export const getCaregiverInsights = () => api.get('/caregiver/insights');

// Progress & Rewards
export const getProgressSummary = () => api.get('/progress/summary');

// AI Assist Explanation / Hint / Scaffolding
export const getAIExplanation = (data) => api.post('/ai/explain', data);
export const generatePersonalizedTask = (data) => api.post('/ai/personalized-task', data);
export const getAIHint = (data) => api.post('/ai/hint', data);
export const getAIScaffold = (data) => api.post('/ai/scaffold', data);
export const getDailyWelcomeMission = () => api.get('/ai/daily-welcome');

// Personal Game World & Non-Competitive Mastery Tree
export const getPersonalGameWorld = () => api.get('/game-world');
export const getPersonalMasteryTree = () => api.get('/game-world/mastery-tree');

// Hackathon Demo Simulation & Profile Switching
export const getDemoProfiles = () => api.get('/demo/profiles');
export const activateDemoProfile = (learnerId) => api.post('/demo/activate-profile', { learner_id: learnerId });
export const simulateState = (stateName) => api.post('/demo/simulate-state', { simulated_state: stateName });
export const getAdaptationExplanation = () => api.get('/demo/adaptation-explanation');

// Student Management & Baseline Screening Flow (Caretaker -> Student Experience)
export const getStudents = () => api.get('/students');
export const getStudent = (studentId) => api.get(`/students/${studentId}`);
export const createStudent = (studentData) => api.post('/students', studentData);
export const getStudentQuestionnaire = (studentId) => api.get(`/students/${studentId}/questionnaire`);
export const saveStudentQuestionnaireDraft = (studentId, draftData) => api.post(`/students/${studentId}/questionnaire/draft`, draftData);
export const completeStudentQuestionnaire = (studentId, submissionData) => api.post(`/students/${studentId}/questionnaire/complete`, submissionData);
export const getStudentBaselineProfile = (studentId) => api.get(`/students/${studentId}/baseline-profile`);

export default api;

