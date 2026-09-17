// WebGazer.js local browser gaze tracking service with non-camera fallback

let isGazerInitialized = false;
let isGazerActive = false;
let lastGazeCoords = { x: 0, y: 0 };
let gazeDriftSamples = [];
let offscreenCount = 0;
let totalGazeSamples = 0;

export const initWebGazer = async (onGazeUpdate) => {
  if (isGazerInitialized) {
    if (window.webgazer) {
      try {
        await window.webgazer.resume();
        isGazerActive = true;
      } catch (e) {
        console.warn('WebGazer resume warning:', e);
      }
    }
    return true;
  }

  // Load WebGazer.js script dynamically if not loaded
  return new Promise((resolve) => {
    if (window.webgazer) {
      setupGazerListener(onGazeUpdate);
      resolve(true);
      return;
    }

    const script = document.createElement('script');
    script.src = 'https://webgazer.cs.brown.edu/webgazer.js';
    script.async = true;
    script.onload = () => {
      setupGazerListener(onGazeUpdate);
      resolve(true);
    };
    script.onerror = () => {
      console.warn('WebGazer.js script failed to load. Falling back to non-camera telemetry.');
      isGazerActive = false;
      resolve(false);
    };
    document.head.appendChild(script);
  });
};

const setupGazerListener = (onGazeUpdate) => {
  if (!window.webgazer) return;

  try {
    window.webgazer
      .setRegression('ridge')
      .setTracker('TBM')
      .setGazeListener((data) => {
        if (!data) return;
        
        totalGazeSamples += 1;
        const x = data.x;
        const y = data.y;

        // Check if looking away/offscreen
        const isOffscreen = x < 0 || y < 0 || x > window.innerWidth || y > window.innerHeight;
        if (isOffscreen) {
          offscreenCount += 1;
        }

        // Calculate gaze drift (distance from center of screen)
        const centerX = window.innerWidth / 2;
        const centerY = window.innerHeight / 2;
        const dist = Math.sqrt(Math.pow(x - centerX, 2) + Math.pow(y - centerY, 2));
        gazeDriftSamples.push(dist);

        lastGazeCoords = { x, y };

        if (onGazeUpdate) {
          onGazeUpdate({ x, y, isOffscreen, dist });
        }
      })
      .saveDataAcrossSessions(false)
      .begin();

    // Hide default WebGazer video feedback box to preserve learner calm & privacy
    window.webgazer.showVideoPreview(false).showPredictionPoints(false);
    isGazerInitialized = true;
    isGazerActive = true;
  } catch (err) {
    console.warn('Failed to configure WebGazer:', err);
    isGazerActive = false;
  }
};

export const stopWebGazer = () => {
  if (window.webgazer && isGazerActive) {
    try {
      window.webgazer.pause();
      isGazerActive = false;
    } catch (e) {
      console.warn('WebGazer pause error:', e);
    }
  }
};

export const getGazeTelemetryMetrics = () => {
  if (!isGazerActive || totalGazeSamples === 0) {
    return {
      has_gaze: false,
      gaze_drift_std: 15.0,
      gaze_offscreen_ratio: 0.0
    };
  }

  const meanDrift = gazeDriftSamples.reduce((a, b) => a + b, 0) / (gazeDriftSamples.length || 1);
  const variance = gazeDriftSamples.reduce((a, b) => a + Math.pow(b - meanDrift, 2), 0) / (gazeDriftSamples.length || 1);
  const stdDrift = Math.sqrt(variance);
  const offscreenRatio = offscreenCount / (totalGazeSamples || 1);

  // Reset sample buffer for next telemetry window
  gazeDriftSamples = [];
  offscreenCount = 0;
  totalGazeSamples = 0;

  return {
    has_gaze: true,
    gaze_drift_std: Math.round(stdDrift * 100) / 100,
    gaze_offscreen_ratio: Math.round(offscreenRatio * 1000) / 1000
  };
};
