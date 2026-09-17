import React, { createContext, useContext, useState, useEffect } from 'react';

const SensoryContext = createContext();

export const SENSORY_MODES = {
  normal: { id: 'normal', name: 'Normal Mode', icon: '✨', desc: 'Standard personalized world' },
  calm: { id: 'calm', name: 'Calm Mode', icon: '🌿', desc: 'Muted colors, low motion, spacious layout' },
  focus: { id: 'focus', name: 'Focus Mode', icon: '🎯', desc: 'Dimmed background, highlighted task card' },
  high_contrast: { id: 'high_contrast', name: 'High Contrast', icon: '👁️', desc: 'Crisp outlines, high legibility' },
  audio: { id: 'audio', name: 'Audio Read-Aloud', icon: '🔊', desc: 'Automatic Web Speech narration' },
  minimal: { id: 'minimal', name: 'Minimal Mode', icon: '📄', desc: 'Distraction-free simple interface' }
};

export const SensoryProvider = ({ children }) => {
  const [activeSensoryMode, setActiveSensoryMode] = useState('normal');
  const [isManualOverride, setIsManualOverride] = useState(false);
  const [currentLearnerState, setCurrentLearnerState] = useState('FOCUSED');
  const [encouragementMessage, setEncouragementMessage] = useState('You are doing great!');

  // Apply Sensory Mode CSS class to top-level app wrapper
  useEffect(() => {
    const root = document.documentElement;
    
    // Remove previous sensory classes
    Object.keys(SENSORY_MODES).forEach(mode => {
      root.classList.remove(`sensory-mode-${mode}`);
    });

    root.classList.add(`sensory-mode-${activeSensoryMode}`);
  }, [activeSensoryMode]);

  // AI-recommended sensory adaptation update
  const applyStateAdaptation = (adaptationData, stateData) => {
    if (stateData?.state_name) {
      setCurrentLearnerState(stateData.state_name);
    }
    if (adaptationData?.encouragementMessage) {
      setEncouragementMessage(adaptationData.encouragementMessage);
    }

    // Only apply AI recommended mode if learner/caregiver hasn't manually overridden it
    if (!isManualOverride && adaptationData?.uiMode) {
      const recMode = adaptationData.uiMode.toLowerCase();
      if (SENSORY_MODES[recMode]) {
        setActiveSensoryMode(recMode);
      }
    }
  };

  const setManualSensoryMode = (modeId) => {
    if (SENSORY_MODES[modeId]) {
      setActiveSensoryMode(modeId);
      setIsManualOverride(true);
    }
  };

  const resetManualOverride = () => {
    setIsManualOverride(false);
  };

  return (
    <SensoryContext.Provider
      value={{
        activeSensoryMode,
        isManualOverride,
        currentLearnerState,
        encouragementMessage,
        setManualSensoryMode,
        resetManualOverride,
        applyStateAdaptation,
        SENSORY_MODES
      }}
    >
      <div className={`sensory-wrapper sensory-mode-${activeSensoryMode}`}>
        {children}
      </div>
    </SensoryContext.Provider>
  );
};

export const useSensory = () => useContext(SensoryContext);
