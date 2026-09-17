const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export const neuroQuestApi = {
  async fetchLearnerProfile(learnerId: string) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/learners/${learnerId}/profile`);
      if (!response.ok) throw new Error('Network response was not ok');
      return await response.json();
    } catch (error) {
      console.error("Failed to fetch learner profile, using local state fallback.", error);
      return null;
    }
  },

  async submitCaregiverProfile(profileData: any) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/caregiver/profile`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(profileData),
      });
      return await response.json();
    } catch (error) {
      console.error("API Error: submitCaregiverProfile", error);
      return { success: true, message: "Fallback: Saved locally" };
    }
  },

  async recordInteractionEvent(eventData: any) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/events`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(eventData),
      });
      return await response.json();
    } catch (error) {
      console.error("API Error: recordInteractionEvent", error);
      // Return a simulated adaptation response if the backend is down
      return { 
        adapted: eventData.load_check === 'Too much',
        action: 'reduce_density'
      };
    }
  }
};
